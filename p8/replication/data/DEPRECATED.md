# Pinned datasets — which to use

## KEEP (current, redesign)
- `p8_7pacific_pinned.csv` — **canonical analytic dataset** for the redesign. 7 genuine
  Pacific SIDS, Timor-Leste excluded; P7 harmonisation (lp_z, fsts_c, fsts_c2, fdi10,
  ln_age, tci_z, dai). Regenerated 2026-06-23 by `build_and_run_p8_7pacific.py`.
  Yields N = 1,450 / 7 clusters and the dissolution result.
- `p8_redesign_fullsample.csv` — redesign full-sample export (level lp + level/z constructs);
  retained as a companion to the pinned file.

## SUPERSEDED (recommend DELETE)
- `p8_sids_pinned_0b288f3.csv` — OLD pinned SIDS dataset (different schema: country/
  ln_labor_prod/dai_z/tci_z, includes pre-redesign harmonisation). Belongs to the −1.339
  FIP build and is superseded by `p8_7pacific_pinned.csv`. Not produced by the live runner.

The β = −1.339 FIP is a superseded limiting case only; the P8 headline is dissolution at
N = 1,450. See `p8/replication/REPRO_2026-06-23/REPRO_NOTE.md`.
