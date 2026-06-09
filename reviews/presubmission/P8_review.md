# Pre-Submission Review — P8

**Paper:** Forced Internationalization Penalty: Firm Performance in Pacific Small Island Developing States
**Target:** Journal of International Development (Wiley, Q2)
**Source:** `p8/submission/jid_package/01_manuscript_blinded.md` (+ cover letter, title page, README)
**Reviewer role:** Academic pre-submission reviewer
**Date:** 2026-06-09

---

## Summary

The manuscript is a well-argued, theoretically coherent contribution. The FIP construct is cleanly defined, differentiated from four adjacent concepts, and tied to three named structural prerequisites that map onto two pre-registered hypotheses. The 7-SIDS / N=959 headline framing is internally consistent across abstract, body, conclusion, and cover letter. No banned em-dashes (—) appear; the 45 dash hits are all legitimate en-dashes (ranges, references, compound terms). The earlier "nine economies / N=1,469 / Comoros / −0.404" artifacts have been fully purged — none remain.

The decisive problem is **statistical-sample consistency**: the headline coefficient β=−1.339 is described throughout as the "country-and-year fixed-effects" result on the N=959 sample, but **Table 2 reports N=209 for M0–M2 and N=205 for M3**. Only M_bivariate is actually estimated on N=959. The prose (abstract, §4.2, §6) implies the flagship FE estimate uses all 959 firms; the table contradicts this. This is a true number/stat inconsistency (CRITICAL per the consistency mandate, though the *direction* of the 7-SIDS/N=959 headline itself is intact). It must be reconciled before submission — either correct the N in the table or correct the prose, and explain the 959→209 attrition.

Secondary issues: Table 1 is an empty shell (all country rows are placeholder commas), several significance stars conflict with their narrated p-values, and a few topic sentences run long. None of these block the contribution; the FE/N reconciliation does.

---

## Counts

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| MAJOR | 4 |
| MINOR | 6 |
| **Total** | **12** |

---

## Top 3 Fixes

1. **Reconcile N=959 vs N=209 for the fixed-effects models (CRITICAL).** Abstract, §4.2, §4.5 (line 214), and §6 attribute β=−1.339 to the FE specification framed against "959 firms," but Table 2 shows N=209 (M1) and N=205 (M3). State plainly that the FE models run on N≈209 (attrition from country/year FE + control missingness) and that only the bivariate uses N=959; revise every "959 ... fixed-effects" phrasing.
2. **Populate Table 1 (CRITICAL/MAJOR).** All seven country rows are empty placeholders (`|, |, |...`). A reviewer cannot verify the 7-SIDS composition, exporter counts, or wave coverage. Fill in the per-country N / Exporters / % / Mean FSTS / Waves, or remove the table and cite the replication archive only.
3. **Fix significance-star / p-value contradictions (MAJOR).** §4.5 line 211 reads "β(TCI_z) = +0.299 ... p = .003 (n.s.)" and "β(DAI_z) = +0.094 ... p = .285 (n.s.)" — the "(n.s.)" tag on the p=.003 TCI estimate is wrong (it is significant, and Table 2 stars it `**`). Remove the erroneous "(n.s.)" from TCI.

---

## Dimension 1 — Macro Logic

| ID | Severity | Location | Finding | Fix |
|----|----------|----------|---------|-----|
| M-1 | CRITICAL | Abstract; §4.2 ln.149–155; §4.5 ln.214; §6 ln.282 | Headline FE coefficient β=−1.339 is framed as the result "from 959 firms" / "country-and-year fixed-effects," but Table 2 reports **N=209** for M1 (and N=205 for M3). Only M_bivariate uses N=959. The sample backing the flagship estimate is misrepresented. | State the FE N (≈209) explicitly wherever β=−1.339 appears; explain 959→209 attrition (FE cells + control missingness). |
| M-2 | MINOR | §1 ln.20 vs §6 ln.284 | Intro promises "three contributions"; Conclusion delivers "two ways." The third intro contribution (capability non-override) is folded into the second conclusion point, but the count mismatch reads as an omission. | Align the framing — either restate three contributions in §6 or note the consolidation. |
| M-3 | MINOR | §1 ln.20 | "the most comprehensive firm-level I-P analysis in Pacific SIDS to date" is an unverifiable superlative. | Soften to "one of the first firm-level I-P analyses across multiple Pacific SIDS." |

