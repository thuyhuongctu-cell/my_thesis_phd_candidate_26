# Tổng quan luận án — gói tài liệu định hướng

> NCS Đỗ Thùy Hương · GVHD: PGS.TS. Phan Anh Tú · Cập nhật 2026-06-23.
> Đề tài: **Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở châu Á.**

Bốn tài liệu tổng quan, đọc theo thứ tự:

| # | Tài liệu | Nội dung |
|---|---|---|
| 1 | [`01_gioi_thieu_chung_du_an.md`](01_gioi_thieu_chung_du_an.md) | Giới thiệu chung dự án: đề tài, hình thức tổng hợp, dữ liệu WBES, khung CDCM–ICRV–FIP, câu hỏi nghiên cứu, tuyên bố trung tâm, cấu trúc 5 chương |
| 2 | [`02_truc_quan_hoa_quan_he.md`](02_truc_quan_hoa_quan_he.md) | Trực quan hóa (sơ đồ Mermaid) quan hệ papers ↔ chuyên đề ↔ chương; bảng "sợi chỉ vàng" tích hợp |
| 3 | [`03_dong_gop_va_tinh_moi.md`](03_dong_gop_va_tinh_moi.md) | Tính đóng góp & tính mới: 4 đóng góp lý thuyết, đóng góp tích hợp, phương pháp/dữ liệu, ghi chú liêm chính |
| 4 | [`04_vi_tri_trong_literature.md`](04_vi_tri_trong_literature.md) | Vị trí trong literature: so với 6 chương trình nghiên cứu, 4 công trình kinh điển, mảng luận án châu Á/Việt Nam; ma trận khác biệt |

## Nguồn gốc & tính nhất quán

- Số liệu khớp `data_wbes/analysis/CANONICAL_NUMBERS.md` (khung canonical 50 nền / 88.869 DN / 103 cặp nền–năm).
- Nội dung tổng hợp từ: `thesis/chuong_5_ket_luan_de_xuat_vi.md` (§5.1–5.3, Bảng 5.1 sợi chỉ vàng), `thesis/11_dissertation_positioning_vi.md` (định vị), `thesis/kappa_synthesis_en.md` (bài luận tổng hợp).
- Mọi headline đã tái lập từ vi dữ liệu thô WBES bằng Python tương đương Stata: `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`.

## Ghi chú liêm chính (giữ tường minh)

- **P3** Việt Nam: Python tái lập đúng *dạng* (chữ U ngược); độ lớn điểm uốn 39–46% cần Stata gốc (mẫu số `b1_d`).
- **P8** SIDS: headline là **dissolution** (N=1.450); β=−1,339 chỉ là trường hợp giới hạn minh họa (3 cụm), không phải kết quả chính.
- **P6** meta: r̄/k/Q_M đã tái lập; I²/lệch công bố cần R `metafor`.
