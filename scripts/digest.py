#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "feedparser>=6.0.11",
#   "yt-dlp>=2025.1.1",
#   "openai>=1.60.0",
#   "requests>=2.32.0",
#   "PyYAML>=6.0.2",
#   "python-dotenv>=1.0.1",
# ]
# ///
"""YouTube subscription digest.

Pipeline (works identically locally and in GitHub Actions):
  1. Read subscriptions.yml and resolve handles/URLs to channel IDs.
  2. Pull each channel's RSS feed (free, no API key, rarely blocked).
  3. Diff against data/processed.json to find new videos.
  4. Fetch each transcript with yt-dlp and clean it to plain text.
  5. Summarize with an OpenAI-compatible endpoint (NVIDIA NIM by default).
  6. Write a Markdown summary into docs/summaries/<channel>/<id>.md.
  7. Regenerate docs/index.md and persist state.

Run:
  python scripts/digest.py            # process new videos
  python scripts/digest.py --seed     # mark current feed items as seen, no summaries
  python scripts/digest.py --resolve  # just resolve + cache channel IDs
  python scripts/digest.py --limit 3  # cap videos this run
  python scripts/digest.py --dry-run  # fetch + summarize but don't write state
"""
from __future__ import annotations

import argparse
import glob
import html
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import requests
import yaml
from openai import (APIConnectionError, APITimeoutError, BadRequestError,
                    InternalServerError, OpenAI, RateLimitError)

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # optional; CI sets env directly
    pass

ROOT = Path(__file__).resolve().parent.parent
SUBSCRIPTIONS = ROOT / "subscriptions.yml"
DATA_DIR = ROOT / "data"
PROCESSED_FILE = DATA_DIR / "processed.json"
CHANNELS_FILE = DATA_DIR / "channels.json"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
SUMMARIES_DIR = ROOT / "docs" / "summaries"
INDEX_FILE = ROOT / "docs" / "index.md"

FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
WATCH_URL = "https://www.youtube.com/watch?v={vid}"

MAX_ATTEMPTS = 6  # give up fetching a transcript after this many runs
# Skip videos longer than this in feed runs (marathons/courses blow the token
# budget and don't summarize well). 0 disables the limit. --video ignores it.
MAX_VIDEO_MINUTES = int(os.environ.get("MAX_VIDEO_MINUTES", "90"))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# 429 handling: keep retrying transcript fetches, respecting Retry-After, until
# success or a genuine (non-rate-limit) error. Caps keep a single run bounded.
RATE_LIMIT_MAX_RETRIES = int(os.environ.get("RATE_LIMIT_MAX_RETRIES", "12"))
RATE_LIMIT_MAX_WAIT = 600  # never sleep longer than this per retry


class BotCheckError(Exception):
    """YouTube demanded 'confirm you're not a bot' — an IP-level block, not a
    per-video problem. Retried on future runs (different IP) without burning the
    per-video attempt budget."""


def is_rate_limited(text: str) -> bool:
    t = (text or "").lower()
    return "429" in t or "too many requests" in t


def is_bot_check(text: str) -> bool:
    t = (text or "").lower()
    return "confirm you" in t and "not a bot" in t


def retry_after_seconds(text: str, attempt: int) -> int:
    """Honor a Retry-After value if the error/header exposes one; else back off
    exponentially (30s, 60s, 120s, ...) capped at RATE_LIMIT_MAX_WAIT."""
    m = re.search(r"retry[- ]after[:\s]+(\d+)", text or "", re.IGNORECASE)
    if m:
        return min(int(m.group(1)), RATE_LIMIT_MAX_WAIT)
    return min(30 * (2 ** attempt), RATE_LIMIT_MAX_WAIT)


