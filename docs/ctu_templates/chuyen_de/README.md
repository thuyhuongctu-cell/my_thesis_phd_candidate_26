# Templates hành chính cho Chuyên đề / Tiểu luận tổng quan (TLTQ)

Tài liệu chính thức do NCS Đỗ Thùy Hương nhận từ Khoa Sau đại học, Trường Đại học Cần Thơ. Các template DOCX này là **form do CTU cung cấp** — NCS điền thông tin và in ra ký tên.

## Danh sách 5 templates

| # | File | Mục đích | Người điền |
|---|---|---|---|
| 1 | `NCS_Huong_dan_viet_TLTQ.docx` | **Hướng dẫn về yêu cầu của TLTQ và Chuyên đề tiến sĩ** — định nghĩa cấu trúc CĐ/TLTQ | (đọc tham khảo) |
| 2 | `NCS_Phieu_dang_ky_bao_cao_TLTQ.docx` | Phiếu đăng ký báo cáo CĐ/TLTQ gửi Khoa SĐH | NCS điền + ký + NHD ký |
| 3 | `NCS_Tom_tat_qua_trinh_TLTQ.docx` | Tóm tắt quá trình thực hiện CĐ/TLTQ (gửi kèm phiếu đăng ký) | NCS điền + ký + NHD ký |
| 4 | `Phieu_cham_diem_TLTQ.docx` | Phiếu chấm điểm CĐ/TLTQ | 3 thành viên Tiểu ban chấm |
| 5 | `Bien_ban_hop_cham_TLTQ.docx` | Biên bản họp Tiểu ban chấm điểm CĐ/TLTQ | Trưởng + Thư ký Tiểu ban |

## Cấu trúc CĐ/TLTQ chuẩn CTU (theo file `NCS_Huong_dan_viet_TLTQ.docx`)

### Phần 1 — Thông tin chung

1. Tên chuyên đề
2. Mục lục
3. Tóm tắt
4. Danh mục từ viết tắt + định nghĩa thuật ngữ (nếu có)

### Phần 2 — Nội dung CĐ/TLTQ

**2.1 Đặt vấn đề**
- 2.1.1 Giới thiệu (tình hình NC trong và ngoài nước + mối quan hệ với LATS)
- 2.1.2 Mục tiêu (mục tiêu cụ thể của CĐ)
- 2.1.3 Nội dung (các nội dung chính)
- 2.1.4 Giới hạn của CĐ/TLTQ (nội dung, lĩnh vực, không gian, thời gian)
- 2.1.5 Ý nghĩa (học thuật + liên quan luận án)

**2.2 Phương pháp nghiên cứu**
Trình bày rõ phương pháp thu thập tài liệu, tổng hợp và xử lý kết quả. Nếu CĐ có lồng ghép kết quả NC của NCS thì trình bày rõ phương pháp thực hiện.

**2.3 Kết quả và thảo luận**
Trình bày kết quả NC trong và ngoài nước về chủ đề CĐ/TLTQ. Trích dẫn ngắn gọn, xúc tích, có trọng tâm. **Phải lồng ghép ý kiến thảo luận của NCS.**

**2.4 Kết luận và đề xuất**
Trình bày kết quả quan trọng từ tổng hợp + những vấn đề còn khuyết + đề xuất NC tiếp theo, **đặc biệt liên hệ với đề tài luận án**.

**Tài liệu tham khảo** — APA hoặc IEEE per QĐ 1799.

### Hình thức trình bày

> "Hình thức và cách viết Chuyên đề/Tiểu luận tổng quan phải tuân thủ như Hướng dẫn và trình bày luận án tiến sĩ do Trường ban hành theo Quyết định số 1799/QĐ-ĐHCT ngày 18/6/2021 của Đại học Cần Thơ."

→ Áp dụng `templates/ctu_thesis_strict.docx`: TNR 13pt, 1.2 spacing, 1cm first-line indent, margins 2-3-2-2.

## Áp dụng cho NCS Đỗ Thùy Hương

Per QĐ 4768/QĐ-ĐHCT (15/10/2024):

| | Tên | NHD |
|---|---|---|
| **Chuyên đề 1** | Thực trạng về hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á | TS. Nguyễn Minh Cảnh |
| **Chuyên đề 2** | Xây dựng mô hình nghiên cứu về ảnh hưởng của quốc tế hóa đến hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á | PGS.TS. Phan Anh Tú |
| **Tiểu luận tổng quan** | Tổng quan tài liệu về ảnh hưởng của quốc tế hóa đến hiệu quả hoạt động kinh doanh | PGS.TS. Phan Anh Tú |

Trang bìa các CĐ/TLTQ: xem `templates/cover_pages/08_*.docx` (CĐ1), `09_*.docx` (CĐ2), `10_*.docx` (TLTQ).

## Mapping với nội dung hiện tại trong repo

| Yêu cầu CĐ/TLTQ chuẩn | File hiện tại trong repo | Compliance |
|---|---|---|
| **CĐ1 — Thực trạng FP doanh nghiệp Châu Á** | `thesis/14_cd1_part1_intro_theory_vi.md` + `15_*` + `16_*` | ⚠ Cấu trúc 7 chương non-standard so với 2.1-2.4. NCS cần **decide**: (a) restructure CĐ1 thành 2.1-2.4, hoặc (b) giữ enriched structure + thêm crosswalk paragraph mở đầu chỉ rõ mapping |
| **CĐ2 — Mô hình nghiên cứu** | `thesis/02_theoretical_framework_vi.md` | ✅ Phù hợp 2.1 + 2.2 (framework + methodology). Có thể bổ sung 2.3 (synthesis của 3-layer hierarchy) + 2.4 (proposed implementation plan) |
| **TLTQ — Tổng quan tài liệu I-P** | (chưa có file cụ thể) | ⚠ Cần soạn TLTQ riêng dựa trên `chuong_2_tong_quan_tai_lieu_vi.md` + meta-analysis P6 |
