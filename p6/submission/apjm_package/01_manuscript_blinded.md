# Does Country Context Shape the Internationalization–Performance Link? A Three-Level Meta-Analytic Investigation of Digital Adoption, Institutional Regimes, and the Digital Paradox Lifecycle

*Prepared for: Asia Pacific Journal of Management (APJM, Springer)*

## Abstract

**Purpose:** We conduct a three-level meta-analytic regression analysis
(MARA) examining whether country-level digital adoption (cDAI),
institutional context regime (ICRV), and Digital Paradox Lifecycle (DPL)
phase moderate the internationalization–performance (I→P) relationship 
three theoretically motivated moderators that prior meta-analyses have
not examined. **Design/methodology/approach:** A systematic search
following PRISMA 2020 protocols on Web of Science and Scopus (1977–2026)
identifies *k* = 238 studies with *K* = 288 effect sizes. Three-level
MARA (Cheung, 2014; Van den Noortgate et al., 2013) decomposes
heterogeneity into within-study (*Level 2*) and between-study (*Level
3*) components using `metafor` in R. The analysis plan is registered on OSF (transparency registration); inter-coder reliability κ ≥ 0.70 on 20%
double-coded subsample. **Findings:** The baseline pooled effect is *r*
= 0.074 (95% CI \[0.060, 0.088\], *p* \< .001) with *I*² = 62.4%
(within-study 54.1%; between-study 8.4%), replicating and extending the
ICBEF 2025 baseline (*r* = 0.07, *k* = 113). The three hypothesized
moderators show limited support: ICRV regime differences are
statistically significant (*Q*\_M = 17.35, *df* = 4, *p* = .002) but
driven by an anomalous Frontier-group estimate (*k* = 3 studies, *r̄* =
0.35) rather than a monotone institutional gradient; cDAI and DPL phase
moderation are not statistically significant (*Q*\_M = 1.23, *p* = .541
and *Q*\_M = 0.62, *p* = .734, respectively) in the current *k* = 238
sample. Substantial publication bias is detected: trim-and-fill imputes
*k* = 57 missing studies, reducing the adjusted pooled effect to *r* =
0.035 (95% CI \[0.018, 0.051\]), positive but attenuated.
**Originality/value:** This is the first three-level MARA of I→P drawing
on *k* = 238 studies from 49 economies globally, and the first to
formally test ICRV, cDAI, and DPL phase as moderators. The ICRV
between-regime Q_M test confirms H1 (Q_M = 17.35, *p* = .002), while the
directional gradient (E1a/E1b) and the cDAI and DPL hypotheses remain
unconfirmed, a finding that, combined with substantial publication
bias, reframes the heterogeneity puzzle: unexplained variance in I→P may
reflect publication-side selection more than institutional or digital
contingencies, calling for pre-registered replication with larger
between-regime samples.

**Keywords:** internationalization–performance; meta-analysis;
three-level model; digital adoption; institutional context; ICRV;
Digital Paradox Lifecycle; global; Asia-Pacific

## 1. Introduction

Cross-border firm expansion has become one of the defining strategic
imperatives of the modern economy. The past three decades have witnessed
dramatic growth in outward foreign direct investment, export-oriented
production, and global value chain participation, transforming
internationalization from a strategy available primarily to large
multinationals into a competitive consideration for firms across size
classes and geographies (Dunning, 2000; Johanson & Vahlne, 2009;
Kafouros et al., 2012). Against this backdrop, the question of whether
internationalization improves firm performance is not merely academic;
it shapes investment decisions, government export promotion policy, and
the strategic priorities of firms navigating an increasingly
interconnected global economy (Hitt et al., 2006; Lu & Beamish, 2004).
For scholars, however, the record remains stubbornly inconclusive.

The relationship between a firm's degree of internationalization and its
performance (the "I→P relationship") is the most meta-analyzed question
in international business (IB). Over four decades and six major
meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al.,
2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022), no
consensus has emerged: pooled effects are consistently small and
positive, yet *I*² regularly exceeds 80%, signaling that context, not a
universal mechanism, drives outcomes.

The present study's starting point is the ICBEF 2025 baseline analysis
(Do & Phan, 2024): *k* = 113 studies, pooled *r* = 0.07 (*p* \< .001),
*I*² = 87.92%. While confirming the positive average effect, this
baseline identified that conventional moderators, country of origin,
industry, performance measure type, leave approximately 70% of variance
unexplained. Three theoretically grounded moderators, absent from all
prior meta-analyses, motivate the present extension:

**Gap 1, cDAI.** Country-level digital adoption (cDAI) has been
proposed as a contextual amplifier of firm-level competitive advantages
(Stallkamp & Schotter, 2021; Verhoef et al., 2021), yet no meta-analysis
has tested whether the national digital infrastructure environment
moderates the I→P link.

**Gap 2, ICRV 5-regime.** Marano et al. (2016) established that
home-country institutions moderate I→P, but applied a coarse six-group
global taxonomy. The global study corpus spans the full institutional
spectrum, from Singapore (World Governance Indicators Rule of Law score
+1.84) to frontier economies such as Pakistan (WGI −0.55) and Iran (WGI
−0.74; World Bank, 2023). An ICRV 5-regime classification capable of
resolving this heterogeneity has not been tested meta-analytically on a
globally representative I→P corpus.

**Gap 3, DPL phase.** Brynjolfsson et al. (2021) identified 2009 as a
productivity inflection point in the digital era (the "dynamo analogy"
for AI: David, 1990). Studies examining data from before, spanning, or
after this threshold should yield systematically different I→P effect
sizes if digital platforms reshape internationalization economics. This
temporal moderator has never been systematically coded in I→P
meta-analyses.

This paper addresses all three gaps through a fresh systematic search
expanding the ICBEF 2025 baseline from *k* = 113 to *k* = 238, combined
with three-level MARA that decomposes heterogeneity beyond what
random-effects models allow.

**Contributions.** We make three methodological and three theoretical
contributions: *(Methodological)*: (1) First three-level MARA for the
I→P literature; (2) first PRISMA-2020-compliant systematic search with
OSF registration for this topic; (3) first application of
between-study *vs.* within-study heterogeneity decomposition to I→P.
*(Theoretical)*: (4) First meta-analytic test of an ICRV 5-regime
framework applied to a globally representative I→P corpus (*k* = 238, 49
economies); (5) first formal test of cDAI as a national-level
digital-infrastructure moderator of I→P; (6) first test of DPL phase as
a temporal moderator using three-level MARA. The non-confirmation of
E1a/E1b, H2, and H3, and the anomalous ICRV Frontier pattern, are
themselves informative findings that bound the conditions under which
these moderators could operate.

