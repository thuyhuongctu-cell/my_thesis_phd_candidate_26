# Cross-Paper Headline-Number Verification — 2026-06-10

**Mục đích:** xác minh mọi con số "đầu bài" (headline turning point / hệ số FIP) trong bản thảo nộp **truy vết được** tới một file kết quả đã commit trong repo — không có số nào bịa. Thực hiện sau khi tái chạy P8 và rà soát toàn bộ P3–P9.

> Phát hiện cấu trúc: mỗi paper có **hai pipeline song song** — (a) pipeline *chính* (Python, sinh `coefs_main_models.csv` / `results_coefs.csv` / `p*_summary_focal.csv`) nuôi các Bảng trong bản thảo; và (b) pipeline *R thay thế* (`p*_R_turning_points.csv`) chạy đối chứng. Bản thảo nhất quán trích pipeline **chính**. Hai pipeline lệch nhẹ ở turning point do khác đặc tả (centering/model), nhưng **không** đổi dấu hay kết luận.

## Bảng truy vết

| Paper | Số đầu bài (bản thảo) | File nguồn (đã commit) | Giá trị nguồn | Khớp |
|---|---|---|---|:--:|
| **P3** Việt Nam | TP band **39–46%** (3 wave, 14 năm) | `p3/replication/coefs_main_models.csv` | per-wave M2 (vd VNM2009: b1=1.0454, b2=−1.7738; VNM2015: 1.1587/−2.115) | ✅ |
| **P4** Singapore | TP ≈ **88.6%**, CI rộng [53%, 253%] | `p4/replication/coefs_main_models.csv` | M2: FSTSc=2.652, FSTSc2=−1.705 (FSTSc2 p=.068) | ✅ |
| **P5** Trung Quốc | TP = **49.4%** | `p5/replication/results/results_coefs.csv` | M2-2012: FSTS=2.0654, FSTSsq=−2.0919 → −b1/(2b2)=0.4937 | ✅ exact |
| **P7** Capstone | TP ≈ **36%** (49 nền KT, N=84,910) | `p7/replication/results/p7_summary_focal.csv` | M2: tp=36.4 (b1=1.3161, b2=−1.8102); country-FE/cap models cụm 32.7–40.0% | ✅ exact |
| **P8** Pacific SIDS | β(FSTS)=**−1.339**, N=209; full N=959 | tái chạy `run_p8_7pacific.py` từ `data_wbes/p7/p7_pooled_clean.csv` | M1=−1.339253/N=209; full N=959/exporter 13.8% | ✅ exact |
| **P9** Ấn Độ | TP **61.8%**(2014)→**40.7%**(2022)→**tan rã**(2025) | `p9_india/replication/results/p9_india_turning_points.csv` | 2014=61.81, 2022=40.72, 2025=−111.9 (CI khổng lồ → dissolution) | ✅ exact |

## Ghi chú lệch pipeline (minh bạch, không phải lỗi)
- **P4:** `p4_R_turning_points.csv` (spec thay thế, b1=3.642/b2=−2.630) cho TP=76.4%; bản thảo **không** dùng số này, mà dùng M2 trong `coefs_main_models.csv` → 88.6% kèm CI rộng và cảnh báo "sparsely populated upper region".
- **P5:** `p5_R_turning_points.csv` cho 47.6% (pooled); bản thảo dùng `results_coefs.csv` → 49.4%. Cả hai cùng vùng ~48%, kết luận inverted-U không đổi.
- **P3:** `p3_R_turning_points.csv` chỉ có pooled M2=34.5%; bản thảo báo cáo band per-wave 39–46% từ `coefs_main_models.csv`.
- **P8:** bivariate R canonical −0.864 (bản thảo) vs Python reimpl −0.919 — chỉ 1 model phụ; cả hai âm, p≈.05.

## Kết luận
Mọi số đầu bài trong 6 paper (P3–P5, P7–P9) **truy vết được tới file kết quả đã commit**; không có số bịa. Khác biệt giữa hai pipeline là chi tiết đặc tả, đã ghi nhận minh bạch, không ảnh hưởng dấu/kết luận. Khuyến nghị NCS: khi nộp, đảm bảo file replication đính kèm là pipeline **chính** (cùng pipeline mà bản thảo trích) để reviewer tái lập khớp.
