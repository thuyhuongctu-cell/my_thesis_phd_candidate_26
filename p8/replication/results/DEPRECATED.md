# DEPRECATED — superseded P8 results (do NOT use)

These files carry the **OLD / superseded** P8 numbers from the pre-redesign "Forced
Internationalization Penalty (FIP)" draft and must NOT be cited as the P8 result.

| File | Stale content | Issue |
|---|---|---|
| `p8_R_summary.csv` | N = 1,469; M1 β = −0.404; bivariate −1.596; `penalty_confirmed: YES` | Wrong N and harmonisation; presents a confirmed negative penalty |
| `p8_R_coefs.csv` | M_bivariate β = −1.596; M_yearFE β = −1.236 | Same superseded build |

**Canonical / live result (redesign, dissolution framing):** N = **1,450** / 7 clusters;
linear FSTS_c slope **−0.085** (wild-cluster p ≈ .656); quadratic FSTS_c **−0.567** /
FSTS_c² **+0.696** (wild p ≈ .088 / .082) → the inverted-U **dissolves**. The β = −1.339
FIP is a superseded **limiting case only**, never the headline.

**Reproduce the live result:** `python3 p8/replication/build_and_run_p8_7pacific.py`
(see `p8/replication/REPRO_2026-06-23/REPRO_NOTE.md`).

**Recommendation:** DELETE this `p8/replication/results/` directory. Retained here only
to flag it; it is fully superseded by `p8/replication/REPRO_2026-06-23/` and
`p8/replication/reanalysis_7pacific/p8_7pacific_models.csv`.
