# seo-changelog — DocWatch

Twice-daily GitHub Action that monitors Google documentation for changes and
notifies via GitHub Issues. Zero cost: uses only the built-in `GITHUB_TOKEN`.
No email provider, no external services, no paid APIs.

## Sources

| Name | Type | Why | URL |
|------|------|-----|-----|
| `search_blog` | Feed | Google Search Central blog — algorithm updates, new features, policy announcements | [feed.xml](https://developers.google.com/search/blog/feed.xml) |
| `search_docs` | Feed | Search documentation change log — when a help page or spec changes | [rss](https://developers.google.com/search/updates/search_docs_updates.rss) |
| `lighthouse` | Feed | Lighthouse release notes — new audits, scoring changes, CLI updates | [releases.atom](https://github.com/GoogleChrome/lighthouse/releases.atom) |
| `chrome_blog` | Feed | Chrome for Developers blog — also carries "What's new in DevTools" posts | [feed.xml](https://developer.chrome.com/static/blog/feed.xml) |
| `merchant_api` | HTML diff | Merchant API "Latest Updates" — the authoritative release notes for the Merchant API (successor to Content API for Shopping). No feed exists; page is diffed each run | [latest-updates](https://developers.google.com/merchant/api/latest-updates) |

**Why no separate Chrome DevTools source:** The `chrome_blog` feed already
surfaces "What's new in DevTools" posts (e.g. `new-in-devtools-149`) — adding a
separate DevTools source would be redundant.

**Why Merchant API and not Content API for Shopping:** Content API for Shopping
is being sunset on August 18, 2026. Merchant API is its successor and where all
new policy, spec, and API changes appear.

## Setup

1. Push this repo to GitHub (fork or create new).
2. **No secrets needed.** The Action uses the built-in `GITHUB_TOKEN` — no
   configuration required.
3. If the Actions tab shows the workflow as disabled, click **Enable workflow**.
4. **Subscribe to notifications:** On the repo page, click **Watch > Custom >
   Issues**. GitHub emails you each time a new issue is opened.

## How it works

The Action runs at **06:00 UTC** and **18:00 UTC** every day, and can be
triggered manually via **Actions > DocWatch > Run workflow**.

Each run, in order:
1. Fetches every source and compares against the committed snapshot in `snapshots/`.
2. Detects changes in memory (new feed entries; or content diff for HTML sources).
3. If anything changed **or** a source is broken: opens a GitHub Issue.
4. Writes updated snapshots to disk.
5. Commits the snapshots (`[skip ci]` so the commit does not re-trigger the Action).

## First run (seed)

On the very first run, every source is new — there is nothing to compare against.
The Action commits the initial snapshots and **opens no issue**. This is expected.
The first issue you receive will be a real content change, never a seed dump.

## Issue format

**Title:** `Docs changed: N source(s) - YYYY-MM-DD HH:MM UTC`

**Body:** one section per changed source.

- Feed sources list new entries with title and link.
- HTML sources (`merchant_api`) show a unified diff of the extracted content
  (capped at 150 lines; the full diff is always in the committed snapshot file).

One issue per run keeps it to a single notification email per event.
Closed issues stay as permanent history.

## Broken sources

If a source fails to fetch or parse, a **:warning: Broken Sources** table appears
at the **top** of the run issue. If nothing else changed but a source is broken,
an issue is still opened — a broken source means the monitor is blind to that
source and you need to know immediately.

Fix broken sources by updating the URL in `scripts/sources.yml` and running the
Action manually to confirm.

> **Note:** A persistently broken source re-alerts every run. A future improvement
> would alert only on broken-state *change* (healthy → broken, broken → healthy).
> See the TODO comment in `scripts/monitor.py` → `post_issue()`.

## Adding a source

Edit `scripts/sources.yml`:

```yaml
- name: my_source        # filename-safe, unique identifier
  type: feed             # "feed" or "html"
  url: https://...
```

**Feed sources** (`type: feed`): RSS or Atom. New entries trigger a notification.
Prefer feeds over HTML diffing — they produce zero false positives.

**HTML sources** (`type: html`): Main content extracted via trafilatura, stored
as markdown in `snapshots/<name>.md`, diffed each run. Use for pages with no feed.

To remove a source: delete its entry from `sources.yml` and delete
`snapshots/<name>.json` (or `.md`).

## Local development

```bash
pip install -r requirements.txt

# Fetch all sources, detect changes, print the exact issue body that WOULD be
# posted. Writes nothing.
python scripts/monitor.py --dry-run

# Live run: writes snapshots locally. Creates a GitHub Issue if
# GITHUB_TOKEN and GITHUB_REPOSITORY are set.
GITHUB_TOKEN=ghp_... GITHUB_REPOSITORY=ViniciusStanula/seo-changelog \
  python scripts/monitor.py
```

To simulate a change locally: edit `snapshots/search_blog.json` and remove one
entry from the `entries` array, then run `--dry-run`. The removed entry appears
as new and the full issue body is printed to stdout.

## Schedule

Runs at **06:00 UTC** and **18:00 UTC** daily.
Trigger manually: **Actions > DocWatch > Run workflow**.
