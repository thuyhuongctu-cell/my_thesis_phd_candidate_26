# Theory & Measures Integration Guide
**PhD Dissertation: Internationalization, Digital Adoption, and Firm Performance in Asia**
**Author: Do Thuy Huong — Can Tho University**
**Version: 1.0 (May 2026)**

> **Purpose**: Reference document for arguing the theoretical grounding of every measure
> and for ensuring cross-paper consistency in theory integration. Read before writing any
> Theory, Hypotheses, or Methodology section. Complements `00_author_voice_guide.md` and
> `cross_paper_terminology.md`.

---

## Part I — Integrated Theoretical Architecture

### 1.1 Why Four Theories, Not One

A single-theory approach would miss the multi-level nature of the I–P relationship. The
dissertation uses four theoretical pillars that operate at different levels of analysis:

| Pillar | Level | Core claim | Role in CDCM |
|--------|-------|-----------|--------------|
| **Uppsala Model** (Johanson & Vahlne, 1977, 2009) | Process (firm trajectory) | Internationalization proceeds via experiential learning; foreign market commitment increases as knowledge accumulates | Explains *why* FSTS follows a non-linear path: early-stage export generates learning returns, but beyond a threshold organisational complexity dominates |
| **Resource-Based View** (Barney, 1991; Wernerfelt, 1984; Peng, 2001) | Firm capabilities | Sustained performance advantage requires VRIN resources; TCI is a validated capability proxy; DAI is a foundational digital adoption indicator | Establishes TCI as a *capability-level moderator* and DAI as a *digital adoption moderator* — both shift the FSTS turning point, but through different mechanisms (process competence vs. market visibility) |
| **Institutional Theory** (North, 1990; Scott, 1995; Khanna & Palepu, 2010) | Country/regime context | Formal and informal institutions shape the transaction-cost environment in which firm resources yield returns | Provides the logic for ICRV as a contextual moderator: the same DAI level yields higher returns in Advanced regimes (credible digital infrastructure) than in Frontier regimes (weak enforcement) |
| **Upper Echelons Theory** (Hambrick & Mason, 1984; Hambrick, 2007) | Manager cognition | Top manager characteristics (experience, gender) shape strategic risk tolerance and foreign-market commitment | Justifies the inclusion of manager-level moderators in M4–M5; also explains heterogeneity in turning points across firm subgroups |

**Foundational Digital Adoption Framework** (Stallkamp & Schotter, 2021; Verhoef et al.,
2021; Banalieva & Dhanaraj, 2019): a fifth integrating layer that bridges RBV (TCI as a
process-capability moderator) and institutional theory (the translation of digital adoption
into export-market benefits varies by ICRV regime). This is the theoretical foundation of
CDCM.

> **Critical measurement boundary (read before citing DAI as "capability"):**
> WBES items for DAI are binary adoption/presence measures — c22b (website presence),
> k33 (e-payment from customers), k38 (e-payment to suppliers). These map to Tier 1
> (digitization) and Tier 2 (digitalization) in the Verhoef et al. (2021) hierarchy.
> WBES does **not** contain items for Tier 3 (digital process integration: ERP, CRM) or
> Tier 4 (digital dynamic capability: AI deployment, platform reconfiguration). Therefore,
> DAI in this dissertation measures **digital adoption/presence**, not digital capability.
> Framing DAI as "dynamic digital capability" would overstate what the WBES instrument
> supports. Use "digital adoption" language when describing DAI; reserve "digital capability"
> for TCI (which captures process-technology absorption) and for theoretical mechanisms only.

### 1.2 The CDCM Logic Chain

```
[Uppsala] → FSTS follows inverted-U path due to learning/complexity trade-off (H1)
               ↓
[RBV] → TCI shifts the turning point rightward by buffering complexity costs (H2)
               ↓
[RBV + Foundational Digital Adoption Framework] → DAI shifts the turning point contingently (H3)
               ↑
[Institutional Theory] → Direction and magnitude of DAI shift depends on ICRV regime (H5)
               ↓
[Upper Echelons] → Manager experience/gender moderate the learning rate (H4)
               ↓
[All theories] → Temporal heterogeneity: DPL phases shift baseline FSTS returns (H6)
```

**Key architectural rule**: Theories are not additive "a list of cited theories" but
interlocking mechanisms. Each theory explains a *different arrow* in the model. A reviewer
who asks "why four theories?" should receive: "Each theory governs a different moderating
pathway; no single theory predicts both capability-contingent and institution-contingent
moderation simultaneously."

### 1.3 Theory Integration Language Template

When introducing the theoretical framework at the start of a paper, use this structure:

> "The internationalization–performance relationship is best understood as a
> **process-capability-context interaction** rather than a main effect. The Uppsala model
> (Johanson & Vahlne, 1977, 2009) predicts a non-linear trajectory driven by learning
> accumulation and coordination complexity; the resource-based view (Barney, 1991) explains
> why technological capability (TCI) and foundational digital adoption (DAI) alter the efficiency of that trajectory;
> institutional theory (North, 1990; Scott, 1995) conditions the returns to those
> capabilities on the regime-level quality of formal institutions; and Upper Echelons theory
> (Hambrick & Mason, 1984) introduces managerial-cognitive heterogeneity as a second
> capability-level moderator. Together, these form the Context-Contingent Digital-and-Capability
> Model (CDCM), which is tested empirically in this study. [Note: 'Digital' in CDCM refers
> to the DAI adoption dimension; 'Capability' refers to the TCI process-competence dimension.
> DAI is a digital adoption measure, not a dynamic capability measure.]"

---