def yt_proxy_url() -> str | None:
    """Proxy URL for YouTube traffic only (residential, to dodge the bot-check).
    Either set YT_PROXY directly, or provide DECODO_USERNAME + DECODO_PASSWORD
    (host/port default to Decodo's gateway; override with DECODO_HOST/PORT)."""
    direct = os.environ.get("YT_PROXY")
    if direct:
        return direct
    user, pw = os.environ.get("DECODO_USERNAME"), os.environ.get("DECODO_PASSWORD")
    if user and pw:
        host = os.environ.get("DECODO_HOST") or "gate.decodo.com"
        # Decodo gives sticky-session ports 10001-10010 (each = a distinct IP).
        # Rotating across them spreads requests over ~10 residential IPs.
        port = _pick_port(os.environ.get("DECODO_PORT") or "10001-10010")
        return f"http://{user}:{pw}@{host}:{port}"
    return None


def _pick_port(spec: str) -> str:
    """A single port ('10001') or an inclusive range ('10001-10010') → one port,
    chosen at random so successive requests use different sticky-session IPs."""
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return str(random.randint(int(lo), int(hi)))
    return spec


def yt_proxies() -> dict | None:
    """requests-style proxies dict. The LLM call deliberately does NOT use this."""
    p = yt_proxy_url()
    return {"http": p, "https": p} if p else None


def http_request(method: str, url: str, **kwargs):
    """requests wrapper that reads the Retry-After header on 429 and waits."""
    resp = None
    for attempt in range(6):
        resp = requests.request(method, url, headers={"User-Agent": UA},
                                timeout=20, proxies=yt_proxies(), **kwargs)
        if resp.status_code != 429:
            return resp
        wait = int(resp.headers.get("Retry-After") or min(30 * (attempt + 1), 120))
        print(f"  429 on {url.split('?')[0]}; waiting {wait}s (Retry-After)")
        time.sleep(min(wait, RATE_LIMIT_MAX_WAIT))
    return resp


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
def env(name: str, default: str | None = None) -> str | None:
    val = os.environ.get(name)
    return val if val not in (None, "") else default


def make_client() -> OpenAI:
    # max_retries: the SDK's own transient/429 retries (honors Retry-After);
    # our summarize() loop wraps this for an additional outer backoff layer.
    return OpenAI(
        base_url=env("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
        api_key=require_llm_key(),
        max_retries=5,
        timeout=120.0,
    )


def require_llm_key() -> str:
    key = env("LLM_API_KEY") or env("NVIDIA_API_KEY")
    if not key:
        sys.exit("ERROR: set LLM_API_KEY (or NVIDIA_API_KEY). See .env.example.")
    return key


# --------------------------------------------------------------------------- #
# State
# --------------------------------------------------------------------------- #
def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------- #
# Channel resolution
# --------------------------------------------------------------------------- #
def normalize_channel_ref(ref: str) -> str:
    ref = ref.strip()
    if ref.startswith("UC") and "/" not in ref and " " not in ref:
        return ref  # already a channel_id
    if ref.startswith("@"):
        return f"https://www.youtube.com/{ref}"
    if ref.startswith("http"):
        return ref
    return f"https://www.youtube.com/@{ref}"


def resolve_channel_id(ref: str, cache: dict) -> str | None:
    if ref in cache:
        return cache[ref]
    target = normalize_channel_ref(ref)
    if target.startswith("UC"):
        cache[ref] = target
        return target
    try:
        html = http_request("GET", target).text
    except requests.RequestException as exc:
        print(f"  ! could not fetch {target}: {exc}")
        return None
    for pattern in (
        r'"channelId":"(UC[\w-]{22})"',
        r'"externalId":"(UC[\w-]{22})"',
        r'<meta itemprop="identifier" content="(UC[\w-]{22})">',
        r'channel/(UC[\w-]{22})',
    ):
        m = re.search(pattern, html)
        if m:
            cache[ref] = m.group(1)
            return m.group(1)
    print(f"  ! could not resolve channel id for {ref}")
    return None


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_-]+", "-", text) or "channel"


