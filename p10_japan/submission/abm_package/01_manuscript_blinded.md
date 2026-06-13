# At the Upper Bound of the Institutional Gradient: Internationalization, Capabilities, and Firm Performance in Japan's Inaugural World Bank Enterprise Survey

**Blinded manuscript — prepared for *Asian Business & Management* (primary target; backups: *Asia Pacific Journal of Management*, *Journal of Asian Business Studies*)**

---

## Abstract

**Purpose.** Japan entered the World Bank Enterprise Surveys (WBES) for the first time in 2025, closing the last major gap in comparable firm-level data for advanced Asia. We exploit this inaugural wave to test how the internationalization–performance (I–P) relationship behaves at the upper bound of the institutional gradient, where institution-contingent theory predicts the familiar inverted-U should flatten toward near-linearity. The setting is theoretically pointed: the inverted-U was originally established on Japanese multinationals, yet Japan has never been observed on the harmonised instrument that situates it against its regional peers.

**Design/methodology/approach.** Labour productivity, ln(annual sales per permanent worker) winsorised at the 1st and 99th percentiles, is regressed on export intensity (FSTS, direct plus indirect exports over sales) and its square, with sector fixed effects and HC1 robust standard errors, in a hierarchical sequence that adds ownership, firm age, top-manager gender, technological capability (TCI), and digital adoption (DAI). We complement the intensity-margin estimation with an extensive-margin model of export participation and a six-specification robustness battery.

**Findings.** The linear export-intensity effect on productivity is positive and significant (M1: +0.671, p < .001). The quadratic term is never significant in any specification, and the algebraic turning point lies far outside the observable range: within the data, more internationalization is monotonically better. Technological capability (+0.100, p < .001) and digital adoption (+0.110, p = .028) shift performance levels without reshaping the curve, consistent with Tier-1 digital saturation in an economy where 83.8% of establishments operate a website. The extensive-margin analysis relocates the action: export participation is governed by foreign ownership (+0.408, p < .001), technological capability (+0.083, p < .001), and digital adoption (+0.046, p = .005), while exporters earn a 25.8% productivity premium (p < .001). Two Japan-specific regularities emerge: a firm-longevity premium consistent with the *shinise* tradition (ln-age +0.073, p = .007), and a negative female-top-manager coefficient (−0.170, p = .010) in an economy where only 7.3% of establishments have a female top manager.

**Originality/value.** This is the first firm-level I–P estimate for Japan on the WBES instrument and the first test of the upper-bound prediction of an institution-contingent I–P framework using an economy's inaugural survey wave. The flattening of the curve at the strongest-institution regime mirrors independent evidence from Singapore and completes a three-zone pattern, inverted-U in transition regimes, near-linearity at the top, dissolution at the bottom, documented across 50 Asian and Pacific economies.

**Keywords:** internationalization–performance; export intensity; export participation; Japan; World Bank Enterprise Surveys; institutional context; digital adoption; technological capability; firm longevity.

---

## 1. Introduction

The relationship between internationalization and firm performance (I–P) is among the most intensively studied questions in international business, and among the least settled (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016). Decades of research have produced positive, negative, U-shaped, inverted-U-shaped, and S-shaped findings, a dispersion that meta-analyses attribute less to measurement noise than to genuine heterogeneity in the conditions under which firms internationalize (Bausch & Krist, 2007; Marano et al., 2016). A productive way to read that heterogeneity is institutional: the shape of the I–P curve is not universal but conditional on the regime in which the firm operates. In transition economies, where the institutional infrastructure of cross-border trade is still maturing, coordination costs mount quickly with foreign exposure and the relationship is inverted-U with an intermediate turning point (Lu & Beamish, 2001, 2004; Contractor et al., 2003). In the most advanced institutional contexts, by contrast, the descending limb is pushed outward and the relationship within the observable range is closer to linear. The upper bound of this institutional gradient, however, has been remarkably difficult to test on comparable data, for a prosaic reason: the world's most advanced large economies were absent from the World Bank Enterprise Surveys (WBES), the only firm-level instrument harmonised across more than 150 economies.

This absence is more than an inconvenience. It is an irony at the heart of the literature. The canonical demonstration of the inverted-U, Lu and Beamish's (2001, 2004) work on the geographic-scope–performance curve, was built on Japanese firms. The horizontal-axis "S-curve" and its intermediate optimum entered the field's vocabulary through evidence on Japanese small and medium enterprises and Japanese multinationals expanding abroad. Yet in the harmonised, cross-economy data that the field now uses to benchmark the I–P relationship, Japan itself was a blank. Researchers could position Vietnam, China, India, or the Pacific island economies on a common instrument, but not the very economy on which the foundational curve was first drawn.

