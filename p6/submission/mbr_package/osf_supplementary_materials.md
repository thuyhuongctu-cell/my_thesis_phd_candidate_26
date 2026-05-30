# OSF Supplementary Materials

**Manuscript:** Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis

**OSF project:** https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN)

**Authors:** Đỗ Thị Thúy Hương; Phan Anh Tú

This document collects the methodological appendices and secondary tables migrated from the main manuscript to meet the MIR word-count envelope. The main manuscript references each item by tag (Supp-A, Supp-B, Supp-C, Supp-T1, Supp-T2, Supp-T3).

---

## Supp-A. PRISMA 2020 Flow Diagram and Screening Trace

> **This flow documents two paths. Path A — the analyzed corpus (k = 238 studies, K = 288 effect sizes) assembled via backward/forward citation tracking of the anchor meta-analyses and hand-search; extraction COMPLETE. Path B — a Web of Science + Scopus database search (20 May 2026); 785 Y records identified through 8-round L2 screening, with 547 records pending full-text extraction (scheduled for revision/Round 2). Path B records are NOT part of the analyzed effects in the current article.**
> Follows PRISMA 2020 (Page et al., 2021). Numbers marked ✓ are confirmed against tracker v3 (snapshot 30 May 2026). Path A (analyzed corpus): supplementary records screened $\approx$ 497 (backward citation scan of anchor meta-analyses $\approx$ 478 + hand-search n = 19) to included k = 238, K = 288. **See `figure_prisma_2020_flow.png` (manuscript Figure 7) for the visual two-path diagram and `prisma_extraction_pipeline_status.md` for the current Path-B extraction-pipeline status report.**

