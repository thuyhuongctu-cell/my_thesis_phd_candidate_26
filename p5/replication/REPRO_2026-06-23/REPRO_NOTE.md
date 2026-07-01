# P5 China — Reproduction Note (2026-06-23)

Reproducibility hardening run for study **P5 (China)**. Re-estimated from the
committed raw WBES `.dta` files; every headline matches the single source of
truth `data_wbes/analysis/CANONICAL_NUMBERS.md`.

## Source of truth

- Canonical: `data_wbes/analysis/CANONICAL_NUMBERS.md` → P5 row: N pooled = 4,544
  (2012: 2,610; 2024: 1,934).
- Cross-check: `reviews/REPLICATION_CROSSCHECK_2026-06-23.md` (P5 marked ✅ khớp).

## Raw inputs (committed)

- `data_wbes/raw_dta/China-2012-full-ES-N2700-data.dta` (2,700 × 287)
- `data_wbes/raw_dta/China-2024-full-data.dta` (2,189 × 339; 217 panel firms)

## Commands

```bash
# 1. Audit-N + per-wave turning points (writes audit_N_all.csv, audit_N_mfg.csv)
cd data_wbes/raw_dta
WBES_RAW="$(pwd)" python3 ../../p5/replication/python/build_and_run.py

# 2. Full estimates table incl. POOLED all-frame M2 + inverted-U b2 (estimates.csv)
python3 p5/replication/REPRO_2026-06-23/make_estimates.py

# 3. (optional) Full M0..M8 + Paternoster cross-wave z-test
python3 p5/replication/python/full_models.py

# 4. (optional) Three-way Tech×wave moderation + joint F-tests
python3 p5/replication/python/three_way_moderation.py
```

All scripts now default to `data_wbes/raw_dta/` via a `WBES_RAW` env override
(see "Path fixes" below); no manual path export is required.

## Headline results vs canonical

Model = M2 (lnLP ~ FSTS + FSTS² + lnEmp + firmage + foreigndummy [+ wave2024 when
pooled]), OLS with HC1 robust SEs. Turning point = −b1 / (2·b2).

| Spec | Reproduced TP | N | Canonical TP | Match |
|---|--:|--:|--:|:--:|
| All-frame, **pooled** | **48.78%** | 4,544 | ≈48.78% | ✅ Y |
| All-frame, 2012 | 49.37% | 2,610 | 49.37% | ✅ Y |
| All-frame, 2024 | 47.19% | 1,934 | 47.19% | ✅ Y |
| Manufacturing, 2012 | 42.31% | 1,656 | 42.31% | ✅ Y |
| Manufacturing, 2024 | 29.65% | 1,062 | 29.65% | ✅ Y |

**Sample sizes (pooled all-frame):** N = 4,544 (2012: 2,610; 2024: 1,934) — exact
match to canonical.

**Inverted-U (b2 = FSTS² coefficient), all-frame:**

| Spec | b2 | SE | p | b2 < 0 |
|---|--:|--:|--:|:--:|
| pooled | **−1.8289** | 0.3753 | ≈1e-06 (< .001) | ✅ |
| 2012 | −2.0919 | 0.4345 | ≈1e-06 | ✅ |
| 2024 | −1.5873 | 0.7117 | 0.026 | ✅ |

Canonical target: inverted-U b2 < 0 (~−1.84, p < .001). Reproduced pooled b2 =
**−1.8289** ✅.

## Path fixes applied (step 1)

`p5/replication/python/build_and_run.py` already defaulted to the repo's
`data_wbes/raw_dta/`. The two companion scripts still pointed at ephemeral
upload filenames (`China2012fullESN2700data.dta` / `China2024fulldata.dta`, no
hyphens, no directory) and would fail to load from the repo. Repointed both to
the same `WBES_RAW` default + hyphenated committed filenames:

- `p5/replication/python/full_models.py`
- `p5/replication/python/three_way_moderation.py`

Both now run with no env vars and reproduce pooled TP 48.78% / N 4,544.

## Files in this snapshot

- `estimates.csv` — long-format estimates (model, term, coef, se, p, n) for all
  six M2 specs (all/mfg × 2012/2024/pooled).
- `audit_N_all.csv`, `audit_N_mfg.csv` — sample-size audit ladders.
- `make_estimates.py` — generator (imports `build_and_run.py` as the single build).
- `make_table2.py` — full Table 2 generator (coef, HC1 SE, p, stars, R², F, N,
  delta-method turning point + 95% CI) for all-frame 2012/2024/pooled; the
  authoritative source for the IJOEM manuscript's Table 2.
- `three_way_moderation.csv` — moderation coefficients + joint F-tests.
- `run_console.txt` — captured console output of the runs.

## Table 2 reconciliation (manuscript sync)

The IJOEM manuscript's Table 2 previously carried stale main-model coefficients
(e.g. FSTS +1.28/+1.19/+1.24, FSTS² −1.53/−1.55, lnEmp +0.31, R² .142–.179)
that matched neither `estimates.csv` nor the table's own (correct) turning
points — recomputing TP from the printed β gave 41.8% rather than the stated
49.4%. The turning points (49.4/47.2/48.8%) and N (2,610/1,934/4,544) were
already canonical. Table 2 and the β-prose were re-synced to `make_table2.py`
output (FSTS +2.07/+1.50/+1.78, FSTS² −2.09/−1.59/−1.83, lnEmp −0.10/+0.12/+0.00,
R² .020/.053/.054); the 2024 Lind–Mehlum u-test is p = .029 (not < .001). The
inverted-U narrative, turning points, and figures are unchanged.

## Integrity

All coefficient values are the literal output of the estimation scripts on the
committed raw data. Table 2 now matches `estimates.csv` / `make_table2.py`.
