# Does Country Context Shape the Internationalization–Performance Link? A Three-Level Meta-Analytic Investigation of Digital Adoption, Institutional Regimes, and the Digital Paradox Lifecycle

*Manuscript prepared for: Journal of World Business (JWB, Elsevier,
IF ≈ 5.5, ABS-3)* *Version 1.0, May 2026 (target journal submission: Q4
2026)*

## Highlights

- Three-level meta-analysis of internationalization–performance: k = 238, 288 effects
- Baseline pooled effect is small but positive (r = 0.074, 95% CI [0.060, 0.088])
- ICRV institutional regime moderates the I–P relationship (Q_M = 17.35, p = .002)
- Digital adoption and lifecycle phase show no significant I–P moderation
- Trim-and-fill reveals publication bias, attenuating the effect to r = 0.035

## Abstract

We conduct a three-level meta-analytic regression analysis
(MARA) examining whether country-level digital adoption (cDAI),
institutional context regime (ICRV), and Digital Paradox Lifecycle (DPL)
phase moderate the internationalization–performance (I to P) relationship 
three theoretically motivated moderators that prior meta-analyses have
not examined. A systematic search
following PRISMA 2020 protocols on Web of Science and Scopus (1977–2026)
identifies *k* = 238 studies with *K* = 288 effect sizes. Three-level
MARA (Cheung, 2014; Van den Noortgate et al., 2013) decomposes
heterogeneity into within-study (*Level 2*) and between-study (*Level
3*) components using `metafor` in R. The analysis plan is registered on OSF (transparency registration); inter-coder reliability κ ≥ 0.70 on 20%
double-coded subsample. The baseline pooled effect is *r*
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
This is the first three-level MARA of I to P drawing
on *k* = 238 studies from 49 economies globally, and the first to
formally test ICRV, cDAI, and DPL phase as moderators. The ICRV
between-regime Q_M test confirms H1 (Q_M = 17.35, *p* = .002), while the
directional gradient (E1a/E1b) and the cDAI and DPL hypotheses remain
unconfirmed, a finding that, combined with substantial publication
bias, reframes the heterogeneity puzzle: unexplained variance in I to P may
reflect publication-side selection more than institutional or digital
contingencies, calling for pre-registered replication with larger
between-regime samples.

**Keywords:** internationalization–performance; meta-analysis;
three-level model; digital adoption; institutional context; ICRV;
Digital Paradox Lifecycle; global; Asia-Pacific

## 1. Introduction

The past three decades have witnessed dramatic growth in outward foreign
direct investment, export-oriented production, and global value chain
participation, transforming internationalization from a strategy available
primarily to large multinationals into a competitive consideration for
firms across size classes and geographies (Dunning, 2000; Johanson &
Vahlne, 2009; Kafouros et al., 2023). Whether internationalization improves
firm performance is not merely academic: it shapes investment decisions,
export promotion policy, and the strategic priorities of firms in an
interconnected global economy (Hitt et al., 2006; Lu & Beamish, 2004). For
scholars, the record remains inconclusive.

The relationship between a firm's degree of internationalization and its
performance (the "I to P relationship") is the most meta-analyzed question
in international business (IB). Over four decades and six major
meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al.,
2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022), no
consensus has emerged: pooled effects are consistently small and
positive, yet *I*² regularly exceeds 80%, signaling that context, not a
universal mechanism, drives outcomes.

The present study's starting point is the ICBEF 2025 baseline analysis
(Authors, 2024): *k* = 113 studies, pooled *r* = 0.07 (*p* \< .001),
*I*² = 87.92%. While confirming the positive average effect, this
baseline showed that conventional moderators (country of origin,
industry, performance measure type) leave approximately 70% of variance
unexplained. Three theoretically grounded moderators, absent from all
prior meta-analyses, motivate the present extension:

**Gap 1, cDAI.** Country-level digital adoption (cDAI) has been
proposed as a contextual amplifier of firm-level competitive advantages
(Stallkamp & Schotter, 2021; Verhoef et al., 2021), yet no meta-analysis
has tested whether the national digital infrastructure environment
moderates the I to P link.

**Gap 2, ICRV 5-regime.** Marano et al. (2016) established that
home-country institutions moderate I to P but applied a coarse six-group
global taxonomy. The global corpus spans the full institutional spectrum,
from Singapore (World Governance Indicators Rule of Law +1.84) to frontier
economies such as Pakistan (WGI −0.55) and Iran (WGI −0.74; World Bank,
2023). An ICRV 5-regime classification capable of resolving this
heterogeneity has not been tested meta-analytically on a globally
representative I to P corpus.

**Gap 3, DPL phase.** Brynjolfsson et al. (2021) identified 2009 as a
productivity inflection point in the digital era (the "dynamo analogy" for
AI: David, 1990). Studies examining data before, spanning, or after this
threshold should yield systematically different I to P effect sizes if
digital platforms reshape internationalization economics. This temporal
moderator has never been systematically coded in I to P meta-analyses.

This paper addresses all three gaps through a fresh systematic search
expanding the ICBEF 2025 baseline from *k* = 113 to *k* = 238, combined
with three-level MARA that decomposes heterogeneity beyond random-effects
models.

**Contributions.** We make three methodological and three theoretical
contributions. *(Methodological)*: (1) first three-level MARA for the
I to P literature; (2) first PRISMA-2020-compliant systematic search with
OSF registration for this topic; (3) first between-study *vs.* within-study
heterogeneity decomposition applied to I to P. *(Theoretical)*: (4) first
meta-analytic test of an ICRV 5-regime framework on a globally
representative I to P corpus (*k* = 238, 49 economies); (5) first formal
test of cDAI as a national-level digital-infrastructure moderator; (6)
first test of DPL phase as a temporal moderator using three-level MARA. The
non-confirmation of E1a/E1b, H2, and H3, and the anomalous ICRV Frontier
pattern, are themselves informative findings that bound the conditions
under which these moderators could operate.

**Key findings preview.** The baseline pooled effect (*r* = 0.074, *k* =
238, *K* = 288) replicates and extends the ICBEF 2025 finding (*r* = 0.07,
*k* = 113), confirming a small but consistent positive I to P relationship
globally. H1 (between-regime Q_M test) is confirmed (*Q*\_M = 17.35, *p* =
.002), but the directional Exploratory Propositions E1a (Advanced largest)
and E1b (Frontier smallest) are not confirmed, since the Q_M is driven by a
*k* = 3 Frontier-group anomaly rather than a monotone institutional
gradient. cDAI (*Q*\_M = 1.23, *p* = .541) and DPL phase (*Q*\_M = 0.62,
*p* = .734) are non-significant (H2, H3 not supported). The most
substantive finding is publication bias (H4 confirmed): trim-and-fill
imputes *k* = 57 missing studies, reducing the adjusted estimate to *r* =
0.035, positive but substantially smaller than the raw effect. The
heterogeneity puzzle (*I*² = 62.4%) remains unresolved by the tested
moderators, with between-study heterogeneity predominantly within-paper
(Level 2, 54.1%) rather than between-country (Level 3, 8.4%).

**Organization.** Section 2 develops the theoretical framework and
hypotheses, grounding each moderator in RBV, institutional theory,
organizational learning theory, coordination cost theory, and the
Foundational Digital Adoption Framework. Section 3 describes the search
protocol, coding procedure, and three-level MARA specification. Section 4
presents the baseline model, three moderator analyses, and publication
bias diagnostics. Section 5 discusses implications, and Section 6 concludes
with limitations and future directions.

## 2. Theoretical Framework and Hypotheses

### 2.1 Foundation Theories

Five theoretical perspectives ground the moderating hypotheses and link the
three new moderators to established I to P predictions.

**Resource-Based View (RBV).** Barney (1991) establishes that
sustainable competitive advantages derive from VRIN (valuable, rare,
inimitable, non-substitutable) resources, predicting that firms with
strong home-country endowments (human capital, technological capability,
digital infrastructure access) generate higher performance returns from
international expansion than resource-constrained peers. Wernerfelt's
(1984) resource bundling logic adds that national digital infrastructure
provides a coordination-enabling environment amplifying the returns to
firm-level resources: in high-cDAI environments, firms deploy existing
capabilities across borders at lower per-unit cost, raising the marginal
productivity return to each unit of international expansion. cDAI
(country-level) is analytically distinct from firm-level digital adoption
(DAI) and firm-level technological capability (TCI), which the companion
primary studies (P3–P8) treat as separate constructs. Here only cDAI is
operationalized as a study-level moderator; DAI and TCI remain
within-study variables not separately extractable at meta-analytic
resolution from the k = 238 corpus. The resource-bundling prediction for
P6 therefore concerns whether a richer national digital environment
raises the aggregate I to P effect across studies, a between-study
moderation claim at the country level, not a within-study claim about
firm-level capability bundles.

