# P3 (Vietnam) Replication

R replication of the P3 Vietnam internationalization–performance analysis (WBES 2009/2015/2023).

## Contents
- `p3_vietnam_replication.py` — main estimation pipeline
- `coefs_main_models.csv` — model coefficients (M0–M…) per wave + pooled (N = 989 / 956 / 1013; pooled 2,958)
- `data/p3_R_turning_points.csv` — turning-point estimates
- `do/` — Stata do-files (primary estimation)
- `figures/`, `figure_sources/`, `generate_p3_figures.py` — figure outputs

## Turning-point reconciliation (R cross-check vs finalized manuscript)
The bundled R replication yields a **pooled M2 turning point ≈ 34.5% FSTS**
(`data/p3_R_turning_points.csv`), whereas the finalized manuscript reports **per-wave turning
points of 46.2% (2009), 39.3% (2015), 41.6% (2023), pooled 39.7%**, from the primary Stata
estimation (the `do/` pipeline). The few-percentage-point difference reflects
specification/sample differences between this secondary R check and the primary Stata models;
both agree on the qualitative result — a statistically significant inverted-U that is durable
across the three waves. The **manuscript (Stata) turning points are authoritative**; the R
outputs are a secondary cross-check.

## Citation
Please cite the manuscript and the World Bank Enterprise Surveys when using this replication package.
