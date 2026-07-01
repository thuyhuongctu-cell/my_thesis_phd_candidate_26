# Đối chiếu số liệu canonical — re-lock từ data thật (p7_pooled_clean.csv)

> Nguồn: `data_wbes/p7/p7_pooled_clean.csv` (106.765 dòng, 55 nhãn nền). Tính ngày 2026-06-11.
> Script tái lập: xem khối tính trong lịch sử commit / `data_wbes/analysis/cd1_relock_descriptives_by_icrv.csv`.

## 1. Pool size canonical (ĐÃ xác nhận bằng data)

| Khung | Định nghĩa | N doanh nghiệp | Số nền |
|---|---|---|---|
| **Phân loại (classification)** | toàn pool có `icrv_group` | **96.415** | 52 |
| **Phân tích (analytic)** | loại 3 panel-trùng (PHL/NPL/MNG_panel) + 3 ngoài Á (Comoros, Cyprus, Turkey) | **91.864** (≈91.982) | **49** |

Đếm theo nhóm ICRV (khung phân tích 49 nền):

| Nhóm | icrv_label | N |
|---|---|---|
| I | Advanced_innovation | 4.222 |
| II | Advanced_resource | 2.269 |
| III | Upper_mid | 13.993 |
| IV | Lower_mid_transition | 50.926 |
| V | Emerging | 18.569 |
| VI | SIDS_small | 1.885 |
| **Tổng** | | **91.864** |

(Pool phân loại 96.415: I=4.708, II=2.269, III=17.905, IV=50.926, V=18.569, VI=2.038.)

## 2. Số LỆCH cần chuẩn hóa trong bản thảo

| Vị trí | Số hiện tại | Chuẩn data | Hành động |
|---|---|---|---|
| `thesis/14_cd1_part1` (abstract CĐ1) | 101.185 / 47 nền | 91.982 (analytic) / 96.415 (class.) — 49 nền | sửa |
| `thesis/chuong_2` Mục 2.3.2 dòng 135 | "84.910–91.982 / 102 waves" | 91.982 / 49 nền / 102–108 waves | bỏ 84.910 |
| CĐ2 / Bảng 2.3.2.1 CĐ1 | 91.864/91.982 · 49 | Có đã khớp | giữ |

> "84.910" là N của mô hình M2 (sau listwise deletion một số biến) — KHÔNG phải pool. Nếu giữ phải ghi rõ "N hồi quy M2".

## 3. ⚠️ Cảnh báo phương pháp — bảng thống kê mô tả theo nhóm

`ln_labor_prod` thô trong master **KHÔNG đơn điệu** theo gradient ICRV
(I=15,70; II=11,92; III=13,25; IV=14,96; V=15,07; VI=10,45) vì chưa chuẩn hóa
PPP/tiền tệ giữa các nước. Do đó **không thể** dùng trực tiếp để chứng minh luận
điểm "phân tán năng suất tăng đơn điệu từ Nhóm I–VI" trong CĐ1/Chương 4.

**Cần quyết định metric trước khi điền bảng mô tả:**
- (a) chuẩn hóa within-country z-score rồi mới so sánh nhóm; hoặc
- (b) dùng PPP-adjusted productivity; hoặc
- (c) chỉ báo cáo phân tán (sd/CV) trong từng nước, gộp theo nhóm.

Các biến tỷ lệ (fsts_pct, exporter%, dai_website%, mgr_female%) so sánh được trực
tiếp — xem `cd1_relock_descriptives_by_icrv.csv`.
