# Cover Page Templates — NCS Đỗ Thùy Hương

Tất cả các trang bìa, lời cam đoan, trang chấp thuận Hội đồng theo **QĐ 1799/QĐ-ĐHCT (18/6/2021)** và **QĐ 4768 + 4769/QĐ-ĐHCT (15/10/2024)**.

## Thông tin định danh đã điền sẵn

| Item | Giá trị |
|---|---|
| Họ tên NCS | Đỗ Thùy Hương |
| Mã số NCS | P1323001 |
| Ngành | Quản trị kinh doanh |
| Mã ngành | 9340101 |
| Khóa | 2023 đợt 1 |
| Tên LATS | Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á |
| NHD LATS | PGS.TS. Phan Anh Tú |
| NHD CĐ1 | TS. Nguyễn Minh Cảnh |
| NHD CĐ2 + TLTQ | PGS.TS. Phan Anh Tú |

## Danh sách 10 templates

| # | File | Phụ lục QĐ 1799 | Mục đích |
|---|---|---|---|
| 1 | `01_trang_bia_chinh_LATS.md` | Phụ lục 1b | Bìa cứng MÀU ĐỎ BORDEAUX cho LATS |
| 2 | `02_trang_phu_bia_LATS.md` | Phụ lục 2b | Trang phụ bìa LATS (có NHD) |
| 3 | `03_trang_chap_thuan_hoi_dong.md` | Phụ lục 3b | Chấp thuận của Hội đồng đánh giá LATS (7 chữ ký) |
| 4 | `04_loi_cam_doan.md` | Phụ lục 10 | Lời cam đoan của tác giả |
| 5 | `05_tom_tat_LATS_bia_1.md` | Phụ lục 4a | Bìa 1 quyển Tóm tắt LATS (A5, đỏ bordeaux) |
| 6 | `06_tom_tat_LATS_bia_2.md` | Phụ lục 4b | Bìa 2 — CÔNG TRÌNH ĐƯỢC HOÀN THÀNH TẠI CTU |
| 7 | `07_tom_tat_LATS_bia_3_cong_trinh.md` | Phụ lục 4c | Bìa 3 — Danh mục công trình đã công bố |
| 8 | `08_trang_bia_chuyen_de_1.md` | (theo QĐ 1799 + 4768) | Trang bìa Chuyên đề 1 — Thực trạng |
| 9 | `09_trang_bia_chuyen_de_2.md` | (theo QĐ 1799 + 4768) | Trang bìa Chuyên đề 2 — Mô hình |
| 10 | `10_trang_bia_TLTQ.md` | (theo QĐ 1799 + 4768) | Trang bìa Tiểu luận tổng quan |

## Build to DOCX

```bash
# Build all cover pages
for f in templates/cover_pages/[0-9]*.md; do
  base=$(basename "$f" .md)
  pandoc "$f" -o "templates/cover_pages/${base}.docx" \
    --reference-doc=templates/ctu_thesis_strict.docx
done
```

Output sẽ vào `templates/cover_pages/01_*.docx` ... `10_*.docx`.

## NCS lưu ý

1. **Bìa cứng**: Khi in thật bìa LATS phải làm bằng **chất liệu bìa cứng MÀU ĐỎ BORDEAUX**, chữ trên bìa cứng là **chữ nhũ vàng** in hoa (per QĐ 1799 §2.3.1.1). Templates in trên giấy A4 trắng chỉ để chuẩn bị nội dung, in chính thức cần in màu/cán plastic theo dịch vụ in tiêu chuẩn.

2. **Gáy bìa**: Khi đóng cứng bìa, gáy phải có: `Đỗ Thùy Hương – Luận án tiến sĩ – 2026` (kiểu chữ in hoa đậm, cỡ 14).

3. **Tóm tắt LATS**: Khổ A5 (140 × 210 mm = A4 gấp đôi). In tối đa 24 trang, hai mặt. Lề trên/dưới/phải: 1.5 cm; lề trái: 2.0 cm.

4. **Năm 2026**: Templates dùng `NĂM 2026` — NCS điều chỉnh nếu nộp năm khác.

5. **Trang chấp thuận Hội đồng**: 7 chữ ký theo LATS (3 phản biện + 3 ủy viên + 1 thư ký + 1 chủ tịch + 1 hướng dẫn = 9 spots; thông thường tiểu ban có 7 thành viên — điều chỉnh theo thực tế hội đồng).
