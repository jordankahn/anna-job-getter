# Workflow: Process a Single Listing ("paste a link")

Trigger: user provides a job URL (or pasted description) and says
**"Process this listing for Anna."**

## Steps

### 1. Fetch + parse
- Fetch the URL (WebFetch). If blocked, ask the user to paste the description.
- Extract: job title, organization, location, remote/hybrid/onsite, employment
  type, salary (range if listed), application method, **whether a cover letter is
  required**, and the full responsibilities + qualifications text.

### 2. Apply hard filters
- Salary ≥ $50,000 (or unlisted — then estimate + flag).
- Location: Chicagoland (onsite/hybrid) OR fully remote (US/IL-eligible).
- Full-time.
- If it fails a filter, STOP and tell the user why (offer to proceed anyway if
  they want).

### 3. Build the keyword map
- Pull the exact job title, repeated nouns, required tools/systems, and must-have
  qualifications into a keyword list.
- Map each to Anna's **true** matching experience from `profile/anna-master-profile.md`.
- Note any genuine gaps.

### 4. Write the evaluation (`jobs/<slug>/evaluation.md`)
- A–F fit grade with one-line rationale per dimension: mission fit, skill match,
  comp, location, growth, legitimacy (scam/ghost check).
- Keyword coverage summary and honest gaps.
- Cover letter required? yes/no.

### 5. Generate the tailored resume
- Choose Track A or Track B base from `templates/`.
- Keyword-mirror to the posting (see `templates/resume-guide.md`); reorder bullets;
  put exact title in summary when truthful.
- Save `jobs/<slug>/Anna_Brown_Resume_<slug>.md`.
- Create a Google Doc (see Delivery).

### 6. Generate the cover letter — ONLY if required/expected
- Follow `templates/cover-letter-voice-guide.md`.
- Run the style checklist; **grep for em dashes (—) and remove all**.
- Save `jobs/<slug>/Anna_Brown_CoverLetter_<slug>.md`.
- Create a Google Doc.

### 7. Delivery
- Save Markdown in `jobs/<slug>/`.
- Create editable Google Docs in the Drive folder "Anna Job Search" (one doc per
  resume / cover letter) so Anna can review and tweak.
- Report back: grade, salary, location, cover-letter status, keyword coverage,
  gaps, and the Drive links.

### 8. Commit
- Commit the new `jobs/<slug>/` folder to the working branch.

## Slug convention
`<org-kebab>-<role-kebab>` e.g. `old-town-school-development-coordinator`.
