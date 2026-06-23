# ⚠️ DEPRECATED — non-canonical partial-sample run

The CSVs here (`p7_summary_focal.csv`, `p7_coefs_all_models.csv`,
`p7_model_fit.csv`, `p7_audit.json`) come from a **partial 34-economy /
68,957-firm** build (`p7_audit.json`: `n_countries: 34`, `n_country_years: 72`,
no Japan, no Azerbaijan). This is neither the canonical 50-economy frame nor a
clean superset — it is an intermediate "expanded" run that predates the locked
numbers.

**Do NOT report any value from this folder.**

## Canonical P7 source of truth
- `data_wbes/analysis/CANONICAL_NUMBERS.md` (master-locked):
  M2 N = **81,022**, TP **51.5%**; M5 N = **79,080**, TP **43.6%**;
  Group IV (Lower_mid_transition) TP **43.0%**.
- Runner: `scripts/p7_run_50econ.py` (= `dist/osf/P7_capstone/code/p7_run_50econ.py`).
- Latest auditable re-estimation: `p7/replication/REPRO_2026-06-23/`.

Flagged for central review for **deletion**.