## Part II — Measure Argumentation Library

### 2.1 FSTS — Export Intensity (Independent Variable, Quadratic)

#### Definition
FSTS = direct export sales / total annual sales, bounded [0, 1]. Mean-centred before
squaring (FSTSc = FSTS − wave mean) to reduce collinearity between FSTS and FSTS².

#### Why FSTS, not DOI or number of foreign markets?

**Theoretical justification (RBV + Uppsala):**
> "Export intensity (FSTS) captures the degree of resource commitment to foreign markets
> at the intensive margin — the *depth* of international engagement among active exporters
> (Lu & Beamish, 2001). Broader DOI indices (e.g., Ramaswamy et al., 1996) confound
> geographic scope with sales intensity, making it impossible to isolate the productivity
> consequences of deepening export engagement from the consequences of market diversification.
> WBES item `e1/d2` provides a direct, comparably-defined intensity measure across all 47
> economies and 14 survey waves, enabling within-country-wave coefficient stability tests
> (Paternoster et al., 1998)."

**Methodological justification (WBES data boundary):**
> "WBES does not collect balance-sheet data (assets abroad, number of subsidiaries) that
> would enable broader internationalisation measures. FSTS is both the theoretically cleanest
> intensive-margin measure and the only internationalisation variable available across all
> country-waves in the pooled dataset."

#### Why include FSTS² (quadratic)?

**Uppsala mechanism:**
> "The Uppsala model predicts that export returns follow an inverted-U path: early
> internationalisation yields economies of scale and learning returns (positive FSTS slope),
> but beyond a threshold the coordination costs of managing large foreign-sales portfolios
> dominate (negative FSTS² coefficient). Including FSTS² is not a data-mining exercise —
> it is the direct empirical implication of the learning-versus-complexity trade-off in
> the 2009 Uppsala revision (Johanson & Vahlne, 2009, p. 1424)."

**Test for interior maximum:**
> "We verify the inverted-U interpretation using the Lind–Mehlum (2010) test for a
> statistically significant interior maximum within the data range, rather than relying
> on the sign pattern alone. A turning point outside the empirical support [0, 1] would
> be theoretically uninteresting; the test confirms an interior maximum at approximately
> [X]% FSTS in each sample."

#### Reviewer challenge: "Why not control for endogeneity of FSTS?"

**Inferential bounds framing (3-part, per author voice guide):**
> "We cannot rule out selection bias — more productive firms may self-select into
> exporting — because the WBES cross-sectional design does not support a valid instrument
> for FSTS that is excluded from the lnLP equation (a). The Heckman inverse Mills ratio
> approach (Heckman, 1979) addresses selection at the extensive margin (exporter vs.
> non-exporter) but does not instrument the continuous FSTS level (b). We address this
> inferential constraint by including an exporter dummy alongside FSTS to partial out
> the selection-into-exporting level effect, and by reporting sensitivity analyses with
> the sample restricted to exporters only, where the selection problem is attenuated (c).
> Following Solon et al. (2015), we interpret our coefficients as conditional associations
> rather than causal estimates."

---

### 2.2 TCI — Technological Capability Index (Moderator)

#### Definition
Z-standardised composite of 2–4 WBES technology items (varying by wave and module
availability): quality certification (b8), foreign technology licensing (e6), imported
machinery (h8), ISO certification (h1). Items standardised within-wave, then averaged
(minimum 3 of 4 non-missing for waves where 4 items available).

#### Why TCI, not R&D expenditure or patent count?

**RBV justification:**
> "TCI operationalises the firm's *absorptive capacity* (Cohen & Levinthal, 1990) and
> *technological resource stock* (Barney, 1991) using items available across all WBES
> waves. Patent counts and R&D expenditures are not collected in WBES. Quality certification
> (b8) and foreign technology licensing (e6) are theoretically central: certification
> signals formal quality control capacity that reduces liability of foreignness in export
> markets (Zaheer, 1995); foreign technology licensing signals the firm's capacity to
> access and absorb external knowledge, the key RBV mechanism by which TCI amplifies
> FSTS returns (Lall, 1992; Teece et al., 1997)."

#### Why a formative composite, not a reflective scale?

> "TCI is specified as a formative index — each item captures a distinct facet of
> technological capability (quality management, technology access, embodied capital) rather
> than being interchangeable reflections of a latent construct. Cronbach's α is therefore
> not the appropriate reliability criterion; instead, we assess construct validity by
> confirming that (a) TCI correlates positively with labour productivity in descriptive
> statistics (convergent validity) and (b) the sign and magnitude of TCI's moderating
> coefficient is stable across robustness specifications with individual items used
> separately (discriminant stability)."

#### Cross-wave comparability caveat

> "The 2009 and 2015 WBES modules include only b8 and e6 (TCI_2item = 2-item composite);
> the 2023 BREADY module adds h1 and h8, enabling TCI_4item (4-item composite). We
> standardise each version within-wave before pooling, which addresses mean-level
> differences but does not fully resolve item-set heterogeneity. We flag this as a
> measurement boundary in Mục 3.2 and treat cross-wave TCI comparisons as
> provisional."

---

### 2.3 DAI — Digital Adoption Index (Moderator)

#### Definition

| Version | Papers | Items | Rationale |
|---------|--------|-------|-----------|
| **DAI Tier-1 (thin)** | P3 (all waves), P5 (2012) | Website presence only (c22b) | Only digital item available in 2009–2012 WBES |
| **DAI Tier-1+2 (composite)** | P4 (Singapore 2023), P5 (2024) | Website (c22b) + e-payment (k33/k38) | BREADY module adds e-payment in 2019+ |

