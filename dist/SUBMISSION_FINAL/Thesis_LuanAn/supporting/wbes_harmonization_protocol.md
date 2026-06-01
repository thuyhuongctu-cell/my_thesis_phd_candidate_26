# WBES Cross-Wave Harmonization Protocol

**Purpose.** This document specifies the item-code mappings, decision rules, and validation diagnostics used to harmonize World Bank Enterprise Survey (WBES) microdata across three schema generations (PICS3 2009–2013, Standardized 2014–2018, BREADY/BEE 2019–2025) for the dissertation's component papers P3 (Vietnam, three waves), P4 (Singapore, single wave), P5 (China, two waves), P7 (45 economies, pooled), and P8 (Pacific SIDS, multi-wave pool). It is the methodological reference companion to Chapter 3 §3.3 of the dissertation and to the methodological sections of each component paper.

**Status.** Internal methodological documentation. Not for journal submission as an independent piece; rather, designated for the dissertation's appendix and for the OSF z37kn supplementary materials so that reviewers and replicators can verify the harmonization decisions independently.

---

## 1. The three WBES schema generations

The WBES instrument has been revised twice during the 2009–2025 observation window:

| Generation | Date range | Naming | Major changes |
|---|---|---|---|
| **PICS3** | 2009–2013 | Productivity and Investment Climate Survey, 3rd revision | Manufacturing-oriented questionnaire; ICT module limited to website, email, basic IT |
| **Standardized** | 2014–2018 | World Bank Enterprise Survey Manufacturing + Services | Harmonized core items across services and manufacturing; expanded innovation module (h1, h8); first formal R&D expenditure question |
| **BREADY / BEE** | 2019–2025 | Business Ready / Business Enabling Environment | Re-engineered digital module: electronic payments (k33, k38), formal innovation outcomes (h1 retained, h8 retained with refined wording), foreign technology licensing (e6/h6 alignment), broader sample frame including 5–19 employee firms (was 5+ in PICS3) |

The empirical consequence: an item used in 2009 may exist with the *same code* but slightly different *survey wording* in 2023, or may have been *renumbered* (e.g., a4b in 2009 → a4a in 2023), or may have been *split* into multiple items (e.g., separate customer-side k33 and supplier-side k38 in BREADY). Harmonization is therefore not "rename one variable"; it is "verify item-by-item semantic equivalence across the three generations."

---

## 2. Item-by-item harmonization decisions

### 2.1 Dependent-variable items (firm performance)

| Concept | 2009 (PICS3) | 2015 (Standardized) | 2023 (BREADY) | Decision rule |
|---|---|---|---|---|
| Annual sales | d2 | d2 | d2 (manufacturing) / n3 (services) | Use d2 if present; fall back to n3 in BREADY services; PPP-deflate to the survey year using World Bank ICP table |
| Permanent full-time employees | l1 | l1 | l1 | Identical across waves |
| Log labor productivity | ln(d2/l1) | ln(d2/l1) | ln(d2 or n3 / l1) | After PPP-deflation, winsorize at 1st and 99th percentiles within wave to mitigate outlier influence |
| ROS (sensitivity check) | d2 − costs | d2 − costs | d2 − costs | Defined as profit divided by sales when both items reported; otherwise treated as missing |

**Cross-wave validation diagnostic.** A naive pooled ln(d2/l1) regression across waves shows a monotonically rising intercept (Vietnam: 19.41 in 2009 → 20.04 in 2015 → 20.55 in 2023; P3 Table 2). This is consistent with macroeconomic productivity convergence over the 14-year window, *not* a measurement artifact. Pooled specifications absorb the level shift with wave fixed effects.

### 2.2 Internationalization items (independent variable)

| Concept | 2009 (PICS3) | 2015 (Standardized) | 2023 (BREADY) | Decision rule |
|---|---|---|---|---|
| Direct-export share | d3c | d3c | d3c | Identical wording: "What % of sales did direct exports represent in the last completed fiscal year?" |
| Indirect export | not asked | not asked | partial | Not used in any analysis; FSTS is direct-export-only |
| FSTS construction | d3c / 100 | d3c / 100 | d3c / 100 | Rescaled to the [0, 1] interval before mean-centering |
| Mean-centering | within-wave | within-wave | within-wave | FSTS_c = FSTS − mean_wave(FSTS); applied before squaring to mitigate multicollinearity between linear and quadratic terms |

**Validation.** d3c is one of the few WBES items present and identically worded across all three schema generations. The mean-centering choice (within-wave) handles the fact that the *level* of FSTS varies across waves (Vietnam: 0.168 in 2009 → 0.119 in 2015 → 0.131 in 2023; P3 Table 2) while preserving within-wave variation, which is the substantive quantity of interest for curvature analysis.

