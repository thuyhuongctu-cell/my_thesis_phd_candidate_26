# P6 Meta-Analysis — Reproducibility Run 2026-06-23

Hardening run for study P6 (internationalization–firm-performance three-level
meta-analysis, MARA). P6 is a meta-analysis of **published effect sizes** — there
is **no WBES `.dta`** to re-run. The "model run" is the meta-analysis computation
over the committed coded study database.

## Command

```
python3 scripts/p6_meta_analysis.py
```

- Input: `p6/results/forest_data.csv` (K=288 effect rows, k=238 unique study_ids).
  Same sample as `p6/data/p6_study_database.csv` filtered to `include_flag == 1`.
- Output: `p6/results/p6_meta_computed.md` (the script's own DEPRECATED cross-check file).
- Environment: Python 3 + numpy/pandas/scipy. R 4.3.3 is present but the canonical
  estimator package `metafor` is **MISSING** and cannot be installed offline, so the
  canonical R pipeline (`p6/scripts/p6_real_mara.R`) **cannot be re-run here**.

## Recomputed numbers (this run)

| Quantity | Recomputed | Canonical target | Match |
|---|---|---|---|
| Pooled r̄ | **0.074** [0.060, 0.088] | 0.074 [0.060, 0.088] | **Y** |
| k (studies) | **238** | 238 | **Y** |
| K (effects) | **288** | 288 | **Y** |
| Q_M ICRV | **17.35** (df 4, p .002) | 17.35 | **Y** |
| Q_M cDAI | **1.23** (p .541) | 1.23 | **Y** |
| Q_M DPL | **0.56** (p .755) | 0.62 | N (minor; both n.s.) |
| I² total | **87.8%** | 62.4% | **N (expected)** |
| Q total | not emitted | 1909.42 | N/A |
| Egger p | **0.007** | 0.057 | N (expected) |
| Trim-and-fill | **~10** imputed | 57 | N (expected) |

## Match vs canonical

- **Headline pooled effect r̄ = 0.074, 95% CI [0.060, 0.088] — MATCHES canonically.**
- **k = 238 studies — MATCHES the canonical target (k = 238).** See the k flag below.
- **K = 288 effect sizes — MATCHES.**
- **Moderation Q_M for ICRV = 17.35 — MATCHES** (the H1/H2/H3 hypothesis test). cDAI
  Q_M = 1.23 also matches; DPL Q_M = 0.56 vs canonical 0.62 is a minor divergence,
  both non-significant.
- **I² = 87.8% (this run) vs 62.4% (canonical) — DOES NOT MATCH, and this is EXPECTED
  and documented.** The canonical I², Q_total, ICRV subgroup r, Egger b, and
  trim-and-fill k come from the R `metafor::rma.mv()` three-level pipeline
  (`p6/scripts/p6_real_mara.R` → `table1_baseline.csv` … `table5_sensitivity.csv`),
  which is the **source of truth** used by all three submission manuscripts. The
  Python script is an explicitly NON-CANONICAL independent cross-check whose own
  header documents that it diverges (I² ≈ 87.8%, trim-fill ≈ 10, Egger p ≈ 0.007)
  because of a different variance-component implementation. It is NOT cited anywhere.

## k = 238 — does it match the target? YES, but with the standing flag

The committed coded database **actually yields k = 238 unique studies and K = 288
effect sizes** — both the canonical `forest_data.csv` (238 unique `study_id`) and
`p6/data/p6_study_database.csv` (288 rows with `include_flag == 1`, 238 unique
studies) agree. So the recomputed k **matches** the canonical target of 238.

HOWEVER, the standing flag in `data_wbes/analysis/CANONICAL_NUMBERS.md` remains true:
k = 238 is still flagged "CẦN hoàn tất search/extraction thật" (the real WoS
search/extraction is not yet fully completed). The coded database covers S01–S237
(k = 237); S238 (Srividhya & Vidya 2024) was added **directly** to `forest_data.csv`
as row E288 from a WoS arm search and is not present in the coded markdown database.
No new studies were invented in this run — k = 238 is recomputed from committed data
only, and the value is reported honestly with this provenance caveat.

## Conclusion

The reproducible, in-environment computation confirms the **headline meta-analytic
result (r̄ = 0.074, k = 238, K = 288, Q_M ICRV = 17.35)**. Heterogeneity /
publication-bias statistics (I², Q, Egger, trim-fill) are owned by the R `metafor`
pipeline and cannot be regenerated here because `metafor` is not available; their
divergence in the Python cross-check is expected and already documented.
