# P6 — PRISMA 2020 Flow Diagram & Search Documentation
# Meta-Analysis I→P 1977–2026 (Independent Systematic Review)

> **Phiên bản**: v2.0 (12/05/2026)
> **Chuẩn áp dụng**: PRISMA 2020 (Page et al., 2021)
> **Loại**: Fresh/independent meta-analysis (không phải update)
> **Tham chiếu**: `p6/06_p6_meta_update_plan_vi.md` §6

---

## 1. PRISMA 2020 Flow (ASCII Diagram)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                     IDENTIFICATION (Nhận diện)                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Records identified from electronic databases:                               ║
║  • Web of Science Core Collection    [n = TBD — ghi sau khi search]         ║
║  • Scopus                            [n = TBD]                              ║
║  • EBSCOhost (Business Source)       [n = TBD — optional]                   ║
║                                                                              ║
║  Records from supplementary methods:                                         ║
║  • Backward citation scan of 5 prior metas:                                  ║
║      Bausch & Krist (2007, MIR)      [n ≈ 68 screened]                      ║
║      Kirca et al. (2012, GSJ)        [n ≈ 180 screened]                     ║
║      Marano et al. (2016, JWB)       [n ≈ 90 screened]                      ║
║      Wu et al. (2022, MIR)           [n ≈ 80 screened]                      ║
║      Arte & Larimo (2022, IBR)       [n ≈ 60 screened]                      ║
║  • Forward citation search via scite.ai    [n = TBD]                        ║
║  • Hand-search (author papers, 2024–26)    [n = 19]                         ║
║                                                                              ║
║  TOTAL RECORDS IDENTIFIED: [N = TBD]                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
                              │
                              ▼ Remove duplicates [n = TBD]
╔══════════════════════════════════════════════════════════════════════════════╗
║                     SCREENING — Level 1 (Title/Abstract)                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Records after deduplication: [n = TBD]                                      ║
║  Records excluded (title/abstract screen): [n = TBD]                        ║
║  Reasons:                                                                    ║
║    • Not examining I→P relationship: [n = TBD]                              ║
║    • Country/industry-level (not firm-level): [n = TBD]                     ║
║    • Qualitative only: [n = TBD]                                             ║
║    • Conceptual/theoretical only: [n = TBD]                                  ║
║    • Non-English: [n = TBD]                                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
                              │
                              ▼ Full-text retrieved [n = TBD]
╔══════════════════════════════════════════════════════════════════════════════╗
║                     ELIGIBILITY — Level 2 (Full Text)                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Records assessed for eligibility: [n = TBD]                                 ║
║  Records excluded (full-text): [n = TBD]                                     ║
║  Reasons:                                                                    ║
║    • No calculable Pearson r or convertible statistic: [n = TBD]            ║
║    • Duplicate sample (kept larger/most recent): [n = TBD]                  ║
║    • Outside 1977–2026 range: [n = TBD]                                     ║
║    • Not firm-level observation: [n = TBD]                                   ║
║    • Meta-analysis (not primary study): [n = TBD]                           ║
║    • Insufficient information for coding: [n = TBD]                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
                              │
                              ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║                     INCLUDED                                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Studies included in meta-analysis: k = [TBD — hiện có 235 trong database]  ║
║  Effect sizes: K ≈ [TBD — hiện có ~385]                                     ║
║                                                                              ║
║  Breakdown by source:                                                        ║
║    Database search (WoS + Scopus):         [n = TBD]                        ║
║    Backward citation scan (5 metas):       [n = TBD]                        ║
║    Forward citation (scite.ai):            [n = TBD]                        ║
║    Hand-search:                            [n = TBD]                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

> ⚠️ **Tất cả [n = TBD]** sẽ được điền sau khi hoàn thành WoS + Scopus search.
> Ngày search: ___/05/2026. Ghi lại số kết quả ngay sau khi chạy query.

---

## 2. Search Query Documentation

### Database 1: Web of Science Core Collection

**Ngày search**: [TBD]
**Người search**: Đỗ Thùy Hương
**Kết quả**: [n = TBD]

**Query (Advanced Search — Topic Search TS):**
```
TS=("internationalization" OR "internationalisation" OR "multinationality" 
    OR "degree of internationalization" OR "export intensity" 
    OR "foreign sales ratio" OR "FSTS" OR "international diversification") 
AND 
TS=("firm performance" OR "corporate performance" OR "financial performance" 
    OR "labor productivity" OR "labour productivity" OR "profitability" 
    OR "Tobin's q" OR "return on assets" OR "ROA" OR "return on equity")
AND
TS=(correlation OR regression OR coefficient OR "effect size" OR "r =")
```

**Filters applied:**
- Timespan: 1977-01-01 to 2026-05-12
- Document Types: Article
- Language: English
- Database: Web of Science Core Collection

**Export**: Full record + Cited references → Plain Text / Excel

---

### Database 2: Scopus

**Ngày search**: [TBD]
**Người search**: Đỗ Thùy Hương
**Kết quả**: [n = TBD]

**Query:**
```
TITLE-ABS-KEY("internationalization" OR "internationalisation" 
    OR "multinationality" OR "degree of internationalization" 
    OR "export intensity" OR "FSTS" OR "international diversification")
AND
TITLE-ABS-KEY("firm performance" OR "labor productivity" 
    OR "labour productivity" OR "profitability" 
    OR "return on assets" OR "Tobin")
AND
TITLE-ABS-KEY(correlation OR regression OR coefficient OR "effect size")
AND PUBYEAR > 1976 AND PUBYEAR < 2027
AND DOCTYPE(ar)
AND LANGUAGE(english)
```

