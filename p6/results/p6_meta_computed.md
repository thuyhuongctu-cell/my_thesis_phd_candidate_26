> ⚠️ **DEPRECATED — KHÔNG DÙNG LÀM NGUỒN / DO NOT CITE.** This file is the output of the
> NON-CANONICAL Python cross-check `scripts/p6_meta_analysis.py`. It diverges from the canonical
> R `metafor` pipeline: here I² = 87.8% (canonical 62.4%), trim-and-fill ~10 (canonical 57),
> Egger p = 0.007 (canonical 0.057), ICRV r 0.045/0.052/−0.007/0.399/0.049 (canonical
> 0.079/0.065/0.069/0.349/0.053). Source of truth = `table1_baseline.csv` … `table5_sensitivity.csv`
> + `p6/results/CANONICAL_NUMBERS_P6.md`. The pooled r̄ = 0.074, k = 238, K = 288 and Q_M
> ICRV = 17.35 below DO match canonical and are the only values safe to reuse from here.

# P6 three-level meta-analysis — FROZEN computed results

Source: `p6/results/forest_data.csv` — k=238 studies, K=288 effect sizes. Reproducible via `scripts/p6_meta_analysis.py`.

Model: three-level random-effects on Fisher-z; REML variance components; GLS pooling; Wald Q_M for moderators. All values below are computed, not placeholders.

## Baseline pooled effect

- Pooled r = **0.074** (95% CI [0.060, 0.088])
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
- Trim-and-fill L0 (Duval & Tweedie) imputes ~10 studies on the left.

