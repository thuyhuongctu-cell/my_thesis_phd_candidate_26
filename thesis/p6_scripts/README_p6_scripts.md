# P6 Meta-Analysis R Framework

Three-level MARA framework for P6:  
*"Systematic meta-analysis of the internationalization–performance relationship for 47 Asian and Pacific economies"*

## Prerequisites

```r
install.packages(c("metafor", "clubSandwich"))
```

## Script Execution Order

| Script | Purpose | Input | Output |
|---|---|---|---|
| `00_simulate_data.R` | Synthetic data for testing | — | `p6_sim_dat.rds` |
| `01_baseline_model.R` | Three-level baseline + variance partition | `p6_sim_dat.rds` | `p6_baseline_results.rds` |
| `02_moderator_analysis.R` | ICRV × I-type × P-type meta-regression | `p6_sim_dat.rds` | `p6_moderator_results.rds` |
| `03_publication_bias.R` | Egger + trim-and-fill + PET-PEESE | `p6_sim_dat.rds` + baseline | `p6_pubias_results.rds` |
| `04_sensitivity.R` | SA1–SA6 sensitivity analyses | `p6_sim_dat.rds` + baseline | `p6_sensitivity_results.rds` |

Run all:
```bash
Rscript thesis/p6_scripts/00_simulate_data.R
Rscript thesis/p6_scripts/01_baseline_model.R
Rscript thesis/p6_scripts/02_moderator_analysis.R
Rscript thesis/p6_scripts/03_publication_bias.R
Rscript thesis/p6_scripts/04_sensitivity.R
```

## Core Model

```r
m0 <- rma.mv(yi, vi,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data   = dat,
             method = "REML")
```

**Level structure:**
- L3 (between-study): `~ 1 | study_id` — variance τ²_L3
- L2 (within-study, between-ES): `~ 1 | study_id/es_id` — variance τ²_L2  
- L1: sampling error from `vi`

## Moderators (PRISMA Mục 4)

| Code | Moderator | H link | Levels |
|---|---|---|---|
| M1 | ICRV regime | H4 | Advanced / Upper_middle / Emerging / Frontier / SIDS |
| M2 | I-measure type | — | FSTS / export_dummy / entropy |
| M3 | P-measure type | — | labor_productivity / ROA / sales_growth |

## Sensitivity Analyses (PRISMA Mục 6.3)

| SA | Description | Exclusion criterion |
|---|---|---|
| SA1 | Published only | Grey literature excluded |
| SA2 | High quality | NOS < 7 excluded |
| SA3 | Outlier-robust | yi winsorized at 2.5%/97.5% |
| SA4 | Temporal | Pre-2015 vs 2015-2025 |
| SA5 | LOSO influence | Leave-one-study-out |
| SA6 | WBES-only | Non-WBES primary data excluded |

## Real Data Integration

When PRISMA database search completes (target: 06/2026), place coded data at  
`data/p6_coded_effects.rds` following coding template in `thesis/p6_prisma_protocol.md` Mục 4.

All scripts auto-detect real vs. simulated data:
```r
if (file.exists("data/p6_coded_effects.rds")) {
  dat <- readRDS("data/p6_coded_effects.rds")
} else {
  dat <- readRDS("p6_sim_dat.rds")  # fallback to simulated
}
```
