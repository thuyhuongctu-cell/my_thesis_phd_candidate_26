# Kết quả pipeline raw đa biến — bảng mô tả CĐ1 theo nhóm ICRV

> Tái tính các chiều mô tả CĐ1 Mục 2.3.3–2.3.8 từ **raw WBES .dta** trên khung canonical
> 49 nền, **dedupe theo nước-năm** (một cross-section chuẩn / economy-year; loại
> panel/Informal/ISBS/ISES/Micro/expansion/TGS). Tái lập: `scripts/cd1_descriptives_pipeline.py`
> + `scripts/wbes_canon.py`. Outputs: `cd1_pipeline_by_icrv.csv`, `cd1_pipeline_coverage.csv`.
> Cập nhật 2026-06-11 sau khi nạp raw bổ sung (GCC + Pacific). 102 file dùng — **đủ 50/50 nền có raw (gồm Nhật Bản 2025, Nhóm I)** (đã loại các đợt khảo sát trước 2006 theo quy ước phạm vi).

## A. Bảng mô tả theo nhóm ICRV (đơn vị %, trừ khi ghi khác)

| Chỉ tiêu | I Adv-innov | II Adv-res | III Upper-mid | IV Lower-mid | V Emerging | VI SIDS |
|---|--:|--:|--:|--:|--:|--:|
| n_firms (raw, dedupe) | 4.222 | 2.231 | 13.993 | 45.003 | 18.957 | 2.295 |
| Đổi mới sản phẩm (h1) | 24,3 | 17,0 | 26,7 | 17,1 | 24,4 | **34,2** |
| Đổi mới quy trình (h5) | 14,7 | 8,6 | 18,9 | 14,7 | 16,3 | **24,7** |
| Chi R&D (h8) | **20,5** | 7,0 | 21,5 | 15,5 | 17,5 | 10,2 |
| Chứng nhận ISO (b8) | **35,0** | 15,2 | 25,4 | 25,3 | 12,7 | 12,2 |
| Website (c22b) | **61,7** | 50,2 | 53,9 | 48,3 | 40,9 | 41,5 |
| Nữ quản lý cấp cao (b7a) | 27,5 | **4,6** | 29,1 | 10,8 | 13,9 | 30,9 |
| Nữ trong chủ sở hữu (b4) | 32,5 | 9,8 | 38,4 | 18,2 | 23,8 | 47,4 |
| DN xuất khẩu (FSTS>0) | **28,4** | 11,7 | 21,3 | 14,3 | 18,8 | 14,7 |
| FDI nước ngoài ≥10% (b2b) | 10,6 | 13,6 | 8,9 | **3,1** | 7,1 | **20,0** |
| SME (<100 lao động, l1) | 79,5 | 77,4 | 78,7 | 74,0 | 86,0 | **91,8** |
| Tham nhũng = trở ngại lớn (j30f≥3) | **2,9** | 4,4 | 10,2 | 22,7 | 28,2 | **28,0** |
| FSTS trung bình | 13,4 | 3,9 | 10,2 | 8,1 | 10,6 | 6,7 |
| Hối lộ (% doanh thu, j7a) | 0,2 | 0,0 | 0,8 | 1,7 | 0,9 | 1,4 |
| Tuổi DN trung bình (năm) | 23,0 | 18,5 | 15,7 | 20,1 | 14,9 | 17,6 |
| CAGR việc làm (l1/l2, %) | 3,0 | 3,7 | 3,8 | 2,8 | 4,5 | **5,3** |

## B. Độ phủ nguồn raw theo nhóm (sau khi nạp bổ sung)

| Nhóm | Coverage | Thành viên / thiếu |
|---|---|---|
| I — Adv. đổi mới | **5/5** Có | HongKong, Israel, Korea, Singapore, Taiwan |
| II — Adv. tài nguyên (GCC) | **6/6** Có | Bahrain, Brunei, Kuwait, Oman, Qatar, Saudi Arabia |
| III — Trung bình cao | **6/6** Có | Armenia, China, Georgia, Kazakhstan, Malaysia, Thailand |
| IV — Chuyển đổi TB-thấp | **7/7** Có | Bangladesh, India, Indonesia, Mongolia, Pakistan, Philippines, Vietnam |
| V — Đang nổi | **17/17** Có | *(đủ — gồm Lebanon, Yemen)* |
| VI — SIDS | **8/8** CóCó | Fiji, Kiribati, PNG, Samoa, Solomon, Timor-Leste, Tonga, Vanuatu |

