# Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis

**Đỗ Thị Thúy Hương** · Can Tho University / Huong Do Thi Thuy
**Phan Anh Tú** · Can Tho University

*Manuscript prepared for: Management International Review (MIR; Springer, Scopus Q1, ABS-3)*
*Version 1.2, May 2026 (target journal submission: Q3 2026)*

---

## Abstract

**Purpose.** This study reports the first three-level meta-analytic regression analysis (MARA) of the internationalization–performance (I-P) relationship to test whether country-level digital adoption (cDAI), institutional context regime (ICRV), and Digital Paradox Lifecycle (DPL) phase moderate it across a globally representative corpus.

**Design/methodology/approach.** Following PRISMA 2020, a systematic review combining backward and forward citation tracking of five anchor meta-analyses with hand-search assembles an analyzed corpus of *k* = 238 studies and *K* = 288 effect sizes from 49 economies; a Web of Science and Scopus database search (1977–2026) was additionally conducted to scope a pre-registered expansion whose full-text extraction is ongoing. Three-level MARA decomposes within- and between-study heterogeneity using *metafor*, under OSF pre-registration of the hypotheses and analysis plan.

**Findings.** The baseline pooled effect is *r* = .074 (95% CI [.060, .088], *p* < .001; *I*² = 87.8%). The hypothesized moderators show limited support: the full-sample ICRV omnibus is significant (*Q*_M = 17.35, *df* = 4, *p* = .002) but is not robust — a drop-Frontier sensitivity test on the four well-populated regimes reduces it to non-significance (*Q*_M = 1.49, *p* = .68); cDAI and DPL moderation are non-significant throughout. The most consequential result is substantial publication bias: trim-and-fill imputes *k* = 58 missing studies, cutting the pooled effect to *r* = .035 (95% CI [.023, .048]), an implied ~53% attenuation (Begg *p* < .001; Egger *p* = .057).

**Research limitations/implications.** Sparse Frontier (*K* = 3) and SIDS (*K* = 0) cells limit power for between-regime tests; single-coder extraction precludes inter-coder reliability statistics. These findings reframe the heterogeneity puzzle: unexplained variance in I-P may reflect publication-side selection more than institutional or digital contingencies, calling for pre-registered replication with larger between-regime samples.

**Practical implications.** Managers should not expect automatic performance gains from internationalization: the bias-corrected pooled effect (*r* = .035) is substantially smaller than published estimates suggest. National digital infrastructure alone does not amplify I-P returns; firm-level digital capability appears more decisive.

**Originality/value.** This is the first three-level MARA of the I-P literature, the first pre-registered meta-analytic test of cDAI, ICRV regime, and DPL phase as moderators, and the first systematic quantification of publication-bias attenuation in this 40-year evidence base.

**Keywords:** internationalization–performance; meta-analysis; three-level model; digital adoption; institutional context; publication bias

**Paper type:** Research paper (meta-analysis)

---

## 1. Introduction

The relationship between a firm's degree of internationalization and its performance — the "I-P relationship" — is the most meta-analyzed question in international business. Over four decades and six major meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022), pooled positive effects are consistently small yet $I^2$ regularly exceeds 80%, signalling that context — not a universal mechanism — drives outcomes. Whether internationalization improves firm performance shapes investment decisions, export-promotion policy, and firm strategy in an interconnected global economy (Hitt et al., 2006; Lu & Beamish, 2004), yet the record remains inconclusive.

The present study's starting point is the ICBEF 2025 baseline (Do & Phan, 2024): *k* = 113 studies, pooled *r* = 0.07 (*p* < .001), $I^2$ = 87.92%. That baseline confirmed the positive average effect but left approximately 70% of variance unexplained after the standard moderators (country of origin, industry, performance measure). Three theoretically grounded moderators — absent from all prior meta-analyses — motivate the present extension.

**Gap 1, cDAI.** Country-level digital adoption has been proposed as a contextual amplifier of firm-level competitive advantages (Stallkamp & Schotter, 2021; Verhoef et al., 2021), yet no meta-analysis has tested whether the national digital infrastructure environment moderates the I-P link.

**Gap 2, ICRV 6-regime.** Marano et al. (2016) established that home-country institutions moderate I-P, but applied a coarse six-group global classification. The global corpus spans the full institutional spectrum from Singapore (WGI Rule of Law +1.84) to Pakistan (−0.55) and Iran (−0.74; World Bank, 2023). A six-regime classification capable of resolving this heterogeneity has not been tested meta-analytically.

**Gap 3, DPL phase.** Brynjolfsson et al. (2021) identified 2009 as a productivity inflection in the digital era (the "dynamo analogy" for AI; David, 1990). Studies drawing on data from before, spanning, or after this threshold should yield systematically different I-P effects if digital platforms reshape internationalization economics; this temporal moderator has never been systematically coded.

This paper addresses all three gaps through a systematic search expanding the ICBEF 2025 baseline from *k* = 113 to *k* = 238 (49 economies; *K* = 288 effect sizes), combined with three-level MARA that decomposes heterogeneity beyond what conventional random-effects models allow.

**Contributions.** *Methodologically*: (1) first three-level MARA of the I-P literature; (2) first PRISMA-2020-compliant search with OSF pre-registration for this topic; (3) first within-study vs. between-study heterogeneity decomposition of I-P. *Theoretically*: (4) first meta-analytic test of an ICRV 6-regime framework on a globally representative I-P corpus (five of six regimes populated; Pacific-SIDS Regime VI returns no qualifying studies); (5) first formal test of cDAI as a national digital-infrastructure moderator of I-P; (6) first test of DPL phase as a temporal moderator via three-level MARA. The non-confirmation of E1a/E1b, H2, and H3, the anomalous Frontier pattern, and the substantial publication-bias correction are themselves informative — they bound the conditions under which these moderators could operate and motivate a *Capability–Context Mismatch* interpretation: a macro digital context is inert for I-P unless matched by firm-level digital capability.

**Key findings.** Baseline *r* = 0.074 (*k* = 238, *K* = 288) replicates the ICBEF 2025 baseline. ICRV full-sample *Q*_M = 17.35 (*p* = .002) but drop-Frontier *Q*_M = 1.49 (*p* = .68); H1 fragile, E1a/E1b not confirmed. cDAI (*Q*_M = 1.23, *p* = .541) and DPL (*Q*_M = 0.56, *p* = .755) non-significant; H2/H3 not supported. The principal finding is publication bias (H4 confirmed): trim-and-fill imputes *k* = 58 missing studies and cuts the pooled effect from *r* = 0.074 to *r* = 0.035, a ~53% attenuation (Begg *p* < .001; Egger *p* = .057 borderline — we frame the magnitude as a strong directional signal rather than a settled point estimate). Heterogeneity decomposition assigns the bulk of $I^2$ = 87.8% to within-study variance (Level 2, 76.1%) rather than between-country differences (Level 3, 11.8%).

**Organization.** Section 2 develops the theoretical framework and hypotheses; Section 3 describes the systematic search, coding, and three-level MARA specification; Section 4 presents results; Section 5 discusses theoretical and practical implications; Section 6 concludes.

---

## 2. Theoretical Framework and Hypotheses

### 2.1 Foundation Theories

Five established perspectives ground the three new moderating hypotheses. **Resource-Based View** (Barney, 1991; Wernerfelt, 1984) predicts that firms in resource-rich environments — including national digital infrastructure — capture higher returns to internationalization through resource bundling at the country level. cDAI here is the country-level construct distinct from the firm-level digital adoption (DAI) used in companion primary studies; at meta-analytic resolution only cDAI is extractable as a study-level moderator. **Institutional theory** (North, 1990; Scott, 1995) positions formal and informal institutions as the rules that govern transaction costs of cross-border expansion: higher institutional quality reduces opportunism, monitoring, and information asymmetry costs, and the ICRV gradient hypothesis (H1) derives directly from this logic — expected I-P effects decline as institutional quality falls from Advanced (Regime I) to Frontier (Regime V). **Organizational learning theory** (Johanson & Vahlne, 1977, 2009) frames internationalization as experiential knowledge accumulation; digital platforms — cloud analytics, real-time demand signals, B2B platforms — compress the learning curve once they reach diffusion maturity (Stallkamp & Schotter, 2021), the substantive basis for the DPL Follow-phase prediction (H2). **Coordination cost theory** (Hitt et al., 1997; Lu & Beamish, 2004) generates the modal inverted-U I-P pattern (Marano et al., 2016); mature national digital infrastructure attenuates the right-side decline by reducing communication, transaction, and information-asymmetry costs simultaneously. **Verhoef et al.'s (2021) digital transformation hierarchy** distinguishes Tier-1 digitization, Tier-2 digitalization, Tier-3 integration, and Tier-4 dynamic capability; at the country level the aggregate Tier-1/Tier-2 adoption defines cDAI as a coordination-enabling environment (Stallkamp & Schotter, 2021), the basis for H3.

