# Reviewer-Perspective Audit — Dissertation & Six-Paper Portfolio

**Auditor role:** simulated journal reviewer / thesis-committee examiner
**Date:** 2026-06-08
**Scope:** P3–P8 submission packages, dissertation (`thesis/`), monographs (`chuyen_de/`)
**Method:** cross-document numeric consistency, placeholder scan, claim↔evidence, ground-truth checks against replication data/results.

---

## A. Defects FIXED in this pass

| # | Issue | Ground truth | Action |
|---|-------|--------------|--------|
| A1 | **P6 meta sample size inconsistent** — JIM & APJM packages reported *k* = 237 studies / *K* = 287 effects, while dissertation, IBR & JWB packages reported 238/288 | `p6/data/p6_study_database.csv` (288 rows, 238 unique `study_id`, all `include_flag = 1`) and `P6_results_workbook.xlsx` ("288 effects, 238 studies; pooled r = 0.074") → **k = 238, K = 288** | Corrected JIM + APJM manuscripts, JIM cover letter, READMEs to **238/288**. Repo-wide now 0 occurrences of 237/287 in any P6 package. |
| A2 | **P6 PRISMA terminal counts blank** ("k = [TBD] studies; K = [TBD]") | 238 / 288 | Filled terminal *included* counts (238/288) in JIM, IBR, JWB packages. |
| A3 | Em-dashes across all 6 first-target packages | — | Removed (0 em-dashes); docx rebuilt. |

(Earlier passes also fixed: P5 cover-letter 4-wave→2-wave drift; P6 cover-letter 288/238 mislabel; abstract formats per publisher house style.)

---

## B. CRITICAL issues the author MUST resolve before submission

