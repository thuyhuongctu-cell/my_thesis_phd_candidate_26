# OSF Pre-Registration: P6 Three-Level Meta-Analysis
# Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship

> **Registration type:** Systematic Review & Meta-Analysis (Secondary Data)  
> **Date prepared:** 2026-05-18  
> **Prepared by:** Đỗ Thùy Hương, Can Tho University, Vietnam  
> **OSF Registration ID:** https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN)  
> **Status:** REGISTERED — submitted 2026-05-18; registration active

---

> **⚠️ Alignment note (resolve before registering):** This template must be reconciled with the final manuscript before OSF submission. Known mismatches to fix:
> - **DPL** is here called "Digital Platform Lifecycle" with phases pre-2000 / 2000–2009 / 2010–2026, but the manuscript uses **"Digital Paradox Lifecycle"** with phases **Precede (<2009) / Span (2005–2014) / Follow (>2014)**. Use the manuscript definitions.
> - **ICRV** is here described as "6 regime groups"; the manuscript's H1 uses the **5-regime** scheme (I, II, III, FR, MX). Use the manuscript scheme.
> - Insert the **OSF project DOI/URL and registration date** once registered, and update the manuscript's Methods §3 accordingly.

## 1. Study Title

Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis

---

## 2. Authors

- **Đỗ Thùy Hương** (corresponding author) — Can Tho University, Vietnam; huongp1323001@gstudent.ctu.edu.vn
- **Phan Anh Tú** — Can Tho University, Vietnam

---

## 3. Research Questions

**RQ1 (Baseline):** What is the pooled internationalization–firm performance (I→P) effect size globally (*k*, *r̄*, *I*²)?

**RQ2 (ICRV moderation):** Does institutional context-regime vulnerability (ICRV; 6 regime groups from Advanced to Frontier/SIDS) moderate the I→P effect, with a gradient such that Frontier regimes show larger turning points and smaller baseline effects than Advanced regimes?

**RQ3 (cDAI moderation):** Does country-level digital adoption (cDAI, World Bank Digital Adoption Index, 0–1) positively moderate the I→P relationship?

**RQ4 (DPL phase):** Does Digital Platform Lifecycle (DPL) phase (1 = pre-2000, 2 = 2000–2009, 3 = 2010–2026) moderate the baseline I→P effect, with Phase 3 showing a different pattern than Phases 1–2?

---

## 4. Hypotheses

**H1 (ICRV between-regime):** The I→P effect size varies significantly across ICRV regime groups (*Q*_M test on between-regime variance is significant).

**E1a (ICRV directional — exploratory):** Advanced-regime firms show the largest baseline I→P effect; Frontier-regime firms show the smallest effect (monotone gradient).

**E1b (ICRV turning point — exploratory):** ICRV TP gradient: Frontier-regime TP > Advanced-regime TP (Frontier firms require greater internationalization before performance improves).

**H2 (DPL phase):** DPL Phase 3 (post-2009) studies show a larger I→P effect than Phase 1 or Phase 2 studies, consistent with digital platform maturation accelerating internationalization payoffs.

**H3 (cDAI moderation):** cDAI positively moderates the I→P relationship: studies from countries with higher digital adoption (higher cDAI) report larger positive I→P effects.

---

## 5. Eligibility Criteria (PICOS Framework)

### 5.1 Inclusion

