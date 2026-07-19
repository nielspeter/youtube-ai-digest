# YouTube AI Transcriptions

Cron-based pipeline that watches YouTube channels and, whenever a new video
appears, extracts its transcript, generates an extensive summary with an LLM,
and publishes it as a searchable static site.

**Stack:** GitHub Actions (cron) → RSS feed diff → `yt-dlp` transcript →
LLM summary (NVIDIA NIM, free & OpenAI-compatible) → Markdown → VitePress →
GitHub Pages. Runs identically on your machine and in CI. Cost: **$0**.

## How it works

1. `subscriptions.yml` lists channels (handles, URLs, or raw IDs).
2. Each channel's free RSS feed (`.../feeds/videos.xml?channel_id=UC...`) is
   polled — no API key, rarely blocked.
3. New videos are diffed against `data/processed.json`.
4. `yt-dlp` pulls the transcript; it's cleaned to readable text with `[mm:ss]` marks
   and cached in `data/transcripts/` (so you can re-summarize later without re-fetching).
5. The transcript is summarized by an OpenAI-compatible endpoint.
6. A Markdown file lands in `docs/summaries/<channel>/<video-id>.md`.
7. VitePress builds `docs/` into a site with local full-text search.

## Local setup

No Python virtualenv to manage. Dependencies are declared inline in
`scripts/digest.py` (PEP 723) and [`uv`](https://docs.astral.sh/uv/) builds a
cached environment on demand — it even fetches the right Python if you don't
have one. Install `uv` once:

```bash
brew install uv            # or: curl -LsSf https://astral.sh/uv/install.sh | sh
```

You also need Node 18+ (for the site) and the `yt-dlp` binary is pulled in as a
Python dependency automatically — nothing else to install.

```bash
cp .env.example .env        # add your free LLM_API_KEY from build.nvidia.com
make install                # just `npm install` for the site; Python env is on-demand
make resolve                # resolve channel handles -> IDs (cached in data/channels.json)
make seed                   # OPTIONAL: mark existing videos as seen, so you only get NEW ones
make run                    # fetch + summarize new videos  (== uv run scripts/digest.py)
make dev                    # live-preview the site at http://localhost:5173
```

The script is also directly executable (`./scripts/digest.py`) thanks to the
`uv run` shebang — no `python`, no `pip`, no `activate`, ever.

Skip `make seed` if you *want* summaries of the most recent existing videos
(capped by `MAX_VIDEOS_PER_RUN`, default 25).

### Commands

| Command | What it does |
|---|---|
| `make run` | Process new videos |
| `make seed` | Mark current feed items seen, no summaries |
| `make resolve` | Resolve + cache channel IDs |
| `make dry` | Full run without writing state |
| `python scripts/digest.py --limit 3` | Cap videos this run |
| `make dev` / `make build` | Preview / build the site |

## Searching the corpus

The site's built-in search covers the *summaries*. To query the transcripts
themselves — from the terminal, or from an agent — build the local index:

```bash
make corpus     # chunk transcripts into data/corpus.db  (seconds)
make embed      # add vectors via the embeddings endpoint (incremental)
make search Q="how should agents handle memory"
```

Transcripts are chunked into ~75s windows on their `[mm:ss]` marks, so every hit
resolves to a moment in a video rather than to a filename:

```
The best AI agents need more humans than you think
  LangChain · 2026-07-16 · [37:15] · rrf=0.0164
  https://www.youtube.com/watch?v=HbUznYhKFOc&t=2235s
```

Search is hybrid: SQLite FTS5 (BM25) for exact terms like model names or `MCP`,
plus cosine similarity over embeddings for paraphrase, fused with reciprocal
rank fusion. The two disagree a lot — on paraphrased queries they typically
share only 0–2 of their top 10 — which is the point of running both. Use
`--mode bm25` or `--mode semantic` to isolate one, `--channel <slug>` to filter,
and `--json` for machine-readable output.

`data/corpus.db` is **not** committed: it is derived data, and SQLite's
page-rewriting would add ~9 MB/month of binary churn to git. The transcripts it
is built from *are* committed, so `make corpus && make embed` reconstructs it.
Embedding is incremental — it only fills in chunks whose vectors are missing, so
a routine run costs a handful of API calls.

CI rebuilds the corpus on every digest run (cached between runs, so only new
chunks are embedded) and publishes it with the site, at
`<site-url>/corpus.db` — a SQLite file any script or agent can fetch and query
without cloning the repo.

### Querying it from an agent

`scripts/mcp_server.py` exposes the same search over MCP, so an agent can cite a
moment in a video directly:

```bash
claude mcp add youtube-corpus -- uv run "$PWD/scripts/mcp_server.py"
```

| Tool | Returns |
|---|---|
| `search_transcripts(query, limit, channel, mode)` | Passages with `?t=` deep links |
| `get_transcript_window(video_id, at_seconds, window)` | Neighbouring passages for context |
| `list_channels()` | Channel slugs and coverage |

It reads `data/corpus.db` directly, so build the corpus first. Without
`LLM_API_KEY` the server still runs and falls back to keyword-only search.

Note that this does **not** change search on the website itself, which is still
VitePress's own index over the summaries. Querying transcripts semantically
needs the embedding model on both sides, and a browser has nowhere safe to hold
the API key — so hybrid search lives in the CLI and in anything server-side, not
in the page.

## Choosing the model

Default is `z-ai/glm-5.2` — currently the strongest free open-weights model on
NVIDIA's catalog, with a 1M-token context (long videos need no chunking).
Because the endpoint is OpenAI-compatible, switching providers/models is just
env vars, no code change:

```bash
LLM_BASE_URL=https://integrate.api.nvidia.com/v1
LLM_MODEL=z-ai/glm-5.2          # or deepseek-ai/deepseek-v4-flash, etc.
```

> Copy the exact model ID from the model's **Playground → API** code sample on
> [build.nvidia.com](https://build.nvidia.com/models) if a name ever changes.
> The transcript is cached, so you can re-run against a better model anytime.

## Deploy (GitHub Actions + Pages)

1. Push this repo to GitHub.
2. **Settings → Pages → Source: GitHub Actions.**
3. **Settings → Secrets and variables → Actions:**
   - Secret `LLM_API_KEY` — your NVIDIA key.
   - Variables (optional): `LLM_MODEL`, `LLM_BASE_URL`, `MAX_VIDEOS_PER_RUN`,
     and `SITE_BASE` = `"/<repo-name>/"` for project pages (omit for a custom
     domain / user page).
4. The workflow runs daily at ~03:17 UTC (`workflow_dispatch` to run manually,
   with an optional **seed** toggle for the first run).

### Notes

- The job commits its own `data/` + `docs/summaries/` each run and writes a
  `data/last-run` heartbeat, which keeps the cron schedule from being
  auto-disabled after 60 idle days.
- If YouTube starts blocking the runner IP ("Sign in to confirm you're not a
  bot"), export browser cookies (Netscape format) to a repo secret and point
  `YTDLP_COOKIES` at the file, or run extraction on a self-hosted runner.
- GitHub cron is best-effort; expect a few minutes of drift.