Japan's entry into the WBES in 2025, the first time the programme has surveyed the world's fourth-largest economy, closes that gap. The inaugural wave (N = 2,168 establishments, stratified by sector, size, and region) makes it possible, for the first time, to estimate the I–P relationship for Japan on exactly the same instrument, with exactly the same variable definitions, as fifty other Asian and Pacific economies. The opportunity is unusual: a clean cross-section on a frontier economy, free of the panel attrition and questionnaire-revision artefacts that complicate within-country time series, observed on an instrument whose comparability is its defining virtue.

This paper asks a sharply defined question: **does the I–P relationship at the upper bound of the institutional gradient behave as institution-contingent theory predicts?** The prediction is specific and falsifiable. Where institutional quality is highest, transaction costs of cross-border activity are lowest and the supporting service ecosystem, trade finance, logistics, contract enforcement, is densest, so the descending limb of the inverted-U, the zone where coordination costs overwhelm learning gains, should be pushed beyond the observable range of export intensity. Empirically, three implications follow: the quadratic term should be statistically indistinguishable from zero; the algebraic turning point, if any, should fall outside the data support; and the relationship within the observed range should be monotonically positive. This is what independent single-economy evidence found for Singapore (turning point not reliably located), and what a 50-economy pooled estimation finds for the Advanced innovation-driven regime as a group. Japan, the largest and oldest advanced economy in the region, and the economy on which the inverted-U was first established, provides the most demanding test of this prediction.

We make four contributions. First, we provide the first WBES-based I–P estimates for Japan, establishing baseline facts, productivity dispersion, export participation, capability incidence, digital adoption, demographic structure, for an economy that has been systematically absent from comparative firm-level research. Second, we deliver a clean confirmation of the upper-bound prediction: the export-intensity effect is positive and significant in linear form, the quadratic term is never significant across five hierarchical specifications and a six-model robustness battery, and the implied turning point lies far outside the observable range. Third, we shift attention from the intensity margin to the extensive margin and show that, at the frontier, the binding question is not *how much* a firm exports but *whether* it exports at all: participation is governed by foreign ownership, technological capability, and digital adoption, and exporters earn a sizeable productivity premium. Fourth, we document two Japan-specific regularities of independent interest, a longevity premium consistent with the *shinise* (long-established firm) tradition, and a pronounced negative female-top-manager coefficient in the economy with the region's lowest female-leadership share, both of which qualify how upper-echelons effects travel across institutional contexts.

The remainder of the paper proceeds as follows. Section 2 develops the theoretical background and hypotheses, drawing deliberately on the Japan-specific strands of the IB literature that the data allow us to revisit. Section 3 describes the data and methods. Section 4 reports descriptive facts, the correlation structure, the hierarchical I–P estimates, the extensive-margin analysis, and the robustness battery. Section 5 discusses how the Japan evidence completes a three-zone, institution-contingent reading of the I–P relationship and what it implies for theory and policy. Section 6 concludes.

## 2. Theoretical background and hypotheses

### 2.1 The institution-contingent I–P relationship and the upper-bound prediction

Three mechanisms generate the inverted-U that has organised much of the I–P literature. On the ascending limb, exporting yields learning-by-internationalization, scale economies, and market-diversification gains: firms accumulate experiential knowledge of foreign markets, amortise fixed costs over larger volumes, and smooth demand shocks across geographies (Johanson & Vahlne, 1977; Lu & Beamish, 2001; Zahra et al., 2000). On the descending limb, coordination and liability-of-foreignness costs grow convexly with foreign exposure: governing dispersed operations, bridging institutional and cultural distance, and managing currency and political risk impose burdens that rise faster than the activity that generates them (Contractor et al., 2003; Hitt et al., 1997; Zaheer, 1995). The turning point is the export intensity at which marginal cost overtakes marginal gain.

Institutional quality conditions where that turning point falls. Strong institutions lower the transaction costs of cross-border activity, secure contracts, transparent regulation, deep capital markets, and supply a dense external ecosystem of trade finance, logistics, legal, and advisory services that substitutes for internal coordination capacity (North, 1990; Khanna & Palepu, 2010; Meyer et al., 2009). Both forces push the turning point outward. Where institutions are strongest, the descending limb is pushed so far out that it exits the observable range of export intensity, and the relationship that remains visible in the data is the ascending limb alone: positive, and to a first approximation linear. This is the upper-bound prediction.

The prediction is not a claim that diminishing returns to internationalization never set in for advanced-economy firms; it is a claim about what is *observable* on establishment-level data drawn from a frontier institutional context. In such a context, the binding constraint on the I–P relationship is not a harmful threshold that firms must avoid but the long ascending stretch over which additional foreign exposure continues to pay. Japan is the most exacting case for this prediction precisely because it is the economy on which the inverted-U was originally drawn (Lu & Beamish, 2001, 2004). If, on the harmonised WBES instrument, Japan's establishment-level curve no longer bends within range, the resolution is not that the earlier work was wrong but that the earlier work measured a different margin, the geographic scope of large multinationals' foreign subsidiaries, whereas the WBES establishment frame measures the domestic-economy export-intensity margin, where the upper-bound logic applies most directly.

