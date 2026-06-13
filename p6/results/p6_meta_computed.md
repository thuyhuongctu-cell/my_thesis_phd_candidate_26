# P6 three-level meta-analysis — FROZEN computed results

Source: `p6/results/forest_data.csv` — k=238 studies, K=288 effect sizes. Reproducible via `scripts/p6_meta_analysis.py`.

Model: three-level random-effects on Fisher-z; REML variance components; GLS pooling; Wald Q_M for moderators. All values below are computed, not placeholders.

## Baseline pooled effect

- Pooled r = **0.074** (95% CI [0.060, 0.088]), z=10.24, p=<.001
- tau^2 (between-study L3) = 0.0014; tau^2 (within-study L2) = 0.0087
- I^2 total = 87.8%  (L3 between = 11.8%, L2 within = 76.1%)

## Moderator tests (Q_M, Wald chi-square)

| Moderator | levels | Q_M | df | p |
|---|---|--:|--:|--:|
| ICRV regime (icrv) | 5 | 17.35 | 4 | 0.002 |
| country digital adoption (cdai) | 3 | 1.23 | 2 | 0.541 |
| digital paradox lifecycle (dpl) | 3 | 0.56 | 2 | 0.755 |

## Subgroup pooled r by ICRV regime

| ICRV | k effects | pooled r |
|---|--:|--:|
| I | 139 | 0.045 |
| II | 25 | 0.052 |
| III | 91 | -0.007 |
| FR | 3 | 0.399 |
| MX | 30 | 0.049 |

## Publication bias

- Egger regression slope p = 0.007 (asymmetry detected)
- Trim-and-fill L0 (Duval & Tweedie) imputes ~10 studies on the left; adjusted pooled effect attenuates the baseline downward.