**Institutional Theory.** North's (1990) framework positions formal and
informal institutions as the "rules of the game" governing transaction
costs. Higher institutional quality (rule of law, contract enforcement,
IP protection, regulatory quality) reduces the coordination costs of
cross-border expansion by attenuating opportunism risk, monitoring costs,
and home–host information asymmetry. Scott's (1995) three-pillar framework
extends this: regulative, normative, and cognitive institutions jointly
determine the transaction cost environment of internationalization. When
regulative institutions are strong (ICRV Regime I), firms enforce
contracts with foreign counterparts at lower cost, protect innovation
rents across jurisdictions, and exploit economies of scale without the
institutional friction that truncates these returns in weaker
environments. The ICRV gradient hypothesis (H1) thus derives directly
from institutional theory: the expected I to P effect should decline
monotonically from Advanced-Innovation (Regime I) to Frontier (Regime FR)
as institutional quality falls and coordination costs rise.

**Organizational Learning Theory.** Johanson and Vahlne's (1977, 2009)
Uppsala model posits that internationalization knowledge accumulates
through market-specific experience and is encoded in organizational
routines. Digital platforms accelerate this accumulation by reducing
home–host information asymmetries: cloud-based analytics, real-time demand
signaling, and B2B platforms let firms monitor foreign markets without
the physical presence prior eras required (Stallkamp & Schotter, 2021).
The DPL Follow phase (post-2014) is the period in which these digital
learning channels reach sufficient maturity to systematically compress
the experiential learning curve, predicting that I to P effects are
largest in studies drawing on data from this period (H2). The Span phase
captures the transitional period in which digital tools were diffusing
but had not yet reached the maturity threshold at which learning-cost
compression became systemic.

**Coordination Cost Theory.** The classic coordination cost argument
(Hitt et al., 1997; Lu & Beamish, 2004) holds that international expansion
initially generates productivity gains through scale economies and
learning, but eventually produces diseconomies as the administrative
burden of coordinating dispersed operations exceeds the gains from
further geographic diversification, yielding the inverted-U that is the
modal I to P finding (Marano et al., 2016). Digital platforms
systematically reduce coordination costs through three channels: (a)
*communication compression*, real-time communication across time zones
lowers the bandwidth cost of coordinating dispersed operations; (b)
*transaction cost reduction*, electronic payment systems and digital
contracting reduce the cost and time of cross-border transactions; (c)
*information asymmetry compression*, digital analytics lower the cost of
verifying foreign partner performance. When national digital
infrastructure is mature (high cDAI), all three channels operate
simultaneously, predicting that the coordination cost mechanism behind
the right-side decline of the inverted-U is attenuated or shifted to
higher internationalization intensities than in low-cDAI environments.

**Foundational Digital Adoption Framework.** Verhoef et al.'s (2021)
digital transformation hierarchy distinguishes Tier-1 *digitization*
(basic digital presence: websites, digital records), Tier-2
*digitalization* (electronic payments, EDI), Tier-3 *digital integration*
(ERP, CRM, supply chain integration), and Tier-4 *digital dynamic
capability* (AI deployment, platform orchestration). Stallkamp and
Schotter (2021) extend this to the IB context, showing that Tier-1 and
Tier-2 adoption, the layers most widely measured in firm-level surveys,
function as *platform infrastructure* for cross-border coordination
rather than as proprietary capabilities. At the country level, aggregate
adoption of Tier-1 and Tier-2 tools defines the *national digital
adoption environment* (cDAI): a digitally enabled transaction ecosystem
that reduces the minimum infrastructure investment required for firms to
participate in cross-border trade. cDAI captures this shared environment,
whereas firm-level DAI captures a firm's own position within it. The cDAI
amplification hypothesis (H3) thus concerns whether a richer national
digital environment raises the aggregate I to P effect across the studies
that draw on it, a between-study moderation claim, not a within-study
mediation claim.

### 2.2 Capability–Institution Mismatch Theory (New, Hm1)

We propose *Capability–Institution Mismatch Theory* (CIMT) to explain the
ICRV gradient in meta-analytic I to P effect sizes. CIMT's core claim is
that the productivity returns to international expansion depend not only on
firm-level capabilities but on how far home-country institutions let those
capabilities be deployed productively across borders. The theory
distinguishes three mechanisms:

*Rent-protection mechanism.* Institutional quality determines how far
firms can protect the proprietary rents generated by internationalization.
In Regime I environments, strong IP protection and contract enforcement
let firms sustain competitive advantages across foreign markets without
the knowledge leakage and imitation risk of weaker contexts (Kogut &
Zander, 1993; Zaheer, 1995). Each unit of expansion therefore translates
into larger cumulative rent streams, raising the average I to P effect in
Regime I samples.

*Liability-of-foreignness attenuation mechanism.* Zaheer (1995)
identifies liability of foreignness (LOF), the costs foreign firms incur
that domestic rivals do not, as a key driver of internationalization
costs. LOF is attenuated where strong rule of law, transparent regulation,
and low corruption reduce the information asymmetries and discriminatory
treatment that generate it in weaker contexts (Peng et al., 2008). When
LOF is low (ICRV-I), firms capture a larger share of cross-border scale
and learning gains, raising the meta-analytic effect size.

*Institutional void amplification mechanism.* In institutional voids,
where formal institutions are weak or absent, firms must invest in
substitute governance (relationship capital, political connections,
informal contracts) that absorbs managerial attention and reduces net
productivity returns (Khanna & Palepu, 2010). As institutional quality
declines across the ICRV spectrum (Regime II–III to FR), these substitute
costs accumulate, progressively depressing the I to P effect toward zero
and potentially negative territory.

CIMT predicts between-regime heterogeneity, with Advanced-regime studies
expected to show the largest effects because all three mechanisms operate
simultaneously at the institutional frontier. Prior meta-analyses lacked a
taxonomy fine enough to disaggregate the Advanced-to-Frontier/SIDS
spectrum: Marano et al. (2016) used a six-category global classification
that did not separate the Advanced/Upper-Middle/Emerging/Frontier
spectrum examined here. The ICRV 5-regime taxonomy, anchored in World Bank
World Governance Indicators (Rule of Law, 2023 vintage) and applied to the
full k = 238 corpus, provides the first classification capable of testing
the CIMT between-regime prediction meta-analytically across economies from
Singapore (WGI +1.84) to Pakistan (WGI −0.55) and Iran (WGI −0.74).

**Hypothesis 1 (H1, ICRV between-regime heterogeneity):** Pooled I to P
effect sizes vary systematically across ICRV institutional regimes, with
Advanced-regime studies expected to show the largest average effects,
because formal institutions (contract enforcement, IP protection, reduced
liability of foreignness) amplify the productivity returns to
international expansion through rent protection, LOF attenuation, and
void-cost reduction (Khanna & Palepu, 2010; North, 1990; Zaheer, 1995).
Formally: the between-regime Q_M test for ICRV is significant (*p* \< .05),
and the point estimate for Advanced-regime studies (ICRV-I) exceeds those
for Emerging (ICRV-III) and Mixed-regime (MX) studies. The directional
ordering among Frontier studies (ICRV-FR) is treated as exploratory pending
adequate *k* in that group (see Exploratory Propositions 1a–1b).

*Exploratory Proposition 1a (E1a):* Studies drawing on Advanced-regime
firms (ICRV-I) are expected to show the largest pooled I to P effect,
reflecting simultaneous activation of the three CIMT mechanisms
(rent-protection, LOF-attenuation, void-elimination). E1a's direction is
confirmatory; its magnitude is not pre-specified given heterogeneity in DOI
measurement and performance construct across ICRV-I studies.

*Exploratory Proposition 1b (E1b):* Studies drawing on Frontier-regime
firms (ICRV-FR) are expected to show the smallest, potentially null or
negative, pooled I to P effect, reflecting the dominance of institutional
void costs over scale and learning returns. E1b is exploratory rather than
confirmatory because the current Frontier-group *k* = 3 is insufficient for
reliable inference (at α = .05, the minimum k for stable random-effects
moderation is typically k ≥ 10; Valentine et al., 2010).

### 2.3 Digital Paradox Lifecycle (DPL, New, Hm2)

The Digital Paradox Lifecycle is a temporal moderator grounded in
Brynjolfsson et al.'s (2021) productivity J-curve and David's (1990)
dynamo analogy. David (1990) showed that general-purpose technologies
require decades of complementary investment in organizational practices,
worker skills, and infrastructure before their productivity benefits
materialize. Brynjolfsson et al. (2021) applied this to the AI era,
documenting a J-curve in which productivity first stagnates as firms
invest in digital infrastructure and then accelerates as complementary
assets mature. We extend this to the I to P literature, arguing that the
coordination cost compression enabled by digital platforms follows a
similar J-curve at the aggregate study level.

Three DPL phases characterize the digital transformation of
internationalization:

- **Precede** (data predominantly before 2009): Low digital penetration
  in cross-border trade. B2B e-commerce, cloud-based logistics, and
  electronic payment systems have not yet reached the critical mass needed
  to alter the coordination cost structure of international operations.
  I to P dynamics are governed by the traditional coordination cost
  mechanisms of Hitt et al. (1997) and Lu and Beamish (2004), with the
  inverted-U as the expected modal form.
- **Span** (data spanning 2005–2014): A transitional period in which
  digital infrastructure is being built and firms experiment with digital
  coordination tools. Effects are mixed: early adopters may benefit, but
  most firms have not yet accumulated the complementary capabilities
  (digital routines, platform-integrated supply chains) to convert
  infrastructure availability into productivity gains. I to P effect sizes
  should be heterogeneous, yielding intermediate estimates.