# --------------------------------------------------------------------------- #
# Transcript
# --------------------------------------------------------------------------- #
def ts_to_seconds(ts: str) -> float:
    h, m, s = ts.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def mmss(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def clean_vtt(raw: str) -> str:
    """Turn YouTube auto/manual VTT into readable text with periodic [mm:ss] marks."""
    words: list[str] = []
    next_mark = 0.0

    def append_dedup(text: str) -> None:
        new = text.split()
        if not new:
            return
        max_k = min(len(words), len(new))
        overlap = 0
        for k in range(max_k, 0, -1):
            if words[-k:] == new[:k]:
                overlap = k
                break
        words.extend(new[overlap:])

    for block in raw.split("\n\n"):
        lines = block.strip().splitlines()
        ts = None
        parts = []
        for ln in lines:
            if "-->" in ln:
                ts = ln.split("-->")[0].strip().split()[0]
            elif ln and not ln.isdigit() and ln not in ("WEBVTT",) \
                    and not ln.startswith(("Kind:", "Language:", "NOTE")):
                parts.append(ln)
        text = re.sub(r"<[^>]+>", "", " ".join(parts))  # strip inline timing tags
        text = html.unescape(text)  # &gt;&gt; -> >>, &amp; -> & etc.
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        if ts:
            try:
                sec = ts_to_seconds(ts)
                if sec >= next_mark:
                    words.append(f"\n\n[{mmss(sec)}] ")
                    next_mark = sec + 30
            except ValueError:
                pass
        append_dedup(text)
    return re.sub(r" *\n\n *", "\n\n", " ".join(words)).strip()


def fetch_transcript(video_id: str) -> str | None:
    """Fetch and clean a transcript. Retries on HTTP 429 (respecting Retry-After)
    until it succeeds or hits a genuine, non-rate-limit error."""
    cached = TRANSCRIPTS_DIR / f"{video_id}.txt"
    if cached.exists() and cached.stat().st_size > 0:
        print("  (using cached transcript)")
        return cached.read_text(encoding="utf-8")

    cookies = env("YTDLP_COOKIES")
    # Local convenience: read cookies straight from a logged-in browser, no export
    # needed. e.g. YTDLP_COOKIES_FROM_BROWSER=chrome (or firefox, safari, brave...).
    cookies_from_browser = env("YTDLP_COOKIES_FROM_BROWSER")
    rate_limit_attempt = 0
    while True:
        with tempfile.TemporaryDirectory() as tmp:
            cmd = [
                "yt-dlp", "--skip-download",
                "--write-subs", "--write-auto-subs",
                "--sub-langs", "en.*,en,en-US,en-GB",
                "--sub-format", "vtt",
                "--retries", "10", "--retry-sleep", "5",
                "--extractor-retries", "3",
                "--sleep-requests", "1",        # pace API calls to dodge 429s
                "--sleep-subtitles", "2",       # extra pause before subtitle download
                "-o", f"{tmp}/%(id)s.%(ext)s",
                WATCH_URL.format(vid=video_id),
            ]
            if cookies:
                cmd += ["--cookies", cookies]
            elif cookies_from_browser:
                cmd += ["--cookies-from-browser", cookies_from_browser]
            proxy = yt_proxy_url()
            if proxy:
                cmd += ["--proxy", proxy]
            try:
                subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=600)
            except subprocess.CalledProcessError as exc:
                stderr = exc.stderr or ""
                if is_bot_check(stderr):
                    # IP-level block — no cookies to authenticate. Don't retry here
                    # (same IP won't clear it); signal the caller to try next run.
                    raise BotCheckError(video_id)
                if is_rate_limited(stderr) and rate_limit_attempt < RATE_LIMIT_MAX_RETRIES:
                    wait = retry_after_seconds(stderr, rate_limit_attempt)
                    rate_limit_attempt += 1
                    print(f"  429 Too Many Requests; waiting {wait}s "
                          f"(retry {rate_limit_attempt}/{RATE_LIMIT_MAX_RETRIES})")
                    time.sleep(wait)
                    continue
                # Genuine error (unavailable / private / no subs / exhausted 429 budget).
                tail = (stderr.strip().splitlines() or ["unknown error"])[-1]
                print(f"  ! yt-dlp failed: {tail}")
                return None
            except subprocess.TimeoutExpired:
                print("  ! yt-dlp timed out")
                return None

            vtts = sorted(glob.glob(f"{tmp}/*.vtt"))
            if not vtts:
                return None  # no subtitles available — a real (non-retryable) outcome
            # Prefer a manual/en track over auto if both exist (heuristic: shorter name).
            vtts.sort(key=lambda p: ("auto" in p, len(p)))
            text = clean_vtt(Path(vtts[0]).read_text(encoding="utf-8", errors="ignore"))
            return text or None