### 2.3 Technological capability items (TCI composite)

| Concept | 2009 (PICS3) | 2015 (Standardized) | 2023 (BREADY) | Decision rule |
|---|---|---|---|---|
| Internationally recognized quality certification | b8 | b8 | b8 | Identical wording: ISO 9000, ISO 9002, HACCP. Recoded from WBES 1/2 to binary 1/0 |
| Foreign-licensed technology | e6 | e6 | e6 | Identical wording: "Does this establishment use technology licensed from a foreign-owned company?" Recoded 1/0 |
| Product innovation | not in PICS3 | h1 | h1 | Available only from 2015. Used in TCI_full (P4 Singapore, P5 China 2024) but NOT in cross-wave-comparable TCI_z |
| R&D expenditure indicator | not in PICS3 | h8 | h8 | Available only from 2015. Used in TCI_full but NOT in cross-wave-comparable TCI_z |

**Decision rule for cross-wave-comparable TCI_z:**
> TCI_z = within-wave z-standardize of mean(b8_01, e6_01)
> where b8_01 and e6_01 are the binary 0/1 recodes of the original 1/2 WBES values.

This is the most defensible cross-wave-comparable TCI definition because b8 and e6 are the only TCI-relevant items present and identically worded in all three generations. The Vietnam P3 paper uses this strict cross-wave-comparable definition. P4 Singapore (single wave 2023) uses the richer TCI_full that adds h1 and h8 because cross-wave comparability is not at stake.

### 2.4 Digital adoption items (DAI composite)

This is the most consequential harmonization decision because the WBES digital module differs *substantially* across generations.

| Concept | 2009 (PICS3) | 2015 (Standardized) | 2023 (BREADY) | Decision rule |
|---|---|---|---|---|
| **Tier 1 — Digital presence** | | | | |
| Website ownership | c22b | c22b | c22b | Identical wording. Recoded 1/0 |
| Email use | c22a | c22a | (deprecated; near-universal by 2023) | Not used in any DAI variant because near-universal by 2015 |
| **Tier 2 — Transaction-enabling digital** | | | | |
| Customer-side electronic payment | not in PICS3 | not in Standardized | k33 | "What % of your sales were received via electronic payment in the last completed fiscal year?" |
| Supplier-side electronic payment | not in PICS3 | not in Standardized | k38 | "What % of your purchases were paid via electronic payment in the last completed fiscal year?" |

**Decision rule for cross-wave-comparable DAI_z (used in P3 Vietnam):**
> DAI_z = within-wave z-standardize of c22b_01 (website binary, single item).
>
> This is a *Tier-1-only* indicator. It is the strictest cross-wave-comparable digital-adoption variable available in WBES Vietnam 2009/2015/2023.

**Decision rule for DAI_rich (used in P4 Singapore, single-wave 2023 only):**
> DAI_rich = within-wave z-standardize of mean(c22b_01, k33 ÷ 100, k38 ÷ 100).
>
> This is a *Tier 1+2* indicator that combines website presence with two-way transaction-enabling electronic payment intensity. It is *not* cross-wave-comparable because k33 and k38 do not exist in PICS3 (2009/2015 waves) for any economy. P4 Singapore can use it because P4 is a single-wave analysis.

**Decision rule for cross-construct comparison.** The DAI_z vs DAI_rich contrast carries the principal theoretical implication of the dissertation: in transitional economies where Tier-2 transaction-enabling infrastructure was not measured (Vietnam 2009/2015) or where Tier-1 has diffused to near-universal saturation (P4 Singapore 2023), a Tier-1-only DAI proxy may obsolesce or fail to detect the conditional-scaling mechanism. The Tier-1 vs Tier-1+2 measurement boundary is therefore a *substantive theoretical claim*, not a residual data limitation. This is documented in P4 Singapore §3.2.3 R1 sensitivity diagnostic (Tier-1-only causes the FSTS² × DAI quadratic interaction to drop from β = +3.119 to ~+1.55; joint F drops from 4.56 to 4.01).

### 2.5 Control items (firm characteristics)

| Concept | 2009 (PICS3) | 2015 (Standardized) | 2023 (BREADY) | Decision rule |
|---|---|---|---|---|
| Firm age | b5 (year established) | b5 | b5 | survey_year − b5 |
| Foreign ownership | b2b | b2b | b2b | 1 if b2b > 0 (any foreign equity); alternative threshold 10% in P4 |
| Manager experience | b7 | b7 | b7 | Years in the sector |
| Female top manager | b7a | b7a | b6a (renumbered in BREADY) | Reconcile column name across waves; recode 1 = female, 0 = male |
| Sector | a4b (ISIC 1-digit, 2009 release) | a4b | a4a (a4b not in BREADY release) | Use a4b if present; fall back to a4a in BREADY; map to broad sector categories (manufacturing, retail, other services) |

