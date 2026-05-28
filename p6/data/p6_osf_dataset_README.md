# P6 Meta-Analysis — OSF Dataset

**File:** `p6_study_database_osf.csv`
**Scope:** Primary-study database for the P6 meta-analysis of the
internationalization → firm-performance relationship (k = 238 studies,
288 effect sizes).

This is the publication copy of `p6_study_database.csv` with authoritative
bibliographic metadata (DOI + provenance) appended.

---

## Data dictionary

| Column | Description |
|--------|-------------|
| `study_id` | Study identifier (S01…S238) |
| `effect_id` | Effect-size identifier within a study |
| `author`, `year` | First author (short form) and publication year |
| `r`, `n` | Correlation effect size and sample size |
| `country`, `sample_start`, `sample_end` | Sample origin and observation window |
| `icrv`, `icrv_std` | Institutional/rule-of-law regime moderator |
| `cdai` | Country-level digital adoption moderator |
| `dpl` | Digital-paradox-lifecycle phase moderator |
| `doi_type`, `fp_type` | Internationalization (DOI) and firm-performance measure types |
| `include_flag`, `is_estimated` | Inclusion flag; whether the effect was estimated/converted |
| `notes` | Coding notes |
| **`doi`** | Resolved DOI (blank if none found yet) |
| **`doi_source`** | Where the DOI came from (`references`, `tracker`, `openalex`, `corpus`, or a `+`-joined combination) |
| **`doi_confidence`** | Trust tier — see below |

## DOI confidence tiers

| Tier | Meaning |
|------|---------|
| `high` | ≥ 2 independent sources agree on the same DOI |
| `medium` | One trustworthy source (the thesis reference list, or an OpenAlex-verified DOI) |
| `review` | Sources disagreed; the thesis reference-list DOI was used. Worth a manual spot-check |
| `suggested` | A single OpenAlex-corpus match (likely correct, not independently confirmed) |
| `none` | No DOI found in any source yet — see `p6_doi_todo_79.csv` |

## Coverage (current)

- **155 / 238 studies carry a DOI** (184 of 288 effect rows).
  - high 22 · medium 74 · review 42 · suggested 21
- **79 studies pending** — listed in `p6_doi_todo_79.csv` for manual completion.
  Many are recent working papers, books, or dissertations that may legitimately
  have no DOI.

## How DOIs were resolved

DOIs were **verified, never invented.** Four independent sources were matched to
each study by exact first-author surname + year (±1) and cross-validated:

1. **Thesis reference list** (`thesis_references_apa7.md`, 191 DOIs) — the
   authoritative bibliography.
2. **Full-text extraction tracker** (`tools/results/fulltext_to_extraction_tracker_v3.csv`,
   2,074 DOIs) — the studies actually screened/extracted.
3. **OpenAlex API verification** (`p6_openalex_enriched.csv`) — DOI lookup +
   author/year/title checks; run on CI (sandbox blocks the API). See
   `tools/README_openalex.md`.
4. **OpenAlex topic-corpus exports** (`tools/results/openalex_corpus*`) — works
   matched by author + year, confirmed by title overlap.

Pipeline scripts: `tools/60_enrich_openalex_metadata.py` (verify/enrich),
`tools/63_match_corpus_dois.py` (corpus match), `tools/64_resolve_dois.py`
(consolidate + cross-validate), `tools/61_merge_openalex_into_database.py`
(build this dataset). Per-study provenance detail: `p6_doi_resolved.csv`.

## Reproduce

```bash
python3 p6/tools/64_resolve_dois.py \
  --db p6/data/p6_study_database.csv \
  --references p6/data/thesis_references_apa7.md \
  --tracker p6/tools/results/fulltext_to_extraction_tracker_v3.csv \
  --enriched p6/data/p6_openalex_enriched.csv \
  --corpus-matches p6/data/p6_corpus_matches.csv \
  --out p6/data/p6_doi_resolved.csv
```