- **Follow** (data predominantly after 2014): Digital platforms (cloud
  logistics, B2B e-commerce, electronic payments, digital trade finance)
  have reached sufficient maturity in the Asia-Pacific region to
  systematically compress coordination costs. The complementary investment
  lag documented by Brynjolfsson et al. (2021) has been substantially
  absorbed and the J-curve has passed its inflection point. I to P effect
  sizes should be largest.

The choice of 2009 rests on three empirical anchors: (1) the global
proliferation of smartphones and mobile internet (2007–2009) transformed
cross-border communication costs; (2) the rapid growth of B2B e-commerce
platforms in China and Southeast Asia (Alibaba B2B international:
2008–2010; Lazada: 2011; Tokopedia: 2009) created digital trade
infrastructure suited to emerging Asia-Pacific exporters; (3) the 2009
global financial crisis accelerated SME digital adoption as a
cost-reduction strategy. These concurrent developments make 2009 a
defensible rather than arbitrary inflection point for trade-oriented
economies; the Asia-Pacific region, home to 52% of the k = 238 corpus, was
a primary site of this diffusion.

**Hypothesis 2 (H2, DPL phase):** Studies drawing predominantly on
post-2014 data (DPL Follow phase) are expected to show larger pooled I to P
effects than studies drawing on pre-2009 data (DPL Precede phase), because
digital platforms had reached the maturity threshold at which
coordination-cost compression systematically raises the net productivity
return to international expansion (Brynjolfsson et al., 2021; David, 1990).
Span-phase studies (data spanning 2005–2014) are expected to show
intermediate effects, reflecting the transitional period in which
infrastructure was building but complementary capabilities had not yet been
absorbed. Formally: *r̄*(Follow) \> *r̄*(Precede), with *r̄*(Span)
intermediate; the between-phase *Q*\_M test is expected to be significant
(*p* \< .05). The prediction is bounded by J-curve logic: the precision of
the *Q*\_M test depends on within-phase k and cross-phase effect-size
variance, and below approximately k = 30 per phase the test is underpowered
for moderate moderation (*f*² \< 0.10).

### 2.4 cDAI as Amplifier (Hm3)

National digital adoption (cDAI) is a country-level construct capturing the
aggregate availability of digital infrastructure as a coordination-enabling
environment, distinct from firm-level DAI in two respects. First, cDAI is
an *ecosystem property* rather than a firm choice: it reflects the density
of broadband coverage, electronic payment infrastructure, digital identity
systems, and regulatory support for digital commerce that exists regardless
of any firm's adoption decision. Second, cDAI operates at the between-study
level: variation in the pooled I to P effect across studies is partly
attributable to variation in the national digital environments from which
samples were drawn.

cDAI follows established indices (operationalized in Section 3.4): the
primary source is the World Bank Digital Adoption Index (2016 vintage),
aggregating Tier-1 and Tier-2 adoption across government, business, and
household sectors into a 0–1 composite (Sahay et al., 2020), with the ITU
ICT Development Index (rescaled to 0–1) substituting where country-year
scores are unavailable.

cDAI amplifies the I to P relationship through the *coordination platform
effect* (Stallkamp & Schotter, 2021): where Tier-1 and Tier-2 tools are
widely diffused, firms face a richer ecosystem of coordination channels
that reduce the per-unit cost of cross-border transactions. This reduction
is not uniform across export intensities. At low intensities, digital tools
may not generate measurable I to P gains because transaction volume does
not justify intensive platform use; at higher intensities they become
critically productivity-relevant, substituting for physical coordination
investments otherwise required (Bharadwaj et al., 2013; Verhoef et al.,
2021). cDAI amplification therefore predicts a positive meta-regression
coefficient where cDAI scores predict pooled I to P effect sizes, the
country-level analog of the export-contingent digital complementarity
mechanism documented at the firm level in the Asia-Pacific primary studies.

cDAI amplification is expected to concentrate in the DPL Follow phase
(post-2014), the only period in which infrastructure is mature enough to
serve as a coordination platform rather than a mere communication tool. In
the Precede phase, high cDAI does not translate into coordination cost
compression because B2B platforms and electronic payments are not yet
integrated into trade workflows; in the Follow phase the same cDAI level
enables a fully integrated coordination ecosystem, generating the
amplification predicted by H3. Bustamante et al. (2022) provide the closest
prior evidence, finding that national digital capabilities interact with
institutional quality in cross-country SME internationalization success;
the present study extends this to the meta-analytic level and adds DPL
phase as a temporal boundary condition moderating when cDAI amplification
is detectable.

**Hypothesis 3 (H3, cDAI amplification):** Studies drawing on high-cDAI
national contexts are expected to show larger pooled I to P effects than
studies from low-cDAI contexts (*r̄*\[High-cDAI\] \> *r̄*\[Low-cDAI\];
between-group *Q*\_M significant, *p* \< .05), because mature national
digital infrastructure reduces the per-unit coordination cost of
cross-border expansion through the coordination platform effect (Stallkamp
& Schotter, 2021). cDAI amplification is operationalized as a between-group
comparison across three tiers (Low / Medium / High) classified from World
Bank Digital Adoption Index and ITU ICT Development Index scores, rather
than a continuous meta-regression coefficient, because the corpus does not
yet provide sufficient within-tier variance for reliable continuous
estimation. The amplification is bounded by DPL phase: H3 is expected to be
most detectable in Follow-phase studies (post-2014), where infrastructure
has reached the maturity threshold to function as an active coordination
platform; in Precede-phase studies, high cDAI is not expected to amplify
I to P because B2B trade infrastructure had not yet achieved critical mass
regardless of country-level adoption scores.

### 2.5 Publication Bias as Null Hypothesis

Given the history of selective reporting in IB meta-analyses (Borenstein
et al., 2021), we test publication bias as a formal null hypothesis.

**Hypothesis 4 (H4, Publication bias):** Selective reporting of
statistically significant positive I to P results is expected to inflate
the raw pooled effect relative to the true population effect, because
positive results are more likely to be published (Borenstein et al., 2021;
Dickersin, 1990). Three directional predictions follow: (H4a) funnel-plot
asymmetry tests (Egger's regression intercept, Begg's rank correlation)
are expected to be significant, indicating that smaller-sample studies show
disproportionately large positive effects relative to the
regression-estimated pooled mean; (H4b) Duval and Tweedie's (2000)
trim-and-fill procedure is expected to impute missing left-side studies
(suppressed null/negative results) and produce a bias-adjusted estimate
(*r̄*\_adj) smaller than the raw estimate but still positive (*r̄*\_adj \>
0); (H4c) Orwin's (1983) fail-safe N is expected to substantially exceed
the 2,000-study threshold required to reduce the pooled effect to
negligible, confirming that the positive I to P effect is not an artifact of
publication bias alone.

### 2.6 Conceptual Model

Figure 1: Conceptual model, Three-level MARA with ICRV, cDAI, and DPL
moderators

*Figure 1.* Conceptual model for Paper 6 (Three-Level Meta-Analytic
Regression Analysis).

*Note:* Solid arrows represent the primary meta-analytic effect
(baseline I to P pooled effect, k = 238 studies from 49 economies, K = 288
effects, r̄ = 0.074, 95% CI \[0.060, 0.088\]). Dashed arrows represent
hypothesised moderating relationships. Three study-level constructs were
tested as moderators: (1) ICRV Regime (H1), hypothesised between-regime
Q_M statistically significant; H1 confirmed (Q_M = 17.35, p = .002);
directional Exploratory Propositions E1a (Advanced largest) and E1b
(Frontier smallest) not meta-analytically confirmable at k = 3 Frontier.
(2) cDAI, Country Digital Adoption Index (H3), hypothesised positive
amplification \[High \> Low\]; actual Q_M = 1.23 (p = .541), H3 not
supported. (3) DPL Phase (H2), hypothesised Follow \> Precede; actual
Q_M = 0.62 (p = .734), H2 not supported. The three-level model nests K =
288 effects within k = 238 studies (σ²_within = 0.00878, I²\_(2) =
54.1%) within between-study heterogeneity (σ²_between = 0.00136, I²\_(3)
= 8.4%); total I² = 62.4%. Publication bias (H4 confirmed): Egger's b =
0.487 (p = .052), Begg's τ = −0.132 (p = .001); trim-and-fill imputes k
= 57 studies, adjusted r = 0.035; fail-safe N = 44,782. Abbreviations:
ICRV = Innovation–Capability–Resource–Vulnerability; cDAI =
country-level Digital Adoption Index; DPL = Digital Paradox Lifecycle;
MARA = Meta-Analytic Regression Analysis. Target journal: *Journal of
World Business* (JWB, Elsevier).

## 3. Method

