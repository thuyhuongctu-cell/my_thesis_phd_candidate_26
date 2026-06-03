# Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis

*Author details removed for blind review*

*Manuscript prepared for: Asia Pacific Journal of Management (APJM; Springer Nature, Scopus Q1, ABS-3)*
*Version 1.5, June 2026 (target journal: APJM; v1.5 retargets from MIR to APJM per stronger geographic and theoretical fit; reframes the §2.2 capability-institution mechanism as an integrated synthesis of established literatures rather than a novel named theory)*

---

## Abstract

**Purpose.** First three-level meta-analytic regression analysis (MARA) of the internationalization–performance (I-P) relationship testing whether country-level digital adoption (cDAI), institutional context regime (ICRV), and Digital Paradox Lifecycle (DPL) phase moderate it.

**Design/methodology/approach.** PRISMA 2020 backward and forward citation tracking of five anchor meta-analyses with hand-search assembles *k* = 238 studies, *K* = 288 effect sizes from 49 economies. Three-level MARA via *metafor* under OSF pre-registration; six bias tests bound the corrected effect.

**Findings.** Pooled *r* =.074 (95% CI [.060,.088], *p* <.001; *I*² = 87.8%). Full-sample ICRV omnibus *Q*_M = 17.35 (*p* =.002) is not robust: drop-Frontier yields *Q*_M = 1.49 (*p* =.68); cDAI and DPL are non-significant. Six bias tests bound the bias-corrected effect: trim-and-fill imputes *k* = 58 and cuts *r* to.035; PET-PEESE yields *r* =.061; Vevea-Hedges selection model returns *r* =.077 with model-based selection evidence (LRT *p* =.002). True effect is best read as interval [.035,.077], not a point.

**Originality/value.** First three-level MARA and first pre-registered cDAI/ICRV/DPL meta-test in the I-P literature; first multi-method bounding of publication-bias attenuation in this 40-year base.

**Keywords:** internationalization–performance; meta-analysis; three-level model; digital adoption; institutional context; publication bias

**JEL classification:** F23 (multinational firms; international business); C83 (survey methods; sampling methods); O33 (technological change: choices and consequences); D22 (firm behaviour: empirical analysis); L25 (firm performance).

**Paper type:** Research paper (meta-analysis)

---

## 1. Introduction

The relationship between a firm's degree of internationalization and its performance, the "I-P relationship", is the most meta-analyzed question in international business. Over four decades and six major meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022), pooled positive effects are consistently small yet $I^2$ regularly exceeds 80%, signalling that context, not a universal mechanism, drives outcomes. Whether internationalization improves firm performance shapes investment decisions, export-promotion policy, and firm strategy in an interconnected global economy (Hitt et al., 2006; Lu & Beamish, 2004), yet the record remains inconclusive.

The present study's starting point is the ICBEF 2025 baseline (Author Citation, 2024, ICBEF): *k* = 113 studies, pooled *r* = 0.07 (*p* <.001), $I^2$ = 87.92%. That baseline confirmed the positive average effect but left approximately 70% of variance unexplained after the standard moderators (country of origin, industry, performance measure). Three theoretically grounded moderators, absent from all prior meta-analyses, motivate the present extension.

**Gap 1, cDAI.** Country-level digital adoption has been proposed as a contextual amplifier of firm-level competitive advantages (Stallkamp & Schotter, 2021; Verhoef et al., 2021), yet no meta-analysis has tested whether the national digital infrastructure environment moderates the I-P link.

**Gap 2, ICRV 6-regime.** Marano et al. (2016) established that home-country institutions moderate I-P, but applied a coarse six-group global classification. The global corpus spans the full institutional spectrum from Singapore (WGI Rule of Law +1.84) to Pakistan (−0.55) and Iran (−0.74; World Bank, 2023). A six-regime classification capable of resolving this heterogeneity has not been tested meta-analytically.

**Gap 3, DPL phase.** Brynjolfsson et al. (2021) identified 2009 as a productivity inflection in the digital era (the "dynamo analogy" for AI; David, 1990). Studies drawing on data from before, spanning, or after this threshold should yield systematically different I-P effects if digital platforms reshape internationalization economics; this temporal moderator has never been systematically coded.

This paper addresses all three gaps through a systematic search expanding the ICBEF 2025 baseline from *k* = 113 to *k* = 238 (49 economies; *K* = 288 effect sizes), combined with three-level MARA that decomposes heterogeneity beyond what conventional random-effects models allow.

**Contributions.** *Methodologically*: (1) the first three-level MARA of the I-P literature; (2) PRISMA-2020-compliant search with OSF pre-registration. *Theoretically*: (3) the first formal meta-analytic test of ICRV institutional regime, country-level digital adoption (cDAI), and Digital Paradox Lifecycle (DPL) phase as moderators of I-P, on a geographically diverse (though Advanced-economy-skewed) corpus of 49 economies. The non-confirmation of E1a/E1b, H2 and H3, the anomalous Frontier pattern, and the substantial publication-bias correction are themselves informative findings that bound the conditions under which these moderators could operate.

**Key findings.** Baseline *r* = 0.074 (*k* = 238, *K* = 288) replicates the ICBEF 2025 baseline. ICRV full-sample *Q*_M = 17.35 (*p* =.002) but drop-Frontier *Q*_M = 1.49 (*p* =.68); H1 fragile, E1a/E1b not confirmed. cDAI (*Q*_M = 1.23, *p* =.541) and DPL (*Q*_M = 0.56, *p* =.755) non-significant; H2/H3 not supported. The principal finding is publication bias (H4 confirmed): trim-and-fill imputes *k* = 58 missing studies and cuts the pooled effect from *r* = 0.074 to *r* = 0.035, a ~53% attenuation (Begg *p* <.001; Egger *p* =.057 borderline, this study frames the magnitude as a strong directional signal rather than a settled point estimate). Heterogeneity decomposition assigns the bulk of $I^2$ = 87.8% to within-study variance (Level 2, 76.1%) rather than between-country differences (Level 3, 11.8%).

**Organization.** Section 2 develops the theoretical framework and hypotheses; Section 3 describes the systematic search, coding, and three-level MARA specification; Section 4 presents results; Section 5 discusses theoretical and practical implications; Section 6 concludes.

---

## 2. Theoretical Framework and Hypotheses

### 2.1 Foundation Theories

Five established perspectives ground the three new moderating hypotheses. **Resource-Based View** (Barney, 1991; Wernerfelt, 1984) predicts that firms in resource-rich environments, including national digital infrastructure, capture higher returns to internationalization through resource bundling at the country level. cDAI here is the country-level construct distinct from the firm-level digital adoption (DAI) used in companion primary studies; at meta-analytic resolution only cDAI is extractable as a study-level moderator. **Institutional theory** (North, 1990; Scott, 1995) positions formal and informal institutions as the rules that govern transaction costs of cross-border expansion: higher institutional quality reduces opportunism, monitoring, and information asymmetry costs, and the ICRV gradient hypothesis (H1) derives directly from this logic, expected I-P effects decline as institutional quality falls from Advanced (Regime I) to Frontier (Regime V). **Organizational learning theory** (Johanson & Vahlne, 1977, 2009) frames internationalization as experiential knowledge accumulation; digital platforms, cloud analytics, real-time demand signals, B2B platforms, compress the learning curve once they reach diffusion maturity (Stallkamp & Schotter, 2021), the substantive basis for the DPL Follow-phase prediction (H2). **Coordination cost theory** (Hitt et al., 1997; Lu & Beamish, 2004) generates the modal inverted-U I-P pattern (Marano et al., 2016); mature national digital infrastructure attenuates the right-side decline by reducing communication, transaction, and information-asymmetry costs simultaneously. **Verhoef et al.'s (2021) digital transformation hierarchy** distinguishes Tier-1 digitization, Tier-2 digitalization, Tier-3 integration, and Tier-4 dynamic capability; at the country level the aggregate Tier-1/Tier-2 adoption defines cDAI as a coordination-enabling environment (Stallkamp & Schotter, 2021), the basis for H3.

