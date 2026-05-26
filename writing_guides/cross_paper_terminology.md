# Cross-Paper Terminology Harmonization Guide
**Papers P3 (Vietnam), P4 (Singapore), P5 (China), P6 (Meta-analysis), P7 (Asian Capstone), P8 (Pacific SIDS)**
**Thesis: Internationalization, Digital Capability, and Firm Performance in Asia**

---

## 1. Internationalization Intensity — FSTS

| Item | Standard |
|------|----------|
| **Full term** | Foreign Sales to Total Sales ratio |
| **Abbreviation** | FSTS |
| **Scale** | 0–1 (decimal, not percentage) |
| **First mention** | "export intensity (Foreign Sales to Total Sales — FSTS)" |
| **Subsequent** | "FSTS" |
| **Centred form** | FSTSc = FSTS − wave mean (used in quadratic specifications) |
| **Squared form** | FSTSsq (raw) or FSTSc² (centred, preferred) |
| **Vietnamese** | cường độ quốc tế hóa (FSTS) |

**Do NOT use**: "degree of internationalization (DOI)" as a synonym for FSTS. DOI is a broader construct (Ramaswamy et al., 1996); FSTS is the specific intensity measure used across P3–P5.

---

## 2. Digital Adoption Index — DAI

| Tier | Papers using | Variable | Items |
|------|-------------|----------|-------|
| **Tier-1 (thin)** | P3 all waves, P5 | `DAIthin` | Website presence only (WBES c22b) |
| **Tier-1+2 (composite)** | P4 Singapore 2023 | `DAIfull` | Website (c22b) + e-payment (k33/k38) |
| **Tier-2 only** | P4 (supplementary) | `DAItier2` | E-payment acceptance (k33/k38) |

**Rationale for tier differences:**
- 2009 and 2015 WBES surveys only include website (c22b) — Tier-1 is a **deliberate data boundary**, not a theoretical omission.
- 2023 BREADY module adds e-payment variables — P4 and P5 2023 can construct Tier-1+2.
- The term "DAI Tier-1 only" signals a measurement constraint; "DAIthin" is the Stata variable name.

**Standardization:** All DAI measures are z-standardized within sample before regression. Reported as `DAI_z` in models.

**Full term:** Digital Adoption Index (DAI)
**Vietnamese:** Chỉ số áp dụng kỹ thuật số (DAI)
**First mention:** "digital adoption (Digital Adoption Index — DAI)"
**Subsequent:** "DAI" or "mức độ áp dụng kỹ thuật số"

---

## 3. Technological Capability Index — TCI

| Paper | Items | Construction |
|-------|-------|-------------|
| **P3 Vietnam 2009/2015** | b8 (quality cert), e6 (foreign tech license) | z-each → rowmean → re-standardize |
| **P3 Vietnam 2023** | b8, e6 + h8 (imported machinery), h1 (ISO) | z-each → rowmean → re-standardize |
| **P4 Singapore 2023** | b8, e6 + h8, h1 (where available) | Same construction as P3-2023 |
| **P5 China** | b8, e6 | z-each → rowmean → re-standardize |

**Why different items?** The 2023 BREADY survey module added h1 and h8. Using more items in 2023 improves construct validity; the P3 comparison across waves is controlled by noting this difference in §3.2.

**Standardization:** TCI composite is z-standardized within sample. Reported as `TCI_z` (or `TCIfull` in raw form, then re-standardized in model prep).

**Full term:** Technological Capability Index (TCI)
**Vietnamese:** Chỉ số năng lực công nghệ (TCI)
**First mention:** "technological capability (Technological Capability Index — TCI)"
**Subsequent:** "TCI" or "năng lực công nghệ"

---

## 4. Margin Terminology

The thesis distinguishes three export participation concepts:

| Term | Definition | Where used |
|------|-----------|-----------|
| **Extensive margin** | Whether a firm exports at all (binary: exporter vs. non-exporter) | P3, P4, P5, P7, P8 (exporter dummy) |
| **Intensive margin** | How much a firm exports, among active exporters (FSTS level within exporters > 0) | P3, P4, P5, P7, P8 (FSTS conditional on export) |
| **Participation-margin effect** | The productivity premium from switching from non-exporter to exporter status — the jump at FSTS = 0 | P3 §4.5, CD2 §3.1 |
| **Forced internationalization penalty** | In SIDS, the NEGATIVE FSTS–LP slope: export engagement reduces productivity due to structural dependency on remittance/aid economies, thin domestic markets, and terms-of-trade vulnerability — not a strategic choice but a structural constraint. | P8 exclusively |

**Standard sentence form:**
> "The participation-margin effect — the productivity premium from entering export markets, as distinct from the intensive-margin gain from deepening export engagement among active exporters (Helpman, Melitz & Yeaple, 2004) — is captured by …"

**Do NOT interchange**: "participation margin" and "extensive margin" are related but distinct. Use "extensive margin" for the binary export decision; use "participation-margin effect" for the *productivity consequence* of that decision.

---

## 5. Outcome Variable

| Term | Definition |
|------|-----------|
| **Labour productivity (LP)** | Annual sales / number of full-time employees |
| **ln(LP)** | Natural log of LP (lnLP in Stata) |
| **Winsorize** | 1st–99th percentile within each wave, applied before any regression |

**Full term:** Labour Productivity (LP)
**Vietnamese:** Năng suất lao động (LP)
**Note:** Use "labour" (British/Australian spelling consistent with WBES documentation), not "labor."

---

## 6. ICRV Framework — Institutional Context Regime Variation

| Regime | CD2 Code (6-regime) | P3/P6 Code (5-regime) | P7 R code | Countries in thesis |
|--------|---------------------|----------------------|-----------|---------------------|
| Advanced Innovation-Driven | Nhóm I | Regime I | `Advanced_innovation` | Singapore (P4); Korea; Taiwan |
| Advanced Resource-Driven | Nhóm II | Regime II | `Advanced_resource` | Gulf states (Chuyên đề 1); Brunei |
| Upper-Middle | Nhóm III | Regime III | `Upper_mid` | China main sample (P5); Malaysia; Thailand |
| Lower-Middle Transition | Nhóm IV | Regime IV | `Lower_mid_transition` | **Vietnam (P3)**; Indonesia; India; Philippines; Bangladesh; Mongolia; Pakistan |
| Frontier (low-income) | Nhóm V | Regime V | `Emerging` | Afghanistan; Nepal; Cambodia; Laos; Myanmar; Bhutan; Jordan; Kyrgyz Rep.; etc. |
| SIDS | Nhóm VI | SIDS (separate) | `SIDS_small` | Pacific SIDS (P8): Fiji, Kiribati, Solomon Islands, Maldives |

**P7 pooled-sample sizes by ICRV group (finalized — JIBS under revision, N=82,302–98,658):**

| Group | N firms (approx) | FSTS–LP shape (within-group) |
|-------|---------|---------------|
| Advanced_innovation (Nhóm I) | ~3,400 | Inverted-U (shallow) |
| Advanced_resource (Nhóm II) | ~1,800 | Inverted-U |
| Upper_mid (Nhóm III) | ~8,500 | Flat / near-linear |
| Emerging / Lower_mid_transition (Nhóm IV) | ~45,500 | Inverted-U |
| Frontier (Nhóm V) | ~12,800 | Flat / near-linear |
| SIDS_small (Nhóm VI) | ~1,400 | **Monotone negative (FIP)** |