Z-standardised within sample before regression (`DAI_z`).

#### Why website presence is sufficient for DAI Tier-1

**Measurement constraint argument:**
> "The 2009 and 2015 WBES instruments predate the BREADY digital survey module
> (introduced 2019). Only item c22b — 'Does this establishment have its own website?' —
> is available across all waves in the 2009–2023 pooled analysis. Website presence
> represents the threshold of *formal digital visibility* that distinguishes digitally
> engaged firms from non-participants in global information flows (Stallkamp & Schotter,
> 2021). While this measure does not capture digital depth (e-payment, e-procurement,
> ERP integration), cross-wave comparability requires a common measurement base.
> We treat DAI Tier-1 as a **foundational digital adoption indicator (lower-bound adoption signal)**
> and report sensitivity analyses using DAI Tier-1+2 where the 2023 BREADY module is available.
> This measure does not claim to capture digital capability; it captures digital presence/adoption."

**Theoretical justification (Foundational Digital Adoption — digital presence as entry condition):**
> "A firm without a website operates below the visibility threshold for digital market
> participation; the binary distinction between website presence and absence captures
> the *entry condition* for digital export market discovery (Stallkamp & Schotter, 2021;
> Banalieva & Dhanaraj, 2019). This is a digital adoption threshold (Rogers, 1962 diffusion
> framework), not a dynamic capability. Above this threshold, the marginal effect of deeper
> digital adoption (e-payment) on performance is better modelled as a continuous interaction
> — addressed in P4 and P5 2024 analyses using DAI Tier-1+2."

#### Why DAI and TCI are kept separate (not collapsed into one composite)

**CDCM theoretical argument:**
> "Digital adoption (DAI) and technological capability (TCI) are theoretically distinct
> constructs that operate through different mechanisms. TCI captures *process-oriented*
> capability — the firm's internal capacity to produce and innovate — and functions as
> a buffer against coordination complexity as FSTS increases. DAI captures
> *market-interface* capability — the firm's visibility and transactional reach in digital
> export markets — and functions as an amplifier of export-market learning returns.
> Collapsing them would conflate capability type and capability domain, obscuring the
> boundary conditions that CDCM predicts (H2 ≠ H3 in direction and magnitude across ICRV
> regimes). The empirical separation is confirmed by their modest correlation
> (r ≈ 0.12–0.18 across samples), indicating low multicollinearity and supporting
> discriminant validity."

#### Reviewer challenge: "DAI is a crude binary — does it really capture digital capability?"

> "We acknowledge that website presence is a *minimum-bar* digital adoption indicator that
> does not distinguish basic informational sites from sophisticated digital sales platforms.
> Three points limit the inferential damage. First, during the 2009–2015 period, website
> presence itself was a meaningful differentiator for SMEs in frontier and emerging Asian
> economies, where fewer than 30% of surveyed firms had websites (WBES descriptive
> statistics, Table 1). Second, the interaction coefficient on DAI × FSTS — rather than
> the DAI main effect — is the theoretical parameter of interest; a crude DAI measure
> biases this interaction toward zero, making any detected effect a conservative lower
> bound. Third, in waves where Tier-1+2 is available, the Tier-1 and Tier-1+2 interaction
> results are directionally consistent, suggesting that the website signal captures genuine
> digital engagement variance."

---

### 2.4 ICRV — Institutional Context Regime Variation (Contextual Moderator)

#### Definition
Six-regime classification of WBES economies based on World Governance Indicators (WGI)
Rule of Law, Control of Corruption, and per-capita GNI:

| Regime | CD2 Code | Economies | WGI Rule of Law threshold |
|--------|---------|-----------|--------------------------|
| Advanced Innovation-Driven | Nhóm I | Singapore, Korea, Israel | > +0.8 |
| Advanced Resource-Driven | Nhóm II | Gulf states (UAE, Oman, Saudi Arabia, Kuwait, Qatar) | > +0.4 (resource rents dominant) |
| Upper-Middle Transition | Nhóm III | China, Malaysia, Thailand | −0.2 to +0.4 |
| Emerging | Nhóm IV | Vietnam, India, Indonesia, Philippines | −0.5 to −0.2 |
| Frontier | Nhóm V | Bangladesh, Pakistan, Myanmar, Cambodia, Nepal, etc. | < −0.5 |
| Pacific SIDS | Nhóm VI | Fiji, Papua New Guinea, Samoa, etc. | Micro-state boundary case |

#### Why six regimes, not continuous WGI?

**Institutional theory justification:**
> "Continuous WGI scores treat institutional quality as a smooth gradient, but institutional
> theory (North, 1990) suggests that *discrete thresholds* in formal institution quality
> produce qualitative changes in the transaction-cost environment. A firm navigating
> contract enforcement with WGI Rule of Law = −0.6 (Vietnam) faces categorically different
> uncertainty than a firm in Singapore (WGI = +1.7). The six-regime classification captures
> these threshold effects while remaining fine-grained enough to detect the Advanced
> Innovation/Resource distinction that is theoretically important for DAI returns: digital
> infrastructure quality and e-commerce regulatory certainty differ systematically between
> innovation-driven and resource-driven Advanced economies."

**Methodological justification (k-means stability):**
> "The six-regime partition was validated using k-means clustering on WGI Rule of Law,
> Control of Corruption, Regulatory Quality, and GNI/capita, with silhouette-score
> stability confirmed for k = 6 against k = 4, k = 5, and k = 7 alternatives. The
> Advanced Innovation / Advanced Resource split within Group I (k = 5) vs. Group I + II
> (k = 6) is supported by the substantively different DAI coefficients observed between
> Singapore (Group I) and Gulf states (Group II) in preliminary analyses."