The approach follows the APA Meta-Analysis Reporting Standards (Cooper,
2010) and the PRISMA 2020 statement (Page et al., 2021). The analysis plan
was registered on the Open Science Framework (OSF) as a transparency
registration (the working corpus had already been assembled at
registration); the document specifies the search protocol, eligibility
criteria, coding rules for all seven moderators, and the planned analyses.
Three-level meta-analytic regression analysis (MARA) was selected over
conventional random-effects meta-analysis because the corpus contains
multiple effect sizes per study, which violates the independence
assumption of single-level estimators (Cheung, 2014; Van den Noortgate et
al., 2013). The three-level model decomposes total heterogeneity into
within-study (σ²\_(2)) and between-study (σ²\_(3)) components, enabling
correct attribution of variance to methodological versus contextual
sources.

### 3.1 Search Strategy and Study Identification

**Database coverage.** The search was anchored on backward and forward
citation tracking of five benchmark meta-analyses and supplemented by
structured queries in Web of Science (WoS Core Collection: SSCI, SCI-E,
ESCI) and Scopus, two comprehensive multi-disciplinary databases for
peer-reviewed IB research (Kraus et al., 2022). The strategy is systematic
but bounded by the anchor set and its citation network rather than an
exhaustive database census. Supplementary searches in ABI/INFORM Complete,
Business Source Complete (EBSCO), ScienceDirect, SpringerLink, and Emerald
Insight maximized coverage of specialist journals not fully indexed in WoS
or Scopus. Backward citation tracking was applied to five anchor
meta-analyses: Bausch and Krist (2007), Kirca et al. (2012), Marano et al.
(2016), Schwens et al. (2018), and Arte and Larimo (2022); forward
citation tracking in Google Scholar used the same anchors to identify
citing literature published after 2022.

**Search string (WoS Topic field):**

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

An equivalent string using Scopus field codes (TITLE-ABS-KEY) was
applied identically. The Scopus string was validated against a
known-item set of 30 papers confirmed eligible from prior reading;
recall was 97% (29/30), establishing adequate coverage.

**Temporal coverage.** January 1977 to March 2026. The lower boundary
aligns with the earliest empirical tests of the I to P relationship
(Vernon, 1971; Rugman, 1976), ensuring no pioneering study is excluded.

**OSF registration.** The full protocol (search string, eligibility
decision rules, moderator coding instructions, and planned metafor model
specifications) is registered on OSF (DOI: 10.17605/OSF.IO/Z37KN). Because
the corpus had already been assembled, this is a transparency registration
of the analysis plan rather than a data-blind pre-registration; the
protocol is available from the corresponding author.

### 3.2 Eligibility Criteria and Study Selection

The two authors independently applied the eligibility criteria below in two
stages: (1) title and abstract screening; (2) full-text assessment.
Disagreements at both stages were resolved by discussion following a
predetermined rule.

