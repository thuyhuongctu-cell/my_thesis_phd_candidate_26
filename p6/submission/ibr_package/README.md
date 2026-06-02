# IBR Submission Package
## International Business Review — Elsevier (IF ≈ 5.5, ABS-3)

**Manuscript:** "Does Country Context Shape the Internationalization–Performance Link? A Three-Level Meta-Analytic Investigation of Digital Adoption, Institutional Regimes, and the Digital Paradox Lifecycle"

**Target submission:** Q4 2026

**Authors:** Đỗ Thùy Hương & Phan Anh Tú (Can Tho University)

---

## Package Contents

| File | Description | Submits as |
|------|-------------|------------|
| `01_manuscript_blinded.docx` | Main manuscript — author info removed | Manuscript (blinded) |
| `02_title_page.docx` | Title page with author details, CRediT, data availability | Title page |
| `03_cover_letter.docx` | Cover letter to Editor-in-Chief | Cover letter |
| `figures/figure_1_conceptual_model.png` | Conceptual model — three-level MARA with ICRV, cDAI, DPL | Figure 1 |
| `figures/figure2_icrv_forest.png` | ICRV 5-regime forest plot with 95% CI | Figure 2 |
| `figures/figure3_dpl_phase.png` | DPL phase moderation — I→P effect by digital epoch | Figure 3 |
| `figures/figure4_sensitivity.png` | Leave-one-out sensitivity range | Figure 4 |
| `figures/figure5_funnel_plot.png` | Funnel plot with trim-and-fill imputed studies | Figure 5 |

---

## IBR Submission Checklist (Editorial Manager / EM)

- [ ] Register / log in to IBR Editorial Manager (editorialmanager.com/ibr)
- [ ] Select "Submit New Manuscript"
- [ ] **Manuscript type:** Research Article
- [ ] **Title:** as above
- [ ] **Abstract:** ~300 words (structured: Purpose / Design / Findings / Originality)
- [ ] **Keywords** (5–6): internationalization–performance; meta-analysis; three-level model; digital adoption; ICRV; Digital Paradox Lifecycle
- [ ] Upload `01_manuscript_blinded.docx` → Manuscript
- [ ] Upload `02_title_page.docx` → Author Information / Title Page
- [ ] Upload `03_cover_letter.docx` → Cover Letter
- [ ] Upload figures 1–5 → Figure files (separately, high-res)
- [ ] Confirm corresponding author (Phan Anh Tú)
- [ ] OSF pre-registration link (add before submission)
- [ ] Conflict of interest statement
- [ ] Data availability: coded dataset available upon reasonable request

---

## Manuscript Statistics

| Item | Count |
|------|-------|
| Word count (main text) | 11,129 words |
| Abstract | ~300 words |
| Tables | 5 (+ appendices) |
| Figures | 5 |
| Studies (k) | 238 |
| Effect sizes | 288 (pre-formal-search baseline) |
| Baseline pooled r | 0.074 (95% CI [0.060, 0.088]) |
| I² total | 87.8% (I²₍₂₎ = 76.1%, I²₍₃₎ = 11.8%) |

---

## Pre-submission Checklist

- [ ] OSF pre-registration completed (planned: before final submission)
- [ ] PRISMA 2020 checklist completed (Appendix A)
- [ ] Inter-coder reliability κ ≥ 0.70 reported
- [ ] `metafor` R package version documented
- [ ] Publication bias diagnostics (Egger test, trim-and-fill) reported in §4.4

---

## Source Files

Main markdown: `p6/p6_meta_manuscript_en.md`
Study database: `p6/p6_study_database_coded.md`
R scripts: `p6/scripts/`
Replication: `p6/tools/`


---

## ⚠ TARGET JOURNAL — under review (2026-06-02)

Per lfe-academic-reviewer Phase A1: package directory is `ibr_package/` but
manuscript header (line 5) says MIR; PRISMA checklist says MRQ. Three-way
contradiction must be resolved before submission. Default per NCS preference:
**MIR (Management International Review, Springer, Scopus Q1, ABS-3)** —
matches manuscript header and Emerald-vs-Springer abstract format better.

If MIR confirmed:
- Rename package folder to `mir_package/`
- Update cover letter to EiC Wiley → Springer Nature
- Update keywords/JEL for MIR (no JEL required) and PRISMA position

If MRQ confirmed (Management Review Quarterly):
- Convert structured abstract to MRQ format (typically structured)
- MRQ word cap ~12,000 — OK
- MRQ is Springer ABS-1, more receptive to single-coder mitigations

If IBR retained:
- Convert structured abstract to IBR unstructured narrative
- Cite Hunter-Schmidt + Geyskens (2009) (standard IB meta-analysis refs)