def format_transcript_for_display(raw: str) -> str:
    """Turn the marked-up transcript into clean reading prose: drop the [mm:ss]
    markers, treat ' >> ' speaker cues as paragraph breaks, and keep the natural
    ~30s paragraphing. Returns text with blank-line-separated paragraphs."""
    text = re.sub(r"\[\d{1,2}:\d{2}\]\s*", "", raw)   # drop timestamps
    text = re.sub(r"\s*>>+\s*", "\n\n", text)          # speaker turns -> paragraphs
    text = re.sub(r"\[music\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[ \t]+", " ", text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return "\n\n".join(paras)


def transcript_details_block(raw: str) -> str:
    """A collapsible <details> section holding the verbatim transcript as clean
    HTML paragraphs (escaped, so no stray markdown/HTML surprises)."""
    paras = format_transcript_for_display(raw).split("\n\n")
    inner = "\n".join(f"<p>{html.escape(p)}</p>" for p in paras if p)
    return (
        '\n\n<details class="transcript">\n'
        "<summary>Full transcript</summary>\n\n"
        f"{inner}\n\n"
        "</details>\n"
    )


def transcript_duration_minutes(text: str) -> float:
    """Approximate video length from the last [mm:ss] mark in the transcript
    (marks are emitted every ~30s, so the final one ≈ the duration)."""
    marks = re.findall(r"\[(\d{1,3}):(\d{2})\]", text)
    if not marks:
        return 0.0
    mm, ss = marks[-1]
    return int(mm) + int(ss) / 60.0


def extract_video_id(url_or_id: str) -> str:
    s = url_or_id.strip()
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([\w-]{11})", s)
    if m:
        return m.group(1)
    return s  # already a bare 11-char id


def fetch_metadata(video_id: str) -> dict:
    """Pull title/channel/date for a single video (used by --video)."""
    entry = {"video_id": video_id, "url": WATCH_URL.format(vid=video_id),
             "title": video_id, "channel": "Unknown", "published": ""}
    cmd = ["yt-dlp", "--skip-download", "--no-warnings",
           "--print", "%(title)s\t%(channel)s\t%(upload_date)s",
           WATCH_URL.format(vid=video_id)]
    if env("YTDLP_COOKIES"):
        cmd += ["--cookies", env("YTDLP_COOKIES")]
    try:
        out = subprocess.run(cmd, check=True, capture_output=True,
                             text=True, timeout=120).stdout.strip()
        title, channel, upload_date = (out.split("\t") + ["", "", ""])[:3]
        entry["title"] = title or video_id
        entry["channel"] = channel or "Unknown"
        if len(upload_date) == 8:  # YYYYMMDD -> ISO
            entry["published"] = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}T00:00:00+00:00"
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        print(f"  ! could not fetch metadata: {exc}")
    entry["channel_slug"] = slugify(entry["channel"])
    return entry