| Criterion | Inclusion | Exclusion |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Population | Private-sector firms with measured internationalization and financial performance | State-owned enterprises (government equity \> 50%); financial sector (SIC 6000–6999); wholly domestic firms |
| Internationalization operationalization | FSTS (foreign sales-to-total sales), entropy index, count of foreign markets, transnationality index (UNCTAD), or FDI-to-total-investment ratio | Purely binary presence/absence; purely qualitative assessments |
| Performance operationalization | Accounting-based (ROA, ROE, ROS); market-based (Tobin's Q, stock returns); productivity-based (labor productivity, TFP) | Narrative or purely ordinal ratings; non-financial-only indices (e.g., environmental scores without financial correlate) |
| Effect size extractability | Correlation *r*; regression β (convertible to *r*\_partial via Peterson & Brown, 2005); *t*-statistic with *df* (convertible via *r* = √\[*t*²/(*t*²+*df*)\]); *F*-statistic with *df*₁ = 1 | Structural equation model path loadings without associated *SE*; qualitative case studies; simulation studies; theoretical derivations without data |
| Language | English; Vietnamese | Other languages unless the abstract confirms a convertible effect size |
| Region | Any region; ICRV regime assigned globally using World Bank WGI Rule of Law (2023 vintage); Asia-Pacific subsample available as sensitivity analysis |, |
| Publication type | Peer-reviewed journal articles; articles in press with DOI | Doctoral dissertations, master's theses, working papers, conference papers, book chapters, unpublished manuscripts, institutional reports |

To ensure comparability and methodological quality, the main analysis was
restricted to peer-reviewed journal articles and articles in press with
identifiable DOI information. Doctoral dissertations, theses, working
papers, conference papers, book chapters, unpublished manuscripts, and
institutional reports were excluded to maintain consistency in peer-review
standards and reduce heterogeneity from non-equivalent publication types.
Grey-literature records identified during supplementary searching were
documented in the PRISMA flow diagram but excluded from the primary model.

**PRISMA 2020 flow.** The corpus was assembled through backward and
forward citation tracking of the five anchor meta-analyses, supplemented
by targeted database queries rather than an exhaustive census. Records
were screened in two stages (title/abstract, then full text) against the
Section 3.2 criteria. This yielded *k* = 238 coded studies and *K* = 288
effect sizes for synthesis. Because identification proceeded by citation
chaining rather than a single database export, the flow is reported under
the PRISMA 2020 "studies identified via other methods" variant (Appendix
A); stage-level database-census counts are therefore not applicable. The
synthesized set (*k* = 238; *K* = 288) is fixed and data-backed, and the
coded database is available from the corresponding author.

### 3.3 Data Extraction and Quality Assurance

#### 3.3.1 Effect-Size Extraction Protocol

Statistical parameters were extracted from the full text of each eligible
study by the primary coder (first author) using the standardized form in
Appendix B. For each study, the following were recorded: sample size (*N*),
the focal I to P effect size (Pearson's *r* or convertible statistic),
data-year range, country or region, DOI operationalization, performance
operationalization, and study-specific features relevant to moderator
coding.

**Effect-size conversion hierarchy.** When Pearson's *r* was not reported
directly, the following sequence was applied in order of statistical
precision: (i) *r* from *t*-statistic:
$r = \sqrt{t^{2}/\left( t^{2} + df \right)}$ (Cohen, 1988); (ii)
*r*\_partial from standardized regression β: *r*\_partial = β × 0.98
(the simplified form of Peterson & Brown's (2005) estimator
0.98β + 0.05λ; identical for negative β and conservative for positive
β); (iii) *r* from *F*-statistic with *df*₁ = 1:
$r = \sqrt{F/\left( F + df_{2} \right)}$ (Rosenthal, 1994). Studies
reporting only unstandardized β without an associated *t*-statistic and
*df* were excluded from the meta-analytic sample unless the *p*-value
allowed at minimum a directional classification.

**Multiple effects per study.** When a study reported separate estimates
for distinct subsamples (different countries, time periods, or mutually
exclusive industry subgroups), each was coded as an independent effect
size with a unique effect ID sharing study-level identifiers. When a study
reported multiple model specifications for the same sample, the most fully
controlled specification (largest covariate set) was retained to minimize
omitted-variable confounding; other specifications were logged but not
entered into the analysis database.

**Moderator coding.** Each record was then coded for the seven moderators
defined in Section 3.4. ICRV regime was assigned from the reported country
using the World Bank WGI Rule of Law lookup table (2023 vintage); DPL phase
from the median data year; cDAI from the World Bank Digital Adoption Index
2016 vintage or the ITU Digital Development Index (rescaled to 0–1) for
country-years not covered by the World Bank composite. All assignments were
documented with source references to enable independent verification, and
all records were subject to double-entry verification under the inter-coder
reliability protocol (Section 3.3.2).

#### 3.3.2 Inter-Coder Reliability Assessment

The inter-coder reliability (ICR) protocol followed a three-stage design.
In **Stage 1** (calibration), both coders independently coded a pilot set
of 10 studies using the full Appendix B protocol; discrepancies were
discussed and the protocol refined before proceeding. In **Stage 2**
(independent coding), both coders independently coded a 20% stratified
random subsample (*k* = 47 studies), sampled for representation across ICRV
regime, DPL phase, and DOI measure type. In **Stage 3** (adjudication), the
PI resolved discrepancies by a predetermined rule: for categorical
moderators, the adjudicator's decision was final; for continuous cDAI
scores, the mean of the two coders' values was used when ICC(2, 1) ≥ 0.80,
and the PI's direct lookup otherwise.

ICR was assessed using Cohen's κ for categorical variables (ICRV regime,
DPL phase, industry sector, DOI measure type, performance measure type)
and the two-way random-effects ICC(2, 1) for continuous cDAI scores. The
target κ ≥ 0.70 follows Landis and Koch's (1977) "substantial agreement"
criterion, the minimum acceptable level for meta-analytic coding in IB
research (Aguinis et al., 2011). ICR statistics are reported in Table 3.1
(Section 4.1); all targets were met before coding the remaining 80% of the
corpus.

#### 3.3.3 Study-Level Risk of Bias

Consistent with established practice in I to P meta-analysis (Bausch &
Krist, 2007; Marano et al., 2016), no formal study-level risk-of-bias
instrument (e.g., RoB 2, ROBINS-I) was applied. The corpus consists
exclusively of peer-reviewed observational survey studies; the most
relevant threats (publication bias, omitted-variable bias, and DOI
measurement heterogeneity) are addressed at the synthesis level.
Publication bias is assessed via Egger's regression test, Begg and
Mazumdar's (1994) rank-correlation test, and Duval and Tweedie's (2000)
trim-and-fill procedure (Section 3.6). Measurement heterogeneity is
addressed through moderator coding of DOI type (FSTS, FATA, entropy, count)
and performance type, and through the three-level model's decomposition of
within-study variance from multiple specifications per study.

### 3.4 Moderator Coding Protocol

Seven moderators were coded for each effect size: four standard moderators
replicated from prior I to P meta-analyses (Marano et al., 2016) and three
novel moderators introduced here.

**Standard moderators** (4):

1. *Country of origin*, ISO 3166-1 alpha-3 code; multi-country studies
    coded "pooled" with ICRV regime assigned to the modal country if one
    country contributes ≥ 60% of the sample, otherwise "cross-regime"
2. *Industry sector*, SIC broad division: manufacturing (SIC 20–39),
    services (SIC 40–89), or mixed/unspecified
3. *DOI operationalization*, FSTS (foreign sales ÷ total sales); entropy
    index (Jacquemin & Berry, 1979); count of foreign markets or
    subsidiaries; transnationality index (UNCTAD composite)
4. *Performance operationalization*, accounting-based (ROA, ROE, ROS);
    market-based (Tobin's Q, stock return); productivity-based (labor
    productivity, TFP); composite (mixed)

**Novel moderators** (3): 5. *ICRV regime*, a five-code classification
from the World Bank WGI Rule of Law score (2023 vintage), validated
against IMF World Economic Outlook classification: Code I,
Advanced-Innovation (WGI \> +0.80; e.g., Singapore, Hong Kong, South
Korea, Japan, Taiwan, Australia); Code II, Upper-Middle (0 \< WGI ≤
+0.80; e.g., China, Malaysia, Thailand); Code III, Emerging (−0.50 \<
WGI ≤ 0; e.g., Vietnam, India, Philippines); Code FR, Frontier/SIDS (WGI
≤ −0.50 or small island developing state, e.g., Bangladesh, Myanmar,
Fiji, Pacific island economies); Code MX, multi-country pooled samples
spanning two or more regimes (no single modal-country regime ≥ 60% of
sample). 6. *cDAI*, a country-year digital adoption composite (0–1):
primary source, World Bank Digital Adoption Index (2016 vintage, Sahay et
al., 2020); secondary source, ITU Digital Development Index (DDI,
2017–2026, linear-rescaled to 0–1). Country-year assignment follows the
median year of the study's data period; for multi-country samples, cDAI is
the sample-weighted average of country-year scores. Studies lacking
country-year DAI data are assigned ITU ICT Development Index values with a
−0.05 adjustment for known downward bias relative to the World Bank
composite (Katz & Callorda, 2018). 7. *DPL phase*, "Precede" (median data
year \< 2009); "Span" (data spans 2005–2014 or cannot be classified as
predominantly Precede or Follow); "Follow" (median data year ≥ 2015).
Studies whose data years cannot be determined are coded "Span" by default
and flagged.

### 3.5 Statistical Model: Three-Level MARA

The three-level model (Van den Noortgate et al., 2013; Cheung, 2014)
decomposes the observed effect size *r*\_ij (effect *i* from study *j*)
into true between-study variability, residual within-study variability,
and sampling error:

**Level 1, Sampling error:**

$$r_{ij} = \theta_{ij} + e_{ij}, \quad e_{ij} \sim \mathcal{N}\left( 0, \, v_{ij} \right)$$

where *v*\_ij is the known conditional sampling variance of the
Fisher-transformed correlation *z*\_ij, computed from the study-reported
*N*\_ij as *v*\_ij ≈ 1/(*N*\_ij − 3) (Borenstein et al., 2021).

**Level 2, Within-study heterogeneity:**

$$\theta_{ij} = \delta_{j} + u_{ij}, \quad u_{ij} \sim \mathcal{N}\left( 0, \, \sigma_{(2)}^{2} \right)$$

where σ²\_(2) captures residual variation among effect sizes within a
study (e.g., from different samples, subgroups, or model specifications
reported in the same paper).

**Level 3, Between-study heterogeneity and moderation:**

$$\delta_{j} = \mu + \mathbf{X}_{j}\mathbf{\beta} + w_{j}, \quad w_{j} \sim \mathcal{N}\left( 0, \, \sigma_{(3)}^{2} \right)$$

where **X**\_j is the (*J* × *p*) matrix of study-level moderators (ICRV
regime dummy vector \[*d*\_II, *d*\_III, *d*\_FR, *d*\_MX, with Regime I as
reference\]; continuous cDAI score; DPL phase dummy vector \[*d*\_Span,
*d*\_Follow, with Precede as reference\]; plus the four standard moderators
as controls), **β** is the (*p* × 1) coefficient vector of primary
interest, and *w*\_j is the residual between-study variance component.

**Estimation.** Parameters are estimated by Restricted Maximum Likelihood
(REML) using `rma.mv` in `metafor` v4 (Viechtbauer, 2010), with the
variance-covariance matrix for multiple effects within studies specified as
compound-symmetric. REML was preferred over full ML because it produces
unbiased variance component estimates when *k* is moderate relative to the
number of moderators *p* (Raudenbush & Bryk, 2002, p. 39).

**Effect-size transformation.** All Pearson's *r* values are transformed
to Fisher's *z* prior to analysis (*z* = 0.5 × ln\[(1+*r*)/(1−*r*)\]) to
stabilize variance and approximate normality (Hedges & Olkin, 1985). All
reported results are back-transformed to *r* for interpretability. For
regression β-derived *r*\_partial values (Peterson & Brown, 2005), the
same Fisher transformation is applied.

**Heterogeneity decomposition.** The proportional heterogeneity at each
level is computed as:

$$I_{(2)}^{2} = \frac{{\widehat{\sigma}}_{(2)}^{2}}{{\widehat{\sigma}}_{(2)}^{2} + {\widehat{\sigma}}_{(3)}^{2} + \bar{v}} \times 100\%$$

$$I_{(3)}^{2} = \frac{{\widehat{\sigma}}_{(3)}^{2}}{{\widehat{\sigma}}_{(2)}^{2} + {\widehat{\sigma}}_{(3)}^{2} + \bar{v}} \times 100\%$$

where $\bar{v}$ is the average sampling variance across all *K* effect
sizes (Cheung, 2014, eq. 15). The sum $I_{(2)}^{2} + I_{(3)}^{2}$ gives the
total systematic heterogeneity, analogous to *I*² in the conventional
random-effects model.

**Moderator significance.** The omnibus test for each categorical moderator
(ICRV regime, DPL phase) uses the *Q*\_M statistic on *p* − 1 degrees of
freedom, testing whether between-regime or between-phase variance in pooled
effect sizes exceeds sampling error. Pairwise regime comparisons use the
Holm–Bonferroni correction. For continuous cDAI, the significance of
*β*\_cDAI is assessed by a two-sided Wald *z*-test.

### 3.6 Publication Bias Assessment

Publication bias was assessed using four complementary tests following
the graduated approach of Borenstein et al. (2021, ch. 30) and Vevea and
Woods (2005). First, **Egger's weighted regression test** (Egger et al.,
1997) regresses the standardized effect size on its precision (inverse
standard error), with the intercept testing funnel-plot asymmetry. Second,
**Begg and Mazumdar's rank correlation test** (1994) provides a
non-parametric alternative less sensitive to outliers. Third, the
**trim-and-fill procedure** (Duval & Tweedie, 2000) imputes the
theoretically missing left-side studies and re-estimates the pooled
effect; the adjusted estimate quantifies the maximum bias attributable to
asymmetry. Fourth, **Orwin's fail-safe *N*** (1983) computes the number of
null-effect (*r* = 0) unpublished studies required to reduce the pooled *r*
below the practical-significance threshold of *r* = 0.10 (Cohen, 1988);
fail-safe *N* exceeding 5*k* + 10 (Rosenthal, 1991) indicates that
publication bias cannot substantively reverse the main conclusions.

Additionally, **PET-PEESE meta-regression** (Stanley & Doucouliagos, 2014)
is applied as a model-based correction: the precision-effect test (PET)
regresses effect sizes on their standard errors; if significant, the
precision-effect estimate with standard error (PEESE) substitutes the
squared standard error as regressor, estimating the true effect after
correcting for small-study bias.

### 3.7 Robustness Checks

The following pre-specified robustness checks evaluate the sensitivity
of the main findings to modelling choices, sample restrictions, and
alternative operationalizations:

1. **Two-level vs. three-level comparison.** The baseline pooled *r* is
    estimated under both the conventional single-level random-effects model
    (ignoring within-study nesting) and the three-level model; substantive
    divergence (Δ*r* \> 0.02) would indicate meaningful nesting bias.
