# Pre-Submission Review — P3 (Vietnam I–P, target: *Journal of Economics and Development*, Emerald/Harvard)

**Source reviewed:** `p3/submission/jed_package/01_manuscript_blinded.md` (full-length version), with `04_tables.md`, `03_cover_letter.md`, `README.md`, `JED_COMPLIANCE.md`.

> Scope note: This review audits the **full-length** `01_manuscript_blinded.md` as instructed. Per `README.md`/`JED_COMPLIANCE.md`, the file actually submitted to JED is the condensed `01_manuscript_blinded_8500.md`. Several findings below (e.g. the missing World Bank 2025 references, the Wolfolds uncited reference) should be checked against the `_8500` file before upload, since that is the version going to the editor.

## Summary

| Severity | Count |
|---|---|
| CRITICAL | 3 |
| MAJOR | 6 |
| MINOR | 6 |

**Top 3 fixes (do these first):**
1. **Add the missing World Bank 2025 references.** The text cites `World Bank, 2025c` and `World Bank (2025b)` but the reference list has no 2025 World Bank entries — a Harvard-completeness failure that a desk editor will catch.
2. **Reconcile the 2023 turning point (41.6% vs 42.0%) and fix the inverted/non-standard significance footnote in Table III** ("*** p<.01, ** p<.05, * p<.10").
3. **Remove or cite Wolfolds and Siegel (2019)** — currently an orphan reference; given the paper leans on a Heckman two-step, citing it would also strengthen Section 3.4.

---

## Dimension 1 — Macro logic & hypothesis–results mapping

| ID | Severity | Quote / location | Issue | Fix |
|---|---|---|---|---|
| 1.1 | MINOR | "This study makes three contributions… First… Second… Third…" (Section 1.3) then "A fourth contribution reframes the inverted-U…" | Section is headed "three contributions" but immediately adds a fourth, and the step-function contribution is the headline claim. | Rename to "four contributions" (or "three contributions, plus a headline reframing") so the count matches. |
| 1.2 | MINOR | H1a: "Crossing from non-exporting (FSTS = 0) to exporting (FSTS > 0) is positively associated with labour productivity" | H1a (the participation-margin jump) is asserted as the dominant margin but is never given a dedicated point estimate in the body; the exporter-only models test H1b, and Section 4.4 infers H1a residually. | Add one explicit participation-margin estimate (e.g. an exporter-dummy coefficient or the PSM/Section 4.4 contrast) so H1a is *reported*, not only inferred. |
| 1.3 | MINOR | Conclusion (Section 7) restates durability "across 14 years of major institutional change, including WTO accession, the Global Financial Crisis, the COVID-19 supply-chain disruption" | Conclusion drops CPTPP/EVFTA which the Highlights/abstract include in the same list. | Harmonise the event list across abstract, highlights, Section 4.3 and Section 7. |

## Dimension 2 — Writing details

| ID | Severity | Quote / location | Issue | Fix |
|---|---|---|---|---|
| 2.1 | MAJOR | Section 2.3–Section 2.4 contain four bold meta-paragraphs: "**Note on hypothesis numbering.**", "**WBES-scope caveat.**", "**Tier-1-only DAI as a deliberate boundary condition.**", "**Two parallel mechanisms behind any later-wave DAI compression.**" | The DAI caveat is repeated 5+ times (Section 2.3 ×3, Section 2.4, Section 3.2 "Construct-tier scope note", Section 4.1, Section 5.1). This is heavily redundant and reads defensively; it also inflates word count against the 8,500 cap. | Consolidate into one caveat paragraph in Section 2.3 and cross-reference it; delete the duplicates. |
| 2.2 | MINOR | "**Note on hypothesis numbering.** Because DAI_z is not advanced as a primary hypothesis… no H3 is formulated… designated H4 to preserve alignment with the broader dissertation framework (P5 China, P7 Multi-country)." | A standalone JED article should not justify its hypothesis numbering by reference to other unpublished dissertation papers; a reviewer reads this as an artefact of a thesis chapter. | Either renumber H4 to H3, or keep the gap but drop the dissertation-cross-reference rationale from the submitted manuscript. |
| 2.3 | MINOR | Abstract "Findings" omits an explicit Originality framing of the step-function, which is the paper's headline. | The step-function result is the lead contribution but appears only as one clause in Findings/Originality. | Lead the Findings sentence with the participation-margin/step-function result. |

## Dimension 3 — Grammar / language

| ID | Severity | Quote / location | Issue | Fix |
|---|---|---|---|---|
| 3.1 | MINOR | Section 3.2: "a foreign-technology and standards capability measure , international quality certification…" and "absorptive-capacity stock (Lall, 1992…)" | Several appositive commas are mis-set as " , " (space-comma) where an em-dash or parenthetical was intended but stripped in the anti-AI pass — e.g. "measure , international", "channel , and DAI_z". | Replace the orphaned " , " with a colon or "(namely …)" so the appositive reads cleanly. Multiple instances (lines ~359, 524, 1027). |
| 3.2 | MINOR | "the negative DAI×FSTS interaction observed only in 2023 … is read as Tier-1 proxy obsolescence" | Generally clean, but "is read as" / "reads as" used as agentless passive throughout; acceptable but repetitive. | Vary phrasing in 2–3 spots. |

## Dimension 4 — Number / stat / citation consistency

