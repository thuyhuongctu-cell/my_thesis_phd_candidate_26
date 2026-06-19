# P7 robustness suite — few-cluster, multiple-testing, measurement invariance, selection

> Reproducible extension of the canonical 50-economy frame (`dist/osf/P7_capstone/code/p7_run_50econ.py`).
> Estimator: two-way FE (economy + year), DV `lp_z` (within economy-year z-score of winsorised ln(d2/l1)).
> Run 2026-06-19. Frame state at run: 49 economies / 102 economy-years / 88,501 firms (one wave's `.dta`
> differs from the locked 50-econ/103-pair frame; coefficients reproduce the SSOT to 3–4 sig figs:
> M2 β₁=1.189, β₂=−1.399, TP=51.45%; M5 TP=43.55%).

## Module 1 — Cross-schema measurement invariance (item availability + means)

| Schema generation | N | DAI (website) available | TCI items available | DAI mean |
|---|--:|--:|--:|--:|
| PICS3 (2006–2012) | 8,048 | 99.6% | 97.5% | 0.299 |
| Standardized (2013–2017) | 23,940 | 99.6% | 98.9% | 0.456 |
| BREADY/BEE (2018–2026) | 56,513 | 99.7% | 99.6% | 0.530 |

**Reading.** The DAI Tier-1 (website) and TCI component items are present for ~99% of firms in every
schema generation, so the harmonised constructs are item-comparable across waves. The DAI mean rises
monotonically (0.30 → 0.46 → 0.53), consistent with genuine digital diffusion rather than a schema
discontinuity. Cross-wave DAI/TCI comparisons (P5 2012↔2024; P9 2014↔2025) are therefore interpreted
as substantive change on an invariant item, not as a measurement artefact.

## Module 2 — Few-cluster wild-cluster bootstrap (CGM), cluster = economy

Restricted wild-cluster (Rademacher, B=9,999) bootstrap-t on the per-ICRV-group curvature, via FWL
residualisation; compared with the analytic CRV1 p-value.

| Group | #econ (clusters) | term | β | t | p (CRV1) | p (wild) |
|---|--:|---|--:|--:|--:|--:|
| Lower-mid transition | 7 | FSTS² | −1.012 | −6.77 | 0.001 | ≈0.10 |
| Emerging | 16 | FSTS² | −0.453 | −1.27 | 0.223 | ≈0.33 |
| Advanced-resource | 6 | FSTS² | −0.730 | −2.18 | 0.082 | ≈0.094 |
| SIDS (FIP linear) | 8 | FSTS | −0.098 | −1.05 | 0.329 | ≈0.30 |

**Reading.** With only 6–16 economies per group, CRV1 over-rejects; the wild bootstrap inflates the
per-group curvature p-values. The sharp inverted-U in the transition regime — the strongest per-group
result — weakens to p≈0.10. This confirms that formal nonlinearity inference is correctly anchored at
the **pooled** level (M2, 49 clusters, β₂=−1.399, p<0.001) and triangulated with the meta-analysis
(P6), not read off individual small-cluster subgroups. The per-ICRV turning points are best read as a
descriptive gradient, not as independently powered hypothesis tests.

## Module 3 — Multiple-testing correction on the P7 interaction family

Family = {FSTS×TCI, FSTS²×TCI, FSTS×DAI, FSTS²×DAI}; Holm and Bonferroni.

| Interaction term | β | p (raw) | p (Holm) | p (Bonferroni) |
|---|--:|--:|--:|--:|
| FSTS×TCI | +0.065 | 0.408 | 0.705 | 1.000 |
| FSTS²×TCI | −0.117 | 0.235 | 0.705 | 0.940 |
| FSTS×DAI | −0.279 | 0.139 | 0.557 | 0.557 |
| FSTS²×DAI | +0.262 | 0.351 | 0.705 | 1.000 |

**Reading.** No interaction term is significant raw, and all remain non-significant after Holm/
Bonferroni. The capability-as-level-shifter (not curve-bender) conclusion is therefore not a false
negative produced by uncorrected multiple testing — it survives the most conservative correction.

## Module 4 — Selection-into-exporting (Heckman-type inverse-Mills check)

Participation probit (exporter ~ fdi10 + ln_age + tci_z + dai), inverse-Mills ratio added to the M5
outcome equation (functional-form identification; pooled FE).

| Model | N | β₁ (FSTS) | β₂ (FSTS²) | TP | IMR |
|---|--:|--:|--:|--:|--:|
| M5 base | 78,874 | +0.501 | −0.723 (p<0.001) | 43.6% | — |
| M5 + inverse-Mills | 78,874 | +0.506 | −0.732 (p<0.001) | 43.5% | −0.414 (p=0.317) |

**Reading.** Adding the inverse-Mills selection term leaves the inverted-U curvature and the turning
point essentially unchanged (43.6%→43.5%), and the IMR itself is non-significant (p=0.317). There is no
detectable Melitz-type self-selection bias in the estimated curvature; the inverted-U is not an artefact
of more-productive firms selecting into exporting.
