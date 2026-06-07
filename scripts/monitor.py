#!/usr/bin/env python3
"""DocWatch: monitor Google documentation sources for changes."""

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

import feedparser
import requests
import yaml

ROOT = Path(__file__).parent.parent
SNAPSHOTS_DIR = ROOT / "snapshots"
SOURCES_PATH = Path(__file__).parent / "sources.yml"

USER_AGENT = "DocWatch/1.0 (+https://github.com/ViniciusStanula/seo-changelog)"
REQUEST_TIMEOUT = 20
RETRY_DELAY = 3.0
FETCH_DELAY = 1.5
DIFF_CAP = 150  # max diff lines included in issue body

TRACKING_PARAMS = frozenset({
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "hl", "ref", "source", "si",
})


@dataclass
class FeedEntry:
    id: str
    title: str
    link: str
    published: str = ""


@dataclass
class ChangeResult:
    name: str
    status: Literal["seeded", "changed", "unchanged", "broken"]
    message: str
    new_entries: list = field(default_factory=list)
    diff_lines: list = field(default_factory=list)


# -- utils ------------------------------------------------------------------

def strip_tracking_params(url: str) -> str:
    try:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query, keep_blank_values=True)
        clean = {k: v for k, v in qs.items() if k.lower() not in TRACKING_PARAMS}
        return urlunparse(parsed._replace(query=urlencode(clean, doseq=True)))
    except Exception:
        return url


def normalize_markdown(text: str) -> str:
    lines = []
    for line in text.splitlines():
        line = line.strip()
        line = re.sub(
            r'\(https?://\S+?\)',
            lambda m: f'({strip_tracking_params(m.group(0)[1:-1])})',
            line,
        )
        lines.append(line)
    out: list[str] = []
    prev_blank = False
    for line in lines:
        is_blank = (line == "")
        if is_blank and prev_blank:
            continue
        out.append(line)
        prev_blank = is_blank
    return "\n".join(out).strip()


# -- fetch ------------------------------------------------------------------

def fetch_source(url: str) -> requests.Response:
    headers = {"User-Agent": USER_AGENT}
    last_exc: Exception | None = None
    for attempt in range(2):
        try:
            resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            last_exc = e
            if attempt == 0:
                print(f"   retry after: {e}")
                time.sleep(RETRY_DELAY)
    raise last_exc  # type: ignore[misc]


# -- feed -------------------------------------------------------------------

def parse_feed(response: requests.Response) -> list[FeedEntry]:
    parsed = feedparser.parse(response.text)
    if parsed.bozo and not parsed.entries:
        raise ValueError(f"feedparser bozo: {parsed.bozo_exception}")
    if not parsed.entries:
        raise ValueError("feed parsed to 0 entries")

    entries: list[FeedEntry] = []
    for entry in parsed.entries:
        # ID fallback: stable id preferred, link as fallback - never key on title alone
        entry_id = entry.get("id") or entry.get("link")
        if not entry_id:
            continue
        link = strip_tracking_params(entry.get("link", ""))
        entries.append(FeedEntry(
            id=entry_id,
            title=entry.get("title", "(no title)"),
            link=link,
            published=entry.get("published", entry.get("updated", "")),
        ))
    return entries


# -- html extraction --------------------------------------------------------

def _strip_support_boilerplate(md: str) -> str:
    """Remove YouTube embed block and feedback footer from support.google.com pages."""
    lines = md.splitlines()
    out = []
    skip_to_blank = False
    for line in lines:
        if "youtube.com" in line or "youtu.be" in line:
            skip_to_blank = True
            continue
        if "subtitles in your language" in line.lower() or "youtube captions" in line.lower():
            skip_to_blank = True
            continue
        if "was this helpful" in line.lower():
            break  # drop feedback footer and everything after
        if skip_to_blank:
            if line.strip() == "":
                skip_to_blank = False
            continue
        out.append(line)
    return "\n".join(out)


def _extract_article_html2text(response: requests.Response) -> str:
    """
    Extract main content from pages with a single <article> tag using html2text.
    Use for pages where trafilatura produces garbage (complex table-heavy layouts).
    """
    from bs4 import BeautifulSoup
    import html2text as h2t

    soup = BeautifulSoup(response.text, "lxml")
    article = soup.find("article")
    if not article:
        raise ValueError("no <article> tag found - cannot use article_html2text extractor")

    for tag in article.find_all(["script", "style", "nav", "button", "form"]):
        tag.decompose()

    h = h2t.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0

    md = h.handle(str(article))
    md = _strip_support_boilerplate(md)
    return normalize_markdown(md)