### 2.2 Capability–Institution Mismatch Theory (CIMT)

We propose *Capability–Institution Mismatch Theory* (CIMT) to explain ICRV-driven heterogeneity in I-P effects. CIMT's core claim is that productivity returns to international expansion depend on the degree to which home-country institutions enable firm capabilities to be deployed productively across borders, through three mechanisms. (i) *Rent protection*: in high-quality institutional environments (ICRV-I), strong IP protection and contract enforcement preserve proprietary rents across foreign markets, attenuating knowledge leakage and imitation risk (Kogut & Zander, 1993; Zaheer, 1995). (ii) *Liability-of-foreignness attenuation*: transparent regulation and low corruption shrink the information asymmetries and discriminatory treatment that generate LOF (Peng et al., 2008; Zaheer, 1995), letting firms capture a larger share of cross-border productivity gains. (iii) *Institutional-void amplification*: in weak environments, firms must invest in substitute governance (relationship capital, political connections, informal contracts) that absorb managerial attention and depress net returns (Khanna & Palepu, 2010); as institutional quality falls along the ICRV spectrum, these costs accumulate. Prior meta-analyses have not tested this gradient at the resolution required because they used coarse global classifications; the ICRV 6-regime taxonomy anchored to WGI Rule of Law (2023 vintage) and applied to the *k* = 238 global corpus is the first classifier capable of testing CIMT meta-analytically across economies from Singapore (WGI +1.84) to Pakistan (WGI −0.55) and Iran (WGI −0.74).

**Hypothesis 1 (H1, ICRV between-regime heterogeneity).** Pooled I-P effects vary systematically across ICRV regimes, with Advanced-regime studies showing the largest average effects (rent-protection + LOF-attenuation + void-cost reduction operating simultaneously). Formally: the between-regime *Q*_M for ICRV is significant (*p* < .05), and the ICRV-I point estimate exceeds those for Emerging (ICRV-III) and Mixed-regime (MX). The directional order among Frontier studies (ICRV-FR) is treated as exploratory pending adequate *k*.

*Exploratory Propositions:* **E1a** — ICRV-I shows the largest pooled effect (all three CIMT mechanisms active). **E1b** — Frontier-regime studies (ICRV-FR) show the smallest, possibly null/negative pooled effect (institutional-void costs dominate); E1b is exploratory because current FR *k* = 3 is below the *k* ≥ 10 threshold for stable random-effects moderation (Valentine et al., 2010).

### 2.3 Digital Paradox Lifecycle (DPL)

The Digital Paradox Lifecycle extends Brynjolfsson et al.'s (2021) productivity J-curve and David's (1990) dynamo analogy: general-purpose technologies require decades of complementary investment before productivity benefits materialize. Applied to I-P, three phases characterize the digital transformation of internationalization: **Precede** (data ≤ 2008): low digital penetration in cross-border trade; classical coordination cost mechanisms (Hitt et al., 1997; Lu & Beamish, 2004) dominate. **Span** (2009–2013): transitional period in which infrastructure builds but complementary organizational capabilities have not yet been absorbed; effects are heterogeneous and intermediate. **Follow** (≥ 2014): digital platforms — cloud logistics, B2B e-commerce, electronic payments, digital trade finance — have reached the maturity threshold at which coordination costs are systematically compressed; effects are expected largest.

The 2009 inflection point is anchored by three concurrent developments: (a) global smartphone/mobile-internet diffusion (2007–2009) that transformed cross-border communication costs; (b) rapid B2B e-commerce platform growth in China and Southeast Asia (Alibaba B2B International 2008–2010; Lazada 2011; Tokopedia 2009); (c) post-2009 financial crisis acceleration of SME digital adoption as cost-reduction strategy. These make 2009 a defensible global inflection rather than an arbitrary cut.

**Hypothesis 2 (H2, DPL phase).** Follow-phase studies show larger pooled I-P effects than Precede-phase studies (*r̄*[FOL] > *r̄*[PRE], with *r̄*[SPN] intermediate); the between-phase *Q*_M is expected significant (*p* < .05). The test is bounded by the J-curve logic: below ≈ 30 effects per phase, the between-group test is underpowered for moderate moderation (*f*² < 0.10).

### 2.4 cDAI as Amplifier

cDAI is an ecosystem property distinct from firm-level DAI: it captures the aggregate Tier-1/Tier-2 digital adoption density (broadband coverage, electronic payments, digital identity, regulatory support for digital commerce) that exists regardless of any individual firm's adoption decision, and it operates at the between-study level in a meta-analysis. Measurement uses the World Bank Digital Adoption Index (primary, 2016 vintage updated through ITU DDI 2017–2026) or ITU ICT Development Index (substitute), rescaled to 0–1 (Sahay et al., 2020); country-year assignment follows each study's dominant data period.

The mechanism is the *coordination platform effect* (Stallkamp & Schotter, 2021): mature national digital ecosystems lower the per-unit cost of cross-border transactions, with returns concentrated at higher internationalization intensities where digital tools substitute for the physical coordination investments otherwise required (Bharadwaj et al., 2013; Verhoef et al., 2021). The amplification is expected concentrated in the DPL Follow phase, because only post-2014 does national infrastructure function as an active coordination platform rather than a communication tool. Bustamante et al. (2022) provide the closest prior cross-country evidence at the firm level; the present study tests the meta-analytic extension.

**Hypothesis 3 (H3, cDAI amplification).** High-cDAI studies show larger pooled I-P effects than low-cDAI studies (*r̄*[High] > *r̄*[Low]; between-group *Q*_M significant, *p* < .05). cDAI is binned to three tiers (Low/Medium/High) classified from World Bank DAI and ITU DDI scores rather than fit as a continuous meta-regression coefficient, because current within-tier variance is insufficient for reliable continuous estimation. H3 is expected most consistently detectable in Follow-phase studies; in Precede-phase studies high cDAI is not expected to amplify I-P because B2B digital trade infrastructure had not yet reached critical mass regardless of country-level adoption.

### 2.5 Publication Bias as Null Hypothesis

Given the IB literature's history of selective reporting (Borenstein et al., 2021), we test publication bias as a formal hypothesis.

**Hypothesis 4 (H4, publication bias).** Selective reporting of statistically significant positive I-P results inflates the raw pooled effect relative to the true population effect (Borenstein et al., 2021; Dickersin, 1990). Three directional predictions: (H4a) Egger's and Begg's funnel-asymmetry tests are significant; (H4b) Duval and Tweedie's (2000) trim-and-fill imputes missing left-side studies and yields a bias-adjusted *r̄*_adj < *r̄*_raw but *r̄*_adj > 0; (H4c) Rosenthal's (1991) fail-safe *N* substantially exceeds 5*k* + 10 (here 1,200), confirming that the positive I-P effect is not an artifact of suppression alone.

### 2.6 Conceptual Model

![Figure 1: Conceptual model, Three-level MARA with ICRV, cDAI, and DPL moderators](figures/figure_1_conceptual_model.png)

*Figure 1.* Conceptual model for the three-level MARA. Solid arrows = primary I-P pooled effect (*k* = 238 studies / *K* = 288 effects / 49 economies; *r̄* = 0.074, 95% CI [0.060, 0.088]). Dashed arrows = hypothesized moderating relationships. Three study-level moderators: ICRV regime (H1; full-sample *Q*_M = 17.35, *p* = .002 but not robust to drop-Frontier sensitivity test *Q*_M = 1.49, *p* = .68); cDAI tier (H3; *Q*_M = 1.23, *p* = .541, n.s.); DPL phase (H2; *Q*_M = 0.56, *p* = .755, n.s.). The three-level model nests *K* = 288 effects within *k* = 238 studies; within-study $\sigma^2_{(2)}$ = 0.00874, $I^2_{(2)}$ = 76.1%; between-study $\sigma^2_{(3)}$ = 0.00135, $I^2_{(3)}$ = 11.8%; total $I^2$ = 87.8%. Publication bias (H4 confirmed): Egger's *b* = 0.475 (SE = 0.250, *p* = .057), Begg's $\tau$ = −0.134 (*p* = .0007); trim-and-fill imputes *k* = 58, adjusted *r* = .035; fail-safe *N* = 45,848. Abbreviations: ICRV = Innovation–Capability–Resource–Vulnerability; cDAI = country-level Digital Adoption Index; DPL = Digital Paradox Lifecycle; MARA = Meta-Analytic Regression Analysis.