#### Cross-paper ICRV placement

| Paper | Economy | ICRV Regime (6-code) | ICRV Regime (5-code P3/P6) |
|-------|---------|---------------------|---------------------------|
| P3 | Vietnam | Nhóm IV (Lower_mid_transition) | Nhóm IV (Lower_mid_transition) |
| P4 | Singapore | Nhóm I (Advanced Innovation) | Advanced I |
| P5 | China 2012–2024 | Nhóm III (Upper-Middle) | Upper-Middle III |
| P6 meta | All 47 | All 6 regimes as moderator | 5-regime subgroup |

**Placement sentence templates:**

*P4 Singapore*: "Singapore represents an analytically extreme case of the Advanced
Innovation-Driven regime (ICRV Group I; WGI Rule of Law +1.71 in 2023), where digital
infrastructure is world-class, contract enforcement is near-certain, and e-payment
regulation is clear — conditions under which CDCM predicts DAI should exert its strongest
amplifying effect on export-performance returns."

*P3 Vietnam*: "Vietnam is classified at Nhóm IV (Lower_mid_transition) of the ICRV
classification (Group 4 of 6; WGI Rule of Law approximately −0.66 to −0.68 in 2009,
improving to −0.09 in 2023, World Bank) — a lower-middle-income transition economy where
digital infrastructure exists but institutional support for digital transactions remains
incomplete, generating the conditional moderation pattern predicted by CDCM."

*P5 China*: "China's WBES private-firm sample — excluding state-owned enterprises by
design — maps to ICRV Group III (Upper-Middle Transition; WGI Rule of Law approximately
−0.15 to +0.06 across the 2012–2024 interval). This regime position predicts that TCI
moderation is present (RBV operates) but DAI moderation is attenuated by the uneven
development of China's digital regulatory environment across provinces."

---

## Part III — Hypothesis Construction Templates

### 3.1 H1 — Non-linear FSTS–Performance Relationship

**Template (Uppsala mechanism):**
> "The Uppsala model (Johanson & Vahlne, 1977, 2009) predicts that firm performance
> responds to export intensity in a non-linear fashion. In early stages of
> internationalisation, increasing FSTS generates knowledge about foreign market demand,
> supply chains, and operational logistics, enabling firms to exploit economies of scale
> and scope (Johanson & Vahlne, 1977). Beyond a threshold level, however, the coordination
> costs of managing diverse foreign-market relationships — liability of foreignness,
> cultural distance, monitoring costs — begin to dominate learning returns (Hilmersson &
> Johanson, 2016; Tan & Mahoney, 2006), generating a negative marginal effect of further
> FSTS increases. This inverted-U trajectory has been documented in manufacturing exporters
> (Hitt et al., 1997; Lu & Beamish, 2001) and in meta-analytic syntheses (Do & Phan, 2026 —
> k = 238, r̄ = 0.07). Therefore:
>
> H1: Export intensity (FSTS) is related to labour productivity in an inverted-U pattern,
> with performance increasing at low FSTS levels and decreasing at high FSTS levels
> (conditional on technological capability [TCI] and foundational digital adoption [DAI], holding other factors constant)."

### 3.1b H1b — Forced Internationalization Penalty (FIP) — SIDS Boundary Condition

**Context:** P8 only — Pacific Small Island Developing States (ICRV Nhóm VI).

**Template (FIP mechanism — 3-prerequisite framework):**
> "The inverted-U paradigm assumes three structural prerequisites that allow internationalization to generate net positive performance returns at low-to-moderate export intensity levels: (1) a viable domestic market of sufficient size to fund the organizational capabilities required for profitable exporting; (2) manageable trade costs commensurate with the value of exportable output; and (3) functional institutional support for international market access — including trade finance intermediaries, contract enforcement, and standards infrastructure (Winters & Martins, 2004; Briguglio, 1995; Khanna & Palepu, 2010). When all three prerequisites are simultaneously absent, the inverted-U collapses into a monotone negative relationship. We term this the Forced Internationalization Penalty (FIP): firms export not because exporting creates competitive advantage but because the domestic market cannot sustain their operations, and the structural costs of exporting exceed the revenue gains in every marginal unit of export intensity. FIP is theoretically distinct from: (a) phase-1 learning costs in three-stage theory (Contractor et al., 2003), which predict eventual positive returns; (b) Liability of Foreignness (Zaheer, 1995), which operates on the host-market side; and (c) necessity entrepreneurship (Sarasvathy et al., 2014), which operates at the firm level rather than as a structural regime-level constraint. Therefore:
>
> H1b: In Pacific SIDS economies — where all three structural prerequisites of the inverted-U are simultaneously absent — export intensity (FSTS) is monotonically negatively associated with labour productivity, with no statistically significant turning point within the observed FSTS range (FIP boundary condition)."

**Empirical anchor (P8):** β(FSTS_c) = −0.404 (p = .032, M1 country+year FE, N = 1,469); M2 quadratic both NS; Lind–Mehlum test: NS. Robust across M_yearFE (β = −1.236, p < .001) and exporters-only (β = −0.901, p = .027).

**Key citations:** Winters & Martins (2004); Briguglio (1995); Read (2004); Khanna & Palepu (2010); Contractor et al. (2003); Zaheer (1995); UN General Assembly (2024).

**Critical rule:** FIP is the *boundary condition* of the inverted-U, not a variant of it. It signals that the institutional context has crossed a threshold below which the basic preconditions for positive internationalization returns no longer hold. This is a qualitative (sign-changing) departure, not a quantitative (magnitude-shifting) one.

