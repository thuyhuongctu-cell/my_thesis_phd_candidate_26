# P6 — PRISMA 2020 Checklist
# Meta-Analysis: Internationalization–Performance (I→P) 1977–2026

> **Version**: v1.0 (2026-05-16)  
> **Standard**: PRISMA 2020 (Page et al., 2021; *BMJ* 372:n71)  
> **Target journal**: *International Business Review*  
> **Manuscript file**: `p6/p6_meta_manuscript_en.md`  
>
> **Status legend**:  
> ✅ Complete — text is in the manuscript and meets PRISMA requirement  
> ⚠️ Partial — content exists but needs updating (e.g., TBD counts after formal search)  
> ❌ Missing — item not yet addressed in the manuscript  

---

## Section 1: TITLE

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 1 | Identify the report as a systematic review (or meta-analysis). | Title: "…the Internationalization–Performance Relationship: A Three-Level Meta-Analysis" — phrase "Meta-Analysis" identifies the report type | ✅ |

---

## Section 2: ABSTRACT

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 2 | Provide a structured abstract covering: background, objectives, data sources, study eligibility criteria, participants/interventions, appraisal and synthesis methods, results, limitations, conclusions and systematic review registration number. | §Abstract: Purpose / Design-methodology / Findings / Originality sub-sections; *k* = 238, *K* = 288 stated; OSF registration https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN; May 18, 2026) | ✅ Complete |

---

## Section 3: INTRODUCTION

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 3 | Rationale: Describe the rationale for the review in the context of existing knowledge. | §1 Introduction: contrasts five prior I→P meta-analyses; identifies three unexplored moderators (ICRV, cDAI, DPL phase); establishes gap | ✅ |
| 4 | Objectives: Provide an explicit statement of the question(s) the review addresses (PICO or equivalent). | §1, §2.1: Research question stated; PICO criteria explicit in §3.2 | ✅ |

---

## Section 4: METHODS

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 5 | **Eligibility criteria**: Specify study characteristics (e.g., PICO, study design) and report characteristics (e.g., years considered, language, publication status) used as criteria for eligibility. | §3.2 PICO table with Inclusion/Exclusion columns; covers population, DOI operationalization, performance measure, effect-size extractability, language, region, publication type | ✅ |
| 6 | **Information sources**: Specify all databases, registers, websites, grey literature sources, and other methods used to identify studies, with the date each was last searched. | §3.1: WoS Core Collection (SSCI, SCI-E, ESCI) searched **2026-05-18** via Starter API (n=2,180); Scopus search pending (CTU campus access required); 5 supplementary DBs (ABI/INFORM, EBSCO, ScienceDirect, SpringerLink, Emerald); backward + forward citation; hand-search (n=19). | ⚠️ Scopus search date pending |
| 7 | **Search strategy**: Present the full search strategy for at least one database, including any filters applied. | §3.1: Full WoS TS= query and equivalent Scopus TITLE-ABS-KEY query shown verbatim with all Boolean operators; validation set (30-paper recall = 97%) | ✅ |
| 8 | **Selection process**: State the process for selecting studies (e.g., screening, eligibility), including the number of reviewers involved in each stage and how discrepancies were resolved. | §3.2: "Two independent screeners… two stages (title/abstract then full-text)… disagreements resolved by third reviewer (majority decision)" | ✅ |
| 9 | **Data collection process**: Specify the methods used to collect data from reports, including the number of coders and how disagreements were handled. | §3.3.1: "primary coder (PI: Đỗ Thùy Hương)… standardized coding form (Appendix B)"; §3.3.2: ICR 3-stage protocol with calibration, independent coding (20% subsample), adjudication | ✅ |
| 10 | **Data items**: List and define all variables for which data were sought; describe any assumptions. | §3.3.1: 7 variables listed (N, r, year range, country, DOI type, performance type, moderators); §3.4: 7 moderators defined with exact coding rules; Appendix B table | ✅ |
| 11 | **Study risk of bias assessment**: Specify the methods used to assess the risk of bias in included studies (e.g., a tool, criteria). | §3.3.3 Study-Level Risk of Bias: no formal RoB instrument applied (consistent with I→P meta-analysis practice); synthesis-level bias addressed via Egger's test, Begg & Mazumdar rank correlation, and trim-and-fill (§3.6). | ✅ Complete |
| 12 | **Effect measures**: Specify the effect measure(s) used in the synthesis (e.g., risk ratio, mean difference). | §3.5: "All Pearson's *r* values are transformed to Fisher's *z* prior to analysis… back-transformed to *r* for interpretability"; conversion hierarchy β→r, t→r, F→r specified | ✅ |
| 13 | **Synthesis methods**: Describe planned methods for synthesising results, including heterogeneity quantification (e.g., *I*²) and any other statistical models. | §3.5: Three-level MARA specified; REML via `rma.mv`; heterogeneity decomposition formulas for *I*²_(2) and *I*²_(3); moderator omnibus *Q*_M test; Holm–Bonferroni pairwise correction | ✅ |
| 14 | **Reporting bias assessment**: Describe planned methods to investigate reporting biases (e.g., publication bias). | §3.6: Four complementary tests — Egger's weighted regression, Begg–Mazumdar rank correlation, trim-and-fill, Orwin's FSN; plus PET-PEESE meta-regression | ✅ |
| 15 | **Certainty assessment**: Describe any methods used to assess the certainty (or confidence) of the body of evidence. | Not addressed. GRADE is rarely applied in IB meta-analysis; reviewers may not require it. Consider: "The certainty of the synthesized evidence was assessed using the adapted GRADE approach for meta-analyses (Murad et al., 2016), classifying evidence as high/moderate/low/very low based on heterogeneity, publication bias, precision, and directness." | ❌ Optional but add if IBR reviewers request |