### 2.2 An Integrated Capability–Institution Mechanism

This study synthesises three established literatures into an integrated mechanism that links the ICRV institutional gradient to heterogeneity in I-P effects. The core proposition is that productivity returns to international expansion depend on the degree to which home-country institutions enable firm capabilities to be deployed productively across borders, through three established channels. (i) *Rent protection*: in high-quality institutional environments (ICRV-I), strong IP protection and contract enforcement preserve proprietary rents across foreign markets, attenuating knowledge leakage and imitation risk (Kogut & Zander, 1993; Zaheer, 1995). (ii) *Liability-of-foreignness attenuation*: transparent regulation and low corruption shrink the information asymmetries and discriminatory treatment that generate LOF (Peng et al., 2008; Zaheer, 1995), letting firms capture a larger share of cross-border productivity gains. (iii) *Institutional-void amplification*: in weak environments, firms must invest in substitute governance (relationship capital, political connections, informal contracts) that absorb managerial attention and depress net returns (Khanna & Palepu, 2010); as institutional quality falls along the ICRV spectrum, these costs accumulate. Prior meta-analyses have not tested this gradient at the resolution required because they used coarse global classifications; the ICRV 6-regime taxonomy anchored to WGI Rule of Law (2023 vintage) and applied to the *k* = 238 global corpus is the first classifier capable of testing this institutional-gradient mechanism meta-analytically across economies from Singapore (WGI +1.84) to Pakistan (WGI −0.55) and Iran (WGI −0.74).

**Hypothesis 1 (H1, ICRV between-regime heterogeneity).** Pooled I-P effects vary systematically across ICRV regimes, with Advanced-regime studies showing the largest average effects (rent-protection + LOF-attenuation + void-cost reduction operating simultaneously). Formally: the between-regime *Q*_M for ICRV is significant (*p* <.05), and the ICRV-I point estimate exceeds those for Emerging (ICRV-III) and Mixed-regime (MX). The directional order among Frontier studies (ICRV-FR) is treated as exploratory pending adequate *k*.

*Exploratory Propositions:* **E1a**, ICRV-I shows the largest pooled effect (all three §2.2 mechanisms active simultaneously). **E1b**, Frontier-regime studies (ICRV-FR) show the smallest, possibly null/negative pooled effect (institutional-void costs dominate); E1b is exploratory because current FR *k* = 3 is below the *k* ≥ 10 threshold for stable random-effects moderation (Valentine et al., 2010).

### 2.3 Digital Paradox Lifecycle (DPL)

The Digital Paradox Lifecycle extends Brynjolfsson et al.'s (2021) productivity J-curve and David's (1990) dynamo analogy: general-purpose technologies require decades of complementary investment before productivity benefits materialize. Applied to I-P, three phases characterize the digital transformation of internationalization: **Precede** (data ≤ 2008): low digital penetration in cross-border trade; classical coordination cost mechanisms (Hitt et al., 1997; Lu & Beamish, 2004) dominate. **Span** (2009–2013): transitional period in which infrastructure builds but complementary organizational capabilities have not yet been absorbed; effects are heterogeneous and intermediate. **Follow** (≥ 2014): digital platforms, cloud logistics, B2B e-commerce, electronic payments, digital trade finance, have reached the maturity threshold at which coordination costs are systematically compressed; effects are expected largest.

The 2009 inflection point is anchored by three concurrent developments: (a) global smartphone/mobile-internet diffusion (2007–2009) that transformed cross-border communication costs; (b) rapid B2B e-commerce platform growth in China and Southeast Asia (Alibaba B2B International 2008–2010; Lazada 2011; Tokopedia 2009); (c) post-2009 financial crisis acceleration of SME digital adoption as cost-reduction strategy. These make 2009 a defensible global inflection rather than an arbitrary cut.

**Hypothesis 2 (H2, DPL phase).** Follow-phase studies show larger pooled I-P effects than Precede-phase studies (*r̄*[FOL] > *r̄*[PRE], with *r̄*[SPN] intermediate); the between-phase *Q*_M is expected significant (*p* <.05). The test is bounded by the J-curve logic: below ≈ 30 effects per phase, the between-group test is underpowered for moderate moderation (*f*² < 0.10).

### 2.4 cDAI as Amplifier

cDAI is an ecosystem property distinct from firm-level DAI: it captures the aggregate Tier-1/Tier-2 digital adoption density (broadband coverage, electronic payments, digital identity, regulatory support for digital commerce) that exists regardless of any individual firm's adoption decision, and it operates at the between-study level in a meta-analysis. Measurement uses the World Bank Digital Adoption Index (primary, 2016 vintage updated through ITU DDI 2017–2026) or ITU ICT Development Index (substitute), rescaled to 0–1 (Sahay et al., 2020); country-year assignment follows each study's dominant data period.

The mechanism is the *coordination platform effect* (Stallkamp & Schotter, 2021): mature national digital ecosystems lower the per-unit cost of cross-border transactions, with returns concentrated at higher internationalization intensities where digital tools substitute for the physical coordination investments otherwise required (Bharadwaj et al., 2013; Verhoef et al., 2021). The amplification is expected concentrated in the DPL Follow phase, because only post-2014 does national infrastructure function as an active coordination platform rather than a communication tool. Bustamante et al. (2022) provide the closest prior cross-country evidence at the firm level; the present study tests the meta-analytic extension.

**Hypothesis 3 (H3, cDAI amplification).** High-cDAI studies show larger pooled I-P effects than low-cDAI studies (*r̄*[High] > *r̄*[Low]; between-group *Q*_M significant, *p* <.05). cDAI is binned to three tiers (Low/Medium/High) classified from World Bank DAI and ITU DDI scores rather than fit as a continuous meta-regression coefficient, because current within-tier variance is insufficient for reliable continuous estimation. H3 is expected most consistently detectable in Follow-phase studies; in Precede-phase studies high cDAI is not expected to amplify I-P because B2B digital trade infrastructure had not yet reached critical mass regardless of country-level adoption.

### 2.5 Publication Bias as Null Hypothesis

Given the IB literature's history of selective reporting (Borenstein et al., 2021), this study tests publication bias as a formal hypothesis.

**Hypothesis 4 (H4, publication bias).** Selective reporting of statistically significant positive I-P results inflates the raw pooled effect relative to the true population effect (Borenstein et al., 2021; Dickersin, 1990). Three directional predictions: (H4a) Egger's and Begg's funnel-asymmetry tests are significant; (H4b) Duval and Tweedie's (2000) trim-and-fill imputes missing left-side studies and yields a bias-adjusted *r̄*_adj < *r̄*_raw but *r̄*_adj > 0; (H4c) Rosenthal's (1991) fail-safe *N* substantially exceeds 5*k* + 10 (here 1,200), confirming that the positive I-P effect is not an artifact of suppression alone.

### 2.6 Conceptual Model

![Figure 1: Conceptual model, Three-level MARA with ICRV, cDAI, and DPL moderators](figures/figure_1_conceptual_model.png)