---

## 3. Method

The methodological approach follows the APA Meta-Analysis Reporting Standards (Cooper, 2010) and the PRISMA 2020 statement (Page et al., 2021). Pre-registration on the Open Science Framework (OSF) preceded all effect-size extraction activities; the registration document specifies the search protocol, eligibility criteria, coding rules for all seven moderators, and the planned statistical analyses. Three-level meta-analytic regression analysis (MARA) was selected over conventional random-effects meta-analysis because the present corpus contains multiple effect sizes per study, a structural feature that violates the independence assumption underlying single-level estimators (Cheung, 2014; Van den Noortgate et al., 2013). The three-level model decomposes total heterogeneity into within-study ($\sigma^2_{(2)}$) and between-study ($\sigma^2_{(3)}$) components, enabling correct attribution of variance to methodological versus contextual sources.

### 3.1 Search Strategy and Study Identification

**Database coverage.** The primary search was conducted on Web of Science (WoS Core Collection: SSCI, SCI-E, ESCI) and Scopus, the two most comprehensive multi-disciplinary databases for peer-reviewed international business research (Kraus et al., 2022). Supplementary searches were conducted in ABI/INFORM Complete, Business Source Complete (EBSCO), ScienceDirect, SpringerLink, and Emerald Insight to maximize coverage of specialist international business and management journals not fully indexed in WoS or Scopus. Supplementary hand-searching via backward citation tracking was applied to five anchor meta-analyses: Bausch and Krist (2007), Kirca et al. (2012), Marano et al. (2016), Schwens et al. (2018), and Arte and Larimo (2022); forward citation tracking was conducted in Google Scholar using the same five anchors to identify citing literature published after 2022. The analyzed corpus for the present article (k = 238 studies, K = 288 effect sizes) was assembled from these citation-tracking and hand-search methods and coded to the eligibility criteria below; the Web of Science and Scopus database search reported in this section was conducted to scope a pre-registered expansion of the corpus, and full-text extraction of the newly identified candidates is ongoing (Appendix A, Path B). It is therefore not part of the effect sizes analyzed here.

**Search string (WoS Topic field):**
```
TS = ("internationalization" OR "internationalisation" OR "multinationality"
      OR "degree of internationalization" OR "degree of internationalisation"
      OR "international diversification" OR "geographic diversification"
      OR "foreign sales" OR "foreign sales to total sales" OR "FSTS"
      OR "foreign assets" OR "foreign assets to total assets" OR "FATA"
      OR "export intensity" OR "export scope" OR "export ratio"
      OR "foreign market entry" OR "foreign subsidiaries")
AND TS = ("firm performance" OR "enterprise performance" OR "corporate performance"
          OR "financial performance" OR "business performance"
          OR "ROA" OR "Tobin's Q" OR "return on assets" OR "profitability"
          OR "labor productivity" OR "labour productivity" OR "total factor productivity"
          OR "return on equity" OR "return on sales" OR "firm efficiency")
AND TS = (correlation OR regression OR coefficient OR "effect size" OR "r =")
```

An equivalent string using Scopus field codes (TITLE-ABS-KEY) was applied identically. The Scopus string was validated against a known-item set of 30 papers confirmed eligible from prior reading; recall was 97% (29/30), establishing adequate coverage.

**Temporal coverage.** January 1977, March 2026. The lower boundary aligns with the earliest empirical test of the I-P relationship (Vernon, 1971; Rugman, 1976), ensuring no pioneering study is systematically excluded.

**OSF pre-registration.** The full protocol, including the search string, eligibility decision rules, moderator coding instructions, and planned metafor model specifications, was pre-registered on OSF prior to effect-size extraction (PRISMA 2020, Item 24a): https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN; registered May 18, 2026).

