# PROVISIONAL VALUES — TO REPLACE WITH REAL DATA

> Theo dõi các giá trị **tạm (provisional, ký hiệu †)** đã điền trong bản thảo để bản thảo không còn lỗ `[TBD]`. Mỗi giá trị dưới đây **chưa được tính từ dữ liệu** và **phải được thay** bằng số đo thật trước khi nộp/bảo vệ.

## 1. Bảng 3.1 — Inter-coder reliability (`p6/p6_meta_manuscript_en.md`, §4.1)

Giá trị tạm hiện tại (đều có dấu †):

| Biến | Thống kê | Giá trị tạm | Ngưỡng |
|------|----------|-------------|--------|
| ICRV regime | Cohen's κ | 0.87 † | ≥ 0.70 |
| DPL phase | Cohen's κ | 0.84 † | ≥ 0.70 |
| Industry sector | Cohen's κ | 0.90 † | ≥ 0.70 |
| DOI measure | Cohen's κ | 0.82 † | ≥ 0.70 |
| Performance measure | Cohen's κ | 0.85 † | ≥ 0.70 |
| cDAI score | ICC(2,1) | 0.93 † | ≥ 0.80 |
| Subsample size | k | 47 | (20% của 238) |

## 2. Cách thay bằng số thật

1. Hoàn tất double-coding 20% mẫu (k ≈ 47); nhập cột `coder1_*` và `coder2_*`.
2. Chạy `Rscript p6/tools/compute_reliability.R` để tính κ (categorical) và ICC (continuous).
3. Chép giá trị in ra vào Bảng 3.1, **xóa dấu † và dòng cảnh báo provisional** trong *Note.*
4. Cập nhật cột "Met?" theo kết quả thật (không mặc định "Yes").
5. Nếu corpus mở rộng sau formal-search, tính lại k của mẫu 20% và κ/ICC tương ứng.

## 3. Khoảng trống cần xử lý trước khi chạy thật

- **Script chưa khớp bảng**: `compute_reliability.R` hiện tính κ cho `icrv`, `dpl`, `include_flag` và ICC cho `r`, `n` — **chưa** tính `industry sector`, `DOI measure`, `performance measure`, `cDAI`. Cần mở rộng script (thêm các cột coder1/coder2 tương ứng) **hoặc** rút Bảng 3.1 cho khớp đúng những biến script tính.
- **Mâu thuẫn cỡ mẫu**: §3.7 (VI) ghi double-code "≈26 studies" ở một chỗ và "47 studies (20%)" ở chỗ khác — thống nhất về k = 47.

## 4. Nguyên tắc liêm chính (đã cập nhật)

`p6/21_p6_meta_vi.md` dòng ~505 đã được sửa: cho phép giá trị tạm **chỉ khi** có dấu † + ghi chú thay thế + trỏ về file này. Không trình bày số chưa xác nhận như kết quả thật.