---

## Section 5: RESULTS

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 16a | **Study selection**: Describe the results of the search and selection process (PRISMA flow diagram recommended). | **PRISMA flow (WoS arm, 2026-05-18):** Records identified: 2,180 → after internal dedup: 2,179 → L1 keyword pre-screen: 782 → L2 title screen: Y=345, N=35, UNSURE=402 → UNSURE re-screen R1 (script 14): Y=135 (129 new, 6 dups), N=3, still UNSURE=263 → UNSURE re-screen R2 (script 18, two-tier): Y=30 (all new), N=29, still UNSURE=204 → UNSURE re-screen R3 (script 20, extended patterns): Y=25 (all new), N=43, still UNSURE=136 → UNSURE re-screen R4 (script 22, capital structure/location/antecedent exclusions; performance consequences/crisis resilience inclusions): Y=15 (all new), N=34, still UNSURE=87 → R5 (first-author title-only 19/05/2026): Y=4, N=11, still=72 → R6 (first-author title-only 19/05/2026): Y=8 (all new), N=46, still=18 → R7 (manual signals: book-chapter DOI, single-case, antecedent-DV, non-business journal, macro-unit; 19/05/2026): Y=0, N=8, still=10 → R8 (WebSearch abstract pass 19/05/2026): Y=3 (S0129 India Born Globals I→P; S0240 SME I→P OL mediator; S0683 Latin America MNE→perf), N=7, still=0 → **Total L2 Y: 565** → dedup: 321 confirmed R1 + 214 probable new (R1-R8). **Active extraction pool: 535** (`extraction_worklist_v9_20260519.csv`). Scopus arm pending. | ⚠️ Scopus arm pending |
| 16b | **Exclusion reasons**: Present reasons for exclusions at the full-text stage in sufficient detail. | L2 exclusion reasons: E1:conceptual/editorial (4), E2:qualitative/case-study (8), E3:macro-level (6), E5:export-as-DV (17). Appendix A updated with actual counts from `l2_deep_screened_20260518.csv`. | ⚠️ Full-text exclusion reasons finalized after abstract screening of 402 UNSURE |
| 17 | **Study characteristics**: Cite each included study; present their characteristics (PICO data, etc.). | §4.1: Sample description — existing *k* = 238 studies, *K* = 288 effect sizes; **535 candidates** in active extraction pool. **Active instrument**: `extraction_worklist_v9_20260519.csv` (535 rows; 166 High priority, 304 Medium, 65 Low; 378 DOI-available). **Rule-based prescreening v2** (`l2_prescreened_v2_20260519.csv`, 19/05/2026): Pre-Y = 396 (74.0%), Pre-N = 34 (6.4%), UNSURE = 105 (19.6%); new rules: wrong-direction capability→export-perf exclusion (−53 UNSURE→N), export-productivity inclusion (+36 UNSURE→Y). | ⚠️ Table S1 pending effect-size extraction for 535 candidates |
| 18 | **Risk of bias in studies**: Present risk-of-bias assessments for each study. | Consistent with §3.3.3 — no per-study RoB scores. Synthesis-level bias diagnostics reported in §4.4 (Egger's, trim-and-fill, PET-PEESE). Acknowledged as study-design constraint in Limitations (§6). | ✅ Addressed (synthesis-level; per-study not applicable) |
| 19 | **Results of individual studies**: Present results from each study — at minimum, effect estimate for each synthesis outcome. | Forest plots in Figures 1–2 show individual study r-values; supplementary `forest_data.csv` | ✅ |
| 20 | **Results of syntheses**: Present the results of all syntheses (pooled r, CI, heterogeneity, moderator results). | §4.2 Baseline, §4.3 Moderator analyses (Tables 2–4), §4.4 Publication bias | ✅ |
| 21 | **Reporting biases**: Present the results of assessments of reporting biases (publication bias). | §4.5: Egger's *p*, trim-fill adjusted *r*, Orwin's FSN, PET-PEESE results | ✅ |
| 22 | **Certainty of evidence**: Present assessments of certainty/confidence in each synthesis. | Not addressed (see Item 15). | ❌ Add if required by IBR |

---

## Section 6: DISCUSSION

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 23 | **Discussion**: Provide a general interpretation of the results in the context of other evidence, and implications for practice, policy, and future research. | §5 Discussion: ICRV gradient interpreted; cDAI mechanism discussed; DPL phase temporal pattern; comparison with Marano et al. (2016), Wu et al. (2022) | ✅ |
| 24 | **Limitations**: Discuss limitations of the evidence included in the review and of the review process itself. | §5.4 Limitations: (a) cross-sectional study-level data / no firm-level causal inference; (b) AP-weighted corpus / Europe/NA underrepresented; (c) DAI Tier-1+2 only, not Tier-3/4; (d) English-only search, anglocentricity bias noted; (e) 80% single-coder — five-item limitations block added May 2026 | ✅ Complete |
| 25 | **Conclusions**: Provide a brief summary of the findings in the context of the implications for practice and future research. | §6 Conclusion | ✅ |

---

## Section 7: OTHER INFORMATION

| Item | PRISMA 2020 Requirement | Location in Manuscript | Status |
|------|------------------------|------------------------|--------|
| 26 | **Registration and protocol**: Provide registration information for the review, including register name and registration number. | §3.1: "Pre-registered on OSF prior to effect-size extraction: https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN; registered May 18, 2026)" | ✅ Complete |
| 27 | **Support**: Describe sources of financial support for the review, and the role of the funders or sponsors. | §Funding: "This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors." | ✅ Complete |
| 28* | **Competing interests**: Declare any competing interests among the reviewers. | §Competing Interests: "The authors declare no conflict of interest." | ✅ Complete |
| 29* | **Data availability**: Report where the data, analytic code, and other materials associated with the review can be accessed. | §Data Availability: "The coded study database (forest_data.csv), R analysis scripts (metafor), and the OSF pre-registration protocol are available from the corresponding author upon reasonable request. The PRISMA 2020 checklist is provided as supplementary material." | ✅ Complete |

> *Items 28–29 are sometimes listed as part of a 29-item extension in PRISMA 2020 guidance; include regardless as IBR requires them.*

---

## Summary Status

| Status | Count | Items |
|--------|-------|-------|
| ✅ Complete | 24 | 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29 |
| ⚠️ Partial (pending extraction / Scopus) | 3 | 6, 16a, 16b |
| ⚠️ Partial (pending extraction completion) | 1 | 17 |
| ❌ Missing / not addressed | 2 | 15, 22 |

> **Updated 2026-05-19 (v2.0)**: Item 17 updated for rule-based prescreening v2 (`l2_prescreened_v2_20260519.csv`): Pre-Y=396 (74%), Pre-N=34 (6.4%), UNSURE=105 (19.6%). New rules: wrong-direction capability→export-perf exclusion + export-productivity inclusion. v1.9: Items 16a/17 for R8 WebSearch abstract pass; R8 3Y+7N; Total L2 Y=565; active pool=535; Batch 1=144. Scopus arm pending.

### Action list before IBR submission

1. ~~**Abstract screening (10 UNSURE)**~~ **✅ COMPLETED (R8, 19/05/2026)**: All 10 UNSURE resolved via WebSearch abstract pass — 3Y (S0129, S0240, S0683) + 7N. PRISMA counts finalized for WoS arm. Scopus arm pending.
2. **Scopus search**: Run on CTU campus network; parse with `02_parse_scopus_export.py`; merge with `03_deduplicate_merge.py` to get final n_unique (Item 6)
3. **OA PDF download**: Run `12_fetch_full_pdfs.py --input results/extraction_worklist_v9_20260519.csv --email <your_email> --delay 1 --skip-existing` → downloads OA PDFs for DOI-available studies in the 535-record pool; outputs `pdfs/`, `pdf_fetch_log.csv`
4. **Effect-size extraction**: Fill `extraction_worklist_v9_20260519.csv` for all 535 candidates (`r` and `n` = NR → fill from PDF). Prioritize: Batch 1 = **144** High+DOI records. Use `11_validate_and_convert_extraction.py` to validate → run `10_merge_new_studies.py` → update k in manuscript
5. **Item 17**: Run `p6_mara_updated.R` after merge → auto-generates Table S1 (`forest_data.csv`) with all k study characteristics
6. **Items 15, 22** (GRADE certainty): Add brief paragraph in §3 and §4 if IBR reviewers request — template: "Certainty assessed using adapted GRADE framework (Murad et al., 2016): high heterogeneity (I²=62%) and potential publication bias reduce certainty to *moderate*."

---

## References

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Liberati, A., Altman, D. G., Tetzlaff, J., Mulrow, C., Gøtzsche, P. C., Ioannidis, J. P. A., ... & Moher, D. (2009). The PRISMA statement for reporting systematic reviews and meta-analyses. *PLOS Medicine, 6*(7), e1000097. https://doi.org/10.1371/journal.pmed.1000097
