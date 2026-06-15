# ⚠️ LEGACY — DO NOT USE FOR REPORTING

The CSVs in this folder (`p7_R_coefs.csv`, `p7_summary_focal.csv`,
`p7_R_turning_points.csv`, `p7_model_fit.csv`, …) are **legacy outputs** from an
earlier run of `p7/replication/02_run_p7_models.py` on the **pre-Japan sample
(N ≈ 84,910)**. They predate the canonical 50-economy frame and are internally
inconsistent with the dissertation's locked numbers — e.g. they report
M2 N = 84,910 and an M2 turning point far from the canonical value.

## Canonical P7 results (use these)
- **Source:** `data_wbes/analysis/p7_50econ_models.csv`
  (generator: `scripts/p7_run_50econ.py`).
- **Locked values:** M2 N = **81,022**, TP = **51.5%**; M5 N = **79,080**,
  TP = **43.6%**; per-ICRV turning points (Advanced ≈ 79%, Lower-mid-transition
  ≈ 43%, Emerging ≈ 35%, SIDS FIP). See `data_wbes/analysis/CANONICAL_NUMBERS.md`.
- **Verification:** `scripts/verify_all.py` (14/14) re-estimates these from the
  `.dta` microdata and confirms them.
- **Consolidated for submission:** `dist/figure_data/dissertation_results_data.xlsx`
  (sheet `P7_50econ_canonical`).

## To regenerate this folder (optional)
`02_run_p7_models.py` requires `statsmodels` and reads
`data_wbes/p7/p7_pooled_clean.csv`. It is a *secondary* pipeline; if regenerated,
cross-check its analytic N against the canonical 81,022 before using any value.
The publication-figure helper `writing_guides/generate_publication_figures.py`
also reads these legacy CSVs and should be repointed to the canonical source.
