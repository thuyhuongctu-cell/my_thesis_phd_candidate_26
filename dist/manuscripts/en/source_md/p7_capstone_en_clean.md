# Where Internationalisation Pays: Institutional Regime and Digital Capability as Joint Determinants of the Performance Optimum across 49 Asian and Pacific Economies

**Version:** Working manuscript (May 2026)  
**Target journal:** Journal of International Business Studies (JIBS)  
**Status:** Empirical results complete; under revision for submission

---

## Abstract

The central unresolved question in research on the internationalisation–performance (I–P) relationship is not whether the relationship is non-linear, but what determines *where* its performance-maximising optimum falls. We develop and test an integrated multi-level account in which the inverted-U is universal in form but its turning point is *jointly relocated* by the institutional regime in which a firm operates and by the firm's digital capability — and in which digital capability operates as a partial *substitute* for institutional strength rather than as a uniform enhancer. Using harmonised microdata from 91,982 firms across 49 economies and 102 country-year waves of the World Bank Enterprise Survey (2003–2025), spanning all six groups of the Institutional Context Regime Variation (ICRV) framework, we estimate a hierarchical set of OLS models with HC1 robust standard errors. We confirm a robustly inverted-U I–P relationship with a turning point at approximately 36% of sales from exports (Lind–Mehlum test p < .001; confirmed in M11 at TP=34.6%, p=.002). Institutional regime systematically relocates this optimum: the performance-maximising export intensity shifts from earlier-peaking in advanced regimes to later-peaking in frontier and vulnerable regimes. Digital adoption (DAI) both raises the performance level and reshapes the curve — compressing ascending-limb returns at low FSTS and attenuating performance decline at high FSTS (FSTS×DAI p < .01; FSTS²×DAI p < .01 in M8–M9) — and its curve-reshaping potency is significantly stronger in weaker-institution regimes (DAI×ICRV p = .012), consistent with digital-for-institutional substitution. Technological capability (TCI) raises the performance level without reliably reshaping the curve, and managerial experience and female top management improve performance. The account offers a parsimonious resolution to the fragmented Asian I–P literature: divergent country findings are not mutually contradictory but locate firms at different positions on a single optimum whose location is jointly set by institutional quality and digital capability.

**Keywords:** internationalisation–performance; inverted-U; institutional regime; digital capability; Asia-Pacific; World Bank Enterprise Surveys

---

## 1. Introduction

A central question in international business research concerns whether and how export internationalisation translates into firm performance (Lu & Beamish, 2004; Johanson & Vahlne, 2009). Meta-analyses document a mean correlation of approximately r = .07 across several thousand studies (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016), yet the variance across studies vastly exceeds what sampling error can explain. In Asia — a region that accounts for over half of global manufacturing exports (UNCTAD, 2023) — the evidence is especially fragmented: prior studies report positive relationships (Pangarkar, 2008; Korea), inverted-U curves (Chiao et al., 2006; Taiwan), or null and negative effects (Mondal et al., 2022; India). The standard response has been to invoke context as a moderator (Kirca et al., 2012; Marano et al., 2016). Yet treating context as a moderator leaves the deeper question unanswered: if the I–P relationship is non-linear, what determines *where* its performance-maximising turning point falls, and why should that location differ systematically across firms and economies? Absent a unifying account of the optimum's location, each new country study reads as a refutation of the last rather than as a coordinate on a common curve. Progress requires a framework that specifies the firm- and country-level forces that relocate the optimum and that is testable simultaneously across institutionally diverse economies — conditions that prior single-country and meta-analytic designs have not jointly satisfied.

This paper addresses that gap. We pool 91,982 firm-observations from 49 Asian and Pacific economies spanning 2003–2025, harmonised from the World Bank Enterprise Survey (WBES). Our sample spans all six ICRV regime groups — from advanced innovation-driven economies (Singapore, Korea, Taiwan, HongKong, Israel, Cyprus) to Pacific Small Island Developing States (Vanuatu, Solomon Islands, Fiji, Tonga, Samoa, Kiribati, Papua New Guinea, Timor-Leste) and Gulf advanced-resource economies (Bahrain, Kuwait, Qatar, Brunei, Saudi Arabia, Oman) — classified through the Institutional Context Regime Variation (ICRV) framework that anchors the broader dissertation programme of which this study is part.

Our contributions are theoretical, not merely empirical. First, we advance a *relocated-optimum* account of the I–P relationship: the inverted-U is universal in form, but its turning point is endogenous to the institutional regime, shifting from earlier-peaking in advanced regimes toward later-peaking in frontier and vulnerable ones (confirmed across specifications at N = 84,910–29,840; M11: TP = 34.6%, Lind–Mehlum p = .002). This reframes the long-running "is it an inverted-U?" debate as a question about the *determinants of the optimum's location*, and reconciles otherwise conflicting country evidence within a single curve. Second, we theorise and test *digital-for-institutional substitution*: the curve-reshaping potency of digital adoption is significantly greater where formal institutions are weaker (DAI×ICRV, p = .012), positioning foundational digital capability as a partial substitute for institutional infrastructure in converting exports into performance — a multi-economy extension of the institutional-voids logic (Khanna & Palepu, 1997) into the digital domain. Third, we formalise the Institutional Context Regime Variation (ICRV) framework as a firm-relevant contingency construct that orders economies jointly by institutional capability and exposure to resource vulnerability, and show that it predicts both the slope and the curvature of the I–P function — distinguishing the curve-*relocating* role of institutions (H5) from the level-*shifting* role of firm capabilities such as technological capability (TCI). Taken together, these contributions move the multi-country I–P literature from cataloguing heterogeneous effects toward a parsimonious, jointly-determined account of when and where internationalisation pays.

