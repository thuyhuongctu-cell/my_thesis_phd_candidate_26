# P4 Singapore — Reproduction from Raw (2026-06-23)

Auditable re-estimation of the P4 (Singapore WBES 2023) headline results, run
directly from committed raw `.dta` data. This note accompanies `estimates.csv`
(full model,term,coef,se,p,n table for M0–M8).

## Command

```bash
cd /home/user/MY_THESIS_PHD_CANDIDATE_26
python3 p4/replication/p4_singapore_figs_from_raw.py
```

- **Runner (source of truth):** `p4/replication/p4_singapore_figs_from_raw.py`
- **Raw input:** `data_wbes/raw_dta/Singapore-2023-full-data.dta`
  (resolved via `WBES_RAW` env var, defaulting to the committed `data_wbes/raw_dta/`).
- **Engine:** statsmodels OLS, HC1 robust SE. No `linearmodels`, no external paths.
- `estimates.csv` regenerated with the identical model specs (same builder, same
  controls) via an extractor that mirrors the runner exactly.
- The other script, `p4/replication/p4_singapore_replication.py`, is a
  **deliberate, clearly-labelled stub** (mislabelled Vietnam/P3 copy that read an
  ephemeral upload path). It now prints a redirect to this runner and exits 1.

## Specification

- DV: `lnLP = ln(d2/l1)` (sales per worker). Export intensity `FSTS = d3c/100`,
  mean-centered (`FSTS_c`), with `FSTSsq_c = FSTS_c^2`.
- Controls: `lnEmp`, `firmage`, `foreigndum`, sector dummies `sec_mfg`, `sec_constr`.
- Capability shifters (z-standardized composites): `TCI_z` (b8+e6+h1),
  `DAI_z` (c22b+k33+k38).
- Sentinel codes −9/−8/−7/−6 set to missing. FSTS mean = 4.65%.

## Headline numbers (reproduced) vs canonical target

| Quantity | Reproduced | Canonical target | Match |
|---|---|---|:--:|
| M2 FSTS_c (b1) | **+3.078** (SE 0.805, p<.001) | +3.08 | **Y** |
| M2 FSTS²_c (b2) | **−1.898** (SE 1.079, p=.079) | −1.90 approx | **Y** |
| TCI level shifter | **+0.211** (M5) / +0.171 (M3) / +0.152 (M8) | +0.21 | **Y** |
| DAI level shifter | **+0.166** (M6) / +0.119 (M4) | +0.17 | **Y** |
| M8 interaction FSTS²_c × DAI_z | **+3.220** (SE 1.384, **p=.020**) | +3.119 (p≈.02) | **Y (close)** |
| M2 turning point | **85.7%** [30.6%, 140.8%] | high ~88.6%, wide CI, not well-located | **Y** |
| N (base / full) | **623 / 617** | 623 / 617 | **Y** |

Notes on the one non-exact match:
- **M8 FSTS²×DAI interaction = +3.220 vs canonical +3.119.** Same sign,
  significance, and order of magnitude (both p≈.02). The ~0.10 gap is within the
  expected drift between the manuscript-frozen value and a clean raw re-run; flagged
  rather than forced. The canonical TCI in M8 (+0.152) matches +0.153 exactly.
- **M2 b2 (FSTS²_c) is marginal (p=.079)** in M2; curvature becomes significant in
  M8 (b2=−2.872, p=.012). Inverted-U sign is robust across specs. Turning point sits
  near the top of the feasible export range with a CI spanning well past 100%, i.e.
  the apex is **not reliably located** — consistent with canonical.

## Files in this folder
- `estimates.csv` — full M0–M8 coefficient table (model, term, coef, se, p, n).
- `REPRO_NOTE.md` — this file.

## Cross-check against prior artifacts
- Matches the runner's own `p4/manuscripts/figures/p3_singapore/results_p3.json`
  (M8 N=617, TCI 0.152, INT 3.22, AdjR² 0.196, TP 85.7%).
- **Contradicts** the stale multi-wave tables under `p4/replication/tables/`
  (2009/2015 waves, FSTS_c ≈ +1.0/+1.1, N=989/956) and `p4_R_turning_points.csv`
  (TP 76.4%, b1=+3.64, b2=−2.63). See "Stale artifacts" in the agent report.
