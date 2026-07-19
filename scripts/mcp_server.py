#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "mcp>=1.2.0",
#   "numpy>=1.26",
#   "requests>=2.32.0",
#   "python-dotenv>=1.0.1",
# ]
# ///
"""MCP server over the transcript corpus.

Exposes the hybrid search built by scripts/corpus.py so an agent can query 186
videos of transcripts directly, getting back deep links to the exact moment in
each video rather than a filename.

Register with Claude Code:
  claude mcp add youtube-corpus -- uv run /abs/path/to/scripts/mcp_server.py

Requires data/corpus.db (`make corpus && make embed`). Semantic search needs
LLM_API_KEY to encode the query; without it the server still runs and silently
uses keyword search only.

Note: stdio transport — nothing may be written to stdout except protocol
frames, so this module must never print.
"""
from __future__ import annotations

import importlib.util
import os
import sqlite3
import sys
from pathlib import Path
from typing import Any

import numpy as np

# The SDK renamed FastMCP -> MCPServer; accept either so this works on both.
try:
    from mcp.server.mcpserver import MCPServer as _Server
except ModuleNotFoundError:
    from mcp.server.fastmcp import FastMCP as _Server

ROOT = Path(__file__).resolve().parent.parent

# Reuse the chunking/search logic rather than duplicating it. corpus.py is a
# PEP 723 script, not an installed module, so it is loaded by path. Its
# module-level code is only constants plus load_dotenv(); main() is guarded.
_spec = importlib.util.spec_from_file_location("corpus", ROOT / "scripts" / "corpus.py")
corpus = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(corpus)

mcp = _Server("youtube-corpus")

MAX_LIMIT = 25
SNIPPET_CHARS = 600


def _require_db() -> sqlite3.Connection:
    if not corpus.CORPUS_DB.exists():
        raise FileNotFoundError(
            f"{corpus.CORPUS_DB} not found — run `make corpus && make embed` first"
        )
    return corpus.connect()


def _row_to_hit(row: sqlite3.Row, score: float | None = None) -> dict[str, Any]:
    hit = {
        "video_id": row["video_id"],
        "title": row["title"],
        "channel": row["channel"],
        "published": (row["published"] or "")[:10],
        "timestamp": f"{row['start_s'] // 60:02d}:{row['start_s'] % 60:02d}",
        # The point of the whole corpus: a citation you can actually follow.
        "url": f"{row['url']}&t={row['start_s']}s",
        "text": row["text"],
    }
    if score is not None:
        hit["score"] = round(score, 5)
    return hit


def _fetch(con: sqlite3.Connection, chunk_id: int) -> sqlite3.Row:
    return con.execute(
        "SELECT c.*, v.title, v.channel, v.url, v.published FROM chunks c"
        " JOIN videos v ON v.video_id = c.video_id WHERE c.id = ?",
        (chunk_id,),
    ).fetchone()