*Note: Under the final geographical-Asia scope (N=82,302, M2), the robust institutional-moderation result is the significant M10 interaction (FSTS×ICRV β=+1.85, FSTS²×ICRV β=−2.93, both p<.001): the inverted-U's **concavity deepens as institutional quality declines** — sharper in weaker-institution regimes, flatter/near-linear in advanced ones. Per-group turning points are heterogeneous (~16–50%) and do NOT form a clean monotonic 28%→55% gradient; the earlier peak-migration table is superseded. Sub-sample group estimates are noisy; the pooled interaction is the reliable inference. (M11 confirms the inverted-U at TP=25.7%, LM p=.026; DAI×ICRV p=.049.)*

**Full term:** Institutional Context Regime Variation (ICRV)
**Vietnamese:** Biến thể chế độ bối cảnh thể chế (ICRV)
**First mention:** "institutional context regime (Institutional Context Regime Variation — ICRV)"
**Subsequent:** "ICRV" or "bối cảnh thể chế"

**Two-system mapping note:** Vietnam = **Nhóm IV (Lower_mid_transition, Group 4)** in the dissertation's 6-regime ICRV classification, consistent across CD1, CD2, P7 data (`ICRV_MAP["Vietnam"] = 4`) and the data registry (Group IV — Lower-Middle Transition). P3 and P6 (5-regime, SIDS excluded) use the same numbering: groups 1–5 without group 6, so Vietnam remains **Regime IV** in the 5-regime context. The earlier label **"Frontier V" in P3 was incorrect** — it was based on an outdated reading of WGI Rule of Law scores and a miscount of the regime numbering. Vietnam WGI Rule of Law estimate (RL.EST scale, −2.5 to +2.5): approximately −0.55 to −0.68 in 2009 (early-wave low), improving to approximately −0.09 in 2023 (source: World Bank / tradingeconomics.com). The Nhóm V regime ("Emerging" in P7 R code) contains lower-governance economies: Afghanistan, Nepal, Cambodia, Laos, Myanmar, Bhutan, Jordan, Kyrgyz Republic, Tajikistan, Uzbekistan, Yemen, etc. Vietnam is **above** this threshold and correctly classified at Nhóm IV across all dissertation documents.

**Critical rule:** Every empirical paper must place its sample within an ICRV regime in §1 Introduction and §5 Discussion. Cross-references in CD2's 6-regime system: **P3→Nhóm IV** (`Lower_mid_transition`; Vietnam = Group 4 of 6), **P4→Nhóm I** (`Advanced_innovation`; Singapore), **P5→Nhóm III** (`Upper_mid`; China), **P7→all 6 groups (cross-regime)**, **P8→Nhóm VI** (`SIDS_small`). Note: "Frontier V" is NOT a valid dissertation-internal label for Vietnam; correct label is "Nhóm IV" or "ICRV Group 4 (Lower_mid_transition)".

**Institutional gradient in P7 results (key cross-paper narrative — CRITICAL direction):** The ICRV gradient is empirically confirmed in P7 — Advanced_innovation shows the **LOWEST** TP (~28%) while Frontier shows the **HIGHEST** TP (~55%). The gradient is monotone: as institutional quality decreases (Advanced → Frontier), the turning point increases. This means in stronger-institution contexts, firms reach performance peak at lower export intensity; in weaker-institution contexts, they need higher FSTS to overcome transaction costs before reaching peak performance. SIDS_small (Nhóm VI) is the exception: FIP (Forced Internationalization Penalty) — monotone negative, no turning point. DAI×ICRV (p=.012): digital adoption delivers stronger per-unit returns in weaker institutional environments ("digital shield").

---

## 7. CDCM Framework

**Full term:** Context-Contingent Digital-and-Capability Model (CDCM)
**Vietnamese:** Mô hình kỹ thuật số và năng lực có điều kiện theo bối cảnh (CDCM)
**First mention:** "digital-and-capability model (Context-Contingent Digital-and-Capability Model — CDCM)"
**Subsequent:** "CDCM"

The CDCM is the theoretical framework developed in Chuyên đề 2 and tested empirically across P3–P5. It has two distinct pillars:
- **"Digital"** = DAI adoption dimension (foundational digital presence — Tier-1/Tier-2 only; **not** dynamic digital capability)
- **"Capability"** = TCI process-competence dimension (foreign-technology and standards capability)

