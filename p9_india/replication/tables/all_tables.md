# P9' India — Tables 1, 2, 4, 5 (consolidated)

*Table 3 is inline in §4.3 of the manuscript.*

---

**Table 1.** Descriptive statistics by WBES wave, India 2014–2025.

| Variable | 2014 (N=8,941) | 2022 (N=9,300) | 2025 (N=10,476) |
|---|---:|---:|---:|
| ln(Labour Productivity) | 13.929 (1.263) | 14.366 (1.214) | 15.012 (0.845) |
| Export intensity (FSTS, 0-1) | 0.072 (0.219) | 0.080 (0.235) | 0.027 (0.115) |
| Technological Capability Index (z) | -0.005 (0.999) | 0.000 (1.001) | 0.000 (1.000) |
| DAI Tier-1 (website binary) | 0.526 (0.499) | 0.606 (0.489) | 0.418 (0.493) |
| DAI Tier-2 (e-payment, share) | — | — | 0.658 (0.148) |
| ln(Permanent full-time employees) | 3.635 (1.292) | 3.640 (1.358) | 3.669 (1.275) |
| Firm age (years) | 19.627 (14.162) | 22.750 (14.957) | 19.753 (14.316) |
| Foreign-owned (≥ 10 % foreign equity) | 0.009 (0.092) | 0.014 (0.116) | 0.019 (0.137) |

*Note: Cell entries are mean (standard deviation). FSTS is direct plus indirect exports as a share of total sales. TCI is the z-standardised mean of four binary capability items (quality certification, foreign technology licence, product innovation, R&D activity), available for firms responding to at least three items. DAI Tier-2 (e-payment share) is measured only in the 2025 BREADY wave.*

---

**Table 2.** Wave-by-wave OLS estimates of the inverted-U M2 specification (HC1 and state-clustered SE).

Dependent variable: ln(Labour Productivity)

| Term | 2014 | 2022 | 2025 |
|---|---:|---:|---:|
| FSTS | +1.865*** | +1.542*** | -0.359* |
|  | (0.235) | (0.223) | (0.153) |
|  | [0.552]*** | [0.550]** | [0.314] |
| FSTS² | -1.508*** | -1.893*** | -0.160 |
|  | (0.254) | (0.239) | (0.199) |
|  | [0.539]** | [0.532]*** | [0.299] |
| ln(Employees) | +0.101*** | +0.244*** | +0.214*** |
|  | (0.011) | (0.009) | (0.007) |
| Firm age | -0.001 | +0.000 | -0.000 |
|  | (0.001) | (0.001) | (0.001) |
| Foreign-owned | +0.403* | +0.252* | +0.249*** |
|  | (0.174) | (0.109) | (0.058) |
| Constant | +13.528*** | +13.463*** | +14.235*** |
|  | (0.043) | (0.036) | (0.024) |
| N | 8,941 | 9,300 | 10,476 |
| R²_adj | 0.0313 | 0.0933 | 0.1023 |
| Turning point (%) | 61.8 | 40.7 | n/a |
| Lind–Mehlum inverted-U | Yes (p = 0.0000) | Yes (p = 0.0000) | No (p = 0.9907) |

*Note: Coefficients with HC1 robust standard errors in parentheses on the second row; state-clustered standard errors (Cameron et al., 2008; ~24 clusters per wave) in brackets on the third row for FSTS and FSTS² terms. Significance under each SE: † p < 0.10, * p < 0.05, ** p < 0.01, *** p < 0.001. Turning point computed as TP = −β̂₁ / (2β̂₂); reported only for waves with inverted-U supported in Lind–Mehlum test.*

---

**Table 4.** Capability moderation models — TCI, DAI Tier-1, and DAI Tier-2 (UPI e-payment).

Dependent variable: ln(Labour Productivity)

