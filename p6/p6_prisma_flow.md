# P6 — PRISMA 2020 Flow Diagram & Search Documentation
# Meta-Analysis I→P 1977–2026 (Independent Systematic Review)

> **Phiên bản**: v2.7 (19/05/2026)
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
║  • Web of Science Core Collection    [n = 2,180 ✅ — API 18/05/2026]        ║
║  • Scopus                            [n = TBD — cần institutional access]   ║
║  • OpenAlex (free, global coverage)  [n = TBD — chạy p6/tools/openalex_    ║
║                                       prisma_search.py trên máy có mạng]   ║
║  • ABI/INFORM Complete               [n = TBD]                              ║
║  • Business Source Complete (EBSCO)  [n = TBD]                              ║
║  • ScienceDirect (Elsevier)          [n = TBD]                              ║
║  • SpringerLink                      [n = TBD]                              ║
║  • Emerald Insight                   [n = TBD]                              ║
║                                                                              ║
║  Records from supplementary methods:                                         ║
║  • Backward citation scan of 5 prior metas:                                  ║
║      Bausch & Krist (2007, MIR)      [n ≈ 68 screened]                      ║
║      Kirca et al. (2012, GSJ)        [n ≈ 180 screened]                     ║
║      Marano et al. (2016, JWB)       [n ≈ 90 screened]                      ║
║      Wu et al. (2022, MIR)           [n ≈ 80 screened]                      ║
║      Arte & Larimo (2022, IBR)       [n ≈ 60 screened]                      ║
║  • Forward citation search (Google Scholar, 5 anchors) [n = TBD]            ║
║  • Hand-search (author papers, 2024–26)    [n = 19]                         ║
║                                                                              ║
║  TOTAL RECORDS IDENTIFIED: [N = TBD — WoS confirmed: 2,180; Scopus TBD]    ║
╚══════════════════════════════════════════════════════════════════════════════╝
                              │
                              ▼ Remove duplicates [n = TBD; WoS-only: 1]
╔══════════════════════════════════════════════════════════════════════════════╗
║                     SCREENING — Level 1 (Title/Abstract)                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Records after WoS dedup: n = 2,179  (1 duplicate removed ✅)              ║
║                                                                              ║
║  L1 keyword pre-screen (WoS; 18/05/2026):                                   ║
║    • Advanced to L2 (I→P title signal)     : n =   782  ✅                  ║
║    • Excluded at L1 (title outside domain) : n = 1,397                     ║
║        – No I→P signal (irrelevant domain) : n ≈ 1,200                     ║
║        – Reviews / meta-analyses           : n ≈    97                     ║
║        – Qualitative / conceptual / medical: n ≈   100                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  L2 TITLE SCREEN — 782 records (18/05/2026):                                ║
║    • Y (clearly eligible)                  : n =   345                     ║
║    • N (clearly excluded)                  : n =    35                     ║
║        – E1: Conceptual/editorial          : n =     4                     ║
║        – E2: Qualitative/case study        : n =     8                     ║
║        – E3: Macro-level analysis          : n =     6                     ║
║        – E5: Export as DV not IV           : n =    17                     ║
║    • UNSURE (title insufficient)           : n =   402                     ║
║                                                                              ║
║  UNSURE re-screen Round 1 (script 14):                                      ║
║    • Resolved Y (new unique)               : n =   129  ✅                  ║
║    • Resolved Y (dup of existing k=287)    : n =     6  → excluded         ║
║    • Resolved N                            : n =     3                     ║
║    • Still UNSURE after R1                 : n =   263                     ║
║                                                                              ║
║  UNSURE re-screen Round 2 (script 18, two-tier rules):                      ║
║    • Resolved Y (all genuinely new)        : n =    30  ✅                  ║
║    • Resolved N                            : n =    29                     ║
║    • Still UNSURE after R2                 : n =   204                     ║
║                                                                              ║
║  UNSURE re-screen Round 3 (script 20, extended HARD_EXCL+STRONG_INCL):      ║
║    • Resolved Y (all genuinely new)        : n =    25  ✅                  ║
║    • Resolved N                            : n =    43                     ║
║    • Still UNSURE after R3                 : n =   136                     ║
║                                                                              ║
║  UNSURE re-screen Round 4 (script 22, capital structure / location /         ║
║      antecedent exclusions; performance consequences / crisis resilience):   ║
║    • Resolved Y (all genuinely new)        : n =    15  ✅                  ║
║    • Resolved N                            : n =    34                     ║
║    • Still UNSURE                          : n =    87                     ║
║                                                                              ║
║  UNSURE re-screen Round 5 (script 24, title-only; 19/05/2026):              ║
║    • Resolved Y (all genuinely new)        : n =     4  ✅                  ║
║    • Resolved N                            : n =    11                     ║
║    • Still UNSURE                          : n =    72                     ║
║                                                                              ║
║  UNSURE re-screen Round 6 (script 26, title-only; 19/05/2026):              ║
║    • Resolved Y (all genuinely new)        : n =     8  ✅                  ║
║    • Resolved N                            : n =    46                     ║
║    • Still UNSURE                          : n =    18                     ║
║                                                                              ║
║  UNSURE re-screen Round 7 (manual signals: book-chapter DOI, single-case,   ║
║      antecedent-DV, non-business journal, macro unit; 19/05/2026):           ║
║    • Resolved Y                            : n =     0                     ║
║    • Resolved N                            : n =     8  ✅                  ║
║    • Still UNSURE (abstract required)      : n =    10  [TBD]              ║
║                                                                              ║
║  Total L2 Y (WoS arm)                      : n =   562  ✅                  ║
║    (345 direct + 135 R1 + 30 R2 + 25 R3 + 15 R4 + 4 R5 + 8 R6 + 0 R7)     ║
╚══════════════════════════════════════════════════════════════════════════════╝
                              │
                              ▼ Dedup vs prior DB + extraction