The remainder of the paper is organised as follows. Section 2 develops the theoretical framework and formal hypotheses. Section 3 describes data and methods. Section 4 presents results. Section 5 discusses implications and limitations. Section 6 concludes.

---

## 2. Theoretical Framework and Hypotheses

### 2.1 Theoretical Foundations

We draw on four theoretical traditions. The Uppsala model (Johanson & Vahlne, 1977, 2009) describes internationalisation as a sequential process in which firms accumulate experiential knowledge, progressively reducing psychic distance and coordination costs. The Resource-Based View (Barney, 1991; Wernerfelt, 1984) positions firm-level capabilities — technological, digital, and managerial — as the mediating mechanism linking export exposure to performance outcomes. Institutional Theory (North, 1990; Scott, 2008) directs attention to how country-level formal and informal institutions shape the cost structure of cross-border transactions. Upper Echelons Theory (Hambrick & Mason, 1984; Hambrick, 2007) emphasises that top management team attributes moderate how firms respond to strategic opportunities and constraints.

These traditions are typically invoked piecemeal. We integrate them through a single contingency construct — the **Institutional Context Regime Variation (ICRV)** framework — that specifies *where* on the I–P curve a firm's environment places it. ICRV orders economies along two theoretically distinct dimensions that prior typologies treat separately: *institutional capability* (the formal-institutional quality emphasised by North (1990) and elaborated in the varieties-of-capitalism tradition; Hall & Soskice, 2001) and *resource vulnerability* (exposure to external shocks, narrow factor endowments, and the institutional voids that firms must internalise; Khanna & Palepu, 1997). The resulting six regime groups range from advanced innovation-driven economies, through resource-driven, upper-middle, emerging, and frontier economies, to highly vulnerable small-island states. Our central theoretical claim follows from locating the firm within this regime space: the inverted-U *form* of the I–P relationship is universal (H1), but its performance-maximising turning point is *jointly relocated* by the institutional regime (H5) and by the firm's digital capability (H3), with digital capability acting as a partial substitute for institutional strength where the latter is weak (H6). Firm capabilities enter on a second axis: technological capability is hypothesised to *amplify* the curve (H2) and managerial characteristics to lift the performance *level* without reshaping it (H4); whether each in fact relocates the optimum or merely shifts the level is an empirical question the design is built to adjudicate. This contrast between optimum-*relocating* forces (institutional regime and digital capability) and firm-*capability* forces (technological and managerial) is the analytical spine of the paper.

### 2.2 The Non-Linear I–P Relationship (H1)

Contractor et al. (2003) formalised the three-stage S-curve hypothesis: early internationalisation carries fixed entry costs that depress performance; intermediate internationalisation yields learning and scale economies; high internationalisation may again impose coordination and agency costs. Empirically, however, the data more consistently support the inverted-U — a special case in which the third stage does not emerge at the export intensities typically observed in developing-economy WBES data (Gomes & Ramaswamy, 1999; Lu & Beamish, 2004).

In the Asian context, three country-specific studies in our broader dissertation programme provide prior evidence. For Vietnam (P3), the inverted-U is confirmed with a turning point at 39–46% using a WBES-based instrumental variable design. For China (P5), an inverted-U turning point of 47–49% is replicated across specifications with Paternoster cross-cohort tests (p = .545). For Singapore (P4), the relationship is predominantly positive with a very late turning point (~82%), consistent with near-monotonic returns in a high-institutional, digitally saturated economy. Pooled across a much larger and institutionally heterogeneous sample, we expect the inverted-U to emerge at an intermediate turning point.

> **H1:** The relationship between export intensity (FSTS) and firm labour productivity (ln LP) is an inverted-U, with a statistically confirmed turning point at intermediate export intensities, in a pooled sample of Asian and Pacific firms.

### 2.3 Technological Capability as a Curve Amplifier (H2)

Technological capability — operationalised as a composite of quality certification, foreign-technology adoption, process innovation, and R&D — raises absorptive capacity (Cohen & Levinthal, 1990), enabling firms to extract greater performance value per unit of export exposure. Critically, we expect TCI to operate as a *curve amplifier*: at low export intensities, high-TCI firms gain more per unit of internationalisation (steeper ascending limb); at high intensities, they experience sharper diminishing returns as coordination demands exceed even their superior capabilities (steeper descending limb). The net effect is a shift and steepening of the inverted-U, not just a parallel upward shift.

This prediction is consistent with P3 Vietnam (β(TCI) = +0.179, IV-identified) and P5 China (β(TCI) increasing from +0.28 to +0.43 across cohorts), both showing TCI as a positive level shifter. P4 Singapore shows negligible TCI moderation of the curve, likely because near-universal adoption in a high-ICRV economy leaves insufficient variance for moderation.

> **H2:** TCI amplifies the I–P curve, raising the average performance level and steepening both the ascending and descending limbs of the inverted-U.

### 2.4 Digital Adoption as a Level Enhancer (H3)

Digital adoption — measured through website presence and electronic-payment share — has been associated with reduced communication and transaction costs (Verhoef et al., 2021). In the CDCM (Context-Contingent Digital Capability Model) developed in the dissertation, DAI's effect depends on the interaction of regime quality, FSTS level, and digital market saturation (Đỗ & Phan, 2024). Specifically, in institutionally advanced economies where digital infrastructure is mature, DAI provides universal performance lifts (as in P4 Singapore: β(DAI) positive and significant). In emerging-economy contexts with substantial selection into digital adoption (P3 Vietnam: IV-estimated β(DAI) ≈ 0, consistent with selection bias in OLS), DAI's curve-shaping role is attenuated. Across the pooled multi-economy sample, we expect DAI to raise performance levels broadly across the sample (level effect). In a fully specified model that also accounts for managerial quality — which correlates with digital adoption — the residual DAI variation may reveal a capability-complementarity curve effect: digitally equipped firms at low FSTS face sunk adoption costs that compress near-term productivity, while digital infrastructure supports coordination efficiency at high FSTS where cross-border management demands are greatest.