```
IDENTIFICATION
─────────────────────────────────────────────────────────────────
Records from electronic databases (full search, 20 May 2026):
  Web of Science Core Collection (SSCI+SCI-E+ESCI): n = 2,180 ✓
  Scopus (All Subject Areas, 1977–2026):             n = 1,083 ✓
  ─────────────────────────────────────────────────────
  Total from databases:                              n = 3,263 ✓

After cross-database deduplication (DOI-exact + title-fuzzy $\geq$ 85%):
  Duplicate records removed:                         n =   795  ✓
  Unique records:                                    n = 2,468  ✓
  Already in existing tracker (prior database):      n =   435  ✓
  New candidates for L2 screening:                   n = 2,032  ✓
    — with DOI (CrossRef enriched, 20 May 2026):     n = 1,512 (74.4%) ✓
    — no DOI (manual retrieval required):            n =   520 (25.6%) ✓

Records from supplementary methods:
  Backward citation scan (5 anchor meta-analyses):  n $\approx$ 478 screened
  Hand-search (author corpus, 2024–2026):           n = 19
  ─────────────────────────────────────────────────────
  Total records identified:                         N = 3,263 (databases) + $\approx$ 497 (supplementary) ✓

SCREENING — Level 1 (Title / Keyword Pre-screen)
─────────────────────────────────────────────────────────────────
After within-WoS deduplication:                      n = 2,179  (1 duplicate removed)
  Excluded at L1 (title clearly outside I-P domain): n = 1,397
    - No internationalization × performance signal  : n $\approx$ 1,200
    - Systematic reviews / meta-analyses            : n $\approx$   97
    - Qualitative / conceptual / medical            : n $\approx$  100
  Retained for Level-2 title screen:                 n =   782  ✓

SCREENING — Level 2 (Title Screen + UNSURE Resolution)
─────────────────────────────────────────────────────────────────
Records screened at L2 (title):                      n =   782
  Initial decisions (18 May 2026):
    Y (clearly eligible):                            n =   345
    N (clearly excluded):                            n =    35
      E1: Conceptual / editorial                     n =     4
      E2: Qualitative / case study                   n =     8
      E3: Macro-level / country-level analysis       n =     6
      E5: Export as DV (not internationalization-to-performance)          n =    17
    UNSURE (title insufficient):                     n =   402

  UNSURE title-only re-screen — Round 1 (script 14):
    Resolved Y:                                      n =   135
      Genuinely new (not in existing k=287):         n =   129  ✓
      Duplicates of existing database:               n =     6 to excluded
    Resolved N:                                      n =     3
    Still UNSURE after R1:                           n =   263

  UNSURE title-only re-screen — Round 2 (script 18, two-tier rules):
    Resolved Y (all genuinely new):                  n =    30  ✓
    Resolved N:                                      n =    29
    Still UNSURE after R2:                           n =   204

  UNSURE title-only re-screen — Round 3 (script 20, extended patterns):
    Resolved Y (all genuinely new):                  n =    25  ✓
    Resolved N:                                      n =    43
    Still UNSURE after R3:                           n =   136

  UNSURE title-only re-screen — Round 4 (script 22, capital structure / location
      strategy / antecedent/determinant exclusions; performance consequences /
      optimal multinationality / crisis resilience inclusions):
    Resolved Y (all genuinely new):                  n =    15  ✓
    Resolved N:                                      n =    34
    Still UNSURE:                                    n =    87

  UNSURE title-only re-screen — Round 5 (first-author manual pass, 19/05/2026):
    Resolved Y (all genuinely new):                  n =     4  ✓
    Resolved N:                                      n =    11
    Still UNSURE:                                    n =    72

  UNSURE title-only re-screen — Round 6 (first-author manual pass, 19/05/2026):
    Resolved Y (all genuinely new):                  n =     8  ✓
    Resolved N:                                      n =    46
    Still UNSURE:                                    n =    18

  UNSURE title-only re-screen — Round 7 (manual signals: book-chapter DOI,
      single-case, antecedent-DV, non-business journal, macro unit):
    Resolved Y:                                      n =     0
    Resolved N:                                      n =     8
    Still UNSURE:                                    n =    10

  UNSURE WebSearch abstract pass — Round 8 (19/05/2026, I-P eligibility
      criteria applied via web-sourced abstracts for all 10 remaining):
    Resolved Y (S0129, S0240, S0683):                n =     3
    Resolved N (wrong I measure/DV/focal unit):      n =     7
    Still UNSURE:                                    n =     0  (all resolved) ✓

  Total L2 Y (WoS arm):                             n =   565  ✓
    (= 345 L2 Y + 135 R1 + 30 R2 + 25 R3 + 15 R4 + 4 R5 + 8 R6 + 0 R7 + 3 R8)

  Extraction pre-screen — Round 9 (worklist v11 to v12, 19/05/2026,
      title-pattern analysis for 92 unresolved prescreen flags):
    Y (include for extraction):                       n =    41  ✓
    N (exclude from extraction priority):             n =    51
    Still UNSURE:                                     n =     0  (all resolved) ✓
  Extraction pool prescreen: Y=435 (81.3%), N=100 (18.7%), UNSURE=0

ELIGIBILITY — Deduplication vs. Prior Database
─────────────────────────────────────────────────────────────────
Deduplicated against existing k=287 coded studies:
  Confirmed genuinely new (R1):                      n =   321  ✓
  Confirmed new (R1-R8):                             n =   214  (129+30+25+15+4+8+0+3)
  Active extraction pool (worklist v12):             n =   535  ✓
  Priority extraction candidates (prescreen Y):      n =   435  (310 with DOI; 125 no-DOI)
  Full-text excluded (Path B expansion — screening ongoing): reasons:
    - No calculable r or convertible statistic
    - Unit of analysis not firm-level
    - Conference paper / thesis / working paper
    - Duplicate sample

NEW CANDIDATES (20 May 2026 full search, pending L2 screening):
─────────────────────────────────────────────────────────────────
  New candidates added to tracker v3:               n = 2,032  ✓
    1_DOI_FIRST (CrossRef DOI recovered):            n = 1,512  ✓
    2_NO_DOI_MANUAL (title/GS search required):      n =   520  ✓
  Working file:  fulltext_to_extraction_tracker_v3.csv
                 (2,467 rows = 435 prior + 2,032 new; 58 cols)
  Status: L2 full-text screening pending (OSF pre-registration confirmed)

INCLUDED
─────────────────────────────────────────────────────────────────
Studies included in meta-analysis:   k = 238 (prior DB: k = 238; updated 23/05/2026)
Effect sizes coded:                  K = 288 (prior DB: K = 288; updated 23/05/2026)

Note: k=238 / K=288 reflects the existing coded database (p6_study_database_v2.csv).
Final k/K will increase further as new L2 extraction from 2,032 new candidates
(fulltext_to_extraction_tracker_v3.csv) is completed.
```

*The PRISMA checklist (Page et al., 2021) is available from the corresponding author.*

