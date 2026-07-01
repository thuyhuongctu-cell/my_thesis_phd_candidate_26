# P3/P4/P5 Manuscript QA Report
Date: 2026-05-13
Branch: claude/edit-vietnamese-academic-standards-xcAmn
Analyst: Claude Code (automated QA run)

---

## P3 (Vietnam) — Language Quality

### 1. Banned / Quasi-Significance Phrases

Four instances of **"marginal significance"** were found. This phrase is on the ban list because it implies graded significance rather than treating p-values as a binary threshold.

| Line | Instance |
|------|----------|
| 533 | "the joint test sits at marginal significance (M4 joint p = .102; M8 joint p = .062)" |
| 620 | "The joint Wald test sits at marginal significance (M8 joint p = .083)" |
| 622 | "reaches marginal significance only in 2023 (M4 joint p = .102; M8 joint p = .062)" |
| 685 | "is also at marginal significance, driven by the 2023 wave" |

**Recommended fix:** Replace with factual p-value reporting without the evaluative label. Example: "the joint test does not reach the conventional α = .05 threshold (M4 joint p = .102; M8 joint p = .062)."

No instances of "marginally significant", "trending toward significance", "nearly significant", "bare significant", or "approach significance" were found.

### 2. Overconfident Language

| Line | Word | Context | Assessment |
|------|------|---------|------------|
| 24 | "demonstrates" | Originality/value: "…demonstrates that pooled digital coefficients on a Tier-1 binary mask progressive proxy obsolescence" | **Flag** — reporting own observational finding with causal-implying verb. Prefer "the findings are consistent with…" or "the pattern suggests…" |
| 130 | "demonstrate" | Citing Pisani et al. (2020): "demonstrate that the inverted-U relationship weakens" | Acceptable — attributing to published meta-analysis. |
| 1189 | "demonstrates" | "The dip demonstrates why pooled averages alone are insufficient" | **Flag** — overconfident claim from one wave's data. Prefer "illustrates" or "is consistent with the view that". |
| 558 | "confirms" | "confirms that only the DAI direct shifts are cross-wave-distinguishable" | Acceptable — reporting statistical test outcome. |
| 784 | "confirms" | "This formal test confirms the descriptive Paternoster" | Acceptable — reporting formal test outcome. |

No instances of "supports H[n]" or "confirms H[n]" without mechanism explanation were found.

### 3. Numerical Consistency

**Sample sizes:** Internally consistent throughout the manuscript.
- Wave-specific: 2009 N = 989; 2015 N = 956; 2023 N = 1,013; Pooled N = 2,958 (confirmed at L490, L501, and L1059–1062).
- Exporter-only: pooled N = 669 (L703).
- Manufacturing subsample: N = 1,854 (L725); Non-manufacturing: N = 1,104 (L728).
- All values are internally consistent across abstract, tables, and body text.

**Year mentions:** No inconsistencies. The three WBES waves (2009, 2015, 2023) are consistently referenced throughout.

**Turning point range:** Abstract states 39%–46%; Table LM shows 46.2% (2009), 39.3% (2015), 41.6% (2023), 39.7% pooled — band is 39.3%–46.2%. The abstract's rounded "between 39% and 46%" is consistent with the data.

### 4. Citation Cross-Validation (Sample of 20)

Citations were extracted from body text and matched against the manuscript's own References section (L1346 onward). The per-manuscript reference list was used as the authoritative source (the shared `thesis/04_references_apa7.md` file contains Vietnamese-language changelog notes that caused false negatives in automated matching).

**Result: No orphan citations found in P3.** All sampled citations verified present in the P3 reference list:
- Bharadwaj et al. (2013) — P3 L1351
- Cohen & Levinthal (1990) — P3 refs (cited as "Cohen and Levinthal, 1990" in body)
- Vial (2019) — P3 L1388
- Oster (2019) — P3 L1374
- Paternoster et al. (1998) — P3 L1375
- Lu & Beamish (2004) — P3 L1371
- Contractor (2007) — P3 L1356 (P3 cites Contractor 2007, not 2003)
- Lind & Mehlum (2010) — P3 refs

**Note on P3 AI statement (L1309):** A formatting artifact — "All con-" appears alone on a line, with the continuation "ceptual framing…" on L1311. This mid-word line break will produce visible formatting damage in the final document and must be corrected.

### 5. Statistical Language

