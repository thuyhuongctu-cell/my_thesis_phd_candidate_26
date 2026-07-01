# P6 Effect Size Extraction Codebook
# Meta-Analysis: Internationalization to Firm Performance (I to P), 1977–2026

> Protocol based on `meta-analysis-extraction-workflow` skill + MARS (Meta-Analysis Reporting Standards)
> Applied to: 782 new WoS candidates (post-L2 screening)

---

## 1. Inclusion Decision (L2 Full-Text)

**INCLUDE if ALL criteria met:**
- [ ] Firm-level unit of analysis (not country, industry, or individual)
- [ ] Quantitative I to P relationship reported (r, β, t, F, or convertible stat)
- [ ] Internationalization operationalized as DOI/FSTS/export/FDI/entropy/number of markets
- [ ] Performance operationalized (ROA, ROE, Tobin's Q, ROS, sales growth, productivity, etc.)
- [ ] Peer-reviewed journal article (not dissertation, working paper, book chapter)
- [ ] English language; data 1977–2026

**EXCLUDE if ANY:**
- Country/macro-level analysis
- Qualitative only (case study, interview, ethnography)
- No extractable effect size (descriptive only, no test of relationship)
- Meta-analysis or review paper (already excluded at L1 mostly)
- Pure conceptual/theoretical

---

## 2. Study Descriptor Fields

| Field | Code | Notes |
|---|---|---|
| `study_id` | Author_Year (e.g., Smith_2020) | Add suffix a/b if same author-year |
| `effect_id` | study_id + _E1, _E2 | For multiple effects per study |
| `author` | Last name(s) | First author only for matching |
| `year` | Publication year | Not data year |
| `journal` | Full journal name | |
| `doi` | DOI or CrossRef-enriched | Lowercase, no https://doi.org/ prefix |
| `country` | Sample country ISO-3 | Multiple: semicolon-separated |
| `sample_start` | First year of data | |
| `sample_end` | Last year of data | |
| `n` | Total firm-level observations | |

---

## 3. Effect Size Extraction

### 3.1 Priority hierarchy (use first available)

1. **Pearson r** reported directly to use as-is
2. **Partial correlation** to note as approximation, code `is_partial=1`
3. **Standardized β** from OLS/panel to r ≈ β (acceptable approximation per Peterson & Brown, 2005)
4. **t-statistic** + N to r = t / √(t² + df)
5. **F-statistic** (1 df numerator) to r = √(F / (F + df_error))
6. **p-value + N** to convert via t-distribution (last resort, conservative)

```r
# R conversion formulas (metafor::escalc)
# From r directly:
escalc(measure="COR", ri=r, ni=n)

# From t:
r <- t / sqrt(t^2 + df)

# From F (1 df numerator):
r <- sqrt(F / (F + df_error))
```

### 3.2 Multiple effects per study

If a study reports multiple I to P effects (e.g., different performance measures):
- Extract ALL effects to separate rows with same `study_id`, different `effect_id`
- Use `rma.mv()` with `random = ~ 1 | study_id/effect_id` (three-level model)
- Correlation between effects from same sample: assume ρ = 0.50 (Cheung & Chan, 2004)

### 3.3 Curvilinear relationships

If study tests U-shape (FSTS + FSTS²):
- Extract linear β to `r` column
- Extract quadratic β to `r_quadratic` column
- Extract turning point if reported to `turning_point` column
- Code `doi_type = "quadratic"` in moderator

---

## 4. Moderator Coding

### 4.1 ICRV — Institutional Context-Resource Vulnerability (6 regimes)

| Code | Label | Examples |
|---|---|---|
| 1 | Advanced Market | USA, UK, Germany, Japan, Australia, Canada |
| 2 | Emerging Market | China, India, Brazil, Turkey, Mexico, Indonesia |
| 3 | Transition Economy | Poland, Czech Republic, Hungary, Russia, Ukraine |
| 4 | Resource-Rich / GCC | Saudi Arabia, UAE, Qatar, Kuwait, Nigeria, Kazakhstan |
| 5 | Small Island / SIDS | Singapore, Malta, Mauritius, Caribbean states |
| 6 | Frontier / LDC | Bangladesh, Ethiopia, Myanmar, Cambodia |

Multi-country studies: code dominant context; if mixed to code "2" (emerging) as conservative

### 4.2 cDAI — Country Digital Adoption Index (continuous, 0–1)

Source: ITU / World Bank Digital Adoption Index for sample country-year midpoint
- Use mean of sample period years
- Code `cdai_source` = "ITU_2023" or "WB_DAI"
- If unavailable: leave blank, code `cdai_missing = 1`

### 4.3 DPL — Digital Platform Lifecycle Phase

| Code | Phase | Years |
|---|---|---|
| 1 | Pre-digital | Before 2000 |
| 2 | Early digital | 2000–2009 |
| 3 | Platform era | 2010–2026 |

Code based on **data midpoint year** (not publication year)

### 4.4 DOI measure type

| Code | Label |
|---|---|
| `fsts` | Foreign Sales to Total Sales |
| `entropy` | Entropy-based DOI index |
| `n_countries` | Number of foreign markets |
| `fdi_stock` | FDI stock / assets abroad |
| `export_dummy` | Exporter vs. non-exporter binary |
| `composite` | Sullivan (1994) or similar composite |
| `other` | Other / not classifiable |

### 4.5 Performance measure type

| Code | Label |
|---|---|
| `roa` | Return on Assets |
| `roe` | Return on Equity |
| `ros` | Return on Sales / Profit margin |
| `tobin_q` | Tobin's Q (market/book) |
| `sales_growth` | Revenue / sales growth |
| `productivity` | Labour or TFP |
| `market_return` | Stock market return |
| `composite` | Composite performance index |

---

## 5. Quality & Bias Flags

| Field | Values | Notes |
|---|---|---|
| `is_estimated` | 0/1 | 1 = r estimated from β or t/F |
| `is_partial` | 0/1 | 1 = partial correlation (not zero-order) |
| `is_panel` | 0/1 | 1 = panel/longitudinal data |
| `endogeneity_corrected` | 0/1 | 1 = IV, Heckman, GMM, DID used |
| `include_flag` | 1/0 | Final inclusion decision |
| `notes` | text | Any coding notes or uncertainties |

---

## 6. R Extraction Template

```r
# After extracting values manually, use escalc():
library(metafor)

new_studies <- data.frame(
  study_id       = "Smith_2020",
  effect_id      = "Smith_2020_E1",
  r              = 0.18,        # Pearson r (or estimated)
  n              = 450,
  country        = "CHN",
  sample_start   = 2010,
  sample_end     = 2019,
  icrv           = 2,           # Emerging market
  cdai           = 0.62,
  dpl            = 3,           # Platform era
  doi_type       = "fsts",
  fp_type        = "roa",
  is_estimated   = 0,
  is_panel       = 1,
  include_flag   = 1
)

# Compute yi (Fisher's z) and vi (sampling variance)
new_studies <- escalc(measure="COR", ri=r, ni=n, data=new_studies)
```

---

## 7. Inter-Coder Reliability Protocol

Per PRISMA-MARA guidelines: 20% random subsample double-coded

**Target statistics:**
- Continuous (r, n): ICC(2,1) ≥ 0.80
- Categorical (icrv, doi_type, fp_type): Cohen's κ ≥ 0.70

```r
library(irr)
# For continuous: ICC
icc(cbind(coder1_r, coder2_r), model="twoway", type="agreement")

# For categorical: kappa
kappa2(cbind(coder1_icrv, coder2_icrv))
```

Disagreements: resolve via discussion; if unresolvable, senior author decides.

---

## 8. Integration with Existing Database

After coding new studies, merge with `p6/data/p6_study_database.csv`:

```python
import pandas as pd

existing = pd.read_csv('p6/data/p6_study_database.csv')
new      = pd.read_csv('p6/tools/results/new_coded_studies.csv')

# Re-number study_ids sequentially
combined = pd.concat([existing, new], ignore_index=True)
combined['study_id'] = ['S' + str(i+1).zfill(4) for i in range(len(combined))]

combined.to_csv('p6/data/p6_study_database_v2.csv', index=False)
print(f"Updated database: k={combined['include_flag'].eq(1).sum()} studies")
```

---

*Codebook version: 1.0 | 2026-05-18 | Đỗ Thùy Hương, CTU*