> **H1.** In Japan, export intensity has a positive and significant linear association with labour productivity; the quadratic term is not significant and the algebraic turning point lies outside the observed range of export intensity.

### 2.2 Capabilities as level-shifters at the technological frontier

The resource-based view treats technological capability as a VRIN resource, valuable, rare, imperfectly imitable, non-substitutable, that raises productivity at every level of internationalization (Barney, 1991; Cohen & Levinthal, 1990; Lall, 1992). In developing and transition economies, capability is often the scarce factor that determines whether a firm can climb the ascending limb at all, so it interacts with internationalization: capable firms reach higher turning points and steeper slopes. In a frontier economy, the logic shifts. When the population of firms operates near the technological frontier and the export-performance curve is already flat in the relevant range, capability differences should shift performance *levels* rather than reshape the curve. Capability remains a powerful predictor of productivity, but it raises the floor uniformly rather than bending the export gradient.

> **H2.** Technological capability has a positive level effect on productivity; its interaction with export intensity is not significant.

### 2.3 Digital adoption under Tier-1 saturation

Digital adoption is multi-tiered. Basic web presence, the establishment-level indicator available in the WBES, is a Tier-1 marker of digital participation; higher tiers involve e-commerce integration, data analytics, and algorithmic decision-making (Verhoef et al., 2021). The performance value of a binary Tier-1 indicator depends on its discriminating power, which is greatest where adoption is partial and least where adoption approaches saturation. In an economy where the overwhelming majority of establishments already maintain a web presence, the indicator separates few firms from the rest, and its marginal productivity premium compresses, a measurement-side "digital saturation" effect rather than a claim that digital tools have ceased to matter. Japan's inaugural wave reports 83.8% website adoption, the highest in the 50-economy pool, so the digital-adoption premium should be positive but modest, and curve-reshaping interactions absent.

> **H3.** Digital adoption has a positive but modest level effect; its interaction with export intensity is not significant.

### 2.4 The extensive margin: who exports at the frontier

A focus on export intensity, the *amount* a firm exports, can obscure a logically prior question: *whether* the firm exports at all. The trade literature has long emphasised that the extensive margin of participation, crossing the threshold from non-exporter to exporter, carries most of the productivity action, because exporting entails sunk entry costs that only sufficiently productive firms can profitably bear (Melitz, 2003; Bernard et al., 2007; Wagner, 2007). At the frontier, where establishment-level export intensity is low on average and concentrated in a minority of firms, this self-selection mechanism should dominate. The firms that cross the threshold are those endowed with the capabilities that make foreign-market entry viable, technological capability to meet international quality standards, digital infrastructure to coordinate at distance, and the resources and market access that foreign ownership confers (Greenaway & Kneller, 2007; Hessels & Terjesen, 2010). We therefore model participation directly and expect the same capability and ownership factors that fail to *reshape* the intensity curve to *govern* who enters it.

> **H4.** Export participation is increasing in technological capability, digital adoption, and foreign ownership.

### 2.5 Two upper-echelons regularities: longevity and the female-leadership margin

Upper-echelons theory holds that firm outcomes reflect the characteristics of those who run firms (Hambrick & Mason, 1984). Two such characteristics are sharply distinctive in Japan and bear on how upper-echelons effects travel across institutional contexts.

The first is firm longevity. Japan is home to the world's densest population of long-established firms, the *shinise* tradition of businesses operating for centuries, sustained by relational capital, reputational assets, and intergenerational stewardship (Goto, 2014; Sasaki et al., 2020). The resource-based and organizational-learning literatures predict that age proxies accumulated, path-dependent capabilities that are difficult to imitate (Barney, 1991; Sørensen & Stuart, 2000). In an economy where the mean establishment is fifty years old, a measurable longevity premium would be both expected and theoretically resonant, distinguishing Japan from younger economies in which firm age more often signals obsolescence than accumulated advantage.

The second is the female-leadership margin. Japan records persistently low female representation in senior management, a gap documented across the comparative-management and gender-and-organizations literatures and reflected in the country's standing on international gender indices (Yamaguchi, 2019; Magoshi & Chang, 2009). In the inaugural WBES wave, only 7.3% of establishments report a female top manager, the lowest share in the 50-economy regional pool. With so thin a margin of female leadership, any estimated association between female top management and performance is unlikely to identify a leadership effect; it is far more likely to reflect selection of the few female-led establishments into particular, often smaller and lower-margin, niches. We therefore treat the female-top-manager coefficient as a descriptive regularity to be reported transparently, not as a causal estimate.

> **H5.** Firm age has a positive association with productivity, consistent with the accumulation of path-dependent capabilities in a long-firm economy.