| ID | Severity | Quote / location | Issue | Fix |
|---|---|---|---|---|
| 4.1 | CRITICAL | Text: "World Bank, 2025c" (Section 1.2, GDP 7.09% / FDI US$20.17bn) and "World Bank (2025b) *Taking Stock*" (Section 5.5). Reference list has only World Bank (2010), (2016), (2024), (2026). | In-text citations with **no matching reference** — Harvard completeness failure. | Add `World Bank (2025b)` (*Taking Stock*) and `World Bank (2025c)` entries, or remove the claims. |
| 4.2 | MAJOR | 2023 turning point: Table III (`04_tables.md`) = **42.0**; Table 5 (body line 977) and Highlight (line 44) and `Supplementary` = **41.6%**; Fig 2c caption = "≈ 42%". | Same quantity reported as 41.6 and 42.0 across tables. | Pick one value (41.6% is the CI-anchored Table 5 figure) and propagate to Table III and Fig 2c. |
| 4.3 | MAJOR | Exporter-only pooled quadratic: body repeatedly "FSTS_c² β = -0.200, **p = .660**" (abstract, Section 1.3, Section 1.4 H1, Section 2.1, Section 4.3, Section 4.4, Table III). Table 4 row (line 835): "FSTSc2 -0.200 (0.581) **0.730**". | The p-value for the headline step-function coefficient is inconsistent (.660 vs .730) between prose and the robustness table. | Reconcile to the actual estimate and use it uniformly. |
| 4.4 | MAJOR | Reference list contains **Wolfolds and Siegel (2019)** (line 1339); no in-text citation anywhere. | Orphan reference (Harvard: every reference must be cited). | Cite it in Section 3.4 (it directly critiques Heckman-without-instrument, which the paper uses) or delete it. |
| 4.5 | CRITICAL | Table III footnote: "Significance: *** p<.01, ** p<.05, * p<.10." | Non-standard and **inconsistent** with the rest of the paper: Table 4 and all body text use "*** p<.001, ** p<.01, * p<.05" with "†" for p<.10. Under the Table III key, FSTS_c² "−1.774***" would mean p<.01, but the body reports p=.009 (which is **). Readers cannot map stars to p-values. | Standardise Table III to the paper's convention (*** p<.001, ** p<.01, * p<.05, † p<.10) and re-mark the cells. |
| 4.6 | MAJOR | Cover letter: "Tables: 5; Figures: 6" and "≈ 6,800 words"; manuscript header also says 5 tables / 6 figures. `04_tables.md` contains only **Tables I–III**; JED package ships 3 main tables + supplement. | Table/figure counts in the cover letter and title block do not match the separated-file reality (3 main tables). | Align the cover-letter and header counts with the final separated-tables file. |
| 4.7 | MINOR | "World Bank (2026)" used for WDI/ITU internet-share figures dated "approximately 26% in 2009, 45% in 2015 and over 78% by 2023" (Section 5.3); ITU reference is "International Telecommunication Union (2026)". | Dating a 2009–2023 data series to a "2026" access-year citation is fine, but the fixed-broadband/internet figures (Section 5.3) are attributed to WDI in prose without an inline `(World Bank, 2026)` / `(ITU, 2026)` cite at the sentence. | Add inline citations at the macro-figure sentences. |

## Dimension 5 — House-style (JED/Emerald) compliance

| ID | Severity | Quote / location | Issue | Fix |
|---|---|---|---|---|
| 5.1 | MAJOR | Main text embeds full Table 2, Table 4b, Table 4 (robustness, ~150 rows), Table 5, Paternoster table, and Figures 1–3 inline. JED requires tables in a **separate file** with `[Insert Table … about here]` markers. | The full-length file violates the separate-tables rule and contains **no** `[Insert Table]` markers (only `04_tables.md` does). | This is handled in the `_8500`/`04_tables` package; ensure the submitted manuscript carries the `[Insert Table I about here]` markers and no inline table bodies. |
| 5.2 | MINOR | AI-use disclosure (Section "Use of generative AI"): discloses Grammarly, "No generative artificial-intelligence tool was used to generate… any substantive content." | Compliant and well-worded. No action, noted as PASS. | — |
| 5.3 | MINOR | Abstract structured (Purpose/Design/Findings/Originality) present and ≤250 words per JED_COMPLIANCE. | PASS. | — |

## Dimension 6 — Banned vocab / em-dash scan

| ID | Severity | Finding | Note |
|---|---|---|---|
| 6.1 | — (PASS) | Full grep for em-dash (—) and AI-tone words (innovative, pioneering, unprecedented, transformative, superior, surpass, remarkable, breakthrough, underscore, pave the way, delve, tapestry) returned **no matches** in `01_manuscript_blinded.md`. | The anti-AI / em-dash-free pass (per README) is confirmed clean. One side-effect: the stripped em-dashes left orphaned " , " appositives — see Finding 3.1. |

---

## Final score and recommendation

**Score: 7 / 10.** The paper is conceptually coherent, the macro logic chain (gap to contribution to results to conclusion) holds, hypotheses H1/H1a/H1b/H2/H4 are each tested and reported, and the AI/ethics/abstract house-style boxes are ticked. It is held back from a higher score by (a) Harvard-completeness defects that a desk editor screens for (missing World Bank 2025 references, orphan Wolfolds reference), (b) cross-table numeric inconsistencies on the paper's own headline statistics (2023 turning point 41.6 vs 42.0; exporter-only p = .660 vs .730), and (c) an inverted/non-standard significance key in Table III. None of these are fatal, but several are exactly the kind a referee flags as "sloppy."

**Recommendation: 1–2 days of revision before submission.** Fix the three CRITICAL/citation items (4.1, 4.4, 4.5), reconcile the two numeric mismatches (4.2, 4.3), consolidate the repeated DAI caveats (2.1), and verify the same defects in the `_8500` file actually being uploaded. After that it is submission-ready.