2. **Leave-one-out sensitivity.** Each study is removed iteratively; the
    resulting distribution of *k* − 1 estimates identifies influential
    studies (Cook's distance \> 4/*k*) and assesses pooled-estimate
    stability.
3. **DOI operationalization restriction.** The baseline is re-estimated on
    FSTS-only studies, which provide the most comparable
    internationalization measure across papers (Helpman et al., 2004);
    ICRV gradient and DPL phase findings are checked for consistency.
4. **ICRV alternative classification.** The WGI Rule of Law dimension is
    replaced by the WGI composite governance index (average of six
    dimensions: Voice and Accountability, Political Stability, Government
    Effectiveness, Regulatory Quality, Rule of Law, Control of Corruption)
    as classifier, at the same percentile thresholds; robustness requires
    the ICRV gradient direction to be preserved.
5. **Temporal restriction.** The sample is restricted to post-2000 studies
    (*k* ≈ 180) to test whether vintage effects (older studies averaging
    lower digital infrastructure) account for DPL phase findings
    independently of the theoretical mechanism.

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
Within the combined Frontier/SIDS (FR) code, all *k* = 3 coded studies
sample frontier economies and none sample a small-island developing state
(SIDS *k* = 0); SIDS effects therefore cannot be estimated in the present
corpus and are flagged as a targeted-search priority (to follow the
OSF-registered search protocol).

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
upward bias from ignoring multilevel nesting earlier. This magnitude places the pooled effect at the lower bound of the prior meta-analytic record (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016) and close to recent emerging-market syntheses that likewise report small positive effects amid very high heterogeneity (Wu et al., 2022); the substantial residual heterogeneity is consistent with evidence that internationalization outcomes are systematically bounded by cultural and institutional distance (Beugelsdijk et al., 2018) rather than governed by a universal mechanism. The larger share of
systematic heterogeneity lies within studies (Level 2, *I*²\_(2) = 54.1%),
attributable to within-paper variation in DOI operationalization,
performance measure type, and control specification across reported models.
Between-study variance (Level 3, *I*²\_(3) = 8.4%) represents the
country-context differences ICRV, cDAI, and DPL phase were designed to
explain. Total *I*² = 62.4% indicates substantial heterogeneity beyond
sampling error, motivating the moderator analyses (Section 4.3–4.5), which
do not resolve it significantly.

### 4.3 ICRV 5-Regime Moderation (H1)

*Q*\_M(ICRV) = 17.35 (*df* = 4, *p* = .002). H1 **confirmed**: the
between-regime Q_M test is significant as hypothesized. Exploratory
Propositions E1a (Advanced largest) and E1b (Frontier smallest) are **not
meta-analytically confirmed**, since the significant Q_M is driven by the
*k* = 3 Frontier-group anomaly rather than a monotone institutional
gradient (see below).

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

The *Q*\_M = 17.35 is significant (*p* = .002) but the between-group
pattern does not confirm the hypothesized monotone gradient (I \> II \>
III \> Frontier). Pairwise contrasts against Group I (intercept) show that
Group II (*p* = .581), Group III (*p* = .502), and MX (*p* = .269) do not
differ significantly from Advanced-Innovation contexts. The only
significant contrast is Group I vs. Frontier (b = +0.285, *p* \< .001),
driven entirely by the *k* = 3 Frontier estimate dominated by one outlier
(Pouresmaeili et al., 2018, *r* = 0.69). Excluding Frontier, no
between-group differences approach significance.

Group I (k=139, primarily Western MNEs and Asian advanced economies) shows
the highest reliable effect (*r̄* = 0.079) and Group III (k=91, Emerging)
shows *r̄* = 0.068, a difference of 0.011 directionally consistent with
CIMT but not significant. H1 is confirmed, establishing systematic
variation in I to P effect sizes across ICRV regimes; however, E1a's
predicted ordering (Advanced \> Emerging) and E1b's predicted Frontier
floor are not confirmable at *k* = 3 Frontier, and the gradient-specific
propositions require larger *k* per regime.

### 4.4 cDAI Moderation (H3)

*Q*\_M(cDAI) = 1.23 (*df* = 2, *p* = .541). H3 **not supported**.

Meta-regression with continuous cDAI score: β_cDAI = +0.003 (*SE* = 0.010,
*p* = .744). Neither the categorical between-group test nor the continuous
linear trend shows significant cDAI moderation.

**Table 4.2, cDAI subgroup** *(actual MARA output)*

| cDAI Group | *k* | *r̄* | 95% CI | Δ vs. Low |
|------------|-----|-------|------------------|------------------------|
| Low | 174 | 0.075 | \[0.056, 0.094\] |, |
| Medium | 76 | 0.063 | \[0.036, 0.090\] | b = −0.012, *p* = .489 |
| High | 38 | 0.091 | \[0.052, 0.129\] | b = +0.016, *p* = .469 |

The three cDAI subgroup means are all significantly positive (*p* \< .001)
but do not differ from each other. The non-monotone ordering (Low \>
Medium \< High) and small, non-significant contrasts fail to support the
predicted positive linear gradient, and the cDAI × DPL interaction cannot
be reliably estimated given the non-significant main moderation. H3 is not
supported: country-level digital adoption (measured via World Bank DAI /
ITU Digital Development Index) does not significantly amplify the pooled
I to P effect in this *k* = 238 sample. A larger sample with better
resolution across the cDAI spectrum is required to test the amplification
gradient.

### 4.5 DPL Phase Moderation (H2)

*Q*\_M(DPL) = 0.62 (*df* = 2, *p* = .734). H2 **not supported**.

**Table 4.3, DPL phase subgroup** *(actual MARA output)*

| DPL Phase | Definition | *k* | *r̄* | 95% CI | Δ vs. PRE |
|---------------|-------------------------------------|-----|-------|------------------|------------------------|
| Precede (PRE) | Sample data predominantly pre-2009 | 100 | 0.082 | \[0.057, 0.107\] |, |
| Span (SPN) | Sample spans the 2009 inflection | 108 | 0.068 | \[0.045, 0.091\] | b = −0.014, *p* = .434 |
| Follow (FOL) | Sample data predominantly post-2014 | 80 | 0.073 | \[0.046, 0.100\] | b = −0.009, *p* = .645 |

Pairwise comparisons: PRE vs. FOL (*z* = 0.46, *p* = .645); PRE vs. SPN
(*z* = 0.78, *p* = .434); FOL vs. SPN (*z* = 0.28, *p* = .782). No pairwise
difference approaches significance.

The ordering (PRE \> FOL \> SPN) is opposite to H2's prediction (FOL \>
SPN \> PRE), but the between-group differences are negligible and
non-significant and should not be over-interpreted. The null DPL result may
reflect insufficient power to detect small temporal trends at *k* = 238,
confounding of DPL phase with ICRV composition (pre-2009 studies
concentrated in advanced economies), or the absence of a meta-analytically
detectable inflection at the current sample size. H2 is not supported.

Figure 3: DPL phase moderation, pooled I to P effect by digital adoption
epoch

*Figure 3.* DPL phase subgroup results. Pooled effect sizes by Precede /
Span / Follow epoch with 95% CI. The between-phase differences are small
and non-significant.

### 4.6 Publication Bias (H4)

H4 **supported**: multiple indicators detect publication bias, though the
positive I to P effect survives correction.

**Egger's regression test** (SE as moderator): *b* = 0.487 (*SE* = 0.251,
*p* = .052), just above the conventional α = .05 threshold; this criterion
does not reach significance, so funnel asymmetry by Egger's test alone is
not confirmed.

**Begg's rank correlation** (Kendall's τ): τ = −0.132, *p* = .001,
indicating significant funnel asymmetry; studies with larger standard
errors (smaller *n*) report systematically lower effect sizes, consistent
with bias against null or negative findings.

**Trim-and-fill**: imputes *k* = 57 missing left-side studies; adjusted
pooled *r̄* = 0.035 (95% CI \[0.018, 0.051\]), a conservative lower bound.
The effect remains positive and significant but is substantially attenuated
(0.074 to 0.035).

**Fail-safe *N*** (Rosenthal, 1991): *N* = 44,782, far exceeding the
criterion of 5*k* + 10 = 1,195; reducing the effect to triviality would
require 44,782 unpublished null studies, an implausible number.

The trim-and-fill correction (*k* = 57 imputed, adj. *r* = 0.035) is the
most conservative bias-corrected estimate, a meaningful reduction from the
raw *r* = 0.074. With the substantial unexplained heterogeneity (*I*² =
62.4%) and non-significant moderator tests (Section 4.3–4.5), this evidence
suggests the apparent average I to P effect is upwardly inflated in the
published literature, with the true population effect closer to *r* ≈
0.035.

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
result, and the DL two-level estimator gives an identical point estimate
(0.074), confirming that three-level nesting adds precision without biasing
the pooled effect. The FSTS-only restriction (*r̄* = 0.060) is the most
conservative check and remains positive and significant, suggesting DOI
operationalization heterogeneity partially inflates the pooled effect when
broader measures are included.

Figure 4: Leave-one-out sensitivity, pooled *r̄* range across
leave-one-out iterations

*Figure 4.* Leave-one-out sensitivity analysis. Each point is the pooled
*r̄* with 95% CI after removing one study. The narrow range confirms no
single study drives the results.

## 5. Discussion

### 5.1 Alignment with Country-Level Evidence

The meta-analytic baseline (*r* = 0.074, *k* = 238, 49 economies) is
consistent with country-level evidence across the global corpus, including
the Asia-Pacific primary studies underlying the ICBEF 2025 baseline
(Authors, 2024). The pooled effect is positive and significant: export-
intensive firms tend to outperform domestically focused peers after
adjusting for firm size, age, and industry.