Intro chain (contested regularity → inverted-U resolution → its hidden prerequisites → SIDS violates all three → FIP), the 3-prerequisite argument, abstract problem+method+result, and both hypotheses (H1 tested in §4.2–4.3, H2 in §4.5) are all sound and reported. Conclusions follow from results.

---

## Dimension 2 — Writing Details

| ID | Severity | Location | Finding | Fix |
|----|----------|----------|---------|-----|
| W-1 | MAJOR | §4.1 ln.145 | "roughly 83% of explained productivity variance is between-country" derived from R² 0.109→0.657 is asserted without showing the arithmetic, and the 83% figure is not obviously recoverable from those two numbers. | Show the decomposition or restate qualitatively ("the large majority of explained variance is between-country"). |
| W-2 | MINOR | §1 ln.18 | One sentence runs ~90 words ("Independent multi-indicator analysis of six development dimensions ... disproportionately represented in this cohort"). The embedded list ("poverty, life expectancy, schooling, gender equality, climate, and electricity") lacks setoff punctuation. | Split into two sentences; set off the dimension list with a colon or dashes. |
| W-3 | MINOR | §2.1 ln.39; §5.1 ln.228; §5.4 ln.264 | Recurring comma-spliced appositive lists ("absent financial intermediaries, unreliable contract enforcement, limited trade facilitation infrastructure, do not merely...") strain readability. | Use "such as ... —" setoff or semicolons within the list. |

Topic sentences are generally strong (each subsection opens with its claim). Abstract is single-paragraph, ~210 words — acceptable for JID, near the README's ~200 target. No substantive redundancy.

---

## Dimension 3 — Grammar / Mechanics

| ID | Severity | Location | Finding | Fix |
|----|----------|----------|---------|-----|
| G-1 | MINOR | §1 ln.18; §2.3 ln.59; throughout | Number formatting inserts a space after the thousands separator: "104, 000", "121, 000", "94, 000", "121, 249". | Remove the space: "104,000", "121,000", "94,000", "121,249". |
| G-2 | MINOR | §5.1 ln.232; §6 ln.282, ln.284 | Stray space before closing quotation marks: `"weaker moderation" to "violated prerequisites, "` and `"institutional determination of I-P sign, "`. | Move the comma inside / close the quote without the leading space. |
| G-3 | MINOR | §2.1 ln.33 | "(Johanson & Vahlne, 1977; 2009)" uses a semicolon between two years of the same authors; APA uses a comma: "(Johanson & Vahlne, 1977, 2009)". | Replace semicolon with comma. |

Articles, S-V agreement, tense, and which/that usage are clean. No Chinglish detected.

---

## Number / Stat / Citation Consistency (CRITICAL CHECK)

| Item | Abstract | Body | Table | Cover letter | Verdict |
|------|----------|------|-------|--------------|---------|
| Scope | 7 Pacific SIDS | 7 (Fiji, Kiribati, PNG, Samoa, Solomon Is., Tonga, Vanuatu) | Table 1 lists the 7 | "Pacific SIDS" | Consistent |
| N | 959 | 959 | Table 1 Total = 959 | (not stated) | Headline consistent |
| β M1 (FE) | −1.339, p<.001 | −1.339, p<.001 | −1.339*** (0.386) | — | Value consistent |
| β M_yearFE | −3.351, p<.001 | −3.351, p<.001 | −3.351*** (0.808) | — | Consistent |
| β bivariate | — | −0.864, p=.050 | −0.864. (0.441) | — | Consistent |
| β exporters | — | −1.176, p=.130 | −1.176 (Table 3) | — | Consistent |
| TCI β | +0.299 | +0.299, p=.003 | +0.299** (0.099) | — | Consistent (but mislabelled "n.s." in prose) |
| DAI β | +0.094 | +0.094, p=.285 | +0.094 (0.088) | — | Consistent |
| **N for FE models** | implies 959 | "959 for M1" (ln.214) | **N=209 (M1), 205 (M3)** | — | **CONFLICT (CRITICAL)** |