---

## Supp-B. Coding Protocol (7 Moderators)

| Moderator | Variable Type | Coding Rule |
|-----------|-------------|-------------|
| ICRV regime | Categorical (6 codes) | WGI Rule of Law, 2023 vintage: I > +0.80; II: 0–+0.80; III: −0.50–0; FR: < −0.50; SIDS: Pacific island state (≡ Regime VI, k = 0 in corpus); MX: multi-country (≥ 2 regimes) |
| cDAI | Continuous (0–1) | World Bank DAI score or ITU DDI score, country-year, standardized. If unavailable: ITU ICT Development Index (substitute) |
| DPL phase | Categorical (3) | By median data year: Precede ≤ 2008; Span 2009–2013; Follow ≥ 2014 |
| Country of origin | Categorical (ISO) | First author's sample country; multi-country = "pooled" |
| Industry | Categorical (3) | SIC: manufacturing (20–39), services (40–89), mixed/unspecified |
| DOI measure | Categorical (4) | FSTS; Entropy; Number-of-markets; Transnationality index (UNCTAD) |
| Performance | Categorical (4) | Accounting (ROA/ROE/ROS); Market (Tobin's Q); Mixed; Other |

---

## Supp-C. Consistency Check: MetaEssentials vs. `metafor`

| Statistic | MetaEssentials 1.5 (ICBEF 2025) | metafor REML (3-level, k=238) |
|-----------|----------------------------------|-------------------------------|
| Pooled *r* | 0.070 | 0.074 |
| 95% CI | [0.050, 0.090] | [0.060, 0.088] |
| *I*²_total | 87.92% | 87.8% |
| *I*²_(2) within-study | — | 76.1% |
| *I*²_(3) between-study | — | 11.8% |
| *k* studies | 113 | 238 |
| *K* effects | — | 288 |
| σ²_(2) within-study | — | 0.00874 |
| σ²_(3) between-study | — | 0.00135 |
| Software | Suurmond et al. (2017) | Viechtbauer (2010) |

*Note:* The three-level total *I*² (87.8%) is essentially identical to the single-level ICBEF 2025 estimate (87.92%); the three-level model's contribution is therefore not a lower total but the correct *partition* of that heterogeneity into within-study (Level 2, *I*²_(2) = 76.1%) and between-study (Level 3, *I*²_(3) = 11.8%) components, which a single-level model cannot separate. *I*² is computed with the Higgins–Thompson typical-variance estimator as implemented for multilevel models in `metafor`. The narrower 95% CI reflects the precision gain from 238 vs. 113 studies. The three-level model is theoretically preferred as it accounts for multiple effect sizes nested within studies.

---

## Supp-T1. Detailed Eligibility Criteria (migrated from §3.2)

| Criterion | Inclusion | Exclusion |
|-----------|-----------|-----------|
| Population | Private-sector firms with measured internationalization and financial performance | State-owned enterprises (government equity > 50%); financial sector (SIC 6000–6999); wholly domestic firms |
| Internationalization operationalization | FSTS (foreign sales-to-total sales), entropy index, count of foreign markets, transnationality index (UNCTAD), or FDI-to-total-investment ratio | Purely binary presence/absence; purely qualitative assessments |
| Performance operationalization | Accounting-based (ROA, ROE, ROS); market-based (Tobin's Q, stock returns); productivity-based (labor productivity, TFP) | Narrative or purely ordinal ratings; non-financial-only indices |
| Effect size extractability | Correlation *r*; regression β (convertible to *r*_partial via Peterson & Brown, 2005); *t*-statistic with *df*; *F*-statistic with *df*₁ = 1 | SEM path loadings without *SE*; qualitative case studies; simulation studies; theoretical derivations without data |
| Language | English; Vietnamese | Other languages unless the abstract confirms a convertible effect size |
| Region | Any region; ICRV regime assigned globally using World Bank WGI Rule of Law (2023 vintage) | — |
| Publication type | Peer-reviewed journal articles; articles in press with DOI | Doctoral dissertations, theses, working papers, conference papers, book chapters, unpublished manuscripts, institutional reports |

---

## Supp-T2. cDAI Subgroup Results (migrated from §4.4)

| cDAI Group | *k* | *r̄* | 95% CI | Δ vs. Low |
|-----------|-----|-----|--------|-----------|
| Low | 174 | 0.075 | [0.056, 0.094] | — |
| Medium | 76 | 0.065 | [0.038, 0.091] | b = −0.010, *p* = .489 |
| High | 38 | 0.091 | [0.052, 0.129] | b = +0.016, *p* = .469 |

Omnibus *Q*_M(cDAI) = 1.23, *df* = 2, *p* = .541; H3 not supported.

---

## Supp-T3. DPL Phase Subgroup Results (migrated from §4.5)

| DPL Phase | Definition | *k* | *r̄* | 95% CI | Δ vs. PRE |
|-----------|-----------|-----|-----|--------|-----------|
| Precede (PRE) | Median data year ≤ 2008 | 100 | 0.082 | [0.057, 0.107] | — |
| Span (SPN) | Median data year 2009–2013 | 108 | 0.069 | [0.046, 0.091] | b = −0.013, n.s. |
| Follow (FOL) | Median data year ≥ 2014 | 80 | 0.073 | [0.046, 0.100] | b = −0.009, n.s. |

Pairwise: PRE vs. FOL (*z* = 0.46, *p* = .645); PRE vs. SPN (*z* = 0.78, *p* = .434); FOL vs. SPN (*z* = 0.28, *p* = .782).

Omnibus *Q*_M(DPL) = 0.56, *df* = 2, *p* = .755; H2 not supported.

---

## Supp-T4. Detailed Robustness Checks (migrated from §4.7)

| Check | K | *r̄* | 95% CI | Note |
|-------|---|-----|--------|------|
| Main analysis | 288 | 0.074 | [0.060, 0.088] | Baseline |
| Confirmed *r* only (exclude estimated) | 241 | 0.077 | [0.060, 0.094] | Consistent |
| Exclude *n* < 30 | 286 | 0.074 | [0.059, 0.088] | Consistent |
| ACC performance only | 247 | 0.075 | [0.060, 0.091] | Consistent |
| FSTS DOI measure only | 138 | 0.061 | [0.042, 0.079] | Attenuated but positive |
| DL estimator (two-level) | 288 | 0.074 | [0.061, 0.087] | Δ*r* < 0.01 vs. three-level |
| Leave-one-out range | 288 | [0.071, 0.075] | — | 0/288 change direction |
| ICRV omnibus, drop Frontier | 285 | — | — | *Q*_M = 1.49 (*df* = 3, *p* = .68); full-sample *Q*_M = 17.35 carried by FR (*K* = 3) |

---

## Supp-T5. Detailed §3.2 PRISMA Screening Narrative (migrated from §3.2)

After cross-database deduplication: *n* = 2,468 unique records (795 duplicates removed); 435 already in existing tracker; 2,032 new candidates for L2 screening (1,512 with DOI via CrossRef enrichment; 520 requiring manual full-text retrieval). After automated within-WoS deduplication: *n* = 2,179 (1 duplicate removed). Level-1 keyword pre-screen: *n* = 782 advanced to Level-2; *n* = 1,397 excluded.

Level-2 title screen of 782 records (18 May 2026) yielded 345 Y, 35 N, 402 UNSURE. The UNSURE pool was resolved across eight rule-based and manual passes:

- Round 1 (script `14`, two-tier rules): 135 Y resolved (129 new after dedup vs. existing *k* = 287; 6 duplicates), 3 N, 263 still UNSURE.
- Round 2 (script `18`, hard antecedent/theory exclusions before I-P detection): 30 Y, 29 N, 204 UNSURE.
- Round 3 (script `20`, extended HARD_EXCL/STRONG_INCL patterns: innovation-as-DV, employment/macro DVs, born-global theory, survival/growth INCL): 25 Y, 43 N, 136 UNSURE.
- Round 4 (script `22`, capital structure / location strategy / antecedent exclusions; performance consequences / optimal multinationality / crisis resilience inclusions): 15 Y, 34 N, 87 UNSURE.
- Round 5 (first-author manual pass, 19 May 2026: born-global-as-DV, determinants-of-exporting, EO-as-DV, health/psychology journals exclusions): 4 Y, 11 N, 72 UNSURE.
- Round 6 (manual pass): 8 Y, 46 N, 18 UNSURE.
- Round 7 (manual signals — book-chapter DOI, single-case, antecedent-DV, non-business journal, macro unit): 0 Y, 8 N, 10 UNSURE.
- Round 8 (WebSearch-assisted abstract pass): 3 Y (S0129 India Born-Global I-P M-curve; S0240 SME internationalization speed to performance with organizational learning mediator; S0683 Latin American EMNEs multinationality with business group diversification moderator), 7 N (wrong I measure / DV / focal unit), 0 UNSURE — all resolved.

Total L2 Y (WoS arm) = 565 (= 345 + 135 + 30 + 25 + 15 + 4 + 8 + 0 + 3). Active extraction pool: 535 reviewed; eligible for extraction = 435 (rule-based pre-screen v5: Y = 435 [81.3%], N = 100 [18.7%], UNSURE = 0). Canonical working file: `fulltext_to_extraction_tracker_v3.csv` (2,467 rows × 58 cols). Status snapshot (21 May 2026): Y = 674, N = 728, UNSURE = 1,065 pending Semantic Scholar abstract retrieval; ready_for_r = 3 (sequences 477, 1549, 1753). ICRV auto-coding via affiliation detection (`51_icrv_from_s2_affiliations.py`) resolved 17 of 370 blank-ICRV Y papers; 267 remain pending manual assignment or full-text review.

The analyzed corpus for the present article is *k* = 238 / *K* = 288 from anchor-meta-analysis citation tracking and hand-search; the database-search screening above belongs to a pre-registered expansion whose full-text extraction is ongoing and is not part of the analyzed effects.

---

## Supp-T6. Path B Extraction Pool — Composition (snapshot 30 May 2026)

### Year distribution of 785 Y records pending or partially complete
| Period | Count | Pct |
|---|---|---|
| < 1990 | 5 | 0.6% |
| 1990–1999 | 12 | 1.5% |
| 2000–2009 | 105 | 13.4% |
| 2010–2019 | 326 | 41.5% |
| 2020–2026 | 337 | 42.9% |

The pending pool is concentrated in the 2010–2026 window (84.5%), which would substantially strengthen DPL Follow-phase representation (currently *K* = 80) and Span-phase representation (currently *K* = 108) once extracted.

### Preliminary ICRV classification (affiliation auto-detection only)
| ICRV code | Count | Note |
|---|---|---|
| 0 (unclassified, pending manual review) | 389 | Largest group; requires sample-country verification |
| 1 (Advanced-Innovation) | 181 | Would add to current Path A *K* = 139 |
| 2 (Upper-middle) | 139 | 5.5× expansion potential vs. current *K* = 25 |
| 3 (Emerging) | 67 | Would add to current Path A *K* = 91 |
| 6 (Pacific SIDS) | **6** | **Currently *K* = 0 in Path A — most consequential** |
| 4 (Frontier/LDC) | 3 | Currently *K* = 3 in Path A |

The Pacific-SIDS auto-detection of 6 records is the most consequential preliminary finding: it suggests the SIDS regime (currently *K* = 0) may be populatable, directly addressing the manuscript's §5.4 (a)(1) limitation.

### Top journals in pending Y pool (n = 15)
| Journal | n |
|---|---|
| International Business Review | 28 |
| Management International Review | 18 |
| Journal of International Business Studies | 15 |
| Journal of Business Research | 14 |
| Global Strategy Journal | 13 |
| Journal of International Management | 12 |
| Multinational Business Review | 12 |
| Journal of World Business | 11 |
| International Marketing Review | 11 |
| European Journal of International Management | 11 |
| International Journal of Emerging Markets | 10 |
| Review of International Business and Strategy | 10 |
| Thunderbird International Business Review | 10 |
| Strategic Management Journal | 10 |
| Journal of Korea Trade | 9 |

These are the field's anchor IB journals; their inclusion would substantially raise corpus quality and quartile mix at Round 2.

### Full-text retrieval status
| Status | Count | Pct of 785 Y |
|---|---|---|
| Records with DOI (auto-fetch eligible) | 741 | 94.4% |
| PDFs retrieved locally | 133 | 16.9% |
| Extraction-ready data populated | 27 | 3.4% |
| **Pending full-text extraction (785 Y minus 238 Path A overlap)** | **547** | 69.7% |

### Estimated effort to complete Path B extraction
| Estimate | Value |
|---|---|
| Records pending | 547 |
| Per-paper effort (effect size + 7 moderators + double-entry) | 30–60 min |
| Total reviewer-hours | 270–550 hours |
| Single reviewer @ 20 h/week | 14–28 weeks (~3–6 months) |
| With inter-coder reliability (20% double-coded, Cohen's κ ≥ 0.70) | + 1 month |

### Implication for current submission
At Round 2 with Path B extraction complete, *k* would plausibly rise from 238 to ~600–700 (if 60–70% of pending records survive full-text review), powering definitive tests of (i) H1 ICRV gradient with a populated Frontier/SIDS cell, (ii) H4 publication-bias estimate at scale, and (iii) the cDAI × DPL interaction at higher per-cell density.

---

## Supp-M. Extended Methodological Notes (migrated from §3.5–§3.7)

### Three-Level Model Specification (full details)

**Level 1, sampling error.** *r*_ij = θ_ij + e_ij, e_ij ~ N(0, v_ij), where *v*_ij is the known conditional sampling variance of the Fisher-transformed correlation *z*_ij, computed from study-reported *N*_ij as *v*_ij ≈ 1/(*N*_ij − 3) (Borenstein et al., 2021).

**Level 2, within-study heterogeneity.** θ_ij = δ_j + u_ij, u_ij ~ N(0, σ²_(2)), where σ²_(2) captures residual variation among effect sizes within a study (different samples, subgroups, or model specifications reported in the same paper).

**Level 3, between-study heterogeneity and moderation.** δ_j = μ + **X**_j **β** + w_j, w_j ~ N(0, σ²_(3)), where **X**_j is the (*J* × *p*) matrix of study-level moderators (ICRV regime dummy vector [*d*_I, *d*_II, *d*_III, *d*_SIDS, with Regime V as reference]; continuous cDAI score; DPL phase dummy vector [*d*_Span, *d*_Follow, with Precede as reference]; plus four standard controls), **β** is the (*p* × 1) coefficient vector of primary interest, and *w*_j is the residual between-study variance component.

Parameters are estimated by Restricted Maximum Likelihood (REML) using `rma.mv` in `metafor` v4 (Viechtbauer, 2010), with the variance-covariance matrix for multiple effects within studies specified as compound-symmetric. REML is preferred over full ML because it produces unbiased variance component estimates when *k* is moderate relative to *p* (Raudenbush & Bryk, 2002, p. 39). All Pearson's *r* are transformed to Fisher's *z* prior to analysis and back-transformed for reporting.

Heterogeneity decomposition follows Cheung (2014, eq. 15):
*I*²_(2) = σ̂²_(2) / [σ̂²_(2) + σ̂²_(3) + v̄] × 100%;
*I*²_(3) = σ̂²_(3) / [σ̂²_(2) + σ̂²_(3) + v̄] × 100%,
where v̄ is the average sampling variance across all *K* effects.

The omnibus *Q*_M statistic on *p* − 1 degrees of freedom tests whether between-regime or between-phase variance exceeds sampling-error expectation. Pairwise regime comparisons use Holm–Bonferroni correction. For continuous cDAI, *β*_cDAI significance is assessed by two-sided Wald *z*-test.

### Publication Bias Tests (full details)

Four complementary tests follow Borenstein et al. (2021, ch. 30) and Vevea and Woods (2005): (1) Egger's weighted regression (intercept tests funnel-plot asymmetry); (2) Begg and Mazumdar's rank correlation (non-parametric, less outlier-sensitive); (3) Duval and Tweedie's trim-and-fill (imputes missing left-side studies, re-estimates pooled effect); (4) Orwin's fail-safe *N* (number of null-effect studies required to push pooled *r* below the *r* = 0.10 practical-significance threshold; Rosenthal's 5*k* + 10 criterion). PET-PEESE meta-regression (Stanley & Doucouliagos, 2014) is applied as a model-based correction: PET regresses effect on standard error; if significant, PEESE substitutes squared standard error.

### Robustness Check Specifications

Five pre-registered checks: (1) two-level vs. three-level comparison (Δr > 0.02 would indicate nesting bias); (2) leave-one-out (Cook's distance > 4/*k* flags influential studies); (3) DOI operationalization restriction (FSTS-only sub-sample); (4) ICRV alternative classification (WGI Rule of Law replaced by WGI composite governance index, same percentile thresholds); (5) temporal restriction (post-2000 sub-sample, *k* ≈ 180, to test vintage confounding of DPL phase).
