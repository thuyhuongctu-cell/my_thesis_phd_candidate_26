# `replication/` — deprecated top-level duplicates removed (2026-06-23)

The scripts that used to live here (`p3_singapore_replication.py`, `p4_vietnam_replication.py`,
`p5_china_replication.py`) and the `p4_vietnam/` output folder were **mislabeled, ephemeral-path
duplicates** (file names and country contents were scrambled vs. the project's P-numbering, and they
read from `/root/.claude/uploads/...` paths that do not exist). They have been **removed**.

Use the **authoritative, path-correct** per-paper runners instead — all read committed raw data from
`data_wbes/raw_dta/` (override with `WBES_RAW`):

| Paper | Context | Runner |
|---|---|---|
| P3 | Vietnam | `p3/replication/do/01_build_vietnam.do` (Stata, authoritative) + `scripts/p3_dai_reproduce.py` |
| P4 | Singapore | `p4/replication/p4_singapore_figs_from_raw.py` (+ `p4/replication/do/`) |
| P5 | China | `p5/replication/python/build_and_run.py` (+ `p5/replication/do/`) |
| P7 | 50 economies | `dist/osf/P7_capstone/code/p7_run_50econ.py` |
| P8 | Pacific SIDS | `p8/replication/build_and_run_p8_7pacific.py` |
| P9 | India | `p9_india/replication/run_pipeline.py` (+ `run_robustness.py`) |
| P10 | Japan | `p10_japan/replication/p10_japan_models.py` |
| Descriptives / correlations | 50-econ canonical | `scripts/relock_descriptives_canonical.py`, `scripts/relock_correlations_canonical.py` |

Cross-validation status: `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`.