Hedging language is well-used throughout (47 lines containing terms such as "associated with", "consistent with", "suggest", "indicate"). The ratio of hedging to overconfident usage is appropriate. Only two instances (L24, L1189) require attention.

---

## P3 (Vietnam) — Submission Check (APJM)

> **Critical discrepancy:** P3’s header (L5) states the target journal is **JABS (Journal of Asia Business Studies, Emerald Publishing)**, not APJM. The QA task specifies APJM. Checks below are run against both JABS and APJM requirements; the mismatch is flagged as Priority Action Item #4.

| Check | APJM | JABS | Status |
|-------|------|------|--------|
| Word count (body, excl. refs/tables) | 6,000–12,000w | 4,000–10,000w | Không ~15,551 body words — exceeds both limits. Total file ~19,327w. Major trimming required. |
| Abstract present | Có required | Có required | Có Present |
| Abstract word limit | ≤150w unstructured OR ≤250w structured | ≤250w structured | ⚠️ 315 words — exceeds APJM ≤250w structured limit by 65w; exceeds JABS ≤250w limit by 65w. Needs trimming. |
| Abstract format | Structured (Purpose/Design/Findings/Originality) | Structured accepted | Có All four sections present |
| Keywords | 4–6 | 4–6 | Có 6 keywords |
| Blind review | Double-blind | Double-blind | Có "Author details removed for blind review" marker at L3; no institutional/author names in body |
| Data availability statement | Required | Required | Có Dedicated section present (L1297) |
| Funding statement | Required | Required | Có Dedicated section present (L1293): "no specific grant from any funding agency" |
| Conflict of interest | Required | Required | Có Present (L1290) |
| AI usage statement | Required (Springer/Emerald policy) | Required (Emerald policy) | Có Present (L1305) — but see formatting artifact note |

---

## P4 (Singapore) — Language Quality

### 1. Banned / Quasi-Significance Phrases

One instance found:

| Line | Instance |
|------|----------|
| 99 | "The IMR enters with marginal significance (β = 0.264, SE = 0.138, t = 1.92, p = .055)" |

This appears within the Heckman robustness discussion. **Flag:** Replace with factual reporting: "the IMR coefficient does not reach the conventional p < .05 threshold (β = 0.264, p = .055)." The key inference — that the DAI × FSTS² interaction is robust — should be front-loaded.

No other banned phrases found.

### 2. Overconfident Language

No instances of "confirms H[n]", "supports H[n]", "proves", or "demonstrates" reporting own hypothesis tests were found. All flagged uses of "establishes/confirms" in P4 refer to setting baseline specifications or citing prior literature — none are overconfident hypothesis reporting. P4 is the cleanest of the three manuscripts on this dimension.

### 3. Numerical Consistency

**Sample sizes:** Internally consistent.
- Full analytic sample: N = 623 (L93, L108, L130).
- Main estimation sample: N = 617 (L166, L188, L190) — 6-firm difference due to missing controls; noted in table footnote.
- Exporters-only: N = 84 (L95, L200).
- All values cross-check across table headers and body prose.

**Year:** Single-wave 2023 Singapore study. No multi-wave consistency issue.

### 4. Citation Cross-Validation (Sample of 20)

| Citation in Text | In P4 Refs? | Notes |
|-----------------|-------------|-------|
| Hitt et al. (1997) | Có | |
| Contractor et al. (2003) | Có | P4 L265 |
| Lu & Beamish (2004) | Có | P4 L273 |
| Bharadwaj et al. (2013) | Có | P4 L259 |
| Cohen & Levinthal (1990) | Có | P4 refs |
| Cohen (1988) | Có | P4 refs — Cohen, J. (1988) statistical power |
| Coltman et al. (2008) | Có | P4 refs |
| Lind & Mehlum (2010) | Có | P4 refs |
| Wolfolds & Siegel (2019) | Có | P4 L284 |
| Antonakis et al. (2010) | Có | P4 refs |
| Marano et al. (2016) | Có | P4 refs |
| Shaver (2020) | Có | P4 refs |
| IMDA (2025) | Có | P4 refs (press release) |
| Peng (2003) | Có | P4 refs |
| Verhoef et al. (2021) | Có | P4 refs |

**Result: No orphan citations found in P4.**

### 5. Statistical Language

Strong hedging throughout (39 lines). P4 explicitly adopts "disciplined causal-language conventions" (associations not effects) and follows them consistently. No genuine overconfident hypothesis reporting found.

---

## P4 (Singapore) — Submission Check (GSJ)