> **Critical naming rule:** Do NOT write "digital capability model" as if DAI represents a capability construct. WBES DAI items (c22b website, k33/k38 e-payment) are binary adoption/presence measures — Tier 1–2 in the Verhoef et al. (2021) hierarchy. DAI cannot support dynamic-capability or reconfiguration-capability framing. Always write "digital *adoption*" when referring to the DAI dimension.

The CDCM posits that TCI's moderating effect on the FSTS–performance inverted-U is the primary capability mechanism, while DAI's role is conditional on ICRV regime and wave (proxy obsolescence in early waves; baseline adoption signal in 2023).

---

## 7b. P7/P8 Specific Terminology

### Forced Internationalization Penalty (P8)

**Full term:** Forced Internationalization Penalty (FIP)
**Vietnamese:** gánh nặng quốc tế hóa bắt buộc (FIP)
**Definition:** In Pacific SIDS economies, export engagement (FSTS > 0) is associated with *lower* labour productivity — β(FSTS_c) = −0.404 (p = .032, country+year FE, HC1 SE, N = 1,469). This is not a strategic performance trap (as in the classic overextension hypothesis) but a **structural constraint**: SIDS firms export under compulsion from thin domestic markets and dependence on remittance/aid economies, without the organisational capabilities to convert export exposure into productivity gains. Defined formally as "the monotone negative effect of internationalization intensity on firm performance in contexts where three structural prerequisites are simultaneously absent: (1) a viable domestic market, (2) manageable trade costs, and (3) functional institutional support for international market access."

**Standard sentence form:**
> "The Forced Internationalization Penalty (gánh nặng quốc tế hóa bắt buộc) — a monotone negative FSTS–labour productivity relationship observed among Pacific SIDS firms — reflects structural dependence on export revenue in resource-scarce, aid-dependent economies (β = −0.404, p = .032, M1 country+year FE), as distinct from the inverted-U overextension threshold documented for larger continental economies."

**Do NOT conflate** with: the downward arm of the inverted-U in continental economies. That arm still shows positive-then-declining LP (turning point clustering near ~40% FSTS; the concavity is sharper in weaker-institution regimes and flatter, even near-linear, in advanced ones); the SIDS penalty shows a negative slope from FSTS = 0.

### Asian Capstone Turning Points (P7)

Key empirical anchors (N = 82,302–98,658 firms, 45 economies, 98 country-year waves):

| Model | Turning Point | Notes |
|-------|--------------|-------|
| M2 (baseline) | **37.1% FSTS** | LM p < .001 |
| M5 (controls + country-year FE) | **39.5% FSTS** | adjR² = .671 |
| M11 (full three-way moderation) | **25.7% FSTS** | LM p = .026; DAI×ICRV p = .049 |
| ICRV moderation (M10) | concavity deepens as institutions weaken | FSTS×ICRV β=+1.85, FSTS²×ICRV β=−2.93 (both p<.001); per-group turning points cluster ~40%, no clean monotonic gradient |
| P8 Pacific SIDS | monotone negative | No TP — FIP confirmed |

**When citing P7 turning points**, always specify which model and whether country FE is included. The no-FE turning point (M2: 8.1%) is spurious and should not be reported in isolation.

### DAI Moderation Joint F-Test (P7)

The DAI moderation test in P7 uses a **joint F-test** for two interaction terms simultaneously:
- `fsts_c × DAI_z` (linear × digital): β = −0.614 (p < .001) — compresses ascending limb
- `fsts_c² × DAI_z` (quadratic × digital): β = +0.766 (p < .01) — amplifies at high FSTS

Result: F(2, 36132) = 7.38, p = .0006***

**DAI level effect (universal):** β = +0.155 (p < .001) — DAI raises the performance floor across all ICRV regimes.

