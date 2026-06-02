# P9 Thailand — JED Submission Package

## Journal of Economics and Development — Emerald Publishing on behalf of NEU

**Manuscript:** "Cross-Wave Stability of the Internationalisation–Performance Relationship in Thai Firms: ASEAN Peer Evidence Across the COVID–RCEP Transition"

**Target journal:** Journal of Economics and Development (JED) — Emerald Publishing on behalf of National Economics University, Vietnam (Scopus + WoS indexed; IF 4.3; CiteScore 8.5; Diamond OA — no APC)

**Status:** ⚠ **DRAFT INFRASTRUCTURE — Empirical analysis pending**

**Authors:** Đỗ Thùy Hương & PGS.TS. Phan Anh Tú (School of Economics, Can Tho University)

---

## ⚠ Status: TBD items

Following items pending NCS running Stata analysis on local machine:
- [ ] Run `replication/do/01_build_thailand.do` to build analytic .dta files
- [ ] Run `replication/do/02_run_models.do` to estimate models
- [ ] Fill in Findings section in `p9_thailand_en_clean.md` with actual coefficient values
- [ ] Render figures from CSV outputs (use existing `generate_p_figures.py` pattern from P3/P4/P5)
- [ ] Finalize abstract Findings + Originality/value sentences based on actual results
- [ ] Build Excel replication workbook via `scripts/build_replication_xlsx.py`

---

## ⚠ Concern: 3 papers same author at JED

This would be the **3rd paper** by NCS targeting JED (along with P3 Vietnam and P8 SIDS).
Editor risk: "self-clustering" → may desk-reject 1 of 3.

**Mitigation strategies**:
1. **Space out timing**: Submit P3 first → wait for editor acknowledgement (~2 weeks) → Submit P8 → wait for decision (~10 weeks) → Submit P9 Thailand
2. **Alternative**: Submit P9 Thailand to **JABES** (UEH HCM, also Emerald Scopus Q1) instead of JED — reduces self-clustering risk
3. **Disclose proactively in cover letter**: "Companion papers on Vietnam and Pacific SIDS are under consideration at this journal; the present Thailand paper offers ASEAN-peer comparative evidence"

---

## Package Contents (when complete)

| File | Description | Status |
|------|-------------|--------|
| `01_manuscript_blinded.docx` | Main manuscript anonymised | ⏳ TBD |
| `02_title_page.docx` | Title page non-anonymous | ✓ Draft ready |
| `03_cover_letter.docx` | Cover letter to JED EiC | ✓ Draft ready |
| `figures/figure_1_conceptual_model.png` | Conceptual model | ⏳ TBD (render from script) |
| `figures/figure_2_predicted_curves.png` | I-P curves by wave | ⏳ TBD (run Stata first) |
| `figures/figure_3_turning_points.png` | Turning points + 95% CI | ⏳ TBD (run Stata first) |

---

## JED Submission Checklist (when ready)

⚠ **CRITICAL — Submission URL**: Email `submission@ktpt.edu.vn` HOẶC portal `https://js.ktpt.edu.vn` (NEU OJS). KHÔNG dùng `mc.manuscriptcentral.com/jed` — URL đó dẫn về Sage's "Journal of Environment and Development".

- [ ] Confirm correct ScholarOne URL via email submission@ktpt.edu.vn
- [ ] Register / log in to confirmed portal
- [ ] Select "Submit a Manuscript"
- [ ] **Manuscript type:** Research Article
- [ ] **Keywords**: internationalisation–performance; export intensity; threshold stability; ASEAN; Thailand; RCEP; COVID-19
- [ ] **JEL codes:** F23, O33, D22, L25, O53
- [ ] **Abstract** (≤250 words structured Emerald format)
- [ ] Upload 01_manuscript_blinded.docx → Main Manuscript (anonymous)
- [ ] Upload 02_title_page.docx → Title Page (non-anonymous)
- [ ] Upload 03_cover_letter.docx → Cover Letter
- [ ] Upload figures 1, 2, 3
- [ ] Confirm corresponding author = Phan Anh Tú (patu@ctu.edu.vn)
- [ ] Confirm no conflict of interest
- [ ] Confirm no simultaneous submission
- [ ] Run Paperpal Preflight AI check (recommended)

---

## Manuscript Statistics (TBD)

| Item | Value |
|------|-------|
| Word count (main text, target) | ~7,500 words |
| Abstract | ≤ 250 words (structured Emerald) |
| Tables | 4 |
| Figures | 3 |
| Firms (2016 wave) | 705 (PICS3 schema) |
| Firms (2025 wave) | 766 (BREADY/BEE schema) |
| Pooled N | 1,471 |
| ICRV context | Upper-Middle (Group III) — same as China P5 |
| Primary result | [TBD pending estimation] |

---

## Replication Pipeline

**Stata workflow (run on NCS local machine with Stata 17+):**

```stata
cd p9_thailand/replication/do/
do 01_build_thailand.do      // Build analytic .dta from WBES raw_dta
do 02_run_models.do          // Estimate M0..M5, Lind-Mehlum, Paternoster z
```

**Outputs:**
- `replication/data/thailand_2016_analytic.dta`
- `replication/data/thailand_2025_analytic.dta`
- `replication/data/thailand_pooled_analytic.dta`
- `replication/results/p9_coefs_main_models.csv`
- `replication/results/p9_moderators.csv`
- `replication/results/p9_turning_points.csv`
- `replication/results/p9_paternoster.csv`

**Then:**
1. NCS fills `p9_thailand_en_clean.md` Findings section with actual numbers
2. Render figures via Python script (use `p5/replication/generate_p5_figures.py` as template)
3. Rebuild DOCX via pandoc
4. Build Excel workbook via `scripts/build_replication_xlsx.py` (add P9 entry to PAPERS dict)
5. Embed figures via `scripts/embed_figures_in_xlsx.py`

---

## Source Files

- Main markdown: `p9_thailand/p9_thailand_en_clean.md`
- Stata pipeline: `p9_thailand/replication/do/`
- Outputs: `p9_thailand/replication/results/`
- Figures: `p9_thailand/replication/figures/`
- Submission package: `p9_thailand/submission/jed_package/`

---

*Generated 2026-06-02 (infrastructure only — empirical analysis pending NCS Stata run).*