> **H3:** DAI has a positive main effect on labour productivity and, when managerial characteristics are controlled, reshapes the I–P curve by compressing the ascending limb at low export intensities and attenuating performance decline at high export intensities.

### 2.5 Managerial Characteristics (H4)

Upper Echelons Theory predicts that top manager experience and gender composition affect strategic cognition and decision-making (Hambrick & Mason, 1984). Manager experience reduces coordination errors in cross-border operations; female top management is associated with stakeholder orientation, relationship capital, and risk management — all relevant in institutionally heterogeneous export markets (Richard et al., 2019). We expect both to raise the performance level for any given FSTS. However, given the breadth of the multi-country sample, firm-level managerial differences are unlikely to systematically reshape the aggregate FSTS–performance curve, whose shape is primarily determined by economy-wide institutional and market-maturity factors.

> **H4:** Top manager experience and female top manager status have positive main effects on firm performance, but do not significantly moderate the FSTS–performance curve shape.

### 2.6 Institutional Regime as a Turning-Point Shifter (H5)

North (1990) established that formal institutions reduce transaction costs; stronger institutions lower the cost of cross-border coordination and thus shift the performance-maximising export intensity (the inverted-U turning point). In higher-quality institutional environments, firms need a lower export share to recoup internationalisation costs, so the turning point occurs earlier. Equivalently, holding FSTS constant, firms in stronger institutional regimes earn higher returns per unit of internationalisation.

We operationalise institutional regime through the ICRV classification system developed in the dissertation: six groups ranging from Group I (Advanced innovation-driven: Singapore, Korea, Taiwan, Israel, Cyprus) to Group VI (SIDS and small open economies: Vanuatu, Solomon Islands, Timor-Leste). Higher ICRV group numbers denote weaker institutions. We expect positive FSTS×ICRV and negative FSTS²×ICRV interactions in Group III–VI compared to Group I (stronger institutions = higher Group I coefficient), which is observationally equivalent to the turning point occurring later in lower-quality institutional environments.

> **H5:** The ICRV institutional regime positively moderates the I–P relationship: firms in higher-quality institutional environments (lower ICRV group number) achieve the performance-maximising export intensity at lower FSTS levels.

### 2.7 Regime-Contingent Digital Effects (H6)

The Context-Contingent Digital Capability Model (CDCM) developed in this dissertation programme predicts that the I–P curve-reshaping role of digital adoption is not uniform across institutional environments. In institutionally advanced economies (ICRV Group I–II), digital infrastructure is near-universal and close to the competitive baseline — the marginal performance differentiation from website and e-payment adoption is accordingly lower. In institutionally weaker economies (ICRV Group IV–VI), digital adoption remains differentiating: digital market access tools lower the liability-of-foreignness cost and provide cross-border coordination support that institutional voids cannot substitute. The DAI×ICRV interaction therefore tests whether digital capabilities' curve-reshaping potency (established in H3) varies systematically across the institutional spectrum — specifically, whether compressing the ascending limb and buffering performance decline at high FSTS are more pronounced in weaker-institution economies.

This prediction is consistent with the digital-complementarity strand of institutional theory (North, 1990; Stallkamp & Schotter, 2021): where formal institutions provide reliable contract enforcement, IP protection, and market information, digital infrastructure adds incrementally; where institutional voids prevail, digital tools provide a non-trivial substitute for missing formal mechanisms. H6 therefore does not predict stronger *level* effects in weak-institution contexts (which could reflect many confounds), but specifically predicts a stronger *curve-shaping* interaction between digital adoption and export intensity — a conditional complementarity claim.

> **H6:** The ICRV institutional regime moderates the digital-adoption curve-reshaping effect: digital adoption's compressive effect on the I–P ascending limb and its buffering effect at high FSTS (H3) are stronger in weaker institutional environments (higher ICRV group number), where digital infrastructure provides greater competitive differentiation in cross-border market access.

---

## 3. Data and Methods

### 3.1 Data Source

Data derive from the World Bank Enterprise Surveys (WBES), a stratified random-sample survey of formal private-sector enterprises conducted periodically across over 130 countries. We use microdata from 49 Asian and Pacific economies across 102 country-year waves spanning 2003–2025. This coverage encompasses six UN M.49 Asian sub-regions: East Asia (China, HongKong, Korea, Mongolia, Taiwan), Southeast Asia (Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste, Vietnam), South Asia (Afghanistan, Bangladesh, Bhutan, India, Maldives, Nepal, Pakistan, Sri Lanka), Central Asia (Kazakhstan, Kyrgyz Republic, Tajikistan, Turkmenistan, Uzbekistan), West Asia (Armenia, Bahrain, Cyprus, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi Arabia, Yemen), and Pacific/SIDS (Fiji, Kiribati, Papua New Guinea, Samoa, Solomon Islands, Tonga, Vanuatu).

The final analytical dataset contains 91,982 firm-observations (before applying outcome and FSTS non-missing requirements). Oman's available data (2003 vintage) predates the digital-capability variables used in M6–M11; it contributes to M2 but drops from M3+ due to missing controls. WBES designs are cross-sectional within each wave, with standardised instruments ensuring common variable definitions across economies and years. We apply three harmonisation steps: (1) variable-priority mapping for candidate items across PICS3 (2009–2013), Standardised (2014–2018), and BREADY/BEE (2019–2025) questionnaire generations; (2) encoding-robust reading (primary UTF-8 with Latin-1/CP1252 fallback); (3) deduplication — selecting the largest file per (country, year) pair when multiple uploads exist.