@mcp.tool()
def search_transcripts(
    query: str,
    limit: int = 8,
    channel: str | None = None,
    mode: str = "hybrid",
) -> dict[str, Any]:
    """Search 186 videos of YouTube transcripts about AI engineering.

    Returns passages with deep links to the exact moment in each video.

    Args:
        query: What to look for. Natural-language questions work well in hybrid
            or semantic mode; use bm25 for exact strings like a model name.
        limit: Number of passages to return (max 25).
        channel: Optional channel-slug filter, e.g. "anthropic", "langchain",
            "ai-engineer". Call list_channels for the full set.
        mode: "hybrid" (default, fuses both), "bm25" (keyword/BM25 only), or
            "semantic" (embeddings only). Hybrid is almost always best —
            the two halves overlap by only 0-2 of their top 10 on paraphrased
            queries, so each finds passages the other misses.
    """
    if mode not in ("hybrid", "bm25", "semantic"):
        raise ValueError(f"mode must be hybrid, bm25 or semantic (got {mode!r})")
    limit = max(1, min(limit, MAX_LIMIT))

    con = _require_db()
    try:
        where, params = "", []
        if channel:
            where, params = " AND v.channel_slug LIKE ?", [f"%{channel}%"]

        pool = max(limit * 10, 100)
        rankings: list[list[int]] = []
        notes: list[str] = []

        if mode in ("hybrid", "bm25"):
            rankings.append(corpus.bm25_ranking(con, query, where, params, pool))

        if mode in ("hybrid", "semantic"):
            if not os.environ.get("LLM_API_KEY"):
                if mode == "semantic":
                    raise RuntimeError("semantic search needs LLM_API_KEY to encode the query")
                notes.append("no LLM_API_KEY — keyword search only")
            else:
                mat, ids = corpus.load_matrix(con)
                if len(ids) == 0:
                    if mode == "semantic":
                        raise RuntimeError("no embeddings yet — run `make embed`")
                    notes.append("no embeddings yet — keyword search only")
                else:
                    try:
                        qv = corpus.embed_texts([query], "query")[0]
                    except SystemExit as e:  # corpus.py exits on API failure
                        raise RuntimeError(f"query embedding failed: {e}") from None
                    qv = qv / (np.linalg.norm(qv) + 1e-9)
                    order = np.argsort(-(mat @ qv))[:pool]
                    ranked = [ids[i] for i in order]
                    if channel:
                        allowed = {
                            r["id"]
                            for r in con.execute(
                                "SELECT c.id FROM chunks c JOIN videos v ON v.video_id = c.video_id"
                                " WHERE v.channel_slug LIKE ?",
                                params,
                            )
                        }
                        ranked = [c for c in ranked if c in allowed]
                    rankings.append(ranked)

        rankings = [r for r in rankings if r]
        if not rankings:
            return {"query": query, "count": 0, "results": [], "notes": notes}

        fused = corpus.rrf(rankings)
        top = sorted(fused.items(), key=lambda kv: -kv[1])[:limit]
        results = [_row_to_hit(_fetch(con, cid), score) for cid, score in top]
        out = {"query": query, "mode": mode, "count": len(results), "results": results}
        if notes:
            out["notes"] = notes
        return out
    finally:
        con.close()


@mcp.tool()
def get_transcript_window(video_id: str, at_seconds: int, window: int = 2) -> dict[str, Any]:
    """Read the transcript around a moment in a video, to get context for a hit.

    Args:
        video_id: YouTube video id, as returned by search_transcripts.
        at_seconds: Position in the video, in seconds.
        window: How many ~75s chunks to include on each side (max 10).
    """
    window = max(0, min(window, 10))
    con = _require_db()
    try:
        meta = con.execute("SELECT * FROM videos WHERE video_id = ?", (video_id,)).fetchone()
        if meta is None:
            raise ValueError(f"unknown video_id {video_id!r}")

        anchor = con.execute(
            "SELECT id FROM chunks WHERE video_id = ?"
            " ORDER BY ABS(start_s - ?) LIMIT 1",
            (video_id, at_seconds),
        ).fetchone()
        if anchor is None:
            raise ValueError(f"no transcript chunks for {video_id!r}")

        rows = con.execute(
            "SELECT * FROM chunks WHERE video_id = ? AND id BETWEEN ? AND ? ORDER BY start_s",
            (video_id, anchor["id"] - window, anchor["id"] + window),
        ).fetchall()

        return {
            "video_id": video_id,
            "title": meta["title"],
            "channel": meta["channel"],
            "url": f"{meta['url']}&t={at_seconds}s",
            "passages": [
                {
                    "timestamp": f"{r['start_s'] // 60:02d}:{r['start_s'] % 60:02d}",
                    "start_s": r["start_s"],
                    "text": r["text"],
                }
                for r in rows
            ],
        }
    finally:
        con.close()


@mcp.tool()
def list_channels() -> dict[str, Any]:
    """List the channels in the corpus with their slugs and coverage.

    Use the returned slug values to filter search_transcripts by channel.
    """
    con = _require_db()
    try:
        rows = con.execute(
            "SELECT v.channel, v.channel_slug, COUNT(DISTINCT v.video_id) videos,"
            " COUNT(c.id) chunks FROM videos v JOIN chunks c ON c.video_id = v.video_id"
            " GROUP BY v.channel_slug ORDER BY chunks DESC"
        ).fetchall()
        total = con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        embedded = con.execute(
            "SELECT COUNT(*) FROM chunks WHERE embedding IS NOT NULL"
        ).fetchone()[0]
        return {
            "channels": [
                {
                    "name": r["channel"],
                    "slug": r["channel_slug"],
                    "videos": r["videos"],
                    "chunks": r["chunks"],
                }
                for r in rows
            ],
            "total_chunks": total,
            "embedded_chunks": embedded,
            "semantic_available": embedded > 0 and bool(os.environ.get("LLM_API_KEY")),
        }
    finally:
        con.close()


if __name__ == "__main__":
    mcp.run()
