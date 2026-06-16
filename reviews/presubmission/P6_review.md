# P6 Pre-Submission Review — Three-Level Meta-Analysis of I to P (target: JIM, Journal of International Management, Elsevier/APA)

**Source reviewed:** `p6/submission/jim_package/01_manuscript_blinded.md` (full, 1678 lines)
**Supporting:** `p6/submission/jim_package/README.md`, `p6/P6_SUBMISSION_READINESS_CHECKLIST.md`
**Reviewer role:** academic pre-submission reviewer. No edits made; no git run.

---

## Summary

The manuscript is methodologically sound, internally consistent on its core numbers (k=238 / K=288; pooled r=0.074 [0.060, 0.088]; I²=62.5%; ICRV Q_M=17.35; cDAI Q_M=1.34; DPL Q_M=0.62; trim-and-fill adj r=0.035, k=57 imputed; fail-safe N=44,782), and the honest reframing the brief describes is in place: the search is presented as citation-anchored *systematic-but-bounded* (PRISMA 2020 "other methods" variant, Appendix A), not an exhaustive WoS/Scopus census; no residual "237/287", "S0129", "expansion pool", or "formal search pending" language survives; the publication-bias finding is correctly foregrounded and the moderator nulls are framed as informative bounds. The honest-framing gates (ICR κ/ICC "[insert after dual-coding]" cells; OSF DOI "[insert OSF DOI at submission]") are present and correctly intentional.

The single most serious problem is a **target-journal mismatch**: the manuscript header, version line, and Figure 1 note all name **International Business Review (IBR)**, but this is the **JIM** submission package. There are also two genuine internal inconsistencies (a Regime-I k count and an undefined "CDCM" acronym) and the expected must-fill gates. None of these is a CRITICAL methodological flaw, but the IBR/JIM mismatch will read as a copy-paste error to a JIM editor and must be fixed before submission.

## Counts

| Severity | Count |
|----------|-------|
| CRITICAL | 1 |
| MAJOR | 5 |
| MINOR | 7 |

## Top 3 fixes (do first)

1. **(CRITICAL) Wrong target journal named throughout.** Header line 3–5 reads *"Manuscript prepared for: International Business Review (IBR, Elsevier, IF ≈ 5.5, ABS-3)"* and Figure 1 note (line 537–538) ends *"Target journal: International Business Review (IBR, Elsevier, IF ≈ 5.5)."* This is the JIM package (README: *"Target: Journal of International Management (Elsevier · Q1)"*). Replace both with JIM (or, per APA blinded-manuscript norms, drop the explicit target-journal line entirely so the blinded file is journal-agnostic).

2. **(MAJOR) Fill the four pre-submission gates before upload.** (a) Six ICR value cells in Table 3.1 read `[insert after dual-coding]` (lines 912–917); (b) OSF DOI `[insert OSF DOI at submission]` in Methods Section 3.1 (line 597) and the Data Availability statement; (c) README checklist still has unchecked boxes (APA 7 ref style, appendices to supplements, title page separate). These are intentional gates, not inconsistencies, but the manuscript cannot be submitted until they are filled.

3. **(MAJOR) Reconcile the Regime-I k count.** Table 4.1 (Sample composition, line 925) reports ICRV Regime I = **140 effects / 108 studies**, but the ICRV results table (line 1000) and Discussion Section 5.1 (lines 1023, 1175) report Regime I as **k = 139**. Decide whether 139 is effects or studies and make the two tables agree (the Section 4.3 table column is headed *k* but the value 139 matches neither the 108 studies nor the 140 effects in Table 4.1).

---

## Per-dimension findings