**DAI×ICRV institutional contingency:** p = .012 — DAI's moderating effect is **stronger in weak-institution contexts** (Frontier/SIDS), not only in Advanced. This is the "digital shield" mechanism: DAI compensates for institutional deficiencies rather than amplifying existing advantages. Do NOT write "DAI only significant in Advanced contexts."

**Interpretation:** DAI is a *situational resource*: the level effect is universal; the moderating mechanism (compression vs amplification of the I→P curve) depends on ICRV regime. This is analytically distinct from TCI (foundational capability with universal level + curvature effects).

**Standard sentence form:**
> "A joint F-test of the two DAI interaction terms (linear and quadratic) confirms that digital adoption significantly moderates the FSTS–labour productivity curve (F = 7.38, p < .001), consistent with digital capability theory (Stallkamp & Schotter, 2021)."

---

## 8. Statistical Terms Consistency

| Concept | Preferred term | Avoid |
|---------|---------------|-------|
| Regression coefficient | β (or b in tables) | "effect size" (ambiguous with meta-analysis) |
| Standard error | SE or se | "std err" |
| Turning point (M2) | TP | "optimal level", "optimal point" |
| Quadratic term | FSTSsq or FSTSc² | "FSTS^2", "squared FSTS" |
| Inverted-U relationship | inverted-U (hyphen) | "inverted U" (no hyphen), "∩-shaped" |
| Test for interior maximum | Lind–Mehlum utest | "utest", "fieller method" |
| Cross-wave stability test | Paternoster z-test | "Paternoster test" (without "z") |
| Robustness | robustness check | "sensitivity analysis" (reserved for sample/model changes) |
| Cluster-robust SE | cluster(idstd) SE | "clustered SE" (specify cluster variable) |

---

## 9. Citation Consistency for Core Methodology

| Method | Canonical citation |
|--------|--------------------|
| Inverted-U theory | Lu & Beamish (2001, 2004); Hitt et al. (1997) |
| Lind–Mehlum utest | Lind & Mehlum (2010, Oxford Bulletin) |
| Paternoster z-test | Paternoster et al. (1998, Criminology) |
| Heckman two-step | Heckman (1979, Econometrica) |
| Three-level MARA | Cheung & Chan (2005); Raudenbush & Bryk (2002) |
| Participation margin | Helpman, Melitz & Yeaple (2004, AER) |
| RBV | Barney (1991, JoM); Wernerfelt (1984, SMJ) |
| Digital platform mechanism | Stallkamp & Schotter (2021, JIBS) |
| Power for interactions | Leon (2004) |

---

## 10. Variable Name Cross-Reference Table

| Concept | Stata name | Python/R name (p7/p8 CSV) | Paper(s) |
|---------|-----------|--------------------------|---------|
| Labour productivity (log) | lnLP | ln_labor_prod | P3, P4, P5, P7, P8 |
| Export intensity | FSTS | fsts | P3, P4, P5, P7, P8 |
| FSTS centred | FSTSc | fsts_c | P3, P4, P5, P7, P8 |
| FSTS squared (centred) | FSTSc2 | fsts_c2 | P3, P4, P5, P7, P8 |
| TCI composite | TCIfull | tci_z | P3, P4, P5, P7, P8 |
| DAI Tier-1 | DAIthin | dai_z | P3, P4, P5, P7, P8 |
| DAI Tier-1+2 | DAIfull | dai_full_z | P4 |
| Firm size (log) | lnEmp | ln_emp | P3, P4, P5, P7, P8 |
| Firm age | firmage | firmage | P3, P4, P5, P7, P8 |
| Foreign ownership | foreigndummy | foreign_own | P3, P4, P5, P7, P8 |
| ICRV regime group | icrv_group | icrv_group | P7, P8 |
| Country identifier | idstd | country | P7, P8 |
| Survey wave year | wave | year | P3, P5, P7, P8 |
| Exporter dummy | exportdummy | exporter | P3, P4, P5, P7, P8 |
| Analytic sample flag | analytic | analytic | P3, P4, P5 |
| Full-sample flag | full_samp | full_samp | P3, P4, P5 |
| SIDS indicator | sids | sids_small | P7, P8 |

