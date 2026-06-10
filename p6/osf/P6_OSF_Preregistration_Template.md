# OSF Pre-Registration — P6 Three-Level Meta-Analysis

**Title:** Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis

> **Registration type:** Secondary-data / meta-analysis registration.
> **Status:** DRAFT — ready to submit to OSF. Insert the OSF URL + DOI + timestamp here after registering, then paste the same identifier into the manuscript Methods §3 and the PRISMA checklist.
> **Transparency disclosure:** Effect-size extraction from the working corpus is already complete. This is therefore a *transparency registration of an analysis plan applied to existing data* (not an a-priori, data-blind pre-registration); this is disclosed honestly here and should be stated as such in the manuscript.
> **Prepared by:** Đỗ Thùy Hương, Can Tho University, Vietnam.

---

## 1. Authors
- **Đỗ Thùy Hương** (corresponding author) — College of Economics, Can Tho University, Vietnam · huongp1323001@gstudent.ctu.edu.vn · ORCID 0000-0002-7711-2487
- **Phan Anh Tú** — College of Economics, Can Tho University, Vietnam · patu@ctu.edu.vn · ORCID 0000-0003-0667-3137

## 2. Research questions
- **RQ1 (Baseline).** What is the pooled internationalization→firm-performance (I→P) effect size (r̄, 95% CI), and how is heterogeneity distributed within vs. between studies (I²₍₂₎, I²₍₃₎) in a three-level model?
- **RQ2 (ICRV).** Do pooled I→P effects vary across **Institutional Context Regime Variation (ICRV)** regimes?
- **RQ3 (cDAI).** Does **country-level Digital Adoption (cDAI, 0–1)** moderate the I→P relationship?
- **RQ4 (DPL).** Does **Digital Paradox Lifecycle (DPL)** phase (temporal) moderate the I→P relationship?
- **RQ5 (Publication bias).** Is the literature affected by selective reporting, and what is the bias-adjusted effect?

## 3. Hypotheses
- **H1 (ICRV between-regime).** Pooled I→P effect sizes vary systematically across ICRV regimes; the between-regime Q_M test is significant (p < .05), with Advanced-regime (ICRV-I) studies expected to show the largest average effect.
- **E1a (exploratory).** Advanced-regime (ICRV-I) studies show the largest pooled effect.
- **E1b (exploratory).** Frontier-regime (ICRV-FR) studies show the smallest (possibly null/negative) effect. Treated as exploratory given small Frontier k.
- **H2 (DPL phase).** Studies drawing predominantly on post-2014 data (Follow phase) show larger pooled I→P effects than pre-2009 (Precede) studies, with Span intermediate; between-phase Q_M significant.
- **H3 (cDAI amplification).** Studies from high-cDAI contexts show larger pooled I→P effects than low-cDAI contexts (between-group Q_M significant), concentrated in the Follow phase.
- **H4 (Publication bias).** Selective reporting inflates the raw pooled effect: (a) funnel asymmetry (Egger, Begg) significant; (b) trim-and-fill yields a smaller but still positive adjusted estimate; (c) Orwin fail-safe N exceeds the negligibility threshold.

