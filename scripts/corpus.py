#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy>=1.26",
#   "requests>=2.32.0",
#   "python-dotenv>=1.0.1",
# ]
# ///
"""Searchable corpus over the cached transcripts.

The transcripts in data/transcripts/ carry [mm:ss] marks every ~30s. This turns
them into timestamp-anchored chunks so a hit resolves to a moment in a video
(?t=413s) rather than to a filename, and makes the whole archive queryable from
outside the browser.

  build   transcripts + processed.json -> data/corpus.db (chunks + FTS5)
  embed   fill in missing vectors via the NIM embeddings endpoint (incremental)
  search  hybrid BM25 + cosine, fused with reciprocal rank fusion
  stats   what's in the corpus right now

Run:
  ./scripts/corpus.py build
  ./scripts/corpus.py embed
  ./scripts/corpus.py search "how should agents handle memory" -n 8
  ./scripts/corpus.py search "prompt injection" --mode bm25 --channel anthropic
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from pathlib import Path

import numpy as np
import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # optional; CI sets env directly
    pass

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
PROCESSED_FILE = DATA_DIR / "processed.json"
CORPUS_DB = DATA_DIR / "corpus.db"

# Chunking. Windows are sized in seconds but hard-capped in words: the embedding
# model rejects >512 tokens outright (it does not truncate), and dense speech can
# run ~1.3 tokens/word, so 350 words leaves real headroom.
TARGET_SECONDS = 75
OVERLAP_SECONDS = 15
MAX_WORDS = 350

def env(name: str, default: str | None = None) -> str | None:
    """Treat an empty value as unset. GitHub Actions injects "" for a `vars.X`
    that was never defined, which is not the same as the name being absent —
    os.environ.get(name, default) would hand back the empty string."""
    val = os.environ.get(name)
    return val if val not in (None, "") else default


# Embeddings. nv-embedqa-e5-v5 is asymmetric: passages and queries must be
# encoded with different input_type or retrieval quality drops sharply.
EMBED_MODEL = env("EMBED_MODEL", "nvidia/nv-embedqa-e5-v5")
EMBED_DIM = 1024
EMBED_BATCH = 64  # 128 verified working; 64 keeps individual retries cheap

RRF_K = 60  # reciprocal rank fusion constant; 60 is the standard default


# --------------------------------------------------------------------------- #
# schema
# --------------------------------------------------------------------------- #

SCHEMA = """
CREATE TABLE IF NOT EXISTS videos (
    video_id     TEXT PRIMARY KEY,
    title        TEXT,
    channel      TEXT,
    channel_slug TEXT,
    url          TEXT,
    published    TEXT
);
CREATE TABLE IF NOT EXISTS chunks (
    id        INTEGER PRIMARY KEY,
    video_id  TEXT NOT NULL REFERENCES videos(video_id),
    start_s   INTEGER NOT NULL,
    end_s     INTEGER NOT NULL,
    text      TEXT NOT NULL,
    n_words   INTEGER NOT NULL,
    embedding BLOB
);
CREATE INDEX IF NOT EXISTS chunks_video ON chunks(video_id);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    text, content='chunks', content_rowid='id', tokenize='porter unicode61'
);
"""


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(CORPUS_DB)
    con.row_factory = sqlite3.Row
    return con


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #

MARK_RE = re.compile(r"\[(\d{1,3}):(\d{2})\]")


def parse_marked(raw: str) -> list[tuple[int, str]]:
    """Split a transcript into (start_seconds, text) segments on its [mm:ss] marks."""
    parts = MARK_RE.split(raw)
    # re.split with 2 groups yields: [pre, mm, ss, text, mm, ss, text, ...]
    segments: list[tuple[int, str]] = []
    for i in range(1, len(parts) - 2, 3):
        start = int(parts[i]) * 60 + int(parts[i + 1])
        text = " ".join(parts[i + 2].split())
        if text:
            segments.append((start, text))
    return segments


def chunk_segments(segments: list[tuple[int, str]]) -> list[tuple[int, int, str]]:
    """Group segments into overlapping windows, capped by duration and word count.

    Returns (start_s, end_s, text). The word cap wins over the duration target so
    a fast talker never produces a chunk the embedder will reject.
    """
    chunks: list[tuple[int, int, str]] = []
    i = 0
    while i < len(segments):
        start = segments[i][0]
        words: list[str] = []
        j = i
        while j < len(segments):
            seg_words = segments[j][1].split()
            over_time = segments[j][0] - start >= TARGET_SECONDS
            over_words = len(words) + len(seg_words) > MAX_WORDS
            if words and (over_time or over_words):
                break
            words.extend(seg_words)
            j += 1
        end = segments[j][0] if j < len(segments) else segments[-1][0] + 30
        if words:
            chunks.append((start, end, " ".join(words)))
        if j <= i:  # a single oversized segment; don't stall
            j = i + 1
        # step back for overlap, but always make forward progress
        back = start + TARGET_SECONDS - OVERLAP_SECONDS
        nxt = j
        while nxt > i + 1 and segments[nxt - 1][0] >= back:
            nxt -= 1
        i = max(nxt, i + 1)
    return chunks


def load_video_meta() -> dict[str, dict]:
    if not PROCESSED_FILE.exists():
        return {}
    return json.loads(PROCESSED_FILE.read_text()).get("videos", {})


def cmd_build(args) -> None:
    meta = load_video_meta()
    files = sorted(TRANSCRIPTS_DIR.glob("*.txt"))
    if not files:
        sys.exit(f"no transcripts in {TRANSCRIPTS_DIR}")

    con = connect()
    con.executescript(SCHEMA)

    # Preserve vectors across rebuilds: re-embedding is the only slow part, and
    # identical chunk text always maps to an identical vector.
    cached = {
        (r["video_id"], r["start_s"], r["text"]): r["embedding"]
        for r in con.execute(
            "SELECT video_id, start_s, text, embedding FROM chunks WHERE embedding IS NOT NULL"
        )
    }
    if cached:
        print(f"reusing {len(cached):,} cached vectors")

    con.execute("DELETE FROM chunks_fts")
    con.execute("DELETE FROM chunks")
    con.execute("DELETE FROM videos")

    n_chunks = skipped = 0
    for f in files:
        vid = f.stem
        raw = f.read_text(encoding="utf-8", errors="replace")
        segments = parse_marked(raw)
        if not segments:
            skipped += 1
            continue

        m = meta.get(vid, {})
        con.execute(
            "INSERT OR REPLACE INTO videos VALUES (?,?,?,?,?,?)",
            (
                vid,
                m.get("title", vid),
                m.get("channel", ""),
                m.get("channel_slug", ""),
                m.get("url", f"https://www.youtube.com/watch?v={vid}"),
                m.get("published", ""),
            ),
        )
        for start, end, text in chunk_segments(segments):
            con.execute(
                "INSERT INTO chunks (video_id, start_s, end_s, text, n_words, embedding)"
                " VALUES (?,?,?,?,?,?)",
                (vid, start, end, text, len(text.split()), cached.get((vid, start, text))),
            )
            n_chunks += 1

    con.execute("INSERT INTO chunks_fts(rowid, text) SELECT id, text FROM chunks")
    con.commit()

    over = con.execute("SELECT COUNT(*) FROM chunks WHERE n_words > ?", (MAX_WORDS,)).fetchone()[0]
    kept = con.execute("SELECT COUNT(*) FROM chunks WHERE embedding IS NOT NULL").fetchone()[0]
    con.close()

    print(f"built {CORPUS_DB.relative_to(ROOT)}: {n_chunks:,} chunks from {len(files) - skipped} videos")
    if skipped:
        print(f"  {skipped} transcript(s) had no [mm:ss] marks and were skipped")
    if over:
        print(f"  warning: {over} chunk(s) exceed {MAX_WORDS} words")
    print(f"  {kept:,} vectors carried over, {n_chunks - kept:,} need embedding")


# --------------------------------------------------------------------------- #
# embed
# --------------------------------------------------------------------------- #


def embed_texts(texts: list[str], input_type: str) -> np.ndarray:
    """Call the OpenAI-compatible embeddings endpoint. input_type is NIM-specific
    and required by asymmetric retrieval models ('passage' to index, 'query' to search)."""
    base = env("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1")
    key = env("LLM_API_KEY")
    if not key:
        sys.exit("LLM_API_KEY is not set (see .env.example)")

    for attempt in range(5):
        try:
            r = requests.post(
                f"{base}/embeddings",
                headers={"Authorization": f"Bearer {key}"},
                json={
                    "input": texts,
                    "model": EMBED_MODEL,
                    "input_type": input_type,
                    "encoding_format": "float",
                },
                timeout=120,
            )
            if r.status_code == 200:
                data = sorted(r.json()["data"], key=lambda d: d["index"])
                return np.array([d["embedding"] for d in data], dtype=np.float32)
            if r.status_code in (429, 500, 502, 503, 504):
                wait = 2**attempt + 1
                print(f"    HTTP {r.status_code}, retrying in {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            sys.exit(f"embeddings failed: HTTP {r.status_code} {r.text[:300]}")
        except requests.RequestException as e:
            wait = 2**attempt + 1
            print(f"    {type(e).__name__}, retrying in {wait}s", file=sys.stderr)
            time.sleep(wait)
    sys.exit("embeddings failed after 5 attempts")


def cmd_embed(args) -> None:
    con = connect()
    rows = con.execute(
        "SELECT id, text FROM chunks WHERE embedding IS NULL ORDER BY id"
    ).fetchall()
    if not rows:
        print("all chunks already embedded")
        return

    print(f"embedding {len(rows):,} chunks with {EMBED_MODEL} (batch {EMBED_BATCH})")
    done = 0
    for i in range(0, len(rows), EMBED_BATCH):
        batch = rows[i : i + EMBED_BATCH]
        vecs = embed_texts([r["text"] for r in batch], "passage")
        # Store float16: halves the file for a cosine-similarity cost far below
        # the noise floor of the retrieval itself.
        con.executemany(
            "UPDATE chunks SET embedding = ? WHERE id = ?",
            [(v.astype(np.float16).tobytes(), r["id"]) for v, r in zip(vecs, batch)],
        )
        con.commit()  # commit per batch so an interrupted run resumes cleanly
        done += len(batch)
        print(f"  {done:,}/{len(rows):,}", end="\r", flush=True)
    con.close()
    print(f"\nembedded {done:,} chunks")


def load_matrix(con: sqlite3.Connection) -> tuple[np.ndarray, list[int]]:
    rows = con.execute(
        "SELECT id, embedding FROM chunks WHERE embedding IS NOT NULL ORDER BY id"
    ).fetchall()
    if not rows:
        return np.zeros((0, EMBED_DIM), dtype=np.float32), []
    mat = np.frombuffer(b"".join(r["embedding"] for r in rows), dtype=np.float16)
    mat = mat.reshape(len(rows), EMBED_DIM).astype(np.float32)
    mat /= np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9
    return mat, [r["id"] for r in rows]


# --------------------------------------------------------------------------- #
# search
# --------------------------------------------------------------------------- #


def fts_queries(q: str) -> list[str]:
    """FTS5 queries from strictest to loosest. Words are quoted so punctuation in
    a natural-language query can't be read as operator syntax.

    Strictness matters here: with plain OR, a query like "prompt injection"
    matches anything saying "prompt" — which in this corpus is nearly every
    chunk — and porter stemming happily equates "injection" with "injected
    thoughts". Phrase and AND matches are tried first and only topped up with OR.
    """
    words = re.findall(r"\w+", q)
    if not words:
        return []
    quoted = [f'"{w}"' for w in words]
    queries = []
    if len(words) > 1:
        # One pair of quotes around the whole thing is a phrase. Juxtaposing
        # separately-quoted terms is implicit AND in FTS5, not adjacency.
        queries.append('"{}"'.format(" ".join(words)))
        queries.append(" AND ".join(quoted))
    queries.append(" OR ".join(quoted))
    return queries


def bm25_ranking(con: sqlite3.Connection, query: str, where: str,
                 params: list, pool: int) -> list[int]:
    """Rank by BM25, tightest query first, topping up with looser ones until the
    pool is full. Order is preserved, so exact phrase hits always outrank OR hits."""
    sql = (
        "SELECT c.id FROM chunks_fts f JOIN chunks c ON c.id = f.rowid"
        " JOIN videos v ON v.video_id = c.video_id"
        f" WHERE chunks_fts MATCH ?{where} ORDER BY bm25(chunks_fts) LIMIT ?"
    )
    ranked: list[int] = []
    seen: set[int] = set()
    for q in fts_queries(query):
        try:
            rows = con.execute(sql, [q, *params, pool])
        except sqlite3.OperationalError:  # malformed FTS expression; skip
            continue
        for r in rows:
            if r["id"] not in seen:
                seen.add(r["id"])
                ranked.append(r["id"])
        if len(ranked) >= pool:
            break
    return ranked[:pool]


def rrf(rankings: list[list[int]], k: int = RRF_K) -> dict[int, float]:
    scores: dict[int, float] = {}
    for ranking in rankings:
        for rank, cid in enumerate(ranking):
            scores[cid] = scores.get(cid, 0.0) + 1.0 / (k + rank + 1)
    return scores


def cmd_search(args) -> None:
    if not CORPUS_DB.exists():
        sys.exit("no corpus.db — run `./scripts/corpus.py build` first")
    con = connect()

    where, params = "", []
    if args.channel:
        where = " AND v.channel_slug LIKE ?"
        params = [f"%{args.channel}%"]

    pool = max(args.n * 10, 100)
    rankings: list[list[int]] = []

    if args.mode in ("hybrid", "bm25"):
        rankings.append(bm25_ranking(con, args.query, where, params, pool))

    if args.mode in ("hybrid", "semantic"):
        mat, ids = load_matrix(con)
        if len(ids) == 0:
            if args.mode == "semantic":
                sys.exit("no embeddings — run `./scripts/corpus.py embed` first")
            print("note: no embeddings yet, falling back to bm25 only", file=sys.stderr)
        else:
            qv = embed_texts([args.query], "query")[0]
            qv /= np.linalg.norm(qv) + 1e-9
            sims = mat @ qv
            order = np.argsort(-sims)[:pool]
            allowed = None
            if args.channel:
                allowed = {
                    r["id"]
                    for r in con.execute(
                        "SELECT c.id FROM chunks c JOIN videos v ON v.video_id = c.video_id"
                        " WHERE v.channel_slug LIKE ?",
                        params,
                    )
                }
            ranked = [ids[i] for i in order]
            if allowed is not None:
                ranked = [cid for cid in ranked if cid in allowed]
            rankings.append(ranked)

    if not rankings or not any(rankings):
        print("no matches")
        return

    fused = rrf(rankings)
    top = sorted(fused.items(), key=lambda kv: -kv[1])[: args.n]

    if args.json:
        out = []
        for cid, score in top:
            r = con.execute(
                "SELECT c.*, v.title, v.channel, v.url, v.published FROM chunks c"
                " JOIN videos v ON v.video_id = c.video_id WHERE c.id = ?",
                (cid,),
            ).fetchone()
            out.append(
                {
                    "score": round(score, 5),
                    "video_id": r["video_id"],
                    "title": r["title"],
                    "channel": r["channel"],
                    "published": r["published"][:10],
                    "start_s": r["start_s"],
                    "url": f"{r['url']}&t={r['start_s']}s",
                    "text": r["text"],
                }
            )
        print(json.dumps(out, indent=2))
        return

    for cid, score in top:
        r = con.execute(
            "SELECT c.*, v.title, v.channel, v.url, v.published FROM chunks c"
            " JOIN videos v ON v.video_id = c.video_id WHERE c.id = ?",
            (cid,),
        ).fetchone()
        mm, ss = divmod(r["start_s"], 60)
        print(f"\n\033[1m{r['title']}\033[0m")
        print(f"  {r['channel']} · {r['published'][:10]} · [{mm:02d}:{ss:02d}] · rrf={score:.4f}")
        print(f"  {r['url']}&t={r['start_s']}s")
        text = r["text"]
        print(f"  {text[:280]}{'…' if len(text) > 280 else ''}")
    con.close()


def cmd_stats(args) -> None:
    if not CORPUS_DB.exists():
        sys.exit("no corpus.db — run `./scripts/corpus.py build` first")
    con = connect()
    q = lambda s: con.execute(s).fetchone()[0]  # noqa: E731
    n = q("SELECT COUNT(*) FROM chunks")
    emb = q("SELECT COUNT(*) FROM chunks WHERE embedding IS NOT NULL")
    # The CI embed step is continue-on-error so a flaky endpoint can't block the
    # site deploy — which also means a total failure reports green. Raise an
    # annotation so incomplete coverage is visible without reading the log.
    if emb < n and os.environ.get("GITHUB_ACTIONS"):
        print(f"::warning::{n - emb:,} of {n:,} chunks have no embedding —"
              " semantic search is degraded until the next successful run")
    print(f"videos:     {q('SELECT COUNT(*) FROM videos'):,}")
    print(f"chunks:     {n:,}")
    print(f"embedded:   {emb:,} ({100 * emb / n if n else 0:.0f}%)")
    print(f"words:      {q('SELECT SUM(n_words) FROM chunks'):,}")
    print(f"hours:      {q('SELECT SUM(end_s - start_s) FROM chunks') / 3600:.0f}")
    print(f"db size:    {CORPUS_DB.stat().st_size / 1e6:.1f} MB")
    print("\nby channel:")
    for r in con.execute(
        "SELECT v.channel, COUNT(DISTINCT v.video_id) vids, COUNT(c.id) chunks"
        " FROM videos v JOIN chunks c ON c.video_id = v.video_id"
        " GROUP BY v.channel ORDER BY chunks DESC"
    ):
        print(f"  {r['channel'][:34]:36} {r['vids']:3} videos  {r['chunks']:5} chunks")
    con.close()


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("build", help="chunk transcripts into corpus.db").set_defaults(func=cmd_build)
    sub.add_parser("embed", help="fill in missing vectors").set_defaults(func=cmd_embed)
    sub.add_parser("stats", help="corpus overview").set_defaults(func=cmd_stats)

    s = sub.add_parser("search", help="hybrid search over the corpus")
    s.add_argument("query")
    s.add_argument("-n", type=int, default=8, help="results to return")
    s.add_argument("--mode", choices=["hybrid", "bm25", "semantic"], default="hybrid")
    s.add_argument("--channel", help="filter by channel slug substring")
    s.add_argument("--json", action="store_true", help="machine-readable output")
    s.set_defaults(func=cmd_search)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