---

### 3.2 H2 — TCI Positive Moderation (Turning-Point Shift)

**Template (RBV mechanism):**
> "Resource-based theory posits that firm-specific capabilities determine the productivity
> of strategic actions (Barney, 1991; Wernerfelt, 1984). Technological capability — captured
> by TCI — reduces the marginal coordination cost of deep internationalisation by increasing
> process efficiency (quality certification đến lower defect rates in export production),
> foreign knowledge absorption (technology licensing đến reduced information asymmetry in
> foreign markets), and product-quality signalling (ISO certification đến reduced liability of
> foreignness). Formally, TCI shifts the FSTS–performance turning point rightward by
> expanding the range over which learning returns dominate complexity costs. Firms with high
> TCI extract positive performance returns from higher FSTS levels before coordination costs
> dominate (Lall, 1992; Peng, 2001). Therefore:
>
> H2: Technological capability (TCI) positively moderates the FSTS–performance relationship,
> such that higher TCI raises the turning-point threshold at which FSTS transitions from
> a positive to a negative performance effect."

### 3.3 H3 — DAI Conditional Moderation (CDCM)

**Template (Foundational Digital Adoption Framework + Institutional Theory interaction):**
> "Digital adoption (DAI) introduces a dual theoretical prediction that distinguishes it
> from TCI moderation. On one hand, the foundational digital adoption framework (Stallkamp &
> Schotter, 2021; Banalieva & Dhanaraj, 2019) predicts that website presence — by increasing
> market visibility, reducing search costs for foreign buyers, and enabling asynchronous
> communication — amplifies the learning returns from international engagement, suggesting
> a positive DAI × FSTS interaction at low-to-moderate FSTS levels. [Note: This is a digital
> *adoption* mechanism, not a dynamic capability mechanism; the WBES binary items support
> the adoption framing, not Tier-3/4 capability framing.] On the other hand,
> institutional theory (North, 1990) implies that this amplifying effect is conditional:
> in regimes where digital infrastructure is high-quality and e-commerce regulations are
> credible (ICRV Group I — Singapore), DAI generates reliable export-discovery advantages;
> in regimes where digital infrastructure is incomplete and enforcement uncertain (ICRV
> Groups IV–V — Vietnam, frontier economies), DAI's amplifying effect is muted or absent.
> This context-contingency distinguishes H3 from H2 and is the core prediction of CDCM.
> Therefore:
>
> H3: Digital adoption (DAI) moderates the FSTS–performance relationship in a
> context-contingent manner: the direction and magnitude of the DAI × FSTS interaction
> varies systematically across ICRV institutional regimes, with the strongest positive
> moderation predicted in Advanced Innovation-Driven regimes and attenuated or absent
> moderation predicted in Emerging and Frontier regimes."

### 3.4 H5 — ICRV Regime Gradient

**Template (Institutional Theory):**
> "Institutional theory (North, 1990; Scott, 1995) predicts that the institutional
> environment in which a firm operates constrains or enables the returns to any given
> strategy. In the context of internationalisation, formal institutions — contract
> enforcement, property rights, regulatory quality — determine whether export-market
> advantages (access to foreign demand, knowledge inflows) can be captured without
> being dissipated by institutional friction (Khanna & Palepu, 2010; Peng, 2003). The
> ICRV framework translates this prediction into a six-regime gradient: moving from
> Frontier (Group V) to Advanced Innovation-Driven (Group I), each step up the regime
> ladder increases the predictability of returns from internationalisation, reduces
> contract uncertainty, and strengthens digital infrastructure quality. We therefore
> expect a positive ICRV-regime gradient in baseline FSTS–performance coefficients.
> Therefore:
>
> H5: The baseline FSTS–labour productivity relationship is stronger in higher-ICRV
> regimes (Advanced Innovation-Driven, Upper-Middle) than in lower-ICRV regimes
> (Emerging, Frontier), reflecting the institutional-context gradient predicted by
> institutional theory."

---

## Part IV — Reviewer Defense Quick Reference

### 4.1 Challenge Map

| Reviewer challenge | Primary response | Backup argument |
|-------------------|-----------------|----------------|
| "FSTS is endogenous" | Inferential bounds framing (Mục 2.1) + exporter-only sensitivity | Panel fixed effects (where available) absorb time-invariant selection |
| "TCI is not validated" | Formative index justification (Mục 2.2) + convergent validity descriptives | Individual-item robustness in Appendix Table |
| "Website binary is too crude for DAI" | Lower-bound conservative bias argument (Mục 2.3) | Tier-1+2 sensitivity in 2023 wave confirms direction |
| "ICRV cutoffs are arbitrary" | k-means silhouette validation (Mục 2.4) | WGI continuous sensitivity in Appendix |
| "Why four theories?" | Process-capability-context interaction necessity (Mục 1.2) | Each theory governs a distinct arrow in the conceptual model — no single theory predicts both H2 and H3 |
| "H3 and H2 are the same hypothesis" | CDCM mechanism differentiation (Mục 1.2 + Mục 3.3) | Empirical test: TCI and DAI coefficients differ in sign/magnitude across ICRV regimes |
| "The turning point is outside sample support" | Report Lind–Mehlum utest | Report CI for TP; if boundary case, reframe as "support-constrained estimate" |
| "FIP is just the first stage of Uppsala learning costs" | FIP is a structural regime, not a temporal phase — no recovery expected within observed FSTS range; Lind–Mehlum NS confirms no inflection | Contrast: 3-stage theory predicts eventual positive slope; SIDS data show uniformly negative slope across all specifications |
| "FIP could be explained by firm-level selection bias" | Country+year FE absorb country-level structural factors; exporters-only subsample β = −0.901 (p = .027) confirms result among active exporters | Direction consistent across 4 specifications with different FE structures |
| "FIP needs to be tested with panel data" | Cross-sectional pooling with country FE is standard in WBES SIDS literature (Goedhuys & Sleuwaegen, 2013); limited panel variation for SIDS in WBES | Future agenda: Fiji + PNG have 2 waves — scope for panel check in future research |