## 4. Eligibility criteria (PICOS)
**Include:** firm-level studies (any country / multi-country); internationalization measured by FSTS, degree of internationalization, export intensity, geographic diversification, foreign subsidiaries, or FATA; performance measured by accounting (ROA/ROE/ROS), market (Tobin's Q, returns), or productivity (labour productivity, TFP) indicators; peer-reviewed journal article reporting Pearson r or a statistic convertible to r (standardized β; t with N; F with df₁ = 1).
**Exclude:** country/macro-level unit; qualitative/conceptual/review-only; non-IB disciplinary context; book chapters, dissertations, conference/working papers (no DOI / not peer-reviewed); duplicates (exact DOI or >90% title match + same year); insufficient statistics to compute r.
**Temporal coverage:** January 1977 – March 2026. **Language:** English (Vietnamese where a convertible effect size is confirmed).

## 5. Search strategy
The corpus is assembled through a **systematic but bounded, citation-anchored strategy** rather than an exhaustive database census, and is reported under the PRISMA 2020 "studies identified via other methods" variant. The anchor set is five benchmark meta-analyses (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Arte & Larimo, 2022); their reference lists (backward citation) and forward-citation networks (Google Scholar) are screened. This is **supplemented** by targeted structured queries in Web of Science Core Collection (SSCI/SCI-E/ESCI), Scopus, and specialist databases (ABI/INFORM, Business Source Complete, ScienceDirect, SpringerLink, Emerald Insight, OpenAlex) to check coverage of the citation network — these queries supplement the citation-anchored search rather than constitute a standalone census.

**Supplementary query string (WoS Topic field):**
```
TS=(internationaliz* OR internationalis* OR multinationality OR "degree of internationalization"
    OR "international diversification" OR "geographic diversification" OR "foreign sales" OR FSTS
    OR "foreign assets" OR FATA OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND TS=("firm performance" OR "enterprise performance" OR "corporate performance" OR "financial performance"
    OR "business performance" OR "labor productivity" OR "labour productivity" OR profitability
    OR "Tobin's q" OR "return on assets" OR ROA OR "return on equity" OR "return on sales"
    OR "total factor productivity" OR "firm efficiency")
AND TS=(correlation OR regression OR coefficient OR "effect size" OR "r =")
```
An equivalent Scopus `TITLE-ABS-KEY` string with `DOCTYPE(ar) AND LANGUAGE(english) AND PUBYEAR AFT 1976` is applied. These queries are used to supplement and cross-check the citation-anchored corpus, not as an exhaustive census.

## 6. Screening protocol
The **two authors** independently apply the eligibility criteria in two stages, (L1) title/abstract and (L2) full text, resolving disagreements by discussion following a predetermined rule. Decisions and exclusion reasons are logged for the PRISMA 2020 flow diagram ("studies identified via other methods" variant).

## 7. Data extraction & coding
**Effect-size priority order:** (1) Pearson r (as-is); (2) standardized β → r_partial = β × 0.98 (Peterson & Brown, 2005); (3) t with N → r = √[t²/(t²+df)] (Cohen, 1988); (4) F with df₁ = 1 → r = √[F/(F+df₂)] (Rosenthal, 1994). For multiple effects per study, distinct subsamples are coded as independent effects; for multiple specifications on one sample, the most fully controlled model is retained.

**Moderator coding (aligned to the final manuscript):**

| Moderator | Variable | Coding |
|---|---|---|
| **ICRV — Institutional Context Regime Variation** | `icrv` | 5 regimes from World Bank WGI Rule of Law (2023): **I** Advanced-Innovation (WGI > +0.80); **II** Upper-Middle (0 to +0.80); **III** Emerging (−0.50 to 0); **FR** Frontier/SIDS (≤ −0.50 or small-island state); **MX** Multi-country pooled (no modal regime ≥ 60%) |
| **cDAI — country Digital Adoption Index** | `cdai` | Continuous 0–1: World Bank Digital Adoption Index (2016; Sahay et al., 2020), or ITU Digital Development Index rescaled; assigned by the study's **median data year** |
| **DPL — Digital Paradox Lifecycle phase** | `dpl` | **Precede** (median data year < 2009); **Span** (2005–2014, or unclassifiable); **Follow** (median data year ≥ 2015) |
| Internationalization measure | `doi_type` | FSTS / geographic-diversification / export-ratio / composite / FDI / other |
| Performance measure | `fp_type` | accounting / market / labour-productivity / mixed |
| Effect-size estimation | `is_estimated` | 1 = converted from t/F/β; 0 = directly reported r |

**Inter-coder reliability:** a 20% stratified subsample (by ICRV regime, DPL phase, DOI type) is independently double-coded; **Cohen's κ ≥ 0.70** for categorical moderators and **ICC(2,1) ≥ 0.80** for continuous cDAI; disagreements resolved by PI adjudication.

## 8. Statistical analysis plan
**Software:** R (≥ 4.3), `metafor` (Viechtbauer, 2010). All r are Fisher-z transformed for analysis and back-transformed for reporting.

**Baseline three-level model** (effects nested in studies):
```r
dat <- escalc(measure="COR", ri=r, ni=n, data=db)
res <- rma.mv(yi, vi, random = ~ 1 | study_id/effect_id, data=dat, method="REML")
# Outputs: pooled r̄ [95% CI]; σ²(2), σ²(3); I² total, I²(2), I²(3); Q_E, Q_M
```
**Moderator tests** (Q_M omnibus; Holm–Bonferroni for pairwise ICRV):
```r
rma.mv(yi, vi, mods = ~ factor(icrv), random = ~ 1|study_id/effect_id, data=dat)  # H1
rma.mv(yi, vi, mods = ~ factor(dpl),  random = ~ 1|study_id/effect_id, data=dat)  # H2
rma.mv(yi, vi, mods = ~ cdai,         random = ~ 1|study_id/effect_id, data=dat)  # H3
```
**Publication bias (H4):** Egger's regression; Begg & Mazumdar rank correlation; Duval & Tweedie trim-and-fill; Orwin fail-safe N; PET-PEESE.
**Sensitivity / robustness:** two-level vs three-level comparison; leave-one-out (Cook's distance > 4/k); FSTS-only restriction; ICRV reclassified on the WGI composite governance index; post-2000 temporal restriction; directly-reported-r-only restriction.

## 9. Reporting standards
PRISMA 2020 (Page et al., 2021) full flow diagram; APA Meta-Analysis Reporting Standards (Cooper, 2010); forest + funnel plots.

## 10. Data availability
- Coded study database: `p6/data/p6_study_database.csv` (288 effects, 238 studies).
- Analysis scripts: `p6/tools/meta_r_scripts/` and `p6/replication/` (GitHub).
- Extraction tool: M-AIDA (`p6/tools/maida/`) — LLM-assisted extraction under 100% PI verification + data lock (disclosed in the manuscript's AI-use statement).
- PRISMA checklist: `p6/p6_prisma_checklist.md`.

## 11. Conflicts of interest / funding
None declared. No specific grant from any public, commercial, or not-for-profit funding agency.

---

## How to register on OSF (≈15–20 min)
1. Sign in at **https://osf.io** → **Create new project**: "P6 I→P Meta-Analysis: ICRV, cDAI, DPL Moderators".
2. Upload this file + the coded database + the R scripts to the project's **Files**.
3. Open the **Registrations** tab → **New registration** → choose **"Open-Ended Registration"** (or "Preregistration") template.
4. Paste sections 1–11 above into the form.
5. **Submit.** OSF time-stamps and locks the registration and issues a URL + DOI (e.g., `https://osf.io/XXXXX`, `10.17605/OSF.IO/XXXXX`).
6. Paste that URL + DOI back into:
   - the header of this file (Status line),
   - the manuscript Methods §3 (replace "registration identifier will be inserted at acceptance"),
   - the data-availability statement and PRISMA checklist.
7. Because the data were already collected, tick/disclose the OSF "data already collected" option so the registration is honest.