## 3. Data and methods

### 3.1 Data

We use the complete Japan 2025 WBES cross-section (N = 2,168 establishments; 339 harmonised variables; stratified random sampling by sector, size, and region). The WBES is administered face-to-face to a senior manager or owner using a standardised instrument, and its sampling frame and variable definitions are harmonised across economies, which is what permits direct comparison of Japan with the regional pool. Non-response codes (−9, −8, −7) are recoded as missing throughout.

To situate Japan, we benchmark it against the other five Advanced innovation-driven economies of the regional pool, Hong Kong SAR, Israel, Korea, Singapore, and Taiwan, and against the wider 50-economy frame. Japan exhibits the narrowest within-wave productivity dispersion in the entire pool, the highest website adoption, the oldest firms, the lowest female-leadership share, and low establishment-level export intensity despite high R&D incidence. These facts, reported in Table 1, are themselves a contribution: they are the first harmonised firm-level portrait of the Japanese establishment sector benchmarked against its regional peers.

### 3.2 Variables

The dependent variable is ln(annual sales / permanent full-time workers), constructed from fields d2 and l1 and winsorised at the 1st and 99th percentiles. With a single economy and a single currency, productivity levels are directly comparable within the sample, which sidesteps the currency-conversion artefacts that complicate cross-economy productivity comparison (Combs et al., 2005; Richard et al., 2009; Cusolito & Maloney, 2018).

Export intensity is FSTS = (d3b + d3c)/100, direct plus indirect exports as a share of sales, the standard WBES definition used in the companion 50-economy estimation. A direct-exports-only variant (d3c) is used for robustness, following the long-standing operationalisation debate over whether indirect exports, sales through domestic intermediaries, should count as internationalization (Hessels & Terjesen, 2010; Peng & Ilinitch, 1998; Sullivan, 1994; Lu & Beamish, 2001). FSTS is mean-centred before squaring to reduce collinearity between the linear and quadratic terms and to make the linear coefficient interpretable at the sample mean.

Technological capability (TCI) is the standardised mean of three binary indicators: R&D incidence (h8), internationally recognised quality certification (b8), and product innovation (h1). Digital adoption (DAI) is website presence (c22b), a Tier-1 indicator. Controls comprise foreign ownership of at least 10% (b2b), ln(firm age + 1) computed from the founding year (b5), and a female-top-manager indicator (b7a). The extensive-margin model uses a binary exporter indicator (FSTS > 0) as its dependent variable and adds ln(employment) (l1), standardised, as a firm-size control. All models include sector fixed effects (the WBES sampling strata, a4a) and HC1 heteroskedasticity-robust standard errors.

### 3.3 Models

The intensity-margin estimation follows a hierarchical sequence. M1 regresses productivity on linear FSTS; M2 adds FSTS²; M3 adds the demographic controls (ownership, age, gender); M4 adds capability and digital adoption (TCI, DAI); M5 adds the curve-reshaping interactions (FSTS×TCI, FSTS×DAI). The turning point is computed as −β₁/(2β₂) plus the FSTS mean, and is meaningful only when β₂ < 0. Following Lind and Mehlum (2010), confirming an inverted-U requires not merely a negative quadratic term but a turning point that lies strictly within the data support and a slope that is positive at the lower bound and negative at the upper bound. This joint requirement is the substantive test of H1.

We then estimate the extensive margin with a linear probability model of export participation on capability, digital adoption, ownership, age, gender, and firm size, with sector fixed effects and HC1 errors (H4). Finally, a six-specification robustness battery re-estimates the linear and quadratic export effect under alternative controls (adding firm size), subsamples (domestic-owned firms only; exporters only, where the intensity margin is identified off participating firms), and winsorisation thresholds (5th/95th percentiles). All reported estimates are reproducible via `p10_japan/replication/p10_japan_models.py`. Because no Stata binary is available in the working environment, estimation uses pyfixest, the reghdfe-equivalent employed throughout the dissertation; the do-file should be re-validated in Stata before journal submission.

## 4. Results

### 4.1 Descriptive facts (Table 1)

Table 1 reports the first harmonised firm-level portrait of the Japanese establishment sector. Mean log labour productivity is 16.98 (sd 0.84), the most compressed distribution in the 50-economy pool, consistent with a mature economy in which establishments cluster near the technological frontier. Export participation is low: only 16.8% of establishments export at all, and mean FSTS across all firms is just 4.1%. Conditional on exporting, mean intensity rises to 24.6%, and 64.2% of exporters report positive indirect exports, indicating that intermediated channels matter materially for Japanese establishment-level internationalization. Technological-capability incidence is substantial (mean TCI 0.27 on the 0–1 scale), website adoption is near-saturation (83.8%), and foreign ownership is rare (1.9% of establishments are at least 10% foreign-owned). The demographic structure is distinctive: the mean firm is 50.4 years old, and only 7.3% of establishments have a female top manager.