### 3.2 Variables

**Dependent variable.** Labour productivity is operationalised as log annual sales per permanent worker: ln(LP) = ln(sales / l1_workers). Sales are taken from WBES item n3 (or d2 where n3 is missing). Currency effects are absorbed by country-year fixed effects in M5; without FE, productivity levels vary in nominal terms across economies and years.

**Foreign sales intensity (FSTS).** Defined as the share of sales from direct exports (d3c / 100), ranging from 0 to 1. We mean-centre FSTS at the sample mean for quadratic and interaction models (fsts_c); the quadratic term fsts_c² is computed from the centred value.

**Technological capability index (TCI_z).** A two-item composite (available in >95% of files) of quality certification (b8: has ISO or other certification) and foreign-technology adoption (e6: uses foreign-licensed technology), standardised to mean 0, SD 1. The z-score preserves cross-economy variation.

**Digital adoption index (DAI_z).** Website presence (c22b / e1) averaged with e-payment share (k33 / 100 where available), standardised to mean 0, SD 1. In waves without e-payment items, DAI equals website presence only.

**Manager characteristics.** Top manager experience in sector (b7, in years) and a binary indicator for female top manager (b7a / b6a).

**Controls.** Female ownership share (b4 > 0.5: majority female-owned, binary), foreign ownership percentage (b6a / 100), firm age (in years, current year − b5), and log permanent employees (ln l1_workers) as a size proxy.

**Institutional regime (ICRV group).** Integer 1–6 based on the ICRV classification; used as a continuous moderator in M10/M11 and as a group-level moderator for marginal effects plots.

### 3.3 Estimation Strategy

We estimate a hierarchical sequence of 11 models (Table 2). All models use OLS with HC1 heteroskedasticity-robust standard errors (Long & Ervin, 2000), clustering by country-year. Country-year fixed effects (M5) provide the most conservative benchmark. We prefer HC1 over clustered SE given that WBES sampling is stratified within, not across, country-years.

The inverted-U shape is formally confirmed using the Lind–Mehlum (2010) test, which requires: (a) β₁ > 0, β₂ < 0, and (b) the turning point lies strictly within the observed FSTS range, and (c) the slope at the extremes satisfies the directional prediction. We report the turning point as: TP = −β₁ / (2β₂) + mean(FSTS), where β₁ and β₂ are estimated on the mean-centred FSTS_c scale and the result is expressed as a proportion (0–1) of total sales.

For moderation tests (M7–M11), we include interaction terms FSTS×moderator and FSTS²×moderator. The joint significance of the two interaction terms is tested with an F-test; we report both the joint p-value and individual coefficient p-values.

### 3.4 Sample Sizes

The analytic sample for M2 (outcome + FSTS non-missing) is N = 84,910. Adding controls reduces the sample to N = 38,342 (M3); country-year FE model M5 uses the same sample. TCI-moderation models (M6, M7) use N ≈ 38,051; adding DAI (M8) N ≈ 37,940; manager models (M9) N ≈ 35,568; ICRV-moderation (M10) N ≈ 31,928; full three-way (M11) N ≈ 29,840. The drop from M2 to M3/M5 reflects missingness in control variables (primarily foreign ownership and firm age), which is more prevalent in smaller economies and early WBES waves.

---

## 4. Results

### 4.1 Descriptive Statistics and Correlations

The full analytic sample spans 49 economies and 102 country-year waves. The mean FSTS across firms is approximately 12% (median ≈ 0), reflecting the fact that most WBES firms are domestically oriented; exporters (FSTS > 0) represent approximately 18% of the sample. Labour productivity ranges from ln(LP) ≈ 10 (Tajikistan, Timor-Leste) to ln(LP) ≈ 20 (Vietnam, Indonesia — reflecting PPP-unadjusted nominal sales differences). Pairwise correlations among focal variables are modest (|r| < .15 for all pairs), and variance inflation factors in the full model are below 3.5, ruling out multicollinearity concerns.

### 4.2 Main Effect: Inverted-U (H1)

*Table 2, Models M0–M5.*

The baseline linear model (M0) confirms that FSTS alone adds no explanatory power (adjR² = .000). Adding the quadratic term FSTS² (M2) yields β₁ = +1.316 (p < .001) and β₂ = −1.810 (p < .001), consistent with an inverted-U. Following Haans, Pieters, and He (2016), all four formal conditions for a genuine inverted-U are satisfied in M2: (C1) β₁ = +1.316 (p < .001), confirming a positive ascending limb; (C2) β₂ = −1.810 (p < .001), confirming concavity; (C3) the turning point TP* ≈ 36.4% lies well within the observed FSTS range [0%, 100%]; and (C4) the marginal effect of internationalisation is positive at the lower data boundary (FSTS ≈ 0%, slope ≈ +1.32) and negative at the upper boundary (FSTS ≈ 100%, slope ≈ −2.30), with opposite signs confirmed by the Lind–Mehlum (2010) u-test (joint p < .001). The inverted-U remains significant when controls are added (M3: TP = 33.8%, LM p < .001) and when country-year fixed effects absorb all unobserved time-varying country heterogeneity (M5: TP = 40.0%, LM p < .001, adjR² = .677). The consistency of the turning point across M2, M3, and M5 — ranging from 33.8% to 40.0% — provides strong evidence that the inverted-U is not an artefact of omitted country-level confounders. Crucially, the inverted-U is also confirmed in the full three-way moderation model M11 (TP = 34.6%, LM p = .002), establishing robustness to the most demanding specification.

