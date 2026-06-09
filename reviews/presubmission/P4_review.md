# P4 Pre-Submission Review

**Paper:** Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore
**Target:** Multinational Business Review (Emerald, Harvard author–date)
**Source reviewed:** `p4/submission/mbr_package/01_manuscript_blinded.md` (full), `03_cover_letter.md`, `02_title_page.md`, `README.md`
**Reviewer role:** Academic pre-submission reviewer
**Date:** 2026-06-09

---

## Summary

The manuscript is well-structured, theoretically careful, and unusually honest about its inferential limits. The "inferential bounds / underpowered" framing is stated consistently and repeatedly (abstract, §1.1, §1.3, Figure notes, §3.3, §3.4, §4.2, §4.5, §7), with the power caveat (exporters-only N = 84, power ≈ 16%, f² ≈ 0.018) surfaced in every place a strong claim could be over-read. This is a genuine strength and the central caveat is honestly carried. The remaining issues are mostly consistency slips in reported statistics and a citation–reference set that does not reconcile bidirectionally — both of which a copy-editor or reviewer would flag quickly.

**Finding counts:** CRITICAL 0 · MAJOR 6 · MINOR 7

### Top 3 fixes
1. **Reconcile the turning-point number (MAJOR-1).** §4.2 reports the implied turning point "near FSTS = 82% on the original scale", while the abstract, §1.3, Figure 1 note, Figure 3 caption, §3.4(i) and §7 all use **88.6%**. Pick one (88.6% is the dominant value and the one derived in the Figure 3 caption) and correct §4.2.
2. **Reconcile the M8 linear interaction coefficient (MAJOR-2).** §4.4 text reports the FSTS × DAI term as "β = −1.177, p = .083"; Table 2 column M8 reports **−1.167† (0.686)**. Align the text to the table (or vice versa).
3. **Fix citation–reference reconciliation (MAJOR-3 / MAJOR-4).** Four in-text citations have **no reference entry** (Teece 2007, Coase 1937, Williamson 1985, Leon 2004); seven reference entries appear to have **no in-text citation** (Antonakis et al. 2010, Brynjolfsson et al. 2021, Contractor 2007, MacKinnon & White 1985, Meyer et al. 2017, Rugman & Verbeke 2004, Shaver 2020). Add the missing references and either cite or delete the orphan entries.

---

## 1. Macro logic

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| L1 | MAJOR | The "inferential bounds / underpowered" caveat is handled well and consistently — no defect. Noting it as a *positive*: N = 84 exporter subsample, power ≈ 16%, f² ≈ 0.018 below Cohen's 0.02 threshold are all flagged at §2.4 note, §3.4(ii), §4.5, §7, and the joint-F corroboration is explicitly labelled "corroborating signal, not independent identification." Keep this; do not weaken it in revision. | None required. |
| L2 | MAJOR | Contribution–results map is sound: primary contribution (DAI as conditional scaling resource, H3, β = +3.119, p = .005) is tested in §4.4 and Table 2/4 and matches the abstract. H1 (TCI direct) and H2 (conditional DAI) are tested and reported. **However, hypothesis numbering is confusing:** §2.3.2 explicitly states "this paper formally states H1, H2, and H3 only" and no TCI-moderation hypothesis is posited, yet Figure 1's note labels a relationship "H1-TCI" and the prose refers to a "supplementary TCI-moderation specification (Model M3)." A reader counting hypotheses sees H1/H2/H3 in text but "H1-TCI" in the figure. | Rename the figure's "H1-TCI" to avoid implying a fourth hypothesis (e.g., "TCI direct effect, non-hypothesised supplementary test"), and confirm in §2.3 that the TCI-moderation test is exploratory, not H-numbered. |
| L3 | MINOR | The brief flags "N ≈ 237 exporters." The manuscript nowhere uses 237 — it consistently uses **N = 84** exporters (§2.4 note, §3.4(ii), §4.5, Table 3 R5, §7). The manuscript is internally consistent; flagging only so the author/brief can reconcile which figure is correct against the replication data. | Verify the true exporter count against `do/02_run_models.do`; ensure 84 is correct and matches "18% of 623 ≈ 112 non-zero" vs "N = 84" (see L4). |
| L4 | MAJOR | **Exporter count internal tension.** §3.1 states "18% of firms report non-zero exports" (18% × 623 ≈ 112), but §3.4(i) states "18% any positive intensity" while the exporters-only subsample is repeatedly N = 84. 18% of 623 is ~112, not 84. Either the 18% figure or the N = 84 figure (or the missing-data deletion that bridges them) needs an explicit reconciling sentence. | Add a sentence reconciling the 18% non-zero share with the N = 84 exporter subsample (e.g., listwise deletion on DAI/controls), or correct whichever figure is wrong. |
| L5 | MINOR | Abstract is structured (Purpose/Design/Findings/Originality) and the problem+method+result chain is complete. Conclusions in §6 are supported by and bounded to the results. No defect. | None. |