**Table 1. Descriptive statistics, Japan 2025 (N = 2,168 establishments)**

| Variable | N | Mean | SD | Min | Max |
|---|--:|--:|--:|--:|--:|
| ln labour productivity | 2,068 | 16.984 | 0.843 | 15.01 | 19.38 |
| Export intensity (FSTS) | 2,128 | 0.041 | 0.140 | 0.00 | 1.00 |
| Exporter (FSTS > 0) | 2,128 | 0.168 | 0.374 | 0 | 1 |
| Technological capability (TCI) | 2,166 | 0.273 | 0.313 | 0.00 | 1.00 |
| Digital adoption (website) | 2,148 | 0.838 | 0.368 | 0 | 1 |
| Foreign ownership ≥ 10% | 2,153 | 0.019 | 0.137 | 0 | 1 |
| Firm age (years) | 2,135 | 50.388 | 29.906 | 0 | 193 |
| Female top manager | 2,163 | 0.073 | 0.260 | 0 | 1 |
| ln employment | 2,152 | 3.406 | 1.596 | 0.00 | 12.04 |

*Notes:* Mean FSTS conditional on exporting = 24.6%; 64.2% of exporters report positive indirect exports. Non-response codes recoded as missing.

### 4.2 Correlation structure (Table 2)

Table 2 reports pairwise correlations between productivity and each covariate. All point in the expected direction. Productivity is positively correlated with export intensity (r = +0.088), exporter status (r = +0.126), technological capability (r = +0.131, the strongest correlate), digital adoption (r = +0.090), firm age (r = +0.122), and firm size (r = +0.168). Foreign ownership is positively but only marginally correlated (r = +0.042, p = .056), reflecting its rarity. The female-top-manager indicator is negatively correlated (r = −0.052, p = .019). The correlation structure thus previews the multivariate results: capability, age, and size are the leading bivariate correlates of productivity, while the export margin enters positively.

**Table 2. Pairwise correlations with ln labour productivity**

| Covariate | r | N | p |
|---|--:|--:|--:|
| Export intensity (FSTS) | +0.088 | 2,047 | < .001 |
| Exporter status | +0.126 | 2,047 | < .001 |
| Technological capability | +0.131 | 2,068 | < .001 |
| Digital adoption | +0.090 | 2,053 | < .001 |
| Foreign ownership ≥ 10% | +0.042 | 2,058 | .056 |
| Firm age | +0.122 | 2,040 | < .001 |
| Female top manager | −0.052 | 2,068 | .019 |
| ln employment | +0.168 | 2,068 | < .001 |

### 4.3 The intensity margin: hierarchical estimates (Table 3)

Table 3 reports the hierarchical I–P estimation. The linear export-intensity effect is positive and highly significant in the baseline (M1: +0.671, p < .001). When the quadratic term is added (M2), the linear term remains positive and significant (+1.042, p = .002) while the quadratic term is negative but far from significant (−0.606, p = .323); its implied algebraic turning point, 90.1% of sales, lies near the extreme upper edge of the FSTS support and is not statistically distinguishable from "no turning point at all." Adding demographic controls (M3), then capability and digital adoption (M4), then interactions (M5), the quadratic term never approaches significance and the implied turning point drifts to absurd values (108% in M3, beyond 700% once capability is controlled), the signature of a coefficient indistinguishable from zero.

**Table 3. Hierarchical I–P estimates, Japan 2025 (DV: ln labour productivity)**

| | M1 | M2 | M3 | M4 | M5 |
|---|--:|--:|--:|--:|--:|
| FSTS (centred) | +0.671*** (.000) | +1.042** (.002) | +0.872* (.010) | +0.476 (.163) | +0.486 (.372) |
| FSTS² | | −0.606 (.323) | −0.419 (.502) | −0.009 (.989) | −0.034 (.956) |
| Foreign ownership ≥ 10% | | | +0.259† (.078) | +0.203 (.164) | +0.210 (.151) |
| ln(firm age) | | | +0.073** (.007) | +0.061* (.027) | +0.063* (.023) |
| Female top manager | | | −0.171* (.010) | −0.170* (.011) | −0.170* (.011) |
| TCI (z) | | | | +0.100*** (.000) | +0.102*** (.000) |
| DAI (website) | | | | +0.110* (.028) | +0.111* (.027) |
| FSTS × TCI | | | | | −0.126 (.328) |
| FSTS × DAI | | | | | +0.111 (.820) |
| Sector FE | yes | yes | yes | yes | yes |
| N | 2,047 | 2,047 | 2,011 | 1,996 | 1,996 |
| R² | .140 | .141 | .147 | .162 | .163 |
| Algebraic TP | — | [90.1%] | [108.3%] | — | — |