**Key difference:** P7/P8 data uses `p7_pooled_clean.csv` column names (lowercase, underscores). P3/P5 Stata do-files use camelCase variable names. The Python merge script (`scripts/merge_wbes_dta.py`) maps WBES raw variables to the CSV column names; consult that script for full mapping.

---

---

## 11. Dissertation-Wide Empirical Summary (Preliminary R Results)

For use in thesis integration chapter and §6 Discussion cross-referencing:

| Paper | Context | TP / Key β | Direction | Confirmed |
|-------|---------|-----------|-----------|-----------|
| P3 Vietnam | Frontier IV (3 waves) | TP ≈ 34.5% (R); 39.7% (Stata) | Inverted-U | ✓ |
| P4 Singapore | Advanced I | TP ≈ 76–89% (wide CI) | Predominantly positive | ✓ saturation |
| P5 China | Upper-mid III (2 waves) | TP ≈ 47.5% | Inverted-U | ✓ Paternoster p=.831 |
| P6 Meta-analysis | All regimes (k=238) | r = 0.074, I² = 62.4%, Q_M=17.35 (df=4, p=.002) | Positive mean | ✓ ICRV Q-mod |
| P7 Capstone | 45 economies (6 ICRV) | TP ≈ **36%** (M2–M5: 36.4–40.0%; M11 full: TP=25.7%, LM p=.026, N=28,500); N=82,302–98,658 | Inverted-U | ✓ ICRV Q-mod; DAI×ICRV p=.049 |
| P8 Pacific SIDS | Nhóm VI | β(FSTS_c) = −0.404 (p=.032, country+year FE, N=1,469) | **NEGATIVE (FIP)** | ✓ Penalty |

**ICRV subgroup TPs (P7 finalized — JIBS under revision):**

| ICRV Group | TP | Shape | Notes |
|-----------|-----|-------|-------|
| Advanced Innovation (Nhóm I) | **~28%** | Inverted-U | Singapore, HK, Korea, Taiwan — TP lowest |
| Advanced Resource / Upper-mid (Nhóm II–III) | ~35–42% | Inverted-U | China, Malaysia, Thailand, Kazakhstan... |
| Emerging / Lower-mid (Nhóm IV) | ~44–50% | Inverted-U | India, Vietnam, Indonesia, Philippines... |
| Frontier (Nhóm V) | **~50–55%** | Inverted-U | Afghanistan, Nepal, Cambodia, Bhutan... |
| Pacific SIDS (Nhóm VI) | No TP | **Negative (FIP)** | β(FSTS_c)=−0.404* — monotone penalty |

**ICRV gradient direction (CRITICAL):** TP **DECREASES** as institutional quality increases. Advanced Innovation (~28%) has the LOWEST TP; Frontier/SIDS (~55%) has the HIGHEST. This means stronger institutions → firms reach performance optimum at lower export intensity. Weaker institutions → firms need higher FSTS before costs exceed benefits. Do NOT write "threshold increases with institutional development."

**Cross-paper narrative:** Results demonstrate an ICRV-contingent internationalization–performance gradient. The inverted-U is universal across non-SIDS regimes, but the turning point **decreases** with institutional quality: Frontier ~50–55%, Emerging ~44–50%, Advanced Innovation ~28%. DAI×ICRV (p=.012) confirms the "digital shield" compensatory mechanism — DAI delivers **stronger** per-unit returns in weaker institutional environments. Pacific SIDS (Nhóm VI) constitute a structural exception (Forced Internationalization Penalty), not overextension.

---

*Last updated: May 2026. For discrepancies between this guide and individual paper §3 sections, the individual paper takes precedence — but update this guide accordingly.*
