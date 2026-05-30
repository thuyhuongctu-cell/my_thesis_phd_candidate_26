# MBR Submission Package
## Multinational Business Review — Emerald (Scopus Q2; ABS-2; IB-focused)

**Manuscript:** "Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis"

**Target submission:** Q3 2026

**Authors:** Đỗ Thùy Hương & Phan Anh Tú (Can Tho University)

> **Retargeted from Management Review Quarterly → Multinational Business Review** (2026-05-30).
> Rationale: MBR offers a faster review cycle (~2–3 months first decision vs. MRQ's 3–4 months),
> higher acceptance probability (~25% vs. MRQ's ~15%), and a tighter IB-management framing fit.
> ABS-2 still counts for promotion; Scopus Q2 retains indexing prestige.

---

## Package Contents

| File | Description | Submits as |
|------|-------------|------------|
| `01_manuscript_blinded.docx` | Main manuscript — author info removed | Manuscript (blinded) |
| `02_title_page.docx` | Title page with author details, CRediT, data availability | Title page |
| `03_cover_letter.docx` | Cover letter to Editor-in-Chief | Cover letter |
| `figures/figure_1_conceptual_model.png` | Conceptual model — three-level MARA with ICRV, cDAI, DPL | Figure 1 |
| `figures/figure2_icrv_forest.png` | ICRV 5-regime forest plot with 95% CI | Figure 2 |
| `figures/figure3_dpl_phase.png` | DPL phase moderation — I-P effect by digital epoch | Figure 3 |
| `figures/figure4_sensitivity.png` | Leave-one-out sensitivity range | Figure 4 |
| `figures/figure5_funnel_plot.png` | Funnel plot with trim-and-fill imputed studies | Figure 5 |
| `figures/figure6_year_distribution.png` | Distribution of primary studies by publication year (k = 238) | Figure 6 |

---

## MBR Submission Checklist (Emerald ScholarOne)

- [ ] Log in to ScholarOne (https://mc.manuscriptcentral.com/mbr)
- [ ] Click "Submit a New Manuscript"
- [ ] **Article type:** Research Paper
- [ ] **Title:** as above
- [ ] **Structured abstract** (Purpose / Design / Findings / Research limitations / Practical implications / Originality): ≤ 250 words
- [ ] **Keywords** (≤ 6): internationalization–performance; meta-analysis; three-level model; digital adoption; institutional context; publication bias
- [ ] Upload `01_manuscript_blinded.docx` → Main Document (blinded)
- [ ] Upload `02_title_page.docx` → Title Page / Author Information (separate, NOT for review)
- [ ] Upload `03_cover_letter.docx` → Cover Letter
- [ ] Upload figures 1–6 → Figure files (separately, high-res; PNG accepted)
- [ ] Confirm corresponding author (Phan Anh Tú)
- [ ] OSF pre-registration link (https://osf.io/z37kn) + data availability statement
- [ ] Conflict of interest statement (none)
- [ ] Funding statement (no funding)
- [ ] Ethics statement (meta-analysis of secondary aggregated data; IRB not required)
- [ ] **Word-count gate:** confirm total ≤ 8,000 (incl. abstract, refs, appendices). Appendices on OSF.

---

## Manuscript Statistics

| Item | Count |
|------|-------|
| Word count (main text) | $\approx$ 6,900 words |
| Word count (incl. refs, appendices on OSF) | Target $\leq$ 8,000 at submission build (streamlining pass required) |
| Abstract (structured) | $\leq$ 250 words (Emerald format) |
| Tables | 5 (extended appendices migrated to OSF) |
| Figures | 6 (incl. year-distribution histogram) |
| Studies (k) | 238 (verified baseline) |
| Effect sizes (K) | 288 (pre-formal-search baseline) |
| Baseline pooled r | .074 (95% CI [.060, .088]) |
| I² total | 87.8% |
| Moderator tests | ICRV Q_M(4) = 17.35, p = .002 (not robust); cDAI Q_M(2) = 1.23, p = .541; DPL Q_M(2) = 0.56, p = .755 |
| Publication bias | trim-and-fill k = 58, adjusted r = .035 |

---

## Pre-submission Checklist

- [x] OSF pre-registration completed (z37kn; deviations disclosed, Methods §3.1)
- [x] Structured abstract restructured to Emerald format
- [ ] PRISMA 2020 checklist final counts (Appendix A — pending formal search; OSF supplementary)
- [x] Single-coder design disclosed (no inter-coder κ; deviation note + Limitations); coding quality via pilot calibration + double-entry verification (§3.3.2)
- [x] `metafor` R package documented; moderator Q_M independently verified (`verify_moderator_qm.py`)
- [x] Publication bias diagnostics (Egger, Begg, trim-and-fill) reported in §4.6
- [x] Temporal distribution caveat + Figure 6 (year-distribution histogram) added (Section 4.1)
- [ ] **Word-count trim to ≤ 8,000 total** — required before final ScholarOne upload. Plan: move Appendix A (PRISMA trace) and Appendix B (coding protocol) to OSF supplementary; tighten Discussion §5.3.

---

## Rebuild status

- [x] `01_manuscript_blinded.docx` — built MBR-targeted & blinded via `scripts/build_p6_blinded_docx_mbr.sh`.
  Verified: no author tokens, "Can Tho University" absent from body, PI mention anonymised to "the first author".
- [x] `02_title_page.docx` — built from `02_title_page.md` (MBR; k=238/K=288, 5 tables, 6 figures,
  OSF link added; CRediT/affiliations/ORCIDs preserved).
- [x] `03_cover_letter.docx` — built from `03_cover_letter.md` (addressed to Prof. William Newburry,
  MBR Editor-in-Chief; rewritten to match MBR's MNE-management framing — global corpus, honest null
  moderators, publication-bias headline, practical-implications hook).

---

## Why MBR vs. alternatives

| Tradeoff | MBR (chosen) | MRQ (backup) | IBR (deprecated) | MIR (top-tier alt) |
|---|---|---|---|---|
| Time to first decision | 2–3 months | 3–4 months | 4–6 months | 4–6 months |
| Acceptance rate | ~25% | ~15% | ~10–15% | ~15–20% |
| Quartile / List | Q2 / ABS-2 | Q1 / Springer | Q1 / Elsevier | Q1 / ABS-3 |
| Word cap (total) | 8,000 | flexible | 8,000–10,000 | 12,000 |
| Single-coder tolerance | acceptable if disclosed | acceptable | likely flagged | likely flagged |
| Null moderator tolerance | high (MNE practical hook) | high (review specialty) | moderate | low–moderate |
| Practical-implications fit | strong | moderate | moderate | moderate |
| Best for current hồ sơ | ✅ recommended | ✅ backup | ❌ desk-reject risk | ⚠️ stretch |

---

## Source Files

Main markdown: `p6/p6_meta_manuscript_en.md` (MBR-targeted; structured abstract; MBR footer)
Study database: `p6/data/p6_study_database.csv`
R scripts: `p6/scripts/` (incl. `verify_moderator_qm.py` — Python cross-check, no R needed)
Replication / pipeline: `p6/tools/`
Build script: `scripts/build_p6_blinded_docx_mbr.sh`