> **Discrepancy:** P4’s header (L3) states the target journal is **MIR (Management International Review)**, not GSJ. Checks below cover both; the mismatch is flagged as Priority Action Item #4.

| Check | GSJ | MIR | Status |
|-------|-----|-----|--------|
| Word count (body, excl. refs/tables) | 6,000–12,000w | 5,000–12,000w | Có ~11,224 body words — within both limits |
| Abstract present | Có required | Có required | Có Present |
| Abstract word limit | ≤150w | ≤250w (MIR) | ⚠️ 201 words — within MIR; **exceeds GSJ ≤150w by ~51 words** if submitting to GSJ |
| Abstract format | Unstructured preferred | Unstructured preferred | ⚠️ Abstract is unstructured (narrative only, no section labels). Acceptable for MIR and GSJ. Would need restructuring if target changes to a structured-abstract Emerald journal. |
| Keywords | 4–6 | 4–6 | Có 6 keywords |
| Blind review | Double-blind | Double-blind | ⚠️ No explicit "author details removed" header marker (contrast with P3). No actual author names/affiliations in body text. "Corresponding author on reasonable request" at L245 is standard disclosure language, not an identification. Recommend adding explicit marker. |
| Data availability statement | Required | Required | Có Dedicated section present (L244) |
| Funding statement | Required | Required | Không No standalone Funding section. Acknowledgements (L247) thanks the World Bank for data but contains no "no specific grant" or funding declaration. |
| Conflict of interest | Required | Required | Không No Conflict of Interest statement found anywhere in P4. |
| AI usage statement | Required (Springer policy 2024+) | Required (Springer policy 2024+) | Không Absent from P4. |

---

## P5 (China) — Language Quality

### 1. Banned / Quasi-Significance Phrases

No instances of banned quasi-significance phrases found. Clean on this dimension.

**Borderline case (L325):** "the joint F-test on (FSTS × Tech, FSTS² × Tech) returns F = 3.26, p = .039 — marginal at the conventional .05 threshold with individual interactions null." The p = .039 result is technically significant at α = .05, but the descriptor "marginal" is potentially misleading. Recommend plain reporting: "the joint F-test reaches the α = .05 threshold (F = 3.26, p = .039), though neither individual interaction term is statistically significant."

### 2. Overconfident Language

| Line | Instance | Assessment |
|------|----------|------------|
| 45 | "**H2b (structural durability) is confirmed over H2a (environmental shift)**" | **Flag** — "confirmed" is too strong for a null finding (failure to reject coefficient equality). Prefer "supported" or "consistent with". |
| 265 | Section heading: "H2b supported — structural durability confirmed" | **Flag** — same issue. Revise heading to "H2b supported — structural durability not rejected". |
| 271 | "**The data support H2b (structural durability) over H2a (environmental shift).**" | Có Correct — uses "support" appropriately. |
| 317 | "the inverted-U curvature of the I–P relationship in China is a durable structural feature" | ⚠️ Stated as fact rather than inference. Suggest "the evidence is consistent with the inverted-U curvature being a durable structural feature." |
| 65 | "we identify and characterise an **optimal** export-intensity threshold" | ⚠️ "Optimal" implies normative optimality; the manuscript estimates a statistical turning point from cross-sectional OLS. Prefer "empirical turning point" or "estimated threshold." |

### 3. Numerical Consistency

**⚠️ Sample size inconsistency — requires author clarification and standardisation.**

The manuscript uses two different sets of N values in different contexts:

| Context | 2012 N | 2024 N | Pooled N |
|---------|--------|--------|----------|
| Abstract (L21) | **2,619** | **1,940** | **4,559** |
| Replication note (L134) | **2,619** | **1,940** | **4,559** |
| Table 1 header (L222) | **2,610** | **1,934** | — |
| Table 2 header (L245) | **2,610** | **1,934** | **4,544** |
| Body text L218 | **2,610** | — | — |

The discrepancy arises because 2,619 is the "sample_base" (firms with non-missing focal variables: sales, employees, FSTS), while 2,610 is the M2 estimation sample after additional listwise deletion of control variables (lnEmp, firmage, foreigndummy). This distinction is documented in the Replication note (L134) but is not clearly labeled in Tables 1 and 2, nor in the abstract.

**Recommended fix:** (a) Add a footnote to Table 1 stating "sample_base (N = 2,619/1,940); M2 estimation sample (N = 2,610/1,934) after listwise deletion of control variables." (b) Revise the abstract to report estimation-sample N (2,610 / 1,934 / 4,544) since those are the observations entering the focal models, and add a parenthetical "sample_base N = 2,619" for context.