## 2. Writing details

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| W1 | MAJOR | **Over-long paragraphs.** §1.2 "Research gap" is a single ~330-word paragraph covering three distinct gaps; §5.1 first paragraph runs ~430 words spanning three theoretical implications plus an innovation-ecosystem digression. These exceed comfortable reading length and bury topic sentences. | Split §1.2 into three short paragraphs (one per gap, each with a topic sentence). Split §5.1 at "Second, the evidence qualifies..." and "Third, the DAI result...". |
| W2 | MINOR | **Redundancy across sections.** The construct-boundary / Tier-1+2 argument and the R1 sensitivity result are restated in §1.3, §2.2, §3.2.3, §4.5, and §5.1 with near-identical phrasing ("the conditional-scaling mechanism is empirically legible when DAI captures the Tier-2 transaction-enabling layer"). At ~9,100 words this repetition is noticeable. | Consolidate to one full statement (§3.2.3 or §5.1) and cross-reference elsewhere. |
| W3 | MINOR | Run-on table-adjacent prose: in §4.4 the sentence "Table 2. Hierarchical OLS regression results — Singapore 2023..." is fused into the body text, and similarly Table 4's title runs into the marginal-effects paragraph. Reads as a formatting artifact of the markdown conversion. | Ensure table titles are set off from body paragraphs in the submitted DOCX. |

## 3. Grammar

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| G1 | MINOR | §5.1 sentence beginning "The scale of Singapore's innovation ecosystem, 25,000 attendees and record 6,800 startup applications... confirming that..." is a fragment — the appositive list has no main verb; "confirming" leaves the subject dangling. | Recast: "...confirm that Singapore's advanced digital maturity extends well beyond the Tier 1–2 layer." |
| G2 | MINOR | Inconsistent number formatting introduced by conversion: "25, 000", "6, 800", "22, 000", "150, 000", "5, 000 replications" contain a space after the thousands comma (lines in §5.1, §4.2, Figure 3 caption). | Remove the stray spaces: 25,000 / 6,800 / 22,000 / 5,000. |
| G3 | MINOR | Mixed ampersand vs "and" in narrative citations: body uses Harvard "and" (e.g., "Cohen and Levinthal 1990") but H1 prose has "Cohen & Levinthal 1990" (§2.3.1), and the reference list mixes "and" with "&" (Banalieva & Dhanaraj; Rugman & Verbeke; MacKinnon & White vs Aguinis ... and). Emerald Harvard requires "and" in narrative citations and consistency in the list. | Replace "&" with "and" throughout in-text and standardise the reference list. |

