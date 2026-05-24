# Active Plan — P6 Deployment + Cross-Paper Survey

Branch: `claude/papers-6-deploy-skills-2JzRB`
Date: 2026-05-24

## Objective

Deploy Paper 6 (three-level meta-analytic regression, Internationalization to
Firm Performance) so the full analysis pipeline runs reproducibly without R,
and the manuscript figures reflect the real coded database instead of simulated
data. Survey the other papers for completeness gaps.

## What was done (P6)

### 1. Pure-Python MARA port — `p6/scripts/p6_real_mara.py`
The reference analysis lived only in `p6_real_mara.R` (metafor), which cannot
run in CI / Claude Code on the web (no R). Added a pure-Python port using a
per-study Sherman-Morrison REML solver for the three-level model
(`random = ~ 1 | study_id / effect_id`).

Validation against the committed R output (k=238 studies, K=288 effects):

| Output | Status |
|--------|--------|
| `table1_baseline.csv` .. `table5_sensitivity.csv` | **byte-identical** to metafor |
| Pooled r = 0.074 [0.060, 0.088], sigma2 0.00135 / 0.00874, I2 62.4% | exact |
| Q_M(ICRV) = 17.35 (df=4, p=.002) | exact |
| Egger b=0.475, p=.057; Begg tau=-0.134, p=.0007; fail-safe N=45,848 | exact |
| Trim-and-fill (metafor k0=58): adj r = 0.035 | exact |
| Q_M(cDAI)=1.23 vs .34; Q_M(DPL)=0.56 vs .62 | trivial diff, both ns |
| LOO range [0.071, 0.075] vs manuscript [0.071, 0.076] | within rounding |

metafor remains authoritative for reported numbers; the Python port is a
validated reproduction. The one metafor-specific procedure is the trim-and-fill
*count* (L0 iteration), so `TRIMFILL_K0 = 58` is taken from metafor and the
standard fill mechanics reproduce adj r = 0.035.

New figure-driving artefacts: `p6/results/loo_data.csv`,
`p6/results/funnel_imputed.csv`.

### 2. Real-data figures — `p6/scripts/generate_p6_figures.py`
Previously Figures 2-5 used hardcoded simulated values that contradicted the
results tables and the manuscript (e.g. pooled r=0.142 vs the real 0.074, random
funnel points, stale Egger/Begg annotations). Now:
- Fig 2 (ICRV forest) and Fig 3 (DPL) read `table2_icrv.csv` / `table4_dpl.csv`.
- Fig 4 (leave-one-out) reads the real `loo_data.csv`.
- Fig 5 (funnel) plots the 288 real effects + 58 real reflected trim-and-fill
  points from `funnel_imputed.csv`; annotations corrected to Egger b=0.475
  p=.057, Begg tau=-0.134 p=.0007, k=58, adj r=0.035 [0.019, 0.051].
- "Framework validation / simulated data" labels removed.
The stale simulated copy at `p6/figures/generate_p6_figures.py` was replaced
with the canonical real-data script.

### 3. Pipeline runner — `p6/scripts/run_mara.sh`
- Step 1 (markdown to CSV parse) is now non-destructive: it only runs with
  `--parse` or when the CSV is missing, protecting the authoritative
  k=238/K=288 dataset.
- Step 2 falls through R to Docker to the Python port (and checks the Docker
  daemon is actually up before using it).
- Step 3 regenerates figures.

## Study count: 238 / 288 (verified, intentional)

The authoritative dataset is **k = 238 studies, K = 288 effects**
(`p6/data/p6_study_database.csv`). This is identical on `origin/main` and this
branch, and `table1_baseline.csv` (K=288, k=238) matches on both. The manuscript
consistently reports k=238 / K=288.

`p6_parse_database.py` now parses the coded markdown
(`p6_study_database_coded.md`) to **k = 238 / K = 288**: the S238 row
(**Srividhya et al. 2024**, India business groups, FSTS to ROA, r=0.13, n=992,
ICRV=III, cDAI=M, DPL=SPN) was added to the coded table, so the markdown is now
a complete source. Parsing the markdown and running the MARA reproduces
`table1_baseline.csv` .. `table5_sensitivity.csv` **byte-identically** to the
committed authoritative dataset. (The committed
`p6/data/p6_study_database.csv` is left untouched — it keeps the curated effect
id `E288` for S238; the markdown-derived CSV labels it `S238`, which does not
affect any REML result.)

`run_mara.sh` still leaves parsing opt-in (`--parse`) so the curated CSV is not
overwritten by accident, but parsing is now verified safe (reproduces 238/288).

## Cross-paper survey