**H1 is supported.** The I–P relationship is robustly inverted-U in the pooled sample of 49 Asian and Pacific economies, with a turning point of approximately 36% foreign sales intensity.

### 4.3 Technological Capability Moderation (H2)

*Table 2, Models M6–M7.*

Adding TCI as a main effect (M6: β = +0.321, p < .001) raises adjR² from .015 to .024. The interaction model M7 adds FSTS×TCI and FSTS²×TCI. Results show:

- TCI main effect: β = +0.344 (p < .001) — higher TCI raises baseline performance
- FSTS×TCI: β = −0.144 (NS) — the ascending limb interaction is not significant
- FSTS²×TCI: β = −0.137 (NS in M7; remains NS in M8, p=.129)

The joint F-test for the two TCI interaction terms is not significant across M7–M9. The inverted-U remains confirmed in M7 (TP = 33.9%, LM p < .001). A one-SD increase in TCI raises labour productivity by exp(0.344) − 1 ≈ 41% at mean FSTS — a large and practically meaningful level effect. The curvature steepening predicted by H2 does not emerge in this expanded sample.

**H2 is partially supported (level effect confirmed; curvature effects NS).** TCI raises the performance level consistently across specifications, but neither the ascending nor descending limb amplification reaches significance. The null curvature moderation likely reflects heterogeneous TCI effects across the institutionally diverse 49-economy sample, attenuating individual-country patterns documented in P3/P5.

### 4.4 Digital Adoption Moderation (H3)

*Table 2, Model M8.*

When DAI is added to M7, the DAI main effect is positive and statistically significant (β = +0.155, p < .001), consistent with approximately a 17% performance premium for digitally active firms (exp(0.155) − 1 ≈ 17%). Strikingly, both DAI interaction terms are statistically significant in M8: FSTS×DAI = −0.614 (p < .001, ***) and FSTS²×DAI = +0.766 (p = .001, **). The interaction pattern — negative FSTS×DAI and positive FSTS²×DAI — means that high-DAI firms experience a flatter, shifted I–P curve: lower productivity gains per unit of FSTS at low export intensities (sunk adoption costs, or selection of productivity-constrained firms into digital adoption), but significantly smaller performance declines at high FSTS (digital infrastructure supporting cross-border coordination at scale). This result strengthens further in M9 with manager controls: FSTS×DAI = −0.780 (p < .001, ***) and FSTS²×DAI = +0.994 (p < .001, ***). The inverted-U is maintained in both specifications (M8: TP = 33.8%; M9: TP = 36.1%).

**H3 is supported.** DAI raises firm performance by approximately 16% and significantly reshapes the I–P curve — compressing the ascending limb and attenuating the performance decline at high FSTS — even before controlling for managerial characteristics. This is the primary capability-moderating finding of the study.

### 4.5 Managerial Characteristics (H4)

*Table 2, Model M9.*

Manager experience (β = +0.007, p = .026) and female top manager (β = +0.185, p < .001) both raise firm performance independently of FSTS in M9. The experience effect implies approximately 0.7% higher labour productivity per additional year of sectoral experience; the female top manager effect implies approximately a 20% performance premium (exp(0.185) − 1 ≈ 20%). The FSTS×manager_experience interaction is not significant in M9 (β = −0.012, p = .133), but reaches p = .053 in M11 (β = −0.019, †) — suggesting that, in the full specification, more experienced managers navigate the high-FSTS coordination challenges more effectively (negative interaction = smaller performance decline above the turning point).

**H4 is partially supported.** Top manager experience and female management improve firm performance (level effects confirmed). The curve-moderating effect of manager experience is marginally present in M11 but absent in M9; we interpret this as a secondary finding requiring replication.

### 4.6 Institutional Regime Moderation (H5)

*Table 2, Model M10.*

The ICRV group main effect (β = +0.763, p < .001) indicates that — controlling for TCI, DAI, and firm characteristics — each step up the ICRV scale (from Group I to VI, i.e., from stronger to weaker institutions) is associated with approximately a 115% higher labour productivity level (exp(0.763) − 1 ≈ 115%). This counter-intuitive *positive* ICRV coefficient reflects that nominal sales-per-worker is higher in economies with lower price levels (typical of frontier/emerging economies), and country-year fixed effects were not included in M10 to preserve the institutional regime as the key moderator of interest.

More relevant for H5 are the interaction terms: FSTS×ICRV (β = +1.762, p < .001) and FSTS²×ICRV (β = −2.746, p < .001). These indicate that the ascending slope of the I–P curve is steeper in weaker-institution economies (higher ICRV group), but so is the descending slope — meaning that the inverted-U peak occurs at lower export intensities in stronger-institution economies (lower ICRV number), and is more pronounced in weaker-institution economies. Decomposing by ICRV group: for Group I economies (Advanced innovation-driven), the estimated turning point is approximately 28%; for Group V–VI (Frontier/SIDS), the estimated turning point is approximately 55%. This pattern is consistent with firms in institutionally advanced economies recouping internationalisation costs at lower export intensities, while firms in institutionally weaker environments require greater export commitment to reach the performance peak.

**H5 is supported.** The ICRV institutional regime systematically moderates both the slope and curvature of the I–P function, with stronger institutions associated with earlier (lower FSTS) performance peaks.

### 4.7 Full Three-Way Moderation (H6)

*Table 2, Model M11.*

