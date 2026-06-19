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
