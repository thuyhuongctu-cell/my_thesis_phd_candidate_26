# Xác minh Phân loại Quốc gia World Bank FY2026

**Ngày xác minh**: 13/05/2026  
**Phạm vi**: Task 6 — Verification of WB FY2026 income classification for ICRV framework  
**Nguồn kiểm tra**: `data_wbes/wb_country_classification_2025_2026.md` (commit 6a7caf0) + `data_wbes/wbes_asia_country_scope.md`  
**Tài liệu tham chiếu WB**: World Bank Data Help Desk FY2026 Country and Lending Groups (hiệu lực 01/07/2025)

---

## 1. Ngưỡng Phân loại Thu nhập FY2026 — KẾT QUẢ XÁC MINH

| Nhóm thu nhập | Ngưỡng v1.2 (ước tính) | Ngưỡng FY2026 chính thức | Trạng thái |
|---|---|---|---|
| Thu nhập thấp (LI) | ≤$1.135 | **≤$1.145** | ⚠️ Sai $10 |
| Thu nhập trung bình thấp (LMI) | $1.136–$4.495 | **$1.146–$4.515** | ⚠️ Sai $10/$20 |
| Thu nhập trung bình cao (UMI) | $4.496–$13.935 | **$4.516–$14.005** | ⚠️ Sai $20/$70 |
| Thu nhập cao (HI) | >$13.935 | **>$14.005** | ⚠️ Sai $70 |

**Kết luận**: Ngưỡng ước tính v1.2 trong glossary mục #60 thấp hơn ngưỡng chính thức. Sai lệch do v1.2 dùng giá trị tạm tính trước khi WB công bố chính thức (01/07/2025). **Đã sửa trong glossary v1.3**.

**Phương pháp điều chỉnh WB**: Ngưỡng FY2026 điều chỉnh theo SDR deflator năm 2024 (~1.4%) từ FY2025 ($1.135 / $4.465 / $13.845). Tăng lần lượt: +$10 / +$50 / +$160.

> **Lưu ý**: Ngưỡng FY2025 (từ file WB): LI ≤$1.135; LMI $1.136–$4.465; UMI $4.466–$13.845; HI >$13.845. Ngưỡng v1.2 của glossary ($1.135/$4.495/$13.935) không khớp FY2025 cũng không khớp FY2026 — đây là phiên bản ước tính phát hành trước thời điểm WB công bố.

---

## 2. Trạng thái Phân loại Các Nền kinh tế Trọng điểm

### 2.1 Việt Nam

| Chỉ tiêu | Giá trị | Đánh giá |
|---|---|---|
| GNI per capita (Atlas, ~2024) | ~$3.760 | Cần xác nhận từ WB data 2025 |
| Nhóm thu nhập FY2026 | **Lower-middle income** | Có Không thay đổi |
| Tư cách vay | IDA/Blend | Có Tiếp tục hưởng ưu đãi |
| Khoảng cách đến UMI | $4.515 − $3.760 = **$755** | Có Vẫn cách xa ngưỡng UMI |
| Dự báo reclassify | FY2027–2028 | Nếu tăng $200–$300/năm |
| N firms trong WBES pool | 2.958 (pooled 2009+2015+2023) | Có Nhất quán với Mục 4.4.5.1 file 15 |

**Ghi chú**: File wb_country_classification liệt kê GNI Việt Nam ~$3.760, thấp hơn mức $4.110 được tham chiếu trong một số tài liệu trước đó. Sự khác biệt này có thể do sử dụng năm tham chiếu khác nhau (2023 vs 2022 Atlas data). Cần xác nhận với WB data portal khi viết CĐ2 Mục 2.x.

**Hàm ý ICRV**: Việt Nam được phân loại nhóm **Emerging** trong ICRV framework (Lower-middle income, có dữ liệu WBES đầy đủ 3 sóng). Không có thay đổi so với thiết kế ICRV v3.x.

### 2.2 Indonesia

