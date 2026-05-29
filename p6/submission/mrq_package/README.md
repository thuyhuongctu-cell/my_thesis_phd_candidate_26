# MRQ Submission Package
## Management Review Quarterly — Springer (Scopus Q1; systematic reviews & meta-analyses)

**Manuscript:** "Does Country Context Shape the Internationalization–Performance Link? A Three-Level Meta-Analytic Investigation of Digital Adoption, Institutional Regimes, and the Digital Paradox Lifecycle"

**Target submission:** Q4 2026

**Authors:** Đỗ Thùy Hương & Phan Anh Tú (Can Tho University)

> **Retargeted from International Business Review → Management Review Quarterly** (2026-05-27).
> MRQ specialises in meta-analyses and accommodates comprehensive length (no rigid word cap),
> which fits this manuscript without trimming. `01_manuscript_blinded.docx` has been **rebuilt**
> (MRQ-targeted, blinded; via `scripts/build_p6_blinded_docx.sh`). The **title page and cover
> letter** still carry IBR wording and must be updated before submission (see "Rebuild status").

---

## Package Contents

| File | Description | Submits as |
|------|-------------|------------|
| `01_manuscript_blinded.docx` | Main manuscript — author info removed | Manuscript (blinded) |
| `02_title_page.docx` | Title page with author details, CRediT, data availability | Title page |
| `03_cover_letter.docx` | Cover letter to Editors-in-Chief | Cover letter |
| `figures/figure_1_conceptual_model.png` | Conceptual model — three-level MARA with ICRV, cDAI, DPL | Figure 1 |
| `figures/figure2_icrv_forest.png` | ICRV 5-regime forest plot with 95% CI | Figure 2 |
| `figures/figure3_dpl_phase.png` | DPL phase moderation — I-P effect by digital epoch | Figure 3 |
| `figures/figure4_funnel_plot.png` | Funnel plot with trim-and-fill imputed studies | Figure 4 |
| `figures/figure5_sensitivity.png` | Leave-one-out sensitivity range | Figure 5 |

---

## MRQ Submission Checklist (Springer Editorial Manager)

- [ ] Open the journal homepage (link.springer.com → *Management Review Quarterly*) → "Submit manuscript" (Springer Editorial Manager)
- [ ] **Article type:** Meta-analysis / Systematic Literature Review
- [ ] **Title:** as above
- [ ] **Abstract:** ~300 words (Purpose / Design / Findings / Originality acceptable but not mandated)
- [ ] **Keywords** (5–6): internationalization–performance; meta-analysis; three-level model; digital adoption; ICRV; Digital Paradox Lifecycle
- [ ] Upload `01_manuscript_blinded.docx` → Manuscript (blinded)
- [ ] Upload `02_title_page.docx` → Title Page / Author Information
- [ ] Upload `03_cover_letter.docx` → Cover Letter
- [ ] Upload figures 1–5 → Figure files (separately, high-res)
- [ ] Confirm corresponding author (Phan Anh Tú)
- [ ] OSF pre-registration link (https://osf.io/z37kn) + data availability statement
- [ ] Conflict of interest / funding statement
- [ ] Reference style: APA (matches manuscript)

---

## Manuscript Statistics

| Item | Count |
|------|-------|
| Word count (incl. appendices) | ~14,900 words (MRQ accommodates review length) |
| Abstract | ~300 words |
| Tables | 5 (+ appendices) |
| Figures | 5 |
| Studies (k) | 238 (verified baseline) |
| Effect sizes (K) | 288 (pre-formal-search baseline) |
| Baseline pooled r | .074 (95% CI [.060, .088]) |
| I² total | 62.4% |
| Moderator tests | ICRV Q_M(4) = 17.35, p = .002; cDAI Q_M(2) = 1.23, p = .541; DPL Q_M(2) = 0.56, p = .755 |
| Publication bias | trim-and-fill k = 58, adjusted r = .035 |

---

## Pre-submission Checklist

- [x] OSF pre-registration completed (z37kn; deviations disclosed, Methods §3.1)
- [ ] PRISMA 2020 checklist final counts (Appendix A — pending formal search)
- [x] Single-coder design disclosed (no inter-coder κ; deviation note + Limitations); coding quality via pilot calibration + double-entry verification (§3.3.2)
- [x] `metafor` R package documented; moderator Q_M independently verified (`verify_moderator_qm.py`)
- [x] Publication bias diagnostics (Egger, Begg, trim-and-fill) reported in §4.4

---

## Rebuild status (after retarget)

- [x] `01_manuscript_blinded.docx` — **rebuilt** MRQ-targeted & blinded (1.4 MB, 5 figures embedded)
  via `bash scripts/build_p6_blinded_docx.sh`. Verified: no author tokens, "Can Tho University"
  absent from body, PI mention anonymised to "the first author".
- [x] `02_title_page.docx` — **rebuilt** from `02_title_page.md` (MRQ; k=238/K=288, 5 tables, 5
  figures, OSF link added; CRediT/affiliations/ORCIDs preserved).
- [x] `03_cover_letter.docx` — **rebuilt** from `03_cover_letter.md` (addressed to MRQ Editors-in-Chief;
  rewritten to match the current manuscript — global corpus, honest null moderators, publication-bias
  headline). **Replaces the prior IBR cover letter, which described an obsolete version with
  contradictory results** (I² > 80%, 65% between-study, significant ICRV gradient/cDAI, Asia-Pacific,
  k=235/385). Markdown sources `02_title_page.md` / `03_cover_letter.md` are the canonical sources;
  rebuild all three with `bash scripts/build_p6_blinded_docx.sh`.

---

## Source Files

Main markdown: `p6/p6_meta_manuscript_en.md`
Study database: `p6/data/p6_study_database.csv`
R scripts: `p6/scripts/` (incl. `verify_moderator_qm.py` — Python cross-check, no R needed)
Replication / pipeline: `p6/tools/`