| Paper | Topic | State |
|-------|-------|-------|
| p1 | Firm performance heterogeneity, WBES (Emerging Asia) | Complete manuscript, **only as .docx** — not in the markdown pipeline |
| p2 | China SMEs (JFAR) | Complete paper, **only as .pdf** — not in the markdown pipeline |
| p3 | Vietnam | Complete: manuscript + full submission package |
| p4 | Singapore | Complete: manuscript + submission + replication |
| p5 | China | Complete: manuscript + submission + design |
| p6 | Meta-analysis (MARA) | Most developed; pipeline deployed here |
| p7 | Capstone | Manuscript + design + data-harmonization protocol |
| p8 | Pacific SIDS | Manuscript + design (thinnest of the source papers) |

### Recommendation for the "missing" papers (p1, p2)
p1 and p2 are finished papers but live only as binary artefacts. To bring them
into the same source pipeline as p3-p8 they need a faithful docx/pdf to markdown
extraction (best done with `pandoc`, which is not installed here). An automatic
lossy text dump would corrupt tables, equations, and citations, so this was not
attempted blindly. Suggested next step: install pandoc and convert to
`p1/p1_..._en_clean.md` and `p2/p2_..._en_clean.md`, then build submission
packages mirroring p3-p5.

## Skills
Per the user's decision, no new skills were installed. The uploaded archives are
mostly software/integration tools (yt-dlp, FinceptTerminal, cybersecurity,
discord/imessage, squad-dev) not suited to academic-paper work; the repo already
carries appropriate academic-writing skills.

## Automated r-extraction for missing studies (v3 tracker)

The "missing studies" are the screened-IN candidates in
`p6/tools/results/fulltext_to_extraction_tracker_v3.csv` (654 marked Y; only ~3
have an effect size, ~651 still need `r`/`n`). Effect sizes must be extracted
from each paper's full text, so they cannot be filled in this session (no PDFs,
no API key, restricted network). Extraction runs as a GitHub Actions workflow.

Fixes made so the extraction loop runs on **this** branch:
- `groq_extract_r.yml`, `claude_api_extract_r.yml`, `mara_run.yml`: replaced the
  hardcoded `claude/edit-vietnamese-academic-standards-xcAmn` checkout/push refs
  with `${{ github.ref_name }}` (run on whatever branch dispatches them).
- Repointed the default inputs from the missing `extraction_queue_pdf_20260522.csv`
  / `oa_manifest_merged.csv` to the present `extraction_queue_y_20260520.csv`
  (654 rows) and `oa_manifest_20260520.csv`.

### How to run it
1. Add repo secret `GROQ_API_KEY` (free at console.groq.com) — or
   `ANTHROPIC_API_KEY` for the Claude-API extractor.
2. GitHub → Actions → **"Groq r-Extraction (P6 — Free API)"** → Run workflow,
   selecting branch `claude/papers-6-deploy-skills-2JzRB`. Start with `limit=50`,
   `dry_run=false`.
3. The job downloads OA PDFs (via the manifest), extracts `r`/`n` with Groq, and
   commits the filled rows back to `fulltext_to_extraction_tracker_v3.csv` on
   this branch. Repeat (increase `limit`) until the backlog is cleared.
4. Merge the tracker into the analysis CSV (`42_merge_tracker_to_database.py`),
   then re-run `p6/scripts/run_mara.sh` (or the `mara_run` workflow) to refresh
   tables/figures.

### Post-extraction runbook (verified, no code changes needed)

The merge → MARA chain was checked end-to-end against the live files:
- The Groq/Claude extractor sets `ready_for_r=1` on every row it fills, so those
  rows become merge-eligible automatically.
- `42_merge_tracker_to_database.py` filters to `decision==Y` + `ready_for_r==1`
  + `converted_r` filled + `seq>435`. Of the 651 studies needing `r`, **605 are
  seq>435 (merge-eligible)**; the 46 with seq≤435 are the original coded corpus
  already in the database and are correctly skipped.
- The 18 columns the merge emits match the database schema exactly (verified), and
  it dedups new rows against the existing k=288 by DOI and author+year, backing up
  `p6_study_database.csv` before writing.

Run, once the tracker has been filled by the extraction workflow:
```bash
# 1. Preview what would merge (no writes)
python3 p6/tools/42_merge_tracker_to_database.py --dry-run

# 2. Merge for real (auto-backs up the DB; guard requires >=50 ready rows)
python3 p6/tools/42_merge_tracker_to_database.py

# 3. Re-run the meta-analysis on the MERGED csv.
#    IMPORTANT: do NOT pass --parse — that regenerates the CSV from the
#    markdown corpus (k=238/K=288) and would discard the merged rows.
bash p6/scripts/run_mara.sh
```

Note: the 8 search/discovery workflows (wos/scopus/semantic_scholar/unpaywall/
doi/abstract/p6_full_search) are still pinned to the old branch; they find new
candidates rather than extract `r`, so they were left untouched for this task.