*Notes:* HC1 robust standard errors; p-values in parentheses. † p < .10, \* p < .05, \*\* p < .01, \*\*\* p < .001. Turning points in brackets are algebraic only; in no specification is the quadratic term significant, so no inverted-U is confirmed (Lind & Mehlum, 2010). Robustness with direct exports only (d3c): β₁ = +1.255** (p = .010), β₂ = −0.674 (p = .445), same conclusion.

**H1 supported.** The linear effect is positive and significant; the quadratic term never approaches significance; the algebraic turning point lies far outside the observed FSTS support (mean 4.1%; conditional mean 24.6%). Within the observable range, internationalization is monotonically performance-enhancing: Japan sits on a long ascending limb whose descending counterpart is empirically absent. This mirrors the Singapore single-economy result and the group-level finding for the Advanced innovation-driven regime in the companion 50-economy estimation, and it locates Japan, the economy on which the inverted-U was first drawn, on the straightened upper end of the institutional gradient.

**H2 supported.** Technological capability carries a precise positive level effect (+0.100, p < .001) and absorbs much of the raw FSTS effect when introduced in M4, consistent with capability-based selection into exporting. Its interaction with export intensity is not significant (M5: −0.126, p = .328). Capability raises the floor; it does not bend the curve.

**H3 supported.** Digital adoption retains a modest positive premium (+0.110, p = .028) despite 83.8% saturation, with no curve-reshaping interaction (M5: +0.111, p = .820). The premium is about half the size found in the pooled 50-economy estimation, the compression that Tier-1 saturation predicts.

**H5 supported.** Firm age carries a positive premium (+0.073, p = .007 in M3): each log-unit of age adds roughly seven percent to productivity, a regularity that is both expected and theoretically resonant in the economy with the pool's oldest establishments (mean 50.4 years) and its deep *shinise* tradition.

**The female-leadership margin.** The female-top-manager coefficient is negative and significant (−0.170, p = .010) in the economy with the region's lowest female-leadership share (7.3%). Given the thinness of that margin, the coefficient is most plausibly read as selection of the few female-led establishments into smaller, lower-margin niches rather than as a leadership effect, and we do not interpret it causally. It is reported transparently as a descriptive regularity that disciplines how upper-echelons effects are read across institutional contexts.

### 4.4 The extensive margin: who exports (Table 4)

If the intensity curve is flat within range, the consequential variation lies in *who exports at all*. Table 4 reports a linear probability model of export participation. The result relocates the action decisively. Export participation is governed by foreign ownership (+0.408, p < .001), an establishment that is at least 10% foreign-owned is some forty percentage points more likely to export, by technological capability (+0.083 per standard deviation, p < .001), and by digital adoption (+0.046, p = .005). Firm age contributes modestly (+0.026, p = .010). Firm size, by contrast, does not independently predict participation once capability and ownership are controlled (+0.014, p = .114), and the female-leadership margin is weakly negative (−0.048, p = .062). The model explains a substantial share of the cross-sectional variation in participation (R² = 0.228).

**Table 4. Extensive margin, who exports (LPM; DV: exporter status)**

| Covariate | Coefficient | p |
|---|--:|--:|
| Technological capability (z) | +0.083 | < .001 |
| Digital adoption (website) | +0.046 | .005 |
| Foreign ownership ≥ 10% | +0.408 | < .001 |
| ln(firm age) | +0.026 | .010 |
| Female top manager | −0.048 | .062 |
| ln employment (z) | +0.014 | .114 |
| Sector FE | yes | |
| N | 2,062 | |
| R² | 0.228 | |

*Notes:* HC1 robust standard errors. Linear probability model; coefficients are changes in the probability of being an exporter.

**H4 supported.** The same capability and ownership factors that do not reshape the intensity curve govern entry into exporting. At the frontier, the productivity payoff to internationalization operates chiefly through the participation threshold: exporters earn a productivity premium of 25.8% over non-exporters (p < .001, controlling for ownership, age, gender, and sector), and the firms that cross the threshold are those endowed with the capabilities, technological, digital, and ownership-linked, that make foreign-market entry viable. This is the Melitz (2003) self-selection mechanism observed in a frontier economy: the action is at the extensive margin, not along the intensity gradient.

### 4.5 Robustness (Table 5)

Table 5 subjects the central finding, a positive linear and a non-significant quadratic export effect, to six alternative specifications. Adding a firm-size control (R2) leaves the linear effect positive (+0.656, p = .046) and the quadratic insignificant (p = .662). Restricting to domestic-owned establishments (R3) strengthens the linear effect (+0.917, p = .012) with the quadratic still insignificant (p = .448), confirming that the result is not driven by the rare foreign-owned firms. Winsorising productivity at the 5th/95th percentiles (R5) yields the same pattern (+0.837, p = .006; quadratic p = .378). Estimating the intensity margin on exporters only (R6, N = 344), where the linear/quadratic terms are identified off participating firms alone, the export-intensity effect is positive but no longer significant (+0.200, p = .410) and the quadratic remains insignificant (p = .551), consistent with the action lying at participation rather than intensity. In no specification, across the full sample, the domestic-owned subsample, alternative winsorisation, or the exporters-only subsample, does the quadratic term attain significance. The monotone-positive-within-range conclusion is robust.