### 1. Macro logic (intro chain to contributions to results to conclusion)

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M1 | CRITICAL | Target journal named as IBR (lines 3–5, 537–538) in a JIM package. | Change to JIM or remove the target-journal line. |
| M2 | MAJOR | Hypothesis numbering is internally crossed: Section 2.3 heading ties **DPL** to "Hm2" and the formal **H2** (lines 324, 383); Section 2.4 ties **cDAI** to "Hm3" and **H3** (lines 401, 466). But the Contributions paragraph (line 87) and Abstract describe results as "H2, H3 not supported" with cDAI Q_M=1.34 and DPL Q_M=0.62 — consistent — yet Section 4.4 (cDAI) is labelled "H3" and Section 4.5 (DPL) "H2", so the section order (cDAI before DPL) inverts the hypothesis order. Readable but invites confusion; verify H2=DPL and H3=cDAI is applied uniformly (it currently is, but the section ordering and the "E1a/E1b, H2, H3" list at line 87 should be checked once more). | Confirm/uniform-label; consider ordering result sections H1 to H2 to H3. |
| M3 | MAJOR | Abstract (line 9) and Conclusion claim "spanning 49 economies" and "first three-level MARA of I to P" — supported by body. Contributions list (lines 78–89) is consistent with results (H1 confirmed but driven by k=3 Frontier; H2/H3 null; H4 publication bias primary). Macro chain otherwise holds. | None beyond M1/M5. |
| M4 | MINOR | Abstract states *I²=62.5%* (consistent with body); the review brief's "62.4%" does not appear anywhere — manuscript is uniformly 62.5%. No action. | None. |

### 2. Writing details (topic sentences, redundancy, abstract structure)

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| W1 | MINOR | Abstract is a single unstructured paragraph (~256 words per README) — correct for Elsevier/JIM. Good. | None. |
| W2 | MINOR | Heavy repetition of the publication-bias result (r 0.074 to 0.035, k=57 imputed) across Abstract, Section 4.6, Section 5.2 Contribution 3, Section 5.3, and Conclusion. Defensible emphasis but at least one Discussion restatement (e.g., lines 1120–1126 vs. 1243–1253) is near-duplicative. | Trim one restatement. |
| W3 | MINOR | "Key findings preview" (lines 91–107) duplicates much of the Abstract and the Section 4 results verbatim (Q_M values, σ² values). Acceptable as a roadmap but consider tightening. | Optional trim. |

### 3. Grammar / English

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| G1 | MINOR | Comma-splice / missing dash where an em-dash was removed during the anti-AI pass leaves a run-on: line 26–27 *"is not merely academic it shapes investment decisions"* (double space, no connector); line 184–185 *"experiential learning curve predicting that"*; line 1274–1275 *"I to P literature where positive effects are over-represented, may be distorting"*. | Insert a connector/comma or restructure (e.g., "academic; it shapes…"). |
| G2 | MINOR | Several appositive lists use commas where the removed em-dash leaves ambiguity, e.g. line 131–133 *"resource endowments including human capital… access, will generate"*. Grammatical but the leading clause boundary is hard to parse. | Use parentheses or "(including …)". |
| G3 | MINOR | Number formatting: "44, 782", "2, 000", "1, 247.3", "1, 895.58", "6, 900" carry a space after the thousands comma (lines 505, 534, 957, 970, 1115, 1677). | Remove the space: 44,782 etc. |