### 4.2 Standard Inferential Bounds Paragraph

Use this structure whenever reporting a finding that has a known methodological limitation:

> "(a) [What cannot be concluded]: We cannot interpret [finding X] as evidence that
> [causal claim Y] because [specific reason — e.g., no instrument, cross-sectional design,
> binary measure].
> (b) [What remediation is available]: The [method Z — e.g., exporter-only subsample,
> Heckman selection check, Tier-1+2 sensitivity] addresses this concern partially by
> [mechanism — e.g., conditioning on export participation, modelling selection, extending
> the digital measure].
> (c) [Citation for the method]: This approach follows [Author, year], who recommend [Z]
> when [constraint] applies."

---

## Part V — Cross-Paper Consistency Rules

### 5.1 Theory citation consistency

Every paper must cite all four pillars in Mục 2 Theory, even if only one is the primary anchor.
Minimum citations per theory:

| Theory | Mandatory citations | Optional additional |
|--------|---------------------|---------------------|
| Uppsala | Johanson & Vahlne (1977, 2009) | Hilmersson & Johanson (2016) |
| RBV | Barney (1991), Wernerfelt (1984) | Peng (2001), Teece et al. (1997) |
| Institutional | North (1990), Scott (1995) | Khanna & Palepu (2010), Peng (2003) |
| Upper Echelons | Hambrick & Mason (1984), Hambrick (2007) | Only in H4 papers |
| Digital Adoption (Foundational) | Stallkamp & Schotter (2021), Banalieva & Dhanaraj (2019), Rogers (1962) | Verhoef et al. (2021) — Tier 1–2 only; NOT dynamic capability |

### 5.2 Contribution framing (per author voice guide Mục 2, Pattern 4)

Each paper's contribution must state: (1) what is found, (2) which prior ambiguity this
resolves, (3) what methodological advance enables this resolution.

| Paper | Core finding | Prior ambiguity resolved | Methodological advance |
|-------|-------------|------------------------|----------------------|
| P3 Vietnam | TP ≈ 12–13% FSTS; TCI positive; DAI null in 2009/2015, positive in 2023 | Whether CDCM holds in Frontier regime | First 3-wave Vietnam test; Paternoster z-test for coefficient stability |
| P4 Singapore | TP ≈ 88.6% FSTS; DAI amplification at high FSTS; Heckman IMR confirms pattern | Whether DAI amplification is strongest in Advanced regime (CDCM Group I prediction) | Exporters-only identification; DAI Tier-1+2 composite; bootstrapped TP CI |
| P5 China | TP ≈ 48–49% FSTS; TCI positive; DAI binary (website) null; 2012 đến 2024 shift | Whether CDCM holds in Upper-Middle Transition regime; DPL phase shift | 2-wave cross-cohort comparison; Paternoster cross-wave z-test |
| P6 meta | r̄ = 0.07, I² = 88%; ICRV gradient confirmed; cDAI positive; DPL phase inflection | Conflation of institutional context with capability effects in prior meta-analyses | Three-level MARA with 3 new moderators; ICRV as continuous regime moderator |

### 5.3 ICRV cross-paper referencing rule

Every paper must contain a sentence in Mục 5 Discussion that:
1. States the paper's ICRV regime placement
2. Explains why the findings are consistent with (or diverge from) CDCM predictions for
   that regime
3. Cross-references at least one other paper at a different regime for comparative framing

**Template:**
> "The [finding] is consistent with CDCM's prediction for [ICRV regime]. In contrast,
> [comparative paper] — operating in [other ICRV regime] — reports [other finding],
> confirming the institutional-context gradient: [mechanism explanation]. Together, these
> results support H5's prediction of a systematic ICRV × DAI interaction across the
> Advanced-to-Frontier spectrum."

---

---

## Part VI — Full H3 Development: The Moderating Role of Digital Adoption (DAI)

> Follows the 4-part structure from `academic-theory-hypotheses-development` skill:
> (1) Theoretical rationale đến (2) Empirical evidence đến (3) Contextual consideration đến 
> (4) Hypothesis statement. This section is a ready-to-use draft for the Theory &
> Hypotheses section of any paper in the dissertation.

---

### Section 2.X (ready to paste into manuscript): The Moderating Role of Digital Adoption

#### 2.X.1 Theoretical Rationale

**Paragraph 1 — Foundational digital adoption and market-interface function:**

> **Framing note**: DAI in this dissertation captures digital *adoption* (binary website
> presence / e-payment usage from WBES), not dynamic digital capability. Theoretical
> arguments in this section refer to the mechanism by which foundational digital presence
> reduces market-interface friction — which is observable with Tier-1/2 WBES items.
> Do not frame this as a "dynamic capability" argument; WBES data cannot support Tier-3/4
> claims.

