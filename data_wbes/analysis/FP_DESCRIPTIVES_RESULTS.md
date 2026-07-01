# Kết quả re-lock thống kê mô tả Firm Performance theo nhóm ICRV

> Khung phân tích 49 nền / 91.864 DN. Nguồn: `p7_pooled_clean.csv` (LP, biến tỷ lệ)
> + raw `.dta` (ROS). Tái lập: `scripts/relock_ros.py`. Ngày 2026-06-11.

## A. Hai chỉ số hiệu quả (nhất quán công trình đã công bố)

### A1. ROS = (doanh thu − chi phí vận hành)/doanh thu — chỉ số MỨC, so sánh được
*(tỷ lệ vô đơn vị; trích book chapter InTechOpen 2025 — India, và P2 JFAR robustness)*

| Nhóm ICRV | n_firms | ROS median | ROS mean | sd |
|---|--:|--:|--:|--:|
| I Advanced_innovation | 3.337 | **0,503** | 0,513 | 0,29 |
| II Advanced_resource | 118¹ | 0,470 | 0,448 | 0,34 |
| III Upper_mid | 13.401 | 0,455 | 0,450 | 0,38 |
| IV Lower_mid_transition | 37.792 | **0,351** | 0,386 | 0,31 |
| V Emerging | 12.523 | 0,408 | 0,283² | 1,16² |
| VI SIDS_small | 520¹ | 0,474 | −0,191² | 3,48² |

¹ mẫu nhỏ (GCC/SIDS ít DN có dữ liệu chi phí). ² mean/sd méo do outlier đến **dùng median**.

**Diễn giải:** biên lợi nhuận cao nhất ở chế độ tiên tiến (I≈0,50), thấp nhất ở
chuyển đổi TB-thấp (IV≈0,35) — nhất quán Institutional Theory (thể chế mạnh đến chi phí
giao dịch thấp đến biên cao). Đây là chỉ số MỨC hợp lệ giữa nước (khác với năng suất thô).

### A2. Năng suất lao động — chuẩn hóa z-score within-country-year — chỉ số PHÂN TÁN
*(trích P1 VEFR, P2 JFAR; chỉ so sánh PHÂN TÁN, không so mức vì đã khử khác biệt nước)*

| Nhóm ICRV | n | lp_z sd (phân tán nội nhóm) |
|---|--:|--:|
| I Advanced_innovation | 4.222 | 1,00 |
| II Advanced_resource | 2.269 | 0,92 |
| III Upper_mid | 13.993 | 1,00 |
| IV Lower_mid_transition | 50.926 | 1,00 |
| V Emerging | 18.569 | 0,97 |
| VI SIDS_small | 1.885 | 1,00 |

Phân tán năng suất nội nhóm ~đồng đều (0,92–1,00).

## B. ⚠️ Đính chính luận điểm cần rà trong CĐ1/Chương 4
Luận điểm "**phân tán/năng suất tăng đơn điệu Nhóm I–VI**" (nếu dựa trên mức
`ln_labor_prod` thô) là **artifact tiền tệ** — phải bỏ hoặc thay bằng: (i) gradient
**ROS** giảm từ I–IV (chỉ số mức hợp lệ); (ii) phân tán LP-z ~đồng đều.

## C. Biến tỷ lệ theo nhóm (so sánh được trực tiếp)
Xem `cd1_relock_descriptives_by_icrv.csv`: fsts_pct, exporter%, dai_website%, tci_z,
mgr_female%, firm_age theo 6 nhóm ICRV.

## D. Trích dẫn khi đưa vào luận án
- Năng suất lao động: P1 (Do & Phan, 2026a — VEFR), P2 (Do & Phan, 2026g — JFAR).
- ROS/ROA: book chapter (InTechOpen, 2025), P2 robustness (Bảng 5 alternative metrics).
- Trình bày là **kết quả của nghiên cứu này** (nghiên cứu thành phần), không cite bài under-review như nguồn ngoài.