### 4. Number / stat / citation consistency

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| N1 | MAJOR | Regime-I k mismatch: 108 studies / 140 effects (Table 4.1, line 925) vs. k=139 (line 1000, 1023, 1175). | Reconcile (see Top-3 #3). |
| N2 | MAJOR | **"CDCM" is undefined** (line 1060: *"required to test the CDCM gradient hypothesis"*). The theory is named CIMT and the cDAI mechanism is the "coordination platform effect" / "cDAI amplification (H3)". CDCM appears nowhere else and looks like a residual label. | Replace with "cDAI amplification (H3)" or define the acronym. |
| N3 | MINOR | DPL/Span k counts differ between tables: Table 4.1 composition (lines 935–936) lists Span=108, Follow=80, Precede=100; Section 4.5 results table (lines 1070–1072) lists Precede=100, Span=**107**, Follow=80. Span 108 vs 107. | Reconcile Span k (107 vs 108). |
| N4 | MINOR | cDAI Medium k: Table 4.1 composition (line 932) = 76; Section 4.4 results table (line 1048) = 75. | Reconcile (75 vs 76). |
| N5 | MINOR | Frontier r̄ = 0.35 (Abstract, line 9) vs 0.349 (Table, line 1003) vs 0.349 (Section 5.1, line 1195) — rounding only, internally fine; ensure Abstract rounds consistently (0.35). | Optional: 0.35 to 0.35 everywhere or 0.349. |
| N6 | OK | Core numbers consistent across Abstract↔body↔tables↔Fig 1 note↔Appendix C: r=0.074 [0.060,0.088], I²=62.5% (54.1%/8.4%), ICRV Q_M=17.35 (df=4, p=.002), cDAI Q_M=1.34 (p=.513), DPL Q_M=0.62 (p=.734), trim-and-fill k=57 to r=0.035 [0.018,0.051], Egger b=0.487 (p=.052), Begg τ=−0.132 (p=.001), fail-safe N=44,782. No "237/287" anywhere. README counts match. | None. |
| N7 | MINOR | Citation to reference check: all in-text cites resolve to the reference list. **Jensen & Meckling (1976)**, **Lakens et al. (2020)**, and **Paternoster et al. (1998)** appear in References (lines 1488, 1520, 1545) but are **not cited in the body** — orphan references (likely leftovers). **Bharadwaj et al. (2013)** is cited (line 440) and present. Remove the three orphans or add citations. | Remove orphan refs Jensen & Meckling, Lakens et al., Paternoster et al. |
| N8 | MINOR | Wu et al. (2022) is listed as *Journal of World Business, 52(2), 192–203* (line 1603–1606) — verify volume/year (JWB vol. 57 ≈ 2022; "52(2)" looks like a typo). | Verify Wu et al. citation details. |

### 5. House-style (JIM / Elsevier; APA; PRISMA; gates)

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| H1 | MAJOR | ICR κ/ICC cells `[insert after dual-coding]` (Table 3.1, lines 912–917) — intentional must-fill gate. | Fill after dual-coding; confirm κ≥0.70, ICC≥0.80. |
| H2 | MAJOR | OSF DOI `[insert OSF DOI at submission]` (line 597) and Data Availability — must-fill gate. | Insert real OSF DOI/URL. |
| H3 | MINOR | ICRV described as a **5-regime** framework in title/abstract/Section 2.2 but Appendix B and Section 3.4 code **6 codes** (I, II, III, FR/SIDS, MX, plus a "Regime V" reference category referenced at lines 171, 798 ["Regime V as reference"] though no Regime V row exists in any results table). "5-regime" vs "Six-code" (line 744) vs "Regime V" reference is inconsistent. | Reconcile the regime-count language (5 vs 6) and remove/clarify the dangling "Regime V" reference category. |
| H4 | MINOR | README still has unchecked boxes (APA 7 ref style; appendices to supplements; blinded uploaded/title page separate; Elsevier word note). Appendices A–C are currently inline. | Move appendices to supplementary; confirm APA 7. |
| H5 | OK | Abstract unstructured single paragraph; APA reference formatting; PRISMA appendix present; AI-disclosure (M-AIDA) statement present and consistent with checklist. | None. |

### 6. Banned vocab / em-dash scan

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B1 | OK | **No em-dashes (—) in the manuscript** — the anti-AI pass removed them (78 dash matches are all en-dashes "–" in page/number ranges and hyphenated terms, which are legitimate APA). | None. |
| B2 | OK | "general-purpose technologies" (line 330) = economics GPT concept — legitimate, not flagged. "pioneering study" (line 592) = seminal early work — legitimate, not flagged. | None. |
| B3 | MINOR | Mild AI-tone residue but no banned terms: heavy "the most …/first … to date" superlative stacking (lines 1218, 1250) and "actionable" (line 1251). Not disqualifying; soften if desired. | Optional. |

---

## Score

**7.0 / 10.** Methodologically strong, numerically consistent on its load-bearing statistics, and honestly reframed. Held back by the IBR/JIM target-journal mismatch (an embarrassing but trivial fix), two real internal count/acronym inconsistencies (Regime-I k; CDCM), three orphan references, the 5-vs-6 regime labelling, and the expected pre-submission gates (ICR κ/ICC, OSF DOI). All are fixable in a focused editing pass.

## Recommendation

**Minor-to-moderate revisions before submission.** Not ready to upload as-is solely because of the must-fill gates and the journal-name error. After (1) correcting IBR to JIM, (2) filling the ICR and OSF gates, (3) reconciling the Regime-I k and removing "CDCM", (4) removing the three orphan references, and (5) settling 5-vs-6 regime language, the manuscript is submission-ready for JIM.