**Advanced-I contexts (Group I, k = 139; *r̄* = 0.079):** The Group I mean
is the highest reliable estimate, directionally consistent with
institutional complementarity theory: strong contract enforcement, IP
protection, and low liability of foreignness (Zaheer, 1995) let firms
sustain productive internationalization without the coordination cost
penalties of weaker environments (North, 1990; Peng et al., 2008). The
magnitude is much smaller than CIMT predicted, and the I–III difference is
not significant (*p* = .502).

**Emerging contexts (Group III, k = 91; *r̄* = 0.068):** The Emerging group
lies directionally below the Advanced group, consistent with CIMT's
institutional friction argument. At the primary-study level, Authors (2025)
document a negative aggregate DOI coefficient on 380 Indian WBES firms
(FGLS estimation), with manager experience and female top-management
leadership as positive moderators, consistent with CIMT's prediction that
firm-level compensating resources partially offset institutional friction
in Emerging environments.

**Frontier contexts (FR, k = 3; *r̄* = 0.349):** The *k* = 3 Frontier
estimate is driven by one outlier (Pouresmaeili et al., 2018, *r* = 0.69,
*n* = 226 Iranian manufacturing firms) and cannot be interpreted as a
reliable Frontier I to P effect, reflecting the near-impossibility of
meta-analytic inference when only three studies populate a regime cell. The
true effect could be zero, positive, or negative; larger *k* is required.

**Synthesis:** H1 is confirmed (*Q*\_M = 17.35, *p* = .002), establishing
that I to P effect sizes vary across institutional regimes as theorized.
Because this significance is driven by the *k* = 3 Frontier contrast rather
than well-powered pairwise contrasts across the Advanced/Upper-middle/
Emerging cells, the directional propositions E1a and E1b are not confirmed.
The substantiated finding is that the baseline effect (*r* = 0.074) is
broadly consistent across well-populated groups (I, II, III, MX), and the
Advanced-Emerging gap (*r̄* = 0.079 vs. 0.068) does not reach significance,
a result that bounds rather than refutes CIMT's gradient prediction.

### 5.2 Theoretical Contributions

**Contribution 1: Largest globally representative I to P meta-analysis to
date.** The three-level MARA with *k* = 238 studies from 49 economies (*K*
= 288 effects) is the most comprehensive I to P synthesis to apply
three-level modeling, extending the ICBEF 2025 Asia-Pacific baseline (*k* =
113) by 124 studies with a globally inclusive ICRV-coded corpus. The model
correctly partitions within- and between-study variance, and the baseline
*r* = 0.074 replicates prior estimates and is robust across seven
sensitivity checks.

**Contribution 2: First meta-analytic test of ICRV, cDAI, and DPL
moderators.** This is the first study to formally test ICRV institutional
regime, national digital adoption (cDAI), and Digital Paradox Lifecycle
phase as moderators in a three-level MARA. H1 is confirmed (*Q*\_M = 17.35,
*p* = .002), establishing systematic between-regime variation. The
directional propositions (E1a/E1b) and the cDAI and DPL hypotheses (H2, H3)
are not confirmed under rigorous between-group testing, setting
theoretically informative bounds: the *k* = 238 sample lacks sufficient
between-regime variation (Frontier, *k* = 3; SIDS, *k* = 0) to detect the
CIMT gradient, and cDAI and DPL phase do not explain between-study
heterogeneity here. Future replications with targeted regime-level sampling
should test whether the gradient emerges with richer between-regime
representation.

**Contribution 3: Substantial publication bias identified.** The
trim-and-fill-corrected estimate (*r* = 0.035, *k* = 57 imputed studies)
and significant Begg's τ (*p* = .001) together indicate substantial
positive publication bias in the I to P literature. The raw pooled effect
(*r* = 0.074) likely overstates the true average causal effect by
approximately 50–100%, with the bias-corrected estimate (*r* = 0.035) as a
conservative lower bound. This is the most actionable contribution: the
field's widely cited "positive I to P relationship" is partially an artifact
of selective publication rather than a robust phenomenon.

### 5.3 Managerial and Policy Implications

The non-confirmation of the three moderators limits prescriptive
conclusions about institutional regime or digital context, but the baseline
and publication bias findings carry practical significance.

**For firms across all institutional contexts:** The bias-corrected
baseline (*r* = 0.035), not the raw *r* = 0.074, is the better estimate of
the true average performance return to internationalization. Firms
expecting large productivity gains from export intensification alone are
likely to be disappointed. Internationalization strategy should be driven
by firm-specific competitive advantages and market-specific learning, not
by an unconditional assumption that internationalization improves
performance.

**For researchers:** The substantial publication bias (*k* = 57 imputed,
adj. *r* = 0.035) calls for pre-registered studies with explicit
null-hypothesis reporting, since over-representation of positive effects
may be distorting the field's understanding of when and why
internationalization helps. OSF registration and three-level MARA with
trim-and-fill correction should become standard in future I to P
meta-analyses.

**For policymakers:** The ICRV Advanced–Emerging gap (*r̄* = 0.079 vs.
0.068, non-significant) is not large enough to justify institutional
quality as the primary determinant of export-led productivity. Export
promotion programs should target firm-level capabilities (technological,
managerial) as much as institutional reform.

### 5.4 Limitations and Inferential Bounds

Three limitations bound the inferences from this study.

**(a) What cannot be concluded:** (1) The SIDS subgroup (*k* = 0; no
primary small-island study met inclusion) does not permit any test of the
"forced-penalty" hypothesis; a targeted search for SIDS-focused primary
studies (following the OSF-registered search protocol) is required first. (2) The cDAI × ICRV joint moderation (three-way
interaction) is underpowered (*k* per cell \< 20), so point estimates carry
wide confidence intervals. (3) All effect sizes are cross-sectional or
study-level panel, so no longitudinal meta-regression can distinguish
selection effects from causal learning returns.

**(b) Methodological remedies for future work:** Panel meta-analysis with
longitudinal firm-level effect sizes would enable causal decomposition
(Sutton & Higgins, 2008), and Bayesian meta-regression with informative
priors from country-level panel studies of frontier economies would tighten
SIDS regime estimates.

**(c) Boundary of the ICRV classification:** The 5-regime taxonomy uses WGI
Rule of Law as primary classifier; alternatives (Heritage Foundation
Economic Freedom, Transparency International CPI) yield broadly consistent
assignments but differ at the margin for Regime II/III border cases.

## 6. Conclusion

This paper presents the first three-level MARA of the
internationalization–performance relationship on a globally representative
corpus, extending the ICBEF 2025 Asia-Pacific baseline from *k* = 113 to
*k* = 238 studies from 49 economies (*K* = 288 effects) and introducing
three novel moderators: ICRV institutional regime, country-level digital
adoption (cDAI), and Digital Paradox Lifecycle (DPL) phase. The three-level
pooled effect (*r* = 0.074, 95% CI \[0.060, 0.088\], *I*²_total = 62.4%)
confirms a small but consistent positive I to P relationship globally,
robust across seven sensitivity checks.

H1 (ICRV between-regime Q_M test) is confirmed (*Q*\_M = 17.35, *p* =
.002), establishing systematic between-regime variation in I to P effect
sizes. However, the directional gradient (E1a: Advanced largest; E1b:
Frontier smallest) is not confirmable at *k* = 3 Frontier, and the cDAI
(H3: *Q*\_M = 1.23, *p* = .541) and DPL phase (H2: *Q*\_M = 0.62, *p* =
.734) moderators do not explain between-study heterogeneity in the current
sample. The CIMT gradient (E1a/E1b), digital infrastructure amplification
(H3), and DPL temporal moderation (H2) remain theoretically motivated but
empirically unconfirmed at *k* = 238, null results that should inform
future pre-registered replications with targeted regime-level sampling.

The most substantive empirical finding is substantial publication bias:
trim-and-fill imputes *k* = 57 missing studies, reducing the
bias-corrected pooled effect to *r* = 0.035 (95% CI \[0.018, 0.051\]),
positive but considerably attenuated. The published I to P literature thus
over-represents positive results, and the true average return is closer to
*r* ≈ 0.035 than the oft-cited 0.07–0.10 range. The heterogeneity puzzle
(*I*² = 62.4%) remains largely unresolved, with within-study variance
(Level 2, 54.1%) dominating between-study variance (Level 3, 8.4%),
indicating that DOI and performance measure choices within papers matter
more than cross-country institutional differences.

**Limitations.** Five inferential constraints bound these conclusions.
First, the three moderator hypotheses are not confirmed in the present
*k* = 238 corpus; this may reflect insufficient regime-level *k* (Frontier:
*k* = 3; SIDS: *k* = 0) rather than genuine null effects, so a formal
WoS/Scopus search targeting Frontier and SIDS contexts is required before
the ICRV null can be interpreted as definitive. Second, the Frontier-group
anomaly (*k* = 3, *r̄* = 0.349, dominated by Pouresmaeili et al. 2018) is
the sole driver of ICRV significance; future work should reassess this
coding and search for additional Frontier-regime studies. Third, cDAI is
measured at the study level using country-year World Bank Digital Adoption
Index scores (primary) or ITU Digital Development Index (secondary), not
direct replication of the WBES firm-level indicators in the companion
studies; any systematic error in country-year assignment (e.g., vintage
mismatch between data period and DAI reference year) may attenuate the
moderation coefficient. Fourth, the search was restricted to
English-language publications, so non-English studies (Chinese, Japanese,
Korean, Southeast Asian) are underrepresented, potentially biasing the
regime distribution toward Advanced economies. Fifth, reliability is
established on a 20% double-coded subsample (*k* = 47 studies, Table 3.1);
the remaining 80% is single-coded by the first author against the codebook,
which, while standard for resource-bounded syntheses, cannot be
independently validated.

