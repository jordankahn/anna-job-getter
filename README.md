# Anna Job Getter

A lean, AI-assisted job-search command center for **Anna Brown** (Chicago, IL) — built to do four things well:

1. **Aggressively source niche jobs** in arts administration, nonprofit operations, and arts/music education across Chicagoland and full-remote — beyond the generic LinkedIn/Indeed firehose.
2. **Generate perfectly tailored, ATS-optimized resumes** for each listing (aggressive but legitimate — exact keyword mirroring, parse-friendly structure, truthful to Anna's real experience).
3. **Generate tailored, human-sounding cover letters** in Anna's own voice — no em dashes, no AI tells — only when a listing requires one.
4. **One-command intake:** hand the system a job link and processes #2 and #3 kick off automatically and produce the deliverables.

## How to use it

### A) Search for new jobs
Run the search workflow in [`workflows/job-search.md`](workflows/job-search.md). Output lands in [`search-results/`](search-results/) as dated reports with graded, filtered listings.

### B) Process a single listing (the "paste a link" flow)
Give Claude Code a job URL and say: **"Process this listing for Anna."**
Claude follows [`workflows/process-listing.md`](workflows/process-listing.md):
1. Fetches + parses the posting (title, org, location, salary, must-have keywords).
2. Checks it against the hard filters.
3. Writes an A–F evaluation.
4. Generates a tailored resume (keyword-mirrored to the posting).
5. Generates a cover letter **only if the posting requires one**, in Anna's voice.
6. Saves Markdown to `jobs/<slug>/` and creates editable **Google Docs** in Drive for review.

## Hard filters (every listing must pass all)
- **Salary:** minimum **$50,000/year**. Listed salary preferred and prioritized.
- **Location:** Chicagoland (in-person or hybrid) **OR** fully remote (US, IL-eligible).
- **Type:** full-time.

## Repo layout
```
profile/      Anna's canonical master profile (source of truth for all tailoring)
sources/      Curated niche job boards + standing search links
templates/    Resume base + cover-letter voice guide + structures
workflows/    Step-by-step SOPs: job-search, process-listing
search-results/  Dated search reports
jobs/         One folder per processed listing (eval + resume + cover letter)
```

## Principles
- **Truthful.** Resumes mirror a posting's language and reorder/emphasize Anna's real experience. They never invent jobs, titles, dates, or skills.
- **Legitimate ATS tactics only.** No hidden white-text keyword stuffing — modern ATS expose it and screeners flag it, which is a real reputational risk in Chicago's tight-knit arts/nonprofit world. We win on real keyword matching instead.
- **Her voice, not the model's.** Cover letters follow the voice guide in `templates/` and are checked against an AI-tell blocklist.
- **Human-in-the-loop.** The system drafts and ranks; Anna reviews and decides before anything is submitted.