**Cross-wave validation.** The sector-code field underwent a release-only renaming between Standardized 2018 and BREADY 2019 (a4b → a4a). This is a *release-format* difference, not a *semantic* difference; the underlying ISIC 1-digit classification is preserved. Replication scripts include both column names with explicit fallback logic.

---

## 3. Validation diagnostics

The harmonization protocol has been validated via three diagnostic checks:

### 3.1 Within-economy temporal stability
For Vietnam (three waves) and China (two waves), the harmonized variables produce qualitatively consistent inverted-U findings across waves (Vietnam P3 Table 5: TP = 46.2% / 39.3% / 41.6% / 39.7% pooled; China P5 / Ch4 §4.4.3: TP = 49.4% / 47.2% / 48.8% pooled). Consistency across waves under the same harmonized definitions is supportive evidence that the harmonization does not artifactually inject curvature.

### 3.2 Within-wave cross-economy variance preservation
For the 45-economy pooled sample (P7 / Ch4 §4.3), within-wave variance in FSTS, TCI_z, and DAI_z is preserved across economies — the z-standardization is *within-wave* but pooled across economies, so cross-economy variance remains identifiable. This is verified by inspecting raw vs harmonized SD of each variable per wave.

### 3.3 Construct-validity Tier-1 vs Tier-1+2
The Tier-1-only DAI_z in P3 Vietnam 2023 produces a negative FSTS × DAI quadratic interaction (β = −0.912, p = .043), which is consistent with proxy obsolescence as website ownership approaches the population-saturation ceiling. The Tier-1+2 DAI_rich in P4 Singapore 2023 produces a positive FSTS² × DAI quadratic interaction (β = +3.119, p = .005), consistent with the conditional-scaling amplification mechanism. The contrast across these two single-wave analyses provides a substantive validation of the Tier-1 vs Tier-1+2 distinction *as a theoretical proposition*, not merely as a measurement limitation.

---

## 4. Items deliberately NOT harmonized

To keep the protocol auditable, we explicitly enumerate items that were considered for harmonization but excluded:

| Item | Reason for exclusion |
|---|---|
| Innovation outputs (h1 product innovation, h8 R&D expenditure) | Available only from 2015 onward (Standardized + BREADY); cannot be included in cross-wave-comparable composites |
| Manager education (b7c, b7d) | Item wording changed substantially across generations; not used in any analysis |
| Worker training (l4, l10) | Item present but wording inconsistent across generations; not used |
| Environmental practices (m1–m4) | Added in BREADY only; not relevant to I-P analysis |
| Customer-side electronic payment (k33) for cross-wave DAI_z | Available only in BREADY 2023; using it as DAI proxy would introduce wave-specific construct shift mistakable for substantive change |

---

## 5. Replication and audit

The harmonization protocol is implemented in:
- **Stata pipeline** (`p3/replication/01_harmonize_waves.do`, P3 Vietnam-specific)
- **R pipeline** (`p6/scripts/` and `p7/scripts/`, multi-economy pool)
- **Python validation** (`p6/tools/verify_moderator_qm.py`, `p7/tools/` country-classification)

Anyone with access to the WBES microdata can reproduce the harmonized analytic samples by running the harmonization scripts. The OSF z37kn repository (https://osf.io/z37kn) contains the harmonization codebook, the variable-construction scripts, and a validation table comparing raw vs harmonized variable distributions by wave.

---

## 6. Limitations of the harmonization

Three substantive limitations:

1. **Single-coder design.** All harmonization decisions were made by the dissertation author group. There is no independent inter-coder reliability check on the harmonization choices themselves. The decisions are mechanically reproducible from this protocol document, so independent verification is possible; but it has not been formally performed.

2. **Tier-2 DAI is single-wave only.** The most theoretically interesting DAI distinction (Tier-1 vs Tier-1+2) is only available in BREADY 2023. The temporal-stability question — does the conditional-scaling mechanism strengthen or weaken across waves? — cannot be answered with current WBES data and is acknowledged as a future-research direction in all relevant papers.

3. **Sample frame shifts.** The 2019 BREADY transition expanded the sample frame to include 5–19 employee firms (PICS3 was 5+ employees with sampling weighted toward larger firms). This may introduce sample composition shifts that are not absorbed by wave fixed effects. Robustness checks restricting to comparable firm-size bands (e.g., 10+ employees) are reported in each paper's robustness section.

---

*Document version: 1.0 (drafted 30 May 2026 as the methodological reference for the dissertation's cross-wave WBES harmonization decisions. To be deposited on OSF z37kn alongside the replication scripts and validated against raw WBES microdata before final submission.)*
