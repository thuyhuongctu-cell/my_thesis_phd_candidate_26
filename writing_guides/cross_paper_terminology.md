# Cross-Paper Terminology Harmonization Guide
**Papers P3 (Vietnam), P4 (Singapore), P5 (China), P6 (Meta-analysis)**
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
| **Extensive margin** | Whether a firm exports at all (binary: exporter vs. non-exporter) | P3, P4, P5 (exporter dummy) |
| **Intensive margin** | How much a firm exports, among active exporters (FSTS level within exporters > 0) | P3, P4, P5 (FSTS conditional on export) |
| **Participation-margin effect** | The productivity premium from switching from non-exporter to exporter status — the jump at FSTS = 0 | P3 §4.5, CD2 §3.1 |

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

| Regime | Code | Countries in thesis |
|--------|------|---------------------|
| Advanced Innovation-Driven | Nhóm I | Singapore (P4) |
| Advanced Resource-Driven | Nhóm II | Gulf SIDS (Chuyên đề 1) |
| Upper-Middle | Nhóm III | China upper tier |
| Emerging | Nhóm IV | China main sample (P5) |
| Frontier | Nhóm V | Vietnam (P3) |
| SIDS | Nhóm VI | Small Island Developing States (Chuyên đề 1) |

**Full term:** Institutional Context Regime Variation (ICRV)
**Vietnamese:** Biến thể chế độ bối cảnh thể chế (ICRV)
**First mention:** "institutional context regime (Institutional Context Regime Variation — ICRV)"
**Subsequent:** "ICRV" or "bối cảnh thể chế"

**Critical rule:** Every empirical paper must place its sample within an ICRV regime in §1 Introduction and §5 Discussion. Cross-references: P3→Nhóm V, P4→Nhóm I, P5→Nhóm IV.

---

## 7. CDCM Framework

**Full term:** Context-Contingent Digital Capability Model (CDCM)
**Vietnamese:** Mô hình năng lực kỹ thuật số có điều kiện theo bối cảnh (CDCM)
**First mention:** "digital capability model (Context-Contingent Digital Capability Model — CDCM)"
**Subsequent:** "CDCM"

The CDCM is the theoretical framework developed in Chuyên đề 2 and tested empirically across P3–P5. It posits that DAI's moderating effect on the FSTS–performance relationship is conditional on the ICRV regime.

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

| Concept | Stata name | Python/R name | Paper(s) |
|---------|-----------|--------------|---------|
| Labour productivity (log) | lnLP | lnLP | P3, P4, P5 |
| Export intensity | FSTS | FSTS | P3, P4, P5 |
| FSTS centred | FSTSc | FSTS_c | P3, P4, P5 |
| FSTS squared (centred) | FSTSc2 | FSTSsq_c | P3, P4, P5 |
| TCI composite | TCIfull | TCI_z | P3, P4, P5 |
| DAI Tier-1 | DAIthin | DAI_thin | P3, P4, P5 |
| DAI Tier-1+2 | DAIfull | DAI_full | P4 |
| Firm size (log) | lnEmp | lnEmp | P3, P4, P5 |
| Firm age | firmage | firmage | P3, P4, P5 |
| Foreign ownership | foreigndummy | foreign_dum | P3, P4, P5 |
| Survey wave year | wave | wave | P3, P5 |
| Analytic sample flag | analytic | analytic | P3, P4, P5 |
| Full-sample flag | full_samp | full_samp | P3, P4, P5 |

---

*Last updated: May 2026. For discrepancies between this guide and individual paper §3 sections, the individual paper takes precedence — but update this guide accordingly.*