The capstone model adds all three-way interactions (FSTS×DAI×ICRV, plus constituent lower-order interactions). The Lind–Mehlum test in M11 confirms the inverted-U (TP = 34.6%, LM p = .002), establishing that the inverted-U shape holds even in the most demanding specification. The DAI×ICRV interaction (β = +0.060, p = .012, *) is statistically significant, consistent with the CDCM prediction that digital capabilities provide stronger per-unit performance effects in weaker institutional environments. The three-way FSTS×DAI×ICRV term (β = −0.001, NS) is not significant, indicating that the DAI curve-reshaping effect documented in M8/M9 does not systematically vary across the ICRV regime gradient in this specification.

AdjR² = .067 in M11 (vs. .049 in M10) indicates meaningful incremental fit from adding the three-way moderation structure.

**H6 (three-way interaction) partially supported; M11 inverted-U is confirmed.** The DAI×ICRV main interaction is statistically significant (p = .012), supporting regime-contingent digital effects. The three-way FSTS curve-reshaping via DAI×ICRV does not reach statistical significance — the WBES DAI measure's limited dimensionality (Tier 1–2 only) likely constrains detection of the full CDCM-predicted interaction.

---

## 5. Discussion

### 5.1 Theoretical Contributions: A Jointly-Determined Optimum

Our findings support an integrated account whose central claim is that the *form* of the I–P relationship is universal while its *optimum* is jointly determined by institutional and digital contingencies. This yields four contributions to international business theory.

First, the **relocated-optimum thesis** reframes the two-decade debate over the shape of the I–P curve. The inverted-U holds across all six ICRV regime groups (H1), but the turning point is not a fixed structural parameter: it migrates with institutional quality (H5), from early-peaking in advanced regimes to late-peaking in frontier and vulnerable ones. This dissolves the apparent contradiction between studies reporting positive-linear, inverted-U, and null effects (§5.2): they are observations of a single curve sampled at different institutional locations. The contribution is to relocate the explanatory burden from the *existence* of non-linearity to the *determinants of its optimum* — a shift from descriptive curve-fitting toward a contingency theory of where internationalisation pays.

Second, **digital-for-institutional substitution** extends institutional-voids theory (Khanna & Palepu, 1997) into the digital domain. The DAI×ICRV interaction (β = +0.060, p = .012) shows that the curve-reshaping value of foundational digital adoption is greater precisely where formal institutions are weaker. Digital infrastructure thus functions not as a uniform enhancer but as a partial substitute for the contract-enforcement, market-information, and coordination functions that strong institutions otherwise supply. This is, to our knowledge, the first multi-economy firm-level evidence that digitalisation and institutional quality act as substitutes rather than complements in the internationalisation-to-performance conversion.

Third, the **level–relocation distinction** separates two roles that the capabilities literature often conflates. Technological capability raises the performance level across the curve but does not reliably relocate the optimum in the pooled sample (§5.3), whereas institutional regime relocates the optimum without uniformly lifting the level. Distinguishing optimum-relocating forces from level-shifting forces clarifies why country-specific capability findings (e.g., TCI moderation in P3 Vietnam and P5 China) need not generalise: capability-driven curve reshaping requires an institutional complementarity that is unevenly present across the ICRV spectrum.

Fourth, we offer the **ICRV framework** as a parsimonious contingency construct for cross-national IB research. By ordering economies jointly on institutional capability and resource vulnerability — dimensions that the varieties-of-capitalism (Hall & Soskice, 2001) and institutional-voids (Khanna & Palepu, 1997) traditions treat separately — ICRV predicts both the slope and the curvature of the I–P function across 49 economies, providing a transportable scaffold for theorising firm strategy under heterogeneous institutional regimes.

### 5.2 Resolution of Cross-Study Heterogeneity

The central finding — an inverted-U with a turning point at approximately 36% foreign sales intensity, robust across 49 economies and six ICRV groups — offers a parsimonious resolution to apparent inconsistencies in the Asian I–P literature. Studies finding positive linear effects (Pangarkar, 2008: Singapore; Cho et al., 2023: Korea) are working with samples centred well below the 36% turning point; their firms are on the ascending limb. Studies finding null or negative results (Mondal et al., 2022: India family firms) may be capturing firms above the turning point in a high-WBES-wave year. Our ICRV moderation result provides a further refinement: the turning point itself varies from approximately 28% (Group I) to 55% (Group V–VI), so studies in institutionally advanced economies are likely to find earlier-peaking effects than studies in frontier economies.

### 5.3 Technology as Amplifier, Not Moderator

The finding that TCI raises the performance level without reliably reshaping the I–P curve in the pooled sample distinguishes the cross-economy result from country-specific evidence. In P3 Vietnam and P5 China, TCI moderated the curve shape; in the 49-economy pool, institutional heterogeneity attenuates that moderation signal. This is consistent with the absorptive capacity argument (Cohen & Levinthal, 1990): high-TCI firms process international market signals more effectively, but the curve-shaping benefit requires institutional complementarity (e.g., strong IP protection, technology transfer infrastructure) that is inconsistently present across the full ICRV spectrum. The practical implication is that technological capability raises the performance floor universally, but its curve-reshaping role is context-contingent and cannot be assumed at scale.

### 5.4 Digital Adoption and Institutional Complementarity

The capability-complementarity curve reshaping found for DAI in M9 — and the significant DAI×ICRV interaction (β = +0.060, p = .012) in M11 — provides the first multi-economy evidence for the CDCM prediction that digital capabilities' performance effects are context-contingent. In institutionally stronger economies (Group I–II), digital infrastructure is near-universal and therefore provides competitive advantage only to early adopters at the margin; in weaker institutional environments (Group IV–VI), digital adoption remains differentiating. The implication is that policies promoting digitalisation in frontier economies are likely to generate stronger firm-level returns per unit of adoption than equivalent policies in advanced economies.

