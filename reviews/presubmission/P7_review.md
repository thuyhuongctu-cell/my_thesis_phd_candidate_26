# P7 Pre-Submission Review — IBR (International Business Review)

**Paper:** Internationalization and Firm Performance across 49 Asian and Pacific Economies (CDCM + ICRV; managerial moderators)
**Target:** International Business Review (Elsevier; unstructured abstract; APA 7)
**Source reviewed:** `p7/submission/ibr_package/01_manuscript_blinded.md` (+ cover letter, title page, README)
**Reviewer role:** Academic pre-submission reviewer

## Summary

The manuscript is methodologically rich and well-organized, with a clear hierarchical model sequence (M0–M11), an explicit Lind–Mehlum testing protocol, and a coherent contribution narrative resolving Asian I–P heterogeneity. House-style fit for IBR is good (unstructured ~250-word abstract, APA references, AI disclosure present). However, there are several substantive consistency defects that a reviewer would catch immediately: (1) a hypothesis-scope mismatch — the abstract advertises a four-hypothesis design while the body develops and tests **six** hypotheses (H1–H6); (2) in-text M10 coefficients (ICRV main, FSTS×ICRV, FSTS²×ICRV) **do not match** Table 3; (3) the pervasive "91, 982"-style thousands spacing affects every large N; (4) several reference/citation bidirectional gaps (one missing reference, six uncited references); and (5) a stray internal sample-size figure ("34 economies") contradicting the 49-economy framing. None of these is fatal, but the coefficient mismatch and the H-count mismatch are MAJOR and must be reconciled before submission.

## Counts

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR | 6 |
| MINOR | 9 |

## Top 3 Fixes (do these first)

1. **Reconcile in-text M10 coefficients with Table 3** (MAJOR). Body Section 4.6 reports ICRV main β = +0.763, FSTS×ICRV = +1.762, FSTS²×ICRV = −2.746; Table 3 reports +0.729, +1.636, −2.501. Pick the correct set and make body = table (and re-check the derived "≈115%" and turning-point decomposition).
2. **Fix the abstract/body hypothesis-count mismatch** (MAJOR). The abstract describes only H1–H4-type content; the body formally states H1–H6. Rewrite the abstract to cover all six hypotheses (institutional regime H5, regime-contingent digital H6) or explicitly note the structure, so reviewers do not see "missing hypotheses."
3. **Global find-replace the thousands spacing** (MINOR but pervasive): "91, 982" to "91,982", "84, 910" to "84,910", "38, 342", "29, 840", "31, 928", "35, 568", "37, 940", "84, 910", "29, 840" in Tables 2/3, etc. Affects abstract, intro, methods, and both tables.

---

## Dimension 1 — Macro Logic

| ID | Severity | Location | Issue | Fix |
|----|----------|----------|-------|-----|
| M-1 | MAJOR | Abstract (lines 8–30) vs Section 2.6–2.7, Section 4.6–4.7 | Abstract frames the design around the I–P curve, TCI, DAI, and managerial moderators (≈H1–H4) and mentions institutional regime only in passing; it never announces H5 (regime turning-point shifter) or H6 (regime-contingent digital, three-way) as hypotheses, yet both are formally stated and tested in the body. | Add one sentence to the abstract covering H5/H6 (ICRV moderation and DAI×ICRV), so the abstract's scope matches the six-hypothesis body. |
| M-2 | MAJOR | Section 5.5 line 640 | "The IV strategy used in P3 Vietnam ... is not available at scale across **34 economies**." The whole paper is built on **49** economies; "34" is an internal contradiction (likely a leftover from an earlier draft). | Change "34 economies" to "49 economies" (or delete the count). |
| m-1 | MINOR | Intro contributions (lines 65–79) vs Results | Contributions are stated as "threefold" (H1 turning point, DAI as primary moderator, ICRV moderation). H4 managerial moderators and H6 three-way are results but absent from the contribution statement. | Either fold managerial/three-way findings into the contributions or note they are secondary, so contributions↔results are symmetric. |
| m-2 | MINOR | Section 4.5 / H4 (lines 469–489) | H4 predicts managerial chars do NOT moderate the curve; Section 4.5 reports FSTS×experience reaches p=.053 in M11 and interprets it as a (marginal) curve moderator. Conclusion "H4 partially supported" is defensible but the abstract claims "experience additionally moderates the curve shape in the full specification" as if confirmed. | Soften abstract wording to "marginally moderates (p=.053)" to match the body's hedged claim. |