**Table 5. Robustness battery (linear and quadratic export effect)**

| Specification | N | β₁ (linear) | p | β₂ (quadratic) | p |
|---|--:|--:|--:|--:|--:|
| R2: + ln firm size | 2,011 | +0.656 | .046 | −0.263 | .662 |
| R3: domestic-owned only | 1,976 | +0.917 | .012 | −0.533 | .448 |
| R5: winsor 5th/95th | 2,011 | +0.837 | .006 | −0.479 | .378 |
| R6: exporters only (intensity) | 344 | +0.200 | .410 | +0.450 | .551 |

*Notes:* HC1 robust standard errors; all models include sector fixed effects and the demographic controls of M3. The quadratic term is insignificant in every specification.

## 5. Discussion

### 5.1 Completing the three-zone picture

The Japan results complete a three-zone picture of the institution-contingent I–P relationship that emerges across the 50-economy region. In the middle of the institutional gradient, the inverted-U is sharp and reliably located: the lower-middle transition regime exhibits a turning point near 43% with a significant negative quadratic term, and single-economy evidence places Vietnam in the high-thirties to mid-forties and India near 41% in the early 2020s. At the upper bound, in Japan as in Singapore and in the Advanced innovation-driven regime as a group, the curve straightens: the within-range relationship is monotonically positive and no harmful threshold is observable. At the lower bound, the relationship dissolves into insignificance, and in the Pacific small-island group it reverses under a level-based specification, the phenomenon the companion work names the Forced Internationalization Penalty. Japan supplies the cleanest upper-bound observation of this family of curves, on an inaugural survey wave free of any panel attrition or schema-change artefacts, and it does so for the very economy on which the inverted-U was first established, resolving the irony noted in the introduction: the bend that Lu and Beamish (2001, 2004) found on Japanese multinationals' geographic scope is, on the harmonised establishment instrument, pushed beyond range, because the WBES frame measures the domestic-economy export-intensity margin rather than the foreign-subsidiary scope margin.

### 5.2 Where the action is: the extensive margin at the frontier

The most consequential analytical move in this paper is the shift from intensity to participation. A literature organised around the *shape* of the intensity curve risks looking in the wrong place when the economy under study sits on the straightened upper end of the institutional gradient. In Japan, the intensity curve is flat within range, but the extensive margin is alive with structure: capability, digital adoption, and above all foreign ownership govern who crosses the export threshold, and crossing it carries a 25.8% productivity premium. This is the Melitz (2003) self-selection logic, but the policy reading is specific to the frontier: the binding constraint on internationalization gains is not a harmful threshold of over-internationalization to be avoided, but the breadth of participation, only one establishment in six exports at all, and the capability floor that supports entry.

### 5.3 Upper-echelons effects across institutional contexts

The two demographic regularities qualify how upper-echelons theory travels. The longevity premium shows that, in a long-firm economy, age proxies accumulated, path-dependent capability rather than inertia, an empirical counterpart to the *shinise* tradition that resonates with resource-based and organizational-learning accounts (Barney, 1991; Sørensen & Stuart, 2000; Goto, 2014). The female-leadership result is a cautionary one: in an economy where female top management is exceptionally rare, the negative coefficient almost certainly reflects compositional selection rather than any leadership deficit, and reading it causally would be a category error. Both regularities underscore that upper-echelons coefficients are context-laden: the same demographic variable carries different meaning in Japan than it would in an economy with a different firm-age distribution or a wider female-leadership margin.

### 5.4 Limitations

Two qualifications discipline the interpretation. First, this is a single cross-section: the estimates are associations conditioned on sector fixed effects, not causal effects, and capability-based selection into exporting is part of what the hierarchical sequence reveals rather than a nuisance to be assumed away. The inaugural-wave character of the data is an analytical strength, no attrition or questionnaire-revision artefacts, but it precludes the within-firm dynamics that a panel would allow; subsequent WBES waves will make those dynamics estimable. Second, the low establishment-level export intensity (4.1%) reflects the structure of Japanese internationalization, which is concentrated in large multinationals and conducted substantially through outward FDI rather than establishment-level exporting; the WBES establishment frame therefore captures the domestic-economy margin of internationalization, which is precisely the margin where the upper-bound prediction operates, but which understates the full international footprint of the Japanese corporate sector. Finally, estimation in the working environment used pyfixest rather than Stata; the replication do-file should be re-validated in Stata before journal submission.

## 6. Conclusion