# --------------------------------------------------------------------------- #
# Summarize
# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = (
    "You are an expert analyst who writes thorough, faithful summaries of "
    "video transcripts. You never invent facts not present in the transcript. "
    "Timestamps in the transcript look like [mm:ss]; reuse them when referencing "
    "moments. Write in clear Markdown, starting at level-2 headings (##). Do not "
    "include a top-level title or YAML frontmatter."
)

USER_TEMPLATE = """Video: {title}
Channel: {channel}
URL: {url}

Write an extensive summary of the transcript below using this structure:

## TL;DR
Two or three sentences capturing the essence.

## Key Takeaways
5–10 bullet points of the most important ideas.

## Detailed Breakdown
Walk through the video section by section. Start each section with its
approximate [mm:ss] timestamp and a short bold heading, then summarize.

## Notable Quotes
A few verbatim or closely-paraphrased quotes worth remembering.

## People, Tools & References Mentioned
Bulleted list (omit the section if nothing notable).

## Who Should Watch
One or two sentences on the ideal audience and why.

Transcript:
---
{transcript}
---
"""


def _thinking_extra_body() -> dict:
    """By default disable the model's hidden 'thinking' pass — for summarization
    it just burns time/tokens. Set LLM_THINKING=1 to keep it on."""
    if env("LLM_THINKING", "").lower() in ("1", "true", "yes"):
        return {}
    # GLM/vLLM use enable_thinking; some NIM models use thinking. Send both;
    # unknown keys are ignored, and a hard rejection falls back (see below).
    return {"chat_template_kwargs": {"enable_thinking": False, "thinking": False}}


def _stream_completion(client: OpenAI, model: str, messages: list,
                       max_tokens: int, extra_body: dict) -> str:
    """Stream the completion. Streaming keeps the connection fed continuously, so
    the free endpoint won't drop a long generation mid-flight the way a single
    blocking request does. Prints a progress line as chunks arrive."""
    stream = client.chat.completions.create(
        model=model, messages=messages, temperature=0.4,
        max_tokens=max_tokens, stream=True,
        extra_body=extra_body or None,
    )
    parts, chars, last_log = [], 0, 0
    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        piece = getattr(delta, "content", None) or ""
        if piece:
            parts.append(piece)
            chars += len(piece)
            if chars - last_log >= 800:  # occasional heartbeat so it's visibly alive
                print(f"  …streaming {chars} chars")
                last_log = chars
    return "".join(parts).strip()


