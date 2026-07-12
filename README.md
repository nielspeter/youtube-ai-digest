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
