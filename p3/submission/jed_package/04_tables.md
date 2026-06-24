# Tables, submitted as a separate file (JED requirement)

*Position of each table is marked in the main text as "[Insert Table I about here]", etc. Tables are numbered in Roman numerals. lnLP = log labour productivity; FSTS = direct-export intensity; TCI_z, DAI_z = within-wave z-standardised composites; HC1 robust standard errors throughout.*

---

**Table I.** Variable definitions and WBES construction.

| Variable | WBES item(s) | Construction | Role |
|---|---|---|---|
| lnLP | d2, l1 | ln(annual sales PPP / permanent employees) | Dependent |
| FSTS | d3c | d3c / 100: direct-export intensity (0–1) | Independent |
| FSTS_c, FSTS_c² | d3c | within-wave mean-centred and squared | Tests inverted-U (H1) |
| TCI_z | b8, e6 | within-wave z of mean(quality certification, foreign-licensed technology) | Technological capability (H2) |
| DAI_z | c22b | within-wave z of website presence | Digital adoption, Tier-1 (H3, exploratory) |
| lnEmp | l1 | ln(permanent employees) | Control: firm size |
| FirmAge | b5 | survey year − year established | Control: firm age |
| ForeignOwned | b2b | 1 if any foreign equity | Control: ownership |
| Sector FE | a4b / a4a | 1-digit ISIC (a4b 2009/2015; a4a 2023) | Fixed effects |
| Wave FE | wave | 2009 / 2015 / 2023 (pooled only) | Fixed effects |

*Notes.* b8, e6, c22b recoded to binary 1/0; composites standardised within wave. TP* = −β₁/(2β₂), confirmed by the Lind and Mehlum (2010) u-test. WBES −9 treated as missing; listwise deletion. Source: WBES Vietnam 2009/2015/2023.

---

**Table II.** Analytic-sample summary statistics by wave, mean (SD).

| Variable | 2009 (N=989) | 2015 (N=956) | 2023 (N=1,013) | Pooled (N=2,958) |
|---|---|---|---|---|
| ln(Labour productivity) | 19.412 (1.307) | 20.042 (1.460) | 20.549 (1.474) | 20.005 (1.491) |
| FSTS | 0.168 (0.337) | 0.119 (0.283) | 0.131 (0.311) | 0.139 (0.312) |
| Exporter share | 0.284 | 0.207 | 0.188 | 0.226 |
| TCI_z | 0.169 (0.305) | 0.142 (0.295) | 0.146 (0.276) | 0.152 (0.292) |
| DAI_z (website) | 0.425 (0.495) | 0.483 (0.500) | 0.498 (0.500) | 0.469 (0.499) |
| Firm size (ln emp.) | 4.067 (1.493) | 3.629 (1.476) | 3.578 (1.539) | 3.758 (1.519) |
| Firm age (years) | 11.9 (11.3) | 12.8 (9.6) | 14.1 (7.9) | 12.9 (9.7) |
| Foreign-owned (share) | 0.142 | 0.090 | 0.125 | 0.119 |

*Notes.* TCI_z, DAI_z z-standardised within wave; listwise deletion; WBES −9 missing. Source: WBES Vietnam; authors' calculations.

---

**Table III.** Focal coefficients by wave and pooled (OLS, HC1). Significance: *** p<.001, ** p<.01, * p<.05, † p<.10.

| Term | 2009 | 2015 | 2023 | Pooled |
|---|---|---|---|---|
| FSTS_c (M2) | 1.045* | 1.159* | 0.962* | 0.984*** |
| FSTS_c² (M2) | −1.774** | −2.115** | −1.686** | −1.909*** |
| Lind–Mehlum p | .006 | .009 | .013 | <.001 |
| Turning point (% FSTS) | 46.2 | 39.3 | 41.6 | 39.7 |
| TCI_z direct (M7) | 0.215*** | 0.128* | 0.123** | 0.179*** |
| DAI_z direct (M7) | 0.175*** | −0.044 | 0.095* | 0.078** |
| FSTS_c × TCI_z (M3) | −0.579† | n.s. | (sig.) | −0.573** |
| TCI moderation, M3 joint p | .040 | .713 | .027 | .003 |
| FSTS_c × DAI_z (M8) | n.s. | n.s. | −0.912* | −0.448 |
| DAI moderation, M8 joint p | .700 | .093 | .062 | .083 |
| Exporter-only FSTS_c² (Panel H) | n/a | n/a | n/a | −0.200 (p=.730) |

*Notes.* β reported; full SEs and the M0–M8 sequence are in the replication package. Exporter-only sub-sample pooled N = 669; its non-significant quadratic term indicates the full-sample inverted-U is driven by the participation margin. Robustness panels (A–K): Supplementary Material.
