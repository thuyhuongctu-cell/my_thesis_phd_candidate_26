# Replication Package — P4 Singapore
## Capability, Digital Adoption, and the Internationalisation–Performance Relationship: Evidence from Singapore (WBES 2023)

### Overview
Single-wave firm-level analysis of the internationalisation–performance (I–P) relationship for
Singapore using World Bank Enterprise Survey (WBES) 2023 microdata (BREADY schema).

### Authoritative runner (reproducible from committed raw data)
```bash
python3 p4/replication/p4_singapore_figs_from_raw.py
```
- Reads `data_wbes/raw_dta/Singapore-2023-full-data.dta` (override with `WBES_RAW`).
- Builds `lnLP = ln(d2/l1)`, `FSTS = d3c/100` (mean-centred), `TCI` (z-composite of b8+e6+h1),
  `DAI` (z-composite of website c22b + k33 + k38).
- Estimates M0–M8 (incl. the `FSTS²×DAI` interaction) with HC1 SEs + Lind–Mehlum turning point.

Stata equivalent (authoritative for the candidate's licensed run):
`p4/replication/do/01_build_singapore.do` → `02_run_models.do` → `03_make_figures.do`.

### Supplementary tables (`tables/` — Singapore, sample `SGP2023`, N=623)
`coefs_main_models.csv` (M0–M8), `joint_tests_main_models.csv`, `table_lind_mehlum.csv` /
`p4_R_turning_points.csv`, `table_3_robustness.csv`, `selection_checks.csv`, `table_paternoster.csv`,
`table_oster_bounds.csv`, `table_psm_balance.csv`, `table_density_around_tp.csv`.

### Key replication targets (OLS, HC1 SEs)
| Quantity | Manuscript | Python re-run (2026-06-23) |
|---|---|---|
| N (base / with DAI) | 623 / 617 | 623 / 617 |
| M2 inverted-U | FSTS_c +; FSTS²_c − | +3.08 / −1.90 |
| TCI level (M5) | + | +0.21 |
| DAI level (M6) | + | +0.17 |
| **FSTS²×DAI (M8)** | **+3.119**, p≈.005 | **+3.22**, p=.020 |
| M2 turning point | ~88.6% (CI exceeds feasible FSTS → not reliably located) | ~86% [31%–141%] |

### Citation
Please cite the manuscript and the World Bank Enterprise Surveys when using this package.