*Figure 1.* Conceptual model for the three-level MARA. Solid arrows = primary I-P pooled effect (*k* = 238 studies / *K* = 288 effects / 49 economies; *r̄* = 0.074, 95% CI [0.060, 0.088]). Dashed arrows = hypothesized moderating relationships. Three study-level moderators: ICRV regime (H1; full-sample *Q*_M = 17.35, *p* =.002 but not robust to drop-Frontier sensitivity test *Q*_M = 1.49, *p* =.68); cDAI tier (H3; *Q*_M = 1.23, *p* =.541, n.s.); DPL phase (H2; *Q*_M = 0.56, *p* =.755, n.s.). The three-level model nests *K* = 288 effects within *k* = 238 studies; within-study $\sigma^2_{(2)}$ = 0.00874, $I^2_{(2)}$ = 76.1%; between-study $\sigma^2_{(3)}$ = 0.00135, $I^2_{(3)}$ = 11.8%; total $I^2$ = 87.8%. Publication bias (H4 confirmed): Egger's *b* = 0.475 (SE = 0.250, *p* =.057), Begg's $\tau$ = −0.134 (*p* =.0007); trim-and-fill imputes *k* = 58, adjusted *r* =.035; fail-safe *N* = 45,848. Abbreviations: ICRV = Innovation–Capability–Resource–Vulnerability; cDAI = country-level Digital Adoption Index; DPL = Digital Paradox Lifecycle; MARA = Meta-Analytic Regression Analysis.

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

**Deviations from pre-registration (PRISMA 2020, Item 24c).** Five operational refinements were made after registration and are disclosed here for transparency; none alters the registered hypotheses, the primary three-level model, or the analysis plan. First, the ICRV moderator was re-specified from the registered six-level ordinal scheme to the WGI Rule-of-Law-anchored coding reported in Section 2 (Codes I, II, III, FR, SIDS), and a multi-country category (MX) was added for pooled samples spanning two or more regimes with no single modal-country regime contributing at least 60% of the sample; the registered protocol had instead folded multi-country studies into the emerging-market code. Second, the DPL moderator was re-specified from the registered publication-year bins (pre-2000 / 2000–2009 / 2010–2026) to the data-period Precede/Span/Follow construct anchored on the 2009 digital-productivity inflection point (Section 2.3), which more directly operationalises the underlying J-curve logic. Third, publication-bias diagnostics, planned in the registration as a robustness analysis, are reported as a labelled hypothesis (H4) because the magnitude of the trim-and-fill adjustment became a primary finding. Fourth, the registered inter-coder reliability protocol (Section 8.3 of the registration: a 20% double-coded subsample with Cohen's $\kappa \geq 0.70$ and ICC $\geq 0.80$) was not executed as registered: a second independent coder was not available, so extraction and moderator coding were performed by a single coder (the first author). Consequently, no inter-coder reliability statistics are reported; coding quality was instead supported by pilot calibration and double-entry verification (Section 3.3.2), and a dual-coded reliability check is a stated priority for the planned formal-search expansion. Fifth, the drop-Frontier sensitivity analysis on ICRV (reported in Section 4.3) and the construct-validity restriction of cDAI moderation to the Span+Follow subsample (reported in Section 4.4) were added in response to data features identified during analysis; the analysis reports both alongside the pre-registered full-sample tests for transparency, with the post-hoc tests interpreted as confirmatory diagnostics rather than primary findings. The extraction codebook accompanying the data (v1.1) documents the coding actually applied; the registered v1.0 scheme remains in the frozen OSF record.

### 3.2 Eligibility Criteria and Study Selection

Two independent screeners applied the eligibility criteria below in two stages (title/abstract, then full-text), with third-reviewer adjudication on disagreements. Inclusion required: private-sector firm samples with measured internationalization (FSTS, entropy, count-of-markets, transnationality index, or FDI-to-investment ratio) and quantitative financial performance (accounting, market, or productivity-based); convertible effect-size statistics (Pearson *r*, regression β, *t*-statistic with *df*, or *F*-statistic with *df*₁ = 1); English or Vietnamese language; and peer-reviewed journal articles or articles in press with DOI. Excluded: state-owned enterprises (government equity > 50%), financial-sector firms (SIC 6000–6999), wholly domestic firms, qualitative case studies, simulations, narrative/ordinal performance measures, and grey literature (dissertations, theses, working papers, conference papers, book chapters, reports). ICRV regime is assigned globally using World Bank WGI Rule of Law (2023 vintage); an Asia-Pacific subsample is available as a sensitivity analysis. The full criteria matrix is provided as **Supp-T1**.

**PRISMA 2020 flow summary (two-path design; Figure 7).** The corpus analysed in this article is *k* = 238 / *K* = 288 from **Path A**, assembled from backward and forward citation tracking of five anchor meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Arte & Larimo, 2022) plus hand-search (≈ 497 records), screened against the eligibility criteria above and double-entry verified. Path A is the *definitive corpus* for the analyses reported here: the eligibility criteria, extraction protocol, and pre-registered hypotheses all apply to it as a self-contained sample, and the substantive conclusions of the article (including the publication-bias paradox documented in Section 5.2) stand on Path A alone. **Path B** is a *prospective extension* via systematic WoS + Scopus search (20 May 2026): 3,263 records; 795 duplicates removed; 1,397 L1 excluded; 782 L2 screened over 8 rounds, yielding 785 Y / 1,694 N / 3 UNSURE; 741 of 785 Y carry DOIs, 547 await full-text extraction. This study discloses Path B to document the planned future replication of the present article's results on a corpus of *k* ≈ 600–700, not as a condition on the validity of the current findings. Full flow (Figure 7), screening trace, and pipeline status are in **Supp-A**, **Supp-T5**, and `prisma_extraction_pipeline_status.md` on OSF.

![Figure 7. PRISMA 2020 two-path flow diagram. Path A (left, blue): the analyzed corpus *k* = 238 / *K* = 288, complete. Path B (right, orange-amber): formal WoS + Scopus expansion, 547 records pending full-text extraction. The final analyzed corpus pools to Path A only at the current build.](figures/figure_prisma_2020_flow.png)

### 3.3 Data Extraction and Quality Assurance

#### 3.3.1 Effect-Size Extraction Protocol

