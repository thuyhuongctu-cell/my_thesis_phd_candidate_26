# P3 Paternoster z-flag — verification (2026-06-19)

**Question.** Ch4 reports two Paternoster z near 3.35 — line 356 z=3,353 (turning-point shift,
2009 vs 2015) and line 374 z=3,35 (DAI-coefficient shift, 2009 vs 2015). Are these a copy-paste
duplication of one statistic, or two genuinely distinct tests?

**Method.** Independent recompute on the same prebuilt data the committed R replication uses
(`data_wbes/analysis/pooled_wbes_6waves.csv`, VNM subset; HC1 SE), reproducing the per-wave specs.

**Result.**

| Test | spec | 2009 | 2015 | Paternoster z (2009v2015) |
|---|---|---|---|---|
| TP shift (FSTS linear) | M2 exporters: lnLP~FSTSc+FSTScsq+ctrls | FSTSc −1.85 | FSTSc +1.21 | z_lin = −3.53 (p<.001) |
| TP shift (FSTS²) | (same) | FSTScsq +0.98 | FSTScsq −2.91 | z_sq = +3.22 (p=.001) |
| DAI shift | lnLP~FSTSc+FSTScsq+DAI+ctrls | DAI +0.70 | DAI +0.20 | z = +3.10 (p=.002) |

**Conclusion.**
1. The two reported values are **two genuinely different tests** (one on the FSTS quadratic
   coefficients, one on the DAI coefficient) that coincidentally both fall near 3.3 — **not a
   duplication error**. The thesis values (3,353 and 3,35) are legitimate and stand.
2. The recompute confirms the substantive claims independently: the turning-point shift 2009→2015
   is strongly significant (|z|≈3.2–3.5), and the DAI trajectory is non-monotonic (strong 2009 →
   dip 2015 → recover 2023) with a significant 2009→2015 shift.
3. **Spec caveat (for the candidate).** The thesis's reported DAI *coefficient magnitudes*
   (+0.175 in 2009 etc.) come from a different DAI specification than this simple replication
   (which yields +0.70 in 2009); the non-monotonic *pattern* and the *significance* of the shift
   reproduce, but the candidate should confirm the exact DAI model spec (standardised vs raw;
   nested moderation vs main effect) against her P3 Stata output so the printed coefficient
   magnitudes match the spec described in §4.5.6.

---

## Follow-up: §4.5.6 DAI per-wave coefficient spec (reviewed 2026-06-19)

**Finding.** The §4.5.6 DAI coefficients (DAI_z: 2009 +0.175, 2015 −0.044, 2023 +0.095,
pooled +0.078) are **not reproducible from the committed harmonised replication**
(`pooled_wbes_6waves.csv`, the data the committed P3 R script reads). Recomputes on that CSV:

| Spec (VNM, HC1) | 2009 | 2015 | 2023 | pooled |
|---|--:|--:|--:|--:|
| DAI_z only (lnLP~FSTSc+FSTScsq+DAI_z+ctrls) | +0.262 | +0.080 | +0.179 | +0.171 |
| M8 full (TCI_z+DAI_z+interactions) | +0.057 | +0.077 | +0.102 | — |
| **Thesis §4.5.6** | **+0.175** | **−0.044** | **+0.095** | **+0.078** |

**Diagnosis.** The thesis numbers derive from the **P3 manuscript Stata build**
(`p3/replication/do/01_build_vietnam.do` → `02_run_models.do`), which differs from the
committed harmonised CSV path in (a) FSTS = **direct exports only** (`d3c`) vs the pooled
`export_pct`; (b) **wave-specific** raw-`.dta` field mappings; (c) winsorise **within wave**;
(d) the DAI estimation sample (`dai_samp`). A direct raw-`.dta` port was attempted but the
per-wave PICS3/Standardized/BREADY schemas differ (the 2009 file lacks `b1_d`; the 2015 file
has a string-encoding issue), so the manuscript build cannot be reproduced here without the
original Stata environment.

**Status of the claim.** The **substantive** result — DAI follows a non-monotonic trajectory
(strong 2009 → weak/null 2015 → recovery 2023) — reproduces qualitatively across specs
(e.g., DAI_z-only: +0.262 → +0.080 → +0.179 still dips at 2015). Only the **exact magnitudes
and the 2015 sign** are build-dependent.

**Recommendation (candidate action, not auto-changed).** Reconcile the two paths so §4.5.6 is
reproducible for examiners/reviewers: either (a) re-run `01/02_*.do` in Stata, confirm the
printed coefficients, and commit the resulting `vietnam_*_analytic.dta` + an estimates table so
the numbers are auditable; or (b) if the harmonised CSV is the canonical path, update §4.5.6 to
the CSV-reproducible DAI_z values. No thesis number was changed pending the candidate's choice of
authoritative build.