### 4. Citation Cross-Validation (Sample of 20)

| Citation in Text | In P5 Refs? | Notes |
|-----------------|-------------|-------|
| Bharadwaj et al. (2013) | Có | P5 L441 |
| Vial (2019) | Có | P5 L508 |
| Paternoster et al. (1998) | Có | P5 L496 |
| Antonakis et al. (2010) | Có | P5 L435 |
| Manova (2013) | Có | P5 L486 |
| Foley & Manova (2015) | Có | P5 L464 |
| Eden & Nielsen (2020) | Có | P5 L458 |
| Lind & Mehlum (2010) | Có | P5 refs |
| Lu & Beamish (2004) | Có | P5 L482 |
| Contractor et al. (2003) | Có | P5 L451 |
| Marano et al. (2016) | Có | P5 refs |
| Schwens et al. (2018) | Có | P5 refs |
| Nambisan et al. (2019) | Có | P5 refs |
| MacKinnon & White (1985) | Có | P5 refs |
| World Bank (2013) | Có | P5 refs |

**Result: No orphan citations found in P5.** Citations that triggered false positives under surname-only matching (e.g., "Nielsen" to Eden & Nielsen 2020; "Piquero" to Paternoster et al. 1998; "Mehlum" to Lind & Mehlum 2010) are all correctly listed in full in the P5 reference section.

### 5. Statistical Language

Good hedging throughout (34 lines). The "confirmed" instances at L45 and L265 are the main concerns; the body text at L271 correctly uses "support."

---

## P5 (China) — Submission Check (IJOEM)

| Check | IJOEM requirement | Status |
|-------|-------------------|--------|
| Word count (body, excl. refs/tables) | 4,000–8,000w | Không ~15,228 body words — **~90% over the 8,000w upper limit**. Most urgent submission-readiness issue for P5. |
| Abstract present | Có required | Có Present |
| Abstract word limit | ≤250w structured | ⚠️ 311 words — **exceeds limit by ~61 words**. Needs trimming. |
| Abstract format | Purpose / Design / Findings / Originality | Có All four sections present, bold-formatted |
| Keywords | 5–8 (IJOEM convention) | Có 7 keywords |
| Blind review | Double-blind | ⚠️ No "author details removed" header marker. Replication note at L522 states "handle withheld for blind review" — adequate, but adding a header marker (as P3 does) is standard practice. No author names or institutional affiliations in body text. |
| Data availability statement | Dedicated section required (Emerald policy) | Không **No standalone Data Availability Statement section.** Data access information is embedded in Section 3.1 (L138) and Acknowledgements (L427). A dedicated section must be added before References. |
| Funding statement | Required | Có Present in Acknowledgements (L429): "no specific grant from any funding agency" |
| Conflict of interest | Required | Có Present in Acknowledgements (L429): "no conflicts of interest" |
| AI usage statement | Required (Emerald policy) | Không **Absent.** Emerald Publishing requires disclosure of AI tool use. Add statement (parallel to P3’s wording at L1305–1313). |

---

## Summary Comparison Table

| Dimension | P3 (Vietnam) | P4 (Singapore) | P5 (China) |
|-----------|-------------|----------------|------------|
| Banned quasi-significance phrases | ⚠️ 4 × "marginal significance" | ⚠️ 1 × "marginal significance" | Có None (1 borderline case L325) |
| Overconfident language (own findings) | ⚠️ L24, L1189 | Có None | ⚠️ L45 "confirmed"; L265 section heading |
| Sample N consistency | Có Consistent | Có Consistent | Không 2,619 vs 2,610 discrepancy across abstract and tables |
| Citation orphans (cited but not in refs) | Có None | Có None | Có None |
| Abstract word count | ⚠️ 315w (limit ~250w) | ⚠️ 201w (MIR OK; GSJ over) | ⚠️ 311w (limit 250w) |
| Abstract structure | Có Structured 4-section | ⚠️ Unstructured narrative | Có Structured 4-section |
| Keyword count | Có 6 | Có 6 | Có 7 |
| Blind review marker | Có Explicit header marker | ⚠️ No header marker | ⚠️ No header marker |
| Data availability statement | Có Dedicated section | Có Dedicated section | Không Missing as dedicated section |
| Funding statement | Có Dedicated section | Không Missing | Có In acknowledgements |
| Conflict of interest statement | Có Present | Không Missing | Có In acknowledgements |
| AI usage statement | Có Present | Không Missing | Không Missing |
| Body word count vs journal limit | Không ~15,551w (limit ~10–12k) | Có ~11,224w (within limits) | Không ~15,228w (limit 8,000w) |
| Target journal header matches task | Không JABS ≠ APJM | Không MIR ≠ GSJ | Có IJOEM = IJOEM |

