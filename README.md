# Anna Job Getter

A lean, AI-assisted job-search command center for **Anna Brown** (Chicago, IL) — built to do four things well:

1. **Aggressively source niche jobs** in arts administration, nonprofit operations, and arts/music education across Chicagoland and full-remote — beyond the generic LinkedIn/Indeed firehose.
2. **Generate perfectly tailored, ATS-optimized resumes** for each listing (aggressive but legitimate — exact keyword mirroring, parse-friendly structure, truthful to Anna's real experience).
3. **Generate tailored, human-sounding cover letters** in Anna's own voice — no em dashes, no AI tells — only when a listing requires one.
4. **One-command intake:** hand the system a job link and processes #2 and #3 kick off automatically and produce the deliverables.

## How to use it

### Primary flow — the Google Sheets
Two native Google Sheets in the `Anna Job Search` Drive folder (see
[`config/drive-locations.md`](config/drive-locations.md)):
- **Anna Job Tracker - My Job Links** — *Anna pastes job URLs here*, one per row.
- **Anna Job Tracker - Job Boards to Check** — live "sort by newest" board links
  to skim in a browser, then paste good ones into My Job Links.

Then say **"check the sheet."**

> **Sourcing reality:** automated job *discovery* is unreliable here — the niche
> boards 403-block direct fetch and the web-search index lags by weeks, so
> "sourced" links are usually stale/already unpublished. The working model is
> human-in-the-loop discovery (skim live boards, paste links) + Claude doing the
> tailoring/packaging. See `search-results/2026-06-19-search.md`. Claude reads the **My Job Links** tab, processes
every new link (see [`workflows/sheet-intake.md`](workflows/sheet-intake.md)), and
files tailored materials in an organized Drive structure:
```
Anna Job Search/Applications/<Org> - <Role>/
    Resume · Cover Letter · Evaluation   (editable Google Docs)
```
Status and links are logged in [`TRACKER.md`](TRACKER.md) (the source of truth) and
mirrored as markdown in `jobs/<slug>/`.

### B) Search for new jobs
Run [`workflows/job-search.md`](workflows/job-search.md) (past-7-days filter).
Output lands in [`search-results/`](search-results/) and the **Claude-Sourced
Jobs** tab.

### C) Process a single link directly
Give Claude a job URL and say **"Process this listing for Anna"** to run
[`workflows/process-listing.md`](workflows/process-listing.md) without the sheet.

> **Tooling note:** the Drive integration can create + read files but cannot edit
> a Sheet's cells in place, or move/delete files. So status lives in `TRACKER.md`
> and the `Applications/` folders, not written back into the sheet. See
> `workflows/sheet-intake.md`.

## Hard filters (every listing must pass all)
- **Salary:** minimum **$50,000/year**. Listed salary preferred and prioritized.
- **Location:** Chicagoland (in-person or hybrid) **OR** fully remote (US, IL-eligible).
- **Type:** full-time.

## Repo layout
```
TRACKER.md    Master log of every job + status + links (source of truth)
profile/      Anna's canonical master profile (source of truth for all tailoring)
config/       Drive folder/sheet IDs (drive-locations.md)
sources/      Curated niche job boards + standing search links
templates/    Resume base + cover-letter voice guide + structures
workflows/    SOPs: sheet-intake, job-search, process-listing
search-results/  Dated search reports
jobs/         One folder per processed listing (eval + resume + cover letter)
```

## Principles
- **Truthful.** Resumes mirror a posting's language and reorder/emphasize Anna's real experience. They never invent jobs, titles, dates, or skills.
- **Legitimate ATS tactics only.** No hidden white-text keyword stuffing — modern ATS expose it and screeners flag it, which is a real reputational risk in Chicago's tight-knit arts/nonprofit world. We win on real keyword matching instead.
- **Her voice, not the model's.** Cover letters follow the voice guide in `templates/` and are checked against an AI-tell blocklist.
- **Human-in-the-loop.** The system drafts and ranks; Anna reviews and decides before anything is submitted.