---

### Supplementary Method 1: Backward Citation Scan

5 major meta-analyses screened in full:

| Meta-analysis | Year | Journal | Primary studies | New to pool |
|---------------|------|---------|----------------|-------------|
| Bausch & Krist | 2007 | MIR | 68 | [TBD] |
| Kirca et al. | 2012 | GSJ | 180 | [TBD] |
| Marano et al. | 2016 | JWB | ~90 | [TBD] |
| Wu et al. | 2022 | MIR | ~80 | [TBD] |
| Arte & Larimo | 2022 | IBR | ~60 | [TBD] |

**Protocol**: Each reference list screened against inclusion criteria; eligible studies retrieved and coded if not already in database from formal search.

---

### Supplementary Method 2: Forward Citation Search (scite.ai)

**Query**: Forward citations of 5 anchor studies:
- Lu & Beamish (2004) — S-curve seminal
- Contractor et al. (2003) — three-stage model
- Hitt et al. (1997) — inverted-U seminal
- Bausch & Krist (2007) — meta-analysis
- Kirca et al. (2012) — meta-analysis

**Date filter**: 2015–2026 (overlap with formal search acceptable — duplicates removed)
**Results**: [n = TBD]

---

### Supplementary Method 3: Hand-search

Author's own publications and papers from known research groups working on I→P in Asia-Pacific (2020–2026). Included only if meeting full eligibility criteria.
**Results**: n = 19 (documented in `p6_primary_studies_apa7.md` S176–S194)

---

## 3. Inclusion / Exclusion Criteria (PICO Framework)

| Element | Criterion |
|---------|-----------|
| **P** — Population | Firms of any size, any country, any industry |
| **I** — Intervention/Exposure | Degree of internationalization (DOI): export intensity (FSTS), foreign assets ratio (FATA), number of foreign countries, composite DOI index |
| **C** — Comparator | Not applicable (observational studies) |
| **O** — Outcome | Firm performance: financial (ROA, ROE, Tobin's q, ROS, profit), operational (labor productivity, sales growth), composite performance index |
| **S** — Study design | Primary empirical studies reporting Pearson r or statistics convertible to r (β, t, F, η²) |

**Inclusion criteria (ALL must be met):**
1. Reports empirical relationship between DOI measure and firm performance measure
2. Reports Pearson r, or statistics allowing r computation
3. Firm-level unit of analysis
4. Published 1977–2026
5. English-language full text available
6. Peer-reviewed journal article

**Exclusion criteria (ANY triggers exclusion):**
1. Meta-analysis, systematic review, or literature review (not primary study)
2. Country/industry/national-level analysis
3. Qualitative study
4. Insufficient statistics for effect size computation
5. Duplicate sample (retained largest/most recent; smaller removed)
6. Conference proceedings, theses, working papers

---

## 4. Inter-Coder Reliability Protocol

- **Primary coder**: Đỗ Thùy Hương
- **Second coder**: [Research assistant / HD Phan Anh Tú — 20% random sample]
- **Target κ**: ≥ 0.80 for all 7 moderator variables
- **Disagreement resolution**: Discussion; if unresolved → third coder

**Variables coded** (7 moderators + study descriptors):

| Variable | Type | Values |
|----------|------|--------|
| Study ID | String | S001–S235+ |
| First author | String | — |
| Year | Integer | 1977–2026 |
| Country/region | String | ISO code |
| Pearson r | Continuous | −1 to +1 |
| Sample size n | Integer | — |
| DOI measure type | Categorical | EXP / FDI / COUNT / COMP |
| FP measure type | Categorical | ROA / PROD / COMP / MIX |
| ICRV regime | Categorical | I / II / III / IV / V / MX |
| cDAI level | Categorical | H / M / L |
| DPL phase | Categorical | PRE / SPN / FOL |

---

## 5. Database Coverage Summary

```
Current database state (pre-formal-search):
  Studies in coded database:       235
  Estimated overlap with WoS:      ~180–200 (will be confirmed)
  Estimated new from WoS/Scopus:   ~15–50 (TBD after search)
  
  Post-search target:              250+ (stretch: 270)
  Minimum viable for publication:  200+
```

---

## 6. Version History

| Version | Date | Change |
|---------|------|--------|
| v1.0 | 12/05/2026 | Initial draft — update framing, estimated numbers |
| v1.1 | 12/05/2026 | k=135→235 in INCLUDED box |
| v2.0 | 12/05/2026 | Full rewrite — fresh/independent search framework; all fake numbers replaced with [TBD]; PICO criteria added; inter-coder protocol added |

---

## 7. Tài liệu tham khảo — PRISMA và Methods

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. *Psychological Methods, 19*(2), 211–229. https://doi.org/10.1037/a0032968

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594. https://doi.org/10.3758/s13428-012-0261-6

Suurmond, R., van Rhee, H., & Hak, T. (2017). Introduction, comparison, and validation of Meta-Essentials. *Research Synthesis Methods, 8*(4), 537–553. https://doi.org/10.1002/jrsm.1260

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *British Medical Journal, 315*(7109), 629–634. https://doi.org/10.1136/bmj.315.7109.629

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot–based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455–463. https://doi.org/10.1111/j.0006-341X.2000.00455.x
