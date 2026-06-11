# Kết quả pipeline raw đa biến — bảng mô tả CĐ1 theo nhóm ICRV

> Tái tính các chiều mô tả của CĐ1 §2.3.3–2.3.8 từ **raw WBES .dta** (84 file
> cross-section chính), khung canonical 49 nền. Tái lập: `scripts/cd1_descriptives_pipeline.py`.
> Outputs: `cd1_pipeline_by_icrv.csv`, `cd1_pipeline_coverage.csv`. Ngày 2026-06-11.

## A. Bảng mô tả theo nhóm ICRV (đơn vị %, trừ khi ghi khác)

| Chỉ tiêu | I Adv-innov | II Adv-res¹ | III Upper-mid | IV Lower-mid | V Emerging | VI SIDS¹ |
|---|--:|--:|--:|--:|--:|--:|
| n_firms (raw) | 4.222 | 300 | 16.693 | 55.675 | 16.880 | 753 |
| Đổi mới sản phẩm (h1) | 24,3 | 53,9 | 26,7 | 17,1 | 23,7 | 20,6 |
| Đổi mới quy trình (h5) | 14,7 | 33,6 | 18,9 | 14,7 | 16,2 | 15,0 |
| Chi R&D (h8) | **20,5** | 22,6 | 21,5 | 15,5 | 15,8 | **5,7** |
| Chứng nhận ISO (b8) | **35,0** | 42,5 | 31,4 | 35,9 | 11,9 | **6,6** |
| Website (c22b) | **61,7** | 83,3 | 56,9 | 48,3 | 39,1 | **28,9** |
| Nữ quản lý cấp cao (b7a) | 27,5 | 17,0 | 26,0 | 10,8 | 15,4 | 30,2 |
| Nữ trong chủ sở hữu (b4) | 32,5 | 42,9 | 42,0 | 31,2 | 25,6 | 40,1 |
| DN xuất khẩu (FSTS>0) | **28,4** | 23,1 | 21,7 | 14,3 | 17,4 | **10,4** |
| FSTS trung bình | 13,4 | 9,4 | 10,3 | 8,1 | 10,4 | 6,9 |
| Tham nhũng = trở ngại lớn (j30f≥3) | **2,9** | 4,2 | 8,9 | **22,7** | 21,1 | **24,9** |
| Hối lộ (% doanh thu, j7a) | 0,2 | 0,1 | 0,7 | 1,7 | 0,9 | 2,5 |
| Tuổi DN trung bình (năm) | 23,0 | 23,5 | 15,3 | 20,1 | 15,0 | 12,0 |

¹ **Coverage thấp** — xem mục B; số nhóm II/VI KHÔNG đại diện cho cả nhóm.

## B. Độ phủ nguồn raw theo nhóm

| Nhóm | Coverage | Thiếu |
|---|---|---|
| I | **5/5** ✅ | — |
| II | **2/6** ⚠️ (Bahrain, Brunei) | Saudi, Qatar, Kuwait, Oman |
| III | **6/6** ✅ | — |
| IV | **7/7** ✅ | — |
| V | **14/17** ✅ | Maldives, Lebanon, Yemen |
| VI | **2/8** ⚠️ (Timor-Leste, Vanuatu) | Fiji, Kiribati, PNG, Samoa, Solomon, Tonga |

## C. Diễn giải chính (gradient thể chế — hợp lệ vì toàn biến tỷ lệ/nhị phân)

1. **Năng lực đổi mới giảm dần theo gradient thể chế**: R&D 20,5%→5,7%; ISO 35%→6,6%; website 61,7%→28,9% (I→VI).
2. **Tham nhũng tăng ngược gradient**: trở ngại lớn 2,9% (I) → 22,7% (IV) → 24,9% (VI); hối lộ %doanh thu 0,2→2,5.
3. **Quốc tế hóa**: tỷ lệ DN xuất khẩu giảm I (28,4%) → VI (10,4%) — nhất quán câu chuyện FIP: SIDS ít DN xuất khẩu nhưng những DN xuất khẩu chịu gánh nặng.
4. Nhóm II (chỉ Bahrain+Brunei) có innovation cao bất thường (53,9%) — artifact coverage, KHÔNG dùng làm đại diện GCC.

## D. Quyết định đồng bộ với CĐ1 (khuyến nghị)

- **Nhóm I, III, IV, V** (coverage đủ): có thể đồng bộ bảng CĐ1 §2.3.4 (đổi mới/số hóa), §2.3.5 (cấu trúc), §2.3.6 (tham nhũng) bằng số pipeline — kèm chú thích "tái tính trên khung 49 nền từ raw WBES".
- **Nhóm II, VI**: GIỮ số bản khóa mô tả CĐ1 (hoặc dùng số master cho biến có sẵn) cho tới khi có raw GCC (Saudi/Qatar/Kuwait/Oman) + Pacific (6 nền); pipeline tự cập nhật khi bổ sung file (idempotent).
- Việc thay số vào prose CĐ1 nên do tác giả duyệt từng bảng (số cũ từ pool mô tả 101.185 khác định nghĩa).