- Residual scan for "nine" / "1,469" / "−0.404" / "Comoros": **none found.** Clean.
- "Caribbean" (ln.278) appears only as a future extension context, correctly excluded from the sample. Legitimate.
- C-1 (MAJOR): §4.5 ln.211 tags TCI_z "p = .003 (n.s.)" — internally contradictory and contradicts Table 2's `**`. Remove "(n.s.)".
- C-2 (MAJOR): §4.5 ln.214 "N = 959 for M1" is the same conflict as M-1 (Table 2 N=209). Listed once as CRITICAL above; the textual claim is the locus.
- Citation↔reference bidirectional check: all in-text cites resolve to the reference list (Barney, Bausch & Krist, Briguglio, Contractor, Doh, Goedhuys & Sleuwaegen, Haans, Hennart, Hitt, Johanson & Vahlne, Khanna & Palepu, Kirca, Lall, Lind & Mehlum, Lu & Beamish, Mahler et al., Marano, North, Pirlea, Read, Sarasvathy, Scott, Teece, UNGA 2024, Verbeke & Brugman, Winters & Martins, Zaheer). Three reference entries are **uncited in text**: Briguglio, Cordina, Farrugia & Vella (2009); Diamantopoulos & Winklhofer (2001); Jarvis, MacKenzie & Podsakoff (2003); Vahlne & Johanson (2020). Note "Mahler, Serajuddin, Wadhwa & Yonzan (2026)" is cited in §1 ln.18 but the reference list only has "Mahler, Wang & Weber (2026)" and "Pirlea et al. (2026)" — the Mahler/Serajuddin/Wadhwa/Yonzan entry is **missing from References** (MAJOR, broken citation).

---

## House Style — JID / Wiley

| ID | Severity | Finding |
|----|----------|---------|
| H-1 | MINOR | README checklist still has unchecked boxes (reference style, word count 8,000–10,000, abstract ~200). Confirm word count before upload. |
| H-2 | — | APA 7 reference style is followed; AI disclosure present and well-formed; declarations (funding/COI/CRediT) on title page are complete. Good. |

---

## Banned Vocab / Em-Dash Scan

- **Em-dash (—): 0 occurrences.** Clean.
- En-dash (–): 45, all legitimate (numeric ranges, page ranges, "internationalization–performance"). No action.
- "superior international capabilities" / "superior technological capabilities" (§2.3 ln.61; §5.3): legitimate comparative usage per the brief — **not flagged.**
- No genuine AI-tone filler ("delve," "tapestry," "it is important to note," "in the realm of," "underscores") detected. The prose reads as human-authored academic register.

---

## Scores (1–10)

| Dimension | Score |
|-----------|-------|
| Macro logic | 7 |
| Writing details | 7 |
| Grammar/mechanics | 8 |
| Number/stat/citation consistency | 4 |
| House style | 8 |
| **Overall** | **6.5** |

The contribution and prose are solid (would score 8); the overall is pulled down by the FE-sample/N misrepresentation and the empty Table 1, both of which a referee will catch immediately.

---

## Recommendation

**Minor-to-Major revision before submission.** The theory, writing, grammar, and AI-tone are submission-ready. Block the upload until two things are fixed: (1) reconcile the N=959-vs-N=209 fixed-effects sample claim across abstract/body/conclusion with Table 2, and (2) populate Table 1. Also clear the missing reference (Mahler/Serajuddin/Wadhwa/Yonzan 2026) and the TCI "(n.s.)" mislabel. With those four corrections the paper is ready for JID.