╔══════════════════════════════════════════════════════════════════════════════╗
║                     ELIGIBILITY — Extraction Pool                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Dedup vs. existing k=287:                                                   ║
║    Confirmed genuinely new (R1 dedup)      : n =   321  ✅                  ║
║    Title-confirmed new (R1-R7 pending)     : n =   211  [TBD: need full-text] ║
║    Active extraction pool (worklist v8)    : n =   532  ✅                  ║
║                                                                              ║
║  Full-text excluded (reasons after extraction — TBD):                       ║
║    • No calculable r / convertible stat    : [TBD]                         ║
║    • Not firm-level unit of analysis       : [TBD]                         ║
║    • Thesis / conference / working paper   : [TBD]                         ║
║    • Duplicate sample                      : [TBD]                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
                              │
                              ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║                     INCLUDED                                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Studies included in meta-analysis:                                          ║
║    Prior database (backward scan + hand-search): k = 237, K = 287  ✅       ║
║    New studies from WoS arm (after extraction) : k = [TBD]                 ║
║    New studies from Scopus arm (pending)        : k = [TBD]                 ║
║    ──────────────────────────────────────────────────────                    ║
║    TOTAL                                        : k = [TBD], K = [TBD]     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

> ✅ = **Confirmed** (WoS arm; 18/05/2026). [TBD] = pending Scopus search or extraction.
> Scopus search: requires CTU campus institutional access. Run `02_parse_scopus_export.py` after export.

---

## 2. Search Query Documentation

### Database 1: Web of Science Core Collection

**Ngày search**: [TBD]
**Người search**: Đỗ Thùy Hương
**Kết quả**: [n = TBD]

**Query (Advanced Search — Topic Search TS):**
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
    OR "ROA" OR "Tobin's Q" OR "return on assets" OR "profitability"
    OR "labor productivity" OR "labour productivity" OR "total factor productivity"
    OR "return on equity" OR "return on sales" OR "firm efficiency")
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
TITLE-ABS-KEY(internationaliz* OR internationalis*
    OR multinationality OR "degree of internationalization"
    OR "degree of internationalisation"
    OR "international diversification" OR "geographic diversification"
    OR "foreign sales" OR "foreign sales to total sales" OR FSTS
    OR "foreign assets" OR "foreign assets to total assets" OR FATA
    OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND
TITLE-ABS-KEY("firm performance" OR "enterprise performance"
    OR "corporate performance" OR "financial performance" OR "business performance"
    OR "labor productivity" OR "labour productivity" OR profitability
    OR "return on assets" OR Tobin OR "return on equity"
    OR "return on sales" OR "total factor productivity" OR "firm efficiency")
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

### Supplementary Method 2: Forward Citation Search (Google Scholar)

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
6. Non-peer-reviewed publication: doctoral dissertations, master's theses, working papers, conference papers, book chapters, unpublished manuscripts, institutional reports

---

## 4. Inter-Coder Reliability Protocol

- **Primary coder**: Đỗ Thùy Hương
- **Second coder**: [Research assistant / HD Phan Anh Tú — 20% random sample]
- **Target κ**: ≥ 0.80 for all 7 moderator variables
- **Disagreement resolution**: Discussion; if unresolved → third coder

**Variables coded** (7 moderators + study descriptors):

| Variable | Type | Values |
|----------|------|--------|
| Study ID | String | S001–S237++ |
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
  Studies in coded database:       238
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
| v2.1 | 16/05/2026 | k=235→238, K=~385→288 (forest_data.csv actual count); Study ID range S001–S237++ |
| v2.2 | 16/05/2026 | Search strategy expanded: WoS/Scopus queries updated to global scope (no Asia-Pacific geo filter); supplementary databases added (ABI/INFORM, Business Source Complete, ScienceDirect, SpringerLink, Emerald Insight); "Non-peer-reviewed publication" added as exclusion reason; scite.ai → Google Scholar for forward citation; INCLUDED breakdown updated |
| v2.3 | 16/05/2026 | Added OpenAlex as free supplementary database; Python search script created at p6/tools/openalex_prisma_search.py; WoS/Scopus noted as requiring institutional access |
| v2.4 | 18/05/2026 | R3 UNSURE resolution: 25 Y + 43 N + 136 still UNSURE; Total L2 Y updated 510→535; pool updated v4/480→v5/505 |
| v2.5 | 19/05/2026 | R5 title-only: 4Y + 11N; R6 title-only: 8Y + 46N; Total L2 Y: 550→562; worklist v7→v8 (524→532); UNSURE: 87→18 |
| v2.6 | 19/05/2026 | EN manuscript synced to R6/v8 counts |
| v2.7 | 19/05/2026 | R7 manual signals: 0Y + 8N; UNSURE: 18→10 (abstract required); both manuscripts updated |

---

## 7. Tài liệu tham khảo — PRISMA và Methods

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. *Psychological Methods, 19*(2), 211–229. https://doi.org/10.1037/a0032968

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594. https://doi.org/10.3758/s13428-012-0261-6

Suurmond, R., van Rhee, H., & Hak, T. (2017). Introduction, comparison, and validation of Meta-Essentials. *Research Synthesis Methods, 8*(4), 537–553. https://doi.org/10.1002/jrsm.1260

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *British Medical Journal, 315*(7109), 629–634. https://doi.org/10.1136/bmj.315.7109.629

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot–based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455–463. https://doi.org/10.1111/j.0006-341X.2000.00455.x