Statistical parameters were extracted manually from the full text of each eligible study by the primary coder (PI; identity withheld for blind review), using the standardized coding form specified in Appendix B. For each study, the following parameters were recorded: sample size (*N*), the focal I-P effect size (Pearson's *r* or the convertible statistic), study data-year range, country or region, DOI operationalization, performance operationalization, and any study-specific features relevant to moderator coding.

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

The three-level model (Van den Noortgate et al., 2013; Cheung, 2014) decomposes the observed effect size *r*_ij (effect *i* from study *j*) into three variance components: Level 1 known sampling variance *v*_ij = 1/(*N*_ij − 3); Level 2 within-study heterogeneity $\sigma^2_{(2)}$ capturing effect-to-effect variation within papers; and Level 3 between-study heterogeneity $\sigma^2_{(3)}$ on which the moderator regression is specified, $\delta_j = \mu + \mathbf{X}_j \boldsymbol{\beta} + w_j$. The moderator matrix $\mathbf{X}_j$ includes ICRV regime dummies (Regime V reference), continuous cDAI, DPL phase dummies (Precede reference), plus four standard controls. Parameters are estimated by REML using `rma.mv` in `metafor` v4 (Viechtbauer, 2010) with compound-symmetric within-study covariance; all *r* are Fisher-*z* transformed before fitting and back-transformed for reporting. Heterogeneity is decomposed using the Higgins–Thompson typical-variance formulation for multilevel models (Cheung, 2014, eq. 15). Moderator significance is assessed via the omnibus *Q*_M on *p* − 1 df (Holm–Bonferroni pairwise correction) for categorical moderators and Wald *z* for continuous cDAI. To guard against potential misspecification of the within-study dependence structure, all moderator-test *p*-values and confidence intervals are additionally reported with cluster-robust standard errors via the CR2 small-sample correction of Tipton (2015), implemented in the `clubSandwich` package (Pustejovsky & Tipton, 2022) and clustered at the study level; this Robust Variance Estimation (RVE; Hedges, Tipton, & Johnson, 2010) is asymptotically equivalent to the three-level model under a large between-study sample (*k* = 238 here) and is reported as a sensitivity rather than as the primary inference (see Section 3.7). Full model equations and estimator rationale are provided as **Supp-M**.

### 3.6 Publication Bias Assessment

Six complementary tests follow Borenstein et al. (2021, ch. 30) and Vevea and Woods (2005): (i) **Egger's weighted regression** (intercept tests funnel-plot asymmetry); (ii) **Begg and Mazumdar's rank correlation** (non-parametric, less outlier-sensitive); (iii) **trim-and-fill** (Duval & Tweedie, 2000; imputes missing left-side studies, re-estimates pooled effect); (iv) **Orwin's fail-safe *N*** (1983; number of null-effect studies required to push pooled *r* below *r* = 0.10; benchmark 5*k* + 10 per Rosenthal, 1991); (v) **PET-PEESE** (Stanley & Doucouliagos, 2014), a precision-effect meta-regression that estimates the bias-corrected pooled effect as the intercept of a regression of effect sizes on their standard errors (PET) or sampling variances (PEESE; used when PET indicates a non-zero true effect); and (vi) **Vevea-Hedges three-parameter step-function selection model** (Vevea & Hedges, 1995; Hedges & Vevea, 1996), a *model-based* bias correction that estimates the publication-selection function directly via maximum likelihood (one-tailed *p*-value cutpoints at.025 and.500) and reports a selection-adjusted pooled effect plus a likelihood-ratio test against the no-selection null. Each test has a distinct failure mode: trim-and-fill is known to over-correct under high heterogeneity (Terrin et al., 2003), PET-PEESE estimates can be biased toward null when *I*² > 80% (Stanley & Doucouliagos, 2014), and Vevea-Hedges can fail to converge in sparse-cell selection regions. Reporting all six tests together provides a direction-of-effect signal that is robust to any single test's specification assumptions; the analysis interprets each adjusted estimate as an inferential bound rather than as a point estimate of the true population effect. Test specifications and the metafor `selmodel` implementation are in **Supp-M**.

### 3.7 Robustness Checks

Six pre-registered checks evaluate sensitivity to modelling choices: (1) two-level vs. three-level estimator comparison; (2) leave-one-out influence diagnostics (Cook's distance > 4/*k*); (3) FSTS-only DOI restriction; (4) WGI composite governance index substituted for Rule of Law as the ICRV classifier (same percentile thresholds); (5) post-2000 temporal restriction (*k* ≈ 180) to test vintage confounding of DPL phase; and (6) cluster-robust standard errors via Robust Variance Estimation (RVE; Hedges, Tipton, & Johnson, 2010) with the CR2 small-sample correction (Tipton, 2015), clustered at the study level using `clubSandwich` (Pustejovsky & Tipton, 2022), reported as a check on the parametric within-study dependence assumption of the primary three-level model. Detailed specifications are provided in **Supp-M**.

---

## 4. Results

### 4.1 Sample Description

*k* = 238 studies (coded), *K* = 288 effect sizes (working database, pre-formal-search). Coding quality and verification are described in Section 3.3.2; because extraction was single-coder, no inter-coder reliability statistics are reported.

**Table 4.1, Working-database sample composition** *(pre-formal-search; *K* = 288 effect sizes, k = 238 coded studies)*

| Category | *K* effects | *k* studies |
|----------|------|------|
| ICRV Regime I, Advanced (e.g., Korea, Japan, Singapore, HK, Australia) | 139 | 107 |
| ICRV Regime II, Upper-middle (e.g., China, Malaysia, Thailand) | 25 | 21 |
| ICRV Regime III, Emerging (e.g., Vietnam, India, Philippines) | 91 | 79 |
| ICRV Frontier / SIDS (FR) | 3 | 3 |
| Cross-regime / multi-country (MX) | 30 | 28 |
| ***K* / *k* total** | **288** | **238** |
| cDAI High (H) | 38 |, |
| cDAI Medium (M) | 76 |, |
| cDAI Low (L) | 174 |, |
| DPL Precede (PRE, median data year ≤2008) | 100 |, |
| DPL Span (SPN, median 2009–2013) | 108 |, |
| DPL Follow (FOL, median ≥2014) | 80 |, |
| By DOI type: FSTS | 138 |, |
| By DOI type: GEO | 50 |, |
| By DOI type: EXP | 65 |, |
| By DOI type: COMP | 31 |, |
| By DOI type: FDI | 3 |, |
| By DOI type: OTH | 1 |, |
| By FP type: ACC (accounting) | 247 |, |
| By FP type: MKT (market-based) | 15 |, |
| By FP type: LAB (labour productivity) | 12 |, |
| By FP type: MIX | 14 |, |

*Note:* Counts from working database (`p6/results/forest_data.csv`, K=288 rows, k=238 unique study IDs, updated 23/05/2026). ICRV *k* and *K* counts sum to > total because MX studies may span multiple regimes. cDAI and DPL counts are pre-formal-search; final values are pending formal WoS/Scopus search and complete coding. Study (*k*) counts by cDAI/DPL are reported after multi-effect deduplication.

**Temporal distribution of the corpus.** The sample is right-skewed toward post-2000 publications, reflecting the field's growth trajectory (Figure 6). The 1978–1989 period contributes only 6 studies (2.6%; density 0.5/year); 1990–1999 contributes 18 studies (7.7%; 1.8/year); 2000–2009 contributes 54 studies (23.2%; 5.4/year); 2010–2019 contributes 92 studies (39.5%; 9.2/year); 2020–2022 contributes 46 studies (19.7%; 15.3/year); and 2023–2026 contributes 17 studies (7.3%). The 2010–2022 window dominates with 138 studies (59% of the corpus). Implication: the main-effect MARA and $I^2$ estimates remain valid because they pool across the full corpus, but any sub-period analysis before 1990 is underpowered, and time-trend moderation interpretations should be confined to the 2000–2022 window where annual density supports stable subgroup estimates.

![Figure 6. Distribution of primary studies by publication year (k = 238). The corpus is right-skewed toward post-2000 publications, with the 2010–2022 window accounting for 59% of the studies. Sparse pre-1990 density precludes a separate early-period subgroup; DPL phase boundaries (2009, 2014) are anchored to digital-coordination diffusion landmarks rather than to within-corpus density.](figures/figure6_year_distribution.png)

### 4.2 Baseline Three-Level Model

**ICBEF 2025 single-level baseline (MetaEssentials 1.5, k = 113):**

$$\bar{r}_{ICBEF} = 0.07 \quad (95\%\ \text{CI}: [0.05, 0.09]),\ p <.001$$
$$I^2_{ICBEF} = 87.92\%,\quad Q_{between} = 1{,}247.3\ (df = 112,\ p <.001)$$

**Three-level decomposition** (three-level REML, k = 238 studies, K = 288 effects):

| Parameter | Estimate |
|-----------|---------|
| σ²_(2) within-study | 0.00874 |
| σ²_(3) between-study | 0.00135 |
| *I*²_(2) within-study | 76.1% |
| *I*²_(3) between-study | 11.8% |
| *I*²_total | 87.8% |
| Pooled *r̂*_3L | 0.074 (95% CI [0.060, 0.088]) |
| *Q*_total | 1,909.42 (*df* = 287, *p* <.001) |

The three-level pooled estimate (*r̂* = 0.074) is consistent with the ICBEF 2025 single-level baseline (*r* = 0.07), confirming no systematic upward bias from ignoring multilevel nesting in the earlier analysis. The decomposition is dominated by the within-study level: effect-to-effect variation within the same study (Level 2, $I^2_{(2)}$ = 76.1%) is roughly six times the between-study contribution (Level 3, $I^2_{(3)}$ = 11.8%). Most unexplained heterogeneity therefore arises from analytic choices *within* primary studies, DOI operationalization, performance metric, specification, sub-sample, rather than from stable cross-country contextual differences. Total $I^2$ = 87.8%, well above the sampling-error floor, motivates the moderator analyses; however, as Sections 4.3–4.5 show, the coded country/time moderators leave the bulk of this within-study heterogeneity unresolved.

### 4.3 ICRV Regime Moderation (H1)

**H1 is not robustly supported.** The pre-registered between-regime test on the four well-populated core regimes (I/II/III/MX, *K* = 285) yields *Q*_M = 1.49 (*df* = 3, *p* =.68), statistically indistinguishable from the null cDAI and DPL moderators reported below. The full-sample omnibus including the three-effect Frontier cell does reach significance (*Q*_M = 17.35, *df* = 4, *p* =.002), but as the subgroup table makes clear this result is generated almost entirely by the Frontier cell rather than by a monotone institutional gradient. The directional Exploratory Propositions E1a (Advanced largest) and E1b (Frontier smallest) are **not** supported.

**Table 4.2, ICRV regime subgroup results** *(actual MARA output, k = 238 / K = 288; subgroup pooled means, no-intercept specification)*

| Regime | *K* (effects) | *r̄* | 95% CI | *p* |
|--------|--------------|------|--------|-----|
| I, Advanced-Innovation (SG, HK, KR, JP, AU...) | 139 | 0.079 | [0.059, 0.099] | <.001 |
| II, Upper-middle (CN, MY, TH, BR...) | 25 | 0.065 | [0.020, 0.109] |.004 |
| III, Emerging (VN, IN, ID, PH...) | 91 | 0.069 | [0.045, 0.093] | <.001 |
| FR, Frontier / LDC | 3 | 0.349 | [0.218, 0.468] | <.001 |
| MX, Cross-regime / multi-country | 30 | 0.053 | [0.012, 0.094] |.012 |

![Figure 2: ICRV regime forest plot, subgroup pooled effects with 95% CI](figures/figure2_icrv_forest.png)

*Figure 2.* ICRV subgroup forest plot. Pooled *r̄* and 95% CI per coded institutional regime.

All five regime means are positive and significant. Among the three well-populated single-country regimes the effects are tightly clustered and statistically indistinguishable, Advanced-Innovation (*r̄* = 0.079, *K* = 139), Emerging (*r̄* = 0.069, *K* = 91), and Upper-middle (*r̄* = 0.065, *K* = 25), providing **no** support for E1a's predicted advanced-over-emerging ordering. Cross-regime/multi-country pooled studies sit lowest (MX, *r̄* = 0.053, *K* = 30), consistent with attenuation when heterogeneous national samples are aggregated within a single primary study. The omnibus significance is attributable almost entirely to the Frontier/LDC cell (FR, *r̄* = 0.349), the only regime whose confidence interval does not overlap the pooled estimate; this cell rests on just *K* = 3 effects, including one outlier (Pouresmaeili et al., 2018, *r* = 0.69, *n* = 226 Iranian manufacturing firms), and is therefore statistically fragile and contrary to E1b's predicted Frontier floor. A drop-FR sensitivity test confirms this directly: re-estimating the omnibus on the four well-populated core regimes (I/II/III/MX, *K* = 285) reduces the between-regime moderation to *Q*_M = 1.49 (*df* = 3, *p* =.68), i.e., non-significant and on a par with the null cDAI (*Q*_M = 1.23) and DPL (*Q*_M = 0.56) tests. The full-sample significance is thus a small-sample Frontier artifact rather than evidence of an institutional-quality gradient; the gradient-specific propositions require substantially larger *K* per regime cell before they can be properly adjudicated. The sixth ICRV code, Pacific SIDS (the dissertation's Regime VI), returns zero qualifying primary studies in this corpus and therefore does not enter the subgroup model, leaving five populated cells (hence *df* = 4). (Numbering crosswalk: P6 Code II ≡ dissertation Regime III, P6 Code III ≡ Regime IV, FR ≡ Regime V, SIDS ≡ Regime VI; see Section 2 moderator coding.)

### 4.4 cDAI Moderation (H3)

*Q*_M(cDAI) = 1.23 (*df* = 2, *p* =.541). **H3 not supported.**

A construct-validity caveat applies to the full-sample test. cDAI scores are sourced from the World Bank Digital Adoption Index (2016 vintage) and the ITU Digital Development Index (2017–2026); for Precede-phase studies (median data year ≤ 2008; *K* = 100) cDAI is back-projected through a period in which the digital-adoption construct did not yet validly describe national economies. The Span+Follow subsample (*K* ≈ 188, median data year ≥ 2009) is the construct-valid test window. A subsample restriction yields no qualitative change to the H3 inference, but the restricted test remains the conceptually preferred specification and is reported as a sensitivity check (**Supp-T2**). This study retains the full-sample result as the headline only because the pre-registration specified it.

Subgroup means are non-monotone (*r̄*[Low] = 0.075, *K* = 174; *r̄*[Medium] = 0.065, *K* = 76; *r̄*[High] = 0.091, *K* = 38; full table in **Supp-T2**). All three subgroup means are individually significant (*p* <.001) but pairwise contrasts are small and non-significant (*b*[Medium−Low] = −0.010, *p* =.489; *b*[High−Low] = +0.016, *p* =.469). The non-monotone ordering (Low > Medium < High) and the omnibus null fail to support the predicted positive linear gradient. The cDAI × DPL interaction cannot be reliably estimated given the non-significant main effect; a larger sample with finer cDAI resolution is required to test the gradient hypothesis. H3 is not supported: country-level digital adoption does not significantly amplify the pooled I-P effect in this *k* = 238 sample.

### 4.5 DPL Phase Moderation (H2)

*Q*_M(DPL) = 0.56 (*df* = 2, *p* =.755). **H2 not supported.**

Subgroup means: PRE (median data year ≤ 2008) *r̄* = 0.082 (*K* = 100); SPN (2009–2013) *r̄* = 0.069 (*K* = 108); FOL (≥ 2014) *r̄* = 0.073 (*K* = 80); full table in **Supp-T3**. Pairwise *z*-tests are all far from significance (PRE-FOL *z* = 0.46, *p* =.645; PRE-SPN *z* = 0.78, *p* =.434; FOL-SPN *z* = 0.28, *p* =.782). The empirical ordering (PRE > FOL > SPN) is opposite to H2's predicted FOL > SPN > PRE, but between-group differences are too small to overinterpret. The null result may reflect insufficient power to detect small temporal trends at *k* = 238, confounding between DPL phase and ICRV composition (pre-2009 studies concentrated in advanced economies), or the absence of a DPL inflection at meta-analytic resolution with the current sample. H2 is not supported.

![Figure 3: DPL phase moderation, pooled I-P effect by digital adoption epoch](figures/figure3_dpl_phase.png)

*Figure 3.* DPL phase subgroup pooled effects with 95% CI. Between-phase differences are small and non-significant.

### 4.6 Publication Bias (H4)

H4 **supported**: multiple indicators consistently detect publication bias, though the positive I-P effect survives correction.

**Egger's regression test** (precision-weighted): *b* = 0.475 (*SE* = 0.250, *p* =.057), marginal and not significant at $\alpha$ =.05; the regression-based asymmetry signal is suggestive but inconclusive.

**Begg's rank correlation** (Kendall's $\tau$): $\tau$ = −0.134, *p* =.0007, significant funnel asymmetry; studies with larger standard errors (smaller *n*) report systematically lower effect sizes, consistent with publication bias against null or negative findings.

**Trim-and-fill**: imputes *k* = 58 missing studies (left side); adjusted pooled *r̄* = 0.035 (95% CI [0.023, 0.048]), a conservative lower bound. The effect remains positive and significant but is substantially attenuated from the raw estimate (0.074 to 0.035).

**Fail-safe *N*** (Rosenthal, 1991): *N* = 45,848, far exceeding the criterion of 5*k* + 10 = 1,200; even under extreme publication suppression assumptions, a trivially small effect would require 45,848 unpublished null studies, implausible.

**PET-PEESE** (Stanley & Doucouliagos, 2014; precision-effect meta-regression on the study-aggregated dataset, k = 238): PET intercept (z-scale) *b* = 0.041 (95% CI [0.009, 0.073], *p* =.012); because PET indicates a non-zero true effect, the PEESE intercept is reported as the bias-corrected estimate, *b* = 0.061 (CI [0.042, 0.080]), back-transforming to *r* = 0.061 (CI [0.042, 0.080]). PET-PEESE thus indicates a milder attenuation than trim-and-fill (raw *r* = 0.074; PET-PEESE *r* = 0.061; ~18% attenuation), consistent with the Stanley–Doucouliagos (2014) note that PET-PEESE estimates can be biased toward null when *I*² > 80%; the present *I*² = 87.8% places this estimate at the upper end of the bias-corrected range rather than at its centre.

**Vevea-Hedges three-parameter step-function selection model** (Vevea & Hedges, 1995; Hedges & Vevea, 1996; one-tailed cutpoints at.025 and.500): the model converges and the likelihood-ratio test against the no-selection null is significant ($\chi^2$ = 12.29, *df* = 2, *p* =.002), confirming model-based evidence of publication selection. The estimated selection weights are *w*[(0,.025]] = 1.000 (reference: one-tailed significant positives) and *w*[(.025,.500]] = 1.000 and *w*[(.500, 1.0]] = 1.736; the elevated weight on the upper p-value range reflects that one-tailed significant *negative* results are 1.74 times more represented in the corpus than significant positives, after adjustment. The selection-adjusted pooled effect is *r* = 0.077 (CI [0.042, 0.111]), nearly identical to the unadjusted estimate, indicating that while selection is detectable, the magnitude of the bias on the central tendency is modest under the step-function specification.

Read together, the six tests bound the publication-bias attenuation: PET-PEESE places the conservative lower bound near *r* = 0.061; the Vevea-Hedges model-based selection-adjusted estimate sits at *r* = 0.077 (with significant evidence of selection); trim-and-fill is the most aggressive correction at *r* = 0.035. The fact that the model-based correction (Vevea-Hedges) detects significant selection but estimates a smaller magnitude adjustment than the non-parametric correction (trim-and-fill) is consistent with the Terrin et al. (2003) and Stanley–Doucouliagos (2014) cautions that trim-and-fill over-corrects under high heterogeneity. The substantive interpretation is therefore that publication selection is real (Begg *p* <.001; Vevea-Hedges LRT *p* =.002) and that the true population effect lies in the interval bounded by these estimates, *r* between approximately 0.035 and 0.077, with the magnitude of the inflation depending on which selection-process assumption one adopts. The headline reading of a substantially upward-biased published average effect survives across all six tests; only the precise magnitude of the bias correction is method-dependent.

![Figure 4: Funnel plot with trim-and-fill imputed studies](figures/figure4_funnel_plot.png)

*Figure 4.* Funnel plot of effect sizes against standard errors. Open circles = original studies; filled circles = trim-and-fill imputed studies (*k* = 58). Substantial left-side asymmetry is visible; the adjusted pooled effect is *r* = 0.035.

### 4.7 Robustness

The baseline *r* = 0.074 is robust across all sensitivity checks: confirmed-*r*-only (*K* = 241, *r̄* = 0.077); exclude *n* < 30 (*K* = 286, *r̄* = 0.074); ACC-performance only (*K* = 247, *r̄* = 0.075); FSTS-only DOI (*K* = 138, *r̄* = 0.061, most conservative, but positive and significant); DL two-level estimator (Δ*r* < 0.01 vs. three-level); leave-one-out range [0.071, 0.075] (0/288 changing direction); ICRV drop-Frontier omnibus *Q*_M = 1.49 (*df* = 3, *p* =.68) versus full-sample *Q*_M = 17.35 carried by FR (*K* = 3). The DL two-level estimator and three-level point estimates coincide, confirming that three-level nesting adds precision without biasing the pooled effect. The FSTS-only attenuation suggests broader DOI heterogeneity partially inflates the pooled effect. Full robustness table in **Supp-T4**.

![Figure 5: Leave-one-out sensitivity, pooled *r̄* range across leave-one-out iterations](figures/figure4_sensitivity.png)

*Figure 5.* Leave-one-out sensitivity. The narrow range across *K* = 288 iterations confirms no single study drives the result.

---

## 5. Discussion

### 5.1 Alignment with Country-Level Evidence

The meta-analytic baseline (*r* = 0.074, *k* = 238, 49 economies) is consistent with country-level evidence from across the global study corpus, including the Asia-Pacific primary studies underlying the ICBEF 2025 baseline (Author Citation, 2024, ICBEF). The pooled effect is positive and significant, confirming that export-intensive firms tend to outperform domestically focused peers even after adjusting for firm size, age, and industry.

**Advanced-Innovation contexts (Regime I, *K* = 139; *r̄* = 0.079, 95% CI [0.059, 0.099]):** The Advanced-Innovation group mean (*r̄* = 0.079) is the best-populated single-country cell and is directionally consistent with institutional complementarity theory: strong contract enforcement, IP protection, and low liability of foreignness (Zaheer, 1995) allow firms to sustain productive internationalization without the coordination cost penalties visible in weaker environments (North, 1990; Peng et al., 2008). It sits marginally above the pooled baseline (*r* = 0.074) but its confidence interval comfortably overlaps the other well-populated regimes.

**Emerging contexts (Regime III, *K* = 91; *r̄* = 0.069, 95% CI [0.045, 0.093]):** The Emerging cell is well-populated and yields a reliable positive estimate (*r̄* = 0.069) statistically indistinguishable from the Advanced-Innovation mean, directly contrary to E1a's predicted advanced-over-emerging ordering. A companion primary-study analysis by the present author group (Author Citation, 2025, IntechOpen) on 380 Indian WBES firms documents a negative aggregate DOI coefficient with manager experience and female top-management leadership as positive moderating factors, a pattern consistent with the firm-level-compensating-resources interpretation discussed in Section 5.2; this study notes this overlap to flag, rather than conceal, the link to the authors' wider primary-study programme.

**Frontier contexts (Regime FR, *K* = 3; *r̄* = 0.349, 95% CI [0.218, 0.468]):** The *K* = 3 Frontier estimate is anomalously high and includes one outlier study (Pouresmaeili et al., 2018, *r* = 0.69, *n* = 226 Iranian manufacturing firms). This cell is the single largest contributor to the significant omnibus *Q*_M, yet on only three effects it cannot be interpreted as a reliable Frontier I-P effect, and its high (not low) point estimate is directly contrary to E1b's predicted Frontier floor. The actual Frontier I-P effect could be zero, positive, or negative, substantially larger *K* is required.

**Synthesis:** H1 receives only fragile support. The full-sample ICRV between-regime Q_M test is significant (*Q*_M = 17.35, *p* =.002), but a drop-FR sensitivity test shows this is carried entirely by the 3-study Frontier cell: on the four well-populated core regimes the omnibus falls to *Q*_M = 1.49 (*p* =.68), non-significant. Robust between-regime moderation is therefore absent at current sample sizes, and the directional gradient propositions E1a and E1b are not meta-analytically confirmed. The substantiated finding is that the baseline I-P effect (*r* = 0.074) is broadly consistent across well-populated regime groups (I, II, III, MX), and the magnitude of the Advanced-Emerging gap (*r̄* = 0.079 vs. 0.069) does not reach significance, a result that bounds, rather than refutes, the institutional-gradient prediction developed in §2.2.

### 5.2 Theoretical Contributions

**Contribution 1: A three-level decomposition of I-P heterogeneity.** Extending the ICBEF 2025 Asia-Pacific baseline (*k* = 113) to *k* = 238 studies from 49 economies (*K* = 288 effects), the three-level MARA correctly partitions within-study and between-study variance and shows that within-study design heterogeneity (Level-2 *I*² = 76.1%) accounts for roughly six times the between-country share (Level-3 *I*² = 11.8%). The baseline *r* = 0.074 replicates prior estimates and is robust across seven sensitivity checks. Marano et al.'s (2016) earlier institutional-moderator finding remains the canonical reference; the present analysis does not overturn it but adds the three-level decomposition and the formal moderator tests below.

**Contribution 2: Pre-registered moderator tests of ICRV, cDAI, and DPL.** This is the first formal test of these three moderators in a three-level MARA. All three return null or fragile results: ICRV core-regime *Q*_M = 1.49 (*p* =.68); cDAI *Q*_M = 1.23 (*p* =.541); DPL *Q*_M = 0.56 (*p* =.755). These nulls set theoretically informative bounds rather than confirming substantive moderation: the *k* = 238 sample lacks adequate between-regime variation in diagnostic cells (Frontier *K* = 3; Upper-middle *K* = 25; SIDS *K* = 0). A *Capability–Context Mismatch* interpretation, that macro digital context is inert without firm-level digital capability to translate it, is consistent with the cDAI null, but is offered as a post-hoc proposition for confirmatory replication rather than as a finding of this study.

**Contribution 3: Quantification of publication-bias attenuation.** Trim-and-fill imputes *k* = 58 missing left-side studies and yields *r* = 0.035 [.023,.048], a ~53% attenuation from the raw *r* = 0.074; Begg's $\tau$ is significant (*p* <.001) and Egger's *p* =.057 is borderline. Because trim-and-fill is known to over-correct under high heterogeneity (*I*² = 87.8% here), the analysis interprets the 53% figure as an upper-bound estimate of selection-driven inflation rather than a point estimate.

**A field-level paradox the paper does not resolve.** The bias-corrected estimate (*r* ≈.035, below Cohen's small-effect floor of.10) raises a foundational question for the moderator project this paper undertakes: if four decades of accumulated I-P evidence are materially inflated by publication selection, then both the canonical inverted-U/positive-I-P findings the theory section invokes (Lu & Beamish, 2004; Hitt et al., 1997; Marano et al., 2016) and the minimum effect size against which moderator power should be calibrated rest on shakier empirical ground than the literature acknowledges. Two implications follow that this paper can only surface, not resolve. First, between-study moderator detection in this literature requires power calibrated to *r* ≈.035 rather than *r* ≈.07–.10, which substantially raises the *k* threshold for adequately powered moderator tests beyond current corpora. Second, future I-P meta-analyses should report bias-corrected pooled estimates as the primary inference and treat raw estimates as descriptive only. This paper intends to register the paradox; resolving it is a research-programme commitment beyond a single article.

### 5.3 Managerial and Policy Implications

Three implications follow within the constraints set by Section 5.2's paradox. Because the bias-corrected effect (*r* ≈.035) sits below Cohen's small-effect floor and the moderators in this analysis do not robustly select environments where the effect is larger, these implications are bounded rather than prescriptive. **For managers:** internationalization should be evaluated on firm-specific strategic logic (resource-leveraging, capability-building, market-portfolio diversification) rather than on the assumption that exporting raises productivity on average, the average return is materially smaller than the published literature suggests. **For policy makers:** the non-significant ICRV Advanced–Emerging gap (*r̄* = 0.079 vs. 0.069) does not warrant treating institutional quality as the primary lever for export-led productivity; export-promotion designs should weight firm-level capability programmes (technological and managerial) alongside institutional reform. **For the IB research community:** pre-registration and bias-corrected pooled reporting should become standard in future I-P meta-analyses.

### 5.4 Limitations and Inferential Bounds

Three limitations bound the inferences available from this study:

**(a) What cannot be concluded:** (1) The SIDS subgroup (*k* $\approx$ 5, wide CI) does not permit definitive conclusions about the "forced-penalty" hypothesis, a targeted search for SIDS-focused primary studies (as specified in Appendix B) is required before meta-analytic SIDS effects are precise. (2) The c$\text{DAI} \times \text{ICRV}$ joint moderation (three-way interaction) is underpowered in the current dataset (*k* per cell < 20); point estimates are provided but confidence intervals are wide. (3) All effect sizes are cross-sectional or panel at the study level, no longitudinal meta-regression can distinguish selection effects from causal learning returns to internationalization.

**(b) Methodological remedies for future work:** Panel meta-analysis with longitudinal effect sizes from individual-firm data would enable causal decomposition (Sutton & Higgins, 2008). Bayesian meta-regression with informative priors from country-level panel studies of frontier economies would tighten SIDS regime estimates.

**(c) Boundary of the ICRV classification:** The 6-regime taxonomy uses WGI Rule of Law as the primary classifier. Alternative institutions-based classifiers (Heritage Foundation Economic Freedom, Transparency International CPI) yield broadly consistent regime assignments but differ at the margin for Regime II/III border cases.

---

## 6. Conclusion

This paper presents the first three-level MARA of the internationalization–performance (I-P) relationship on a globally representative corpus (*k* = 238 studies, *K* = 288 effects, 49 economies), extending the ICBEF 2025 Asia-Pacific baseline (*k* = 113) and introducing three previously untested moderators, ICRV institutional regime, country-level digital adoption (cDAI), and Digital Paradox Lifecycle (DPL) phase. The pooled effect (*r* = 0.074, 95% CI [0.060, 0.088], $I^2$ = 87.8%) is small, positive, and robust across seven sensitivity checks.

H1 receives only fragile support: the full-sample ICRV omnibus is significant (*Q*_M = 17.35, *p* =.002) but collapses to non-significance once the 3-study Frontier cell is removed (*Q*_M = 1.49, *p* =.68). The directional gradient (E1a/E1b) and the cDAI (*Q*_M = 1.23, *p* =.541) and DPL (*Q*_M = 0.56, *p* =.755) hypotheses are not confirmed at current sample sizes. The most substantive finding is publication bias (H4 confirmed): trim-and-fill imputes *k* = 58 missing studies, reducing the bias-corrected effect to *r* = 0.035 (95% CI [0.023, 0.048]), a ~53% attenuation. The I-P field's published literature appears to over-represent positive findings, and the true average performance return to internationalization may sit closer to *r* ≈ 0.035 than to the 0.07–0.10 range commonly cited. The heterogeneity puzzle remains largely unresolved, but the three-level decomposition reframes it: within-study variance (Level 2, 76.1%) is the dominant source, not between-country differences (Level 3, 11.8%), methodological choices within papers contribute substantially more to dispersion than cross-country institutional contexts.

**Future research.** Three directions follow from the null moderator findings. First, a formal WoS/Scopus search targeting Frontier and SIDS economies would lift Frontier *k* from 3 to a plausible 20–40, enabling a powered between-regime test. Second, a pre-registered replication with explicit per-cell power calibrated to *r* ≈.035 on a *k* ≥ 400 corpus would deliver a definitive moderator test. Third, the publication-bias finding motivates a dedicated audit of unpublished I-P results (surveys, grey literature, dissertations) to bound the true population effect more precisely than trim-and-fill alone (see Section 5.4 for the full inferential-bound argument).

---


## Acknowledgements
We thank the authors of the 238 primary studies whose effect sizes are aggregated here; without their original data collection this meta-analysis would not be possible. We also acknowledge methodological guidance from the published works of Borenstein et al. (2021) and Vevea & Woods (2005). For primary studies drawing on World Bank Enterprise Surveys, we thank the Enterprise Analysis Unit of the Development Economics Global Indicators Group of the World Bank for the underlying data infrastructure that enabled multi-country effect-size extraction.

## Use of Generative AI in the Writing Process
Generative AI tools were used during manuscript preparation to assist with language editing, consistency checking of statistical notation across six bias-test methods, formatting of the reference list, and assembly of replication-package documentation. All conceptual framing, hypothesis development, meta-analytic model specification, results interpretation, and final wording were authored by the human authors, who take full responsibility for the content of the publication.

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

Author Citation (2024, December). *Internationalization and firm performance: A meta-analysis review* [Paper presentation]. International conference on sustainable development in economics, business, and finance (ICBEF). [Author details removed for blind review.]

Author Citation (2025). Internationalization and firm performance of firms in India: The role of top management. In M. Bartekova (Ed.), *International business research: Traditional and creative approaches*. IntechOpen. [Author details removed for blind review.]

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455–463.

Egger, M., Smith, G. D., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ, 315*(7109), 629–634.

Hunter, J. E., & Schmidt, F. L. (2015). *Methods of meta-analysis: Correcting error and bias in research findings* (3rd ed.). Sage Publications.

Geyskens, I., Krishnan, R., Steenkamp, J.-B. E. M., & Cunha, P. V. (2009). A review of survey research on inter-organizational outcomes in international business. *Journal of Management, 35*(2), 393–419. https://doi.org/10.1177/0149206308328488

Hedges, L. V., & Olkin, I. (1985). *Statistical methods for meta-analysis*. Academic Press.

Hedges, L. V., Tipton, E., & Johnson, M. C. (2010). Robust variance estimation in meta-regression with dependent effect size estimates. *Research Synthesis Methods, 1*(1), 39–65. https://doi.org/10.1002/jrsm.5

Hedges, L. V., & Vevea, J. L. (1996). Estimating effect size under publication bias: Small sample properties and robustness of a random effects selection model. *Journal of Educational and Behavioral Statistics, 21*(4), 299–332. https://doi.org/10.3102/10769986021004299

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

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S.,... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Peng, M. W., Wang, D. Y. L., & Jiang, Y. (2008). An institution-based view of international business strategy: A focus on emerging economies. *Journal of International Business Studies, 39*(5), 920–936.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology, 90*(1), 175–181.

Pustejovsky, J. E., & Tipton, E. (2022). Meta-analysis with robust variance estimation: Expanding the range of working models. *Prevention Science, 23*(3), 425–438. https://doi.org/10.1007/s11121-021-01246-3

Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models: Applications and data analysis methods* (2nd ed.). Sage.

Rosenthal, R. (1991). *Meta-analytic procedures for social research* (rev. ed.). Sage.

Rosenthal, R. (1994). Parametric measures of effect size. In H. Cooper & L. V. Hedges (Eds.), *The handbook of research synthesis* (pp. 231–244). Sage.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollender, L. (2018). Limits to outsourcing: A meta-analysis and empirical investigation. *Journal of International Business Studies, 49*(6), 682–703.

Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression approximations to reduce publication selection bias. *Research Synthesis Methods, 5*(1), 60–78.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80.

Sutton, A. J., & Higgins, J. P. T. (2008). Recent developments in meta-analysis. *Statistics in Medicine, 27*(5), 625–650.

Terrin, N., Schmid, C. H., Lau, J., & Olkin, I. (2003). Adjusting for publication bias in the presence of heterogeneity. *Statistics in Medicine, 22*(13), 2113–2126. https://doi.org/10.1002/sim.1461

Tipton, E. (2015). Small sample adjustments for robust variance estimation with meta-regression. *Psychological Methods, 20*(3), 375–393. https://doi.org/10.1037/met0000011

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong, J., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Vevea, J. L., & Hedges, L. V. (1995). A general linear model for estimating effect size in the presence of publication bias. *Psychometrika, 60*(3), 419–435. https://doi.org/10.1007/BF02294384

Vevea, J. L., & Woods, C. M. (2005). Publication bias in research synthesis: Sensitivity analysis using a priori weight functions. *Psychological Methods, 10*(4), 428–443.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software, 36*(3), 1–48.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic Management Journal, 5*(2), 171–180.

World Bank. (2023). *Worldwide Governance Indicators*. https://info.worldbank.org/governance/wgi/

Wu, J., Wood, G., & Khan, Z. (2022). Internationalization and firm performance: Evidence from a meta-analysis. *International Business Review, 31*(2), 101920. https://doi.org/10.1016/j.ibusrev.2021.101920

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of Management Journal, 38*(2), 341–363.

---

## Supplementary Materials (OSF)

The complete PRISMA 2020 flow diagram with both Path A (analyzed corpus, *k* = 238 / *K* = 288 from anchor-meta-analysis citation tracking and hand-search) and Path B (database-search expansion, full-text extraction ongoing) is provided as **Supp-A**; the full 7-moderator coding protocol as **Supp-B**; the MetaEssentials-vs-`metafor` consistency check as **Supp-C**; the detailed eligibility criteria as **Supp-T1**; the cDAI and DPL phase subgroup tables as **Supp-T2** and **Supp-T3**; the full robustness-checks table as **Supp-T4**; the detailed Section 3.2 PRISMA screening narrative as **Supp-T5**; and the extended methodological notes (three-level model specification, publication-bias tests, robustness-check specifications) as **Supp-M**. All items are deposited on OSF (https://osf.io/z37kn).

---

*Word count (main text Sections 1–6 prose, excluding tables, references, in-paper tables, and OSF supplementary materials): $\approx$ 8,040 words. Submission-build total (body + references + 3 in-paper tables × 280 + 7 figures × 280): $\approx$ 11,966 word-equivalents, within MIR's $\approx$ 12,000-word envelope. Revision v1.3 addresses the publication-bias paradox (Section 5.2), construct-validity restriction of cDAI (Section 4.4), drop-Frontier-led ICRV framing (Section 4.3), and a fifth disclosed pre-registration deviation (Section 3.1).*
*Target journal: Asia Pacific Journal of Management (APJM; Springer Nature, Scopus Q1, ABS-3). Extended methodological appendices (PRISMA 2020 flow; 7-moderator coding protocol; MetaEssentials-vs-`metafor` consistency check), the detailed eligibility criteria, the cDAI and DPL subgroup tables, the full robustness-checks table, the Section 3.2 PRISMA screening narrative, and extended methodological notes are migrated to OSF as Supp-A through Supp-M (https://osf.io/z37kn; OSF pre-registration DOI: 10.17605/OSF.IO/Z37KN; the pre-registration body is journal-agnostic and remains the same across target-journal exploration). Analyses use the verified baseline corpus (k = 238 studies, K = 288 effect sizes); the formal WoS/Scopus search expansion (Path B) is pre-registered for follow-up replication on a corpus of k ≈ 600–700 and is not a condition on the validity of the present findings. Effect-size coding follows the standardized protocol summarized in Section 3.4 and detailed in Supp-B.*
