---
name: p6-openalex-enrich
description: >
  Verify, enrich, and publish DOI/metadata for the P6 meta-analysis study
  database (k=238) using OpenAlex. Use this skill when the user wants to:
  enrich or verify DOIs, look up metadata (journal, year, citation count, OA
  status) from OpenAlex, build a manual DOI-review sheet, produce the OSF
  publication dataset, or asks about p6 enrichment / "làm giàu metadata" /
  "xác minh DOI" / "tạo bảng review DOI" / "dataset OSF". Covers the three
  pipeline tools (60 enrich, 61 merge→OSF, 62 review sheet) and the GitHub
  Actions workflow that runs the network step. Vietnamese + English.
---

# P6 OpenAlex Metadata Enrichment

Verify the P6 study database's candidate DOIs against the live OpenAlex API,
enrich with authoritative metadata, flag disagreements for manual review, and
emit an OSF-publication dataset. **Never invent a DOI** — only record what
OpenAlex returns, and flag every mismatch.

## Key constraint: the network step runs on CI, not in the sandbox

`api.openalex.org` is blocked inside the Claude Code sandbox (HTTP 403, host not
in allowlist). So **step 1 (enrichment) runs on GitHub Actions**; steps 2–3
(merge, review sheet) are offline and run locally.

## Pipeline

| Step | Tool | Where | Output |
|------|------|-------|--------|
| 1. Enrich | `p6/tools/60_enrich_openalex_metadata.py` | GitHub Actions (`.github/workflows/openalex_enrich.yml`) | `p6/data/p6_openalex_enriched.csv` (+ `.log.jsonl`) |
| 2. Merge → OSF | `p6/tools/61_merge_openalex_into_database.py` | local/offline | `p6/data/p6_study_database_osf.csv` |
| 3. Review sheet | `p6/tools/62_build_review_sheet.py` | local/offline | `p6/data/p6_openalex_review.csv` |

### Step 1 — run enrichment (on CI)
The workflow checks out the working branch, runs `60_…py` over all 238 studies,
and commits the result back to the branch.
- Tell the user to open **Actions → "OpenAlex Metadata Enrich (P6)" → Run workflow**.
- Inputs: `max_studies=0` (all; use a small number like `20` for a smoke test).
- The script is **resumable** (skips `study_id`s already in the output). To force
  a full re-run after changing verification logic, delete
  `p6/data/p6_openalex_enriched.csv` + `.log.jsonl` first.
- Optional repo secret `OPENALEX_API_KEY`; otherwise it uses the polite pool via
  `OPENALEX_MAILTO=huongdt@vlute.edu.vn`.

### Step 2 — build the OSF dataset (offline)
```bash
python3 p6/tools/61_merge_openalex_into_database.py \
  --db       p6/data/p6_study_database.csv \
  --enriched p6/data/p6_openalex_enriched.csv \
  --out      p6/data/p6_study_database_osf.csv
```
Writes a DOI **only** when `verify_status` is `verified` or `title_match`;
mismatches/guesses/not-found get a blank DOI + an `oa_match_status` column, so
the public dataset never carries an unverified DOI.

### Step 3 — build the manual-review sheet (offline)
```bash
python3 p6/tools/62_build_review_sheet.py \
  --enriched p6/data/p6_openalex_enriched.csv \
  --apa      p6/p6_primary_studies_apa7.md \
  --out      p6/data/p6_openalex_review.csv
```
One row per study still needing a human, with candidate vs OpenAlex DOI/title,
the expected APA title, and tap-to-search links (OpenAlex web/API, Google
Scholar) plus blank `correct_doi` / `decision` / `notes` columns.

## verify_status meanings

| status | meaning | action |
|--------|---------|--------|
| `verified` | DOI resolves; year (±1) **and** an author surname match | trust it |
| `title_match` | found by title search (no candidate DOI) | usually fine |
| `doi_mismatch_check` | DOI resolves but author/year disagree → likely wrong/garbled DOI | **review** |
| `author_year_guess` | last-resort author+year search; low confidence | review |
| `not_found` | no candidate DOI/title and no confident match | add a title / find DOI manually |

## Manual review loop
1. After CI run, regenerate the review sheet (step 3) and send it to the user.
2. User fills `correct_doi` + `decision` (keep | replace | no_doi_exists).
3. Fold corrections back into `p6/p6_primary_studies_apa7.md` (the candidate
   source), clear the enriched output, and re-run step 1 for a clean verify pass.
4. Regenerate the OSF dataset (step 2).

## Notes on the matcher (script 60)
- `surname()` strips "et al." and handles `Surname, F.` / `A & B` forms.
- `author_matches()` is diacritic-insensitive (`Çapar`==`Capar`) and matches the
  surname against **any** author on the record — this is what stops false
  `doi_mismatch_check` flags while still rejecting genuinely wrong DOIs.
- The loader backfills a missing `year` column from a `(YYYY)` in the author
  field (a few Group-B rows).
