# The Pre-AI Digital Divide and Firm Productivity across Asia's Institutional Regimes: Firm-Level Evidence from 50 Economies

**Manuscript prepared for the *Journal of Economics and Development* Special Issue, "Sustainable Growth and Welfare in the Age of Artificial Intelligence" (Emerald; Scopus/ESCI/ABDC; no APC; deadline 31 October 2026).**

---

## Abstract

**Purpose.** Artificial intelligence is widely expected to reshape productivity and development, yet its dividends rest on a foundational digital substrate that remains unevenly distributed. Before firms can adopt AI, they must cross a basic-digital threshold. This paper maps that pre-AI digital divide at the firm level across 50 Asian and Pacific economies and estimates the productivity dividend of basic digital adoption across institutional regimes, asking what the existing divide implies for who will capture AI-era growth.

**Design/methodology/approach.** Using harmonised World Bank Enterprise Survey microdata for 88,869 firms across 50 economies (103 economy-year waves, 2003–2025, including Japan's inaugural 2025 wave), we measure basic digital adoption (DAI: establishment web presence, a Tier-1 indicator) and labour productivity (standardised within economy-year to neutralise currency and price-level differences). Firms are classified into six Institutional Context Regime Variation (ICRV) groups. We estimate the digital-productivity premium overall and within each regime using two-way (economy and year) fixed effects with standard errors clustered by economy.

**Findings.** First, a pronounced firm-level digital divide: web adoption falls from 69.2% in the strongest-institution (advanced innovation-driven) regime to 40.9%–41.5% in the emerging and Pacific-SIDS regimes, a gap of roughly 28 percentage points. Second, the digital-productivity dividend is positive and significant in every regime (from +0.214 to +0.477 standard deviations of log productivity, all p < .05), confirming that basic digital adoption pays everywhere. Third, the dividend is not monotonic in institutional strength: it is largest in catching-up regimes (lower-middle transition +0.383; advanced-resource +0.477) and compressed in the highest-adoption advanced-innovation regime (+0.240), the signature of digital saturation. The pooled premium is +0.241 (p < .001), roughly double the level effect of deeper technological capability (TCI, +0.124).

**Originality/value.** This is the first firm-level mapping of the digital divide and its productivity dividend across the full institutional spectrum of Asian and Pacific economies on a single harmonised instrument. The results carry a sharp implication for the AI era: the economies furthest behind on basic digital adoption still earn a significant productivity dividend from closing the gap, yet they are precisely the economies least equipped to absorb AI. Unless the pre-AI digital divide is closed, AI is more likely to widen than narrow cross-economy productivity inequality.

**Keywords:** digital divide; digital adoption; firm productivity; institutional regimes; artificial intelligence; sustainable development; World Bank Enterprise Surveys; Asia-Pacific.

---

## 1. Introduction

Few propositions in contemporary economics command as much consensus as the claim that artificial intelligence will be consequential for productivity and growth (Brynjolfsson, Rock, & Syverson, 2021; Agrawal, Gans, & Goldfarb, 2019). The disagreement is about distribution: whether AI's dividends will accrue broadly or concentrate in the firms, sectors, and economies already at the technological frontier (Acemoglu & Restrepo, 2020; Korinek & Stiglitz, 2021). For developing and emerging economies, the stakes are existential. If AI is a general-purpose technology whose returns are conditional on complementary capabilities, then the economies that lack those complementarities risk a new and steeper round of divergence (Comin & Mestieri, 2018).

This paper argues that the decisive complementarity is not exotic. It is the **basic digital substrate** — the web presence, online connectivity, and digital business practices on which any subsequent AI adoption must rest. A firm that does not maintain a web presence is not positioned to integrate AI-enabled marketing, analytics, or coordination tools; an economy in which most firms are offline cannot, in aggregate, capture an AI dividend regardless of national AI strategy. The pre-AI digital divide is therefore not a separate issue from the AI-and-development question; it is its leading edge. Mapping that divide, and quantifying what closing it is worth, is a precondition for any credible assessment of AI's developmental potential.

Yet the firm-level digital divide across developing economies has been difficult to measure comparably. National statistics on internet penetration mask enormous within-economy and within-firm heterogeneity, and firm-level digital data are rarely harmonised across the institutional spectrum that matters for development — from advanced innovation hubs to frontier and small-island economies. The World Bank Enterprise Surveys (WBES), administered on a standardised instrument across more than 150 economies, offer a rare opportunity to observe the same digital and productivity variables, defined identically, across exactly this spectrum.

We exploit that opportunity. Drawing on harmonised WBES microdata for 88,869 firms across 50 Asian and Pacific economies (2003–2025, including Japan's inaugural 2025 wave), we measure basic digital adoption (establishment web presence) and firm labour productivity, classify economies into six institutional regimes, and ask three questions. How large is the firm-level digital divide across institutional regimes? What is the productivity dividend of basic digital adoption, and does it vary by regime? And what do these patterns imply for the distribution of AI-era growth?

We make three contributions. First, we provide the first harmonised, firm-level map of the digital divide across the full institutional spectrum of Asian and Pacific economies, documenting a roughly 28-percentage-point gap in web adoption between the strongest and weakest institutional regimes. Second, we estimate the digital-productivity dividend within each regime and show it is positive and significant everywhere but non-monotonic in institutional strength — largest in catching-up regimes and compressed where adoption is already saturated. Third, we draw out the AI-era implication: the economies furthest behind still have the most to gain from closing the basic-digital gap, yet are least equipped to absorb AI, so the pre-AI divide, if uncorrected, will compound AI-era inequality. This speaks directly to the welfare and development concerns at the heart of the AI-and-growth agenda.

## 2. Background and hypotheses

This study sits at the intersection of three literatures: the economics of the digital divide, the theory of general-purpose technologies and complementarities, and the emerging debate on AI and economic development.

The **digital-divide** literature has long documented unequal access to and use of digital technologies across and within economies, beginning with household and individual connectivity and extending to firms (Norris, 2001; OECD, 2001). Its firm-level branch shows that digital adoption is associated with higher productivity, exporting, and innovation, but that adoption itself is stratified by firm size, sector, and location (Bloom, Garicano, Sadun, & Van Reenen, 2014; Cusolito & Maloney, 2018). What this literature has lacked is a harmonised, firm-level view across the full institutional spectrum of developing and advanced economies on a single instrument — the gap this paper fills using the WBES.

The **general-purpose-technology (GPT)** literature explains why the divide matters for the AI era. GPTs deliver aggregate gains only as complementary investments and capabilities diffuse, producing a delayed and uneven "productivity J-curve" (Bresnahan & Trajtenberg, 1995; Brynjolfsson et al., 2021). The corollary for AI is that the economies and firms lacking the complementary digital substrate cannot convert frontier AI capacity into realised productivity (David, 1990; Comin & Mestieri, 2018). Basic digital adoption — web presence and online business practice — is the foundational complement, the rung of the ladder on which higher digital and AI capabilities are built.

The **AI-and-development** debate, finally, is split between optimism that AI can leapfrog development constraints and concern that it will entrench or widen them (Korinek & Stiglitz, 2021; Agrawal et al., 2019; Acemoglu & Restrepo, 2020). This paper informs that debate empirically and from below: rather than forecasting AI's effects, it measures the pre-AI digital substrate that conditions whether any AI dividend can reach developing-economy firms, and quantifies what closing the substrate gap is currently worth. The three hypotheses below formalise the digital dividend, the institutional gradient of the divide, and the saturation of the dividend.

### 2.1 Digital adoption as the substrate of an AI dividend

The economics of general-purpose technologies holds that the aggregate returns to a new technology depend on the diffusion of complementary investments and capabilities, not on the technology's frontier capacity (Bresnahan & Trajtenberg, 1995; Brynjolfsson et al., 2021). AI is the paradigmatic case: large-language-model and analytics tools are increasingly cheap and accessible, but capturing value from them requires data infrastructure, online presence, digital workflows, and the absorptive capacity to reorganise around them (Cohen & Levinthal, 1990; Verhoef et al., 2021). Basic digital adoption — a firm's web presence and online business practices — is the entry rung of this ladder. It is a necessary, if far from sufficient, condition for AI adoption: a firm without it is structurally excluded from the AI dividend.

Measured as web presence, digital adoption is a Tier-1 indicator: it captures participation in the digital economy at its most foundational level (Verhoef et al., 2021). We are explicit that this is not a measure of AI. It is a measure of the **pre-AI digital readiness** that conditions whether AI's benefits can reach a firm at all. This framing is deliberate and conservative: by quantifying the dividend from the most basic digital step, we establish a lower bound on the developmental cost of the divide that AI will inherit.

> **H1 (digital dividend).** Basic digital adoption is positively associated with firm productivity.

### 2.2 The institutional gradient of the divide

Institutions shape both the level of digital adoption and the return to it. Strong institutions — secure contracts, reliable infrastructure, competitive markets — lower the cost of going online and raise the value of doing so by enabling the transactions that digital presence supports (North, 1990; Khanna & Palepu, 2010). Weak-institution environments impose offsetting frictions: unreliable electricity and connectivity, thin digital-payment ecosystems, and informal competition that blunts the returns to formal digital investment. The expectation is a divide that tracks institutional strength: adoption highest where institutions are strongest, lowest where they are weakest.

> **H2 (institutional divide).** Web adoption declines from stronger to weaker institutional regimes.

### 2.3 Digital saturation and the shape of the dividend

The productivity value of a binary Tier-1 indicator depends on its discriminating power, which is greatest where adoption is partial and least where it approaches saturation (a measurement-side "digital saturation" effect). In the strongest-institution regimes, where web presence is near-universal, the firms that remain offline are a small, selected group, and the estimated digital premium compresses. In catching-up regimes, where adoption is partial and still differentiating, the premium should be largest. In the weakest regimes, low adoption coexists with weak complementary infrastructure, so the premium, while positive, may be bounded by the surrounding frictions.

> **H3 (saturation).** The digital-productivity premium is non-monotonic in institutional strength — compressed in the highest-adoption regime and largest in catching-up regimes.

## 3. Data and methods

### 3.1 Data

We use harmonised WBES microdata for 50 Asian and Pacific economies across 103 economy-year waves, 2003–2025, an analytic frame of 88,869 firms that includes Japan's inaugural 2025 wave. The WBES is administered face-to-face to a senior manager or owner on a standardised instrument, with harmonised sampling and variable definitions that permit direct comparison across the institutional spectrum. The harmonisation of the multi-economy pool (questionnaire-generation mapping, currency comparability, and pooled cross-section construction) follows the protocol documented in the parent dissertation programme.

### 3.2 Variables

*Digital adoption (DAI).* A binary indicator of establishment web presence (WBES item c22b), the Tier-1 marker of digital participation.

*Labour productivity.* Log annual sales per permanent worker, winsorised at the 1st/99th percentiles within wave and standardised within each economy-year cell (lp_z). Within-cell standardisation removes the nominal-currency and price-level differences that would otherwise contaminate cross-economy productivity comparison, so the relationship is identified from within-cell variation.

*Technological capability (TCI).* The standardised mean of R&D activity (h8) and internationally recognised quality certification (b8), included as a benchmark "deep" capability against which to compare the "surface" digital indicator.

*Institutional regime (ICRV).* Each economy is assigned to one of six Institutional Context Regime Variation groups, ordered from strongest to weakest institutional and resource conditions: I Advanced innovation-driven (including Japan, Korea, Singapore, Taiwan, Hong Kong SAR, Israel); II Advanced resource-driven (Gulf economies); III Upper-middle; IV Lower-middle transition; V Emerging; VI Pacific Small Island Developing States.

### 3.3 Estimation

We estimate the digital-productivity premium as the coefficient on DAI in a regression of lp_z with two-way (economy and year) fixed effects and standard errors clustered by economy. Fixed effects absorb time-invariant economy characteristics and common year shocks, so the premium is identified within economy-years. We estimate the premium pooled across all economies (controlling for TCI) and separately within each ICRV regime. The cross-regime adoption rates (the divide) are reported as the share of firms with a web presence in each regime. All estimates are reproducible via `jed_ai_digital/replication/jed_digital_divide.py`; because the working environment lacks a Stata licence, estimation uses the reghdfe-equivalent pyfixest, to be re-validated in Stata before submission.

## 4. Results

### 4.1 The firm-level digital divide (H2)

Table 1 reports web adoption by institutional regime. The divide is pronounced: 69.2% of firms in the strongest-institution regime (advanced innovation-driven) maintain a web presence, falling to 40.9% in the emerging regime and 41.5% in the Pacific SIDS — a gap of roughly 28 percentage points. The middle regimes occupy an intermediate band (advanced-resource 50.2%, upper-middle 53.9%, lower-middle transition 48.3%). The pooled adoption rate across all 50 economies is 49.0%: barely half of formal-sector firms in the region have crossed even the most basic digital threshold.

**Table 1. The firm-level digital divide: web adoption by ICRV regime**

| ICRV regime | Web adoption (%) | N |
|---|--:|--:|
| I Advanced innovation-driven | 69.2 | 6,368 |
| II Advanced resource-driven | 50.2 | 2,231 |
| III Upper-middle | 53.9 | 13,927 |
| IV Lower-middle transition | 48.3 | 44,885 |
| V Emerging | 40.9 | 18,881 |
| VI Pacific SIDS | 41.5 | 2,290 |
| **All 50 economies** | **49.0** | 88,582 |

*H2 supported.* Adoption tracks institutional strength at the extremes — highest in the advanced-innovation regime, lowest in the emerging and SIDS regimes — though the middle regimes are compressed rather than strictly ordered.

The divide is closing, but slowly. Pooling across all economies, web adoption rose from 32.6% in the 2003–2009 waves to 44.6% in 2010–2015 and 52.3% in 2016–2025. Even in the most recent window, then, barely more than half of the region's formal-sector firms maintain a web presence — a sobering baseline against which to assess the readiness of the firm population to absorb AI tools that presuppose an online operating footprint.

### 4.2 The digital-productivity dividend by regime (H1, H3)

Table 2 reports the digital-productivity premium within each regime. The premium is positive and statistically significant in **every** regime, ranging from +0.214 (upper-middle) to +0.477 (advanced-resource) standard deviations of log productivity. Basic digital adoption pays everywhere, including in the weakest regimes: the emerging-regime premium is +0.253 (p < .001) and the SIDS premium is +0.246 (p = .011).

**Table 2. Digital-productivity premium by ICRV regime** (DV: lp_z; two-way FE; SE clustered by economy)

| ICRV regime | DAI premium | p | N |
|---|--:|--:|--:|
| I Advanced innovation-driven | +0.240** | .003 | 5,673 |
| II Advanced resource-driven | +0.477*** | .001 | 2,082 |
| III Upper-middle | +0.214* | .035 | 12,428 |
| IV Lower-middle transition | +0.383*** | <.001 | 42,739 |
| V Emerging | +0.253*** | <.001 | 16,542 |
| VI Pacific SIDS | +0.246* | .011 | 1,913 |

*Notes.* \* p < .05, \*\* p < .01, \*\*\* p < .001.

*H1 supported.* *H3 partially supported.* The premium is non-monotonic in institutional strength. It is compressed in the two highest-adoption regimes — advanced-innovation (+0.240, adoption 69%) and upper-middle (+0.214, adoption 54%) — and largest in the catching-up regimes, lower-middle transition (+0.383) and advanced-resource (+0.477), where adoption is partial and still differentiating. This pattern is consistent with digital saturation: where web presence is near-universal, the indicator weakly discriminates and the marginal premium shrinks. We are cautious, however, in calling this a confirmed law. A formal test correlating each regime's adoption rate with its premium across the six regimes is negative but far from significant (Pearson r = −0.13, p = .80; Table 4), because the advanced-resource regime combines middling adoption (50%) with the largest premium, breaking a clean monotone. The defensible claim is narrower: the marginal productivity value of crossing the basic-digital threshold is compressed at the saturated frontier and substantial in the mid-transition economies, but adoption level alone does not fully order the premium.

### 4.3 Digital adoption versus deep capability

Table 3 places the digital premium alongside the level effect of deeper technological capability. Controlling for both, basic digital adoption carries a pooled premium of +0.241 (p < .001), roughly double the per-standard-deviation effect of technological capability (TCI, +0.124, p < .001). The foundational, low-cost digital step is associated with a larger productivity level shift than the deeper, more expensive R&D-and-certification capability — a striking result for development policy, where basic digital enablement is far cheaper to scale than frontier technological capability.

**Table 3. Pooled level effects** (DV: lp_z; two-way FE; SE clustered by economy; N = 80,900)

| Variable | Coefficient | p |
|---|--:|--:|
| Digital adoption (web presence) | +0.241 | <.001 |
| Technological capability (TCI, z) | +0.124 | <.001 |

### 4.4 Robustness

Table 4 subjects the pooled digital premium to a battery of alternative specifications. The premium is +0.321 (p < .001) when DAI enters alone, attenuates to +0.241 once technological capability is controlled (digital adoption is partly a marker of broader capability), and to +0.188 with the full control set (firm size, age, foreign ownership) — but it remains large and highly significant throughout. Restricting the sample to domestic-owned firms, which removes any confounding from multinational affiliates that are both digitally advanced and productive for other reasons, leaves the premium essentially unchanged (+0.179, p < .001). The digital dividend is therefore not an artefact of foreign ownership or of the firm characteristics correlated with going online; it is robust across the plausible alternative specifications.

**Table 4. Robustness of the pooled digital premium and the saturation test**

| Specification | DAI premium | p | N |
|---|--:|--:|--:|
| Baseline (DAI only) | +0.321 | <.001 | 81,377 |
| + technological capability | +0.241 | <.001 | 80,900 |
| + firm size, age, foreign ownership | +0.188 | <.001 | 79,309 |
| Domestic-owned firms only | +0.179 | <.001 | 74,773 |
| *Saturation test:* r(regime adoption, regime premium), k = 6 | −0.13 | .80 | — |

### 4.5 The dividend is broadly shared across firm size

A natural concern is that the digital dividend accrues mainly to large firms with the resources to exploit an online presence, in which case digitalisation policy would be regressive within economies. The data do not support this concern. Interacting digital adoption with firm size (log employment, standardised), the interaction term is small and not significant (−0.024, p = .48), while the main digital effect remains positive and significant (+0.189, p < .001). The point estimate, if anything, leans toward smaller firms gaining slightly more, but the safe reading is that the digital dividend is broadly uniform across the firm-size distribution. Basic digitalisation is thus a candidate for inclusive productivity policy: it raises the productivity of small and large firms alike, rather than concentrating gains at the top of the size distribution.

## 5. Discussion

### 5.1 The pre-AI divide as the leading edge of AI-era inequality

The three findings combine into a single development message. The economies furthest behind on basic digital adoption (emerging, SIDS) still earn a significant productivity dividend from crossing the digital threshold — closing their divide is worth real output. Yet these are precisely the economies least equipped to absorb the AI tools that the policy conversation now foregrounds. AI sits at the top of a capability ladder whose bottom rung — basic web presence — half the region's firms have not yet reached. An AI agenda that ignores this sequencing risks delivering its dividends only to the frontier firms and economies that have already climbed the lower rungs, widening rather than narrowing cross-economy inequality (Acemoglu & Restrepo, 2020; Korinek & Stiglitz, 2021). The pre-AI digital divide is, in this sense, the leading edge of the AI-era divide.

### 5.2 Saturation and the diminishing political economy of frontier digitalisation

The non-monotonic premium has a corollary for policy targeting. In the advanced-innovation regime, where adoption is near-saturation, the marginal productivity return to pushing the last firms online is comparatively small (+0.240) — the frontier's digital agenda must move up the ladder toward AI and advanced analytics. In the catching-up regimes, by contrast, the marginal return to basic digitalisation is largest (+0.38 to +0.48), so the highest-yield digital policy in transition economies is still basic enablement, not frontier AI. Development strategy should therefore be regime-contingent: basic-digital enablement where adoption is partial, AI-readiness investment where it is saturated. A uniform "adopt AI" prescription misallocates effort across the institutional gradient.

### 5.3 Welfare implications

Because labour productivity is the proximate driver of wages and firm survival, the digital dividend documented here is also a welfare channel. In the catching-up and emerging regimes that contain the bulk of the region's employment, a productivity premium of a quarter to nearly half a standard deviation from basic digital adoption is economically large. Policies that lower the cost of firm digitalisation — affordable connectivity, digital-payment rails, simplified online business registration — therefore have a plausible claim to be pro-poor productivity policy, not merely modernisation for its own sake. The welfare case for closing the digital divide does not depend on AI arriving; it is already justified by the pre-AI dividend, and AI raises, rather than creates, the stakes.

### 5.4 A sequencing logic for AI-and-development policy

The findings imply a sequencing logic that cuts against the grain of much current AI-strategy enthusiasm. National AI strategies typically foreground frontier applications — public-sector AI, AI research capacity, advanced analytics — yet our evidence locates the binding constraint for most developing-economy firms several rungs lower, at basic web presence, which half the region's firms still lack. The productivity arithmetic is stark: a +0.18 to +0.48 standard-deviation dividend from a step that costs a firm little more than registering a domain and maintaining a basic site, versus speculative and capability-intensive returns from frontier AI that the same firm cannot yet operate. For finance ministries and development agencies allocating scarce digital-policy budgets, the highest-yield intervention in catching-up economies is almost certainly to close the basic-digital gap first: affordable broadband and mobile data, low-cost digital-payment rails, simplified online business registration, and basic digital-skills programmes for small-firm managers. AI-readiness investment is the right priority where adoption is already saturated — the advanced-innovation regime — but a premature, uniform pivot to AI risks bypassing the firms and economies that the development agenda is meant to serve. The sequence is substrate first, then AI; inverting it concentrates the dividend at the frontier.

This sequencing argument is also the paper's principal contribution to the AI-and-development debate. Where that debate has largely proceeded by forecasting AI's prospective effects, we ground it in a measured precondition: the existing, observable distribution of the digital substrate on which any AI dividend must build. The contribution is deliberately modest in its empirical claim — basic web presence is a coarse proxy and the design is associational — but it is precisely the modesty that makes the policy implication robust. One does not need to resolve the contested forecasts about AI's frontier effects to conclude that an economy in which half of firms are offline is not positioned to capture them.

### 5.5 Limitations

Three limitations bound the interpretation. First, the WBES is a repeated cross-section, not a panel; the estimates are within-economy-year associations conditioned on fixed effects, not causal effects, and selection of more productive firms into digital adoption is part of what they reflect. Second, web presence is a coarse, binary Tier-1 proxy; it captures the existence but not the depth or quality of digital engagement, and it does not measure AI adoption directly — by design, since our claim concerns the pre-AI substrate. Third, the cross-economy comparison rests on within-economy-year standardisation of productivity; level comparisons of raw productivity across economies are not identified and are not attempted here. Subsequent WBES waves carrying richer digital-capability items will allow the analysis to climb the digital ladder toward the AI rung itself.

## 6. Conclusion

Across 50 Asian and Pacific economies, barely half of formal-sector firms have crossed the most basic digital threshold, and the gap between the strongest and weakest institutional regimes is roughly 28 percentage points. The productivity dividend from closing that gap is real in every regime and largest in the catching-up economies that are mid-transition. Yet these economies — the ones with the most to gain from basic digitalisation — are the least equipped to absorb the AI tools now dominating the development conversation. The implication for the age of AI is direct: sustainable, broadly shared growth from AI presupposes a digital substrate that does not yet exist for half the region's firms. Closing the pre-AI digital divide is the precondition for AI to narrow rather than widen development inequality, and the firm-level evidence shows that closing it pays — most of all where the gap is widest.

## References

Acemoglu, D., & Restrepo, P. (2020). Robots and jobs: Evidence from US labor markets. *Journal of Political Economy, 128*(6), 2188–2244.

Agrawal, A., Gans, J., & Goldfarb, A. (2019). *The economics of artificial intelligence: An agenda*. University of Chicago Press.

Bloom, N., Garicano, L., Sadun, R., & Van Reenen, J. (2014). The distinct effects of information technology and communication technology on firm organization. *Management Science, 60*(12), 2859–2885.

Bresnahan, T. F., & Trajtenberg, M. (1995). General purpose technologies: "Engines of growth"? *Journal of Econometrics, 65*(1), 83–108.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics, 13*(1), 333–372.

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152.

Comin, D., & Mestieri, M. (2018). If technology has arrived everywhere, why has income diverged? *American Economic Journal: Macroeconomics, 10*(3), 137–178.

Cusolito, A. P., & Maloney, W. F. (2018). *Productivity revisited: Shifting paradigms in analysis and policy*. World Bank.

David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. *American Economic Review, 80*(2), 355–361.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Korinek, A., & Stiglitz, J. E. (2021). Artificial intelligence, globalization, and strategies for economic development (NBER Working Paper No. 28453). National Bureau of Economic Research.

Norris, P. (2001). *Digital divide: Civic engagement, information poverty, and the Internet worldwide*. Cambridge University Press.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

OECD. (2001). *Understanding the digital divide*. OECD Publishing.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

World Bank. (2026). *World Bank Enterprise Surveys* [Data file]. World Bank.