Digital adoption at the foundational level — website presence (Tier 1) and electronic
payment usage (Tier 2) — functions primarily at the market-interface rather than the
production-process level. The foundational digital adoption framework (Stallkamp &
Schotter, 2021; Banalieva & Dhanaraj, 2019) conceptualises these tools as mechanisms that
reduce the geographic and informational friction inherent in cross-border transactions. A firm with a web presence — the minimum-bar indicator of digital adoption
(DAI Tier-1) — gains visibility to foreign buyers through search engines and digital
marketplaces, reduces response latency to international orders, and signals credibility in
markets where physical proximity cannot substitute for reputational signals. These
properties directly address the *information asymmetry* that drives liability of foreignness
in export markets (Zaheer, 1995): digitally visible firms face lower discovery costs for
foreign buyers and lower verification costs for foreign buyers evaluating unfamiliar
suppliers. As export intensity (FSTS) increases, these advantages compound — each
additional percentage of foreign sales is more efficiently managed through digital channels
than through agent-mediated or physical showroom contact. This predicts a positive DAI ×
FSTS interaction: among firms with equivalent internationalisation depth, digitally adopted
firms extract higher performance returns per unit of FSTS increase.

**Paragraph 2 — The ICRV conditioning mechanism:**

However, the foundational digital adoption framework does not operate in an institutional
vacuum. The returns to digital adoption for export-market engagement depend critically on
the *credibility* and *completeness* of the digital infrastructure in the firm's operating
environment — a factor that varies systematically across the ICRV institutional spectrum.
Institutional theory (North, 1990; Scott, 1995) predicts that formal institutions —
specifically, digital-transaction regulations, payment system reliability, intellectual
property protection, and e-commerce enforcement capacity — determine whether digital
adoption translates into realised competitive advantages or remains latent potential.
In Advanced Innovation-Driven regimes (ICRV Group I, e.g., Singapore), digital
infrastructure is world-class, e-commerce regulation is transparent, and digital payment
systems are ubiquitous; a firm's DAI investment yields predictable, reliable export-market
discovery and transaction-processing benefits. In Emerging and Frontier regimes (ICRV
Groups IV–V, e.g., Vietnam, Bangladesh), digital infrastructure exists but is patchy,
e-commerce trust is lower, and payment system reliability is inconsistent — conditions
under which the same DAI investment yields uncertain returns, and may even generate
disadvantages if digital visibility attracts fraudulent buyers or creates compliance costs
without corresponding revenue gains. This ICRV conditioning mechanism generates the
context-contingency prediction at the core of CDCM: *DAI moderates the FSTS–performance
relationship in the direction predicted by the foundational digital adoption framework, but
only above a threshold institutional quality that varies by ICRV regime.*

**Paragraph 3 — Distinguishing DAI moderation from TCI moderation:**

It is important to distinguish the mechanism by which DAI moderates the I–P relationship
from the mechanism by which TCI moderates it (H2). TCI operates through a
*process-competence* channel: higher quality certification and foreign technology absorption
reduce the marginal coordination cost of managing complex export operations, shifting the
inverted-U turning point rightward without requiring institutional complementarity. DAI
operates through a *market-discovery-and-signalling* channel: digital visibility reduces
search and verification frictions for foreign buyers, amplifying learning returns at the
intensive margin of internationalisation. This mechanism is more exposed to institutional
context than TCI because it depends on external infrastructure (reliable digital payment
rails, enforceable e-contracts) that the firm does not control. A firm with high TCI
benefits regardless of whether digital payment systems are reliable; a firm with high DAI
benefits primarily when the surrounding digital ecosystem can support the transactional
chain from discovery to payment. Formally: TCI shifts the *turning point*, while DAI
shifts the *slope before the turning point* — and does so only where institutional quality
supports the digital transaction chain. This dual differentiation — construct-level and
mechanism-level — justifies testing H2 and H3 as separate hypotheses with potentially
distinct results across ICRV regimes.

#### 2.X.2 Empirical Evidence

**Paragraph 4 — Positive evidence for digital adoption–export performance link:**

A growing empirical literature supports the premise that digital adoption amplifies export
performance, particularly for small and medium-sized firms (SMEs) in developing economies.
Stallkamp and Schotter (2021) find that digital platform engagement reduces the psychic
distance penalty for cross-border sales, enabling firms from institutionally distant
markets to access Advanced-regime buyers more effectively. Verhoef et al. (2021) document
that digital transformation capabilities generate performance premiums that are
particularly pronounced in firms with high foreign-sales exposure, consistent with the
market-interface mechanism above. Banalieva and Dhanaraj (2019) theorise that digital
globalisation capabilities are a new source of internationalisation-specific advantage that
supplements Dunning's (1988) OLI ownership advantages. At the country level, Hashem et al.
(2022) and Meijers (2014) show that national ICT development positively moderates the
aggregate export-productivity relationship, although these studies operate at the macro
level and do not identify firm-level mechanisms. In the WBES firm-level context, Atiase et al.
(2021) find that website adoption among African SMEs is positively associated with export
market access, and Awiagah et al. (2016) report that digital adoption — even at the
website-presence level — significantly predicts revenue growth among Ghanaian SMEs,
particularly those engaged in cross-border trade.

**Paragraph 5 — Inconsistencies and the ICRV explanation:**

The evidence is not uniformly positive. Several studies report null or negative digital
adoption effects in frontier institutional contexts. Diaz Andrade and Urquhart (2012) find
that ICT adoption in developing countries often fails to translate into productivity gains
due to complementary infrastructure gaps. Dewan and Kraemer (2000) show that ICT returns
differ fundamentally between developed and developing countries, with the latter displaying
near-zero returns — consistent with weak institutional complementarity rather than weak
digital capability per se. In the WBES context specifically, Cirera et al. (2021) document
that digital adoption impacts on firm performance are heterogeneous across firm size, sector,
and country income group, with the strongest effects concentrated in upper-middle and
high-income countries. These null results in low-income and frontier contexts support the
ICRV conditioning mechanism: DAI generates performance returns *when the institutional
environment completes the digital transaction chain*, not universally. Taken together,
this literature identifies institutional context as the critical boundary condition that
determines whether digital adoption amplifies or fails to amplify export-performance
returns — precisely the condition captured by ICRV.

