# Replication Package — P3 Vietnam
## Technological Capability, Digital Adoption, and the Internationalisation–Performance Relationship: Evidence from Vietnam (2009–2015–2023)

### Overview
This replication package contains the Python script and supplementary output tables for the paper above. All analysis uses three waves of World Bank Enterprise Survey (WBES) microdata for Vietnam (2009, 2015, 2023).

### Requirements
- Python ≥ 3.9
- `pandas`, `numpy`, `statsmodels`, `pyreadstat`, `matplotlib`
- WBES raw DTA files (see Data Availability below)

### Data Availability
The WBES microdata are publicly available from the World Bank Enterprise Surveys portal:
- Vietnam 2009: https://www.enterprisesurveys.org (survey year 2009)
- Vietnam 2015: https://www.enterprisesurveys.org (survey year 2015)
- Vietnam 2023: https://www.enterprisesurveys.org (survey year 2023)

Place the three DTA files in a local directory and update the `UPLOAD` path variable at the top of `p4_vietnam_replication.py`.

### Running the Replication
```bash
python replication/p4_vietnam_replication.py
```

Outputs are written to `/tmp/p4_vietnam_figures/` by default. This includes:
- PNG figures (figure_2a–2d, figure_3)
- `results_p4.json` summary statistics

### Supplementary Tables
The `tables/` subdirectory contains CSV files with the underlying coefficient outputs:

| File | Contents |
|------|----------|
| `table_1_descriptives.csv` | Analytic-sample summary statistics by wave (Table 1 in manuscript) |
| `coefs_main_models.csv` | Long-format regression coefficients for M0–M8, all waves and pooled |
| `joint_tests_main_models.csv` | Joint F-tests for H2 (TCI moderation) and H4 (DAI moderation) by wave |
| `table_lind_mehlum.csv` | Lind–Mehlum U-shape test results with turning-point estimates |
| `table_3_robustness.csv` | Robustness specifications (Panels A–D and G) |
| `selection_checks.csv` | Heckman selection and control-function robustness checks |
| `table_paternoster.csv` | Cross-wave Paternoster z-tests for coefficient equality |

### Key Replication Targets
From the manuscript (all models OLS with HC1 robust SEs):

| Wave | N | TCI_z (M7) | DAI_z (M7) | LM p-value | Turning point |
|------|---|-----------|-----------|------------|---------------|
| 2009 | 989 | +0.215*** | +0.175*** | .006 | ~40% |
| 2015 | 956 | +0.128** | −0.044 | .009 | ~44% |
| 2023 | 1,013 | +0.123** | +0.095* | .013 | ~46% |
| Pooled | 2,958 | +0.179*** | +0.078** | <.001 | 39.7% |

### Citation
Please cite the manuscript and the World Bank Enterprise Surveys when using this replication package.
