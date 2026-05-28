# P6 ↔ Dissertation Consistency Audit

> Date: 2026-05-27 · Scope: verify that every P6 (three-level meta-analysis) statistic and claim
> used across the dissertation matches the verified P6 manuscript, and that P6 (meta-analysis) is
> not conflated with P7 (the multi-country empirical analysis).

## Verdict
- **Numbers: CONSISTENT.** ✅ Every P6 statistic in the dissertation body matches the verified P6.
- **One framing nuance to tighten (candidate's call).** ⚠️ See §2.
- **Scope label: minor.** ℹ️ See §3.

## 1. Numbers check — PASSED ✅
The verified P6 values (r = .074; 95% CI [.060, .088]; I² = 62.4% = 54.1% L2 + 8.4% L3;
ICRV Q_M = 17.35, df = 4, p = .002; cDAI Q_M = 1.23, p = .541 ns; DPL Q_M = 0.56, p = .755 ns;
trim-and-fill k = 58 → r = .035, ~53%; Begg p = .0007; fail-safe N = 45,848; FR r̄ = .349, K = 3)
appear **correctly** in:
- `thesis/chuong_2_tong_quan_tai_lieu_vi.md` (§ lit-review backbone, line ~178) — incl. the correct
  "single- vs multi-country composition" hedge on Q_M.
- `thesis/chuong_4_ket_qua_vi.md` (lines ~107–131) — incl. cDAI/DPL **correctly reported as
  non-significant**, the Frontier cell flagged as fragile (K = 3, one outlier), and ~53% bias.
- `thesis/tom_tat_noi_dung_vi.md` (lines ~81, 277) — full split 54.1/8.4, trim-fill, fail-safe N.

**The obsolete/contradictory numbers (I² > 80%, 65% between-study, Q_M = 18.4, Advanced r̄ = 0.21,
Frontier −0.02, cDAI β = .089 "significant", J-curve, k = 235 / ~385, Asia-Pacific-only) were
isolated to the old IBR cover letter / title page and have been fixed** (mrq_package rebuild). None
leaked into the dissertation body.

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
**Recommendation (candidate's call, not auto-edited):** where the meta-analysis (P6) is cited for
H5, state its contribution precisely — "P6 confirms regime *heterogeneity* (Q_M significant); the
monotone gradient/concavity mechanism is established by the multi-country empirical analysis (P7)."
This removes any appearance that P6 confirms a gradient its own results decline to support. Note
`04_05_chapters_results_discussion_vi.md` appears to overlap `chuong_4_*` + `chuong_5_*`; confirm
which is the canonical chapter file before editing to avoid divergent copies.

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
