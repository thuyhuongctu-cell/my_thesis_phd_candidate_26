# ⚠️ Stale / divergent P3 result artifacts — flagged for central review

Generated 2026-06-23 alongside the from-raw reproduction in this folder.
**Nothing here is deleted** — listing only, per instruction. Each item below either
contradicts the from-raw reproduction (`estimates.csv` + `REPRO_NOTE.md`) or is a
dead/intermediate output.

## A. Contradicts the from-raw reproduction (resolve before relying on it)

1. `p3/replication/coefs_main_models.csv`
   - Pooled M2 = (FSTSc +0.984, FSTSc2 -1.909). From-raw run gives (+0.733, -1.750)
     and the committed R track gives (+0.661, -2.152). Three different pooled M2
     coefficient sets. Per-wave M2 also differ (e.g. 2009: this file +1.045/-1.774
     vs from-raw +0.575/-1.524).
   - **Load-bearing**: consumed by `generate_p3_figures.py`, the JED submission
     package, and the manuscript. Do NOT delete; it must be re-derived from the
     authoritative Stata build (`do/01_build_vietnam.do` -> `do/02_run_models.do`)
     and the divergence reconciled, OR the figures/manuscript re-pointed to the
     reproduced numbers.

2. README turning-point table (`p3/replication/README.md`, lines ~25-28)
   - Claims per-wave TP 40% / 44% / 46% and pooled 39.7%. From-raw Python (33-37%,
     pooled 34.8%) and committed R (`data/p3_R_turning_points.csv`, pooled 34.5%)
     both land ~5 pts lower. Likely the Stata `b1_d` employment denominator vs the
     `l1` proxy. Needs a Stata run to confirm which the locked manuscript uses.

## B. Likely-stale intermediate outputs (verify, then prune centrally)

3. `p3/replication/data/p3_dai_reproduced.csv`
   - Regenerated cleanly by `scripts/p3_dai_reproduce.py` from raw; consistent with
     this run. Keep, but it is a derived file (not a source) — safe to regenerate.

4. `p3/replication/data/p3_R_coefs.csv`, `p3/replication/data/p3_R_turning_points.csv`
   - R track outputs; AGREE with the from-raw Python on the turning point (good
     cross-check). Keep as corroboration, not stale. Listed here only so the
     reviewer sees the full provenance chain.

## Authoritative-from-raw outputs (this folder)
- `estimates.csv`  — M2 / M4 / M6, per wave + pooled, HC1, built from
  `data_wbes/raw_dta/` via `run_repro.py`.
- `REPRO_NOTE.md`  — headline + match-vs-canonical.