#### 2.X.3 Contextual Consideration

**Paragraph 6 — Why Asia-Pacific ICRV diversity provides the right test:**

The Asia-Pacific WBES sample examined in this dissertation offers an analytically ideal
test bed for context-contingent DAI moderation. The 47 economies span the full ICRV
spectrum — from Singapore's world-class digital infrastructure (Global Connectivity Index
rank 1, ITU 2024) to frontier economies with less than 20% broadband penetration and
fragmented e-payment regulation. This institutional heterogeneity is far greater than
that available in single-region studies focusing on Western Europe or North America, where
ICRV variation is compressed into the Advanced-innovation range. Moreover, the Asia-Pacific
context is characterised by rapid but uneven DPL (Digital Platform and Legislation) phase
transitions: Korea and Singapore completed phase 3 (mature e-commerce infrastructure) by
2015; Vietnam and India are transitioning through phase 2 (expanding digital access) in
the 2023 wave; Cambodia, Nepal, and Pacific SIDS remain in phase 1 (basic connectivity
expansion). This temporal and cross-sectional variation allows the CDCM framework to be
tested not just as a static cross-sectional comparison but as a prediction about *when*
within each economy's development trajectory the DAI moderating effect should emerge —
generating testable predictions that go beyond "digital is good" to "digital is good under
these specific institutional conditions and at this specific DPL phase."

#### Hypothesis Statement

> **H3 (CDCM):** Digital adoption (DAI) moderates the relationship between export
> intensity (FSTS) and labour productivity in a context-contingent manner: specifically,
> the DAI × FSTS interaction is positive and significant in Advanced Innovation-Driven
> institutional regimes (ICRV Group I), where digital infrastructure is complete and
> digital-transaction regulations are credible, and is attenuated toward zero or absent
> in Emerging and Frontier regimes (ICRV Groups IV–V), where institutional
> complementarity for digital-export transactions is incomplete.

---

### Operationalization of H3 in Regression Models

**Empirical specification (M8 in P4; M6 in P3/P5):**

```
lnLP = β₀ + β₁ FSTSc + β₂ FSTSc² + β₃ TCI_z + β₄ DAI_z
     + β₅ (FSTSc × TCI_z) + β₆ (FSTSc × DAI_z)
     + β₇ lnEmp + β₈ firmage + β₉ foreignown
     + country FE + year FE + ε
```

**H3 identification**: β₆ is the coefficient of primary interest. Predicted sign:
- P4 Singapore (ICRV I): β₆ > 0 (positive amplification)
- P3 Vietnam 2009/2015 (ICRV IV, DPL phase 1): β₆ ≈ 0 (institutional incompleteness)
- P3 Vietnam 2023 (ICRV IV, DPL phase 2): β₆ > 0 or weakly positive (partial transition)
- P5 China (ICRV III): β₆ ambiguous — Upper-Middle transition regime, provincial variation

**H3 ≠ H2 test**: If β₅ (TCI × FSTS, H2) and β₆ (DAI × FSTS, H3) differ in sign or
magnitude across ICRV regimes, this confirms that TCI and DAI operate through distinct
mechanisms. Paternoster et al. (1998) z-test: z = (β₆_P4 − β₆_P3) / √(SE₆_P4² + SE₆_P3²).
A significant z confirms the ICRV regime gradient in DAI moderation.

**Key references for H3:**

- Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy.
  *Journal of International Business Studies, 50*(8), 1372–1387.
- Cirera, X., et al. (2021). Catching up to the technological frontier? Panel evidence from
  the firm-level impacts of digital adoption in developing countries. *World Bank Policy
  Research Working Paper 9696.*
- Dewan, S., & Kraemer, K. L. (2000). Information technology and productivity: Evidence
  from country-level data. *Management Science, 46*(4), 548–562.
- North, D. C. (1990). *Institutions, institutional change and economic performance.*
  Cambridge University Press.
- Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international
  strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80.
- Verhoef, P. C., et al. (2021). Digital transformation: A multidisciplinary reflection and
  research agenda. *Journal of Business Research, 122*, 889–901.
- Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of Management
  Journal, 38*(2), 341–363.

---

## Appendix — WBES Data Verification Note

**Pool status (as of May 2026):**

| File | Rows | Scope | Notes |
|------|------|-------|-------|
| `data_wbes/analysis/pooled_wbes_6waves.csv` | 8,589 | P3/P4/P5 countries only (Vietnam, Singapore, China) | Working dataset for empirical papers |
| `data_wbes/p7/p7_pooled_clean.csv` | 102,332 total; 91,982 non-panel | Full Asia-Pacific WBES scope (49 economies, 102 country-waves) | P7 / CD1 / CD2 full pool |

**Discrepancy note**: CD1/CD2 manuscripts cite "101,185 firms · 108 country-year pairs ·
14 survey waves · 47 economies." The current `p7_pooled_clean.csv` has 91,982 non-panel
firms across 49 economies and 102 country-waves. This discrepancy reflects data updates
since the CD manuscripts were drafted. When CD1/CD2 are submitted for defence, the pool
statistics should be re-verified against the final locked P7 dataset.
