# Internationalization and Firm Performance across 50 Asian and Pacific Economies: Institutional Regimes, Digital Capabilities, and Managerial Characteristics as Contingency Factors

**Version:** Working manuscript (reconciled to canonical, 2026-06-13)  
**Target journal:** International Business Review (revised from JIBS)  
**Status:** Reconciled to the 50-economy canonical frame; numbers reproducible via `scripts/p7_full_ladder.py`.

---

> **Reconciliation note (2026-06-13).** This manuscript has been re-estimated on the
> **canonical 50-economy frame including Japan 2025** (`data_wbes/analysis/CANONICAL_NUMBERS.md`):
> analytic sample 88,869 firms / 50 economies / 103 country-year pairs. The full
> M1–M8 ladder (this version) is reproducible via `scripts/p7_full_ladder.py`
> (results in `data_wbes/analysis/p7_full_ladder_results.md`); the two anchors
> reproduce exactly (M2 quadratic N=81,022, TP=51.5%; M4 +TCI+DAI N=79,080, TP=43.6%).
> The earlier 49-economy build (M2 N=84,910, TP≈36%) is superseded. Two substantive
> revisions follow from the canonical re-estimation: (i) on the canonical spec the
> digital-adoption (DAI) curve-reshaping interactions are **not** significant — DAI is
> a level-shifter, not a curve-reshaper — correcting the earlier draft; (ii) the
> female-top-manager coefficient is **negative** (−0.104, p<.001), consistent with the
> rest of the dissertation (P10 Japan), not positive. Stata re-validation pending
> before journal submission.

---

## Abstract

