# ⚠️ DEPRECATED — superseded Japan-inclusive run (different spec)

This folder is the **Japan-inclusive 50-economy** legacy run
(`p7_audit.json`: `n_countries: 50` incl. Japan + Azerbaijan + Timor,
`n_total: 78,810`, `n_country_years: 111`, models M0–M11). It was the closest
predecessor to the canonical 50-economy frame, but it was produced by a
**different builder/specification** than the canonical runner and must not be
used for reporting:

- It estimates on raw `lp` levels (Intercept ≈ 14.56), **not** the canonical
  within-wave z-scored `lp_z`.
- Its **M2 turning point = 56.7%**, which does **NOT** reproduce the canonical
  **51.5%**; its N (78,810) and pair count (111) also differ from both the
  master-locked frame (81,022 / 103 pairs) and the canonical raw build.

So even though it is "50 economies incl. Japan," its headline numbers diverge
from the locked dissertation values. The authoritative Japan-inclusive 50-economy
estimates come from the canonical runner, not this folder.

## Canonical P7 source of truth
- `data_wbes/analysis/CANONICAL_NUMBERS.md` (master-locked):
  M2 N = **81,022**, TP **51.5%**; M5 N = **79,080**, TP **43.6%**;
  Group IV (Lower_mid_transition) TP **43.0%**; SIDS no inverted-U.
- Runner: `scripts/p7_run_50econ.py` (= `dist/osf/P7_capstone/code/p7_run_50econ.py`),
  output `data_wbes/analysis/p7_50econ_models.csv`.
- Latest auditable re-estimation (raw build, reproduces TPs + three zones):
  `p7/replication/REPRO_2026-06-23/`.

Flagged for central review for **deletion** (superseded by REPRO_2026-06-23 +
the canonical runner output).
