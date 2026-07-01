# Manifest cập nhật dữ liệu WBES — Japan + sóng mới 2024–2026

> Ngày 2026-06-11. Kho raw `data_wbes/raw_dta/` đã: (i) nạp đủ **49/49 nền** khung phân tích;
> (ii) thêm **Japan-2025** (nền mới, ngoài khung 49/52); (iii) loại đợt **trước 2006**
> (bộ câu hỏi không so sánh được); (iv) **dedupe theo nước-năm**. Tái lập:
> `scripts/wbes_canon.py` + `scripts/cd1_descriptives_pipeline.py`.

## 1. Ranh giới năng lực (QUAN TRỌNG — đọc trước)

| Tầng | Có thể cập nhật bằng AI? |
|---|---|
| **Dữ liệu thô + kho** (ingest, dedupe, lọc) | Có Đã làm |
| **Mô tả/phân loại** (đếm, ICRV, bảng descriptive) | Có Làm được từ raw |
| **Kết quả KINH TẾ LƯỢNG** (turning point, hệ số FIP, điều tiết của P3–P9) | Không **KHÔNG** — phải chạy lại mô hình Stata/R thực tế; không được bịa hệ số |

 đến Việc "cập nhật P3–P9 với data mới" đòi hỏi **tác giả chạy lại mô hình** trên bộ data mở rộng. Manifest này chuẩn bị đầu vào cho việc đó.

## 2. Trạng thái công bố (theo xác nhận của NCS)

| Nghiên cứu | Trạng thái | Hệ quả với data mới |
|---|---|---|
| P1, P2 | **Đã công bố** | Khóa — không đổi |
| Book chapter (India, IntechOpen 2025) | **Đã công bố** | Khóa — không đổi |
| Meta-analysis (P6, 2025) | **Đã công bố** | Khóa — không đổi |
| P3, P4, P5, P7, P8, P9 | **Đang bình duyệt** | CÓ THỂ cập nhật khi tác giả chạy lại mô hình với data mở rộng |

## 3. Japan-2025 — hồ sơ nền mới (Nhóm I ứng viên)

Khảo sát WBES **lần đầu** cho Japan (2025) đến KHÔNG thể có trong bất kỳ kết quả P1–P9
hiện tại. Hồ sơ mô tả (2.168 DN):

| Chỉ tiêu | Japan-2025 | Nhóm I hiện tại (5 nền) |
|---|--:|--:|
| Đổi mới sản phẩm | 32,2 | 24,3 |
| R&D | 21,9 | 20,5 |
| Website | **83,8** | 61,7 |
| ISO | 27,7 | 35,0 |
| Nữ quản lý cấp cao | 7,3 | 27,5 |
| DN xuất khẩu | 16,8 | 28,4 |
| FDI ≥10% | 1,9 | 10,6 |
| FSTS trung bình | 4,1 | 13,4 |
| Tuổi DN TB (năm) | **50,4** | 23,0 |

Đặc trưng: số hóa rất cao (website 83,8%), DN rất lâu đời (50 năm), nữ lãnh đạo thấp,
quốc tế hóa thấp bất ngờ (FSTS 4,1% — thị trường nội địa lớn). Phù hợp Nhóm I về thể chế
nhưng pattern quốc tế hóa khác biệt đến **nếu đưa vào khung sẽ là case lý thú**.

## 4. Khuyến nghị xử lý Japan + sóng mới

- **Khung PHÂN TÍCH (econometrics)**: **giữ 49 nền** cho mọi kết quả P3–P9 trong luận án
  hiện tại (khớp số đã/đang bình duyệt). Đổi 49 đến 50 mà không chạy lại mô hình sẽ tạo mâu
  thuẫn frame-vs-results khắp luận án — KHÔNG nên.
- **Khung PHÂN LOẠI/mô tả**: có thể ghi nhận Japan là nền thứ 50 (Nhóm I) ở tầng mô tả,
  **kèm chú thích minh bạch** "Japan 2025 mới khảo sát lần đầu, đưa vào phân loại; chưa
  nhập vào mô hình kinh tế lượng — dành cho vòng ước lượng kế tiếp."
- **Vòng revise P3–P9**: khi tác giả chạy lại mô hình, dùng bộ raw đã mở rộng trong kho
  (31 nền có sóng ≥2024 + Japan) — danh sách ở Mục 5.

## 5. 31 nền có sóng mới ≥2024 (đầu vào cho re-estimate)

Afghanistan(2025), Armenia(2024), Azerbaijan(2024), Bahrain(2024), Bhutan(2024),
Brunei(2025), China(2024), Comoros(2025), Fiji(2025), India(2025), Israel(2024),
Japan(2025)*, Jordan(2024), Kazakhstan(2024), Kiribati(2025), Korea(2024),
Kuwait(2025), Laos(2024), Malaysia(2024), Maldives(2025), Oman(2026),
PapuaNewGuinea(2024), Qatar(2025), SaudiArabia(2025), SolomonIslands(2025),
SriLanka(2025), Taiwan(2024), Tajikistan(2024), Thailand(2025), Tonga(2024),
Turkmenistan(2024), Uzbekistan(2024).

(*Japan ngoài khung 49/52 hiện tại.)

## 6. Việc đã đồng bộ vào CĐ1 (tầng mô tả, an toàn)

Bảng 2.3.3.2 / 2.3.4.1 / 2.3.5.1 đã cập nhật theo raw đủ 49/49 nền (dedupe, ≥2006).
Các kết quả kinh tế lượng (turning point P5, FIP P8, gradient P7…) trong luận án
**giữ nguyên** số đã/đang bình duyệt — chờ tác giả chạy lại nếu muốn mở rộng mẫu.