Macro logic is otherwise sound: intro chain (gap to pooled multi-economy test to contributions) is clear; H1–H6 are each tested and reported; conclusions track the results.

## Dimension 2 — Writing Details

| ID | Severity | Location | Issue | Fix |
|----|----------|----------|-------|-----|
| m-3 | MINOR | Lines 3–4 | Manuscript header still reads "**Version:** Working manuscript (May 2026)" / "**Status:** Empirical results complete; under revision for submission." This is a draft artifact that should not appear in a blinded submission. | Delete the version/status block. |
| m-4 | MINOR | Section 2.4 (lines 172–174) | Long, multi-clause sentence ("In a fully specified model that also accounts for managerial quality, which correlates with digital adoption, the residual DAI variation may reveal...") stacks three dependent clauses; topic sentence health suffers. | Split into two sentences. |
| m-5 | MINOR | Repetition of "approximately 36%" | The ~36% turning point is restated in abstract, intro (twice), Section 4.2, Section 5.1, and conclusions. Some restatement is fine; the intro and Section 4.2 instances are near-verbatim. | Trim one or two redundant restatements. |

## Dimension 3 — Grammar

| ID | Severity | Location | Issue | Fix |
|----|----------|----------|-------|-----|
| m-6 | MINOR | Line 95 | "firm-level capabilities technological, digital, and managerial, as the mediating mechanism" — an em-dash/colon was removed leaving a double-space gap and a broken appositive. | Insert a colon or comma: "firm-level capabilities, technological, digital, and managerial, as the mediating mechanism" or "capabilities (technological, digital, and managerial)". |
| m-7 | MINOR | Lines 134–135, 238–239, 450–451 | Same removed-punctuation gaps create stranded appositives: "process innovation, and R&D raises absorptive capacity"; "close to the competitive baseline the marginal..."; "The interaction pattern negative FSTS×DAI and positive FSTS²×DAI, means...". The anti-em-dash pass deleted dashes without restoring grammar. | Restore connecting punctuation (comma/colon) at each gap so each clause is grammatical. |
| m-8 | MINOR | Line 57, 278 | "HongKong" should be "Hong Kong" (two words), appears twice. | Correct spelling. |

S-V agreement, articles, tense, which/that usage are otherwise clean.

## Dimension 4 — Number / Stat / Citation Consistency