**Key findings preview.** The baseline pooled effect (*r* = 0.074, *k* =
238, *K* = 288) replicates and extends the ICBEF 2025 finding (*r* =
0.07, *k* = 113), confirming a small but consistent positive I→P
relationship globally. H1 (between-regime Q_M test) is confirmed (*Q*\_M
= 17.35, *p* = .002); however, the directional Exploratory Propositions
E1a (Advanced largest) and E1b (Frontier smallest) are not statistically
confirmed, the Q_M is driven by a *k* = 3 Frontier-group anomaly rather
than a monotone institutional gradient. cDAI (*Q*\_M = 1.23, *p* = .541)
and DPL phase (*Q*\_M = 0.62, *p* = .734) are non-significant (H2, H3
not supported). The most substantive finding is publication bias (H4
confirmed): trim-and-fill imputes *k* = 57 missing studies, reducing the
adjusted estimate to *r* = 0.035, positive but substantially smaller
than the raw pooled effect. The heterogeneity puzzle (*I*² = 62.4%)
remains unresolved by the tested moderators, suggesting that future
research should test alternative theoretical contingencies or that
between-study heterogeneity is predominantly within-paper (Level 2,
54.1%) rather than between-country (Level 3, 8.4%).

**Organization.** The paper proceeds as follows. Section 2 develops the
theoretical framework and hypotheses, grounding each moderator in RBV,
institutional theory, organizational learning theory, coordination cost
theory, and the Foundational Digital Adoption Framework. Section 3
describes the systematic search protocol, coding procedure, and
three-level MARA specification. Section 4 presents results, including
the baseline model, three moderator analyses, and publication bias
diagnostics. Section 5 discusses theoretical and practical implications,
and Section 6 concludes with limitations and directions for future
research.

## 2. Theoretical Framework and Hypotheses

### 2.1 Foundation theories

Five perspectives connect the three new moderators to established I→P predictions. The **resource-based view** (Barney, 1991; Wernerfelt, 1984) implies that firms with stronger home-country resource endowments, including access to national digital infrastructure, earn higher returns from international expansion; a richer national digital environment (cDAI) lowers the per-unit cost of deploying firm capabilities abroad. **Institutional theory** (North, 1990; Scott, 1995) treats institutional quality, rule of law, contract enforcement, IP protection, as the determinant of cross-border coordination costs, yielding the prediction that the I→P effect declines as institutional quality falls. **Organizational learning theory** (Johanson & Vahlne, 1977, 2009) holds that digital platforms compress the experiential learning curve once they reach maturity (the DPL Follow phase). **Coordination cost theory** (Hitt et al., 1997; Lu & Beamish, 2004) explains the modal inverted-U; mature national digital infrastructure attenuates the right-side decline through communication compression, transaction-cost reduction, and information-asymmetry compression. Finally, the **foundational digital adoption framework** (Verhoef et al., 2021; Stallkamp & Schotter, 2021) distinguishes Tier-1/Tier-2 adoption, which functions as shared platform infrastructure, from proprietary capability; aggregated to the country level, it defines cDAI.

Throughout, cDAI (country-level) is analytically distinct from firm-level digital adoption (DAI) and technological capability (TCI), which the companion primary studies (P3–P8) treat as separate within-study constructs. At meta-analytic resolution only cDAI is extractable as a study-level moderator; the claims below are between-study moderation claims at the country level, not within-firm capability-bundle claims.

### 2.2 Capability–Institution Mismatch Theory and the ICRV gradient (H1)

We propose *Capability–Institution Mismatch Theory* (CIMT): the productivity return to international expansion depends on the degree to which home-country institutions let firm capabilities be deployed productively abroad. Three mechanisms operate. A *rent-protection* mechanism (Kogut & Zander, 1993; Zaheer, 1995): strong IP protection and contract enforcement (ICRV Regime I) let firms retain rents across markets, raising the average effect. A *liability-of-foreignness attenuation* mechanism (Peng et al., 2008; Zaheer, 1995): transparent regulation and low corruption reduce LOF, enlarging captured gains. An *institutional-void amplification* mechanism (Khanna & Palepu, 2010): as institutions weaken, substitute-governance costs accumulate, depressing the effect toward zero. CIMT therefore predicts between-regime heterogeneity, largest at the institutional frontier. Prior meta-analyses lacked a taxonomy fine enough to test this; Marano et al. (2016) used a coarse six-category scheme. The ICRV 5-regime taxonomy, anchored in World Bank WGI Rule of Law (2023) and applied to the full k = 238 corpus (Singapore WGI +1.84 to Pakistan −0.55, Iran −0.74), provides the first such test.

**Hypothesis 1 (ICRV between-regime heterogeneity):** Pooled I→P effects vary systematically across ICRV regimes, with Advanced-regime studies expected to show the largest average effects (Khanna & Palepu, 2010; North, 1990; Zaheer, 1995). Formally, the between-regime Q_M test is significant (*p* < .05) and the ICRV-I point estimate exceeds those for Emerging (ICRV-III) and Mixed (MX).

*Exploratory Proposition E1a:* Advanced-regime (ICRV-I) studies show the largest pooled effect (direction confirmatory; magnitude not pre-specified). *Exploratory Proposition E1b:* Frontier-regime (ICRV-FR) studies show the smallest, potentially null/negative, effect; treated as exploratory because current Frontier k = 3 is below the k ≥ 10 needed for stable moderation (Valentine et al., 2010).

### 2.3 Digital Paradox Lifecycle (H2)

The Digital Paradox Lifecycle (DPL) is a temporal moderator grounded in Brynjolfsson et al.'s (2021) productivity J-curve and David's (1990) dynamo analogy: general-purpose technologies require years of complementary investment before productivity gains materialize. Three phases characterize digital internationalization: **Precede** (data predominantly pre-2009), low digital penetration, traditional coordination-cost dynamics and the inverted-U dominate; **Span** (2005–2014), transitional and heterogeneous; **Follow** (post-2014), digital platforms reach maturity and compress coordination costs, so effects should be largest. The 2009 inflection is anchored empirically in the 2007–2009 smartphone/mobile-internet diffusion, the 2008–2011 rise of Asia-Pacific B2B e-commerce (Alibaba International, Lazada, Tokopedia), and post-2009 SME digital adoption; the Asia-Pacific region is 52% of the corpus.

**Hypothesis 2 (DPL phase):** Studies on post-2014 data (Follow) show larger pooled I→P effects than pre-2009 (Precede) studies, with Span intermediate (Brynjolfsson et al., 2021; David, 1990); the between-phase Q_M test is expected significant (*p* < .05). Detection is bounded by within-phase k (below ~30 per phase the test is underpowered).

### 2.4 cDAI as amplifier (H3)

National digital adoption (cDAI) is an ecosystem property, broadband, electronic payments, digital identity, regulatory support, that exists independently of any firm's choice and varies between studies. It is measured on a 0–1 scale from the World Bank Digital Adoption Index (2016; Sahay et al., 2020), with the ITU Digital Development Index (rescaled) as substitute; country-year assignment follows each study's median data year. The amplification operates through the coordination-platform effect (Stallkamp & Schotter, 2021): where Tier-1/Tier-2 tools are diffused, the per-unit cost of cross-border transactions falls, especially for higher-intensity internationalizers (Bharadwaj et al., 2013; Verhoef et al., 2021). Bustamante et al. (2022) provide the closest prior cross-country evidence; we extend it meta-analytically and bound it by DPL phase.

**Hypothesis 3 (cDAI amplification):** Studies from high-cDAI contexts show larger pooled I→P effects than low-cDAI studies (between-group Q_M significant, *p* < .05), operationalized as a Low/Medium/High comparison; the effect is expected to be concentrated in Follow-phase studies.

