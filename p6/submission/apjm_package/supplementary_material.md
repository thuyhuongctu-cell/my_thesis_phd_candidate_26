# Supplementary Material — P6 (APJM)

## Appendix A, PRISMA 2020 Flow Diagram

> **⚠️ All counts marked \[TBD\] will be confirmed after formal WoS +
> Scopus search.** The diagram below follows PRISMA 2020 (Page et al.,
> 2021).

    IDENTIFICATION
    ─────────────────────────────────────────────────────────────────
    Records from electronic databases (WoS Core Collection + Scopus):
      [n = TBD]
    Records from supplementary methods
      Backward citation scan (5 anchor meta-analyses): [n = TBD]
      Hand-search (author's corpus, 2020–2026): n = 19
      ──────────────────────────────────────
      Total identified: [N = TBD]

    SCREENING, Level 1 (Title / Abstract)
    ─────────────────────────────────────────────────────────────────
    After deduplication: [n = TBD]
      Excluded (title/abstract screen): [n = TBD]
        - Does not examine I→P relationship: [n = TBD]
        - Not firm-level analysis: [n = TBD]
        - Non-English, no convertible ES in abstract: [n = TBD]
        - Qualitative / conceptual only: [n = TBD]
      Retained for full-text review: [n = TBD]

    ELIGIBILITY, Level 2 (Full Text)
    ─────────────────────────────────────────────────────────────────
    Full texts assessed: [n = TBD]
      Excluded: [n = TBD]
        - No effect size convertible to r: [n = TBD]
        - No DOI measure meeting PICO I criterion: [n = TBD]
        - State-owned enterprise / government-controlled sample: [n = TBD]
        - Duplicate sample (smaller/older retained for exclusion): [n = TBD]
        - Meta-analysis or review (not primary study): [n = TBD]
        - Conference paper / thesis / working paper: [n = TBD]

    INCLUDED
    ─────────────────────────────────────────────────────────────────
    Studies included in meta-analysis: k = [TBD]
    Effect sizes coded: K = [TBD]
      (Current working database prior to formal search: k = 237, K = 287)

*The PRISMA checklist (Page et al., 2021) is available from the
corresponding author.*

## Appendix B, Coding Protocol (7 Moderators)

| Moderator | Variable Type | Coding Rule |
|-------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------|
| ICRV regime | Categorical (6 codes) | WGI Rule of Law, 2023 vintage: I \> +0.80; II: 0–+0.80; III: −0.50–0; SIDS: island state; V: \< −0.50 |
| cDAI | Continuous (0–1) | World Bank DAI score or ITU DDI score, country-year, standardized. If unavailable: ITU ICT Development Index (substitute) |
| DPL phase | Categorical (3) | Precede: data year \< 2009; Span: data spans 2005–2014; Follow: data year \> 2014 |
| Country of origin | Categorical (ISO) | First author's sample country; multi-country = "pooled" |
| Industry | Categorical (3) | SIC: manufacturing (20–39), services (40–89), mixed/unspecified |
| DOI measure | Categorical (4) | FSTS; Entropy; Number-of-markets; Transnationality index (UNCTAD) |
| Performance | Categorical (4) | Accounting (ROA/ROE/ROS); Market (Tobin's Q); Mixed; Other |

## Appendix C, Consistency Check: MetaEssentials vs. `metafor`

| Statistic | MetaEssentials 1.5 (ICBEF 2025) | metafor REML (3-level, k=237) |
|-------------------------|---------------------------------|-------------------------------|
| Pooled *r* | 0.070 | 0.074 |
| 95% CI | \[0.050, 0.090\] | \[0.060, 0.088\] |
| *I*²_total | 87.92% | 62.5% |
| *I*²\_(2) within-study |, | 54.1% |
| *I*²\_(3) between-study |, | 8.4% |
| *k* studies | 113 | 237 |
| *K* effects |, | 287 |
| σ²\_(2) |, | 0.00878 |
| σ²\_(3) |, | 0.00136 |
| Software | Suurmond et al. (2017) | Viechtbauer (2010) |

*Note:* Lower total I² in the three-level model (62.5% vs. 87.92%)
reflects the expanded *k* = 237 sample and the three-level structure
that partitions variance across levels correctly. The narrower 95% CI
reflects the precision gain from 237 vs. 113 studies. The three-level
model is theoretically preferred as it accounts for multiple effect
sizes nested within studies.

*Word count (excluding tables, references, appendices): ≈ 6, 900 words*
