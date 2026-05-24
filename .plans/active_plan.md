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

`p6_parse_database.py` parses the human-readable coded markdown
(`p6_study_database_coded.md`) to k=237 / K=287 because that markdown documents
study rows **S01-S237 only**. The 238th study — **S238, Srividhya et al. (2024),
India business groups, FSTS to ROA, r=0.13, n=992** — was added directly to the
analysis CSV (effect E288) from the WoS-arm search. The markdown's own
19/05/2026 update note records this decision. So 237/287 is the markdown-tabulated
subset; 238/288 is the correct analysis count.

Consequence: re-parsing the markdown would drop S238 and regress the dataset to
237/287, which is why `run_mara.sh` no longer parses by default (use `--parse`
only after S238 has been written into the coded markdown tables).

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
