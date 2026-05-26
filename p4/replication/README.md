# Replication Package — P4 Singapore
## Technological Capability, Digital Adoption, and the Internationalisation–Performance Relationship: Firm-Level Evidence from Singapore (WBES 2023)

### Overview
This replication package contains the analysis pipeline and supplementary output
tables for the paper above. All analysis uses the World Bank Enterprise Survey
(WBES) Singapore 2023 wave (B-READY methodology). After listwise deletion on the
focal variables the analytic sample is N = 623 (N = 617 with all controls).

### Requirements
- Stata ≥ 17 (build + main models) and R ≥ 4.2 (turning-point / bootstrap stage)
- R packages: `sandwich`, `lmtest`, `boot`
- WBES Singapore 2023 raw DTA file (see Data Availability below)

### Data Availability
The WBES microdata are publicly available from the World Bank Enterprise Surveys portal:
- Singapore 2023: https://www.enterprisesurveys.org (survey year 2023, B-READY)

### Running the Replication
The authoritative pipeline is the Stata + R do-file chain in `do/`:
```bash
# 1. Build the analytic dataset from the raw WBES Singapore 2023 DTA
stata -b do do/01_build_singapore.do
# 2. Estimate the main OLS models (M0–M8, HC1 robust SEs)
stata -b do do/02_run_models.do
# 3. Turning-point estimation, Lind–Mehlum test and bootstrap CI
Rscript do/03_run_models_R.R
```

### Output Tables (Singapore)
These files in this folder are the Singapore outputs produced by the pipeline above:

| File | Contents |
|------|----------|
| `coefs_main_models.csv` (top level) | Regression coefficients for M0–M8 (`sample = SGP2023`, HC1 robust SEs) |
| `tables/p4_R_coefs.csv` | R-stage coefficient outputs (`sample = SGP2023`) |
| `tables/p4_R_turning_points.csv` | Turning-point estimate, quadratic terms and Lind–Mehlum verdict |

### Key Replication Targets
From the manuscript (OLS, HC1 robust SEs; analytic sample N = 623 / 617 with controls):

| Quantity | Value |
|----------|-------|
| M2 FSTS (linear) | +2.652*** (SE 0.691, p < .001) |
| M2 FSTS² (quadratic) | −1.705† (SE 0.931, p = .068) |
| Turning point (R replication, raw FSTS) | 76.4% |
| Lind–Mehlum p-value | .303 (inverted-U **not** formally confirmed) |
| Bootstrap 95% CI for turning point | [53%, 253%]; inverted-U shape recovered in 96.3% of 5,000 resamples |
| Zero-export share | 82% of firms (only 3% exceed 50% FSTS) |

> Note: the manuscript discusses the turning point as lying near FSTS ≈ 82% in the
> sparse upper tail of the export-intensity distribution; the R pipeline point
> estimate is 76.4%. Both fall in a thinly supported region where the conventional
> inverted-U interpretation is not formally identified (the *digital saturation
> paradox* discussion in the manuscript).

### Known Issues — Stray Vietnam Artifacts (do **not** use for P4)
This folder currently also contains files that belong to the **P3 Vietnam** package
and were copied here by mistake. They are **not** part of the Singapore replication
and should be regenerated from the Singapore pipeline above (or removed) before the
package is finalised. No data has been deleted in this commit.

- `p4_singapore_replication.py` — misnamed: its header reads "P4 Vietnam" and it
  loads the Vietnam 2009/2015/2023 DTA files. This is the Vietnam Python script, not
  the Singapore pipeline.
- The following `tables/*.csv` contain Vietnam rows (`VNM2009/VNM2015/VNM2023/VNMpooled`)
  rather than `SGP2023`, and are stale Vietnam outputs:
  `table_1_descriptives.csv`, `table_lind_mehlum.csv`, `joint_tests_main_models.csv`,
  `selection_checks.csv`, `table_3_robustness.csv`, `table_density_around_tp.csv`,
  `table_oster_bounds.csv`, `table_paternoster.csv`, `tables/coefs_main_models.csv`.
- `tables/table_psm_balance.csv` carries no country marker; provenance unverified.

### Citation
Please cite the manuscript and the World Bank Enterprise Surveys when using this replication package.
