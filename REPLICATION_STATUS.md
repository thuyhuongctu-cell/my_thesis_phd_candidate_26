# Replication status (2026-06-19)

Convention going forward: replication scripts must read the **committed** raw WBES files in
`data_wbes/raw_dta/` (override with the `WBES_RAW` env var), never ephemeral upload paths.

| Paper | Canonical script | Status | Reproduces headline? |
|---|---|---|---|
| **P5** China | `p5/replication/python/build_and_run.py` | ✅ **fixed** (paths → raw_dta) | ✅ exact (TP 49.37/47.19; N=2610/1934=4544; mfg 42.31/29.65) |
| **P7** 50-econ | `dist/osf/P7_capstone/code/p7_run_50econ.py` | ✅ runnable | ✅ exact (β₁=1.189; TP 51.5%/43.6%) |
| **P4** Singapore (figures) | `p4/replication/p4_singapore_figs_from_raw.py` | ✅ **path fixed** (→ Singapore-2023-full-data.dta) | figures only |
| **P3** Vietnam | `p3/replication/do/01_build_vietnam.do` (+ `scripts/p3_dai_reproduce.py`) | ⚠️ Stata build authoritative | pattern reproduces; exact magnitudes need candidate's Stata (b1_d denominator — see p3_paternoster_zflag note) |
| **P8** SIDS | `p8/replication/build_and_run_p8_7pacific.py` | ✅ **rebuilt from raw (7 Pacific, Timor excluded)** | dissolution: linear −0.085 (p_wild=.66), FSTS² +0.696 (.082); M3 FSTS² +1.051 (.056), TCI +0.064 (.036); pinned `p8/replication/data/p8_7pacific_pinned.csv`. −1.339 only on restricted 3-economy build (illustrative) |

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

---

## Cập nhật 2026-06-23 — A1 cross-check (Python) + P4 fix

Đã chạy lại bằng phần mềm tương đương (Python) trên `data_wbes/raw_dta/` và **tái lập headline**:

| Paper | Runner | Tái lập 2026-06-23 |
|---|---|---|
| P4 Singapore | `p4/replication/p4_singapore_figs_from_raw.py` | ✅ chữ U ngược; **FSTS²×DAI +3,22** (≈ bản thảo +3,119); TP ~86% (không định vị); N=623/617 |
| P5 China | `p5/replication/python/build_and_run.py` | ✅ mfg TP 42,31/29,65; pooled 48,78 |
| P7 50-econ | `dist/osf/P7_capstone/code/p7_run_50econ.py` | ✅ TP 51,40/43,83; Nhóm IV 43,03; SIDS U-shape (N theo khung raw, gồm Azerbaijan — xem `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`) |
| P8 SIDS | `p8/replication/build_and_run_p8_7pacific.py` | ✅ N=1.450/7cl; lin −0,085 (.656); quad +0,696 (.082) |
| P9 India | `p9_india/replication/run_pipeline.py` | ✅ TP 61,81/40,72/tan biến; Paternoster z=−7,94 |
| P10 Japan | `p10_japan/replication/p10_japan_models.py` | ✅ premium +0,258; FSTS 4,1% |

**Fix:** `p4/replication/p4_singapore_replication.py` (bản Vietnam dán nhầm nhãn, đường dẫn upload tạm)
→ chuyển thành **stub deprecation** chỉ sang runner đúng `p4_singapore_figs_from_raw.py` (đã path-correct
`WBES_RAW`/`data_wbes/raw_dta`) và do-files `p4/replication/do/`.

**P9 + P10 path-audit:** ✅ cả hai đã đọc `data_wbes/raw_dta/` (không cần sửa).

**Còn lại:** P3 (độ lớn chính xác cần Stata `b1_d`); top-level `replication/*.py` xáo trộn (trùng per-paper,
khuyến nghị dọn); A2 verify DOI phải chạy trên máy có mạng của NCS (container chặn outbound — CrossRef 403).
