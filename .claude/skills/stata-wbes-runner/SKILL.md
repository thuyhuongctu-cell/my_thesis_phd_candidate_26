---
name: stata-wbes-runner
description: >
  Run and reproduce the dissertation's WBES econometric analyses (P3–P9 component
  studies: quadratic FSTS inverted-U, ICRV turning-point gradient, FIP, moderation)
  via Stata do-files in batch mode, OR via the validated Python fallback when no
  Stata licence/binary is available. Use when asked to: run a do-file, re-estimate
  P7 / P8 / P5, reproduce a turning point or coefficient, build the pooled WBES
  dataset, add a new economy/wave (e.g. Japan-2025) to the analytic frame, or
  check a regression result against the locked thesis numbers. Triggers: run stata,
  chạy stata, do-file, re-estimate, turning point, pooled WBES, P7 regression,
  reproduce coefficient, .do, .dta analysis.
---

# Stata / WBES re-estimation runner (with Python fallback)

This skill executes the dissertation's multi-country WBES analyses reproducibly.
It is the operational counterpart to **Phụ lục A** (`thesis/phu_luc_A_hop_nhat_du_lieu_vi.md`),
which documents the pooling/harmonisation methodology and its APA-7 justification.

## 0. INTEGRITY RULE (read first)

Reported econometric results (turning points, FIP β, moderation coefficients) for
P3–P9 are **published or under review on locked samples**. NEVER fabricate or
hand-edit a coefficient. A number may change in the manuscript **only** after it
is produced by an actual estimation run (Stata do-file, or the validated Python
pipeline) on the documented data. If a result cannot be reproduced, report the
mismatch — do not invent a value. See `data_wbes/analysis/P7_REESTIMATION_NOTE.md`.

## 1. Detect the environment

```bash
which stata stata-mp stata-se xstata 2>/dev/null   # -> Stata available?
python3 -c "import pandas,numpy,pyreadstat" 2>/dev/null && echo "python-ok"
```

- **Stata present** → use the batch pattern in §2.
- **No Stata** (this container) → use the Python fallback in §3. This is a valid
  alternative for pooled cross-section econometrics (see skill
  `stata-khong-license-giai-phap`).

## 1b. Ready-made do-files for this dissertation (run these first)

| Do-file | Purpose | Locked benchmark to verify against |
|---|---|---|
| `scripts/stata/00_prep_data.do` | Master CSV -> `p7_analytic.dta` (49-frame, lp_z within country-year) | N ~ 75,607 |
| `scripts/stata/p7_reestimate.do` | P7 M2/M5 reghdfe + utest + per-ICRV TP + M11 | TP(M5) = 40.0%; gradient ~28% -> ~55% |
| `scripts/stata/p8_sids_fip.do` | P8 FIP linear M1 + robustness | beta = -1.339 (p<.001); exporters N=26 |

One-time: `ssc install reghdfe ftools utest estout`. Full execution plan incl.
benchmark-match rules: `docs/STATA_TRONG_CLAUDE_CODE.md`.

## 1c. Stata-MCP route (deep Claude Code integration, local machine)

If the user runs VS Code locally with Stata 17+: install the "Stata MCP"
extension (github.com/hanlulong/stata-mcp), then register once:
```bash
claude mcp add --transport http stata-mcp http://localhost:4000/mcp-streamable --scope user
```
This exposes `stata_run_file` / `stata_run_selection` + data viewer + graph
display directly as MCP tools — prefer it over raw batch when available.
Alternative official bridge: pystata (`pip install stata-setup`;
`stata_setup.config('<stata path>','mp')` then `stata.run('do file.do')`).

## 2. Run a Stata do-file in batch mode

```bash
# -b = batch (no GUI); writes <dofile>.log next to the do-file
stata-mp -b do path/to/analysis.do      # or: stata -b do ... / xstata -b do ...
```

After it returns, ALWAYS inspect the log and surface errors before trusting output:

```bash
LOG=path/to/analysis.log
grep -nE "^r\([0-9]+\);" "$LOG"   # Stata error codes -> non-empty means it FAILED
tail -40 "$LOG"                    # final results block
```

A Stata error looks like `r(199);`. If present, the run failed — read the lines
above it, fix the do-file, re-run. Do not report partial results from a failed log.

Conventions for this project's do-files:
- Set `set more off` and a stable seed if bootstrapping (turning-point CIs).
- Two-way FE: `reghdfe ln_lp c.fsts##c.fsts $controls, absorb(country year) vce(cluster country)`.
- Turning point: `nlcom -_b[fsts]/(2*_b[c.fsts#c.fsts])`; test with `utest` (Lind–Mehlum).

## 3. Python fallback (no Stata) — this environment

Reproducible pipelines already in `scripts/` (run from repo root):

| Task | Command |
|------|---------|
| Build/harmonise pooled dataset + PRISMA data-flow | `python3 scripts/build_pooled_dataset.py` |
| Per-ICRV descriptive tables (CD1) | `PYTHONPATH=scripts python3 scripts/cd1_descriptives_pipeline.py` |
| P7 turning-point reproduction check | `python3 scripts/p7_reestimate_check.py` |
| Filename canonicalisation / Asia filter / ≥2006 | `scripts/wbes_canon.py` (library) |

OLS with fixed effects in pure NumPy (no statsmodels needed): build a design matrix
with `fsts`, `fsts2`, controls, and `pd.get_dummies(country)`, `pd.get_dummies(year)`;
solve `np.linalg.lstsq`; turning point = `-b_fsts/(2*b_fsts2)`. See
`scripts/p7_reestimate_check.py` for a worked example.

### Currency comparability (critical)
Raw `ln_labor_prod` mixes national currencies. Before pooling levels, z-standardise
**within country-year**, and always include **country fixed effects** so the I–P
slope is identified from within-country variation. Cross-country level comparisons
must use ratios (ROS) or PPP — never raw labour-productivity levels.

## 4. Adding a new economy/wave (e.g. Japan-2025)

1. Place the standard cross-section `.dta` in `data_wbes/raw_dta/` (named
   `Economy-YEAR-full-data.dta`); `scripts/wbes_canon.py` parses it.
2. Re-run the relevant pipeline (§3). New waves ≥2024 and out-of-frame economies
   are listed in `data_wbes/analysis/DATA_UPDATE_MANIFEST.md`.
3. Econometric numbers in the manuscript change ONLY after the authors run the
   original P-study do-file on the expanded sample (per §0).

## 5. World Bank data via MCP

For macro context (WGI for ICRV, GNI, PPP deflators), the project ships two MCP
servers configured in `.mcp.json`: `world-bank` (World Bank Open Data API) and
`data360` (World Bank Data360). Use them to pull indicators rather than hard-coding.
