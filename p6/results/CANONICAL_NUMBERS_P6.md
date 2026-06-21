# P6 Canonical Numbers — single source of truth

_Locked 2026-06-21. Internationalization–performance three-level meta-analysis (MARA)._

## Authoritative pipeline

| | |
|---|---|
| **Canonical estimator** | R `metafor::rma.mv()` three-level model — `p6/scripts/p6_real_mara.R` (and `p6_mara_updated.R`) |
| **Canonical outputs** | `p6/results/table1_baseline.csv` … `table5_sensitivity.csv` |
| **Used by** | the P6 submission manuscripts (JWB, JIM, APJM) and the thesis — all mutually consistent |
| **NOT canonical** | `scripts/p6_meta_analysis.py` (simplified Python re-implementation) and its output `p6/results/p6_meta_computed.md` — **DEPRECATED** (diverges: I² ≈ 87.8%, trim-fill ≈ 10, Egger p ≈ 0.007) |

> R is **not installed** in this environment, so the canonical pipeline cannot be
> re-run here. The locked numbers below are taken from the committed `table*.csv`
> (R `metafor` outputs) and verified to match all three live manuscripts.

## Headline numbers (canonical)

| Quantity | Value | Source CSV |
|---|---|---|
| Baseline pooled effect | r = 0.074, 95% CI [0.060, 0.088], p < .001 | `table1_baseline.csv` |
| Effect sizes / studies | K = 288 effects, k = 238 studies | `table1_baseline.csv` |
| Heterogeneity | I² = 62.4% (between 8.4%, within 54.1%); Q = 1909.42, df = 287 | `table1_baseline.csv` |
| ICRV subgroup r | I 0.079 · II 0.065 · III 0.069 · FR 0.349 · MX 0.053 | `table2_icrv.csv` |
| cDAI subgroup r | L 0.075 · M 0.065 · H 0.091 | `table3_cdai.csv` |
| DPL subgroup r | PRE 0.082 · SPN 0.069 · FOL 0.073 | `table4_dpl.csv` |
| Publication bias | trim-and-fill k = 57 imputed; adjusted r = 0.035 [0.018, 0.051]; Egger b = 0.487 | manuscript |

## Q_M — two valid statistics, do not confuse them

The CSV `QM` columns and the manuscript report **different, both-valid** tests:

| Test | ICRV | cDAI | DPL | Meaning |
|---|---|---|---|---|
| **Manuscript Q_M** (moderation) | 17.35 (df 4, p .002) | 1.23 (p .541) | 0.62 (p .734) | Do subgroups **differ**? (with-intercept) — the hypothesis test (H1/H2/H3) |
| **CSV `QM` column** (omnibus) | 128.22 | 105.34 | 104.67 | Are **all** subgroup effects jointly = 0? (no-intercept) |

The manuscripts correctly report the **moderation** Q_M (between-group difference).
The CSV stores the no-intercept omnibus Wald. This is an artefact of the R model
parameterisation, **not** a manuscript error.

## Verification status (2026-06-21)

- The three live manuscripts (`p6/submission/{jwb,jim,apjm}_package/01_manuscript_blinded.md`)
  are mutually consistent on every headline number above (r, I², k/K, ICRV/cDAI/DPL r,
  Q_M 17.35/1.23/0.62, trim-fill 57, adj r 0.035, Egger 0.487).
- The Python cross-check output (`p6_meta_computed.md`) remains DEPRECATED and is not cited anywhere.