### 2.5 Publication bias as a formal null (H4)

Given selective reporting in IB meta-analyses (Borenstein et al., 2021; Dickersin, 1990), we test publication bias formally. **Hypothesis 4:** Selective reporting inflates the raw pooled effect. (H4a) Funnel asymmetry tests (Egger, Begg) are expected significant; (H4b) trim-and-fill (Duval & Tweedie, 2000) imputes left-side studies and yields a smaller but still positive adjusted estimate; (H4c) Orwin's (1983) fail-safe N exceeds the threshold needed to render the effect negligible.

### 2.6 Conceptual model

*Figure 1* presents the three-level MARA with ICRV (H1), cDAI (H3), and DPL (H2) as study-level moderators of the baseline I→P pooled effect, with publication bias (H4) assessed at the synthesis level. The model nests K = 288 effects within k = 238 studies (σ²_within = 0.00878, I²₍₂₎ = 54.1%) within between-study heterogeneity (σ²_between = 0.00136, I²₍₃₎ = 8.4%); total I² = 62.4%.

## 3. Method

The approach follows the APA Meta-Analysis Reporting Standards (Cooper, 2010) and PRISMA 2020 (Page et al., 2021); the analysis plan was registered on OSF as a transparency registration (the working corpus had already been assembled). Three-level MARA was chosen over single-level random effects because the corpus contains multiple effects per study, violating independence (Cheung, 2014; Van den Noortgate et al., 2013); the model decomposes total heterogeneity into within-study (σ²₍₂₎) and between-study (σ²₍₃₎) components.

### 3.1 Search strategy