## 4. Number / statistic / citation consistency

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| N1 | MAJOR | **Turning point inconsistent (see Top-3 #1).** §4.2: "near FSTS = 82% on the original scale" vs **88.6%** everywhere else (abstract, §1.3, Fig 1 note, Fig 3 caption, §3.4(i), §7). | Standardise to 88.6%; correct §4.2. |
| N2 | MAJOR | **M8 linear interaction inconsistent (see Top-3 #2).** §4.4: "β = −1.177, p = .083"; Table 2 M8: "−1.167† (0.686)". | Align text and table. |
| N3 | MAJOR | **Citations without references (see Top-3 #3):** Teece 2007 (Fig 1 note, §2.3.4 context), Coase 1937 and Williamson 1985 (§5.1), Leon 2004 (§3.4(ii)). None appear in the reference list. | Add all four reference entries. |
| N4 | MAJOR | **References without citations:** Antonakis et al. 2010, Brynjolfsson et al. 2021, Contractor 2007, MacKinnon & White 1985, Meyer et al. 2017, Rugman & Verbeke 2004, Shaver 2020 appear in the list but no in-text citation was located. | Cite each where relevant (e.g., MacKinnon & White 1985 supports the HC1 SE choice in §3.3; Antonakis 2010 / Shaver 2020 support the causal-claims caveat in §3.3/§7) or delete the orphan entries. |
| N5 | MINOR | **β = +3.119 vs +3.098.** The headline DAI×FSTS² is +3.119 (abstract, §1.3, §4.4, §5.1, Table 2 M8, Table 3 baseline). Table 2 column M4 (DAI-only moderation, no TCI) shows +3.098, and §4.4 prose says "the quadratic interaction term is positive and statistically significant (β = 3.119...)" while M4 = +3.098. This is correct (two different models) but the two near-identical numbers invite confusion. | Add a half-sentence clarifying M4 (+3.098) vs M8 (+3.119) so readers do not read it as a typo. |
| N6 | MINOR | Website-presence share reported as "approximately 67%" (§3.1 DAI note, §4.2) and "≈67%" (Fig 1 / Fig 3); consistent. DAI model N = 617 (six dropped) consistent across Table 2 note, §4.4, Figure 2. No defect — recorded as a passed check. | None. |

## 5. House style (MBR / Emerald)

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| H1 | MINOR | Structured abstract present and ~205 words (Purpose/Design/Findings/Originality) — compliant. Keywords present. README confirms Harvard style. AI-use disclosure present in both cover letter and §"AI and Data Availability" (Grammarly, language only) — compliant with Emerald policy. | None — passed. |
| H2 | MAJOR | **Harvard "and" not applied uniformly** (see G3) and the reference list mixes "and"/"&", which fails the Emerald Harvard house style the README claims is "applied." This is the single most visible house-style defect a desk editor will see. | Global pass: narrative citations use "and"; parenthetical lists per Emerald; reference list uses "and" before final author consistently. |
| H3 | MINOR | Reference list ordering/splitting: the "Additional contextual sources" block (Enterprise Singapore, GovTech, IMDA, StartupBlink, World Bank) is segregated from the main A–Z list. Emerald uses a single alphabetical reference list. | Merge into one alphabetical list. |
| H4 | MINOR | Mixed date-in-citation style for grey sources: "StartupBlink 2025, 2026", "GovTech Singapore 2024" in §1.1 are fine, but ensure each maps to a dated entry (StartupBlink 2026 = Innovators Index; present). Verified present. | None. |

## 6. Banned vocabulary / em-dash scan

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B1 | MINOR | **Em-dash scan: clean.** Zero em-dashes (—) found. All long dashes are en-dashes in compound terms ("internationalization–performance", "Tier 1–2", "Lind–Mehlum"), which is correct typography. README's "Em-dash-free" claim holds. | None — passed. |
| B2 | MINOR | AI-tone vocabulary is largely absent. The text leans on legitimate domain phrasing ("conditional scaling resource", "super-linearly", "discriminatory power", "informative positive null"), which is appropriate, not AI-filler. One mild tic: repeated "Taken together," opening sentences (§4.2 closing, §4.5 twice, Table 3 prose). | Vary or trim a couple of the "Taken together," openers; not a substantive issue. |

---

## Final score

**7 / 10.**

Theoretically disciplined, honestly bounded, and methodologically self-aware — the underpowered/inferential-bounds framing is exemplary and consistently maintained, which is the hardest thing to get right in a paper like this. The score is held back by reconcilable but real consistency defects: one turning-point number, one coefficient, and a citation–reference set that does not close in either direction. None are fatal; all are fixable in a focused revision pass before submission.

## Recommendation

**Minor-to-moderate revision before submission.** No CRITICAL issues. Resolve the six MAJOR items first (turning point 82% vs 88.6%; M8 interaction −1.167 vs −1.177; four missing references; seven orphan references; 18%-vs-N=84 exporter reconciliation; Harvard "and" consistency), then the paragraph-splitting and number-formatting MINORs. After these, the manuscript is in good shape for MBR.