def extract_html(response: requests.Response, url: str, hint: str | None = None) -> str:
    """Extract main content from an HTML page and return normalized markdown.

    hint='article_html2text': use BeautifulSoup <article> + html2text instead of
    trafilatura. Use for pages where trafilatura produces garbage (e.g. complex
    table-heavy support.google.com pages).
    """
    if hint == "article_html2text":
        return _extract_article_html2text(response)

    import trafilatura
    extracted = trafilatura.extract(
        response.text,
        url=url,
        include_comments=False,
        include_tables=True,
        no_fallback=False,
        output_format="markdown",
    )
    if not extracted:
        raise ValueError("trafilatura returned empty extraction")
    return normalize_markdown(extracted)


# -- snapshots --------------------------------------------------------------

def snapshot_path(name: str, stype: str) -> Path:
    ext = ".json" if stype == "feed" else ".md"
    return SNAPSHOTS_DIR / f"{name}{ext}"


def load_snapshot(name: str, stype: str):
    path = snapshot_path(name, stype)
    if not path.exists():
        return None
    if stype == "feed":
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return path.read_text(encoding="utf-8")


def save_snapshot(name: str, stype: str, data, dry_run: bool) -> None:
    if dry_run:
        return
    SNAPSHOTS_DIR.mkdir(exist_ok=True)
    path = snapshot_path(name, stype)
    if stype == "feed":
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        path.write_text(data, encoding="utf-8")


# -- change detection -------------------------------------------------------

def detect_feed_changes(
    name: str, fresh: list[FeedEntry], snapshot
) -> tuple[ChangeResult, dict]:
    fresh_data = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "entries": [
            {"id": e.id, "title": e.title, "link": e.link, "published": e.published}
            for e in fresh
        ],
    }
    if snapshot is None:
        return ChangeResult(name, "seeded", f"first run, {len(fresh)} entries stored"), fresh_data

    known_ids = {e["id"] for e in snapshot.get("entries", [])}
    new = [e for e in fresh if e.id not in known_ids]

    if new:
        titles = ", ".join(f'"{e.title}"' for e in new[:3])
        suffix = f" (+ {len(new) - 3} more)" if len(new) > 3 else ""
        return (
            ChangeResult(name, "changed", f"{len(new)} new: {titles}{suffix}", new_entries=new),
            fresh_data,
        )

    return ChangeResult(name, "unchanged", f"{len(fresh)} entries, 0 new"), fresh_data


def detect_html_changes(
    name: str, fresh: str, snapshot
) -> tuple[ChangeResult, str]:
    if snapshot is None:
        return ChangeResult(name, "seeded", "first run, content stored"), fresh
    if fresh == snapshot:
        return ChangeResult(name, "unchanged", "no content change"), fresh

    import difflib
    diff = list(difflib.unified_diff(
        snapshot.splitlines(), fresh.splitlines(),
        fromfile=f"{name}.md (snapshot)", tofile=f"{name}.md (fresh)",
        lineterm="",
    ))
    added = sum(1 for ln in diff if ln.startswith("+") and not ln.startswith("+++"))
    removed = sum(1 for ln in diff if ln.startswith("-") and not ln.startswith("---"))
    return (
        ChangeResult(name, "changed", f"+{added} lines, -{removed} lines", diff_lines=diff),
        fresh,
    )


# -- issue building ---------------------------------------------------------

def build_issue_body(
    changed: list[ChangeResult],
    broken: list[ChangeResult],
    sources_map: dict[str, dict],
    run_time: str,
) -> str:
    parts: list[str] = []

    if broken:
        rows = "\n".join(f"| `{r.name}` | `{r.message}` |" for r in broken)
        parts.append(
            ":warning: **Broken Sources**\n\n"
            "> These sources failed to fetch or parse. "
            "The monitor is blind to changes on these until the URL is fixed in `sources.yml`.\n\n"
            "| Source | Error |\n"
            "|--------|-------|\n"
            + rows
        )

    for r in changed:
        src = sources_map.get(r.name, {})
        url = src.get("url", "")
        lines = [f"### {r.name}"]
        if url:
            lines.append(f"\n**Source:** {url}\n")

        if r.new_entries:
            count = len(r.new_entries)
            noun = "entry" if count == 1 else "entries"
            lines.append(f"**{count} new {noun}:**\n")
            for e in r.new_entries:
                if e.link:
                    lines.append(f"- [{e.title}]({e.link})")
                else:
                    lines.append(f"- {e.title}")

        elif r.diff_lines:
            lines.append("**Content diff:**\n")
            lines.append("```diff")
            lines.extend(r.diff_lines[:DIFF_CAP])
            if len(r.diff_lines) > DIFF_CAP:
                lines.append(f"... ({len(r.diff_lines) - DIFF_CAP} more lines truncated - see snapshot file)")
            lines.append("```")

        parts.append("\n".join(lines))

    parts.append(f"*DocWatch run: {run_time}*")
    return "\n\n---\n\n".join(parts)


