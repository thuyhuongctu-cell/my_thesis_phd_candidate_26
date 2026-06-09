# P9' India, MIR Submission Package

## Management International Review, Springer Nature

**Manuscript:** "Cross-Wave Stability of the Internationalisation–Performance Threshold in Indian Firms: Digital and Technological Capability Moderation Across a Decade of Institutional Transformation"

**Primary target journal:** Management International Review (MIR), Springer Nature (Scopus Q1; IF 6.0+; ABS-3)
**Alternate target:** International Journal of Emerging Markets (IJOEM), Emerald Publishing (Scopus Q1; IF 3.0+)

**Status:** ✅ **Empirical analysis complete** — manuscript, tables, and figures finalised; pending author-only pre-submission steps (iThenticate, OSF/replication-workbook, portal upload).

**Authors:** Đỗ Thùy Hương & PGS.TS. Phan Anh Tú (School of Economics, Can Tho University)

---

## Data Availability, VERIFIED ✓

All three India WBES waves extracted to `data_wbes/raw_dta/`:

| Wave | File | N firms | Schema | Key vars |
|---|---|---:|---|---|
| 2014 | `India-2014-full-data.dta` | 9,281 | PICS3 standardized | d2, FSTS, TCI, c22b |
| 2022 | `India-2022-full-data.dta` | 9,376 | BEE intermediate | d2, FSTS, TCI, c22b |
| 2025 | `India-2025-full-data.dta` | 10,479 | BREADY full | d2, n3, FSTS, TCI, c22b, **k33 (Tier-2 DAI)** |

**Total pooled raw N = 29,136 firm-year observations**, largest sample in the portfolio.

**Critical discovery**: India 2025 BREADY includes `k33` (% sales via e-payment) → enables **DAI Tier-2 moderation test**, the public-vs-private digital infrastructure distinction.

---

## Strategic Significance vs P9 Thailand

| Criterion | P9 Thailand | **P9' India** |
|---|:-:|:-:|
| Institutional gap-filling | ❌ Cluster with China/Vietnam | ✅ **Lấp 6 dimensions** (democratic + federal + common-law + South Asia + Hindu/Muslim + 2nd-largest population) |
| Cross-wave durability stress test | Moderate (COVID + RCEP) | **Extreme** (demonetisation + GST + IBC + UPI + PLI + COVID + Atmanirbhar Bharat) |
| Digital quasi-experiment | ❌ Không có | ✅ **UPI 2016 launch → 12B txn/month by 2024** |
| Sample size | 1,471 obs | **~29,000 obs (~20× larger)** |
| Existing scaffolding | Không | ✅ Book chapter (Do & Phan 2025 IntechOpen) |
| Target journal ceiling | JED/JABES Q1 | **MIR (Springer ABS-3) hoặc IJOEM Q1** |
| Self-clustering risk | Cao (3 papers JED) | ✅ Thấp (different publisher) |
| TC Scopus potential | +10 | +10-12 (MIR có higher impact) |

→ **P9' India là phương án rõ ràng hơn về mọi mặt** so với P9 Thailand.

---

## Status: completed vs. author-only remaining

Analysis pipeline complete:
- [x] Build analytic samples for all 3 waves (`replication/data/india_{2014,2022,2025}_analytic.csv`)
- [x] Estimate M0..M5 + Lind–Mehlum U-test + Paternoster cross-wave z (`replication/results/`)
- [x] Findings section filled with actual coefficient values (manuscript §Results)
- [x] Render all four figures (`replication/figures/` → copied into `figures/`)
- [x] Finalise abstract Findings + Originality/value from actual results
- [x] Target decided: **MIR primary, IJOEM backup**

Author-only remaining (cannot be automated):
- [ ] Run iThenticate similarity check against the book chapter
- [ ] Build Excel replication workbook (add P9 India entry to PAPERS dict)

---

## Package Contents (when complete)

