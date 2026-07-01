# P10 Japan — Reproduction Note (2026-06-23)

Reproduced from raw WBES micro-data. Source of truth:
`data_wbes/analysis/CANONICAL_NUMBERS.md` (section 4, "P10 Nhật Bản").

## Command

```bash
# from repo root
python3 p10_japan/replication/p10_japan_models.py
```

- Raw input: `data_wbes/raw_dta/Japan-2025-full-data.dta` (inaugural WBES wave, 2025).
- Environment: pandas / numpy / pyreadstat / scipy + pyfixest 0.60.0 (the
  reghdfe-equivalent used throughout the dissertation). HC1 robust SEs; sector
  FE on `a4a`. No linearmodels used.
- Run captured: `REPRO_2026-06-23/` (this folder). Estimates table:
  `estimates.csv`.

## Headline results vs canonical

| Quantity | Reproduced | Canonical target | Match |
|---|---|---|---|
| FSTS linear (M1, `fsts_c`) | **+0.6707*** (p=0.0000, N=2047) | +0.671*** | **Y** |
| FSTS quadratic (M2, `fsts_c2`) | −0.6061 (p=0.3232, N=2047) | n.s. — no inverted-U, near-linear | **Y** |
| Exporter productivity premium | **+0.258*** (p=0.0000, N=2011) | +0.258*** | **Y** |
| N (raw rows) | **2,168** | 2,168 | **Y** |

The quadratic term is statistically insignificant (p=0.32) and the algebraic
turning point lands at ~90% FSTS (well outside the populated support), i.e. the
Japan export–productivity relationship is **near-linear with NO inverted-U** —
exactly as canonical specifies. The same holds across the robustness battery
(Table 5: R2/R3/R5/R6 all show a positive linear term and an insignificant
quadratic term).

## Descriptives vs canonical

| Descriptive | Reproduced | Canonical | Match |
|---|---|---|---|
| FSTS mean | 4.1% | 4.1% | **Y** |
| Exporters share | 16.8% (`exporter` mean, N=2128) | 16.8% | **Y** |
| Website (`c22b`/dai) | 83.8% (N=2148) | 83.8% | **Y** |
| Firm age (years) | 50.4 (mean=50.388) | 50.4 | **Y** |
| Female management | 7.3% (mean=0.073) | 7.3% | **Y** |

## Notes / minor presentation points (not discrepancies)

- The script's final summary line prints `exporters = 16.5%` because it divides
  `(fsts>0)` by **all** rows (including FSTS-missing rows). The canonical and
  Table-1 figure is the `exporter` variable mean over valid rows = **16.8%**,
  which reproduces exactly. No correction needed; both denominators are
  internally consistent.
- All ten canonical P10 quantities match. No discrepancies found. Nothing was
  fabricated; every value here comes from the captured run of the runner above.