def create_github_issue(title: str, body: str, token: str, repo: str) -> str:
    """POST to GitHub Issues API. Returns the URL of the created issue."""
    api_url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    resp = requests.post(api_url, headers=headers, json={"title": title, "body": body}, timeout=30)
    resp.raise_for_status()
    return resp.json()["html_url"]


def post_issue(
    results: list[ChangeResult],
    dry_run: bool,
    run_time: str,
    sources_map: dict[str, dict],
) -> None:
    changed = [r for r in results if r.status == "changed"]
    broken = [r for r in results if r.status == "broken"]

    # TODO: a persistently broken source re-alerts every run. Future fix: track
    # last known status per source in snapshots/<name>.status and alert only on
    # broken-state CHANGE (healthy→broken or broken→healthy), not on every run.

    if not changed and not broken:
        print("\nNothing to report. No issue created.")
        return

    if changed:
        title = f"Docs changed: {len(changed)} source(s) - {run_time}"
    else:
        title = f"Broken sources: {len(broken)} - {run_time}"

    body = build_issue_body(changed, broken, sources_map, run_time)

    if dry_run:
        print("\n" + "=" * 65)
        print("DRY-RUN: Issue that WOULD be posted")
        print("=" * 65)
        print(f"Title: {title}")
        print("-" * 65)
        print(body)
        print("=" * 65 + "\n")
        return

    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not token or not repo:
        print("\nWARNING: GITHUB_TOKEN or GITHUB_REPOSITORY not set - skipping issue creation")
        return

    try:
        issue_url = create_github_issue(title, body, token, repo)
        print(f"\nIssue created: {issue_url}")
    except Exception as e:
        print(f"\nWARNING: failed to create issue: {e}")


# -- main -------------------------------------------------------------------

STATUS_ICON = {
    "seeded":    "[SEEDED] ",
    "changed":   "[NEW]    ",
    "unchanged": "[OK]     ",
    "broken":    "[BROKEN] ",
}


def load_sources() -> list[dict]:
    with open(SOURCES_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)["sources"]


def run(dry_run: bool) -> None:
    sources = load_sources()
    sources_map = {s["name"]: s for s in sources}
    run_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Collect results and snapshot data separately so issue is posted
    # BEFORE snapshots are written to disk (ordering requirement).
    results: list[ChangeResult] = []
    pending_saves: list[tuple[str, str, object]] = []

    print(f"DocWatch - {run_time}")
    print(f"Mode     : {'dry-run (no writes)' if dry_run else 'live (writes snapshots)'}")
    print(f"Sources  : {len(sources)}")
    print()

    for i, src in enumerate(sources):
        name, stype, url = src["name"], src["type"], src["url"]
        if i:
            time.sleep(FETCH_DELAY)

        print(f"-- {name} ({stype})")
        try:
            resp = fetch_source(url)
            print(f"   HTTP {resp.status_code}  {len(resp.content):,} bytes")
        except Exception as e:
            result = ChangeResult(name, "broken", f"fetch failed: {e}")
            print(f"   {STATUS_ICON['broken']} BROKEN SOURCE: {name} - {e}")
            results.append(result)
            continue

        snapshot = load_snapshot(name, stype)

        try:
            if stype == "feed":
                entries = parse_feed(resp)
                print(f"   Parsed {len(entries)} entries")
                result, fresh_data = detect_feed_changes(name, entries, snapshot)
                pending_saves.append((name, stype, fresh_data))
            elif stype == "html":
                md = extract_html(resp, url, hint=src.get("hint"))
                print(f"   Extracted {len(md):,} chars")
                result, fresh_data = detect_html_changes(name, md, snapshot)
                pending_saves.append((name, stype, fresh_data))
            else:
                raise ValueError(f"unknown source type {stype!r}")
        except Exception as e:
            result = ChangeResult(name, "broken", f"parse/extract failed: {e}")
            print(f"   {STATUS_ICON['broken']} BROKEN SOURCE: {name} - {e}")
            results.append(result)
            continue

        print(f"   {STATUS_ICON[result.status]} {result.message}")
        results.append(result)

    # 1. Post issue (built from in-memory results)
    post_issue(results, dry_run, run_time, sources_map)

    # 2. Write snapshots AFTER issue posted
    for name, stype, data in pending_saves:
        save_snapshot(name, stype, data, dry_run)

    print()
    print("-- Summary " + "-" * 55)
    for r in results:
        print(f"  {STATUS_ICON[r.status]} {r.name:<22} {r.message}")

    broken = [r for r in results if r.status == "broken"]
    changed = [r for r in results if r.status == "changed"]
    seeded = [r for r in results if r.status == "seeded"]
    print()
    print(f"  Changed : {len(changed)}   Seeded : {len(seeded)}   Broken : {len(broken)}   Total : {len(results)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DocWatch: monitor Google doc sources.")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="fetch and diff, print issue body that WOULD be posted, skip all writes",
    )
    args = parser.parse_args()
    run(dry_run=args.dry_run)