| PICOS Element | Criterion |
|---|---|
| **P** (Population) | Firm-level unit of analysis; any country or multi-country sample |
| **I** (Intervention) | Internationalization measure: FSTS, DOI, export intensity, geographic diversification, number of foreign subsidiaries, FATA, or equivalent |
| **C** (Comparison) | Domestic-only firms or lower-internationalization baseline (implicit or explicit) |
| **O** (Outcome) | Firm performance: financial (ROA, ROE, ROS, Tobin's Q, sales growth) or operational (labor productivity, TFP, efficiency) |
| **S** (Study design) | Quantitative, peer-reviewed journal article; reports Pearson *r*, standardized *β*, *t*-value, *F*-statistic (*df* = 1), or odds ratio convertible to *r* |

### 5.2 Exclusion

| Criterion | Reason |
|---|---|
| Country-level or macro-level unit of analysis | Unit mismatch |
| Qualitative, conceptual, or review-only (no quantitative I→P coefficient) | No extractable effect size |
| Health, environmental, or non-IB disciplinary context | Out of scope |
| Book chapter, dissertation, conference paper, working paper (no DOI, not peer-reviewed) | Publication quality |
| Duplicate of existing k = 287 coded database (exact DOI match or >90% title similarity + same year) | Deduplication |
| Insufficient statistics to compute *r* (e.g., only reports direction without magnitude) | Effect size cannot be extracted |

---

## 6. Search Strategy

### 6.1 Web of Science (Primary Database)

**Platform:** Web of Science Core Collection  
**Access:** Institutional (Can Tho University) + WoS Starter API (free tier)  
**Date range:** 1977–2026  
**Document types:** Article only (exclude Review, Book Chapter, Proceedings, Editorial)  
**Language:** English  

**Search string (Advanced Search — Topic field):**
```
TS=(internationaliz* OR internationalis* OR multinationality 
    OR "degree of internationalization" OR "degree of internationalisation"
    OR "international diversification" OR "geographic diversification"
    OR "foreign sales" OR "foreign sales to total sales" OR FSTS
    OR "foreign assets" OR "foreign assets to total assets" OR FATA
    OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND 
TS=("firm performance" OR "enterprise performance" OR "corporate performance"
    OR "financial performance" OR "business performance"
    OR "labor productivity" OR "labour productivity" OR profitability 
    OR "Tobin's q" OR "return on assets" OR ROA OR "return on equity"
    OR "return on sales" OR "total factor productivity" OR "firm efficiency")
AND
TS=(correlation OR regression OR coefficient OR "effect size" OR "r =")
```

### 6.2 Scopus (Secondary Database)

**Platform:** Scopus (Elsevier)  
**Access:** CTU campus network (IP-restricted)  
**Date range:** 1977–2026  
**Status:** Pending — blocked by IP restriction outside campus network

**Search string (TITLE-ABS-KEY):**
```
TITLE-ABS-KEY((internationaliz* OR internationalis* OR multinationality
    OR "degree of internationalization" OR "foreign sales" OR FSTS
    OR "export intensity" OR "foreign subsidiaries")
AND ("firm performance" OR "financial performance" OR profitability
    OR "Tobin's q" OR "return on assets" OR ROA OR "labor productivity")
AND (correlation OR regression OR coefficient))
AND DOCTYPE(ar) AND LANGUAGE(english) AND PUBYEAR AFT 1976
```

### 6.3 OpenAlex (Supplementary — Free, Open Access)

**Script:** `p6/tools/openalex_prisma_search.py`  
**Date range:** 1977–2026  
**Filter:** peer_reviewed = true, type = journal-article

### 6.4 WoS Starter API (Supplementary Search — Completed)

**Script:** `p6/tools/06_wos_api_search.py`  
**Run date:** 2026-05-18  
**Records retrieved:** 782 (max_records = 2500)  
**Output:** `p6/tools/results/wos_api_20260518.csv`

---

## 7. Screening Protocol

### 7.1 Level 1 Screening (Title/Abstract)

- **Tool:** `p6/tools/04_screen_l1.py` (automated) + manual review of UNSURE
- **Decision rules:**
  - **INCLUDE** → passes title/abstract for L2
  - **EXCLUDE** → discarded with reason logged
  - **UNSURE** → manual review by lead author

### 7.2 Level 2 Screening (Full-Text)

- **Template:** `p6/tools/results/l2_extraction_template.csv`
- **Codebook:** `p6/tools/p6_extraction_codebook.md` (v1.0, 2026-05-18)
- **Decision fields:** `include_flag` (Y / N / UNSURE), `screen_l2_reason`
- **Discrepancies:** resolved by consensus or third-party adjudication

---

## 8. Data Extraction and Coding Protocol

### 8.1 Effect Size Extraction (Priority Order)

| Priority | Source statistic | Conversion formula |
|---|---|---|
| 1 | Pearson *r* (direct) | *r* used as-is |
| 2 | Standardized *β* | *r* ≈ *β* / √(*β*² + 1) |
| 3 | *t*-value + *N* | *r* = *t* / √(*t*² + *N* − 2) |
| 4 | *F*-statistic (*df* = 1) + *N* | *r* = √(*F* / (*F* + *N* − 2)) |
| 5 | Quadratic term (nonlinear studies) | Extract β₁ (linear) and β₂ (quadratic) + TP = −β₁/(2β₂) |

**Reference:** Borenstein et al. (2009) *Introduction to Meta-Analysis*, Appendix B

### 8.2 Moderator Coding

| Moderator | Variable name | Coding |
|---|---|---|
| Institutional Context-Resource Vulnerability | `icrv` | Integer 1–6 (1=Advanced, 2=Upper-Middle, 3=Lower-Middle, 4=Frontier, 5=SIDS, 6=LDC) |
| Country Digital Adoption Index | `cdai` | Continuous 0–1 (World Bank Digital Adoption Index, or nearest available proxy) |
| cDAI source | `cdai_source` | "WB_DAI", "ITU", "estimated", "missing" |
| Digital Platform Lifecycle phase | `dpl` | Integer 1/2/3 (1=pre-2000, 2=2000–2009, 3=2010–2026, based on publication year) |
| Internationalization measure type | `doi_type` | "FSTS", "DOI", "export_ratio", "geographic_diversification", "other" |
| Performance measure type | `fp_type` | "ROA", "ROE", "ROS", "Tobin_Q", "labor_productivity", "TFP", "sales_growth", "other" |
| Effect size estimation method | `is_estimated` | Binary (1 = converted from t/F/β; 0 = directly reported Pearson r) |
| Panel data | `is_panel` | Binary (1 = panel/longitudinal; 0 = cross-sectional) |
| Endogeneity correction | `endogeneity_corrected` | Binary (1 = IV/2SLS/Heckman/GMM; 0 = OLS/FE only) |

### 8.3 Inter-Coder Reliability

- **Subsample:** 20% of included studies, stratified by DPL phase and ICRV regime
- **Coders:** Đỗ Thùy Hương (lead) + one independent coder (advisor or research assistant)
- **Thresholds:** Cohen's κ ≥ 0.70 for categorical variables; ICC ≥ 0.80 for continuous variables
- **Resolution:** Consensus meeting for all disagreements; adjudication by third party if consensus fails

---

## 9. Statistical Analysis Plan

### 9.1 Primary Analysis — Three-Level MARA

**Software:** R (version ≥ 4.3), `metafor` package (Viechtbauer, 2010)

```r
library(metafor)

# Effect size calculation
dat <- escalc(measure = "COR", ri = r, ni = n, data = coded_db)

# Three-level random-effects model (baseline)
res_base <- rma.mv(
  yi, vi,
  random = ~ 1 | study_id / effect_id,
  data = dat,
  method = "REML"
)

# Key outputs:
# - Pooled effect r̄ [95% CI], p-value
# - σ²(2) within-study variance, σ²(3) between-study variance
# - I² total, I²(2), I²(3)
# - Q_E (residual heterogeneity), Q_M (moderator test)
```

### 9.2 Moderator Analyses

```r
# M2: ICRV regime (H1)
res_icrv <- rma.mv(yi, vi, mods = ~ factor(icrv),
  random = ~ 1 | study_id / effect_id, data = dat)

# M3: cDAI continuous (H3)
res_cdai <- rma.mv(yi, vi, mods = ~ cdai,
  random = ~ 1 | study_id / effect_id, data = dat)

# M4: DPL phase (H2)
res_dpl <- rma.mv(yi, vi, mods = ~ factor(dpl),
  random = ~ 1 | study_id / effect_id, data = dat)

# M5: Internationalization measure type (exploratory)
res_doi_type <- rma.mv(yi, vi, mods = ~ doi_type,
  random = ~ 1 | study_id / effect_id, data = dat)

# M6: Performance measure type (exploratory)
res_fp_type <- rma.mv(yi, vi, mods = ~ fp_type,
  random = ~ 1 | study_id / effect_id, data = dat)
```

### 9.3 Publication Bias

```r
# Egger's regression test
regtest(rma(yi, vi, data = dat), model = "rma")

# Trim-and-fill
taf <- trimfill(rma(yi, vi, data = dat))
funnel(taf, legend = TRUE)
```

### 9.4 Sensitivity Analyses

```r
# Leave-one-out
loo <- leave1out(res_base)

# Alternative estimator comparison: REML vs DerSimonian-Laird
res_dl <- rma(yi, vi, method = "DL", data = dat)

# Restriction to directly-reported Pearson r only (no conversions)
res_direct <- rma.mv(yi, vi,
  random = ~ 1 | study_id / effect_id,
  data = dat[dat$is_estimated == 0, ])

# Restriction to panel data only
res_panel <- rma.mv(yi, vi,
  random = ~ 1 | study_id / effect_id,
  data = dat[dat$is_panel == 1, ])
```

---

## 10. Reporting Standards

- **PRISMA 2020** (Page et al., 2021): full flow diagram with records identified, screened, eligible, and included
- **APA Meta-Analysis Reporting Standards** (Cooper, 2010): Table 1 study characteristics, Table 2 moderator results
- **MAAS-G** (Marsh et al., 2009): forest plot with study-level estimates and CIs

---

## 11. Timeline

| Milestone | Target date |
|---|---|
| OSF pre-registration submitted | 2026-05-19 (or earliest available) |
| L2 full-text screening complete | 2026-06-15 |
| Inter-coder reliability computed | 2026-06-20 |
| Database merge + MARA re-run | 2026-06-30 |
| Manuscript revision submitted to IBR | 2026-07-15 |

---

## 12. Data Availability

- Coded study database: `p6/data/p6_study_database_updated.csv` (available upon reasonable request)
- R analysis scripts: `p6/tools/meta_r_scripts/` (GitHub repository, branch: `claude/edit-vietnamese-academic-standards-xcAmn`)
- OSF pre-registration: this document (time-stamped after submission)
- PRISMA 2020 checklist: `p6/p6_prisma_checklist.md`

---

## 13. Conflicts of Interest

None declared. This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

---

## HOW TO SUBMIT THIS REGISTRATION TO OSF.IO

1. Go to **https://osf.io** and sign in (create account if needed)
2. Click **"Create a new project"** → name it: *"P6 I→P Meta-Analysis: ICRV, cDAI, DPL Moderators"*
3. Inside the project, click **"Registrations"** tab → **"New Registration"**
4. Choose template: **"Open-Ended Registration"** (or "Secondary Data Preregistration")
5. Copy the content of this file into the registration form
6. Upload this file (`P6_OSF_Preregistration_Template.md`) as an attachment
7. **Submit** — OSF will timestamp and lock the registration
8. Copy the registration URL (e.g., `https://osf.io/xxxxx`) 
9. Send the URL to Claude for insertion into the manuscript and PRISMA checklist

**Time estimate:** ~15–20 minutes to complete the form