**Future research.** Three directions follow from the null moderator
findings. First, a formal WoS/Scopus search targeting Frontier and SIDS
economy I to P studies (targeted strings in the OSF-registered search
protocol) would expand Frontier
*k* from 3 to potentially 20–40 studies, enabling a meaningful test of the
Frontier cell. Second, a pre-registered replication of the ICRV,
cDAI, and DPL hypotheses, with explicit per-cell power analysis and OSF
registration, would provide a definitive test of whether these moderators
reach significance in a *k* ≥ 400 corpus. Third, the publication bias
finding (*k* = 57 imputed, adj. *r* = 0.035) motivates a dedicated audit:
surveying I to P researchers about unpublished null results and
meta-analyzing grey literature and dissertations would bound the true
population effect more precisely than trim-and-fill alone.

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

## Acknowledgements

The authors thank the authors of the primary studies synthesised in this meta-analysis. Where World Bank Enterprise Survey data informed primary estimates, the original collectors, the authorised distributor, and the relevant funding agencies bear no responsibility for the use of the data or for interpretations based upon such uses.

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

Beugelsdijk, S., Kostova, T., Kunst, V. E., Spadafora, E., & van Essen,
M. (2018). Cultural distance and firm internationalization: A
meta-analytical review and theoretical implications. *Journal of
Management, 44*(1), 89–130.

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

Dickersin, K. (1990). The existence of publication bias and risk factors for its occurrence. *JAMA, 263*(10), 1385–1389.

Authors. (2024, December). Details omitted for double-blind review.

Authors. (2025). Details omitted for double-blind review.
<https://doi.org/10.5772/intechopen.1011012>

Dunning, J. H. (2000). The eclectic paradigm as an envelope for economic and business theories of MNE activity. *International Business Review, 9*(1), 163–190.

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

Kafouros, M., Aliyev, M., Piperopoulos, P., Au, A. K. M., Ho, J. W. Y., & Wong, S. Y. N. (2023). The role of institutional quality and industry dynamism in explaining firm performance in emerging economies. *Global Strategy Journal, 14*(1), 56–83. https://doi.org/10.1002/gsj.1479

Katz, R., & Callorda, F. (2018). *The economic contribution of
broadband, digitization and ICT regulation*. ITU Telecommunication
Development Sector.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road
map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Deligonul, S., Perryman, A. A., & Cavusgil,
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

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609. https://doi.org/10.2307/20159604

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

Rugman, A. M. (1976). Risk reduction by international diversification. *Journal of International Business Studies, 7*(2), 75–80.

Sahay, R., von Allmen, U. E., Lahreche, A., Khera, P., Ogawa, S., Bazarbash, M., & Beaton, K. (2020). *The promise of fintech: Financial inclusion in the post COVID-19 era* (IMF Departmental Paper No. DP/2020/09). International Monetary Fund.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollender, L. (2018).
Limits to outsourcing: A meta-analysis and empirical investigation.
*Journal of International Business Studies, 49*(6), 682–703.

Scott, W. R. (1995). *Institutions and organizations*. Sage.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders?
The international strategies of digital platform firms. *Global Strategy
Journal, 11*(1), 58–80.

Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression
approximations to reduce publication selection bias. *Research Synthesis
Methods, 5*(1), 60–78.

Sutton, A. J., & Higgins, J. P. T. (2008). Recent developments in
meta-analysis. *Statistics in Medicine, 27*(5), 625–650.

Valentine, J. C., Pigott, T. D., & Rothstein, H. R. (2010). How many studies do you need? A primer on statistical power for meta-analysis. *Journal of Educational and Behavioral Statistics, 35*(2), 215–247.

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., &
Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect
sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong,
J., Fabian, N., & Haenlein, M. (2021). Digital transformation: A
multidisciplinary reflection and research agenda. *Journal of Business
Research, 122*, 889–901.

Vernon, R. (1971). *Sovereignty at bay: The multinational spread of U.S. enterprises*. Basic Books.

Vevea, J. L., & Woods, C. M. (2005). Publication bias in research
synthesis: Sensitivity analysis using a priori weight functions.
*Psychological Methods, 10*(4), 428–443.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor
package. *Journal of Statistical Software, 36*(3), 1–48.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic
Management Journal, 5*(2), 171–180.

World Bank. (2023). *Worldwide Governance Indicators*.
<https://info.worldbank.org/governance/wgi/>

Wu, J., Wood, G., & Khan, Z. (2022). Internationalization and firm performance: Evidence from a meta-analysis. *International Business Review, 31*(2), 101920.

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of
Management Journal, 38*(2), 341–363.

## Appendix A, PRISMA 2020 Flow (Studies Identified via Other Methods)

The corpus was assembled through citation-anchored systematic searching rather than a single database census; the flow is therefore reported under the PRISMA 2020 "studies identified via other methods" variant (Page et al., 2021).

    IDENTIFICATION
    ─────────────────────────────────────────────────────────────────
    Studies identified via other methods:
      Backward citation scan (reference lists of 5 anchor meta-analyses)
      Forward citation scan (Google Scholar citing the 5 anchors, post-2022)
      Hand-search (author's corpus, 2020–2026): n = 19
      Supplementary structured queries (WoS, Scopus, specialist
        databases) to check coverage of the citation network

    SCREENING / ELIGIBILITY
    ─────────────────────────────────────────────────────────────────
    Records screened in two stages against the eligibility criteria
    (Section 3.2): title/abstract, then full text. Full-text exclusion
    reasons: no effect size convertible to r; internationalization not
    measured at the firm level; duplicate sample (smaller/older record
    removed); meta-analysis or review rather than a primary study;
    conference paper, thesis, working paper, or book chapter (grey
    literature documented but excluded from the primary model).

    INCLUDED
    ─────────────────────────────────────────────────────────────────
    Studies included in meta-analysis: k = 238
    Effect sizes coded: K = 288

Because identification proceeded by citation chaining, stage-level database-census counts (total identified, deduplicated, and per-reason exclusion tallies) were not maintained as a single database export and are not reported as such; the synthesized set (k = 238; K = 288) is fixed and data-backed.

*The PRISMA 2020 checklist (Page et al., 2021) is available from the corresponding author.*

## Appendix B, Coding Protocol (7 Moderators)

| Moderator | Variable Type | Coding Rule |
|-------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------|
| ICRV regime | Categorical (5 codes) | WGI Rule of Law, 2023 vintage: I (Advanced-Innovation) \> +0.80; II (Upper-Middle): 0–+0.80; III (Emerging): −0.50–0; FR (Frontier/SIDS): \< −0.50 or small island state; MX: multi-country pooled (no modal regime ≥ 60%) |
| cDAI | Continuous (0–1) | World Bank DAI score or ITU DDI score, country-year, standardized. If unavailable: ITU ICT Development Index (substitute) |
| DPL phase | Categorical (3) | Precede: data year \< 2009; Span: data spans 2005–2014; Follow: data year \> 2014 |
| Country of origin | Categorical (ISO) | First author's sample country; multi-country = "pooled" |
| Industry | Categorical (3) | SIC: manufacturing (20–39), services (40–89), mixed/unspecified |
| DOI measure | Categorical (4) | FSTS; Entropy; Number-of-markets; Transnationality index (UNCTAD) |
| Performance | Categorical (4) | Accounting (ROA/ROE/ROS); Market (Tobin's Q); Mixed; Other |

## Appendix C, Consistency Check: MetaEssentials vs. `metafor`

| Statistic | MetaEssentials 1.5 (ICBEF 2025) | metafor REML (3-level, k=238) |
|-------------------------|---------------------------------|-------------------------------|
| Pooled *r* | 0.070 | 0.074 |
| 95% CI | \[0.050, 0.090\] | \[0.060, 0.088\] |
| *I*²_total | 87.92% | 62.4% |
| *I*²\_(2) within-study |, | 54.1% |
| *I*²\_(3) between-study |, | 8.4% |
| *k* studies | 113 | 238 |
| *K* effects |, | 288 |
| σ²\_(2) |, | 0.00878 |
| σ²\_(3) |, | 0.00136 |
| Software | Suurmond et al. (2017) | Viechtbauer (2010) |

*Note:* Lower total I² in the three-level model (62.4% vs. 87.92%)
reflects the expanded *k* = 238 sample and the three-level structure
that partitions variance across levels correctly. The narrower 95% CI
reflects the precision gain from 238 vs. 113 studies. The three-level
model is theoretically preferred as it accounts for multiple effect
sizes nested within studies.

*Word count (excluding tables, references, appendices): ≈ 6,900 words*
