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

### Cleanup Notes — Stray Vietnam Artifacts Removed
Several files belonging to the **P3 Vietnam** package had been copied into this folder
by mistake. They have been removed or renamed so this folder cleanly represents the
Singapore replication:

- **Removed** nine Vietnam-data CSVs from `tables/` (they carried `VNM*` / 2009–2015–2023
  rows with N = 989/956/1013, not `SGP2023`): `coefs_main_models.csv`,
  `joint_tests_main_models.csv`, `selection_checks.csv`, `table_1_descriptives.csv`,
  `table_3_robustness.csv`, `table_density_around_tp.csv`, `table_lind_mehlum.csv`,
  `table_oster_bounds.csv`, `table_paternoster.csv`. Their Singapore equivalents must be
  regenerated from the do-file pipeline above (raw WBES Singapore 2023 DTA required;
  not bundled in this environment).
- **Renamed** `p4_singapore_replication.py` → `misplaced_vietnam_replication.py`. Its
  content is an exact byte-for-byte duplicate of the root `replication/p4_vietnam_replication.py`
  (loads Vietnam 2009/2015/2023 DTA). It is **not** the Singapore pipeline and is kept
  only for traceability.
- `tables/table_psm_balance.csv` carries no country marker; provenance unverified — left
  in place for review.

### Citation
Please cite the manuscript and the World Bank Enterprise Surveys when using this replication package.
