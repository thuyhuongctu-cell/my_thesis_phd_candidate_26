# CTU Official Templates & Decisions

Trung tâm chính thức cho mọi tài liệu CTU mà NCS Đỗ Thùy Hương cần.

## Cấu trúc thư mục

```
docs/ctu_templates/
├── README.md                          # File này
├── NCS_PERSONAL_INFO.md               # Thông tin định danh + QĐ chính thức (PRIVATE)
├── qd_official/                       # 3 PDF chính thức từ CTU
│   ├── QD_4768_giao_chuyen_de_TLTQ.pdf       # Giao CĐ/TLTQ
│   ├── QD_4769_dieu_chinh_ten_LATS.pdf       # Điều chỉnh tên LATS
│   └── HuongDan_QD_1799_trinh_bay_LVThS_LATS.pdf  # Hướng dẫn QĐ 1799 (63 pages)
└── chuyen_de/                         # 5 DOCX hành chính cho CĐ/TLTQ
    ├── README.md                                  # Hướng dẫn dùng + structure CĐ
    ├── NCS_Huong_dan_viet_TLTQ.docx               # Hướng dẫn cấu trúc CĐ/TLTQ
    ├── NCS_Phieu_dang_ky_bao_cao_TLTQ.docx        # Phiếu đăng ký báo cáo CĐ
    ├── NCS_Tom_tat_qua_trinh_TLTQ.docx            # Tóm tắt quá trình thực hiện
    ├── Phieu_cham_diem_TLTQ.docx                  # Phiếu chấm điểm CĐ
    └── Bien_ban_hop_cham_TLTQ.docx                # Biên bản họp tiểu ban chấm

templates/
├── ctu_thesis_reference.docx          # Legacy reference (1.2 line spacing — OK)
├── ctu_thesis_strict.docx             # ✅ STRICT — verified per QĐ 1799 §2.2.1-2.2.3
├── ctu_paper_reference.docx           # Cho journal manuscripts (P-papers)
├── ctu_tomtat_reference.docx          # Cho summary documents
└── cover_pages/                       # 10 trang bìa templates (xem README riêng)
    ├── README.md
    ├── 01_trang_bia_chinh_LATS.{md,docx}
    ├── 02_trang_phu_bia_LATS.{md,docx}
    ├── 03_trang_chap_thuan_hoi_dong.{md,docx}
    ├── 04_loi_cam_doan.{md,docx}
    ├── 05_tom_tat_LATS_bia_1.{md,docx}
    ├── 06_tom_tat_LATS_bia_2.{md,docx}
    ├── 07_tom_tat_LATS_bia_3_cong_trinh.{md,docx}
    ├── 08_trang_bia_chuyen_de_1.{md,docx}
    ├── 09_trang_bia_chuyen_de_2.{md,docx}
    └── 10_trang_bia_TLTQ.{md,docx}
```

## 3 QĐ chính thức từ CTU

| QĐ | Ngày | Mục đích |
|---|---|---|
| 1799/QĐ-ĐHCT | 18/6/2021 | **Hướng dẫn trình bày LVThS/LATS** — 63 pages, source of truth cho format |
| 4768/QĐ-ĐHCT | 15/10/2024 | **Giao Chuyên đề và Tiểu luận tổng quan** cho NCS Đỗ Thùy Hương |
| 4769/QĐ-ĐHCT | 15/10/2024 | **Điều chỉnh tên LATS** — chính thức: "Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á" |

## Build commands

```bash
# Build 10 cover-page templates to DOCX
bash scripts/build_ctu_cover_pages.sh

# Build all dissertation chapters + chuyên đề with CTU-strict format
bash scripts/build_ctu_thesis_strict.sh
```

## Tài liệu liên quan

- `docs/CTU_FORMATTING_GUIDE.md` — Full guide 20 sections theo QĐ 1799
- `templates/cover_pages/README.md` — Hướng dẫn 10 trang bìa
- `docs/ctu_templates/chuyen_de/README.md` — Structure chuẩn CĐ/TLTQ + mapping với repo hiện tại
