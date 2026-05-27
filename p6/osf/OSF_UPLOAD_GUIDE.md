# Hướng dẫn tải gói tài liệu P6 lên OSF

> Tài liệu này dành cho **bạn** (người nộp), KHÔNG tải lên OSF. Gói cần tải nằm ở
> `p6/osf/upload_package/`. Dự án OSF đích đã tồn tại: **https://osf.io/z37kn**
> (DOI `10.17605/OSF.IO/Z37KN`, đã đăng ký preregistration 2026-05-18).

## Bối cảnh quan trọng
- OSF là **bản ghi mở, KHÔNG ẩn danh** → giữ nguyên tên tác giả (khác với bản nộp tạp chí phải ẩn).
- Dữ liệu/kết quả trong gói là **pool baseline (k=238 / K=288)** đã đăng ký và phân tích xong.
  Phần mở rộng formal-search (mục tiêu k≥250) và độ tin cậy liên-mã hóa (inter-coder) **đang làm dở** →
  xem mục "TẠM GIỮ" bên dưới.

## Cấu trúc gói (`p6/osf/upload_package/`)
```
00_START_HERE.md            ← README, tải LÊN OSF (làm mô tả/wiki dự án)
1_Preregistration/          ← bản preregistration
2_Search_and_Screening/     ← chiến lược tìm kiếm WoS+Scopus, PRISMA flow + checklist, template sàng lọc
3_Data/                     ← database 288 effect-size + codebook + danh mục nghiên cứu (APA7)
4_Analysis_Code/            ← parse (py) → MARA 3 tầng (R/metafor) → vẽ hình (py)
5_Results/                  ← table1–5 + forest_data (kết quả baseline)
```

## Manifest — nguồn ↔ đích
| File trong gói | Nguồn trong repo | Trạng thái |
|---|---|---|
| `1_Preregistration/P6_preregistration.md` | `p6/osf/P6_OSF_Preregistration_Template.md` | ✅ Sẵn sàng |
| `2_*/search_strategy_WoS_Scopus.md` | `p6/p6_wos_search_guide.md` | ✅ |
| `2_*/PRISMA_2020_flow.md` · `…_checklist.md` | `p6/p6_prisma_flow.md` · `p6/p6_prisma_checklist.md` | ✅ |
| `2_*/screening_template.csv` | `p6/p6_wos_screening_template.csv` | ✅ |
| `3_Data/p6_study_database_baseline.csv` | `p6/data/p6_study_database.csv` | ✅ (baseline) |
| `3_Data/codebook.md` | `p6/tools/p6_extraction_codebook.md` | ✅ |
| `3_Data/primary_studies_APA7.md` | `p6/p6_primary_studies_apa7.md` | ✅ |
| `4_Analysis_Code/*` | `p6/scripts/p6_real_mara.R`, `p6/scripts/p6_parse_database.py`, `p6/figures/generate_p6_figures.py` | ✅ |
| `5_Results/*.csv` | `p6/results/*.csv` | ✅ (baseline) |

## Các bước tải lên (thủ công, ~10 phút)
1. Đăng nhập **osf.io** → mở dự án **z37kn**.
2. Vào tab **Files** → khung **OSF Storage** → kéo-thả từng thư mục `1_…` → `5_…` và file `00_START_HERE.md`.
   (Hoặc tạo **Components** riêng cho mỗi nhóm nếu muốn cấu trúc rõ hơn: Preregistration / Search & Screening / Data / Code / Results.)
3. Dán nội dung `00_START_HERE.md` vào phần **Description** hoặc tab **Wiki** của dự án.
4. Thiết lập **License**: Settings → CC-BY 4.0 (tài liệu/mã) ; cân nhắc CC0 cho dataset.
5. Bấm **Make Public** khi sẵn sàng công khai (preregistration đã active sẵn).

## ⛔ TẠM GIỮ — chưa tải lên cho tới khi hoàn tất
- Dataset **pool mở rộng** + thư mục `p6/scripts/.../results/updated/` (formal-search k≥250 đang chạy).
- File tracker đang làm dở: `p6/tools/results/fulltext_to_extraction_tracker_v3.csv` (WIP, ~2.467 dòng).
- **Bảng độ tin cậy liên-mã hóa** (inter-coder reliability — Bảng 3.1 hiện còn `[TBD]`).
- **Bản thảo / preprint** P6: chỉ đăng sau khi nộp IBR (tránh xung đột chính sách preprint của tạp chí).
- **KHÔNG** tải file PDF toàn văn của các nghiên cứu gốc (vi phạm bản quyền) — chỉ metadata/effect-size.

## Checklist trước khi public
- [ ] Mọi số trong `5_Results/` khớp với bản thảo baseline (k=238/K=288, r̄=0.074, I²=62.4%).
- [ ] `00_START_HERE.md` nêu rõ trạng thái "baseline; mở rộng đang tiến hành".
- [ ] Tên tác giả + email đúng (bản ghi mở, không ẩn danh).
- [ ] License đã đặt.
- [ ] Không có PDF toàn văn / dữ liệu bản quyền trong gói.
