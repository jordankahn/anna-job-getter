# Drive Locations (IDs)

Canonical IDs for the Google Drive + Sheet surfaces. Update if anything is
regenerated.

## Folders
- **Anna Job Search** (root): `18eTwfbKia-JOCo61eNrG76btjGXpJiyZ`
  https://drive.google.com/drive/folders/18eTwfbKia-JOCo61eNrG76btjGXpJiyZ
- **Applications**: `1SU6qQ0iKWfMMMz0-c5WLinZUXGvxIAig`
  https://drive.google.com/drive/folders/1SU6qQ0iKWfMMMz0-c5WLinZUXGvxIAig

## Sheets (native Google Sheets — verified working)
Two native sheets instead of one multi-tab file: the Drive integration can't
upload a verifiable binary `.xlsx` (no md5 in metadata) or convert xlsx to a
native Sheet, so a multi-tab workbook corrupted in transit. Native sheets are
created from CSV text (`contentMimeType: text/csv`), which is reliable and
read-back verifiable.

- **Anna Job Tracker - My Job Links** (Anna's input — paste live links here): `1jX62iui_TUrsyLEiMKwjlDm9kDRKtGmPSqgb9Hc4mxE`
  https://docs.google.com/spreadsheets/d/1jX62iui_TUrsyLEiMKwjlDm9kDRKtGmPSqgb9Hc4mxE/edit
- **Anna Job Tracker - Job Boards to Check** (live "sort by newest" board links to skim in a browser): `1-tyV2YwSAPFlA6gbpmvGIjn1bD1ZVN8e11QW1uEi19s`
  https://docs.google.com/spreadsheets/d/1-tyV2YwSAPFlA6gbpmvGIjn1bD1ZVN8e11QW1uEi19s/edit

> DELETE MANUALLY (stale): the old **Anna Job Tracker - Claude-Sourced Jobs**
> sheet (`1ays8tt1pTyWzazScQoz9ZehhV869mmwezhf7bLi13hg`) was built from search-index
> data whose links are now unpublished/dead. Replaced by "Job Boards to Check".
> Automated sourcing is unreliable here (boards 403-block fetch; search index lags),
> so the model is: skim live boards in a browser -> paste links into My Job Links
> -> Claude processes them.

> DELETE MANUALLY: a broken `Anna Job Tracker.xlsx`
> (`1L_bZwgWACkm6IbApnWigLhxZeCE547Kc`) was left in the root folder by a failed
> binary upload. The integration can't delete files; remove it by hand.

### How to refresh a sheet (no in-place cell edits available)
To update content, rebuild the CSV and create a NEW native sheet, then update the
id here. (We cannot append rows or edit cells in an existing sheet with the
current tools.) `tools/build_sheet.py` documents the column layout.

## Per-job folders
- After School Matters - Manager of Events & Donor Relations:
  `1zhiAAVnBn6L7i_VA5XK10L7VKxejZ8_b`
  - Resume doc: `1wEloikFPx4SYvBtQJKjsxqHq7sns_9hUn5l_yE7CS4s`
  - Cover Letter doc: `1qYk15eymcxpwWF6JsBAG7eIw0HkWzFaLf60Gopie9yY`
  - Evaluation doc: `1L5n0KpszA9s0cD2m8qF1KTCVZFHQhtxLQToXRpJTbcQ`

> Note: two loose copies of the After School Matters resume/cover letter were
> created in the root `Anna Job Search` folder before reorganization. The
> integration cannot delete files; Anna can remove those two manually. The
> organized copies live in the per-job folder above.