## C. Diễn giải chính (gradient thể chế — hợp lệ vì toàn biến tỷ lệ/nhị phân)

1. **Năng lực công nghệ nền tảng giảm theo gradient thể chế**: R&D 20,5% đến (VI) 10,2%; ISO 35,0% đến 12,2%; website 61,7% đến 41,5% (I–VI).
2. **Tham nhũng tăng ngược gradient**: trở ngại lớn thấp nhất ở Nhóm I (2,9%) đến 22,7% (IV) đến cao nhất ở VI (28,0%); GCC ở mức 4,4%.
3. **SIDS "thích nghi & nhảy vọt" — XÁC NHẬN bằng đủ 8/8 nền**: đổi mới sản phẩm CAO NHẤT mọi nhóm (34,2%), đổi mới quy trình cao nhất (24,7%), website 41,5% ngang nhóm V dù GNI thấp hơn — đổi mới bằng nguồn lực hạn chế.
4. **GCC (II) số THẬT đủ 6/6 nền** thay artifact 2-nền trước đây: đặc trưng dầu mỏ — R&D thấp (7,0%), nữ quản lý cấp cao rất thấp (4,6%), FDI cao (13,6%).
5. **SIDS FDI cao (20,0%) + SME cao nhất (91,8%)**: cấu trúc du lịch/viễn thông do MNE dẫn dắt trên nền kinh tế vi mô.
6. **Quốc tế hóa phân cực**: DN xuất khẩu 28,4% (I) đến 11,7% (II) đến 14,7% (VI); FSTS trung bình thấp khắp nơi (3,5–13,4%).

## D. Lưu ý phương pháp

- **Dedupe nước-năm** loại double-count (vd Nhóm IV trước 55.675 đến 45.003 sau khi gộp đúng các sóng trùng). n_firms là tổng DN của TẤT CẢ sóng khảo sát mỗi nước (khác mẫu phân tích master vì pool nhiều đợt).
- File raw không xóa khỏi kho; dedupe chỉ ở bước đọc (idempotent). Quy ước phạm vi: chỉ đợt khảo sát ≥2006 **dùng bộ công cụ WBES Standardized toàn cầu** — nhận diện bằng sự hiện diện của các biến lõi đã hài hòa (d2 doanh thu, l1 lao động, d3b/d3c xuất khẩu). Chạy lại pipeline khi có raw mới (idempotent).
- Bảng đã tính từ pipeline raw và dùng trong CĐ1: **2.3.3.2, 2.3.4.1, 2.3.5.1** (file này), **2.3.3.1** phân tán within-wave (`cd1_dispersion_by_wave.csv`), **2.3.6.1/2.3.6.4/2.3.6.5** temporal + tiểu nhóm + đợt 2025 (`cd1_wave_stats.csv`), **2.3.8.1** tương quan (`cd1_correlations_by_icrv.csv`), **Bảng A.1** (`cd1_economy_inventory.csv`). Toàn bộ CĐ1 hiện chỉ dùng MỘT pool mô tả: 86.701 DN / 49 nền / 102 cặp (2006–2026).
- **Ba đợt khảo sát nằm ngoài pool vì lý do tương thích bộ công cụ (không phải lỗi dữ liệu)**: Lebanon 2009 (bộ PICS khu vực MENA 2009, 651 biến mã `q####`), Cambodia 2007 (828 biến) và Cambodia 2013 (579 biến) — cả ba **không chứa** các biến lõi đã hài hòa (d2/l1/d3b/d3c) nên không thể đưa vào khung so sánh chung. Đây là cùng một quy tắc loại trừ với mọi bộ công cụ phi chuẩn (Informal/ISBS/ISES/Micro/panel). Các đợt Standardized của chính hai nền này **đã có** trong pool: Lebanon 2013 (561) + 2019 (532); Cambodia 2016 (373) + 2023 (519). Đối chiếu: Jordan 2006 và 16 đợt 2009–2012 khác dùng bộ công cụ Standardized (có đủ d2/l1/d3b/d3c) nên được giữ.
