# OSF project structure for the dissertation papers (P3–P11)

A standard Open Science Framework layout so each paper has a citable,
reproducibility-grade project. Building these strengthens reviewer confidence and
is the public counterpart to `REPRODUCIBILITY.md`.

## One OSF project per paper — standard component layout

```
osf.io/<paper>/
├── Registration / Analysis plan      ← see labelling rule below
├── data/
│   ├── README_data_access.md         ← WBES licence + how to obtain the .dta
│   └── (no raw WBES micro-data committed — licensed; link + access steps only)
├── code/
│   ├── <paper>_models.py             ← the estimation script (from the repo)
│   ├── verify.txt                    ← exact command + expected output lines
│   └── stata/ *.do                   ← the matching Stata do-files
├── materials/
│   ├── codebook.md                   ← variable definitions (WBES item → variable)
│   ├── ICRV_crosswalk.csv            ← economy → ICRV regime mapping
│   └── PRISMA / coding protocol      ← P6 only
└── manuscript/
    └── <paper>_blinded.pdf
```

## Labelling rule (fixes the P6 issue — important)

OSF distinguishes **Preregistration** (analysis plan deposited *before* data are
seen) from **Registration of an analysis plan** (plan deposited after data exist).
Use the accurate label:

| Paper | Correct OSF label | Why |
|---|---|---|
| P3, P4, P5, P7, P8, P9, P10, P11 | *Registered analysis materials* (post-hoc) | These analyse pre-existing WBES waves; they are not pre-registered. |
| P6 meta-analysis | *Registered analysis plan* — **not** "pre-registration" | Corpus partly assembled by backward-citation before the OSF date (18 May 2026); calling it a strict pre-registration would misstate the timeline (already fixed in `p6/p6_meta_manuscript_en.md`). |

Mislabelling a post-hoc plan as a "preregistration" is a common and avoidable
integrity flag; the rule above keeps every claim defensible.

## Per-paper checklist

- [ ] Create OSF project; set licence (CC-BY for materials, an OSI licence for code).
- [ ] Upload the estimation script + the matching Stata do-file.
- [ ] Add `verify.txt`: the one command and the expected output (from the repo's
      `*_results.md`), so a visitor reproduces the headline number in one step.
- [ ] Upload the codebook + ICRV crosswalk; do **not** upload raw WBES micro-data
      (licensed) — provide the access link and steps instead.
- [ ] Upload the blinded manuscript.
- [ ] Mint the OSF DOI; cite it in the paper ("Data and code: osf.io/xxxx").
- [ ] Cross-link to the GitHub repository and (for code) the Zenodo release DOI.

## Recommended creation order

P9 to P10 to P11 (JED) to P4 to P5 to P3 to P7 to P8 to P6, mirroring the submission
roadmap in `reviews/PUBLICATION_PLAN_2026-06-13.md`. P6 last, because its OSF
component needs the corrected registered-plan labelling and the completed
inter-coder-reliability statistics (pending the double-coding data).

## What already exists in the repo to upload

- Estimation scripts: `scripts/p7_run_50econ.py`, `scripts/p7_full_ladder.py`,
  `p10_japan/replication/p10_japan_models.py`,
  `jed_ai_digital/replication/jed_digital_divide.py`, `scripts/p6_meta_analysis.py`.
- Verification: `scripts/verify_all.py` (the one-command reproducibility proof).
- Stata do-files: `scripts/stata/*.do`.
- Codebook/crosswalk material: `data_wbes/analysis/CANONICAL_NUMBERS.md`,
  `p6/tools/p6_extraction_codebook.md`, the ICRV mapping in
  `scripts/cd1_descriptives_pipeline.py`.
- P6 registration template: `p6/osf/P6_OSF_Preregistration_Template.md`
  (rename/relabel to "registered analysis plan").