| ID | Severity | Location | Issue | Fix |
|----|----------|----------|-------|-----|
| M-3 | MAJOR | Section 4.6 (lines 495, 506–507) vs Table 3 (lines 937–939) | M10 coefficients disagree: body ICRV main = **+0.763**, FSTS×ICRV = **+1.762**, FSTS²×ICRV = **−2.746**; Table 3 = **+0.729**, **+1.636**, **−2.501**. The derived "≈115%" (exp(0.763)−1) and the 28%/55% group turning points depend on which is correct. | Reconcile to a single set; recompute derived quantities. |
| M-4 | MAJOR | Missing reference | "Stallkamp & Schotter, 2021" cited (line 252) but absent from the reference list. | Add the full APA reference or remove the citation. |
| M-5 | MAJOR | Uncited references | Six list entries are never cited in text: Aiken & West (1991); Contractor, Kumar, & Kundu (2007); Cuervo-Cazurra et al. (2018); Dawson (2014); Hayes (2018); Wu et al. (2022). APA/Elsevier require bidirectional matching. | Cite each in text or delete from references. |
| m-9 | MINOR | Thousands spacing (pervasive) | All large WBES Ns are written with a space after the comma: "91, 982", "84, 910", "38, 342", "29, 840", "31, 928", "35, 568", "37, 940" (abstract, intro, methods Section 3.4, Tables 2 & 3). | Global replace to no-space form, e.g., "91,982". |
| m-10 | MINOR | Abstract (line 18) vs Section 4.2 (line 393) | Abstract says turning point "at approximately 36%"; M2 TP is 36.4%; both fine, but H1 box (line 67) says "approximately 36% ... (N = 84, 910–29, 840)" — the N range mixes the broadest (84,910) and narrowest (29,840) samples for a turning-point claim that is model-specific. | Either drop the N range from the H1 contribution sentence or label it as the span of analytic samples. |
| m-11 | MINOR | Table 2 / Table 3 caption vs body | Table 3 caption says "Key coefficient estimates (M2, M7, M8, M10)" but the table columns are M2, M7, M8, **M9, M10** (5 columns). | Fix caption to list M2, M7, M8, M9, M10. |
| m-12 | MINOR | World Bank references | Several World Bank entries (2025, 2025a, 2025b, 2025c, 2026a, 2024) appear in the list but are not all cited in text; text cite "World Bank Prosperity Data360, 2025" (line 618) does not map cleanly to a dated list entry. | Audit each World Bank entry for an in-text citation; align year-letter suffixes. |
| m-13 | MINOR | DAI premium wording | Section 4.4 line 449 says DAI ≈ "17% performance premium (exp(0.155)−1)"; line 463 summary says "approximately 16%". | Use one figure consistently (exp(0.155)−1 = 16.8%). |

β/p values for the core curve (M2: +1.316/−1.810; DAI interactions in M8/M9) are internally consistent between abstract, body, and Table 3.

## Dimension 5 — House-Style (IBR / Elsevier)

| ID | Severity | Location | Issue | Fix |
|----|----------|----------|-------|-----|
| m-14 | MINOR | README vs package | README keywords list ("institutional regimes; digital capabilities; ...; contingency") differs from the manuscript keyword line (line 32–34: "internationalization–performance; inverted-U; institutional regime; digital capability; Asia-Pacific; World Bank Enterprise Surveys"). | Align keyword sets across manuscript and submission metadata. |

Positive: unstructured ~250-word abstract (Elsevier-correct), APA 7 references, AI/Generative-AI disclosure present (lines 690–692) and in cover letter, declarations (funding/COI) on title page, CRediT statement present.

## Dimension 6 — Banned Vocab / Em-Dash Scan

- **Em-dashes:** No literal em-dashes (—) remain in body prose; the anti-AI pass was applied. However, the removal left grammatical gaps (see m-6, m-7) where dashes/colons should be restored — those are the visible residue of the pass.
- **AI-tone vocabulary:** Largely clean. "Strikingly" (line 449) and "Crucially" (lines 137, 401) are mild intensifiers a reviewer may flag; consider trimming for an even tone (MINOR, taste — not scored).
- **"superior capabilities/performance":** Used at lines 141 ("exceed even their superior capabilities") and 626 ("superior risk management") — legitimate comparative usage; not flagged per instructions.

---

## Scores (1–10)

| Dimension | Score |
|-----------|-------|
| Macro logic | 7 |
| Writing details | 7 |
| Grammar | 6 |
| Number/stat/citation consistency | 5 |
| House-style (IBR/Elsevier) | 8 |
| Banned vocab / em-dash | 8 |
| **Overall** | **6.5 / 10** |

## Recommendation

**Minor-to-moderate revision before submission.** The science and structure are submission-ready, but the package has correctable consistency defects that referees notice on the first pass: the M10 body↔Table coefficient mismatch (M-3), the abstract/body hypothesis-count mismatch (M-1), the "34 economies" contradiction (M-2), the missing/uncited references (M-4, M-5), and the pervasive thousands-spacing (m-9). Resolve the six MAJOR items and the numeric MINORs, then submit to IBR.
