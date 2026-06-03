# PRISMA 2020 Extraction Pipeline — Status Report

**Manuscript:** Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis

**Snapshot:** 30 May 2026
**Source:** `p6/tools/results/fulltext_to_extraction_tracker_v3.csv` (2,510 rows × 58 columns)

---

## Two-Path Design

This meta-analysis adopts a **two-path PRISMA design** distinguishing the *analyzed corpus* (Path A) from the *expansion pool* (Path B):

| | Path A: Anchor-pool (analyzed) | Path B: Formal database search (expansion) |
|---|---|---|
| Identification method | Backward + forward citation tracking of 5 anchor meta-analyses + hand-search | WoS Core Collection + Scopus systematic search |
| Identification date | Ongoing through May 2024 | 20 May 2026 |
| Records identified | ≈ 497 | 3,263 |
| Screening completed | Yes | Yes (8 rounds, mixed rule-based + manual) |
| Full-text extraction | **COMPLETE** | **IN PROGRESS** |
| Current status | *k* = 238 studies, *K* = 288 effect sizes | 547 records pending extraction; 28 excluded at full-text review |
| Used in current analysis | ✅ Yes — sole basis of the reported MARA | ❌ No — pre-registered for revision/Round 2 |

---

## Path A — Analyzed Corpus (COMPLETE)

| Stage | Count |
|---|---|
| Anchor-MA backward citation scan | ≈ 478 |
| Hand-search (author corpus, 2024–2026) | 19 |
| **Total identified** | **≈ 497** |
| Screened against eligibility criteria (§3.2) | 497 |
| Full-text reviewed and coded | 238 |
| **INCLUDED — studies (k)** | **238** |
| **INCLUDED — effect sizes (K)** | **288** |
| Source countries | 49 economies |

All Path A records have been extracted, double-entry verified, and stored in `p6/data/p6_study_database.csv`.

---

## Path B — Expansion Pool (EXTRACTION IN PROGRESS)

### Identification (20 May 2026)

| Source | Records |
|---|---|
| Web of Science Core Collection (SSCI + SCI-E + ESCI, 1977–2026) | 2,180 |
| Scopus (All Subject Areas, 1977–2026) | 1,083 |
| **Total from databases** | **3,263** |
| Cross-database duplicates removed (DOI-exact + title-fuzzy ≥ 85%) | 795 |
| **Unique records** | **2,468** |

### Screening — Level 1 (Title/Keyword Pre-screen)

| Stage | Count |
|---|---|
| Records after within-WoS dedup | 2,179 |
| Excluded at L1 (title clearly outside I-P domain) | 1,397 |
| **Retained for Level-2** | **782** |

### Screening — Level 2 (Title-Abstract, 8 rounds rule-based + manual)

Tracker decision distribution across all 2,510 processed records:

| Decision | Count | Description |
|---|---|---|
| Y (eligible) | **785** | Carried forward to full-text retrieval |
| N_title | 1,187 | Excluded on title alone (hard-exclusion patterns) |
| N | 352 | Excluded on full-text title-abstract review (generic N reason) |
| N_abstract | 155 | Excluded after Semantic Scholar abstract retrieval |
| N_fulltext | 28 | Excluded after full-text review (Path B full-text sample) |
| UNSURE | 3 | Remaining unresolved |

### Full-Text Retrieval Status

| Status | Count | Pct of Y |
|---|---|---|
| Y records with DOI (auto PDF fetch eligible) | 741 | 94.4% |
| Y records with PDF retrieved locally | 133 | 16.9% |
| Y records with extraction-ready data populated | 27 | 3.4% |
| **Y records pending full-text extraction** | **547** | 69.7% (of 785 Y minus 238 Path A overlap) |

### Pending-Extraction Pool — Composition (785 Y records)

#### Year distribution
| Period | Count |
|---|---|
| < 1990 | 5 |
| 1990–1999 | 12 |
| 2000–2009 | 105 |
| 2010–2019 | 326 |
| 2020–2026 | 337 |

The pending pool is heavily concentrated in the 2010–2026 window (84.5%), which would substantially strengthen DPL Follow-phase representation (currently *K* = 80) and Span-phase representation (currently *K* = 108) if extracted.

