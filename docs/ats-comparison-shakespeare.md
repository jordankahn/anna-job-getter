# ATS comparison — Anna's actual resume vs ATS-optimized (Chicago Shakespeare job)

Ran both through the same local ATS-style parse (extract text, detect contact +
sections, keyword-match vs the Donor Services Associate JD). See `tools/`.

| Metric | Anna's actual two-column resume | ATS-optimized version |
|---|---|---|
| Keyword match vs JD | **12%** (5/41) | **78%** |
| Standard sections detected | 3/5 (no Summary) | 5/5 |
| Email / phone parsed | yes / yes | yes / yes |
| Layout | two-column PDF (garbled spacing, side-column risk) | single column, clean text |

## Honest read
The gap is TWO stacked effects, not one:
1. **Tailoring (bigger):** her actual resume is the generic nonprofit version, so
   it lacks the job's vocabulary (donor, gifts, pledges, stewardship, Tessitura,
   fundraising). Any generic resume scores low on a specific posting.
2. **Format (secondary):** the two-column PDF degrades extraction (letter-spacing
   artifacts), drops the Summary, and risks interleaving the side column.

Takeaway: not "ugly = better" but "tailored + machine-readable = better."
ATS-safe does NOT require ugly — tables/text-boxes/columns/images break parsers,
but color, good fonts, and spacing are fine. A nicer single-column template can
be both attractive and ATS-safe.
