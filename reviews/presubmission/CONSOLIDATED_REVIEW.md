# Pre-Submission Review — Consolidated Report (P3–P9)

**Date:** 2026-06-09 · **Method:** `pre-submission-reviewer` skill (5 dimensions + banned-vocab + house-style), one reviewer per paper. Per-paper detail: `reviews/presubmission/PX_review.md`.

## Scoreboard

| Paper | Target | CRIT | MAJOR | MINOR | Score | Recommendation |
|---|---|:--:|:--:|:--:|:--:|---|
| P3 Vietnam | JED | 3→0* | 6 | 6 | 7.0 | 1–2 days |
| P4 Singapore | MBR | 0 | 6 | 7 | 7.0 | minor–moderate |
| P5 China | IJOEM | 0 | 5 | 9 | 7.5 | minor |
| P6 Meta | JIM | 1→0* | 5 | 7 | 7.0 | minor–moderate |
| P7 Capstone | IBR | 0 | 6 | 9 | 6.5 | minor–moderate |
| P8 Pacific SIDS | JID | 1 | — | — | 6.5 | **fix CRITICAL first** |
| P9 India | MIR | 0 | 7 | — | 7.0 | minor |

\* CRITICAL items already fixed this session (see below). No paper has unresolved CRITICAL except P8's estimation-N framing (partially fixed; abstract decision pending author).

## ✅ Fixed automatically this session (safe, no fabrication)
1. **P6 (CRITICAL):** jim package header + Figure-1 note named the wrong journal (International Business Review) → corrected to **Journal of International Management (JIM)**.
2. **P8 (CRITICAL, partial):** text claimed "N = 959 for M1" but the reanalysis CSV confirms the country+year FE model (β = −1.339) is estimated on **N = 209** complete cases (only the bivariate uses 959). Line 214 corrected. **Abstract framing flagged for author** (see below).
3. **P9:** AI-tone regression removed (`unprecedented`×4, `transformative`) from source + 3 manuscripts + build script + 3 cover letters; **title** in MIR cover/title-page aligned to the manuscript title ("When Institutional Transformation Breaks the Threshold…").
4. **All papers:** spaced thousands separators ("2, 610" → "2,610") fixed in 6 manuscripts (P5: 42, P7: 29, P6: 8, P3/P4/P8: 5 each).

## ⏳ Author-action items (need data verification or author judgment — not auto-fixable)

### CRITICAL / high priority
- **P8 abstract framing:** the headline FE betas (β = −1.339 country+year FE; β = −3.351 year-FE) are estimated on **N = 209** (complete cases on controls), while "959 firms" is the full sample (used only in the bivariate, β = −0.864). Decide how to present honestly: either report the estimation N alongside each beta, or address the control-variable missingness (re-impute / reduced control set) to retain N. Also: **Table 1 is empty** (fill country-level summary stats), and **TCI "p = .003 (n.s.)" is mislabelled** (p = .003 is significant — remove "n.s.").

### Internal number reconciliations (verify against your tables/data)
- **P3:** 2023 turning point 41.6 vs 42.0; exporter-only headline p = .660 vs .730. Also verify all fixes land in the **`01_manuscript_blinded_8500.md`** (the file actually submitted to JED), not only the full version.
- **P4:** turning point 82% (§4.2) vs 88.6% (elsewhere); M8 interaction −1.177 (text) vs −1.167 (Table 2).
- **P5:** §3.3 claims a 217-firm cross-wave "panel core" but §5.4 says WBES anonymisation makes panel matching impossible — resolve the contradiction. Cover letter mis-frames the full private-firm sample as "manufacturing". Package metadata (table count 3 vs 4; word count; JEL/keywords) disagrees with the manuscript.
- **P7:** M10 in-text coefficients (+0.763/+1.762/−2.746) contradict Table 3 (+0.729/+1.636/−2.501); abstract advertises H1–H4 but body tests H1–H6; stray "34 economies" vs the 49-economy framing; "HongKong" → "Hong Kong"; DAI premium 16% vs 17%.
- **P6:** Regime-I k mismatch (108 studies / 140 effects vs k = 139); undefined "CDCM" at line 1060 (should be "cDAI amplification (H3)"); 5-vs-6 ICRV regime labelling with a dangling "Regime V".
- **P9:** pooled N 28,717 vs 28,742 (§4.4); structured abstract ~600 words vs the ≤250 claim (condense); "three contributions / H1–H3" framing mislabels the actual H1 / H2a-b / H3a-b / H4a-b set.

### Missing references (cited in text, absent from reference list — add from your library)
- **P3:** World Bank (2025b), World Bank (2025c)
- **P4:** Teece (2007), Coase (1937), Williamson (1985), Leon (2004)
- **P5:** Johanson and Vahlne (1977), Helpman et al. (2004)
- **P7:** Stallkamp and Schotter (2021)
- **P8:** Mahler, Serajuddin, Wadhwa and Yonzan (2026)
- **P9:** Hutzschenreuter et al. (2026)

### Orphan references (listed but never cited — remove or cite)
- P3: Wolfolds and Siegel (2019); P4: 7 orphans; P5: Meyer et al. (2017); P6: Jensen & Meckling, Lakens et al., Paternoster et al.; P7: 6 orphans; P9: ~12 orphans.

### House-style polish
- **Harvard "&" → "and"** in narrative citations (Emerald packages P4, P5).
- **P3:** Table III significance footnote is inverted/non-standard; consolidate the DAI Tier-1 caveat (repeated 5+ times); fix orphaned " , " appositives left by an earlier em-dash pass.
- **P6 / P7:** split run-on sentences left where em-dashes were stripped.

## Clean across all papers (verified)
- Em-dashes: 0 in all 7 manuscripts. Banned AI-tone: 0 genuine (domain terms "superior performance", "pioneering study", "general-purpose technologies" correctly retained). No author-identity leaks in blinded manuscripts. P8 fully 7-SIDS/N=959 consistent. P6 citation-anchored PRISMA + two-author ICR framing intact.

## Bottom line
The seven papers are **scientifically sound and structurally complete**; remaining work is **revision hygiene** (number reconciliation, reference completeness, P8 estimation-N transparency). No paper needs a major rewrite. Recommended order: P8 (estimation-N + Table 1) → number reconciliations → reference lists → house-style polish.