#### Preliminary ICRV classification (from affiliation auto-detection)
| Code | Count | Notes |
|---|---|---|
| 0 (unclassified pending manual review) | 389 | Largest group; requires sample-country verification |
| 1 (Advanced-Innovation) | 181 | Would add to current Path A *K* = 139 |
| 2 (Upper-middle) | 139 | Would add to current Path A *K* = 25 (5.5× expansion potential) |
| 3 (Emerging) | 67 | Would add to current Path A *K* = 91 |
| 6 (Pacific SIDS) | 6 | Critical — currently *K* = 0 in Path A |
| 4 (Frontier/LDC) | 3 | Currently *K* = 3 in Path A; small expansion |

The **Pacific SIDS auto-detection of 6 records** is the most consequential preliminary finding: it suggests the SIDS regime (currently *K* = 0) may be populatable, addressing one of the manuscript's explicit limitations (§5.4 (a)(1)).

#### Top journals in pending pool
| Journal | Count |
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

These are exactly the high-quality IB journals that anchor the field; their inclusion would substantially raise the analysed corpus quality and quartile mix.

---

## Estimated Effort to Complete Path B Extraction

Per-paper extraction effort (effect size + 7 moderators + double-entry verification): **30–60 minutes**.

| Estimate | Value |
|---|---|
| Records pending | 547 |
| Total reviewer-hours | 270–550 hours |
| Single reviewer @ 20 h/week | 14–28 weeks (~3–6 months) |
| With inter-coder reliability (20% double-coded, target Cohen's κ ≥ 0.70) | +1 month |

Effort can be reduced by:
1. **Auto-fetch PDFs** for the 741 records with DOI via Unpaywall + OpenAlex + institutional access (requires outbound network, currently blocked in this execution environment but routine in the candidate's local environment)
2. **LLM-assisted extraction** of statistical tables from PDFs (with human verification) — could halve per-paper time
3. **Prioritised triage** — extract Pacific-SIDS (6 records) and Upper-middle (139 records) first, since they have the largest marginal information value for the H1 gradient test

---

## Implications for Current Submission

The current MIR submission is built on **Path A only** (*k* = 238 / *K* = 288), which is:

- **Methodologically self-contained**: Path A's anchor-MA citation tracking + hand-search is a legitimate identification method in its own right (used by Marano et al., 2016; Schwens et al., 2018), not a "preliminary" version of Path B.
- **Pre-registered**: OSF z37kn explicitly registered Path A as the primary analysis and Path B as a planned expansion.
- **Transparently bounded**: Sections 5.4 and 6 of the manuscript flag the Frontier (*K* = 3) and SIDS (*K* = 0) underpowering as the principal threat to inference, motivating Path B as a follow-up.

For revision/Round 2 (or a follow-up paper), the Path B extraction would:
- Plausibly raise *k* from 238 to **~600–700** if 60–70% of the 547 pending records survive full-text review
- Strengthen the Pacific SIDS cell (currently *K* = 0 → potentially *K* = 5–6)
- Modestly strengthen Upper-middle (currently *K* = 25 → potentially *K* = 50–100)
- Provide a powered re-test of the H1 ICRV gradient and the H4 publication-bias estimate

---

## Files

| File | Purpose |
|---|---|
| `prisma_status_report.json` | Machine-readable status (counts, percentages) |
| `figures/figure_prisma_2020_flow.png` | Two-path PRISMA flow diagram for inclusion in manuscript/supplementary |
| `osf_supplementary_materials.md` (Supp-A, Supp-T5) | Round-by-round screening trace |
| `p6/tools/results/fulltext_to_extraction_tracker_v3.csv` | Canonical tracker (2,510 rows × 58 cols) |
| `p6/data/p6_study_database.csv` | Path A analysed corpus (238 studies / 288 effect sizes) |

---

## Next Steps (PhD candidate, post-session)

1. **OSF upload**: Lodge this status report alongside `osf_supplementary_materials.md` to OSF project z37kn so reviewers can independently audit the two-path design.
2. **Path B prioritised triage**: Begin full-text extraction with the 6 Pacific SIDS records and the 139 Upper-middle records (highest marginal information value for H1).
3. **DOI enrichment** (when local network access available): Run `p6/tools/07_enrich_doi_crossref.py` + `12_fetch_full_pdfs.py` to bulk-fetch 741 DOI-bearing records.
4. **Inter-coder reliability**: Recruit a second coder for a 20% sub-sample to retroactively compute Cohen's κ on the Path A corpus (addresses Limitation 5 in §5.4).