### B1. P6 meta-analysis — PRISMA flow & inter-coder reliability are incomplete (29 `TBD` per package)
The manuscript reports **definitive results** (pooled *r* = 0.074, *I²* = 62.5%, *Q*_M tests, trim-and-fill *k* = 57) **but** the PRISMA flow intermediates (records identified → deduplicated → screened → excluded-by-reason) and the inter-coder reliability table (Cohen's κ, ICC) are all `[TBD]`, with a standing note that "all counts will be confirmed after the formal WoS/Scopus search." **A reviewer will read this as a meta-analysis run on a pre-formal-search convenience database.** These cannot be auto-filled or fabricated (no κ/PRISMA outputs exist in the repo).
**Required:** run and report the formal PRISMA search + double-coding reliability, *or* explicitly reframe the paper as a preliminary/working synthesis. This is the single biggest acceptance risk in the portfolio.

### B2. P6 — substantive contribution is thin once results are read honestly
- Publication bias is severe: trim-and-fill cuts the pooled effect from *r* = 0.074 to **0.035** (>50% attenuation).
- Two of three novel moderators are null (cDAI *Q*_M = 1.34, p = .513; DPL *Q*_M = 0.62, p = .734).
- The one "significant" moderator (ICRV, *Q*_M = 17.35) is **driven by a *k* = 3 Frontier anomaly**, not a monotone gradient (the paper says so).
**Reviewer concern:** the headline (first 3-level MARA; new moderators) rests on mostly-null moderators + a heavily bias-attenuated main effect. The framing should foreground the *publication-bias* finding as the primary contribution and treat the moderator nulls as informative bounds (the abstract already moves this way — extend it into the positioning/title).

### B3. P8 — "Pacific SIDS" label is geographically inaccurate (needs author decision)
P8 analyses **nine** economies (Fiji, Kiribati, PNG, Samoa, Solomon Is., Timor-Leste, Tonga, Vanuatu, **Comoros**), N = 1,469. **Comoros is in the Indian Ocean (East Africa), not the Pacific**; Timor-Leste is usually classed as Southeast Asia. Calling the sample "nine **Pacific** SIDS" (incl. the title framing) is a reviewer red flag. The monographs (CD1/CD2) use a different, truly-Pacific set of **7** economies. See Section C decision.

---

## C. Decision required from the author

**SIDS scope/label for P8** (affects sample, title, and dissertation↔paper consistency):
- **Option A (relabel, no re-analysis):** keep the nine-economy analysis but relabel as "nine Small Island Developing States (Pacific and Indian Ocean)" and drop "Pacific" from the framing/title. Reconcile CD1/CD2 (currently "7 Pacific SIDS") to the nine-economy set.
- **Option B (restrict to Pacific, re-analyse):** drop Comoros (and possibly Timor-Leste) to obtain a genuinely Pacific set (7–8 economies); re-estimate; this matches the monographs but requires re-running models and updating N.

---

## D. Cross-document distinctions verified as LEGITIMATE (no fix needed)

| Quantity | Resolution |
|----------|-----------|
| **47 vs 49 economies** | 49 = final WBES empirical pool (P7 + dissertation); 47 = earlier CD-era scope. Documented in `writing_guides/theory_measures_integration.md:707`. |
| **91,982 vs 101,185 vs 102,332 firms** | 102,332 = raw pool; **91,982 = analytic (non-panel) sample — the dissertation/P7 headline**; 101,185 = CD-era lock. Distinct, labelled. |
| **P7 headline** | 91,982 firms / 49 economies / 102 country-year waves — consistent across dissertation abstract and P7 manuscript. |
| **Figures** | All figures referenced in the 6 first-target packages have image files present; P7 & P8 are intentionally table-only. |

> **Note (author action at defense):** CD1/CD2 monographs still carry CD-era figures (101,185 firms · 47 economies · 7 Pacific SIDS). Since the dissertation declares it is built from these monographs, the committee may expect the monograph statistics to be reconciled to the final locks (91,982 · 49 · nine SIDS) or an explicit "data updated since monograph" note added. Same class of issue as the SIDS label.

---

## E. Reviewer-perspective scientific concerns (per paper) — recommended pre-emptive responses

**P3 (Vietnam, JED).** The inverted-U is explicitly a *participation-margin* effect (quadratic loses significance on exporters-only). Good that this is stated; reviewers will still ask for a hurdle/Heckman or exporters-only robustness in the main text, and the "proxy-obsolescence" Tier-1 claim should be bounded to the single website item. Endogeneity of TCI/export intensity is associational — keep the caveat prominent.

**P4 (Singapore, MBR).** The H3 amplification rests on the high-export tail where only ~3% of firms (exporters-only N = 84, power ≈ 16%) live. This is disclosed thoroughly (§3.4), but a reviewer may still regard H3 as under-identified; consider foregrounding it as a *conditional, power-bounded* finding rather than a confirmed mechanism. Now condensed to ~10.6k total.

**P5 (China, IJOEM).** Two-wave threshold-stability claim is clean; pre-empt a measurement-invariance question for the TCI composite across 2012 vs 2024, and keep the single-item DAI explicitly as a control (already done).

**P7 (49-economy, IBR).** Strength = scale. Reviewers will want: standard errors clustered by country and/or country-year; explicit treatment of WBES cross-country/cross-wave measurement comparability; and a multiple-comparisons note across the moderator battery.

**P8 (SIDS, JID).** Beyond B3, the FIP ("Forced Internationalization Penalty") construct needs to be defended as more than "a negative slope" — tie it to the three structural prerequisites (domestic market, trade costs, institutions) operationally. Exporter representation is thin (12.7%).

**Portfolio-wide.** (i) All identification is associational (single-wave or pooled cross-sections) — consistent causal-language discipline is needed. (ii) FSTS captures *direct* exports only (indirect/GVC participation excluded) — state as a measurement boundary. (iii) AI disclosure: journals (Emerald/Elsevier/Wiley) keep the Grammarly statement; the CTU thesis/monographs correctly omit it per CTU presentation rules.

---

## F. Suggested priority order
1. **B1** (P6 PRISMA/ICR) — blocking for P6 submission.
2. **C / B3** (P8 SIDS label) — author decision, then apply.
3. **B2** (P6 reframing toward the publication-bias finding).
4. **D-note** (reconcile CD monograph statistics or add data-update note).
5. **E** items — strengthen robustness/caveats per target-journal expectations.
