# P6 Effect Size Extraction Codebook
# Meta-Analysis: Internationalization → Firm Performance (I→P), 1977–2026

> Protocol based on `meta-analysis-extraction-workflow` skill + MARS (Meta-Analysis Reporting Standards)
> Applied to: 782 new WoS candidates (post-L2 screening)
>
> **Version 1.1 (2026-05-27)** — supersedes v1.0 (2026-05-18, prereg-era draft). The ICRV (§4.1)
> and DPL (§4.3) coding schemes were reconciled to the final operationalisation actually used in
> the analysed dataset and reported in the manuscript (§2). The original prereg/v1.0 schemes are
> retained in the frozen OSF preregistration; the changes are disclosed in the manuscript's
> "Deviations from preregistration" statement.

---

## 1. Inclusion Decision (L2 Full-Text)

**INCLUDE if ALL criteria met:**
- [ ] Firm-level unit of analysis (not country, industry, or individual)
- [ ] Quantitative I→P relationship reported (r, β, t, F, or convertible stat)
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

1. **Pearson r** reported directly → use as-is
2. **Partial correlation** → note as approximation, code `is_partial=1`
3. **Standardized β** from OLS/panel → r ≈ β (acceptable approximation per Peterson & Brown, 2005)
4. **t-statistic** + N → r = t / √(t² + df)
5. **F-statistic** (1 df numerator) → r = √(F / (F + df_error))
6. **p-value + N** → convert via t-distribution (last resort, conservative)

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

If a study reports multiple I→P effects (e.g., different performance measures):
- Extract ALL effects → separate rows with same `study_id`, different `effect_id`
- Use `rma.mv()` with `random = ~ 1 | study_id/effect_id` (three-level model)
- Correlation between effects from same sample: assume ρ = 0.50 (Cheung & Chan, 2004)

### 3.3 Curvilinear relationships

If study tests U-shape (FSTS + FSTS²):
- Extract linear β → `r` column
- Extract quadratic β → `r_quadratic` column
- Extract turning point if reported → `turning_point` column
- Code `doi_type = "quadratic"` in moderator

---

## 4. Moderator Coding

### 4.1 ICRV — Institutional Context-Resource Vulnerability (final scheme)

Six codes, classified by World Bank WGI Rule-of-Law score (2023 vintage), validated against the
IMF World Economic Outlook country classification. Five codes are populated in the corpus; the
Pacific-SIDS code is defined a priori but returns zero qualifying studies.

| Code | Label | WGI Rule of Law | Examples |
|---|---|---|---|
| `I` | Advanced-Innovation | > +0.80 | Singapore, Hong Kong, South Korea, Japan, Taiwan, Australia |
| `II` | Upper-Middle | 0 < WGI ≤ +0.80 | China, Malaysia, Thailand |
| `III` | Emerging | −0.50 < WGI ≤ 0 | Vietnam, India, Philippines |
| `FR` | Frontier / LDC | ≤ −0.50 | Bangladesh, Myanmar, Pakistan |
| `SIDS` | Pacific small-island developing states | — | Fiji, Samoa, Tonga (k = 0 in corpus) |
| `MX` | Multi-country pooled (≥ 2 regimes) | — | samples with no single modal-country regime ≥ 60% |

**Country-assignment rule.** Single-country samples → that country's regime. Multi-country
samples → the modal country's regime **if one country contributes ≥ 60% of the sample**;
otherwise code `MX` (cross-regime). *(Note: v1.0 instead folded multi-country into "emerging"; the
standalone `MX` category is a post-registration refinement — see manuscript "Deviations".)*

**Crosswalk to the dissertation's canonical six-regime ICRV:** P6 `I` ≡ Regime I (Advanced-
Innovation); P6 `II` (Upper-Middle) ≡ Regime III; P6 `III` (Emerging) ≡ Regime IV; `FR` ≡ Regime V;
`SIDS` ≡ Regime VI. The dissertation's Regime II (Advanced Resource-Driven / GCC) is not separately
populated here, and `MX` has no I–VI equivalent.

### 4.2 cDAI — Country Digital Adoption Index (continuous, 0–1)

Source: ITU / World Bank Digital Adoption Index for sample country-year midpoint
- Use mean of sample period years
- Code `cdai_source` = "ITU_2023" or "WB_DAI"
- If unavailable: leave blank, code `cdai_missing = 1`

### 4.3 DPL — Digital Paradox Lifecycle Phase (final scheme)

Coded by the position of the study's **data-collection period** relative to the 2009 digital
productivity inflection point (Brynjolfsson et al., 2021; David, 1990), not by publication year.

| Code | Phase | Data-period rule |
|---|---|---|
| `PRE` | Precede | data collected predominantly before 2009 |
| `SPN` | Span | data spanning the transitional 2005–2014 window |
| `FOL` | Follow | data collected predominantly after 2014 |

*(v1.0 instead used publication-year bins 1 = pre-2000 / 2 = 2000–2009 / 3 = 2010–2026; the
Precede/Span/Follow construct is a post-registration refinement — see manuscript "Deviations".)*

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
  icrv           = "II",        # Upper-Middle (CHN); see 4.1
  cdai           = 0.62,
  dpl            = "FOL",       # Follow (data 2010-2019, post-2014); see 4.3
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
