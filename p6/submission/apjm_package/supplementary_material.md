# Supplementary Material — P6 (APJM)

## Appendix A, PRISMA 2020 Flow (Studies Identified via Other Methods)

The corpus was assembled through citation-anchored systematic searching
rather than a single database census; the flow is therefore reported
under the PRISMA 2020 "studies identified via other methods" variant
(Page et al., 2021).

    IDENTIFICATION
    ─────────────────────────────────────────────────────────────────
    Studies identified via other methods:
      Backward citation scan (reference lists of 5 anchor meta-analyses)
      Forward citation scan (Google Scholar citing the 5 anchors, post-2022)
      Hand-search (author's corpus, 2020–2026): n = 19
      Supplementary structured queries (WoS, Scopus, specialist
        databases) to check coverage of the citation network

    SCREENING / ELIGIBILITY
    ─────────────────────────────────────────────────────────────────
    Records screened in two stages against the eligibility criteria
    (Section 3.2): title/abstract, then full text. Full-text exclusion
    reasons: no effect size convertible to r; internationalization not
    measured at the firm level; duplicate sample (smaller/older record
    removed); meta-analysis or review rather than a primary study;
    conference paper, thesis, working paper, or book chapter (grey
    literature documented but excluded from the primary model).

    INCLUDED
    ─────────────────────────────────────────────────────────────────
    Studies included in meta-analysis: k = 238
    Effect sizes coded:                K = 288

Because identification proceeded by citation chaining, stage-level
database-census counts (total identified, deduplicated, and per-reason
exclusion tallies) were not maintained as a single database export and
are not reported as such; the synthesized set (k = 238; K = 288) is
fixed and data-backed.

*The PRISMA 2020 checklist (Page et al., 2021) is available from the
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

| Statistic | MetaEssentials 1.5 (ICBEF 2025) | metafor REML (3-level, k=238) |
|-------------------------|---------------------------------|-------------------------------|
| Pooled *r* | 0.070 | 0.074 |
| 95% CI | \[0.050, 0.090\] | \[0.060, 0.088\] |
| *I*²_total | 87.92% | 62.5% |
| *I*²\_(2) within-study |, | 54.1% |
| *I*²\_(3) between-study |, | 8.4% |
| *k* studies | 113 | 238 |
| *K* effects |, | 288 |
| σ²\_(2) |, | 0.00878 |
| σ²\_(3) |, | 0.00136 |
| Software | Suurmond et al. (2017) | Viechtbauer (2010) |

*Note:* Lower total I² in the three-level model (62.5% vs. 87.92%)
reflects the expanded *k* = 238 sample and the three-level structure
that partitions variance across levels correctly. The narrower 95% CI
reflects the precision gain from 238 vs. 113 studies. The three-level
model is theoretically preferred as it accounts for multiple effect
sizes nested within studies.

*Word count (excluding tables, references, appendices): ≈ 6, 900 words*
