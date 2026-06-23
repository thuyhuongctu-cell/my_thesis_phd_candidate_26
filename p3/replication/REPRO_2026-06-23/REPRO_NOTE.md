# P3 Vietnam — Reproduction Note (2026-06-23)

Reproduction run from the **committed raw WBES microdata** in `data_wbes/raw_dta/`
via the Python (statsmodels/pyreadstat) Stata-equivalent runner. No fabricated
numbers; everything below is printed by the script.

## Command run
```bash
python3 p3/replication/REPRO_2026-06-23/run_repro.py
```
This harness imports `build()` from `scripts/p3_dai_reproduce.py` (unchanged spec)
and additionally estimates the quadratic FSTS model (M2), the DAI-moderation model
(M4), and the DAI-level model (M6) per wave and pooled, with HC1 robust SEs.
Outputs: `estimates.csv` (model, term, coef, se, p, n).

Raw inputs (paths already correct in the runner — no broken/ephemeral path needed
repointing):
- `data_wbes/raw_dta/Vietnam-2009-full-data.dta`
- `data_wbes/raw_dta/Vietnam-2015-full-data.dta`
- `data_wbes/raw_dta/Vietnam-2023-full-data.dta`

## Headline reproduced (M2: lnLP ~ FSTSc + FSTSc2 + controls, HC1)

| Wave   | N (M4/DAI) | b1 (FSTSc) | b2 (FSTSc2) | Turning point |
|--------|-----------:|-----------:|------------:|--------------:|
| 2009   | 995 | +0.575  | −1.524*** | 35.6% |
| 2015   | 964 | +0.952* | −1.907*** | 37.0% |
| 2023   | 1014| +0.852  | −2.096*** | 33.3% |
| Pooled | 2973| +0.733* | −1.750*** | 34.8% |

(b1/b2 with stars per `estimates.csv`; b2 < 0 and significant in every wave →
inverted-U confirmed. b1 > 0 in every wave → ascending-then-descending shape.)

DAI level (M6, DAI_z coefficient):

| Wave   | DAI_z (M6) | p |
|--------|-----------:|--:|
| 2009   | +0.273 | <.001 |
| 2015   | +0.045 | .340 |
| 2023   | +0.153 | .001 |
| Pooled | +0.157 | <.001 |

## Match vs canonical target

Canonical P3 target (from the task brief / manuscript pattern):
inverted-U in FSTS; turning point in **39–46%** range; DAI positive moderation.

| Claim | Canonical | Reproduced | Match |
|-------|-----------|-----------|:-----:|
| Inverted-U shape (b2 < 0, sig.) | yes | yes, all waves (b2 −1.52 to −2.10, p ≤ .028) | **Y** |
| Ascending branch (b1 > 0) | yes | yes, all waves | **Y** |
| Turning point 39–46% | 39–46% | **33.3–37.0%** (pooled 34.8%) | **N** |
| DAI positive moderation (level) | positive | positive & sig. 2009/2023/pooled; n.s. 2015 | **Y (partial)** |
| DAI × FSTS interaction sig. | (curvature shift) | n.s. 2009/2015; sig. only 2023 (−1.097, p=.036) | weak |

### Discrepancy — turning point (NOT overwritten)
The reproduced turning points (33–37%) sit **below** the canonical 39–46% band
and below the values printed in `p3/replication/README.md` (40% / 44% / 46% /
39.7% pooled). This is **not** a coding error in this run — the committed
R-track output `p3/replication/data/p3_R_turning_points.csv` independently gives
**pooled M2 TP = 34.5%**, which matches this Python run (34.8%) almost exactly.

Most plausible cause is the documented `b1_d` employment-denominator difference:
the authoritative Stata do-files (`do/01_build_vietnam.do`, `do/02_run_models.do`)
define `lnLP` via a Stata-specific labour denominator and the DAI instrument that
the Python/R ports approximate with `ln(l1)`. The README itself flags that the
Python equivalent reproduces the *pattern* (inverted-U; TP ~39–46%) "but not the
exact magnitudes (the IV `b1_d` denominator differs)". The reproducible Python +
R magnitudes land ~5 points lower than the README's stated band.

**Action taken: none forced.** Numbers are reported as produced. Resolving the
39–46% vs 33–37% gap requires running the authoritative Stata do-files on the
licensed machine to confirm which denominator the locked manuscript numbers use.
Flagged for central review (see stale-artifacts list in the report).

### Cross-artifact coefficient divergence (flagged)
Pooled M2 (FSTSc, FSTSc2) differs across three committed artifacts:
- this run: (+0.733, −1.750), TP 34.8%
- `p3/replication/data/p3_R_coefs.csv` / `p3_R_turning_points.csv`: (+0.661, −2.152), TP 34.5%
- `p3/replication/coefs_main_models.csv` (feeds figures): (+0.984, −1.909)

The R track and this Python track agree closely; `coefs_main_models.csv` is the
outlier and appears to be from an earlier/divergent build (different sample
construction). It does not reproduce from raw with the current spec.