| Term | M3 TCI 2014 | M3 TCI 2022 | M3 TCI 2025 | M4 DAI Tier-1 2025 | M4b DAI Tier-2 2025 |
|---|---:|---:|---:|---:|---:|
| FSTS | +1.728*** | +0.980*** | -0.271 | -1.128* | +2.454* |
| FSTS² | -1.383*** | -1.332*** | -0.225 | +0.919 | -2.546† |
| TCI | +0.119*** | +0.185*** | -0.084*** |
| FSTS × TCI | -0.010 | +0.128 | +0.204* |
| FSTS² × TCI | -0.018 | -0.331† | -0.172 |
| DAI Tier-1 |  |  |  | -0.031† |
| FSTS × DAI Tier-1 |  |  |  | +0.896† |
| FSTS² × DAI Tier-1 |  |  |  | -1.231† |
| DAI Tier-2 (e-payment) |  |  |  |  | +0.887*** |
| FSTS × DAI Tier-2 |  |  |  |  | -4.022** |
| FSTS² × DAI Tier-2 |  |  |  |  | +3.391† |
| N | 8,941 | 9,300 | 10,476 | 10,476 | 10,473 |
| R²_adj | 0.0384 | 0.1114 | 0.1088 | 0.1025 | 0.1238 |

*Note: M3 augments M2 with TCI and FSTS × TCI / FSTS² × TCI interactions. M4 augments M2 with DAI Tier-1 (own-website binary) and corresponding interactions. M4b augments M2 with DAI Tier-2 (% sales received via electronic payment, 2025 BREADY only) and corresponding interactions. All HC1 robust standard errors. Significance: † p < 0.10, * p < 0.05, ** p < 0.01, *** p < 0.001. Controls (ln(Employees), firm age, foreign ownership) included but suppressed for space.*

---

**Table 5.** Robustness specifications — five sub-samples and one alternative dependent variable.

M2 specification: ln(Labour Productivity) = β₀ + β₁ FSTS + β₂ FSTS² + controls.

| Specification | Wave | N | β̂₁ FSTS | β̂₂ FSTS² | TP (%) | Inv-U? |
|---|---:|---:|---:|---:|---:|:-:|
| Baseline (full sample) | 2014 | 8,941 | +1.865*** | -1.508*** | 61.8 | Yes |
|  | 2022 | 9,300 | +1.542*** | -1.893*** | 40.7 | Yes |
|  | 2025 | 10,476 | -0.359* | -0.160 | n/a | No |
| | | | | | | |
| R1: Manufacturing only | 2014 | 6,974 | +1.896*** | -1.649*** | 57.5 | Yes |
|  | 2022 | 5,366 | +1.697*** | -2.056*** | 41.3 | Yes |
|  | 2025 | 5,706 | -0.073 | -0.464* | -7.9 | No |
| | | | | | | |
| R2: Trimmed FSTS ≤ 0.95 | 2014 | 8,666 | +2.263*** | -2.324*** | 48.7 | Yes |
|  | 2022 | 8,937 | +1.585*** | -1.998*** | 39.7 | Yes |
|  | 2025 | 10,436 | -0.301 | -0.303 | -49.7 | No |
| | | | | | | |
| R3a: SME (employees < 100) | 2014 | 6,844 | +0.758* | -0.071 | n/a | No |
|  | 2022 | 6,497 | +1.354*** | -1.644*** | 41.2 | Yes |
|  | 2025 | 7,383 | -0.713* | +0.382 | 93.2 | No |
| | | | | | | |
| R3b: Large (employees ≥ 100) | 2014 | 2,097 | +3.047*** | -3.037*** | 50.2 | Yes |
|  | 2022 | 2,803 | +1.942*** | -2.379*** | 40.8 | Yes |
|  | 2025 | 3,093 | -0.033 | -0.547* | -3.0 | No |
| | | | | | | |
| R4: Alt DV (standardised levels) | 2014 | 8,941 | +0.600* | -0.551* | 54.4 | No |
|  | 2022 | 9,300 | +0.927*** | -1.116*** | 41.5 | Yes |
|  | 2025 | 10,476 | -0.648*** | +0.028 | n/a | No

*Note: HC1 robust standard errors used throughout. Significance: † p < 0.10, * p < 0.05, ** p < 0.01, *** p < 0.001. Inv-U? column indicates whether Lind–Mehlum (2010) joint U-test supports inverted-U at the 5 % level. Manufacturing classification uses ISIC Rev 3.1 codes 15–37 for 2014 PICS3 and ISIC Rev 4 codes 10–33 for 2022 BEE and 2025 BREADY. R4 uses standardised labour productivity in levels (z-score within wave) as the dependent variable.*

---

