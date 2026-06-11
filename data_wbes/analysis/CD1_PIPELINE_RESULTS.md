# Kết quả pipeline raw đa biến — bảng mô tả CĐ1 theo nhóm ICRV

> Tái tính các chiều mô tả CĐ1 §2.3.3–2.3.8 từ **raw WBES .dta** trên khung canonical
> 49 nền, **dedupe theo nước-năm** (một cross-section chuẩn / economy-year; loại
> panel/Informal/ISBS/ISES/Micro/expansion/TGS). Tái lập: `scripts/cd1_descriptives_pipeline.py`
> + `scripts/wbes_canon.py`. Outputs: `cd1_pipeline_by_icrv.csv`, `cd1_pipeline_coverage.csv`.
> Cập nhật 2026-06-11 sau khi nạp raw bổ sung (GCC + Pacific). 97 file dùng.

## A. Bảng mô tả theo nhóm ICRV (đơn vị %, trừ khi ghi khác)

| Chỉ tiêu | I Adv-innov | II Adv-res | III Upper-mid | IV Lower-mid | V Emerging | VI SIDS |
|---|--:|--:|--:|--:|--:|--:|
| n_firms (raw, dedupe) | 4.222 | 1.932 | 13.993 | 45.003 | 17.034 | 2.295 |
| Đổi mới sản phẩm (h1) | 24,3 | 17,0 | 26,7 | 17,1 | 23,8 | **34,2** |
| Đổi mới quy trình (h5) | 14,7 | 7,7 | 18,9 | 14,7 | 15,9 | **24,7** |
| Chi R&D (h8) | **20,5** | 6,1 | 21,5 | 15,5 | 15,9 | 10,2 |
| Chứng nhận ISO (b8) | **35,0** | 14,4 | 25,4 | 25,3 | 12,3 | 12,2 |
| Website (c22b) | **61,7** | 49,7 | 53,9 | 48,3 | 39,8 | 41,5 |
| Nữ quản lý cấp cao (b7a) | 27,5 | **4,0** | 29,1 | 10,8 | 15,2 | 30,9 |
| Nữ trong chủ sở hữu (b4) | 32,5 | 8,9 | 38,4 | 18,2 | 25,1 | 47,4 |
| DN xuất khẩu (FSTS>0) | **28,4** | 11,2 | 21,3 | 14,3 | 17,9 | 14,7 |
| FDI nước ngoài ≥10% (b2b) | 10,6 | 13,3 | 8,9 | **3,1** | 7,5 | **20,0** |
| SME (<100 lao động, l1) | 79,5 | 77,1 | 78,7 | 74,0 | 85,7 | **91,8** |
| Tham nhũng = trở ngại lớn (j30f≥3) | **2,9** | **0,8** | 10,2 | 22,7 | 22,6 | **28,0** |
| FSTS trung bình | 13,4 | 3,5 | 10,2 | 8,1 | 10,6 | 6,7 |
| Hối lộ (% doanh thu, j7a) | 0,2 | 0,0 | 0,8 | 1,7 | 0,9 | 1,4 |
| Tuổi DN trung bình (năm) | 23,0 | 18,6 | 15,7 | 20,1 | 14,9 | 17,6 |
| CAGR việc làm (l1/l2, %) | 3,0 | 3,4 | 3,8 | 2,8 | 4,7 | **5,3** |

## B. Độ phủ nguồn raw theo nhóm (sau khi nạp bổ sung)

| Nhóm | Coverage | Thành viên / thiếu |
|---|---|---|
| I — Adv. đổi mới | **5/5** ✅ | HongKong, Israel, Korea, Singapore, Taiwan |
| II — Adv. tài nguyên (GCC) | **5/6** ✅ | Bahrain, Brunei, Kuwait, Qatar, Saudi Arabia · *thiếu Oman (chỉ có bản 2003 dùng bộ biến cũ)* |
| III — Trung bình cao | **6/6** ✅ | Armenia, China, Georgia, Kazakhstan, Malaysia, Thailand |
| IV — Chuyển đổi TB-thấp | **7/7** ✅ | Bangladesh, India, Indonesia, Mongolia, Pakistan, Philippines, Vietnam |
| V — Đang nổi | **15/17** ✅ | *(thiếu Lebanon, Yemen — chưa có raw)* |
| VI — SIDS | **8/8** ✅✅ | Fiji, Kiribati, PNG, Samoa, Solomon, Timor-Leste, Tonga, Vanuatu |

## C. Diễn giải chính (gradient thể chế — hợp lệ vì toàn biến tỷ lệ/nhị phân)

1. **Năng lực công nghệ nền tảng giảm theo gradient thể chế**: R&D 20,5%→ (VI) 10,2%; ISO 35,0%→12,2%; website 61,7%→41,5% (I→VI).
2. **Tham nhũng tăng ngược gradient**: trở ngại lớn 2,9% (I) → 22,7% (IV) → 28,0% (VI); GCC thấp nhất (0,8%).
3. **SIDS "thích nghi & nhảy vọt" — XÁC NHẬN bằng đủ 8/8 nền**: đổi mới sản phẩm CAO NHẤT mọi nhóm (34,2%), đổi mới quy trình cao nhất (24,7%), website 41,5% ngang nhóm V dù GNI thấp hơn — đổi mới bằng nguồn lực hạn chế.
4. **GCC (II) số THẬT 5/6 nền** thay artifact 2-nền trước đây: đặc trưng dầu mỏ — R&D thấp (6,1%), nữ quản lý cấp cao rất thấp (4,0%), tham nhũng-trở-ngại thấp nhất (0,8%), FDI cao (13,3%).
5. **SIDS FDI cao (20,0%) + SME cao nhất (91,8%)**: cấu trúc du lịch/viễn thông do MNE dẫn dắt trên nền kinh tế vi mô.
6. **Quốc tế hóa phân cực**: DN xuất khẩu 28,4% (I) → 11,2% (II) → 14,7% (VI); FSTS trung bình thấp khắp nơi (3,5–13,4%).

## D. Lưu ý phương pháp

- **Dedupe nước-năm** loại double-count (vd Nhóm IV trước 55.675 → 45.003 sau khi gộp đúng các sóng trùng). n_firms là tổng DN của TẤT CẢ sóng khảo sát mỗi nước (khác mẫu phân tích master vì pool nhiều đợt).
- File raw không xóa khỏi kho; dedupe chỉ ở bước đọc (idempotent). Nếu có raw Oman chuẩn / Lebanon / Yemen, chạy lại `scripts/cd1_descriptives_pipeline.py` là tự cập nhật.
- Bảng đã đồng bộ vào CĐ1: **2.3.3.2, 2.3.4.1, 2.3.5.1**. Các bảng phân tán năng suất (2.3.3.1), temporal (2.3.6.x), tiểu cảnh (2.3.7.1), tương quan (2.3.8.x) vẫn theo bản khóa mô tả 101.185.
