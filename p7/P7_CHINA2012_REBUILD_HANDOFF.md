# P7 China-2012 Rebuild — Handoff for Authoritative Re-run

**Status:** parser bug fixed (committed); canonical rebuild + thesis renumber **handed to the candidate** to run on the *authoritative* pipeline.
**Date:** 2026-06-22 · **Branch:** claude/phd-thesis-review-L9Gml

---

## 1. What was wrong and what is already fixed

The China 2012 full WBES wave (`data_wbes/raw_dta/China-2012-full-ES-N2700-data.dta`,
N = 2,700) was silently dropped from P7 (and CD1) rebuilds by fragile filename heuristics
that mishandle the `ES-N2700` sample-size token:

- `scripts/wbes_canon.py` — `ES-N####` collapses to `esn`, which broke the contiguous
  `fulldata` test **and** matched the `_NONSTANDARD` `esn` tag → `standard=False`.
- `p7/replication/01_build_p7_dataset.py` — `is_panel_filename` read `2700` as a second
  year → file misclassified as a multi-wave panel.

**FIXED and committed** (commit `31b7895`): both parsers now strip the `N####` size token
and accept only real `19xx/20xx` year tokens. Verified: `wbes_canon.parse(...)` now returns
`standard=True, panel=False` for the China 2012 file; standard waves and informal/micro/panel
exclusions are unaffected.

The exploratory canonical-CSV rebuild was **reverted** (commit `5ab1efa`) because it was
produced by re-running the *committed Python* pipeline, which does **not** reproduce the
dissertation's authoritative descriptive numbers (see §4). Re-run on the authoritative
pipeline instead.

---

## 2. Measured impact (reference only — from the committed Python pipeline)

Re-running `01_build_p7_dataset.py` + `scripts/p7_run_50econ.py` with the fix produced:

| Quantity | Before (committed CSV) | After (with China 2012) |
|---|---|---|
| M2 (FSTS+FSTS², FE) N / TP | 80,814 / 51.45% | **83,505 / 51.37%** |
| M5 (+controls, FE) N / TP | 78,874 / 43.55% | **81,457 / 43.82%** |
| Upper-mid regime N / TP | 12,055 / 55.02% | **14,638 / 53.64%** |
| pooled classification rows | 96,384 | 99,084 |
| Other ICRV regimes | — | unchanged |

**Key takeaway: the turning point is essentially unchanged (M5 43.55% → 43.82%).**
The inverted-U, the ~44% turning point, and the three-zone institutional gradient are all
robust to including China 2012. Only the sample sizes grow (~+2,700) and the Upper-mid
regime turning point shifts ~1.4 pp.

> These figures are **indicative**, from the committed Python scripts. Treat the values from
> your authoritative pipeline as canonical (they differ from these by a small pre-existing
> drift — see §4).

---

## 3. Steps to complete (authoritative pipeline)

1. Re-run the **authoritative** P7 and CD1 build/estimation that originally produced the
   thesis numbers (M2 N = 81,022; M5 N = 79,080; pool 96,415; frame 88,869; ~10,350
   unclassified). The committed Python scripts below are a cross-check, **not** confirmed to
   be the authoritative source:
   ```
   python3 p7/replication/01_build_p7_dataset.py --raw-dir data_wbes/raw_dta --out-dir data_wbes/p7
   python3 scripts/p7_run_50econ.py
   python3 scripts/cd1_descriptives_pipeline.py
   ```
2. Read the new authoritative numbers (M2/M5 N + TP, classification pool, analytic frame,
   Table 4.1 per-ICRV breakdown, unclassified count).
3. Renumber the files in §5 from the old values to the new authoritative values.
4. Re-verify internal consistency (thesis ↔ CD1 ↔ P7 manuscript ↔ CSVs) and the OSF /
   replication package.

---

## 4. Why the descriptive numbers were NOT auto-renumbered (provenance gap)

The committed scripts give **different** descriptive totals than the thesis, so the thesis's
descriptive numbers come from a pipeline/version not reproducible here:

| Quantity | Thesis | committed `pooled_clean` | committed CD1 descriptives |
|---|---|---|---|
| Classification pool | 96,415 | 96,384 (≈, drift 31) | — |
| Analytic frame | 88,869 | — | 87,987 |
| Unclassified | ~10,350 | 3,531 (**~3× off**) | — |
| Lower-mid n (Table 4.1) | (table) | 47,664 | 45,003 |

The ~3× discrepancy in the unclassified count and the per-group disagreement show the
descriptive pool/Table 4.1 were built by a different process. Auto-replacing them with
committed-script numbers would inject wrong values. The P7 **regression** numbers (M2/M5 N,
TP), by contrast, map cleanly to `scripts/p7_run_50econ.py`.

There is also a pre-existing drift in the regression N (thesis M2 = 81,022 vs committed CSV
= 80,814, ~0.26%), confirming the thesis was written from a slightly different run than the
committed CSVs even before this issue.

---

## 5. Files containing P7 numbers to renumber (~18)

**Old values to find:** `81.022`/`81,022` (M2 N), `79.080`/`79,080` (M5 N),
`88.869`/`88,869` (frame), `96.415`/`96,415` (pool), `43,6%`/`43.6%` (M5 TP),
`51,5%`/`51.5%` (M2 TP), `55,02`/`55,0%` (Upper-mid TP), and the Table 4.1 per-ICRV column.

- thesis/00_phan_dau_vi.md
- thesis/chuong_1_gioi_thieu_vi.md
- thesis/chuong_2_tong_quan_tai_lieu_vi.md
- thesis/chuong_3_phuong_phap_vi.md
- thesis/chuong_4_ket_qua_vi.md  *(Table 4.1 + §4.6)*
- thesis/chuong_5_ket_luan_de_xuat_vi.md
- thesis/11_dissertation_positioning_vi.md
- thesis/99_MASTER_PLAN_2026.md
- thesis/appendix_A_data_harmonisation_en.md
- thesis/phu_luc_A_hop_nhat_du_lieu_vi.md
- thesis/en/chapter_1_introduction_en.md
- thesis/en/abstract_en.md
- thesis/slides/defense_slides_vi.tex
- thesis/slides/defense_qa_vi.md
- chuyen_de/cd1/00_cd1_ctu_final_vi.md
- chuyen_de/cd2/00_cd2_ctu_final_vi.md
- p7/submission/ibr_package/01_manuscript_blinded.md
- p7/submission/ibr_package/04_manuscript_latex.tex
- chuyen_de/cd1/figures/make_cd1_descriptive_figs.py  *(hard-coded figure values)*
- chuyen_de/cd2/figures/cd2_fig41_conceptual_model.puml  *(hard-coded figure values)*

> Note: when checking `43.6%` / `51.5%`, confirm each occurrence is the P7 turning point
> (some percentages in the same files refer to other statistics) before changing.

---

## 6. What is safe to keep as-is

The substantive P7 conclusions (inverted-U; turning point ≈ 44%; three-zone gradient;
FIP at SIDS) are unchanged by including China 2012, so no narrative/interpretation needs
rewriting — only the numeric values in §5.