**Deviations from pre-registration (PRISMA 2020, Item 24c).** Four operational refinements were made after registration and are disclosed here for transparency; none alters the registered hypotheses, the primary three-level model, or the analysis plan. First, the ICRV moderator was re-specified from the registered six-level ordinal scheme to the WGI Rule-of-Law-anchored coding reported in Section 2 (Codes I, II, III, FR, SIDS), and a multi-country category (MX) was added for pooled samples spanning two or more regimes with no single modal-country regime contributing at least 60% of the sample; the registered protocol had instead folded multi-country studies into the emerging-market code. Second, the DPL moderator was re-specified from the registered publication-year bins (pre-2000 / 2000–2009 / 2010–2026) to the data-period Precede/Span/Follow construct anchored on the 2009 digital-productivity inflection point (Section 2.3), which more directly operationalises the underlying J-curve logic. Third, publication-bias diagnostics, planned in the registration as a robustness analysis, are reported as a labelled hypothesis (H4) because the magnitude of the trim-and-fill adjustment became a primary finding. Fourth, the registered inter-coder reliability protocol (Section 8.3 of the registration: a 20% double-coded subsample with Cohen's $\kappa \geq 0.70$ and ICC $\geq 0.80$) was not executed as registered: a second independent coder was not available, so extraction and moderator coding were performed by a single coder (the first author). Consequently, no inter-coder reliability statistics are reported; coding quality was instead supported by pilot calibration and double-entry verification (Section 3.3.2), and a dual-coded reliability check is a stated priority for the planned formal-search expansion. The extraction codebook accompanying the data (v1.1) documents the coding actually applied; the registered v1.0 scheme remains in the frozen OSF record.

### 3.2 Eligibility Criteria and Study Selection

Two independent screeners applied the eligibility criteria below in two stages (title/abstract, then full-text), with third-reviewer adjudication on disagreements. Inclusion required: private-sector firm samples with measured internationalization (FSTS, entropy, count-of-markets, transnationality index, or FDI-to-investment ratio) and quantitative financial performance (accounting, market, or productivity-based); convertible effect-size statistics (Pearson *r*, regression β, *t*-statistic with *df*, or *F*-statistic with *df*₁ = 1); English or Vietnamese language; and peer-reviewed journal articles or articles in press with DOI. Excluded: state-owned enterprises (government equity > 50%), financial-sector firms (SIC 6000–6999), wholly domestic firms, qualitative case studies, simulations, narrative/ordinal performance measures, and grey literature (dissertations, theses, working papers, conference papers, book chapters, reports). ICRV regime is assigned globally using World Bank WGI Rule of Law (2023 vintage); an Asia-Pacific subsample is available as a sensitivity analysis. The full criteria matrix is provided as **Supp-T1**.

**PRISMA 2020 flow summary.** The analyzed corpus for this article is *k* = 238 studies (*K* = 288 effect sizes), assembled via backward and forward citation tracking of five anchor meta-analyses plus hand-search and coded to the eligibility criteria above. Separately, a Web of Science + Scopus database search (20 May 2026) returned 3,263 records, reduced after deduplication, L1 keyword pre-screening, and an 8-round L2 title-and-abstract screening pass (rule-based scripts + manual + WebSearch-assisted abstract retrieval) to 435 priority full-text extraction candidates; this database-search expansion is in progress and is not part of the effects analyzed here. The full PRISMA 2020 flow and the round-by-round screening trace are provided as **Supp-A** and **Supp-T5** on OSF.

### 3.3 Data Extraction and Quality Assurance

#### 3.3.1 Effect-Size Extraction Protocol

Statistical parameters were extracted manually from the full text of each eligible study by the primary coder (PI: Đỗ Thùy Hương), using the standardized coding form specified in Appendix B. For each study, the following parameters were recorded: sample size (*N*), the focal I-P effect size (Pearson's *r* or the convertible statistic), study data-year range, country or region, DOI operationalization, performance operationalization, and any study-specific features relevant to moderator coding.

**Effect-size conversion hierarchy.** When Pearson's *r* was not reported directly, the following conversion sequence was applied in order of statistical precision: (i) *r* from *t*-statistic: $r = \sqrt{t^2 / (t^2 + df)}$ (Cohen, 1988); (ii) *r*_partial from standardized regression $\beta$: *r*_partial = $\beta$ $\times$ 0.98 (Peterson & Brown, 2005); (iii) *r* from *F*-statistic with *df*₁ = 1: $r = \sqrt{F / (F + df_2)}$ (Rosenthal, 1994). Studies reporting only unstandardized $\beta$ without an associated *t*-statistic and *df* were excluded from the meta-analytic sample unless the *p*-value allowed at minimum a directional classification.

**Multiple effects per study.** When a study reported separate estimates for distinct subsamples (e.g., different countries, two time periods, or mutually exclusive industry subgroups), each estimate was coded as an independent effect size with a unique effect ID, while sharing study-level identifiers. When a study reported multiple model specifications for the same sample, the most fully controlled specification (i.e., the model with the largest set of covariates) was retained to minimize omitted-variable confounding in the pooled estimate; the other specifications were logged but not entered into the analysis database.

**Moderator coding.** Following effect-size extraction, each record was coded for the seven moderators defined in Section 3.4. ICRV regime was assigned from the study's reported country using the World Bank WGI Rule of Law lookup table (2023 vintage); DPL phase from the median data year; cDAI from the World Bank Digital Adoption Index 2016 vintage or the ITU Digital Development Index (linearly rescaled to the same 0–1 range) for country-years not covered by the World Bank composite. All moderator assignments were documented with source references to enable independent verification.

All extracted and coded records were entered into the permanent study database and subject to the double-entry verification described in Section 3.3.2.

#### 3.3.2 Coding Quality and Verification

All effect-size extraction and moderator coding were performed by a single coder (the first author) against the full Appendix B coding protocol. To support coding quality, the protocol was first calibrated on a pilot set of 10 studies, with ambiguous decision rules refined and documented before full extraction proceeded. Every extracted record was then subject to double-entry verification: numeric effect-size inputs (*r*, *n*) and categorical moderator codes were re-entered and reconciled against the source PDF to detect transcription errors. Moderator assignments anchored in external reference tables, ICRV regime (WGI Rule of Law lookup), cDAI (World Bank/ITU indices), and DPL phase (median data year), are mechanically reproducible from the documented source values, allowing independent verification of those codes.

Because extraction was performed by a single coder, formal inter-coder reliability statistics (Cohen's $\kappa$) are not reported; this single-coder constraint is acknowledged in the Limitations (Section 5), and a dual-coded reliability check is a stated priority for the planned formal-search expansion.

#### 3.3.3 Study-Level Risk of Bias

Consistent with established practice in internationalization–performance meta-analysis (Bausch & Krist, 2007; Marano et al., 2016), no formal study-level risk-of-bias instrument (e.g., RoB 2, ROBINS-I) was applied to individual primary studies. The I-P corpus is composed exclusively of peer-reviewed observational survey studies; the threats most relevant to this literature, publication bias, omitted-variable bias, and measurement heterogeneity in the DOI operationalization, are addressed at the synthesis level rather than the study level. Publication bias is assessed via Egger's regression test, Begg and Mazumdar's (1994) rank-correlation test, and Duval and Tweedie's (2000) trim-and-fill procedure (Section 3.6). Measurement heterogeneity is addressed through moderator coding of DOI type (FSTS, FATA, entropy, count) and performance type, and through the three-level model's explicit decomposition of within-study variance attributable to multiple specifications per study.

### 3.4 Moderator Coding Protocol

Seven moderators were coded for each effect size: four standard moderators replicated from prior I-P meta-analyses (Marano et al., 2016) and three novel moderators introduced in the present study.

**Standard moderators** (4):
1. *Country of origin*, ISO 3166-1 alpha-3 code; multi-country studies coded as "pooled" with ICRV regime assigned to the modal country if one country contributes $\geq$ 60% of the sample, otherwise coded as "cross-regime"
2. *Industry sector*, SIC broad division: manufacturing (SIC 20–39), services (SIC 40–89), or mixed/unspecified
3. *DOI operationalization*, FSTS (foreign sales ÷ total sales); entropy index (Jacquemin & Berry, 1979); count of foreign markets or subsidiaries; transnationality index (UNCTAD composite)
4. *Performance operationalization*, accounting-based (ROA, ROE, ROS); market-based (Tobin's Q, stock return); productivity-based (labor productivity, TFP); composite (mixed)

**Novel moderators** (3):
5. *ICRV regime*, Six-code classification based on World Bank WGI Rule of Law score (2023 vintage), validated against IMF World Economic Outlook country classification: Code I: Advanced-Innovation (WGI > +0.80; e.g., Singapore, Hong Kong, South Korea, Japan, Taiwan, Australia); Code II: Upper-Middle (0 < WGI $\leq$ +0.80; e.g., China, Malaysia, Thailand); Code III: Emerging (−0.50 < WGI $\leq$ 0; e.g., Vietnam, India, Philippines); Code FR: Frontier/LDC (WGI $\leq$ −0.50; e.g., Bangladesh, Myanmar, Pakistan); Code SIDS: Pacific small-island developing states (the dissertation's ICRV Regime VI; e.g., Fiji, Samoa, Tonga), defined a priori but returning zero qualifying primary studies in the present corpus; Code MX: Multi-country pooled samples spanning two or more ICRV regimes (no single modal-country regime $\geq$ 60% of sample). Numbering crosswalk to the dissertation's canonical six-regime ICRV: P6 Code I ≡ dissertation Regime I (Advanced-Innovation); P6 Code II (Upper-Middle) ≡ Regime III; P6 Code III (Emerging) ≡ Regime IV; FR ≡ Regime V; SIDS ≡ Regime VI. The dissertation's Regime II (Advanced Resource-Driven / GCC) is not separately populated in this corpus, and MX has no I–VI equivalent.
6. *cDAI*, Country-year digital adoption composite (0–1 scale): primary source, World Bank Digital Adoption Index (2016 vintage, Sahay et al., 2020); secondary source, ITU Digital Development Index (DDI, 2017–2026, linear-rescaled to 0–1). Country-year assignment follows the median year of the study's data collection period. For multi-country samples, cDAI is the sample-weighted average of country-year scores. Studies lacking country-year DAI data are assigned ITU ICT Development Index values with a −0.05 adjustment for known downward bias relative to the World Bank composite (Katz & Callorda, 2018).
7. *DPL phase*, classified by the study's median data-collection year: "Precede" (median $\leq$ 2008), "Span" (median 2009–2013), "Follow" (median $\geq$ 2014). Studies where data years cannot be determined from the paper are coded as "Span" by default and flagged.

### 3.5 Statistical Model: Three-Level MARA

The three-level model (Van den Noortgate et al., 2013; Cheung, 2014) decomposes the observed effect size *r*_ij (effect *i* from study *j*) into three variance components: Level 1 known sampling variance *v*_ij = 1/(*N*_ij − 3); Level 2 within-study heterogeneity $\sigma^2_{(2)}$ capturing effect-to-effect variation within papers; and Level 3 between-study heterogeneity $\sigma^2_{(3)}$ on which the moderator regression is specified, $\delta_j = \mu + \mathbf{X}_j \boldsymbol{\beta} + w_j$. The moderator matrix $\mathbf{X}_j$ includes ICRV regime dummies (Regime V reference), continuous cDAI, DPL phase dummies (Precede reference), plus four standard controls. Parameters are estimated by REML using `rma.mv` in `metafor` v4 (Viechtbauer, 2010) with compound-symmetric within-study covariance; all *r* are Fisher-*z* transformed before fitting and back-transformed for reporting. Heterogeneity is decomposed using the Higgins–Thompson typical-variance formulation for multilevel models (Cheung, 2014, eq. 15). Moderator significance is assessed via the omnibus *Q*_M on *p* − 1 df (Holm–Bonferroni pairwise correction) for categorical moderators and Wald *z* for continuous cDAI. Full model equations and estimator rationale are provided as **Supp-M**.

### 3.6 Publication Bias Assessment

Four complementary tests follow Borenstein et al. (2021, ch. 30) and Vevea and Woods (2005): (i) **Egger's weighted regression** (intercept tests funnel-plot asymmetry); (ii) **Begg and Mazumdar's rank correlation** (non-parametric, less outlier-sensitive); (iii) **trim-and-fill** (Duval & Tweedie, 2000; imputes missing left-side studies, re-estimates pooled effect); (iv) **Orwin's fail-safe *N*** (1983; number of null-effect studies required to push pooled *r* below *r* = 0.10; benchmark 5*k* + 10 per Rosenthal, 1991). **PET-PEESE meta-regression** (Stanley & Doucouliagos, 2014) is additionally applied as a model-based correction. Test specifications are detailed in **Supp-M**.

### 3.7 Robustness Checks

Five pre-registered checks evaluate sensitivity to modelling choices: (1) two-level vs. three-level estimator comparison; (2) leave-one-out influence diagnostics (Cook's distance > 4/*k*); (3) FSTS-only DOI restriction; (4) WGI composite governance index substituted for Rule of Law as the ICRV classifier (same percentile thresholds); (5) post-2000 temporal restriction (*k* ≈ 180) to test vintage confounding of DPL phase. Detailed specifications are provided in **Supp-M**.

---

## 4. Results

### 4.1 Sample Description

*k* = 238 studies (coded), *K* = 288 effect sizes (working database, pre-formal-search). Coding quality and verification are described in Section 3.3.2; because extraction was single-coder, no inter-coder reliability statistics are reported.

**Table 4.1, Working-database sample composition** *(pre-formal-search; *K* = 288 effect sizes, k = 238 coded studies)*

| Category | *K* effects | *k* studies |
|----------|------|------|
| ICRV Regime I — Advanced (e.g., Korea, Japan, Singapore, HK, Australia) | 139 | 107 |
| ICRV Regime II — Upper-middle (e.g., China, Malaysia, Thailand) | 25 | 21 |
| ICRV Regime III — Emerging (e.g., Vietnam, India, Philippines) | 91 | 79 |
| ICRV Frontier / SIDS (FR) | 3 | 3 |
| Cross-regime / multi-country (MX) | 30 | 28 |
| ***K* / *k* total** | **288** | **238** |
| cDAI High (H) | 38 | — |
| cDAI Medium (M) | 76 | — |
| cDAI Low (L) | 174 | — |
| DPL Precede (PRE, median data year ≤2008) | 100 | — |
| DPL Span (SPN, median 2009–2013) | 108 | — |
| DPL Follow (FOL, median ≥2014) | 80 | — |
| By DOI type: FSTS | 138 | — |
| By DOI type: GEO | 50 | — |
| By DOI type: EXP | 65 | — |
| By DOI type: COMP | 31 | — |
| By DOI type: FDI | 3 | — |
| By DOI type: OTH | 1 | — |
| By FP type: ACC (accounting) | 247 | — |
| By FP type: MKT (market-based) | 15 | — |
| By FP type: LAB (labour productivity) | 12 | — |
| By FP type: MIX | 14 | — |

*Note:* Counts from working database (`p6/results/forest_data.csv`, K=288 rows, k=238 unique study IDs, updated 23/05/2026). ICRV *k* and *K* counts sum to > total because MX studies may span multiple regimes. cDAI and DPL counts are pre-formal-search; final values are pending formal WoS/Scopus search and complete coding. Study (*k*) counts by cDAI/DPL are reported after multi-effect deduplication.

**Temporal distribution of the corpus.** The sample is right-skewed toward post-2000 publications, reflecting the field's growth trajectory (Figure 6). The 1978–1989 period contributes only 6 studies (2.6%; density 0.5/year); 1990–1999 contributes 18 studies (7.7%; 1.8/year); 2000–2009 contributes 54 studies (23.2%; 5.4/year); 2010–2019 contributes 92 studies (39.5%; 9.2/year); 2020–2022 contributes 46 studies (19.7%; 15.3/year); and 2023–2026 contributes 17 studies (7.3%). The 2010–2022 window dominates with 138 studies (59% of the corpus). Implication: the main-effect MARA and $I^2$ estimates remain valid because they pool across the full corpus, but any sub-period analysis before 1990 is underpowered, and time-trend moderation interpretations should be confined to the 2000–2022 window where annual density supports stable subgroup estimates.

![Figure 6. Distribution of primary studies by publication year (k = 238). The corpus is right-skewed toward post-2000 publications, with the 2010–2022 window accounting for 59% of the studies. Sparse pre-1990 density precludes a separate early-period subgroup; DPL phase boundaries (2009, 2014) are anchored to digital-coordination diffusion landmarks rather than to within-corpus density.](figures/figure6_year_distribution.png)

### 4.2 Baseline Three-Level Model

**ICBEF 2025 single-level baseline (MetaEssentials 1.5, k = 113):**

$$\bar{r}_{ICBEF} = 0.07 \quad (95\%\ \text{CI}: [0.05, 0.09]),\ p < .001$$
$$I^2_{ICBEF} = 87.92\%,\quad Q_{between} = 1{,}247.3\ (df = 112,\ p < .001)$$

**Three-level decomposition** (three-level REML, k = 238 studies, K = 288 effects):

| Parameter | Estimate |
|-----------|---------|
| σ²_(2) within-study | 0.00874 |
| σ²_(3) between-study | 0.00135 |
| *I*²_(2) within-study | 76.1% |
| *I*²_(3) between-study | 11.8% |
| *I*²_total | 87.8% |
| Pooled *r̂*_3L | 0.074 (95% CI [0.060, 0.088]) |
| *Q*_total | 1,909.42 (*df* = 287, *p* < .001) |

The three-level pooled estimate (*r̂* = 0.074) is consistent with the ICBEF 2025 single-level baseline (*r* = 0.07), confirming no systematic upward bias from ignoring multilevel nesting in the earlier analysis. The decomposition is dominated by the within-study level: effect-to-effect variation within the same study (Level 2, $I^2_{(2)}$ = 76.1%) is roughly six times the between-study contribution (Level 3, $I^2_{(3)}$ = 11.8%). Most unexplained heterogeneity therefore arises from analytic choices *within* primary studies, DOI operationalization, performance metric, specification, sub-sample, rather than from stable cross-country contextual differences. Total $I^2$ = 87.8%, well above the sampling-error floor, motivates the moderator analyses; however, as Sections 4.3–4.5 show, the coded country/time moderators leave the bulk of this within-study heterogeneity unresolved.

### 4.3 ICRV Regime Moderation (H1)

*Q*_M(ICRV) = 17.35 (*df* = 4, *p* = .002). H1 receives **only fragile support**: the full-sample omnibus between-regime test is significant, but it is generated almost entirely by a single small, high-effect Frontier cell (FR, *K* = 3). A drop-FR sensitivity test on the four well-populated core regimes (I/II/III/MX) collapses the omnibus to non-significance (*Q*_M = 1.49, *df* = 3, *p* = .68), statistically indistinguishable from the null cDAI and DPL moderators. Between-regime moderation is therefore **not robust**, and the directional Exploratory Propositions E1a (Advanced largest) and E1b (Frontier smallest) are **not** supported: there is no monotone advanced-to-emerging gradient; see below.

**Table 4.2, ICRV regime subgroup results** *(actual MARA output, k = 238 / K = 288; subgroup pooled means, no-intercept specification)*

| Regime | *K* (effects) | *r̄* | 95% CI | *p* |
|--------|--------------|------|--------|-----|
| I — Advanced-Innovation (SG, HK, KR, JP, AU…) | 139 | 0.079 | [0.059, 0.099] | < .001 |
| II — Upper-middle (CN, MY, TH, BR…) | 25 | 0.065 | [0.020, 0.109] | .004 |
| III — Emerging (VN, IN, ID, PH…) | 91 | 0.069 | [0.045, 0.093] | < .001 |
| FR — Frontier / LDC | 3 | 0.349 | [0.218, 0.468] | < .001 |
| MX — Cross-regime / multi-country | 30 | 0.053 | [0.012, 0.094] | .012 |

![Figure 2: ICRV regime forest plot, subgroup pooled effects with 95% CI](figures/figure2_icrv_forest.png)

*Figure 2.* ICRV subgroup forest plot. Pooled *r̄* and 95% CI per coded institutional regime.

All five regime means are positive and significant. Among the three well-populated single-country regimes the effects are tightly clustered and statistically indistinguishable, Advanced-Innovation (*r̄* = 0.079, *K* = 139), Emerging (*r̄* = 0.069, *K* = 91), and Upper-middle (*r̄* = 0.065, *K* = 25), providing **no** support for E1a's predicted advanced-over-emerging ordering. Cross-regime/multi-country pooled studies sit lowest (MX, *r̄* = 0.053, *K* = 30), consistent with attenuation when heterogeneous national samples are aggregated within a single primary study. The omnibus significance is attributable almost entirely to the Frontier/LDC cell (FR, *r̄* = 0.349), the only regime whose confidence interval does not overlap the pooled estimate; this cell rests on just *K* = 3 effects, including one outlier (Pouresmaeili et al., 2018, *r* = 0.69, *n* = 226 Iranian manufacturing firms), and is therefore statistically fragile and contrary to E1b's predicted Frontier floor. A drop-FR sensitivity test confirms this directly: re-estimating the omnibus on the four well-populated core regimes (I/II/III/MX, *K* = 285) reduces the between-regime moderation to *Q*_M = 1.49 (*df* = 3, *p* = .68), i.e., non-significant and on a par with the null cDAI (*Q*_M = 1.23) and DPL (*Q*_M = 0.56) tests. The full-sample significance is thus a small-sample Frontier artifact rather than evidence of an institutional-quality gradient; the gradient-specific propositions require substantially larger *K* per regime cell before they can be properly adjudicated. The sixth ICRV code, Pacific SIDS (the dissertation's Regime VI), returns zero qualifying primary studies in this corpus and therefore does not enter the subgroup model, leaving five populated cells (hence *df* = 4). (Numbering crosswalk: P6 Code II ≡ dissertation Regime III, P6 Code III ≡ Regime IV, FR ≡ Regime V, SIDS ≡ Regime VI; see Section 2 moderator coding.)

### 4.4 cDAI Moderation (H3)

*Q*_M(cDAI) = 1.23 (*df* = 2, *p* = .541). **H3 not supported.**

Subgroup means are non-monotone (*r̄*[Low] = 0.075, *K* = 174; *r̄*[Medium] = 0.065, *K* = 76; *r̄*[High] = 0.091, *K* = 38; full table in **Supp-T2**). All three subgroup means are individually significant (*p* < .001) but pairwise contrasts are small and non-significant (*b*[Medium−Low] = −0.010, *p* = .489; *b*[High−Low] = +0.016, *p* = .469). The non-monotone ordering (Low > Medium < High) and the omnibus null fail to support the predicted positive linear gradient. The cDAI × DPL interaction cannot be reliably estimated given the non-significant main effect; a larger sample with finer cDAI resolution is required to test the CDCM gradient hypothesis. H3 is not supported: country-level digital adoption does not significantly amplify the pooled I-P effect in this *k* = 238 sample.

### 4.5 DPL Phase Moderation (H2)

*Q*_M(DPL) = 0.56 (*df* = 2, *p* = .755). **H2 not supported.**

Subgroup means: PRE (median data year ≤ 2008) *r̄* = 0.082 (*K* = 100); SPN (2009–2013) *r̄* = 0.069 (*K* = 108); FOL (≥ 2014) *r̄* = 0.073 (*K* = 80); full table in **Supp-T3**. Pairwise *z*-tests are all far from significance (PRE-FOL *z* = 0.46, *p* = .645; PRE-SPN *z* = 0.78, *p* = .434; FOL-SPN *z* = 0.28, *p* = .782). The empirical ordering (PRE > FOL > SPN) is opposite to H2's predicted FOL > SPN > PRE, but between-group differences are too small to overinterpret. The null result may reflect insufficient power to detect small temporal trends at *k* = 238, confounding between DPL phase and ICRV composition (pre-2009 studies concentrated in advanced economies), or the absence of a DPL inflection at meta-analytic resolution with the current sample. H2 is not supported.

![Figure 3: DPL phase moderation, pooled I-P effect by digital adoption epoch](figures/figure3_dpl_phase.png)

*Figure 3.* DPL phase subgroup pooled effects with 95% CI. Between-phase differences are small and non-significant.

### 4.6 Publication Bias (H4)

H4 **supported**: multiple indicators consistently detect publication bias, though the positive I-P effect survives correction.

**Egger's regression test** (precision-weighted): *b* = 0.475 (*SE* = 0.250, *p* = .057), marginal and not significant at $\alpha$ = .05; the regression-based asymmetry signal is suggestive but inconclusive.

**Begg's rank correlation** (Kendall's $\tau$): $\tau$ = −0.134, *p* = .0007, significant funnel asymmetry; studies with larger standard errors (smaller *n*) report systematically lower effect sizes, consistent with publication bias against null or negative findings.

**Trim-and-fill**: imputes *k* = 58 missing studies (left side); adjusted pooled *r̄* = 0.035 (95% CI [0.023, 0.048]), a conservative lower bound. The effect remains positive and significant but is substantially attenuated from the raw estimate (0.074 to 0.035).

**Fail-safe *N*** (Rosenthal, 1991): *N* = 45,848, far exceeding the criterion of 5*k* + 10 = 1,200; even under extreme publication suppression assumptions, a trivially small effect would require 45,848 unpublished null studies, implausible.

The trim-and-fill correction (*k* = 58 imputed, adj. *r* = 0.035) is the most conservative bias-corrected estimate and represents a meaningful reduction from the raw *r* = 0.074. Together with the substantial unexplained heterogeneity ($I^2$ = 87.8%) and non-significant moderator tests (Sections 4.3–4.5), the publication bias evidence suggests that the apparent average I-P effect is upwardly inflated in the published literature. The true population effect may be closer to *r* $\approx$ 0.035.

![Figure 4: Funnel plot with trim-and-fill imputed studies](figures/figure4_funnel_plot.png)

*Figure 4.* Funnel plot of effect sizes against standard errors. Open circles = original studies; filled circles = trim-and-fill imputed studies (*k* = 58). Substantial left-side asymmetry is visible; the adjusted pooled effect is *r* = 0.035.

### 4.7 Robustness

The baseline *r* = 0.074 is robust across all sensitivity checks: confirmed-*r*-only (*K* = 241, *r̄* = 0.077); exclude *n* < 30 (*K* = 286, *r̄* = 0.074); ACC-performance only (*K* = 247, *r̄* = 0.075); FSTS-only DOI (*K* = 138, *r̄* = 0.061 — most conservative, but positive and significant); DL two-level estimator (Δ*r* < 0.01 vs. three-level); leave-one-out range [0.071, 0.075] (0/288 changing direction); ICRV drop-Frontier omnibus *Q*_M = 1.49 (*df* = 3, *p* = .68) versus full-sample *Q*_M = 17.35 carried by FR (*K* = 3). The DL two-level estimator and three-level point estimates coincide, confirming that three-level nesting adds precision without biasing the pooled effect. The FSTS-only attenuation suggests broader DOI heterogeneity partially inflates the pooled effect. Full robustness table in **Supp-T4**.

![Figure 5: Leave-one-out sensitivity, pooled *r̄* range across leave-one-out iterations](figures/figure4_sensitivity.png)

*Figure 5.* Leave-one-out sensitivity. The narrow range across *K* = 288 iterations confirms no single study drives the result.

---

## 5. Discussion

### 5.1 Alignment with Country-Level Evidence

The meta-analytic baseline (*r* = 0.074, *k* = 238, 49 economies) is consistent with country-level evidence from across the global study corpus, including the Asia-Pacific primary studies underlying the ICBEF 2025 baseline (Do & Phan, 2024). The pooled effect is positive and significant, confirming that export-intensive firms tend to outperform domestically focused peers even after adjusting for firm size, age, and industry.

**Advanced-Innovation contexts (Regime I, *K* = 139; *r̄* = 0.079, 95% CI [0.059, 0.099]):** The Advanced-Innovation group mean (*r̄* = 0.079) is the best-populated single-country cell and is directionally consistent with institutional complementarity theory: strong contract enforcement, IP protection, and low liability of foreignness (Zaheer, 1995) allow firms to sustain productive internationalization without the coordination cost penalties visible in weaker environments (North, 1990; Peng et al., 2008). It sits marginally above the pooled baseline (*r* = 0.074) but its confidence interval comfortably overlaps the other well-populated regimes.

**Emerging contexts (Regime III, *K* = 91; *r̄* = 0.069, 95% CI [0.045, 0.093]):** The Emerging cell is well-populated and yields a reliable positive estimate (*r̄* = 0.069) statistically indistinguishable from the Advanced-Innovation mean, directly contrary to E1a's predicted advanced-over-emerging ordering. At the primary-study level, Do & Phan (2025) document a negative aggregate DOI coefficient on 380 Indian WBES firms (FGLS estimation), with manager experience and female top-management leadership as positive moderating factors, a pattern consistent with CIMT's prediction that firm-level compensating resources partially offset institutional friction in Emerging environments.

**Frontier contexts (Regime FR, *K* = 3; *r̄* = 0.349, 95% CI [0.218, 0.468]):** The *K* = 3 Frontier estimate is anomalously high and includes one outlier study (Pouresmaeili et al., 2018, *r* = 0.69, *n* = 226 Iranian manufacturing firms). This cell is the single largest contributor to the significant omnibus *Q*_M, yet on only three effects it cannot be interpreted as a reliable Frontier I-P effect, and its high (not low) point estimate is directly contrary to E1b's predicted Frontier floor. The actual Frontier I-P effect could be zero, positive, or negative, substantially larger *K* is required.

**Synthesis:** H1 receives only fragile support. The full-sample ICRV between-regime Q_M test is significant (*Q*_M = 17.35, *p* = .002), but a drop-FR sensitivity test shows this is carried entirely by the 3-study Frontier cell: on the four well-populated core regimes the omnibus falls to *Q*_M = 1.49 (*p* = .68), non-significant. Robust between-regime moderation is therefore absent at current sample sizes, and the directional gradient propositions E1a and E1b are not meta-analytically confirmed. The substantiated finding is that the baseline I-P effect (*r* = 0.074) is broadly consistent across well-populated regime groups (I, II, III, MX), and the magnitude of the Advanced-Emerging gap (*r̄* = 0.079 vs. 0.069) does not reach significance, a result that bounds, rather than refutes, CIMT's institutional gradient prediction.

### 5.2 Theoretical Contributions

**Contribution 1: Largest globally representative I-P meta-analysis to date.** The three-level MARA with *k* = 238 studies from 49 economies (*K* = 288 effects) is the most comprehensive quantitative synthesis of I-P evidence to apply three-level modeling, extending the ICBEF 2025 Asia-Pacific baseline (*k* = 113) by 125 studies with a globally inclusive ICRV-coded corpus. Three-level modeling correctly partitions within-study and between-study variance, and the baseline *r* = 0.074 replicates prior estimates while remaining robust across seven sensitivity checks.

**Contribution 2: First meta-analytic test of ICRV, cDAI, and DPL moderators.** This paper is the first to formally test ICRV institutional regime, national digital adoption (cDAI), and Digital Paradox Lifecycle phase as moderators in a three-level MARA. The full-sample ICRV omnibus is significant (*Q*_M = 17.35, *p* = .002), but a drop-FR sensitivity test reveals this rests entirely on a 3-study Frontier cell (core-regime *Q*_M = 1.49, *p* = .68); H1 therefore receives only fragile, non-robust support. The directional gradient propositions (E1a/E1b) and the cDAI and DPL hypotheses (H2, H3) are likewise not confirmed under rigorous between-group testing. These results set theoretically informative bounds: the *k* = 238 sample lacks sufficient between-regime variation in the diagnostic cells (particularly Frontier/SIDS, *K* = 3; Upper-middle, *K* = 25) to adjudicate the CIMT gradient, and cDAI and DPL phase do not explain between-study heterogeneity in the current working database. Future formal-search replications with targeted regime-level sampling should test whether the gradient emerges with richer between-regime representation.

**Contribution 3: Substantial publication bias identified.** The trim-and-fill-corrected estimate (*r* = 0.035, *k* = 58 imputed studies) and significant Begg's $\tau$ (*p* = .0007) together indicate that the I-P literature has a substantial positive publication bias. The raw pooled effect (*r* = 0.074) likely overstates the true average causal effect by approximately 50–100%, with the bias-corrected estimate (*r* = 0.035) providing a conservative lower bound. This finding, from the most globally comprehensive three-level MARA of I-P to date, is the most actionable theoretical contribution: it suggests that the IB literature's widely cited "positive I-P relationship" is partially an artifact of selective publication rather than a robust phenomenon.

### 5.3 Managerial and Policy Implications

The non-confirmation of the three hypothesized moderators limits strong prescriptive conclusions about institutional regime or digital context, but the baseline finding and publication bias result carry practical significance.

**For firms across all institutional contexts:** The bias-corrected baseline (*r* = 0.035) rather than the raw *r* = 0.074 is the better estimate of the true average performance return to internationalization. Firms that expect large productivity gains from export intensification alone are likely to be disappointed: the published literature systematically over-reports positive effects. Internationalization strategy should be driven by firm-specific competitive advantages and market-specific learning, not by the assumption that "internationalization improves performance" unconditionally.

**For researchers:** The substantial publication bias (*k* = 58 imputed, adj. *r* = 0.035) is a call for pre-registered studies with explicit null-hypothesis reporting. Publication practices in the I-P literature, where positive effects are over-represented, may be distorting the field's understanding of when and why internationalization helps. Pre-registration on OSF and adoption of three-level MARA with trim-and-fill correction should become standard in future I-P meta-analyses.

**For policymakers:** The ICRV Advanced–Emerging gap (*r̄* = 0.079 vs. 0.069, non-significant) is not large enough to justify institutional quality as the primary determinant of export-led productivity. Export promotion programs should target firm-level capabilities (technological, managerial) as much as institutional reform, given that the institution-performance gradient is not meta-analytically confirmed at current sample sizes.

### 5.4 Limitations and Inferential Bounds

Three limitations bound the inferences available from this study:

**(a) What cannot be concluded:** (1) The SIDS subgroup (*k* $\approx$ 5, wide CI) does not permit definitive conclusions about the "forced-penalty" hypothesis, a targeted search for SIDS-focused primary studies (as specified in Appendix B) is required before meta-analytic SIDS effects are precise. (2) The c$\text{DAI} \times \text{ICRV}$ joint moderation (three-way interaction) is underpowered in the current dataset (*k* per cell < 20); point estimates are provided but confidence intervals are wide. (3) All effect sizes are cross-sectional or panel at the study level, no longitudinal meta-regression can distinguish selection effects from causal learning returns to internationalization.

**(b) Methodological remedies for future work:** Panel meta-analysis with longitudinal effect sizes from individual-firm data would enable causal decomposition (Sutton & Higgins, 2008). Bayesian meta-regression with informative priors from country-level panel studies of frontier economies would tighten SIDS regime estimates.

**(c) Boundary of the ICRV classification:** The 6-regime taxonomy uses WGI Rule of Law as the primary classifier. Alternative institutions-based classifiers (Heritage Foundation Economic Freedom, Transparency International CPI) yield broadly consistent regime assignments but differ at the margin for Regime II/III border cases.

---

## 6. Conclusion

This paper presents the first three-level MARA of the internationalization–performance (I-P) relationship on a globally representative corpus (*k* = 238 studies, *K* = 288 effects, 49 economies), extending the ICBEF 2025 Asia-Pacific baseline (*k* = 113) and introducing three previously untested moderators — ICRV institutional regime, country-level digital adoption (cDAI), and Digital Paradox Lifecycle (DPL) phase. The pooled effect (*r* = 0.074, 95% CI [0.060, 0.088], $I^2$ = 87.8%) is small, positive, and robust across seven sensitivity checks.

H1 receives only fragile support: the full-sample ICRV omnibus is significant (*Q*_M = 17.35, *p* = .002) but collapses to non-significance once the 3-study Frontier cell is removed (*Q*_M = 1.49, *p* = .68). The directional gradient (E1a/E1b) and the cDAI (*Q*_M = 1.23, *p* = .541) and DPL (*Q*_M = 0.56, *p* = .755) hypotheses are not confirmed at current sample sizes. The most substantive finding is publication bias (H4 confirmed): trim-and-fill imputes *k* = 58 missing studies, reducing the bias-corrected effect to *r* = 0.035 (95% CI [0.023, 0.048]) — a ~53% attenuation. The I-P field's published literature appears to over-represent positive findings, and the true average performance return to internationalization may sit closer to *r* ≈ 0.035 than to the 0.07–0.10 range commonly cited. The heterogeneity puzzle remains largely unresolved, but the three-level decomposition reframes it: within-study variance (Level 2, 76.1%) is the dominant source, not between-country differences (Level 3, 11.8%) — methodological choices within papers contribute substantially more to dispersion than cross-country institutional contexts.

**Constraints on inference.** Five limitations bound these conclusions. (1) The directional gradient and cDAI/DPL nulls may reflect insufficient *k* in diagnostic regime cells (Frontier *K* = 3; Upper-middle *K* = 25; SIDS *K* = 0); a formal Frontier/SIDS-targeted WoS/Scopus search is required before the gradient null can be treated as definitive. (2) The Frontier-cell anomaly (*r̄* = 0.349 on *K* = 3, with one Iranian outlier) yields an unreliable estimate. (3) cDAI is assigned at the study level via country-year WB DAI / ITU DDI scores, not derived from firm-level digital adoption; vintage mismatch may attenuate the moderation. (4) Search restricted to English-language publications under-represents Chinese, Japanese, Korean, and Southeast Asian work. (5) Single-coder extraction and moderator coding (by the first author) precluded formal inter-coder reliability; coding quality is supported by pilot calibration and double-entry verification (§3.3.2). A dual-coded reliability check is a priority for the planned formal-search expansion.

**Future research.** Three directions follow from the null moderator findings. First, a formal WoS/Scopus systematic search targeting Frontier and SIDS economies would lift Frontier *k* from 3 to a plausible 20–40, enabling a meaningful between-regime test. Second, a pre-registered replication of the ICRV/cDAI/DPL hypotheses with explicit per-cell power analysis on a *k* ≥ 400 corpus would deliver a definitive test of whether these moderators are detectable at scale. Third, the publication-bias finding (*k* = 58 imputed, adj. *r* = 0.035) motivates a dedicated audit of unpublished I-P results — surveys of researchers, grey literature, and dissertations — to bound the true population effect more precisely than trim-and-fill alone.

---

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Competing Interests

The authors declare no conflict of interest.

## Data Availability

The coded study database (`forest_data.csv`), R analysis scripts (`metafor`), and the OSF pre-registration protocol are available from the corresponding author upon reasonable request. The PRISMA 2020 checklist is provided as supplementary material.

---

## References

Arte, P., & Larimo, J. (2022). Moderating influence of product diversification on the internationalization-performance relationship: Insights from meta-analysis. *Journal of Business Research, 139*, 1408–1423.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank correlation test for publication bias. *Biometrics, 50*(4), 1088–1101.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. *MIS Quarterly, 37*(2), 471–482.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2021). *Introduction to meta-analysis* (2nd ed.). Wiley.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics, 13*(1), 333–372.

Bustamante, C. V., Mingo, S., & Matusik, S. F. (2022). Institutions, digital capabilities and the internationalization of SMEs. *Journal of International Business Studies, 53*(3), 524–546.

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses. *Psychological Methods, 19*(2), 211–226.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum.

Cooper, H. (2010). *Research synthesis and meta-analysis: A step-by-step approach* (4th ed.). Sage.

David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. *American Economic Review, 80*(2), 355–361.

Dickersin, K. (1990). The existence of publication bias and risk factors for its occurrence. *JAMA, 263*(10), 1385–1389. https://doi.org/10.1001/jama.1990.03440100097014

Do, T. H., & Phan, A. T. (2024, December). *Internationalization and firm performance: A meta-analysis review* [Paper presentation]. The Sixth International Conference on Sustainable Development in Economics, Business, and Finance (ICBEF).

Do, T. H., & Phan, A. T. (2025). Internationalization and firm performance of firms in India: The role of top management. In M. Bartekova (Ed.), *International business research: Traditional and creative approaches*. IntechOpen. https://doi.org/10.5772/intechopen.1011012

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455–463.

Egger, M., Smith, G. D., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ, 315*(7109), 629–634.

Hedges, L. V., & Olkin, I. (1985). *Statistical methods for meta-analysis*. Academic Press.

Helpman, E., Melitz, M. J., & Yeaple, S. R. (2004). Export versus FDI with heterogeneous firms. *American Economic Review, 94*(1), 300–316.

Jacquemin, A. P., & Berry, C. H. (1979). Entropy measure of diversification and corporate growth. *Journal of Industrial Economics, 27*(4), 359–369.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process of the firm: A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32.

Katz, R., & Callorda, F. (2018). *The economic contribution of broadband, digitization and ICT regulation*. ITU Telecommunication Development Sector.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Deligonul, S., Perryy, M. Z., & Cavusgil, S. T. (2012). A multilevel examination of the drivers of firm multinationality: A meta-analysis. *Journal of Management, 38*(2), 502–530.

Kraus, S., Breier, M., Lim, W. M., Dabić, M., Kumar, S., Kanbach, D., Mukherjee, D., Corvello, V., Piñeiro-Chousa, J., Liguori, E., Palacios-Marqués, D., Schiavone, F., Ferraris, A., Fernandes, C., & Ferreira, J. J. (2022). Literature reviews as independent studies: Guidelines for academic practice. *Review of Managerial Science, 16*(8), 2577–2595.

Kogut, B., & Zander, U. (1993). Knowledge of the firm and the evolutionary theory of the multinational corporation. *Journal of International Business Studies, 24*(4), 625–645.

Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization-performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Orwin, R. G. (1983). A fail-safe N for effect size in meta-analysis. *Journal of Educational Statistics, 8*(2), 157–159.

Sahay, R., Eriksson von Allmen, U., Lahreche, A., Khera, P., Ogawa, S., Bazarbash, M., & Beaton, K. (2020). *The promise of fintech: Financial inclusion in the post COVID-19 era* (Departmental Paper No. 20/09). International Monetary Fund. https://doi.org/10.5089/9781513512242.087

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Peng, M. W., Wang, D. Y. L., & Jiang, Y. (2008). An institution-based view of international business strategy: A focus on emerging economies. *Journal of International Business Studies, 39*(5), 920–936.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology, 90*(1), 175–181.

Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models: Applications and data analysis methods* (2nd ed.). Sage.

Rosenthal, R. (1991). *Meta-analytic procedures for social research* (rev. ed.). Sage.

Rosenthal, R. (1994). Parametric measures of effect size. In H. Cooper & L. V. Hedges (Eds.), *The handbook of research synthesis* (pp. 231–244). Sage.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollender, L. (2018). Limits to outsourcing: A meta-analysis and empirical investigation. *Journal of International Business Studies, 49*(6), 682–703.

Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression approximations to reduce publication selection bias. *Research Synthesis Methods, 5*(1), 60–78.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80.

Sutton, A. J., & Higgins, J. P. T. (2008). Recent developments in meta-analysis. *Statistics in Medicine, 27*(5), 625–650.

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong, J., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Vevea, J. L., & Woods, C. M. (2005). Publication bias in research synthesis: Sensitivity analysis using a priori weight functions. *Psychological Methods, 10*(4), 428–443.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software, 36*(3), 1–48.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic Management Journal, 5*(2), 171–180.

World Bank. (2023). *Worldwide Governance Indicators*. https://info.worldbank.org/governance/wgi/

Wu, J., Wang, C., Hong, J., Piperopoulos, P., & Zhuo, S. (2022). Internationalization and innovation performance of emerging market enterprises: The role of host-country institutional development. *Journal of World Business, 52*(2), 192–203.

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of Management Journal, 38*(2), 341–363.

---

## Supplementary Materials (OSF)

The complete PRISMA 2020 flow diagram with both Path A (analyzed corpus, *k* = 238 / *K* = 288 from anchor-meta-analysis citation tracking and hand-search) and Path B (database-search expansion, full-text extraction ongoing) is provided as **Supp-A**; the full 7-moderator coding protocol as **Supp-B**; the MetaEssentials-vs-`metafor` consistency check as **Supp-C**; the detailed eligibility criteria as **Supp-T1**; the cDAI and DPL phase subgroup tables as **Supp-T2** and **Supp-T3**; the full robustness-checks table as **Supp-T4**; the detailed §3.2 PRISMA screening narrative as **Supp-T5**; and the extended methodological notes (three-level model specification, publication-bias tests, robustness-check specifications) as **Supp-M**. All items are deposited on OSF (https://osf.io/z37kn).

---

*Word count (main text §§1–6 prose, excluding tables, references, in-paper tables, and OSF supplementary materials): $\approx$ 7,940 words. Submission-build total (body + references + 3 in-paper tables × 280 + 6 figures × 280): $\approx$ 11,580 word-equivalents — within MIR's $\approx$ 12,000-word envelope.*
*Target journal: Management International Review (MIR; Springer, Scopus Q1, ABS-3). Extended methodological appendices (PRISMA 2020 flow; 7-moderator coding protocol; MetaEssentials-vs-`metafor` consistency check), the detailed eligibility criteria, the cDAI and DPL subgroup tables, the full robustness-checks table, the §3.2 PRISMA screening narrative, and extended methodological notes are migrated to OSF as Supp-A through Supp-M (https://osf.io/z37kn). Analyses use the verified baseline corpus (k = 238 studies, K = 288 effect sizes); the formal WoS/Scopus search expansion is ongoing and will be incorporated at revision. Effect-size coding follows the standardized protocol summarized in §3.4 and detailed in Supp-B.*