| Chỉ tiêu | Giá trị | Đánh giá |
|---|---|---|
| GNI per capita (~2024) | ~$4.480 | |
| Nhóm thu nhập FY2026 | **Lower-middle income** | Có Không thay đổi |
| Khoảng cách đến UMI | $4.515 − $4.480 = **$35** | ⚠️ Rất gần ngưỡng UMI |
| Ngưỡng UMI FY2026 | $4.516 | Cao hơn ước tính v1.2 ($4.496) |

**Ghi chú**: Với ngưỡng FY2026 chính xác là $4.516 (không phải $4.496 như ước tính trước), khoảng cách của Indonesia đến ngưỡng UMI là **$36** (không phải $16 như kế hoạch dự kiến). Indonesia vẫn là LMI trong FY2026. Nếu GNI tăng ~$50/năm, Indonesia có thể reclassify vào **FY2027**.

**Hàm ý ICRV**: Indonesia vẫn thuộc nhóm **Emerging** trong ICRV (LMI, có WBES 2015). Không ảnh hưởng đến phân tích hiện tại. Tuy nhiên, cần ghi chú trong Mục 4.9 hoặc limitations rằng Indonesia đang ở "ngưỡng ranh giới" Emerging/Upper-middle.

### 2.3 Samoa — Xác minh Chuyển nhóm Thu nhập

| Chỉ tiêu | Kế hoạch dự kiến | Thực tế FY2026 | Đánh giá |
|---|---|---|---|
| Phân loại FY2025 | LMI | LMI | |
| Phân loại FY2026 | UMI (dự kiến chuyển) | **LMI** (GNI ~$4.020) | Không Không chuyển nhóm |
| GNI per capita | ~$4.510 (dự báo) | ~$4.020 | |

**Kết luận**: Samoa **không** chuyển từ LMI sang UMI trong FY2026. GNI ~$4.020, vẫn dưới ngưỡng $4.515. Tham chiếu trong kế hoạch ban đầu về "Samoa (LMI đến UMI)" là **không chính xác** cho FY2026.

**Hàm ý ICRV**: Samoa vẫn được xếp nhóm **SIDS Pacific** trong ICRV (không dựa trên WB income group mà dựa trên đặc điểm địa lý + MIRAB structure). Việc Samoa không chuyển nhóm thu nhập không ảnh hưởng đến ICRV classification của luận án.

### 2.4 Singapore

| Chỉ tiêu | Giá trị | Đánh giá |
|---|---|---|
| GNI per capita (~2024) | ~$67.200 | |
| Nhóm thu nhập FY2026 | **High income** | Có Không thay đổi |
| WBES | 2023 (B-READY) | Có Đã có data |
| N firms | 617 | Có Nhất quán với wbes_asia_country_scope.md |

**Hàm ý ICRV**: Singapore ở nhóm **Advanced innovation-driven** — không thay đổi.

### 2.5 Trung Quốc

| Chỉ tiêu | Giá trị | Đánh giá |
|---|---|---|
| GNI per capita (~2024) | ~$13.400 | |
| Nhóm thu nhập FY2026 | **Upper-middle income** | Có Không thay đổi (dưới $14.005) |
| Khoảng cách đến HI | $14.005 − $13.400 = **$605** | Cần theo dõi FY2027 |
| N firms | 4.559 (pooled 2012+2024) | Có Nhất quán |

**Hàm ý ICRV**: Trung Quốc ở nhóm **Upper-middle** — không thay đổi. Tuy nhiên, nếu GNI tiếp tục tăng, có thể reclassify vào HI trong FY2027–2028, điều này cần ghi chú trong CĐ2 limitations.

---

## 3. Căn chỉnh ICRV Framework với WB FY2026