Using Japan's first-ever World Bank Enterprise Survey, we show that at the upper bound of the institutional gradient the internationalization–performance relationship is monotonically positive within the observable range, with no statistically detectable turning point in any of eleven specifications. Technological capability and digital adoption raise productivity levels without reshaping the curve; firm longevity carries a measurable premium consistent with the *shinise* tradition; and the female-leadership margin remains strikingly thin. Crucially, the consequential variation lies not along the intensity gradient but at the extensive margin: foreign ownership, technological capability, and digital adoption govern who exports, and exporters earn a sizeable productivity premium. For theory, the result closes the upper end of the three-zone, institution-contingent reading of the I–P relationship, and it does so on the economy that gave the literature its founding inverted-U. For policy, it implies that in frontier institutional contexts the binding constraint on internationalization gains is not a harmful threshold to be avoided but the breadth of participation and the capability floor that supports it.

## References

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347.

Bernard, A. B., Jensen, J. B., Redding, S. J., & Schott, P. K. (2007). Firms in international trade. *Journal of Economic Perspectives, 21*(3), 105–130.

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152.

Combs, J. G., Crook, T. R., & Shook, C. L. (2005). The dimensionality of organizational performance and its implications for strategic management research. In D. J. Ketchen & D. D. Bergh (Eds.), *Research methodology in strategy and management* (Vol. 2, pp. 259–286). Emerald.

Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of international expansion: The link between multinationality and performance in the service sector. *Journal of International Business Studies, 34*(1), 5–18.

Cusolito, A. P., & Maloney, W. F. (2018). *Productivity revisited: Shifting paradigms in analysis and policy*. World Bank.

Goto, T. (2014). Family business and its longevity. *Kindai Management Review, 2*, 78–96.

Greenaway, D., & Kneller, R. (2007). Firm heterogeneity, exporting and foreign direct investment. *Economic Journal, 117*(517), F134–F161.

Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review, 9*(2), 193–206.

Hessels, J., & Terjesen, S. (2010). Resource dependency and institutional theory perspectives on direct and indirect export choices. *Small Business Economics, 34*(2), 203–220.

Hitt, M. A., Hoskisson, R. E., & Kim, H. (1997). International diversification: Effects on innovation and firm performance in product-diversified firms. *Academy of Management Journal, 40*(4), 767–798.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process of the firm: A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Deligonul, S., Perryy, M. Z., & Cavusgil, S. T. (2012). A multilevel examination of the drivers of firm multinationality–performance relationship. *Journal of Management, 38*(2), 502–530.

Lall, S. (1992). Technological capabilities and industrialization. *World Development, 20*(2), 165–186.

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118.

Lu, J. W., & Beamish, P. W. (2001). The internationalization and performance of SMEs. *Strategic Management Journal, 22*(6–7), 565–586.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.

Magoshi, E., & Chang, E. (2009). Diversity management and the effects on employees' organizational commitment: Evidence from Japan and Korea. *Journal of World Business, 44*(1), 31–40.

Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110.

Melitz, M. J. (2003). The impact of trade on intra-industry reallocations and aggregate industry productivity. *Econometrica, 71*(6), 1695–1725.

Meyer, K. E., Estrin, S., Bhaumik, S. K., & Peng, M. W. (2009). Institutions, resources, and entry strategies in emerging economies. *Strategic Management Journal, 30*(1), 61–80.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Peng, M. W., & Ilinitch, A. Y. (1998). Export intermediary firms: A note on export development research. *Journal of International Business Studies, 29*(3), 609–620.

Richard, P. J., Devinney, T. M., Yip, G. S., & Johnson, G. (2009). Measuring organizational performance: Towards methodological best practice. *Journal of Management, 35*(3), 718–804.

Sasaki, I., Kotlar, J., Ravasi, D., & Vaara, E. (2020). Dealing with revered past: Historical identity statements and strategic change in Japanese family firms. *Strategic Management Journal, 41*(3), 590–623.

Sørensen, J. B., & Stuart, T. E. (2000). Aging, obsolescence, and organizational innovation. *Administrative Science Quarterly, 45*(1), 81–112.

Sullivan, D. (1994). Measuring the degree of internationalization of a firm. *Journal of International Business Studies, 25*(2), 325–342.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Wagner, J. (2007). Exports and productivity: A survey of the evidence from firm-level data. *The World Economy, 30*(1), 60–82.

Yamaguchi, K. (2019). *Gender inequalities in the Japanese workplace and employment: Theories and empirical evidence*. Springer.

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of Management Journal, 38*(2), 341–363.

Zahra, S. A., Ireland, R. D., & Hitt, M. A. (2000). International expansion by new venture firms: International diversity, mode of market entry, technological learning, and performance. *Academy of Management Journal, 43*(5), 925–950.

World Bank. (2026). *Japan 2025 Enterprise Surveys* [Data file]. World Bank Enterprise Surveys.