| File | Description | Status |
|------|-------------|--------|
| `01_manuscript_blinded_full.md` | Main manuscript anonymised (real results) | ✓ Complete |
| `02_title_page.docx` | Title page non-anonymous | ✓ Ready |
| `03_cover_letter.docx` | Cover letter to MIR EiC | ✓ Ready |
| `BOOK_CHAPTER_DIFFERENTIATION.md` | Self-plagiarism management memo | ✓ Complete |
| `figures/figure_1_conceptual_model.png` | Conceptual model | ✓ Complete |
| `figures/figure_2_predicted_curves.png` | I-P curves by wave | ✓ Complete |
| `figures/figure_3_turning_points.png` | Turning points + 95% CI | ✓ Complete |
| `figures/figure_4_upi_timeline.png` | UPI quasi-experiment timeline | ✓ Complete |

---

## MIR Submission Checklist (when ready)

⚠ Verify Springer Nature ScholarOne URL for MIR before submission.

- [ ] Register / log in to MIR submission portal (Springer Nature)
- [ ] Select "Submit a Manuscript"
- [ ] **Manuscript type:** Research Article
- [ ] **Keywords**: internationalisation–performance; export intensity; threshold stability; India; UPI; digital capability; technological capability; institutional transformation; emerging markets; CDCM
- [ ] **JEL codes:** F23, O33, D22, L25, O53, O25
- [ ] **Abstract** (standard MIR format)
- [ ] Upload 01_manuscript_blinded.docx → Main Manuscript (anonymous)
- [ ] Upload 02_title_page.docx → Title Page (non-anonymous)
- [ ] Upload 03_cover_letter.docx → Cover Letter
- [ ] Upload figures 1, 2, 3, 4
- [ ] **Disclose prior related work** in cover letter (book chapter DOI 10.5772/intechopen.1011012) ← critical
- [ ] Confirm corresponding author = Phan Anh Tú (patu@ctu.edu.vn)
- [ ] Confirm no conflict of interest
- [ ] Confirm no simultaneous submission

---

## Manuscript Statistics

| Item | Value |
|------|-------|
| Word count (main text) | ~8,500 words |
| Abstract | ≤ 250 words |
| Tables | 5 |
| Figures | 4 |
| Firms (2014 wave) | 9,281 raw / 8,941 complete-core |
| Firms (2022 wave) | 9,376 raw / 9,300 complete-core |
| Firms (2025 wave) | 10,479 raw / 10,476 complete-core |
| Pooled raw N | 29,136 |
| Pooled analytic N | 28,717 |
| ICRV context | Lower-Middle (Group IV), same as Vietnam P3 |
| Primary result | Threshold dissolution: inverted-U in 2014 (TP 61.8%) and 2022 (TP 40.7%) collapses to a monotone-negative slope in 2025 (curvature p = .42); Paternoster cross-wave z rejects coefficient equality (FSTS z = −7.94; FSTS² z = +4.17, both p < .0001) |
| Prior author work | Do & Phan 2025 IntechOpen DOI 10.5772/intechopen.1011012 |

---

## Replication Pipeline

**Stata workflow:**

```stata
cd p9_india/replication/do/
do 01_build_india.do      // Build 2014, 2022, 2025, pooled analytic .dta
do 02_run_models.do       // Estimate M0..M5 + tests
```

**Outputs:**
- `replication/data/india_2014_analytic.dta`
- `replication/data/india_2022_analytic.dta`
- `replication/data/india_2025_analytic.dta`
- `replication/data/india_pooled_analytic.dta`
- `replication/results/p9_india_coefs_main_models.csv`
- `replication/results/p9_india_moderators.csv`
- `replication/results/p9_india_turning_points.csv`
- `replication/results/p9_india_paternoster.csv`
- `replication/results/p9_india_3wave_pooled.csv`

**Then:**
1. NCS fills `p9_india_en_clean.md` Findings section with actual numbers
2. Render figures via Python script (use P5 template)
3. Rebuild DOCX via pandoc
4. Run iThenticate against book chapter PDF
5. Update Excel workbook (add P9' India entry to PAPERS dict)

---

## Source Files

- Main markdown: `p9_india/p9_india_en_clean.md`
- Book chapter differentiation: `p9_india/BOOK_CHAPTER_DIFFERENTIATION.md`
- Stata pipeline: `p9_india/replication/do/`
- Outputs: `p9_india/replication/results/`
- Figures: `p9_india/replication/figures/`
- Submission package: `p9_india/submission/mir_package/`

---

*Updated 2026-06-09 (empirical analysis complete: results, tables, and figures finalised).*