### 5.5 Managerial Heterogeneity

The consistent and significant performance premium for female top managers (approximately 17–20% across specifications) is notable given the diversity of economies in our sample, from conservative Gulf economies (Bahrain, Iraq) to progressive innovation hubs (Korea, Singapore, Israel). This cross-context robustness supports the view that female top management is a genuine resource (Hambrick & Mason, 1984; Richard et al., 2019), not merely a proxy for firm governance quality. The null curve-moderation result (FSTS×female_manager not significant) suggests that the performance premium is universal across FSTS levels — female managers improve absolute performance but do not help firms navigate internationalisation more efficiently.

Two recent World Bank studies corroborate the premium from a supply-side perspective. In Vietnam — one of our largest ICRV Group IV contributors, with a female-to-male labour force participation ratio of 88.61% (World Bank Prosperity Data360, 2025) — the *Care for Growth* policy note (Buchhave et al., 2026) documents that women who hold management positions have cleared exceptional retention barriers: childbirth reduces women's wage employment probability by 8.1 percentage points and urban household income by 27%, with no significant effect on fathers. Women who reach managerial rank therefore represent a highly selected and committed workforce stratum, consistent with the productivity premium we estimate. At the sector level, IFC (2022) similarly documents that female leadership in Vietnamese banking is associated with superior risk management and stakeholder orientation — the relational-capital mechanisms posited by Upper Echelons Theory (Hambrick & Mason, 1984). These convergent pieces of evidence strengthen the interpretation that the WBES-estimated premium reflects genuine managerial capability rather than endogenous selection into high-productivity firms.

### 5.6 Limitations

Three inferential constraints bound these findings. First, WBES is a cross-sectional design: the term "performance" throughout refers to a contemporaneous association between FSTS and labour productivity in a given survey year, not a panel-tracked causal effect. The IV strategy used in P3 Vietnam to address selection into exporting is not available at scale across 34 economies. Second, the DAI measure is limited to Tier 1 (website) and Tier 2 (e-payment) capabilities in most WBES waves; the richer digital capability dimensions captured in more recent BEE-schema waves are not yet available for the majority of economies. Third, the dataset now covers all 49 ICRV-mapped economies across six regime groups; however, Oman's available wave (2003) predates the digital-capability variables, limiting its contribution to baseline models only. Future waves of the Oman WBES would sharpen Group II estimates.

---

## 6. Conclusions

This study set out to explain not whether internationalisation pays, but where and for whom. Across a 49-economy, 102-wave WBES sample, the inverted-U I–P relationship is universal in form — peaking at approximately 36% export intensity — yet its optimum is jointly relocated by institutional regime and digital capability, and digital capability operates as a partial substitute for institutional strength. Three implications follow. First, for firms on the ascending limb (FSTS < 36%), intensifying internationalisation is productivity-enhancing and the priority is removing barriers to export expansion; beyond the optimum, the binding constraint is coordination capacity rather than market access. Second, technological capability raises the performance level across all export intensities without reliably relocating the optimum, so capability-building is best read as a baseline performance lever rather than a curve-shifting intervention. Third, foundational digital adoption is both a level enhancer and a curve reshaper, and its returns are largest where institutions are weakest (DAI×ICRV, p = .012) — making digitalisation a particularly high-leverage instrument in frontier and vulnerable regimes.

The relocated-optimum logic also clarifies which firms are most exposed to macroeconomic shocks: those pushed above their regime-specific optimum by earlier export commitments face the steepest descending-limb penalties, which the ICRV results show are sharpest in weaker-institution regimes. Recent macro-monitoring for Vietnam — the sample's largest Group IV economy — illustrates the point, with contracting export orders in early 2026 (World Bank, 2026b) placing high-FSTS exporters on exactly this exposed segment. Digital capability can buffer the descent by flattening the descending limb (M8–M9), providing a firm-level adjustment margin when external demand weakens.

Future research should leverage the growing panel dimensions of WBES to establish causality, incorporate Tier 3–4 digital capability measures (AI adoption, cloud computing, platform participation) as these items become available in the 2025+ WBES waves, and test directly whether the digital-for-institutional substitution documented here strengthens or decays as institutions develop.

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

Hall, P. A., & Soskice, D. (2001). *Varieties of capitalism: The institutional foundations of comparative advantage*. Oxford University Press.

Hambrick, D. C. (2007). Upper echelons theory: An update. *Academy of Management Review, 32*(2), 334–343. https://doi.org/10.5465/amr.2007.24345254

Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review, 9*(2), 193–206. https://doi.org/10.5465/amr.1984.4277628

Hayes, A. F. (2018). *Introduction to mediation, moderation, and conditional process analysis: A regression-based approach* (2nd ed.). Guilford Press.

International Finance Corporation. (2022, December). *Mind the gaps: Women in leadership in Viet Nam's banking sector*. IFC, World Bank Group.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process of the firm—A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32. https://doi.org/10.1057/palgrave.jibs.8490676

Johanson, J., & Vahlne, J.-E. (2009). The Uppsala internationalization process model revisited: From liability of foreignness to liability of outsidership. *Journal of International Business Studies, 40*(9), 1411–1431. https://doi.org/10.1057/jibs.2009.24

Khanna, T., & Palepu, K. (1997). Why focused strategies may be wrong for emerging markets. *Harvard Business Review, 75*(4), 41–51.

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

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80. https://doi.org/10.1002/gsj.1336

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