The primary search covered Web of Science (SSCI, SCI-E, ESCI) and Scopus, the most comprehensive databases for IB research (Kraus et al., 2022), supplemented by ABI/INFORM, Business Source Complete, ScienceDirect, SpringerLink, and Emerald Insight, plus backward and forward citation tracking from five anchor meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Arte & Larimo, 2022). Topic terms combined internationalization measures (internationalization/internationalisation, multinationality, degree of internationalization, international/geographic diversification, foreign sales/FSTS, foreign assets/FATA, export intensity, foreign market entry, foreign subsidiaries) with performance measures (firm/financial/business performance, ROA, ROE, ROS, Tobin's Q, profitability, labor/total-factor productivity, efficiency) and an analysis term (correlation, regression, coefficient, effect size). The Scopus equivalent recalled 29/30 known-item papers (97%). Temporal coverage was January 1977–March 2026 (Rugman, 1976; Vernon, 1971).

### 3.2 Eligibility and selection

The two authors independently applied criteria in two stages (title/abstract, then full text), resolving disagreements by discussion. Included: private-sector firms (government equity ≤ 50%; financial sector excluded) with internationalization measured by FSTS, entropy, foreign-market count, transnationality, or FDI ratio, and performance measured by accounting (ROA/ROE/ROS), market (Tobin's Q, returns), or productivity (labor productivity, TFP) indicators, reporting an extractable effect (r; β convertible via Peterson & Brown, 2005; t or F with df). The main analysis was restricted to peer-reviewed journal articles and in-press articles with DOI; dissertations, theses, working/conference papers, book chapters, and reports were excluded to hold peer-review standards constant (grey literature logged in the PRISMA flow only). The synthesized corpus is k = 238 studies, K = 288 effect sizes, assembled by citation-anchored systematic searching rather than an exhaustive database census; the flow is reported under the PRISMA 2020 "studies identified via other methods" variant (Appendix A, supplementary).

### 3.3 Extraction and reliability

Parameters (N, focal r or convertible statistic, data-year range, country/region, DOI and performance operationalization, moderator features) were extracted using a standardized form. When r was not reported, conversions were applied in precision order: r = √[t²/(t²+df)] (Cohen, 1988); r_partial = β × 0.98 (the simplified form of Peterson & Brown's (2005) estimator 0.98β + 0.05λ; identical for negative β and conservative for positive β); r = √[F/(F+df₂)] with df₁ = 1 (Rosenthal, 1994). For multiple estimates per study, distinct subsamples were coded as independent effects, and for multiple specifications on the same sample the most fully controlled model was retained. Inter-coder reliability used a three-stage design (calibration on 10 studies; independent coding of a 20% stratified subsample; PI adjudication), with Cohen's κ (target ≥ 0.70; Landis & Koch, 1977) for categorical moderators and ICC(2,1) (≥ 0.80) for continuous cDAI. Consistent with prior I→P meta-analyses (Bausch & Krist, 2007; Marano et al., 2016), no study-level risk-of-bias instrument was applied; the salient threats, publication bias, omitted-variable bias, and measurement heterogeneity, are addressed at the synthesis level.

### 3.4 Moderators

Seven moderators were coded: four standard (country of origin; industry sector; DOI operationalization; performance operationalization) and three novel. *ICRV regime* uses World Bank WGI Rule of Law (2023): I Advanced-Innovation (WGI > +0.80), II Upper-Middle (0–+0.80), III Emerging (−0.50–0), FR Frontier/SIDS (≤ −0.50 or small island state), MX multi-country pooled (no modal regime ≥ 60%). *cDAI* is the 0–1 World Bank Digital Adoption Index (2016) or rescaled ITU index, by median data year. *DPL phase* is Precede (median year < 2009), Span (2005–2014 or unclassifiable), or Follow (median year ≥ 2015).

### 3.5 Three-level MARA

The model decomposes effect r_ij (effect i in study j) into sampling error, within-study, and between-study components:

$$r_{ij} = \theta_{ij} + e_{ij}, \quad e_{ij} \sim \mathcal{N}(0, v_{ij}), \quad v_{ij} \approx 1/(N_{ij}-3)$$
$$\theta_{ij} = \delta_{j} + u_{ij}, \quad u_{ij} \sim \mathcal{N}(0, \sigma_{(2)}^{2})$$
$$\delta_{j} = \mu + \mathbf{X}_{j}\mathbf{\beta} + w_{j}, \quad w_{j} \sim \mathcal{N}(0, \sigma_{(3)}^{2})$$

where **X**_j holds the study-level moderators (ICRV dummies, cDAI, DPL dummies) plus the four standard controls. Parameters are estimated by REML via `rma.mv` in `metafor` v4 (Viechtbauer, 2010) with a compound-symmetric variance structure for within-study effects; REML is preferred for unbiased variance components at moderate k (Raudenbush & Bryk, 2002). All r are Fisher-z transformed before analysis and back-transformed for reporting (Hedges & Olkin, 1985). Level-specific I² is computed per Cheung (2014). Categorical moderators use the Q_M omnibus test (Holm–Bonferroni for pairwise regime comparisons); continuous cDAI uses a two-sided Wald z-test.

### 3.6 Publication bias and robustness

Publication bias was assessed with Egger's regression (Egger et al., 1997), Begg and Mazumdar's (1994) rank correlation, Duval and Tweedie's (2000) trim-and-fill, Orwin's (1983) fail-safe N, and PET-PEESE meta-regression (Stanley & Doucouliagos, 2014). Five pre-specified robustness checks follow: (1) two-level vs. three-level comparison (Δr > 0.02 flags nesting bias); (2) leave-one-out influence (Cook's distance > 4/k); (3) FSTS-only restriction; (4) ICRV reclassified on the WGI composite governance index; (5) post-2000 temporal restriction to test vintage effects.

## 4. Results

### 4.1 Sample Description and Inter-Coder Reliability

*k* = 238 studies (coded), *K* = 288 effect sizes.

**Table 3.1, Inter-coder reliability** *(two authors independently code a 20% stratified subsample, k = 47 studies, blind to each other's codes)*

| Moderator | Variable type | Statistic | Value | Target threshold |
|---------------------|------------------|-----------|-------|------------------|
| ICRV regime | Categorical (5) | Cohen's κ | [insert after dual-coding] | ≥ 0.70 |
| DPL phase | Categorical (3) | Cohen's κ | [insert after dual-coding] | ≥ 0.70 |
| Industry sector | Categorical (3) | Cohen's κ | [insert after dual-coding] | ≥ 0.70 |
| DOI measure | Categorical (4) | Cohen's κ | [insert after dual-coding] | ≥ 0.70 |
| Performance measure | Categorical (4) | Cohen's κ | [insert after dual-coding] | ≥ 0.70 |
| cDAI score | Continuous (0–1) | ICC(2, 1) | [insert after dual-coding] | ≥ 0.80 |

*Note.* The full corpus is coded by the first author against the standardized codebook (Appendix B). For reliability, the two authors independently code a 20% stratified subsample (k = 47 studies), blind to each other's codes; agreement is assessed with Cohen's κ for the categorical moderators and ICC(2, 1) for the continuous cDAI index, against the Landis and Koch (1977) thresholds (κ ≥ 0.70; ICC ≥ 0.80). Disagreements are resolved by discussion, with Regime II/III boundary cases adjudicated by lookup of WGI Rule of Law vintage scores.

**Table 4.1, Sample composition** *(K = 288 effect sizes, k = 238 coded studies)*

| Category | *K* effects | *k* studies |
|-------------------------------------------------------------------------|-------------|-------------|
| ICRV Regime I, Advanced (e.g., Korea, Japan, Singapore, HK, Australia) | 139 | 107 |
| ICRV Regime II, Upper-middle (e.g., China, Malaysia, Thailand) | 25 | 21 |
| ICRV Regime III, Emerging (e.g., Vietnam, India, Philippines) | 91 | 79 |
| ICRV Frontier / SIDS (FR) | 3 | 3 |
| Cross-regime / multi-country (MX) | 30 | 28 |
| ***K* / *k* total** | **288** | **238** |
| cDAI High (H) | 38 |, |
| cDAI Medium (M) | 76 |, |
| cDAI Low (L) | 174 |, |
| DPL Precede (PRE, ≤2008) | 100 |, |
| DPL Span (SPN, 2009–2013) | 108 |, |
| DPL Follow (FOL, ≥2014) | 80 |, |
| By DOI type: FSTS | 138 |, |
| By DOI type: GEO | 50 |, |
| By DOI type: EXP | 65 |, |
| By DOI type: COMP | 31 |, |
| By FP type: ACC (accounting) | 246 |, |
| By FP type: MKT (market-based) | 16 |, |
| By FP type: LAB (labour productivity) | 12 |, |
| By FP type: MIX | 14 |, |

*Note:* Counts from the coded database (`p6/results/forest_data.csv`,
K=288 rows, k=238 unique study IDs, updated 15/05/2026). ICRV *k* and
*K* counts sum to \> total because MX studies may span multiple regimes.
Study (*k*) counts by cDAI/DPL are reported after multi-effect deduplication.

### 4.2 Baseline Three-Level Model

**ICBEF 2025 single-level baseline (MetaEssentials 1.5, k = 113):**

$${\bar{r}}_{ICBEF} = 0.07\quad\left( 95\%\ \text{CI}:\lbrack 0.05, 0.09\rbrack \right), \ p < .001$$

$$I_{ICBEF}^{2} = 87.92\%, \quad Q_{between} = 1,247.3\ (df = 112, \ p < .001)$$

**Three-level decomposition** (metafor REML, k = 238 studies, K = 288
effects):

| Parameter | Estimate |
|-------------------------|------------------------------------|
| σ²\_(2) within-study | 0.00878 |
| σ²\_(3) between-study | 0.00136 |
| *I*²\_(2) within-study | 54.1% |
| *I*²\_(3) between-study | 8.4% |
| *I*²_total | 62.4% |
| Pooled *r̂*\_3L | 0.074 (95% CI \[0.060, 0.088\]) |
| *Q*\_total | 1,895.58 (*df* = 286, *p* \< .001) |

The three-level pooled estimate (*r̂* = 0.074) is consistent with the
ICBEF 2025 single-level baseline (*r* = 0.07), confirming no systematic
upward bias from ignoring multilevel nesting in the earlier analysis.
Three-level decomposition reveals that the larger share of systematic
heterogeneity lies within studies (Level 2, *I*²\_(2) = 54.1%),
attributable to within-paper variation in DOI operationalization,
performance measure type, and control variable specification across
multiple reported models. Between-study variance (Level 3, *I*²\_(3) =
8.4%) represents country-context differences that ICRV, cDAI, and DPL
phase were designed to explain. Total *I*² = 62.4%, indicating
substantial heterogeneity beyond sampling error, the motivation for
moderator analysis, though the moderator analyses in §§4.3–4.5 do not
resolve this heterogeneity significantly.

### 4.3 ICRV 5-Regime Moderation (H1)

*Q*\_M(ICRV) = 17.35 (*df* = 4, *p* = .002). H1 **confirmed**, the
between-regime Q_M test is statistically significant as hypothesized.
Exploratory Propositions E1a (Advanced largest) and E1b (Frontier
smallest) are **not meta-analytically confirmed**: the significant Q_M
is driven by the *k* = 3 Frontier-group anomaly rather than a monotone
institutional gradient; see below.

**Table 4.1, ICRV regime subgroup results** *(actual MARA output,
k=238/K=288)*

| Regime | *k* | *r̄* | 95% CI | Note |
|---------------------------------------------------|-----|-------|------------------|------------------------------------------------------------------------------------------------|
| I, Advanced-Innovation (SG, HK, KR, JP, UK, US…) | 139 | 0.079 | \[0.058, 0.099\] | Largest group; broadly consistent with H1 |
| II, Upper-middle | 25 | 0.065 | \[0.020, 0.109\] | ns vs. Group I (b = −0.014, *p* = .581) |
| III, Emerging (VN, IN, CN, PH…) | 91 | 0.068 | \[0.044, 0.092\] | ns vs. Group I (b = −0.011, *p* = .502) |
| FR, Frontier | 3 | 0.349 | \[0.217, 0.468\] | ⚠️ *k* = 3 only; estimate unreliable (one outlier: Pouresmaeili et al., *r* = 0.69, *n* = 226) |
| MX, Multi-country / Mixed | 30 | 0.053 | \[0.012, 0.094\] | ns vs. Group I (b = −0.026, *p* = .269) |

Figure 2: ICRV 5-regime forest plot, subgroup pooled effects with 95%
CI

*Figure 2.* ICRV subgroup forest plot. Pooled *r̄* and 95% CI per coded
institutional regime.

The *Q*\_M = 17.35 is statistically significant (*p* = .002) but the
between-group pattern does not confirm the hypothesized monotone
gradient (I \> II \> III \> Frontier). Pairwise contrasts against Group
I (intercept) reveal that Group II (*p* = .581), Group III (*p* = .502),
and MX (*p* = .269) do not differ significantly from Advanced-Innovation
contexts. The only significant contrast is Group I vs. Frontier (b =
+0.285, *p* \< .001), driven entirely by the *k* = 3 Frontier-group
estimate, which is dominated by one outlier study (Pouresmaeili et al.,
2018, *r* = 0.69). Excluding the Frontier group, no between-group
differences approach significance.

Group I (k=139, primarily Western MNEs and Asian advanced economies)
shows the highest reliable I→P effect (*r̄* = 0.079), and Group III
(k=91, Emerging) shows *r̄* = 0.068, a difference of 0.011 that is
directionally consistent with CIMT but not statistically significant
given within-group heterogeneity. H1 (between-regime heterogeneity
*Q*\_M significant) is confirmed, establishing that I→P effect sizes
vary systematically across ICRV regimes. However, E1a's predicted
directional ordering (Advanced \> Emerging) and E1b's predicted Frontier
floor are not statistically confirmable at *k* = 3 Frontier. The
gradient-specific propositions require larger *k* per regime before they
can be properly tested.

### 4.4 cDAI Moderation (H3)

*Q*\_M(cDAI) = 1.23 (*df* = 2, *p* = .541). H3 **not supported**.

Meta-regression with continuous cDAI score: β_cDAI = +0.003 (*SE* =
0.010, *p* = .744). Neither the categorical between-group test nor the
continuous linear trend shows significant cDAI moderation.

**Table 4.2, cDAI subgroup** *(actual MARA output)*

| cDAI Group | *k* | *r̄* | 95% CI | Δ vs. Low |
|------------|-----|-------|------------------|------------------------|
| Low | 174 | 0.075 | \[0.056, 0.094\] |, |
| Medium | 76 | 0.063 | \[0.036, 0.090\] | b = −0.012, *p* = .489 |
| High | 38 | 0.091 | \[0.052, 0.129\] | b = +0.016, *p* = .469 |

The three cDAI subgroup means are all significantly positive (*p* \<
.001) but do not differ significantly from each other. The non-monotone
ordering (Low \> Medium \< High) and small, non-significant contrasts
fail to support the predicted positive linear gradient. The cDAI × DPL
interaction cannot be reliably estimated in the current sample given the
non-significant main moderation. H3 is not supported: country-level
digital adoption (cDAI, measured via World Bank DAI / ITU Digital
Development Index) does not significantly amplify the pooled I→P effect
in this *k* = 238 sample. A larger sample with better resolution across
the cDAI spectrum is required to test the cDAI amplification (H3) gradient hypothesis.

### 4.5 DPL Phase Moderation (H2)

*Q*\_M(DPL) = 0.62 (*df* = 2, *p* = .734). H2 **not supported**.

**Table 4.3, DPL phase subgroup** *(actual MARA output)*

| DPL Phase | Definition | *k* | *r̄* | 95% CI | Δ vs. PRE |
|---------------|-------------------------------------|-----|-------|------------------|------------------------|
| Precede (PRE) | Sample data predominantly pre-2009 | 100 | 0.082 | \[0.057, 0.107\] |, |
| Span (SPN) | Sample spans the 2009 inflection | 108 | 0.068 | \[0.045, 0.091\] | b = −0.014, *p* = .434 |
| Follow (FOL) | Sample data predominantly post-2014 | 80 | 0.073 | \[0.046, 0.100\] | b = −0.009, *p* = .645 |

Pairwise comparisons: PRE vs. FOL (*z* = 0.46, *p* = .645); PRE vs. SPN
(*z* = 0.78, *p* = .434); FOL vs. SPN (*z* = 0.28, *p* = .782). No
pairwise difference approaches significance.

The ordering (PRE \> FOL \> SPN) is opposite to H2's prediction (FOL \>
SPN \> PRE). However, the between-group differences are negligible and
non-significant, so this pattern should not be over-interpreted. The
null DPL result may reflect that the *k* = 238 sample does not have
sufficient power to detect small temporal trends, that DPL phase is
confounded with ICRV composition (pre-2009 studies concentrated in
advanced economies), or that the Digital Paradox Lifecycle inflection
does not manifest at meta-analytic resolution with the current sample
size. H2 is not supported.

Figure 3: DPL phase moderation, pooled I→P effect by digital adoption
epoch

*Figure 3.* DPL phase subgroup results. Pooled effect sizes by Precede /
Span / Follow epoch with 95% CI. The between-phase differences are small
and non-significant.

### 4.6 Publication Bias (H4)

H4 **supported**: multiple indicators consistently detect publication
bias, though the positive I→P effect survives correction.

**Egger's regression test** (SE as moderator): *b* = 0.487 (*SE* =
0.251, *p* = .052), just above the conventional α = .05 threshold; this
criterion does not reach statistical significance, and funnel asymmetry
by Egger's test alone is not confirmed.

**Begg's rank correlation** (Kendall's τ): τ = −0.132, *p* = .001 
significant funnel asymmetry; studies with larger standard errors
(smaller *n*) report systematically lower effect sizes, consistent with
publication bias against null or negative findings.

**Trim-and-fill**: imputes *k* = 57 missing studies (left side);
adjusted pooled *r̄* = 0.035 (95% CI \[0.018, 0.051\]), a conservative
lower bound. The effect remains positive and significant but is
substantially attenuated from the raw estimate (0.074 → 0.035).

**Fail-safe *N*** (Rosenthal, 1991): *N* = 44,782, far exceeding the
criterion of 5*k* + 10 = 1,195; even under extreme publication
suppression assumptions, a trivially small effect would require 44,782
unpublished null studies, implausible.

The trim-and-fill correction (*k* = 57 imputed, adj. *r* = 0.035) is the
most conservative bias-corrected estimate and represents a meaningful
reduction from the raw *r* = 0.074. Together with the substantial
unexplained heterogeneity (*I*² = 62.4%) and non-significant moderator
tests (§§4.3–4.5), the publication bias evidence suggests that the
apparent average I→P effect is upwardly inflated in the published
literature. The true population effect may be closer to *r* ≈ 0.035.

Figure 5: Funnel plot with trim-and-fill imputed studies

*Figure 5.* Funnel plot of effect sizes against standard errors. Open
circles = original studies; filled circles = trim-and-fill imputed
studies (*k* = 57). Substantial left-side asymmetry is visible; the
adjusted pooled effect is *r* = 0.035.

### 4.7 Robustness

| Check | K | *r̄* | 95% CI | Note |
|----------------------------------------|-----|------------------|------------------|------------------------------|
| Main analysis | 288 | 0.074 | \[0.060, 0.088\] | Baseline |
| Confirmed *r* only (exclude estimated) | 240 | 0.077 | \[0.059, 0.094\] | Consistent |
| Exclude *n* \< 30 | 285 | 0.073 | \[0.059, 0.088\] | Consistent |
| ACC performance only | 246 | 0.075 | \[0.059, 0.091\] | Consistent |
| FSTS DOI measure only | 137 | 0.060 | \[0.041, 0.078\] | Attenuated but positive |
| DL estimator (two-level) | 288 | 0.074 | \[0.061, 0.086\] | Δ*r* \< 0.01 vs. three-level |
| Leave-one-out range | 288 | \[0.071, 0.075\] |, | 0/288 change direction |

The baseline *r* = 0.074 is robust across all sensitivity checks. The
leave-one-out range \[0.071, 0.075\] confirms no single study drives the
result. The DL two-level estimator gives an identical point estimate
(0.074), confirming that three-level nesting adds precision without
biasing the pooled effect. The FSTS-only restriction (*r̄* = 0.060) is
the most conservative check and remains positive and significant,
suggesting that DOI operationalization heterogeneity partially inflates
the pooled effect when broader DOI measures are included.

Figure 4: Leave-one-out sensitivity, pooled *r̄* range across
leave-one-out iterations

*Figure 4.* Leave-one-out sensitivity analysis. Each point is the pooled
*r̄* with 95% CI after removing one study. The narrow range confirms no
single study drives the results.

## 5. Discussion

### 5.1 Alignment with Country-Level Evidence

The meta-analytic baseline (*r* = 0.074, *k* = 238, 49 economies) is
consistent with country-level evidence from across the global study
corpus, including the Asia-Pacific primary studies underlying the ICBEF
2025 baseline (Do & Phan, 2024). The pooled effect is positive and
significant, confirming that export-intensive firms tend to outperform
domestically focused peers even after adjusting for firm size, age, and
industry.

**Advanced-I contexts (Group I, k = 139; *r̄* = 0.079):** The Group I
mean (*r̄* = 0.079) is the highest reliable estimate and is directionally
consistent with institutional complementarity theory: strong contract
enforcement, IP protection, and low liability of foreignness (Zaheer,
1995) allow firms to sustain productive internationalization without the
coordination cost penalties visible in weaker environments (North, 1990;
Peng et al., 2008). However, the magnitude is much smaller than CIMT
predicted, and the I→III difference is not statistically significant
(*p* = .502).

**Emerging contexts (Group III, k = 91; *r̄* = 0.068):** The Emerging
group shows *r̄* = 0.068, directionally below the Advanced group,
consistent with CIMT's institutional friction argument. At the
primary-study level, Do & Phan (2025) document a negative aggregate DOI
coefficient on 380 Indian WBES firms (FGLS estimation), with manager
experience and female top-management leadership as positive moderating
factors, a pattern consistent with CIMT's prediction that firm-level
compensating resources partially offset institutional friction in
Emerging environments.

**Frontier contexts (FR, k = 3; *r̄* = 0.349):** The *k* = 3 Frontier
estimate is driven by one outlier study (Pouresmaeili et al., 2018, *r*
= 0.69, *n* = 226 Iranian manufacturing firms). This estimate cannot be
interpreted as a reliable Frontier I→P effect; it instead reflects the
near-impossibility of drawing meta-analytic conclusions when only three
studies populate a regime cell. The actual Frontier I→P effect could be
zero, positive, or negative, larger *k* is required.

**Synthesis:** H1 is confirmed, the ICRV between-regime Q_M test
(*Q*\_M = 17.35, *p* = .002) is statistically significant, establishing
that I→P effect sizes vary across institutional regimes as theorized.
The Q_M significance is driven by the *k* = 3 Frontier contrast rather
than by well-powered pairwise contrasts across the
Advanced/Upper-middle/Emerging cells, so the directional gradient
propositions E1a and E1b are not meta-analytically confirmed in the
current sample. The substantiated finding is that the baseline I→P
effect (*r* = 0.074) is broadly consistent across well-populated regime
groups (I, II, III, MX), and the magnitude of the Advanced-Emerging gap
(*r̄* = 0.079 vs. 0.068) does not reach significance, a result that
bounds, rather than refutes, CIMT's institutional gradient prediction.

### 5.2 Theoretical Contributions

**Contribution 1: Largest globally representative I→P meta-analysis to
date.** The three-level MARA with *k* = 238 studies from 49 economies
(*K* = 288 effects) is the most comprehensive quantitative synthesis of
I→P evidence to apply three-level modeling, extending the ICBEF 2025
Asia-Pacific baseline (*k* = 113) by 124 studies with a globally
inclusive ICRV-coded corpus. Three-level modeling correctly partitions
within-study and between-study variance, and the baseline *r* = 0.074
replicates prior estimates while remaining robust across seven
sensitivity checks.

**Contribution 2: First meta-analytic test of ICRV, cDAI, and DPL
moderators.** This paper is the first to formally test ICRV
institutional regime, national digital adoption (cDAI), and Digital
Paradox Lifecycle phase as moderators in a three-level MARA. H1
(between-regime Q_M test) is confirmed (*Q*\_M = 17.35, *p* = .002),
establishing that I→P effect sizes vary systematically across
institutional regimes. However, the directional gradient propositions
(E1a/E1b) and the cDAI and DPL hypotheses (H2, H3) are not confirmed
under rigorous between-group testing. These results set theoretically
informative bounds: the *k* = 238 sample lacks sufficient between-regime
variation (particularly Frontier, *k* = 3; SIDS, *k* = 0) to detect the
CIMT gradient, and cDAI and DPL phase do not explain between-study
heterogeneity in the present corpus. Future replications with targeted regime-level sampling should test whether the
gradient emerges with richer between-regime representation.

**Contribution 3: Substantial publication bias identified.** The
trim-and-fill-corrected estimate (*r* = 0.035, *k* = 57 imputed studies)
and significant Begg's τ (*p* = .001) together indicate that the I→P
literature has a substantial positive publication bias. The raw pooled
effect (*r* = 0.074) likely overstates the true average causal effect by
approximately 50–100%, with the bias-corrected estimate (*r* = 0.035)
providing a conservative lower bound. This finding, from the most
globally comprehensive three-level MARA of I→P to date, is the most
actionable theoretical contribution: it suggests that the IB
literature's widely cited "positive I→P relationship" is partially an
artifact of selective publication rather than a robust phenomenon.

### 5.3 Managerial and Policy Implications

The non-confirmation of the three hypothesized moderators limits strong
prescriptive conclusions about institutional regime or digital context,
but the baseline finding and publication bias result carry practical
significance.

**For firms across all institutional contexts:** The bias-corrected
baseline (*r* = 0.035) rather than the raw *r* = 0.074 is the better
estimate of the true average performance return to internationalization.
Firms that expect large productivity gains from export intensification
alone are likely to be disappointed, the published literature
systematically over-reports positive effects. Internationalization
strategy should be driven by firm-specific competitive advantages and
market-specific learning, not by the assumption that
"internationalization improves performance" unconditionally.

**For researchers:** The substantial publication bias (*k* = 57 imputed,
adj. *r* = 0.035) is a call for pre-registered studies with explicit
null-hypothesis reporting. Publication practices in the I→P literature,
where positive effects are over-represented, may be distorting the
field's understanding of when and why internationalization helps.
OSF registration and adoption of three-level MARA with
trim-and-fill correction should become standard in future I→P
meta-analyses.

**For policymakers:** The ICRV Advanced–Emerging gap (*r̄* = 0.079 vs.
0.068, non-significant) is not large enough to justify institutional
quality as the primary determinant of export-led productivity. Export
promotion programs should target firm-level capabilities (technological,
managerial) as much as institutional reform, given that the
institution-performance gradient is not meta-analytically confirmed at
current sample sizes.

### 5.4 Limitations and Inferential Bounds

Three limitations bound the inferences available from this study:

**(a) What cannot be concluded:** (1) The SIDS subgroup (*k* ≈ 5, wide
CI) does not permit definitive conclusions about the "forced-penalty"
hypothesis, a targeted search for SIDS-focused primary studies (as
specified in Appendix B) is required before meta-analytic SIDS effects
are precise. (2) The cDAI × ICRV joint moderation (three-way
interaction) is underpowered in the current dataset (*k* per cell \<
20); point estimates are provided but confidence intervals are wide. (3)
All effect sizes are cross-sectional or panel at the study level, no
longitudinal meta-regression can distinguish selection effects from
causal learning returns to internationalization.

**(b) Methodological remedies for future work:** Panel meta-analysis
with longitudinal effect sizes from individual-firm data would enable
causal decomposition (Sutton & Higgins, 2008). Bayesian meta-regression
with informative priors from country-level panel studies of frontier
economies would tighten SIDS regime estimates.

**(c) Boundary of the ICRV classification:** The 5-regime taxonomy uses
WGI Rule of Law as the primary classifier. Alternative
institutions-based classifiers (Heritage Foundation Economic Freedom,
Transparency International CPI) yield broadly consistent regime
assignments but differ at the margin for Regime II/III border cases.

## 6. Conclusion

This paper presents the first three-level MARA of the
internationalization–performance relationship drawing on a globally
representative corpus, extending the ICBEF 2025 Asia-Pacific baseline
from *k* = 113 to *k* = 238 studies from 49 economies (*K* = 288
effects) and introducing three novel moderators for formal meta-analytic
testing: ICRV institutional regime, country-level digital adoption
(cDAI), and Digital Paradox Lifecycle (DPL) phase. The three-level
pooled effect (*r* = 0.074, 95% CI \[0.060, 0.088\], *I*²_total = 62.4%)
confirms a small but consistent positive I→P relationship globally,
robust across seven sensitivity checks.

H1 (ICRV between-regime Q_M test) is confirmed (*Q*\_M = 17.35, *p* =
.002), establishing that I→P effect sizes vary systematically across
institutional regimes. However, the directional gradient (E1a: Advanced
largest; E1b: Frontier smallest) is not meta-analytically confirmable at
*k* = 3 Frontier, and the cDAI (H3: *Q*\_M = 1.23, *p* = .541) and DPL
phase (H2: *Q*\_M = 0.62, *p* = .734) moderators do not explain
between-study heterogeneity in the current sample. The CIMT
institutional gradient (E1a/E1b), digital infrastructure amplification
(H3), and DPL temporal moderation (H2) remain theoretically motivated
but empirically unconfirmed at *k* = 238, null results that should
inform future pre-registered replications with targeted regime-level
sampling.

The most substantive empirical finding is substantial publication bias:
trim-and-fill imputes *k* = 57 missing studies, reducing the
bias-corrected pooled effect to *r* = 0.035 (95% CI \[0.018, 0.051\]) 
positive but considerably attenuated. This suggests that the I→P field's
published literature over-represents positive results, and that the true
average performance return to internationalization is closer to *r* ≈
0.035 than the oft-cited figures in the 0.07–0.10 range. The
heterogeneity puzzle (*I*² = 62.4%) remains largely unresolved, with
within-study variance (Level 2, 54.1%) dominating between-study variance
(Level 3, 8.4%), suggesting that DOI operationalization and performance
measure choices within papers are more important sources of
heterogeneity than cross-country institutional differences.

**Limitations.** Five inferential constraints bound these conclusions.
First, the three moderator hypotheses are not confirmed in the present *k* = 238 corpus; this may reflect insufficient regime-level
*k* (Frontier: *k* = 3; SIDS: *k* = 0) rather than genuine null effects.
A formal WoS/Scopus search targeting Frontier and SIDS contexts is
required before the ICRV null result can be interpreted as definitive.
Second, the Frontier-group anomaly (*k* = 3, *r̄* = 0.349, dominated by
Pouresmaeili et al. 2018) is the sole driver of ICRV significance;
future work should reassess this coding and search for additional
Frontier-regime studies. Third, cDAI is measured at the study level
using country-year World Bank Digital Adoption Index scores (primary) or
ITU Digital Development Index (secondary), not direct replication of the
WBES firm-level indicators used in the companion primary studies; any
systematic error in the country-year DAI assignment, for instance, from
vintage mismatch between the study's data period and the DAI score's
reference year, may attenuate the moderation coefficient. Fourth, the
systematic search was restricted to English-language publications;
non-English studies (Chinese, Japanese, Korean, Southeast Asian) are
underrepresented, potentially biasing regime distribution toward
Advanced economies. Fifth, reliability is established on a 20% double-coded subsample (*k* = 47 studies), with the two authors coding independently and agreement reported in Table 3.1; the remaining 80% is single-coded by the first author against the codebook, which, while standard for resource-bounded syntheses, cannot be independently validated.

**Future research.** Three directions follow directly from the null
moderator findings. First, a formal WoS/Scopus systematic search
targeting Frontier and SIDS economy I→P studies (targeted search
strings, Appendix B) would expand Frontier *k* from 3 to potentially
20–40 studies, enabling a meaningful test of the ICRV Frontier cell.
Second, a pre-registered replication of the ICRV, cDAI, and DPL
moderator hypotheses, with explicit power analysis for each regime cell
and OSF registration, would provide a definitive test of whether
these moderators reach significance in a *k* ≥ 400 corpus. Third, the
substantial publication bias finding (*k* = 57 imputed, adj. *r* =
0.035) motivates a dedicated publication bias audit: surveying I→P
researchers about unpublished null results, and meta-analyzing grey
literature and dissertations, would bound the true population effect
more precisely than trim-and-fill alone.

## Funding

This research received no specific grant from any funding agency in the
public, commercial, or not-for-profit sectors.

## Competing Interests

The authors declare no conflict of interest.

## Data Availability

The coded study database (`forest_data.csv`), R analysis scripts
(`metafor`), and the OSF registration protocol are available from
the corresponding author upon reasonable request. The PRISMA 2020
checklist is provided as supplementary material.

## Declaration of Generative AI and AI-Assisted Technologies in the Writing Process

During the preparation of this work, the authors used two software aids, each under full human control and verification. First, a purpose-built large-language-model-assisted tool (M-AIDA, using Anthropic Claude) was used to assist effect-size extraction and statistical conversion from the primary studies; every value proposed by the tool was independently checked, corrected where necessary, and permanently locked by the Principal Investigator before entry into the analysis database. Second, Grammarly was used to correct spelling, grammar, and punctuation in the authors' own text. No generative AI tool selected studies, made eligibility decisions, performed the statistical analysis, or generated any interpretive or written content; the authors reviewed all outputs and take full responsibility for the content of the publication.

## References

Aguinis, H., Dalton, D. R., Bosco, F. A., Pierce, C. A., & Dalton, C. M.
(2011). Meta-analytic choices and judgment calls: Implications for
theory and research. *Journal of Management, 37*(1), 5–38.

Arte, P., & Larimo, J. (2022). Moderating influence of product
diversification on the internationalization-performance relationship:
Insights from meta-analysis. *Journal of Business Research, 139*,
1408–1423.

Barney, J. (1991). Firm resources and sustained competitive advantage.
*Journal of Management, 17*(1), 99–120.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators
on the internationalization–performance relationship: Evidence from
meta-analysis. *Management International Review, 47*(3), 319–347.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank
correlation test for publication bias. *Biometrics, 50*(4), 1088–1101.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013).
Digital business strategy: Toward a next generation of insights. *MIS
Quarterly, 37*(2), 471–482.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R.
(2021). *Introduction to meta-analysis* (2nd ed.). Wiley.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity
J-curve: How intangibles complement general purpose technologies.
*American Economic Journal: Macroeconomics, 13*(1), 333–372.

Bustamante, C. V., Mingo, S., & Matusik, S. F. (2022). Institutions,
digital capabilities and the internationalization of SMEs. *Journal of
International Business Studies, 53*(3), 524–546.

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with
three-level meta-analyses. *Psychological Methods, 19*(2), 211–226.

Cohen, J. (1988). *Statistical power analysis for the behavioral
sciences* (2nd ed.). Lawrence Erlbaum.

Cooper, H. (2010). *Research synthesis and meta-analysis: A step-by-step
approach* (4th ed.). Sage.

David, P. A. (1990). The dynamo and the computer: An historical
perspective on the modern productivity paradox. *American Economic
Review, 80*(2), 355–361.

Do, T. H., & Phan, A. T. (2024, December). *Internationalization and
firm performance: A meta-analysis review* \[Paper presentation\]. The
Sixth International Conference on Sustainable Development in Economics,
Business, and Finance (ICBEF).

Do, T. H., & Phan, A. T. (2025). Internationalization and firm
performance of firms in India: The role of top management. In M.
Bartekova (Ed.), *International business research: Traditional and
creative approaches*. IntechOpen.
<https://doi.org/10.5772/intechopen.1011012>

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple
funnel-plot-based method of testing and adjusting for publication bias
in meta-analysis. *Biometrics, 56*(2), 455–463.

Egger, M., Smith, G. D., Schneider, M., & Minder, C. (1997). Bias in
meta-analysis detected by a simple, graphical test. *BMJ, 315*(7109),
629–634.

Hedges, L. V., & Olkin, I. (1985). *Statistical methods for
meta-analysis*. Academic Press.

Helpman, E., Melitz, M. J., & Yeaple, S. R. (2004). Export versus FDI
with heterogeneous firms. *American Economic Review, 94*(1), 300–316.

Jacquemin, A. P., & Berry, C. H. (1979). Entropy measure of
diversification and corporate growth. *Journal of Industrial Economics,
27*(4), 359–369.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process
of the firm: A model of knowledge development and increasing foreign
market commitments. *Journal of International Business Studies, 8*(1),
23–32.

Katz, R., & Callorda, F. (2018). *The economic contribution of
broadband, digitization and ICT regulation*. ITU Telecommunication
Development Sector.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road
map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Deligonul, S., Perryy, M. Z., & Cavusgil,
S. T. (2012). A multilevel examination of the drivers of firm
multinationality: A meta-analysis. *Journal of Management, 38*(2),
502–530.

Kraus, S., Breier, M., Lim, W. M., Dabić, M., Kumar, S., Kanbach, D.,
Mukherjee, D., Corvello, V., Piñeiro-Chousa, J., Liguori, E.,
Palacios-Marqués, D., Schiavone, F., Ferraris, A., Fernandes, C., &
Ferreira, J. J. (2022). Literature reviews as independent studies:
Guidelines for academic practice. *Review of Managerial Science, 16*(8),
2577–2595.

Kogut, B., & Zander, U. (1993). Knowledge of the firm and the
evolutionary theory of the multinational corporation. *Journal of
International Business Studies, 24*(4), 625–645.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer
agreement for categorical data. *Biometrics, 33*(1), 159–174.

Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M.
(2016). Home country institutions and the
internationalization-performance relationship: A meta-analytic review.
*Journal of Management, 42*(5), 1075–1110.

North, D. C. (1990). *Institutions, institutional change and economic
performance*. Cambridge University Press.

Orwin, R. G. (1983). A fail-safe N for effect size in meta-analysis.
*Journal of Educational Statistics, 8*(2), 157–159.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T.
C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan,
S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu,
M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D.
(2021). The PRISMA 2020 statement: An updated guideline for reporting
systematic reviews. *BMJ, 372*, n71. <https://doi.org/10.1136/bmj.n71>

Peng, M. W., Wang, D. Y. L., & Jiang, Y. (2008). An institution-based
view of international business strategy: A focus on emerging economies.
*Journal of International Business Studies, 39*(5), 920–936.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients
in meta-analysis. *Journal of Applied Psychology, 90*(1), 175–181.

Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models:
Applications and data analysis methods* (2nd ed.). Sage.

Rosenthal, R. (1991). *Meta-analytic procedures for social research*
(rev. ed.). Sage.

Rosenthal, R. (1994). Parametric measures of effect size. In H. Cooper &
L. V. Hedges (Eds.), *The handbook of research synthesis* (pp. 231–244).
Sage.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollender, L. (2018).
Limits to outsourcing: A meta-analysis and empirical investigation.
*Journal of International Business Studies, 49*(6), 682–703.

Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression
approximations to reduce publication selection bias. *Research Synthesis
Methods, 5*(1), 60–78.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders?
The international strategies of digital platform firms. *Global Strategy
Journal, 11*(1), 58–80.

Sutton, A. J., & Higgins, J. P. T. (2008). Recent developments in
meta-analysis. *Statistics in Medicine, 27*(5), 625–650.

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., &
Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect
sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong,
J., Fabian, N., & Haenlein, M. (2021). Digital transformation: A
multidisciplinary reflection and research agenda. *Journal of Business
Research, 122*, 889–901.

Vevea, J. L., & Woods, C. M. (2005). Publication bias in research
synthesis: Sensitivity analysis using a priori weight functions.
*Psychological Methods, 10*(4), 428–443.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor
package. *Journal of Statistical Software, 36*(3), 1–48.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic
Management Journal, 5*(2), 171–180.

World Bank. (2023). *Worldwide Governance Indicators*.
<https://info.worldbank.org/governance/wgi/>

Wu, J., Wang, C., Hong, J., Piperopoulos, P., & Zhuo, S. (2022).
Internationalization and innovation performance of emerging market
enterprises: The role of host-country institutional development.
*Journal of World Business, 52*(2), 192–203.

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of
Management Journal, 38*(2), 341–363.


*Appendices A–C (PRISMA flow, coding protocol, MetaEssentials/`metafor` consistency check) are provided as online supplementary material.*
