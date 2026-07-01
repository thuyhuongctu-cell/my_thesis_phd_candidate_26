# Kế hoạch rà soát & chọn chỉ số đo Firm Performance (re-lock bảng mô tả)

> Mục tiêu: chọn chỉ số đo hiệu quả doanh nghiệp (firm performance) cho các bảng
> thống kê mô tả theo nhóm ICRV (CĐ1 Mục 2.3.3–2.3.8, Chương 4 Mục 4.1) **nhất quán với
> các công trình đã công bố** của tác giả, và xử lý đúng vấn đề so sánh giữa nước.

## 1. Cách đo FP trong các công trình đã công bố (đã rà soát)

| Công trình | Phạm vi | Chỉ số FP chính | Robustness | Ghi chú |
|---|---|---|---|---|
| **P1 — VEFR** (đã đăng) | 17 nền Á mới nổi | **Năng suất lao động** = doanh thu/lao động thường xuyên | — | = `ln_labor_prod` |
| **P2 — JFAR** (đã đăng) | Trung Quốc (SME) | **Năng suất lao động** | **ROA**, Sales Growth (Bảng 5) | 1 nước đến so sánh được |
| **Book chapter — InTechOpen** (đã đăng) | Ấn Độ | **ROS** (Return on Sales) | — | 1 nước đến so sánh được |
| **P3–P9 (luận án)** | 1 nước hoặc 49 nước | Năng suất lao động (FSTS đến LP) | — | dùng country-year FE |

 đến Hai trục đo chuẩn của nhóm tác giả: **năng suất lao động** (P1, P2, P7) và **ROS/ROA** (book chapter, P2 robustness).

## 2. ⚠️ Phát hiện then chốt — biến năng suất thô KHÔNG so sánh được giữa nước

`ln_labor_prod` trong `p7_pooled_clean.csv` tính từ doanh thu **nội tệ** (chưa quy đổi
USD/PPP). Bằng chứng (median doanh thu/lao động):

| Nước | exp(median lnLP) | Loại |
|---|---|---|
| Việt Nam | 372.727.273 | VND |
| Cambodia | 27.807.027 | KHR |
| Singapore | 60.000 | SGD |
| Bangladesh | 480.000 | BDT |

Việt Nam "năng suất cao nhất" chỉ là **ảo giác đơn vị tiền tệ**. Do đó, **Không được** dùng
mức `ln_labor_prod` thô để so sánh giữa nhóm ICRV, và phải **kiểm tra lại** mọi luận
điểm dạng "phân tán/năng suất tăng đơn điệu Nhóm I–VI" trong CĐ1/Chương 4 — có thể là
artifact tiền tệ.

> Lưu ý: P1 (đa nước) hợp lệ vì (giả định) đã quy đổi USD hoặc báo cáo theo vùng;
> P2/book chapter hợp lệ vì 1 nước. Luận án pool 49 nước nên **bắt buộc** xử lý.

## 3. Chỉ số đề xuất (nhất quán công bố + so sánh được)

1. **Năng suất lao động chuẩn hóa within-country-year z-score** — chỉ số CHÍNH cho so
   sánh mức/phân tán giữa nhóm ICRV (loại bỏ tiền tệ). Trích dẫn P1, P2, P7.
   - Bảng mô tả: mean/sd của z-score theo nhóm; phân tán = sd/CV.
2. **ROS = lợi nhuận/doanh thu** — chỉ số PHỤ (tỷ lệ, vô đơn vị đến so sánh được trực tiếp).
   Trích dẫn book chapter (InTechOpen) + P2 (ROA). Cần tính từ raw `.dta` (biến doanh
   thu d2/n3 + chi phí n2*) vì master không có sẵn ROS.
3. Biến tỷ lệ khác (FSTS%, exporter%, DAI%, TCI, nữ quản trị%, firm age) — đã so sánh
   được, dùng trực tiếp (xem `cd1_relock_descriptives_by_icrv.csv`).

## 4. Các bước thực hiện (re-lock)

| # | Việc | Nguồn | Output |
|---|---|---|---|
| 1 | Xác nhận P1 quy đổi USD hay within-region (đọc kỹ P1 Mục 3.2) | `p1/*.docx` | ghi chú metric |
| 2 | Tính LP z-score within-country-year từ master | `p7_pooled_clean.csv` | cột `lp_z` |
| 3 | Tính ROS từ raw `.dta` (doanh thu, chi phí, lợi nhuận) | `data_wbes/raw_dta/` | `ros` per firm |
| 4 | Lập bảng mô tả theo nhóm ICRV: LP-z (mean/sd), ROS, biến tỷ lệ | bước 2–3 | bảng chuẩn |
| 5 | Cập nhật CĐ1 Mục 2.3.3–2.3.8 + Chương 4 Mục 4.1; trích P1/P2/book chapter | bước 4 | re-lock |
| 6 | Rà lại luận điểm "gradient năng suất I–VI" — sửa nếu là artifact | — | đính chính |
| 7 | Gate calibration (Singapore) + linter `check-consistency.py` | — | validate |

## 5. Cần tác giả xác nhận
- (a) Đồng ý chỉ số chính = **LP z-score within-country** + phụ = **ROS**? 
- (b) Có muốn tính ROS từ raw .dta (nặng hơn) hay tạm chỉ LP z-score + biến tỷ lệ?
- (c) P1 đã quy đổi USD chưa (ảnh hưởng cách diễn giải "regional hierarchy")?