---

## Priority Action Items

### P1 — Critical (blocks submission)

1. **[P5] Word count** (~15,228 body words vs 8,000w IJOEM limit): Approximately 90% over limit. Move detailed robustness panels to online supplementary materials, consolidate discussion, and shorten literature review. This is the single most urgent revision across all three manuscripts.

2. **[P3] Word count** (~15,551 body words vs ~10,000–12,000 JABS/APJM limit): Approximately 30–55% over limit depending on target journal. Similar structural condensation required.

3. **[P5] Sample N inconsistency** (abstract/replication note: N = 2,619/1,940/4,559 vs tables: N = 2,610/1,934/4,544): Inconsistency will be flagged by any careful reviewer. Fix: align abstract to use estimation-sample N (2,610/1,934/4,544) and add a footnote to Table 1 explaining the distinction between sample_base and estimation sample.

4. **[P3, P4] Target journal mismatch**: P3 header names JABS (Emerald); task specifies APJM (Springer). P4 header names MIR; task specifies GSJ. These are different publishers with different style guides, abstract formats, section heading conventions, and word limits. Clarify intended submission outlet before committing formatting effort.

### P2 — Required before submission (likely desk-reject if absent)

5. **[P5] Add Data Availability Statement section**: Emerald requires a dedicated section header. Consolidate the data-access text from Section 3.1 L138 and Acknowledgements L427 into a new "## Data Availability Statement" section placed before References.

6. **[P5] Add AI usage statement**: Emerald Publishing requires disclosure per author guidelines effective 2023. Model on P3’s statement (L1305–1313).

7. **[P4] Add Funding section and Conflict of Interest statement**: Both are required by MIR (Springer) and GSJ (Wiley). Add a "## Funding" section ("This research received no specific grant…") and a "## Conflict of Interest" section before References.

8. **[P4] Add AI usage statement**: Required by Springer’s research integrity policy (effective 2024 for all Springer journals including MIR).

9. **[P3, P4, P5] Abstract word count**:
   - P3: 315w — trim by ~65w to meet ≤250w structured limit (JABS/APJM).
   - P4: 201w — acceptable for MIR (≤250w); trim by ~51w if target is GSJ (≤150w).
   - P5: 311w — trim by ~61w to meet IJOEM ≤250w limit.

### P3 — Language quality issues (fix before external review)

10. **[P3] "Marginal significance" phrases (4 instances)**: Lines 533, 620, 622, 685. Replace with plain p-value statements: "the joint test does not reach the α = .05 threshold (p = .102)" etc.

11. **[P4] "Marginal significance" phrase (1 instance)**: Line 99. Replace with: "the IMR coefficient does not reach the conventional threshold (β = 0.264, p = .055)."

12. **[P5] "H2b is confirmed" overconfidence**: Lines 45 and 265 (section heading). Replace "confirmed" with "supported" or restructure as "H2b not rejected."

13. **[P3] "Demonstrates" overconfidence**: Lines 24 and 1189. Replace with "suggests" or "is consistent with."

14. **[P3] AI statement formatting artifact**: Lines 1309–1311 contain a mid-word split ("All con-" / "ceptual framing…"). Merge into a single paragraph.

### P4 — Lower priority (good practice)

15. **[P3, P4] Add explicit blind-review header markers**: P4 currently lacks the "Author details removed for blind review" header line. Add to P4 header (L1–L5 area). P5 handles this inline at L522 but a header marker is standard.

16. **[P5] L325 borderline quasi-significance language**: Rephrase "marginal at the conventional .05 threshold" to plain p-value reporting.

17. **[P5] "Optimal" threshold language (L65)**: Replace "optimal export-intensity threshold" with "empirical turning point" or "estimated export-intensity threshold."

---

*Report covers: 100% of p3_vietnam_en_clean.md (128,756 chars / 1,399 lines), p4_singapore_en_clean.md (89,951 chars / 298 lines), p5_china_en_clean.md (115,899 chars / 521 lines), and thesis/04_references_apa7.md (69,156 chars / 651 lines). All four files read in full.*
