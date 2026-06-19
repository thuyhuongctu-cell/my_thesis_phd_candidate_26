# Replication status (2026-06-19)

Convention going forward: replication scripts must read the **committed** raw WBES files in
`data_wbes/raw_dta/` (override with the `WBES_RAW` env var), never ephemeral upload paths.

| Paper | Canonical script | Status | Reproduces headline? |
|---|---|---|---|
| **P5** China | `p5/replication/python/build_and_run.py` | ✅ **fixed** (paths → raw_dta) | ✅ exact (TP 49.37/47.19; N=2610/1934=4544; mfg 42.31/29.65) |
| **P7** 50-econ | `dist/osf/P7_capstone/code/p7_run_50econ.py` | ✅ runnable | ✅ exact (β₁=1.189; TP 51.5%/43.6%) |
| **P4** Singapore (figures) | `p4/replication/p4_singapore_figs_from_raw.py` | ✅ **path fixed** (→ Singapore-2023-full-data.dta) | figures only |
| **P3** Vietnam | `p3/replication/do/01_build_vietnam.do` (+ `scripts/p3_dai_reproduce.py`) | ⚠️ Stata build authoritative | pattern reproduces; exact magnitudes need candidate's Stata (b1_d denominator — see p3_paternoster_zflag note) |
| **P8** SIDS | `p8/replication/reanalysis_7pacific/run_p8_7pacific.py` | ⚠️ **data-version issue** | −1.339 only on pinned 3-economy build (`p8/replication/data/p8_sids_pinned_0b288f3.csv`); see p8_fip_reproduction note |

## Broken / mis-wired scripts (need candidate action)

- **`p4/replication/p4_singapore_replication.py`** — reads **Vietnam** `.dta` (a leftover P3
  template), not Singapore. There is no correct, committed P4 Singapore *model* runner; the
  candidate should commit the authoritative Singapore model script (Stata or Python) that
  reproduces the P4 headline (inverted-U, DAI×FSTS² ≈ +3.119).
- **Top-level `replication/` scripts** (`p3_singapore_replication.py`, `p4_vietnam_replication.py`,
  `p5_china_replication.py`) — file names and country contents are scrambled and reference stale
  upload paths; these duplicate the per-paper scripts and should be reconciled or removed.
- **P9, P10** replication scripts were not path-audited in this pass; recommend the same
  raw_dta convention.

## Recommendation

Before submission/defense, pin each paper's analytic `.dta` (or confirm raw → analytic builds
run from `data_wbes/raw_dta/`) and commit an estimates table per paper so every headline number
is auditable by a reviewer.