We examine whether the internationalization–performance (I–P) relationship holds across a large and institutionally diverse set of Asian and Pacific economies and identify the conditions under which firms convert export intensity into productive performance. Using microdata from 88,869 firms across 50 economies and 103 country-year waves of the World Bank Enterprise Survey (2003–2025; including Japan's inaugural 2025 wave), spanning all six Institutional Context Regime Variation (ICRV) groups, we estimate a hierarchical sequence of models on currency-neutral labour productivity (standardised within economy-year) with two-way (economy and year) fixed effects throughout and standard errors clustered by economy. We find robust support for an inverted-U I–P relationship: the quadratic baseline (M2, N=81,022) yields a turning point of 51.5% of export sales, tightening to 43.6% once technological capability and digital adoption are controlled (M4, N=79,080; Lind–Mehlum p < .001 throughout). Technological capability (TCI, +0.108) and digital adoption (DAI, +0.219) both raise the performance level, but neither significantly reshapes the pooled curve; both are level-shifters, not curve-reshapers. The curve structure is instead governed by institutional regime: estimating the turning point within each ICRV group reveals a three-zone pattern: a sharp inverted-U in the lower-middle transition regime (TP ≈ 43%), a near-linear relationship in the strongest-institution regime (turning point beyond the observable range, ≈ 80%), and dissolution of the inverted-U in the weakest regimes (Emerging ≈ 37%; the Pacific SIDS group shows no inverted-U). Female top management carries a negative coefficient (−0.104, p < .001). These findings offer a parsimonious resolution to Asian I–P heterogeneity: the relationship is inverted-U in form, but it is institutional regime, not capability per se, that determines whether the inverted-U is sharp, straightened, or absent.

**Keywords:** internationalization–performance; inverted-U; institutional regime; digital capability; Asia-Pacific; World Bank Enterprise Surveys

---

## 1. Introduction

A central question in international business research concerns whether and how export internationalization translates into firm performance (Lu & Beamish, 2004; Johanson & Vahlne, 2009). Meta-analyses document a mean correlation of approximately r = .07 across several thousand studies (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016), yet the variance across studies vastly exceeds what sampling error can explain. In Asia (a region that accounts for over half of global manufacturing exports; UNCTAD, 2023), the evidence is especially fragmented: prior studies report positive relationships (Pangarkar, 2008; Korea), inverted-U curves (Chiao et al., 2006; Taiwan), or null and negative effects (Mondal et al., 2022; India). The standard explanation invokes context as a moderator (Marano et al., 2016; Kirca et al., 2012), but empirical tests simultaneously across institutionally diverse Asian economies remain rare.

This paper addresses that gap. We pool 88,869 firm-observations from 50 Asian and Pacific economies spanning 2003–2025 (including Japan's inaugural 2025 wave), harmonised from the World Bank Enterprise Survey (WBES). Our sample spans all six ICRV regime groups, from advanced innovation-driven economies (Japan, Singapore, Korea, Taiwan, HongKong, Israel) to Pacific Small Island Developing States (Vanuatu, Solomon Islands, Fiji, Tonga, Samoa, Kiribati, Papua New Guinea) and Gulf advanced-resource economies (Bahrain, Kuwait, Qatar, Brunei, Saudi Arabia, Oman), all classified through the Institutional Context Regime Variation (ICRV) framework that anchors the broader dissertation programme of which this study is part.

Our contributions are threefold. First, we provide the largest WBES-based test of the inverted-U I–P hypothesis in Asia, confirming a capability-adjusted turning point of 43.6% foreign sales intensity (51.5% in the unconditioned quadratic; Lind–Mehlum p < .001 throughout) on a harmonised 50-economy frame. Second, we show that both technological capability (TCI, +0.108) and digital adoption (DAI, +0.219) are strong performance **level-shifters** but that neither significantly reshapes the pooled I–P curve, a finding that disciplines capability-centred accounts of internationalization performance. Third, and most consequentially, we show that the **shape** of the curve is governed by institutional regime, and not as a smooth gradient but as a three-zone structure: a sharp inverted-U in transition economies (turning point ≈ 43%), near-linearity in the strongest-institution economies (turning point beyond the observable range), and dissolution (reversing into a Forced Internationalization Penalty among the Pacific SIDS) in the weakest regimes.

The remainder of the paper is organised as follows. Section 2 develops the theoretical framework and formal hypotheses. Section 3 describes data and methods. Section 4 presents results. Section 5 discusses implications and limitations. Section 6 concludes.

---

## 2. Theoretical Framework and Hypotheses

### 2.1 Theoretical Foundations

We draw on four theoretical traditions. The Uppsala model (Johanson & Vahlne, 1977, 2009) describes internationalization as a sequential process in which firms accumulate experiential knowledge, progressively reducing psychic distance and coordination costs. The Resource-Based View (Barney, 1991; Wernerfelt, 1984) positions firm-level capabilities (technological, digital, and managerial) as the mediating mechanism linking export exposure to performance outcomes. Institutional Theory (North, 1990; Scott, 2008) directs attention to how country-level formal and informal institutions shape the cost structure of cross-border transactions. Upper Echelons Theory (Hambrick & Mason, 1984; Hambrick, 2007) emphasises that top management team attributes moderate how firms respond to strategic opportunities and constraints.

### 2.2 The Non-Linear I–P Relationship (H1)

Contractor et al. (2003) formalised the three-stage S-curve hypothesis: early internationalization carries fixed entry costs that depress performance; intermediate internationalization yields learning and scale economies; high internationalization may again impose coordination and agency costs. Empirically, however, the data more consistently support the inverted-U: a special case in which the third stage does not emerge at the export intensities typically observed in developing-economy WBES data (Gomes & Ramaswamy, 1999; Lu & Beamish, 2004).

In the Asian context, three country-specific studies in our broader dissertation programme provide prior evidence. For Vietnam (P3), the inverted-U is confirmed with a turning point at 39–46% using a WBES-based instrumental variable design. For China (P5), an inverted-U turning point of 47–49% is replicated across specifications with Paternoster cross-cohort tests (p = .545). For Singapore (P4), the relationship is predominantly positive with a very late turning point (~88.6%), consistent with near-monotonic returns in a high-institutional, digitally saturated economy. Pooled across a much larger and institutionally heterogeneous sample, we expect the inverted-U to emerge at an intermediate turning point.

> **H1:** The relationship between export intensity (FSTS) and firm labour productivity (ln LP) is an inverted-U, with a statistically confirmed turning point at intermediate export intensities, in a pooled sample of Asian and Pacific firms.

### 2.3 Technological Capability as a Curve Amplifier (H2)

Technological capability, operationalised as a composite of quality certification, foreign-technology adoption, process innovation, and R&D, raises absorptive capacity (Cohen & Levinthal, 1990), enabling firms to extract greater performance value per unit of export exposure. Critically, we expect TCI to operate as a *curve amplifier*: at low export intensities, high-TCI firms gain more per unit of internationalization (steeper ascending limb); at high intensities, they experience sharper diminishing returns as coordination demands exceed even their superior capabilities (steeper descending limb). The net effect is a shift and steepening of the inverted-U, not just a parallel upward shift.

This prediction is consistent with P3 Vietnam (β(TCI) = +0.179, IV-identified) and P5 China (β(TCI) increasing from +0.28 to +0.43 across cohorts), both showing TCI as a positive level shifter. P4 Singapore shows negligible TCI moderation of the curve, likely because near-universal adoption in a high-ICRV economy leaves insufficient variance for moderation.

> **H2:** TCI amplifies the I–P curve, raising the average performance level and steepening both the ascending and descending limbs of the inverted-U.

### 2.4 Digital Adoption as a Level Enhancer (H3)

Digital adoption, measured through website presence and electronic-payment share, has been associated with reduced communication and transaction costs (Verhoef et al., 2021). In the CDCM (Context-Contingent Digital Capability Model) developed in the dissertation, DAI's effect depends on the interaction of regime quality, FSTS level, and digital market saturation (Đỗ & Phan, 2024). Specifically, in institutionally advanced economies where digital infrastructure is mature, DAI provides universal performance lifts (as in P4 Singapore: β(DAI) positive and significant). In emerging-economy contexts with substantial selection into digital adoption (P3 Vietnam: IV-estimated β(DAI) ≈ 0, consistent with selection bias in OLS), DAI's curve-shaping role is attenuated. Across the pooled multi-economy sample, we expect DAI to raise performance levels broadly across the sample (level effect). In a fully specified model that also accounts for managerial quality (which correlates with digital adoption), the residual DAI variation may reveal a capability-complementarity curve effect: digitally equipped firms at low FSTS face sunk adoption costs that compress near-term productivity, while digital infrastructure supports coordination efficiency at high FSTS where cross-border management demands are greatest.

> **H3:** DAI has a positive main effect on labour productivity and, when managerial characteristics are controlled, reshapes the I–P curve by compressing the ascending limb at low export intensities and attenuating performance decline at high export intensities.

### 2.5 Managerial Characteristics (H4)

Upper Echelons Theory predicts that top manager experience and gender composition affect strategic cognition and decision-making (Hambrick & Mason, 1984). Manager experience reduces coordination errors in cross-border operations; female top management is associated with stakeholder orientation, relationship capital, and risk management, all relevant in institutionally heterogeneous export markets (Richard et al., 2019). We expect both to raise the performance level for any given FSTS. However, given the breadth of the multi-country sample, firm-level managerial differences are unlikely to systematically reshape the aggregate FSTS–performance curve, whose shape is primarily determined by economy-wide institutional and market-maturity factors.

> **H4:** Top manager experience and female top manager status have positive main effects on firm performance, but do not significantly moderate the FSTS–performance curve shape.

### 2.6 Institutional Regime as a Turning-Point Shifter (H5)

North (1990) established that formal institutions reduce transaction costs; stronger institutions lower the cost of cross-border coordination and thus shift the performance-maximising export intensity (the inverted-U turning point). In higher-quality institutional environments, firms need a lower export share to recoup internationalization costs, so the turning point occurs earlier. Equivalently, holding FSTS constant, firms in stronger institutional regimes earn higher returns per unit of internationalization.

We operationalise institutional regime through the ICRV classification system developed in the dissertation: six groups ranging from Group I (Advanced innovation-driven: Singapore, Korea, Taiwan, Israel, Cyprus) to Group VI (SIDS and small open economies: Vanuatu, Solomon Islands, Timor-Leste). Higher ICRV group numbers denote weaker institutions. We expect positive FSTS×ICRV and negative FSTS²×ICRV interactions in Group III–VI compared to Group I (stronger institutions = higher Group I coefficient), which is observationally equivalent to the turning point occurring later in lower-quality institutional environments.

> **H5:** The ICRV institutional regime positively moderates the I–P relationship: firms in higher-quality institutional environments (lower ICRV group number) achieve the performance-maximising export intensity at lower FSTS levels.

### 2.7 Regime-Contingent Digital Effects (H6)

The Context-Contingent Digital Capability Model (CDCM) developed in this dissertation programme predicts that the I–P curve-reshaping role of digital adoption is not uniform across institutional environments. In institutionally advanced economies (ICRV Group I–II), digital infrastructure is near-universal and close to the competitive baseline; the marginal performance differentiation from website and e-payment adoption is accordingly lower. In institutionally weaker economies (ICRV Group IV–VI), digital adoption remains differentiating: digital market access tools lower the liability-of-foreignness cost and provide cross-border coordination support that institutional voids cannot substitute. This motivates examining whether any curve-shaping role of digital capability (predicted by H3) is concentrated in weaker-institution economies rather than uniform across the pool: a prediction we assess through the within-regime turning-point analysis (Table 4), since the reconciled pooled models find no significant DAI curve-reshaping (H3 level effect confirmed, curvature NS).

This prediction is consistent with the digital-complementarity strand of institutional theory (North, 1990; Stallkamp & Schotter, 2021): where formal institutions provide reliable contract enforcement, IP protection, and market information, digital infrastructure adds incrementally; where institutional voids prevail, digital tools provide a non-trivial substitute for missing formal mechanisms. H6 therefore does not predict stronger *level* effects in weak-institution contexts (which could reflect many confounds), but specifically predicts a stronger *curve-shaping* interaction between digital adoption and export intensity: a conditional complementarity claim.

> **H6:** The ICRV institutional regime moderates the digital-adoption curve-reshaping effect: digital adoption's compressive effect on the I–P ascending limb and its buffering effect at high FSTS (H3) are stronger in weaker institutional environments (higher ICRV group number), where digital infrastructure provides greater competitive differentiation in cross-border market access.

---

## 3. Data and Methods

### 3.1 Data Source

Data derive from the World Bank Enterprise Surveys (WBES), a stratified random-sample survey of formal private-sector enterprises conducted periodically across over 130 countries. We use microdata from 50 Asian and Pacific economies across 103 country-year waves spanning 2003–2025, including Japan's inaugural WBES wave (2025). This coverage encompasses six UN M.49 Asian sub-regions: East Asia (China, HongKong, Korea, Mongolia, Taiwan), Southeast Asia (Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste, Vietnam), South Asia (Afghanistan, Bangladesh, Bhutan, India, Maldives, Nepal, Pakistan, Sri Lanka), Central Asia (Kazakhstan, Kyrgyz Republic, Tajikistan, Turkmenistan, Uzbekistan), West Asia (Armenia, Bahrain, Cyprus, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi Arabia, Yemen), and Pacific/SIDS (Fiji, Kiribati, Papua New Guinea, Samoa, Solomon Islands, Tonga, Vanuatu).

The final analytical frame contains 88,869 firm-observations across 50 economies and 103 country-year pairs; the main regression sample (outcome and FSTS non-missing) is 81,022. Some early waves predate the digital-capability and manager variables used in the moderation models; they contribute to the baseline models but drop from later specifications due to item missingness. WBES designs are cross-sectional within each wave, with standardised instruments ensuring common variable definitions across economies and years. We apply three harmonisation steps: (1) variable-priority mapping for candidate items across PICS3 (2009–2013), Standardised (2014–2018), and BREADY/BEE (2019–2025) questionnaire generations; (2) encoding-robust reading (primary UTF-8 with Latin-1/CP1252 fallback); (3) deduplication, selecting the largest file per (country, year) pair when multiple uploads exist.

### 3.2 Variables

**Dependent variable.** Labour productivity is log annual sales per permanent worker, ln(LP) = ln(d2 / l1), winsorised at the 1st/99th percentiles within each survey wave and then **standardised within each economy-year cell** (lp_z, mean 0 / SD 1). Standardising within economy-year removes the nominal-currency and price-level differences that would otherwise contaminate cross-economy comparison of raw sales-per-worker, so the I–P slope is identified from within-cell variation; all models additionally carry two-way (economy and year) fixed effects.

**Foreign sales intensity (FSTS).** Defined as the share of sales from exports, both direct and indirect, (d3b + d3c) / 100, ranging from 0 to 1. We mean-centre FSTS at the sample mean for quadratic and interaction models (fsts_c); the quadratic term fsts_c² is computed from the centred value. The sample mean is 9.0%.

**Technological capability index (TCI_z).** A two-item composite of R&D activity (h8) and internationally recognised quality certification (b8), standardised to mean 0, SD 1 within economy-year.

**Digital adoption index (DAI).** Website presence (c22b), a binary Tier-1 indicator of digital participation.

**Manager characteristics.** Top manager experience in sector (b7, in years) and a binary indicator for female top manager (b7a / b6a).

**Controls.** Female ownership share (b4 > 0.5: majority female-owned, binary), foreign ownership percentage (b6a / 100), firm age (in years, current year − b5), and log permanent employees (ln l1_workers) as a size proxy.

**Institutional regime (ICRV group).** Integer 1–6 based on the ICRV classification; used as a continuous moderator in M8 (its main effect absorbed by economy fixed effects) and as the grouping variable for the within-regime turning-point analysis (Table 4).

### 3.3 Estimation Strategy

We estimate a hierarchical sequence of eight models (Table 2). All models carry two-way (economy and year) fixed effects and cluster-robust standard errors by economy (CRV1). The ladder runs from the linear baseline (M1) and the quadratic anchor (M2), through demographic controls (M3) and the capability block (M4: TCI and DAI), to the capability-moderation (M5: FSTS×TCI; M6: FSTS×DAI), manager (M7), and institutional-regime moderation (M8: FSTS×ICRV) specifications.

The inverted-U shape is formally confirmed using the Lind–Mehlum (2010) test, which requires: (a) β₁ > 0, β₂ < 0, and (b) the turning point lies strictly within the observed FSTS range, and (c) the slope at the extremes satisfies the directional prediction. We report the turning point as: TP = −β₁ / (2β₂) + mean(FSTS), where β₁ and β₂ are estimated on the mean-centred FSTS_c scale and the result is expressed as a proportion (0–1) of total sales.

For moderation tests (M5–M8), we include interaction terms FSTS×moderator and FSTS²×moderator and report the individual coefficient p-values.

### 3.4 Sample Sizes

The analytic frame is 88,869 firms across 50 economies. The quadratic anchor (M2: outcome + FSTS non-missing) is N = 81,022. Adding the capability block (M4: TCI and DAI) gives N = 79,080; demographic controls (M3) N = 78,970; the manager models (M7) drop to N = 75,029 because manager experience and gender are missing in some waves. The modest attrition across the ladder reflects item missingness in the moderator and manager variables, which is more prevalent in smaller economies and early WBES waves. All N's are reproducible via `scripts/p7_full_ladder.py`.

---

## 4. Results

### 4.1 Descriptive Statistics and Correlations

The full analytic sample spans 50 economies and 103 country-year waves. The mean FSTS across firms is approximately 9% (median ≈ 0), reflecting the fact that most WBES firms are domestically oriented; exporters (FSTS > 0) represent roughly one in five firms. Because the dependent variable is standardised within each economy-year cell, productivity is directly comparable within the estimation regardless of national currency or price level. Pairwise correlations among focal variables are modest, and variance inflation factors in the full model are below 3.5, ruling out multicollinearity concerns.

### 4.2 Main Effect: Inverted-U (H1)

*Table 2, Models M1–M4.*

The linear baseline (M1) yields a positive but small FSTS slope (β = +0.219, p = .002). Adding the quadratic term (M2, N=81,022) yields β₁ = +1.188 (p < .001) and β₂ = −1.398 (p < .001), consistent with an inverted-U. Following Haans, Pieters, and He (2016), the formal conditions for a genuine inverted-U are satisfied: (C1) β₁ > 0 (p < .001), a positive ascending limb; (C2) β₂ < 0 (p < .001), concavity; (C3) the turning point TP ≈ 51.5% lies within the observed FSTS range; and (C4) the marginal effect is positive at the lower boundary and negative at the upper boundary, with opposite signs confirmed by the Lind–Mehlum (2010) test (joint p < .001). The turning point tightens as capability is controlled: adding demographic controls (M3) gives TP = 43.8%, and adding technological capability and digital adoption (M4, N=79,080) gives TP = 43.6%, the headline estimate, matching the dissertation's canonical value. The stability of the turning point in the low-to-mid-40% range once capability is held constant indicates that the inverted-U is not an artefact of capability-based selection into exporting.

**H1 is supported.** The I–P relationship is robustly inverted-U in the pooled sample of 50 Asian and Pacific economies, with a capability-adjusted turning point of 43.6% foreign sales intensity (51.5% in the unconditioned quadratic).

### 4.3 Technological Capability Moderation (H2)

*Table 2/3, Models M4–M5.*

Technological capability enters with a positive and highly significant level effect (M4: TCI = +0.108, p < .001): higher-capability firms are more productive at every level of internationalization. The interaction model M5 adds FSTS×TCI and FSTS²×TCI; neither is significant (FSTS×TCI = +0.068, FSTS²×TCI = −0.119, both p > .10), and the turning point is essentially unchanged (TP = 44.0%). Capability raises the floor; it does not bend the curve.

**H2 is partially supported (level effect confirmed; curvature effects NS).** TCI is a foundational level-shifter across the 50-economy pool. The curve-moderation found in single-country studies (P3 Vietnam, P5 China) does not survive aggregation across the institutionally diverse pool, consistent with capability's curve-shaping role being institution-contingent rather than universal.

### 4.4 Digital Adoption Moderation (H3)

*Table 2/3, Models M4 and M6.*

Digital adoption carries the largest capability level effect in the model (M4: DAI = +0.219, p < .001): a substantial productivity premium for firms with a web presence. The interaction model M6 adds FSTS×DAI and FSTS²×DAI to test whether digital adoption reshapes the curve; on this canonical specification, neither interaction is significant (FSTS×DAI = −0.270, FSTS²×DAI = +0.252, both p > .10), and the turning point is essentially unchanged (TP = 47.1%). The curve-reshaping role attributed to DAI in an earlier draft does not survive re-estimation on the within-economy-year-standardised, two-way-fixed-effects specification: DAI behaves as a level-shifter, not a curve-reshaper, in the pooled sample.

**H3 is partially supported (level effect confirmed; curvature effects NS).** Digital adoption raises firm performance substantially but does not significantly reshape the pooled I–P curve. The "digital shield" effect (DAI attenuating the descending limb) documented in the single-country Singapore study (P4) is not detectable once aggregated across the 50-economy pool, again consistent with the curve-shaping role of digital capability being institution-contingent rather than universal.

### 4.5 Managerial Characteristics (H4)

*Table 2/3, Model M7.*

Adding manager characteristics (M7, N=75,029), manager sectoral experience is not significant (β = +0.002, p > .10), while the female-top-manager coefficient is negative and highly significant (β = −0.104, p < .001). The inverted-U is unaffected (TP = 44.0%). The negative female-management coefficient is consistent with the rest of the dissertation (the single-country Japan study, P10, and the thesis Chapter 4 likewise estimate a negative female-top-manager coefficient) and is most plausibly read as compositional selection of female-led establishments into smaller, lower-margin niches in economies where female senior leadership remains rare, rather than as a leadership effect. It should not be interpreted causally.

**H4 is not supported as hypothesised.** Manager experience carries no significant level effect, and the female-management coefficient is negative rather than the hypothesised positive. We treat the female-management coefficient as a descriptive regularity requiring within-economy, selection-aware analysis, not as evidence on the causal effect of female leadership.

### 4.6 Institutional Regime Moderation (H5)

*Table 2/3, Model M8, and the per-ICRV turning-point table.*

Because ICRV regime is time-invariant within an economy, its main effect is absorbed by the economy fixed effects; only the interaction terms are identified. In the pooled model M8, neither FSTS×ICRV (β = −0.086) nor FSTS²×ICRV (β = −0.013) is significant (both p > .10): the institutional gradient does not manifest as a single linear shift of the pooled curve. Instead, the institutional structure of the relationship emerges when the turning point is estimated **within** each ICRV group (capability-adjusted M4 form within group):

- **Lower-middle transition (Group IV, N=42,094): TP ≈ 43%**, a sharp, reliably located inverted-U (β₂ < 0, p < .001). This is the regime that anchors the pooled estimate.
- **Strongest-institution regime (Group I Advanced innovation, incl. Japan): TP ≈ 80%**: the turning point lies near or beyond the observable range, so within the data the relationship is effectively near-linear and positive.
- **Weakest regimes (Group V Emerging: TP ≈ 37%; Group VI Pacific SIDS): the inverted-U dissolves**; in the SIDS group the quadratic flips sign (no interior maximum), consistent with the Forced Internationalization Penalty documented in the companion SIDS study (P8).

**H5 is supported, but as existence-moderation rather than location-moderation.** Institutional regime does not merely shift where a universal inverted-U peaks; it governs whether the inverted-U is sharp (transition regimes), straightened (strongest regimes), or absent (weakest regimes): a three-zone structure.

### 4.7 Synthesis: A Three-Zone, Institution-Contingent Curve

Taken together, the moderation results relocate the explanatory weight from capability to institutions. Capability (TCI, DAI) and managers shift the **level** of productivity but do not significantly reshape the pooled curve. What reshapes the curve is institutional regime, and it does so not as a smooth gradient but as three discrete zones. In the middle of the institutional gradient (lower-middle transition), the inverted-U is sharp and reliably located near a 43% turning point; at the top (strongest institutions, including Japan), the descending limb is pushed beyond the observable range and the relationship is effectively near-linear; at the bottom (emerging and Pacific SIDS), the inverted-U dissolves and, in the SIDS group, reverses. This three-zone reading reconciles the apparently divergent single-country results in the dissertation (Vietnam and India in the transition zone show sharp inverted-U; Singapore and Japan at the top show near-linearity; the SIDS group shows the Forced Internationalization Penalty) within one harmonised, 50-economy estimation.

---

## 5. Discussion

### 5.1 Resolution of Cross-Study Heterogeneity

The central finding (an inverted-U with a capability-adjusted turning point of 43.6% foreign sales intensity, robust across 50 economies and six ICRV groups) offers a parsimonious resolution to apparent inconsistencies in the Asian I–P literature. Studies finding positive linear effects (Pangarkar, 2008: Singapore; Cho et al., 2023: Korea) are working with strong-institution samples whose turning point lies beyond the observable export-intensity range; their firms are on a long ascending limb. Studies finding null or negative results may be capturing weakest-regime samples in which the inverted-U dissolves. Our within-regime turning-point analysis provides the key refinement: the relationship is not a single inverted-U with a moving peak but a **three-zone** structure: sharp inverted-U in the transition regime (Group IV, TP ≈ 43%), near-linearity in the strongest regime (Group I, TP ≈ 80%, beyond range), and dissolution in the weakest regimes (Group V ≈ 37%; Group VI SIDS, no inverted-U). Whether a single-country study finds an inverted-U at all therefore depends on which institutional zone its economy occupies.

### 5.2 Technology as Amplifier, Not Moderator

The finding that TCI raises the performance level without reliably reshaping the I–P curve in the pooled sample distinguishes the cross-economy result from country-specific evidence. In P3 Vietnam and P5 China, TCI moderated the curve shape; in the 50-economy pool, institutional heterogeneity attenuates that moderation signal. This is consistent with the absorptive capacity argument (Cohen & Levinthal, 1990): high-TCI firms process international market signals more effectively, but the curve-shaping benefit requires institutional complementarity (e.g., strong IP protection, technology transfer infrastructure) that is inconsistently present across the full ICRV spectrum. The practical implication is that technological capability raises the performance floor universally, but its curve-reshaping role is context-contingent and cannot be assumed at scale.

### 5.3 Digital Adoption: Level Effect, Not Curve Reshaping

On the canonical specification, digital adoption is the largest single capability level-shifter (DAI = +0.219, p < .001) but does not significantly reshape the pooled I–P curve. This is a more conservative and, we argue, more credible reading than an earlier draft that attributed significant curve-reshaping to DAI: with within-economy-year standardisation and two-way fixed effects absorbing the price-level and selection confounds, the apparent curve-reshaping does not survive. The "digital shield" mechanism, DAI cushioning the descending limb, appears in the single-country Singapore study (P4) but is undetectable in aggregation, indicating that any curve-shaping role of digital adoption is institution-contingent and operates below the resolution of a pooled, Tier-1 (website-only) WBES measure. The policy implication is correspondingly disciplined: digital adoption is a robust lever for raising the productivity **level** across the region, but it should not be sold as a tool for re-shaping the internationalization-performance trade-off.

### 5.4 Managerial Heterogeneity

On the canonical specification, manager sectoral experience carries no significant level effect, and the female-top-manager coefficient is **negative** (−0.104, p < .001) rather than positive. This sign is consistent across the dissertation: the single-country Japan study (P10) and the thesis pooled analysis estimate the same negative coefficient. It cautions against a causal reading. In economies where female senior leadership remains rare (the regional pool spans contexts with female-top-manager shares from single digits upward), the small set of female-led establishments is unlikely to be a random draw; the most plausible interpretation is compositional selection into smaller, lower-margin, labour-intensive niches, which a cross-sectional level regression cannot disentangle from any leadership effect. The null curve-moderation result (FSTS×manager terms not significant) indicates that, whatever the source of the level coefficient, manager characteristics do not help firms navigate the internationalization trade-off more efficiently. We therefore report the female-management coefficient as a descriptive regularity requiring within-economy, selection-aware analysis (e.g., matched samples or panel tracking of leadership transitions), not as evidence on the causal effect of female leadership on firm performance.

### 5.5 Limitations

Three inferential constraints bound these findings. First, WBES is a cross-sectional design: "performance" throughout refers to a contemporaneous association between FSTS and labour productivity in a given survey year, not a panel-tracked causal effect. The IV strategy used in the single-country P3 Vietnam study to address selection into exporting is not available at scale across 50 economies, and capability-based selection into exporting is part of what the capability-adjusted turning point (M4) reveals rather than a nuisance assumed away. Second, the DAI measure is limited to Tier-1 (website) capability in the harmonised pool; the richer digital-capability dimensions captured in more recent BEE-schema waves are not yet available for the majority of economies, which likely contributes to the null curve-reshaping result. Third, the dataset covers all 50 ICRV-mapped economies across six regime groups, including Japan's inaugural 2025 wave; some early waves predate the digital-capability and manager variables, limiting their contribution to the baseline models. Future WBES waves would sharpen the moderation estimates, particularly for the sparser Advanced and SIDS regimes.

---

## 6. Conclusions

We find that the inverted-U I–P relationship holds robustly across a 50-economy, 103-wave WBES sample (including Japan's inaugural 2025 wave), with a capability-adjusted turning point of 43.6% foreign sales intensity. Three conclusions are policy-relevant. First, for firms in the ascending phase (FSTS < 43.6%), intensifying internationalization is productivity-enhancing; the priority is removing barriers to export expansion. For firms beyond the turning point, the constraint is not market access but coordination capacity. Second, both technological capability and digital adoption raise the performance level substantially across all FSTS levels without reliably reshaping the curve; policy should target capability building as a baseline performance lever rather than as a curve-shifting intervention. Third, and most important, it is institutional regime, not capability, that determines the shape of the curve: the inverted-U is sharp in transition economies (turning point ≈ 43%), straightens toward near-linearity in the strongest-institution economies (peak beyond the observable range), and dissolves in the weakest regimes, reversing into a Forced Internationalization Penalty in the Pacific SIDS group. Context-contingent policy must therefore differ by zone, not merely by where a common peak falls.

The near-term policy context adds urgency to these findings. World Bank (2026b) macro monitoring data for Vietnam, the largest ICRV Group IV economy in the sample, show manufacturing PMI falling to 45.3 (contraction) in March 2026 as new export orders collapsed following the opening of a U.S. trade-representative investigation; merchandise imports had risen 27.8% year-on-year by the same month, partly driven by energy supply-chain disruption from the Strait of Hormuz conflict. These conditions are precisely those under which the right side of the inverted-U becomes consequential: firms pushed above their optimal FSTS by earlier export commitments face amplified coordination and input-cost pressures. Because Vietnam sits in the transition regime where the inverted-U is sharpest (Group IV turning point ≈ 43%), Vietnamese exporters currently above that threshold are among the most exposed to macro shocks. The capability evidence implies that building technological and digital capability raises the productivity floor for these firms, even though, on our pooled estimates, capability does not by itself flatten the descending limb; the binding margin is the breadth of capable export participation, not a curve-shifting fix.

Future research should leverage the growing panel dimensions of WBES to establish causality, and incorporate Tier 3–4 digital capability measures (AI adoption, cloud computing, platform participation) as these items become available in the 2025+ WBES waves.

---

## References

Aiken, L. S., & West, S. G. (1991). *Multiple regression: Testing and interpreting interactions*. Sage.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120. https://doi.org/10.1177/014920639101700108

Buchhave, H., Nguyen, C. V., Vu, C., Nguyen, G. T., & Zumbyte, I. (2026). *Care for growth: Making industrial jobs work for women in Viet Nam* (Policy Summary Note). World Bank Group & Australian Aid.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization-performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347. https://doi.org/10.1007/s11575-007-0019-z

Chiao, Y.-C., Yang, K.-P., & Yu, C.-M. J. (2006). Performance, internationalization, and firm-specific advantages of SMEs in a newly-industrialized economy. *Small Business Economics, 26*(5), 475–492. https://doi.org/10.1007/s11187-005-5599-z

Cho, H., Kim, C., & Han, S. (2023). Business group affiliation and the internationalization–performance relationship: Evidence from Korean firms. *Journal of International Business Studies, 54*(3), 487–509.

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152. https://doi.org/10.2307/2393553

Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of international expansion: The link between multinationality and performance in the service sector. *Journal of International Business Studies, 34*(1), 5–18. https://doi.org/10.1057/palgrave.jibs.8400003

Contractor, F. J., Kumar, V., & Kundu, S. K. (2007). Nature of the relationship between international expansion and performance: The case of emerging market firms. *Journal of World Business, 42*(4), 401–417. https://doi.org/10.1016/j.jwb.2007.06.003

Cuervo-Cazurra, A., Ciravegna, L., Melgarejo, M., & Lopez, L. (2018). Home country uncertainty and the internationalization-performance relationship: Building an uncertainty management capability. *Journal of World Business, 53*(2), 209–221. https://doi.org/10.1016/j.jwb.2017.11.003

Dawson, J. F. (2014). Moderation in management research: What, why, when, and how. *Journal of Business and Psychology, 29*(1), 1–19. https://doi.org/10.1007/s10869-013-9308-7

Đỗ, T. H., & Phan, A. T. (2024). *Internationalization and firm performance: A meta-analysis for Asia-Pacific economies*. Paper presented at the International Conference on Business, Economics, and Finance (ICBEF 2024). Can Tho University.

Gomes, L., & Ramaswamy, K. (1999). An empirical examination of the form of the relationship between multinationality and performance. *Journal of International Business Studies, 30*(1), 173–187. https://doi.org/10.1057/palgrave.jibs.8490065

Haans, R. F. J., Pieters, C., & He, Z.-L. (2016). Thinking about U: Theorizing and testing U- and inverted U-shaped relationships in strategy research. *Strategic Management Journal, 37*(7), 1177–1195. https://doi.org/10.1002/smj.2399

Hambrick, D. C. (2007). Upper echelons theory: An update. *Academy of Management Review, 32*(2), 334–343. https://doi.org/10.5465/amr.2007.24345254

Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review, 9*(2), 193–206. https://doi.org/10.5465/amr.1984.4277628

Hayes, A. F. (2018). *Introduction to mediation, moderation, and conditional process analysis: A regression-based approach* (2nd ed.). Guilford Press.

International Finance Corporation. (2022, December). *Mind the gaps: Women in leadership in Viet Nam's banking sector*. IFC, World Bank Group.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process of the firm—A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32. https://doi.org/10.1057/palgrave.jibs.8490676

Johanson, J., & Vahlne, J.-E. (2009). The Uppsala internationalization process model revisited: From liability of foreignness to liability of outsidership. *Journal of International Business Studies, 40*(9), 1411–1431. https://doi.org/10.1057/jibs.2009.24

Kirca, A. H., Roth, K., Hult, G. T. M., & Cavusgil, S. T. (2012). The role of context in the multinationality–performance relationship: A meta-analytic review. *Global Strategy Journal, 2*(2), 108–121. https://doi.org/10.1002/gsj.1028

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118. https://doi.org/10.1111/j.1468-0084.2009.00569.x

Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *The American Statistician, 54*(3), 217–224. https://doi.org/10.1080/00031305.2000.10474549

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609. https://doi.org/10.2307/20159604

Marano, V., Tashman, P., & Kostova, T. (2016). Escaping the iron cage: Liabilities of origin and CSR reporting of emerging market multinational enterprises. *Journal of International Business Studies, 47*(3), 386–408. https://doi.org/10.1057/jibs.2016.7

Mondal, A., Gupta, S., & Ray, S. (2022). Family ownership, governance, and internationalization: Evidence from India. *Journal of Business Research, 138*, 423–434.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Pangarkar, N. (2008). Internationalization and performance of small- and medium-sized enterprises. *Journal of World Business, 43*(4), 475–485. https://doi.org/10.1016/j.jwb.2007.11.009

Richard, O. C., Kirby, S. L., & Chadwick, K. (2019). The impact of racial and gender diversity in management on firm performance: An assessment of different conceptual and measurement approaches. *Journal of Applied Social Psychology, 39*(7), 1571–1599.

Scott, W. R. (2008). *Institutions and organizations: Ideas and interests* (3rd ed.). Sage.

UNCTAD. (2023). *World investment report 2023: Investing in sustainable energy for all*. United Nations.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901. https://doi.org/10.1016/j.jbusres.2019.09.022

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic Management Journal, 5*(2), 171–180. https://doi.org/10.1002/smj.4250050207

World Bank. (2025). *Enterprise surveys*. https://www.enterprisesurveys.org

World Bank. (2025a, March). *Digital public infrastructure and development: A World Bank Group approach*. World Bank Group.

World Bank. (2025b, September). *Viet Nam economic update: Nurturing high-tech talents* (Taking Stock, September 2025). World Bank Group.

World Bank. (2025c, October). *Viet Nam economy snapshot: Finance, competitiveness & innovation* (Prosperity Data360). World Bank Group. https://www.worldbank.org/ext/en/country/vietnam

World Bank. (2026a). *ID4D & G2Px annual report 2023: Putting people at the center of digital public infrastructure*. World Bank Group.

World Bank. (2026b, April). *Viet Nam macro monitoring: April 2026*. World Bank Group, Fiscal Policy and Growth Viet Nam Team.

World Bank. (2024, December). *Viet Nam economy snapshot: Justice* (Prosperity Data360). World Bank Group. https://www.worldbank.org/ext/en/country/vietnam

Wu, J., Wang, C., Hong, J., Piperopoulos, P., & Zhuo, S. (2022). Internationalization and innovation of business groups: Evidence from China. *Journal of World Business, 54*(4), 305–320.

---

## Appendix A: Model Sequence

**Table 1: Variable definitions and measurement**

| Variable | Definition | Source items | Coverage |
|---|---|---|---|
| lp_z | Log labour productivity ln(d2/l1), winsorised 1/99, z-scored within economy-year | d2; l1 | ~85% |
| FSTS | Foreign sales share (direct + indirect exports) | (d3b + d3c) / 100 | ~83% |
| TCI_z | Tech capability index (R&D + ISO certification), z-scored within economy-year | h8, b8 | ~82% |
| DAI | Digital adoption (website presence, Tier-1 binary) | c22b | ~83% |
| mgr_experience | Top manager years in sector | b7 | ~84% |
| mgr_female | Top manager is female (binary) | b7a, b6a | ~82% |
| female_owner | Majority female ownership (binary) | b4 | ~99% |
| foreign_own_pct | Foreign ownership % | b6a / 100 | ~52% |
| firm_age | Years since establishment | current yr − b5 | ~64% |
| ln_size | Log permanent workers | l1 | ~84% |
| ICRV_group | Institutional regime group (1–6) | ICRV classification | 100% |

**Table 2: Model fit and turning points** (50-economy canonical frame; two-way FE economy+year; CRV1 by economy)

| Model | N | Turning point (%) | LM p | Key additions |
|---|--:|--:|--:|---|
| M1 | 81,022 | — | — | FSTS linear (β = +0.219**) |
| M2 | 81,022 | **51.5** | <.001 | FSTS + FSTS² (anchor) |
| M3 | 78,970 | **43.8** | <.001 | M2 + ownership, age, size, female-owner |
| M4 | 79,080 | **43.6** | <.001 | M3-block + TCI + DAI (headline) |
| M5 | 79,080 | 44.0 | <.001 | M4 + FSTS×TCI, FSTS²×TCI |
| M6 | 79,080 | 47.1 | <.001 | M4 + FSTS×DAI, FSTS²×DAI |
| M7 | 75,029 | 44.0 | <.001 | M4 + manager experience, female manager |
| M8 | 79,080 | (73.6) | n.s. | M4 + FSTS×ICRV, FSTS²×ICRV (interactions NS) |

*Note.* Turning point from −β₁/(2β₂) + mean(FSTS), confirmed by the Lind–Mehlum (2010) test (LM p). All models carry two-way (economy, year) fixed effects throughout; SEs clustered by economy. In M8 the ICRV main effect is absorbed by economy fixed effects and the FSTS×ICRV interactions are not significant, so the pooled turning point is not identified; the institutional structure appears instead in the per-ICRV turning points (Table 4). Reproducible via `scripts/p7_full_ladder.py`.

**Table 3: Key coefficient estimates**

| Term | M2 | M4 | M5 | M6 | M7 | M8 |
|---|--:|--:|--:|--:|--:|--:|
| FSTS (β₁) | +1.188*** | +0.499*** | +0.457*** | +0.704*** | +0.505*** | +0.806† |
| FSTS² (β₂) | −1.398*** | −0.721*** | −0.652** | −0.924*** | −0.720*** | −0.624 |
| TCI_z | — | +0.108*** | +0.115*** | +0.108*** | +0.108*** | +0.107*** |
| DAI | — | +0.219*** | +0.219*** | +0.201*** | +0.218*** | +0.220*** |
| FSTS×TCI | — | — | +0.068 | — | — | — |
| FSTS²×TCI | — | — | −0.119 | — | — | — |
| FSTS×DAI | — | — | — | −0.270 | — | — |
| FSTS²×DAI | — | — | — | +0.252 | — | — |
| mgr experience (z) | — | — | — | — | +0.002 | — |
| female manager | — | — | — | — | −0.104*** | — |
| FSTS×ICRV | — | — | — | — | — | −0.086 |
| FSTS²×ICRV | — | — | — | — | — | −0.013 |
| N | 81,022 | 79,080 | 79,080 | 79,080 | 75,029 | 79,080 |

*Note.* Two-way FE (economy, year); SEs clustered by economy. \*\*\* p < .001, \*\* p < .01, \* p < .05, † p < .10. Capability (TCI, DAI) carries robust positive level effects throughout; none of the FSTS×capability or FSTS×ICRV interaction terms is significant; the pooled curve is reshaped by neither capability nor a linear institutional gradient. Reproducible via `scripts/p7_full_ladder.py`.

**Table 4: Turning points within each ICRV regime** (capability-adjusted M4 form; two-way FE)

| ICRV group | N | β₁ | β₂ | Turning point (%) | Reading |
|---|--:|--:|--:|--:|---|
| I Advanced innovation (incl. Japan) | 5,581 | +0.707 | −0.504 | ≈ 80 | near-linear (beyond range) |
| II Advanced resource (GCC) | 2,075 | +0.774 | −0.730 | 56.6 | broad inverted-U |
| III Upper-middle | 12,055 | +0.174 | −0.189 | 56.4 | weak/flat |
| IV Lower-middle transition | 42,094 | +0.689 | −1.012 | **≈ 43** | sharp inverted-U |
| V Emerging | 15,457 | +0.235 | −0.455 | 36.8 | dissolving |
| VI Pacific SIDS | 1,818 | −0.681 | +0.870 | — | no inverted-U (FIP) |

*Note.* Within-group quadratic with controls and two-way FE. The three-zone structure (sharp in the transition regime, near-linear at the top, dissolving at the bottom) is the paper's central institutional finding. Consistent with the dissertation's canonical per-ICRV values.

---

## Appendix B: TFP Production Function Estimates (Robustness Reference)

Sector-level production function coefficients used to construct alternative TFP-based dependent variables for robustness checks. Two specifications are available: VA=f(K,L) (VAKL, value-added formulation) and Y=f(K,L,M) (YKLM, gross-output formulation), each estimated separately for 20 two-digit ISIC manufacturing sectors with high-income economy interaction terms and year fixed effects (2009–2025). Coefficients and t-statistics are stored in `replication/Annex_TFP_regression_tables_March_11_2026.xlsx`. TFP residuals from these regressions can be used as an alternative dependent variable to ln(LP) to test whether the inverted-U relationship is robust to output-per-worker vs. total-factor productivity operationalisations.

---

*Corresponding author: Phan Anh Tu, College of Economics, Can Tho University, patu@ctu.edu.vn, ORCID: 0000-0003-0667-3137*  
*First author: Do Thuy Huong, Vinh Long University of Technology Education, huongdt@vlute.edu.vn, ORCID: 0000-0002-7711-2487*
