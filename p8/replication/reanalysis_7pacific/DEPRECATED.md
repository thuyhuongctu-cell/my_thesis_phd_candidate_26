# Partially DEPRECATED — superseded FIP artifacts in this directory

## KEEP (current)
- `p8_7pacific_models.csv` — regenerated 2026-06-23 by `build_and_run_p8_7pacific.py`.
  Carries the **live dissolution result**: M1 fsts_c −0.085 (p_wild .656); M2 −0.567 /
  +0.696 (p_wild .088 / .082). This is the source of truth in this folder.

## DELETE / IGNORE (superseded — OLD −1.339 FIP build)
| File | Stale content |
|---|---|
| `p8_R_summary.csv` | N_total = 959; M1 β = **−1.339**; FIP-confirmed framing |
| `p8_R_coefs.csv` | same N = 959 FIP build |
| `p8_7pacific_coefs.csv` | yet another superseded variant (N = 515; M1 fsts_c +0.022) |
| `01_p8_run_models_R_7pacific.R` | R driver encoding the −1.339 FIP analysis; replaced by the pure-Python `build_and_run_p8_7pacific.py` (no `linearmodels`, wild-cluster bootstrap) |
| `run_p8_7pacific.py` | early Python runner; superseded by `build_and_run_p8_7pacific.py` |

The β = −1.339 FIP is a superseded **theoretical limiting case only**, never the P8
headline. Headline = dissolution at **N = 1,450** (slope ≈ 0; curvature positive, marginal).

**Recommendation:** delete the five files above; keep only `p8_7pacific_models.csv`.
See `p8/replication/REPRO_2026-06-23/REPRO_NOTE.md`.