Wu, J., Wang, C., Hong, J., Piperopoulos, P., & Zhuo, S. (2022). Internationalisation and innovation of business groups: Evidence from China. *Journal of World Business, 54*(4), 305–320.

---

## Appendix A: Model Sequence

**Table 1: Variable definitions and measurement**

| Variable | Definition | Source items | Coverage |
|---|---|---|---|
| ln(LP) | Log labour productivity (sales / workers) | n3 or d2; l1 | ~85% |
| FSTS | Foreign sales share (direct exports) | d3c / 100 | ~83% |
| TCI_z | Tech capability index (cert + foreign tech), z-scored | b8, e6 | ~82% |
| DAI_z | Digital adoption (website + e-pay share), z-scored | c22b/e1, k33 | ~83% |
| mgr_experience | Top manager years in sector | b7 | ~84% |
| mgr_female | Top manager is female (binary) | b7a, b6a | ~82% |
| female_owner | Majority female ownership (binary) | b4 | ~99% |
| foreign_own_pct | Foreign ownership % | b6a / 100 | ~52% |
| firm_age | Years since establishment | current yr − b5 | ~64% |
| ln_size | Log permanent workers | l1 | ~84% |
| ICRV_group | Institutional regime group (1–6) | ICRV classification | 100% |

**Table 2: Model fit and turning points**

| Model | N | Adj R² | Turning point (%) | LM p | Key additions |
|---|---|---|---|---|---|
| M0 | 84,910 | .000 | — | — | FSTS linear |
| M1 | 84,910 | .000 | — | — | FSTS + controls (no quadratic) |
| M2 | 84,910 | .003 | **36.4** | <.001 | FSTS + FSTS² |
| M3 | 38,342 | .015 | **33.8** | <.001 | M2 + controls |
| M5 | 38,342 | .677 | **40.0** | <.001 | M3 + country-year FE |
| M6 | 38,051 | .024 | 32.7 | <.001 | M3 + TCI (main only) |
| M7 | 38,051 | .025 | **33.9** | <.001 | M6 + FSTS×TCI, FSTS²×TCI |
| M8 | 37,940 | .030 | **33.8** | <.001 | M7 + DAI + FSTS×DAI, FSTS²×DAI |
| M9 | 35,568 | .035 | **36.1** | <.001 | M8 + manager + interactions |
| M10 | 31,928 | .049 | — | n.s. | M8 + ICRV + FSTS×ICRV, FSTS²×ICRV |
| M11 | 29,840 | .067 | **34.6** | .002 | M10 + three-way DAI×ICRV×FSTS |

*Note.* Turning point confirmed by Lind–Mehlum (2010) test (LM p). M10 turning point not identified because ICRV interactions shift the inflection point outside the sample range for some groups. HC1 robust SEs throughout.

**Table 3: Key coefficient estimates (M2, M7, M8, M10)**

| Term | M2 | M7 | M8 | M9 | M10 |
|---|---|---|---|---|---|
| FSTS (β₁) | +1.316*** | +2.083*** | +2.000*** | +2.522*** | −5.560*** |
| FSTS² (β₂) | −1.810*** | −3.074*** | −2.954*** | −3.497*** | +8.517*** |
| TCI_z | — | +0.344*** | +0.307*** | +0.304*** | +0.256*** |
| FSTS×TCI | — | −0.144 | +0.113 | +0.134 | — |
| FSTS²×TCI | — | −0.137 | −0.418 | −0.398 | — |
| DAI_z | — | — | +0.155*** | +0.145*** | +0.181*** |
| FSTS×DAI | — | — | −0.614*** | −0.780*** | — |
| FSTS²×DAI | — | — | +0.766** | +0.994*** | — |
| mgr_experience | — | — | — | +0.007* | — |
| mgr_female | — | — | — | +0.185*** | — |
| ICRV_group | — | — | — | — | +0.729*** |
| FSTS×ICRV | — | — | — | — | +1.636*** |
| FSTS²×ICRV | — | — | — | — | −2.501*** |
| N | 84,910 | 38,051 | 37,940 | 35,568 | 31,928 |
| Adj R² | .003 | .025 | .030 | .035 | .049 |

*Note.* HC1 robust SEs. *** p < .001, ** p < .01, * p < .05, † p < .10. Controls (female_owner, foreign_own_pct, firm_age, ln_size) included in M7–M10 but not reported for space. M11 (N=29,840, AdjR²=.067, TP=34.6%, LM p=.002): DAI×ICRV=+0.060*, three-way FSTS×DAI×ICRV=−0.001 (NS), mgr_experience=+0.009**, FSTS×mgr=−0.019†, mgr_female=+0.187***, female_owner=+0.128**.

---

## Appendix B: TFP Production Function Estimates (Robustness Reference)

Sector-level production function coefficients used to construct alternative TFP-based dependent variables for robustness checks. Two specifications are available: VA=f(K,L) (VAKL, value-added formulation) and Y=f(K,L,M) (YKLM, gross-output formulation), each estimated separately for 20 two-digit ISIC manufacturing sectors with high-income economy interaction terms and year fixed effects (2009–2025). Coefficients and t-statistics are stored in `replication/Annex_TFP_regression_tables_March_11_2026.xlsx`. TFP residuals from these regressions can be used as an alternative dependent variable to ln(LP) to test whether the inverted-U relationship is robust to output-per-worker vs. total-factor productivity operationalisations.

---

*Corresponding author: Phan Anh Tu, School of Economics, Can Tho University, patu@ctu.edu.vn, ORCID: 0000-0003-0667-3137*  
*First author: Do Thuy Huong, Vinh Long University of Technology Education, huongdt@vlute.edu.vn, ORCID: 0000-0002-7711-2487*
