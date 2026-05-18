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
| 2 | Provide a structured abstract covering: background, objectives, data sources, study eligibility criteria, participants/interventions, appraisal and synthesis methods, results, limitations, conclusions and systematic review registration number. | §Abstract: Purpose / Design-methodology / Findings / Originality sub-sections; *k* = 237, *K* = 287 stated; OSF pre-registration mentioned | ⚠️ Registration ID not yet inserted |

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
| 6 | **Information sources**: Specify all databases, registers, websites, grey literature sources, and other methods used to identify studies, with the date each was last searched. | §3.1: WoS Core Collection (SSCI, SCI-E, ESCI) + Scopus; 5 supplementary DBs (ABI/INFORM, EBSCO, ScienceDirect, SpringerLink, Emerald); backward + forward citation; hand-search (n=19). Dates TBD. | ⚠️ Search dates not yet filled in |
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
| 16a | **Study selection**: Describe the results of the search and selection process (PRISMA flow diagram recommended). | §3.2 last paragraph: PRISMA 2020 flow inline text with TBD counts; Appendix A: full ASCII flow diagram | ⚠️ TBD counts after formal search |
| 16b | **Exclusion reasons**: Present reasons for exclusions at the full-text stage in sufficient detail. | Appendix A: six exclusion reasons at full-text stage; §3.2 inline | ⚠️ Counts TBD |
| 17 | **Study characteristics**: Cite each included study; present their characteristics (PICO data, etc.). | §4.1: Sample description — *k* = 237 studies, *K* = 287 effect sizes; Table 3.1 (ICR statistics); forest_data.csv contains all study-level data | ⚠️ Formal Table of Study Characteristics (all k studies listed) not yet in manuscript |
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
| 26 | **Registration and protocol**: Provide registration information for the review, including register name and registration number. | §3.1: "Pre-registration on the Open Science Framework (OSF)… registration identifier will be inserted at acceptance" | ⚠️ Insert actual OSF registration ID before submission |
| 27 | **Support**: Describe sources of financial support for the review, and the role of the funders or sponsors. | §Funding: "This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors." | ✅ Complete |
| 28* | **Competing interests**: Declare any competing interests among the reviewers. | §Competing Interests: "The authors declare no conflict of interest." | ✅ Complete |
| 29* | **Data availability**: Report where the data, analytic code, and other materials associated with the review can be accessed. | §Data Availability: "The coded study database (forest_data.csv), R analysis scripts (metafor), and the OSF pre-registration protocol are available from the corresponding author upon reasonable request. The PRISMA 2020 checklist is provided as supplementary material." | ✅ Complete |

> *Items 28–29 are sometimes listed as part of a 29-item extension in PRISMA 2020 guidance; include regardless as IBR requires them.*

---

## Summary Status

| Status | Count | Items |
|--------|-------|-------|
| ✅ Complete | 22 | 1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 18, 19, 20, 21, 23, 24, 25, 27, 28, 29 |
| ⚠️ Partial (fill after formal search) | 6 | 2, 6, 16a, 16b, 17, 26 |
| ❌ Missing / not addressed | 2 | 15, 22 |

### Action list before IBR submission

1. **After formal WoS+Scopus search** (highest priority): Fill all [TBD] counts in §3.2, Appendix A, Abstract, §4.1 (Items 2, 6, 16a, 16b, 17)
2. **Item 11**: Add one sentence to §3 acknowledging no study-level risk-of-bias tool was applied and why (standard in I→P meta-analysis)
3. **Item 17**: Add Table S1 (supplementary) listing all *k* studies with study characteristics — title, author, year, country, N, DOI measure, performance measure, r, ICRV code, cDAI category, DPL phase
4. **Item 24**: Confirm §5/§6 contains explicit limitations paragraph (check content)
5. **Item 26**: Insert actual OSF registration identifier (e.g., `osf.io/XXXXX`)
6. **Items 27–29**: Add before submission:
   - Funding acknowledgement (e.g., CTU research fund, or "This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.")
   - Competing interests ("The authors declare no conflict of interest.")
   - Data availability ("The study database, R scripts, and PRISMA checklist are available at [OSF link].")

---

## References

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Liberati, A., Altman, D. G., Tetzlaff, J., Mulrow, C., Gøtzsche, P. C., Ioannidis, J. P. A., ... & Moher, D. (2009). The PRISMA statement for reporting systematic reviews and meta-analyses. *PLOS Medicine, 6*(7), e1000097. https://doi.org/10.1371/journal.pmed.1000097
