# P6 Meta-Analysis — Final Quick Results

**Date**: 2026-05-23
**Method**: Three-level random-effects MARA via R metafor 4.4.0
**Input data**: `p6/data/p6_study_database.csv` (288 effect sizes from 238 studies)

## Headline numbers (P6 final, to replace CD2 §2.4.3 PENDING block)

| Metric | Value | Notes |
|---|---:|---|
| k studies | **238** | unique study_id |
| K effect sizes | **288** | total nested observations |
| Countries | **49** | per study database |
| **Pooled r** | **0.0743** | Fisher-z back-transformed, 3-level |
| **95% CI** | **[0.0601, 0.0886]** | from rma.mv |
| **I²** | **87.9%** | total heterogeneity |
| **τ²** | 0.0101 | between-study variance |
| **Q(df=287)** | 1909.42 | all-effects Q |
| **σ²₁ (level-3, between-study)** | 0.0014 | sqrt = 0.0368 |
| **σ²₂ (level-2, within-study)** | 0.0087 | sqrt = 0.0935 |

## H1 — ICRV moderator test (regime moderation)

| Test | Value | Decision |
|---|---:|---|
| Q_M | **17.42** | |
| df | 4 | |
| **p** | **.0016** | **H1 SUPPORTED** ✓ |

### Mean r by ICRV regime

| Regime | k | Mean r |
|---|---:|---:|
| FR (Frontier) | 3 | 0.3122 ⚠ small k, anomalous |
| I (Advanced innovation) | 139 | 0.0796 |
| II (Advanced resource) | 25 | 0.0640 |
| III (Upper-middle) | 91 | 0.0687 |
| MX (Mixed/Other) | 30 | 0.0540 |

**Note**: Frontier (FR) high r driven by small k=3; gradient I→II→III→MX roughly monotone declining.

## Publication bias

| Test | Statistic | p-value | Interpretation |
|---|---:|---:|---|
| Egger's regression | z = 1.849 | .0644 | Marginal |
| Begg–Mazumdar rank | τ = -0.134 | **.0007** | Significant asymmetry |
| Trim-and-fill | 58 imputed | – | Substantial |
| **Adjusted r** | **0.0348** | – | ~50% reduction from raw |

## Comparison: CD2 PROVISIONAL vs P6 FINAL

| Metric | CD2 PROVISIONAL | P6 FINAL | Δ |
|---|---:|---:|---|
| k | 238 | 238 | exact match |
| K | 288 | 288 | exact match |
| Pooled r | 0.074 | 0.0743 | +0.0003 |
| CI lower | 0.060 | 0.0601 | +0.0001 |
| CI upper | 0.088 | 0.0886 | +0.0006 |
| ICRV Q_M | 17.35 | 17.42 | +0.07 |
| ICRV p | .002 | .0016 | -0.0004 |
| τ (rank test) | -0.134 | -0.134 | exact |
| Trim-fill k | 58 | 58 | exact |
| r_adj | 0.035 | 0.0348 | -0.0002 |

**The PROVISIONAL numbers were highly accurate**. CD2 PENDING block can be promoted to FINAL with minimal change (round to 3 decimals).

## Conclusion

- **P6 ready for IBR submission** with these confirmed numbers.
- CD2 §2.4.3 Hướng 1 can drop PENDING block — numbers verified.
- Luận án §4.2 (Chương 4) can use these numbers as final P6 reporting.

## Next steps

1. Update CD2 §2.4.3: replace PENDING blockquote with confirmed numbers + remove "(số liệu PENDING cho lần chạy P6 cuối)" parenthetical
2. Update P6 manuscript abstract (already has these numbers as v1.0)
3. Generate P6 figures (forest, funnel, sensitivity, ICRV) from same data