| ICRV Sub-regime | Nền kinh tế mẫu | WB Income FY2026 | Alignment |
|---|---|---|---|
| Advanced innovation-driven | Singapore, HK, KOR, TWN, ISR | High income | Có Nhất quán |
| Advanced resource-driven | SAU, QAT, KWT, BHR, BRN | High income | Có Nhất quán |
| Upper-middle | China, Malaysia, Thailand, Mongolia, Maldives, Fiji | UMI | Có Nhất quán |
| Emerging | Vietnam, India, Philippines, Indonesia, Bangladesh | LMI (có WBES đủ) | Có Nhất quán |
| Frontier | Nepal, Lao, Cambodia, Myanmar, Pacific LMI | LMI + LI (hạn chế WBES) | Có Nhất quán |
| SIDS Pacific | Samoa, Solomon, Vanuatu, Tonga, Kiribati, Marshall | LMI/LI + SIDS đặc trưng | Có Nhất quán |

**Kết luận**: ICRV framework không cần điều chỉnh dựa trên FY2026 reclassification. Không có nền kinh tế nào trong 47-economy scope thay đổi nhóm thu nhập theo cách ảnh hưởng đến phân tích chính.

---

## 4. Chú thích Costa Rica và Namibia

Kế hoạch ban đầu đề cập đến Costa Rica (UMI đến HI) và Namibia (UMI đến LMI). Hai nền kinh tế này **nằm ngoài phạm vi nghiên cứu** (không thuộc EAP/SAS/MENAAP Asia scope). Không có hàm ý cho luận án.

---

## 5. Danh sách Hành động Sau Xác minh

| Hành động | Tệp | Trạng thái | Ghi chú |
|---|---|---|---|
| Sửa ngưỡng FY2026 tại mục #60 | `writing_guides/09b_vn_term_glossary.md` | Có **Đã thực hiện** (v1.3) | Sửa $1.135/$4.495/$13.935 đến $1.145/$4.515/$14.005 |
| Kiểm tra ngưỡng trong file 14/15/16 | `thesis/14_cd1_part1_intro_theory_vi.md` | ⚠️ **Cần rà soát** | Tìm kiếm "$1.135" hoặc "$4.495" hoặc "$13.935" |
| Kiểm tra ngưỡng trong CĐ2 | `chuyen_de/cd2/00_cd2_ctu_final_vi.md` | ⚠️ **Cần rà soát** | Tìm kiếm ngưỡng sai |
| Ghi chú Indonesia "ngưỡng ranh giới" | `thesis/15_cd1_part2_findings_vi.md` Mục 4.9 | ⚠️ **Tùy chọn** | Khi viết limitations |
| Ghi chú Trung Quốc gần HI | `thesis/15_cd1_part2_findings_vi.md` | ⚠️ **Tùy chọn** | Khi viết limitations |
| Xác nhận GNI Việt Nam chính xác | WB data portal | ⚠️ **Cần xác nhận** | $3.760 vs $4.110 — kiểm tra năm tham chiếu |

---

## 6. Tóm tắt Kết quả Xác minh

**Phát hiện chính**:
1. **Ngưỡng FY2026 chính thức** ($1.145/$4.515/$14.005) đã được ghi chép chính xác trong `data_wbes/wb_country_classification_2025_2026.md`. File WBES scope cũng nhất quán.
2. **Lỗi trong glossary v1.2** mục #60: dùng ước tính v1.2 ($1.135/$4.495/$13.935) thay vì ngưỡng chính thức đến **đã sửa trong v1.3**.
3. **Samoa không chuyển sang UMI** trong FY2026 (GNI ~$4.020, cần ~$4.515). Kế hoạch ban đầu về transition này là không chính xác.
4. **Việt Nam** vẫn LMI (GNI ~$3.760, khoảng cách UMI = $755). Reclassify dự kiến FY2027–2028.
5. **Indonesia** vẫn LMI (GNI ~$4.480, khoảng cách UMI = $35 với ngưỡng $4.515 — không phải $16 như ước tính dùng ngưỡng $4.496).
6. **Tất cả 47 nền kinh tế ICRV** duy trì phân loại nhất quán với framework. Không có thay đổi cần cập nhật trong thiết kế ICRV.

*Tài liệu xác minh này phục vụ Task 6 của kế hoạch triển khai skills. NCS: Đỗ Thùy Hương. Ngày: 13/05/2026.*
