# Workflow: Google Sheet Intake + File Organization

Anna's job links live in a Google Sheet. Claude reads the sheet, processes new
links into tailored materials, and files them in an organized Drive structure.

## The surfaces

**Google Sheet — "Anna Job Tracker"** (in the `Anna Job Search` Drive folder).
Three tabs:
- **Start Here** — instructions.
- **My Job Links** — *Anna's input.* She pastes one job URL per row.
- **Claude-Sourced Jobs** — *Claude's output.* Jobs Claude found, posted within
  the last 7 days (see `workflows/job-search.md`).

**Drive folders:**
```
Anna Job Search/
├── Anna Job Tracker            (the Google Sheet)
└── Applications/
    └── <Org> - <Role>/         (one folder per job)
        ├── Anna Brown - Resume - <Org> (<Role>)
        ├── Anna Brown - Cover Letter - <Org> (<Role>)
        └── Anna Brown - Evaluation - <Org> (<Role>)
```

**Repo (canonical log):**
- `TRACKER.md` — master table of every job + its status + links.
- `jobs/<slug>/` — markdown mirror of each package (evaluation, resume, cover letter).
- IDs of all Drive folders/sheet live in `config/drive-locations.md`.

## Run it: "check the sheet"
When the user says **"check the sheet"** (or on a schedule via the `/loop` skill):
1. Read the sheet with `read_file_content` (Drive file id in `config/drive-locations.md`).
2. Parse the **My Job Links** tab. A row is **new** if its URL is not already a
   row in `TRACKER.md`.
3. For each new link, run `workflows/process-listing.md`:
   - Evaluate (A–F) against the hard filters.
   - Generate the tailored resume; generate a cover letter only if the posting
     requires one.
   - Create `Applications/<Org> - <Role>/` and add the Resume, Cover Letter, and
     Evaluation as Google Docs.
   - Mirror markdown into `jobs/<slug>/`.
4. Add a row to `TRACKER.md` (status `Materials ready`) with the Drive links.
5. Commit + push the repo. Report the folder + doc links in chat.

## Refreshing Claude-Sourced jobs
Run `workflows/job-search.md` with the **past-7-days** filter, append results to
`TRACKER.md`, and regenerate the sheet's **Claude-Sourced Jobs** tab.

## Tooling limitation (read this)
The Drive integration can **create and read** files but **cannot edit a Sheet's
cells in place, move, or delete** files. Consequences:
- Status/links are written to **`TRACKER.md` (versioned in git)** and the
  **Applications** folders, which are the source of truth — not back into the
  sheet's cells.
- Refreshing the sheet means **regenerating** it (Anna's `My Job Links` rows are
  read first and carried forward). The regenerated sheet may get a new URL; update
  `config/drive-locations.md` when that happens.
- The sheet is the easy human **input** surface; the repo + Applications folder
  are the durable **output** record.
