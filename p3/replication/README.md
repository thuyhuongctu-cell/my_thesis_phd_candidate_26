# Replication Package — P3 Vietnam
## Technological Capability, Digital Adoption, and the Internationalisation–Performance Relationship: Evidence from Vietnam (2009–2015–2023)

### Overview
Three-wave firm-level analysis of the internationalisation–performance (I–P) relationship for
Vietnam using World Bank Enterprise Survey (WBES) microdata for 2009, 2015 and 2023.

### Authoritative runner
The P3 build/estimation is **Stata-authoritative** (the `b1_d` employment denominator and the
DAI instrument are defined in the do-files):
```bash
# Stata (candidate's licensed machine — authoritative for exact magnitudes)
p3/replication/do/01_build_vietnam.do      # build analytic .dta from data_wbes/raw_dta/
p3/replication/do/02_run_models.do         # M0–M8 + Lind–Mehlum + IV(DAI) + Paternoster
```
Python equivalent reproduces the **pattern** (inverted-U; turning point ~39–46%) but not the exact
magnitudes (the IV `b1_d` denominator differs): `scripts/p3_dai_reproduce.py`. Figures:
`p3/replication/generate_p3_figures.py`.

Data: place the WBES Vietnam DTA files in `data_wbes/raw_dta/` (override with `WBES_RAW`).

### Key replication targets (OLS, HC1 robust SEs)
| Wave | N | TCI_z (M7) | DAI_z (M7) | LM p-value | Turning point |
|------|---|-----------|-----------|------------|---------------|
| 2009 | 989 | +0.215*** | +0.175*** | .006 | ~40% |
| 2015 | 956 | +0.128** | −0.044 | .009 | ~44% |
| 2023 | 1,013 | +0.123** | +0.095* | .013 | ~46% |
| Pooled | 2,958 | +0.179*** (IV) | +0.078** | <.001 | 39.7% |

### Citation
Please cite the manuscript and the World Bank Enterprise Surveys when using this package.
