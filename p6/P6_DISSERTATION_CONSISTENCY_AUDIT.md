# P6 ↔ Dissertation Consistency Audit

> Date: 2026-05-27 · Scope: verify that every P6 (three-level meta-analysis) statistic and claim
> used across the dissertation matches the verified P6 manuscript, and that P6 (meta-analysis) is
> not conflated with P7 (the multi-country empirical analysis).

## Verdict
- **Numbers: CONSISTENT.** ✅ Every P6 statistic in the dissertation body matches the verified P6.
- **One framing nuance to tighten (candidate's call).** ⚠️ See §2.
- **Scope label: minor.** ℹ️ See §3.

## 1. Numbers check — PASSED ✅
The verified P6 values (r = .074; 95% CI [.060, .088]; I² = 87.8% = 76.1% L2 + 11.8% L3;
ICRV Q_M = 17.35, df = 4, p = .002 — **but NOT robust: drop-FR core-regime Q_M = 1.49, df = 3,
p = .68** (see table5_sensitivity.csv); cDAI Q_M = 1.23, p = .541 ns; DPL Q_M = 0.56, p = .755 ns;
trim-and-fill k = 58 → r = .035, ~53%; Begg p = .0007; fail-safe N = 45,848; FR r̄ = .349, K = 3)
appear **correctly** in:
- `thesis/chuong_2_tong_quan_tai_lieu_vi.md` (§ lit-review backbone, line ~178) — incl. the correct
  "single- vs multi-country composition" hedge on Q_M.
- `thesis/chuong_4_ket_qua_vi.md` (lines ~107–131) — incl. cDAI/DPL **correctly reported as
  non-significant**, the Frontier cell flagged as fragile (K = 3, one outlier), and ~53% bias.
- `thesis/tom_tat_noi_dung_vi.md` (lines ~81, 277) — full split 76.1/11.8, trim-fill, fail-safe N.

**The obsolete/contradictory numbers (an old mis-attribution of heterogeneity to the between-study
level ≈ 65% L3, Q_M = 18.4, Advanced r̄ = 0.21, Frontier −0.02, cDAI β = .089 "significant", J-curve,
k = 235 / ~385, Asia-Pacific-only) were isolated to the old IBR cover letter / title page and have
been fixed** (mrq_package rebuild). None leaked into the dissertation body.

> **I² convention update (2026-05-29).** Total $I^2$ was revised from 62.4% (arithmetic-mean-of-$v_i$
> "typical variance" convention, prior draft) to **87.8%** (Higgins–Thompson typical-variance
> estimator, the `metafor` multilevel default), with the decomposition revised from 54.1%/8.4% to
> **76.1% L2 / 11.8% L3**. An independent Python re-analysis (`scripts/p6_reanalysis.py`) reproduces
> all headline statistics from `data/p6_study_database.csv` (20/20 metrics; see
> `results/reanalysis_reconciliation.csv`). The within-study-dominant story (L2 ≈ 6× L3) is
> unchanged; only the magnitude and the typical-variance convention changed. The three-level total
> (87.8%) is now essentially identical to the single-level ICBEF baseline (87.92%), with the
> three-level model contributing the correct partition across levels rather than a different total.

## 2. Framing nuance — ICRV "gradient confirmed" vs "regimes differ" ⚠️
Two consistent-but-differently-pitched framings coexist:
- **Honest (matches P6):** `chuong_4_ket_qua_vi.md:123` — the directional gradient (Advanced largest
  → Frontier smallest) is **not** confirmed; Q_M significance is driven by the single- vs
  multi-country split and a fragile Frontier spike, "**chưa phải một dải biến thiên đơn điệu**."
- **Stronger pitch:** `04_05_chapters_results_discussion_vi.md:139/198/218` and the H5 rows
  (`chuong_4:288`) present Q_M = 17.35 as confirming an "ICRV **gradient**," alongside the empirical
  FSTS×ICRV interaction.

Both can be true if H5 is defined as "institutions moderate I-P" (the **empirical/P7** confirms the
concavity gradient at p < .001; P6 confirms only that **regimes differ**, not a monotone gradient).
**RESOLVED (2026-05-28).** A drop-FR sensitivity test was added to the meta-analysis pipeline
(`65_meta_analysis.py` → `table_icrv_dropFR_sensitivity.csv`): removing the 3-study Frontier cell collapses the
ICRV omnibus from Q_M = 17.35 (p = .002) to **Q_M = 1.49 (df = 3, p = .68)**, i.e., not robust and on
a par with cDAI/DPL. The manuscripts (EN + VI), `chuong_2`, and `chuong_4` were revised so P6 is cited
precisely: the literature-level main-effect moderation (institutional **and** digital) is weak/not
robust, and the institutional contingency is established by the firm-level **conditional interaction**
(FSTS×ICRV, FSTS²×ICRV, p < .001) in the multi-country empirical analysis (P7). This converts the
moderator nulls from an apparent weakness into the gap that motivates the dissertation's conditional
specification. The superseded `04_05_chapters_results_discussion_vi.md` (banner-marked, not for
submission) was left as-is by design.

## 3. Scope label — "Asia-Pacific" vs "global/49 economies" ℹ️
Some dissertation lines label the meta-analysis corpus "châu Á và Thái Bình Dương." The P6
manuscript frames it as a **globally representative corpus of 49 economies with an Asia-Pacific
majority (~52% of k)** — so the AP label is *incomplete*, not wrong. Optional: phrase as "globally
representative (49 economies; Asia-Pacific majority)" where the meta-analysis scope is introduced
(e.g., `chuong_2:178`), to match the manuscript exactly.

## Bottom line
No number-level landmines remain in the dissertation. The only items are (a) a precise-wording
tightening of the P6 contribution to H5, and (b) an optional scope-label clarification — both are
narrative decisions for the candidate/advisor, not mechanical fixes.