def summarize(client: OpenAI, model: str, meta: dict, transcript: str) -> str:
    max_tokens = int(env("LLM_MAX_TOKENS", "8192"))
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_TEMPLATE.format(
            title=meta["title"], channel=meta["channel"],
            url=meta["url"], transcript=transcript)},
    ]
    extra_body = _thinking_extra_body()
    # Retry transient LLM failures (connection drops, timeouts, 429s, 5xx) with
    # backoff — keep going until success or a genuine error which raises.
    transient = (APIConnectionError, APITimeoutError, RateLimitError, InternalServerError)
    for attempt in range(RATE_LIMIT_MAX_RETRIES):
        try:
            return _stream_completion(client, model, messages, max_tokens, extra_body)
        except BadRequestError:
            if extra_body:  # server rejected the thinking kwargs — retry without them
                print("  (server rejected thinking kwargs; retrying without)")
                extra_body = {}
                continue
            raise
        except transient as exc:
            if attempt == RATE_LIMIT_MAX_RETRIES - 1:
                raise
            header_ra = ""
            resp_obj = getattr(exc, "response", None)
            if resp_obj is not None:
                header_ra = f"retry-after: {resp_obj.headers.get('retry-after', '')}"
            wait = retry_after_seconds(header_ra or str(exc), attempt)
            print(f"  LLM {type(exc).__name__} (429/transient); waiting {wait}s "
                  f"(retry {attempt + 1}/{RATE_LIMIT_MAX_RETRIES})")
            time.sleep(wait)
    return ""


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #
def yaml_escape(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def thumbnail_url(video_id: str) -> str:
    # hqdefault always exists (480x360); maxresdefault is missing for some videos.
    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"


def write_summary(meta: dict, body: str, transcript: str = "") -> Path:
    out_dir = SUMMARIES_DIR / meta["channel_slug"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{meta['video_id']}.md"
    fm = "\n".join([
        "---",
        f"title: {yaml_escape(meta['title'])}",
        f"channel: {yaml_escape(meta['channel'])}",
        f"video_id: {meta['video_id']}",
        f"url: {meta['url']}",
        f"published: {meta['published']}",
        f"generated: {meta['generated']}",
        f"model: {yaml_escape(meta['model'])}",
        f"thumbnail: {thumbnail_url(meta['video_id'])}",
        "---",
        "",
    ])
    thumb = thumbnail_url(meta["video_id"])
    header = (
        f"# {meta['title']}\n\n"
        f"[![{meta['title']}]({thumb})]({meta['url']})\n\n"
        f"[Watch on YouTube]({meta['url']}) · **{meta['channel']}** · {meta['published'][:10]}\n\n"
    )
    transcript_block = transcript_details_block(transcript) if transcript else ""
    out_path.write_text(fm + header + body + "\n" + transcript_block, encoding="utf-8")
    return out_path

def regenerate_index(processed: dict) -> None:
    done = [{**v, "video_id": vid}
            for vid, v in processed["videos"].items() if v.get("status") == "done"]
    done.sort(key=lambda v: v.get("published", ""), reverse=True)

    lines = [
        "---",
        "title: Home",
        "---",
        "",
        "# YouTube Digest",
        "",
        f"Auto-generated summaries of subscribed channels. "
        f"**{len(done)}** videos summarized.",
        "",
    ]
    by_channel: dict[str, list] = {}
    for v in done:
        by_channel.setdefault(v["channel"], []).append(v)
    for channel in sorted(by_channel):
        lines.append(f"## {channel}")
        lines.append("")
        lines.append('<div class="video-grid">')
        for v in by_channel[channel]:
            # Relative link (no leading slash): VitePress doesn't rewrite raw-HTML
            # anchors with the site base, but a relative href resolves correctly
            # under any base — "/youtube-ai-digest/" in prod and "/" locally.
            link = f"summaries/{v['channel_slug']}/{v['video_id']}"
            thumb = thumbnail_url(v["video_id"])
            date = v.get("published", "")[:10]
            title = html.escape(v["title"])
            lines.append(
                f'<a class="video-card" href="{link}">'
                f'<img loading="lazy" src="{thumb}" alt="">'
                f'<span class="video-title">{title}</span>'
                f'<span class="video-date">{date}</span></a>'
            )
        lines.append("</div>")
        lines.append("")
    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")


def is_short(video_id: str) -> bool:
    """A YouTube Short lives at /shorts/<id> and returns 200; a regular video
    redirects from that path to /watch. Cheap check, no yt-dlp call."""
    try:
        r = http_request("HEAD", f"https://www.youtube.com/shorts/{video_id}",
                         allow_redirects=False)
        return r.status_code == 200
    except requests.RequestException:
        return False  # on error, don't over-filter


def process_one(client: OpenAI, model: str, entry: dict, videos: dict,
                max_minutes: int = 0) -> bool:
    """Fetch transcript, summarize, write markdown, update state.
    Returns True on success, False on a per-video failure, None on an IP-level
    bot-check (caller should stop the run). max_minutes > 0 skips longer videos."""
    vid = entry["video_id"]
    print(f"→ {entry['title']}  ({vid})")
    try:
        transcript = fetch_transcript(vid)
    except BotCheckError:
        # IP-level bot-block: keep the video queued and retry next run (likely a
        # different, cleaner IP). Does NOT count against the attempt budget.
        # Returns None (not False) so the caller stops hammering the flagged IP.
        rec = {k: v for k, v in entry.items() if k != "status"}
        videos[vid] = {**rec, "status": "blocked"}
        print("  blocked by YouTube bot-check; will retry next run")
        return None
    if not transcript:
        attempts = videos.get(vid, {}).get("attempts", 0) + 1
        videos[vid] = {**entry, "status": "no_transcript", "attempts": attempts}
        print(f"  no transcript (attempt {attempts}/{MAX_ATTEMPTS})")
        return False

    if max_minutes:
        minutes = transcript_duration_minutes(transcript)
        if minutes > max_minutes:
            videos[vid] = {**entry, "status": "too_long", "minutes": round(minutes)}
            print(f"  skipped: too long ({round(minutes)}m > {max_minutes}m limit)")
            return False

    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    (TRANSCRIPTS_DIR / f"{vid}.txt").write_text(transcript, encoding="utf-8")

    meta = {**entry, "model": model,
            "generated": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    try:
        body = summarize(client, model, meta, transcript)
    except Exception as exc:  # noqa: BLE001 - surface any API error, keep going
        print(f"  ! summarization failed: {exc}")
        videos[vid] = {**entry, "status": "llm_error",
                       "attempts": videos.get(vid, {}).get("attempts", 0) + 1}
        return False
    if not body:
        print("  ! empty summary, will retry next run")
        return False

    path = write_summary(meta, body, transcript)
    videos[vid] = {"status": "done", "title": entry["title"],
                   "channel": entry["channel"], "channel_slug": entry["channel_slug"],
                   "published": entry["published"], "url": entry["url"],
                   "generated": meta["generated"]}
    print(f"  ✓ {path.relative_to(ROOT)}")
    return True


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def load_subscriptions() -> list[str]:
    data = yaml.safe_load(SUBSCRIPTIONS.read_text()) or {}
    return [c for c in (data.get("channels") or []) if c and not str(c).startswith("#")]


def feed_entries(channel_id: str) -> list[dict]:
    parsed = feedparser.parse(FEED_URL.format(cid=channel_id))
    out = []
    for e in parsed.entries:
        vid = e.get("yt_videoid") or e.get("id", "").split(":")[-1]
        if not vid:
            continue
        out.append({
            "video_id": vid,
            "title": e.get("title", "Untitled"),
            "channel": e.get("author", parsed.feed.get("title", "Unknown")),
            "published": e.get("published", ""),
            "url": WATCH_URL.format(vid=vid),
        })
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="YouTube subscription digest")
    ap.add_argument("--seed", action="store_true",
                    help="mark current feed items as seen without summarizing")
    ap.add_argument("--resolve", action="store_true",
                    help="resolve and cache channel IDs, then exit")
    ap.add_argument("--limit", type=int, default=None,
                    help="max videos to summarize this run")
    ap.add_argument("--dry-run", action="store_true",
                    help="do the work but don't persist state or index")
    ap.add_argument("--video", metavar="URL_OR_ID", default=None,
                    help="summarize a single video by URL or ID (bypasses feeds)")
    ap.add_argument("--include-shorts", action="store_true",
                    help="include YouTube Shorts (skipped by default)")
    args = ap.parse_args()

    include_shorts = args.include_shorts or env("INCLUDE_SHORTS", "").lower() in ("1", "true", "yes")
    limit = args.limit if args.limit is not None else int(env("MAX_VIDEOS_PER_RUN", "25"))
    channels_cache = load_json(CHANNELS_FILE, {})
    processed = load_json(PROCESSED_FILE, {"videos": {}})
    processed.setdefault("videos", {})
    videos = processed["videos"]

    # Single-video mode: summarize one URL/ID directly, no feeds involved.
    if args.video:
        client = make_client()
        model = env("LLM_MODEL", "z-ai/glm-5.2")
        entry = fetch_metadata(extract_video_id(args.video))
        process_one(client, model, entry, videos)
        if not args.dry_run:
            regenerate_index(processed)
            save_json(PROCESSED_FILE, processed)
        return

    subs = load_subscriptions()
    if not subs:
        sys.exit("No channels in subscriptions.yml")

    # Resolve channel IDs.
    resolved = []
    for ref in subs:
        cid = resolve_channel_id(str(ref), channels_cache)
        if cid:
            resolved.append((str(ref), cid))
            print(f"• {ref} -> {cid}")
    save_json(CHANNELS_FILE, channels_cache)
    if args.resolve:
        return

    # --- DISCOVERY -------------------------------------------------------- #
    # Register every new feed video into state immediately (as "pending" or
    # "short"). This captures videos while they're briefly in the ~15-item RSS
    # window, so nothing is lost if the queue can't be fully processed this run.
    discovered = skipped_shorts = 0
    for ref, cid in resolved:
        for entry in feed_entries(cid):
            vid = entry["video_id"]
            if vid in videos:
                continue  # already known (any status) — don't re-discover
            entry["channel_slug"] = slugify(entry["channel"] or ref.lstrip("@"))
            if not include_shorts and is_short(vid):
                videos[vid] = {**entry, "status": "short"}
                skipped_shorts += 1
            else:
                videos[vid] = {**entry, "status": "pending"}
                discovered += 1
    if skipped_shorts:
        print(f"  (skipped {skipped_shorts} new Shorts; use --include-shorts to keep them)")
    if discovered:
        print(f"  discovered {discovered} new video(s)")
    # Persist discovery up front, so a crash mid-processing never loses a video.
    if not args.dry_run and not args.seed:
        save_json(PROCESSED_FILE, processed)

    if args.seed:
        for rec in videos.values():
            if rec.get("status") == "pending":
                rec["status"] = "seeded"
        if not args.dry_run:
            save_json(PROCESSED_FILE, processed)
        print("Seeded pending videos as seen (no summaries generated).")
        return

    # --- THROUGHPUT ------------------------------------------------------- #
    # Work the persisted queue (not just the current feed): pending videos plus
    # transient failures still within their retry budget. Newest-first so fresh
    # uploads jump ahead of old backlog. The cap only limits pace, never loss.
    workable = [
        {**rec, "video_id": vid}
        for vid, rec in videos.items()
        if rec.get("status") in ("pending", "blocked")  # blocked: retry until a clean IP
        or (rec.get("status") in ("no_transcript", "llm_error")
            and rec.get("attempts", 0) < MAX_ATTEMPTS)
    ]
    workable.sort(key=lambda v: v.get("published", ""), reverse=True)

    unlimited = limit <= 0  # MAX_VIDEOS_PER_RUN=0 -> process the whole queue
    cap_desc = "all" if unlimited else str(limit)
    print(f"\n{len(workable)} video(s) in queue; processing up to {cap_desc}.\n")
    if not workable:
        if not args.dry_run:
            regenerate_index(processed)
            save_json(PROCESSED_FILE, processed)
        return

    client = make_client()
    model = env("LLM_MODEL", "z-ai/glm-5.2")

    made = attempted = 0
    for entry in workable:
        if not unlimited and attempted >= limit:
            print(f"Reached limit of {limit}; {len(workable) - attempted} still queued for next run.")
            break
        attempted += 1
        result = process_one(client, model, entry, videos, max_minutes=MAX_VIDEO_MINUTES)
        if result is None:  # bot-check
            if yt_proxy_url():
                # Rotating proxy: the next fetch draws a different residential IP,
                # so don't give up — just move on to the next video.
                print("  (proxy IP flagged; continuing on a fresh IP)")
                continue
            print("  IP flagged by YouTube; ending run early — queued videos retry next run.")
            break
        if result:
            made += 1

    if not args.dry_run:
        regenerate_index(processed)
        save_json(PROCESSED_FILE, processed)
    print(f"\nDone. {made} new summary(ies) this run.")


if __name__ == "__main__":
    main()
