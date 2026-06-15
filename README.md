# Luận án Tiến sĩ — Quốc tế hóa và Hiệu quả Doanh nghiệp tại châu Á

> **Đề tài:** Mối quan hệ giữa quốc tế hóa và hiệu quả hoạt động doanh nghiệp (*internationalization–firm performance*, I–P) tại châu Á — các điều kiện biên thể chế, năng lực số và đặc điểm nhà quản trị.

Kho lưu trữ này chứa toàn bộ bản thảo luận án, các nghiên cứu thành phần (papers), chuyên đề, dữ liệu WBES, mã tái lập (replication) và quy trình biên dịch ra DOCX/PDF theo định dạng CTU.

---

## 🎯 Khung lý thuyết & phát hiện chính

Luận án xây dựng khung điều tiết đa tầng **CDCM (Country–Digital–Capability Moderation)** tích hợp mô hình Uppsala, lý thuyết dựa trên nguồn lực (RBV), lý thuyết thể chế và lý thuyết thượng tầng quản trị, với ba tầng điều tiết:

1. **Bối cảnh thể chế** — vận hành hóa bằng taxonomy **ICRV** sáu nhóm.
2. **Năng lực số** — tách **TCI** (năng lực công nghệ) và **DAI** (chỉ số chấp nhận số).
3. **Đặc điểm nhà quản trị cấp cao**.

**Phát hiện chính:**
- Quan hệ I–P có dạng **phi tuyến chữ U ngược**, điểm uốn gộp **43,6%** (mô hình đầy đủ, **50 nền kinh tế châu Á–Thái Bình Dương, gồm Nhật Bản 2025**).
- TCI và DAI **nâng mặt bằng hiệu quả phổ quát**, nhưng vai trò *uốn đường cong* chỉ rõ ở bối cảnh đơn quốc gia đặc thù (vd "lá chắn số" DAI tại Singapore).
- Tại nhóm SIDS, quan hệ chuyển thành **âm đơn điệu** — construct mới: **Gánh nặng quốc tế hóa bắt buộc (Forced Internationalization Penalty, FIP)**.

---

## 🗂️ Cấu trúc kho lưu trữ

```
MY_THESIS_PHD_CANDIDATE_26/
├── thesis/                # Bản thảo luận án (Chương 1–5, phụ lục, tiếng Việt + thesis/en)
├── manuscripts/           # Bản thảo các bài báo thành phần (EN + VI)
├── chuyen_de/             # Chuyên đề CĐ1 (mô tả) + CĐ2 (ước lượng)
├── p1 … p11_jed/          # Hồ sơ từng nghiên cứu thành phần
│   └── p7/                #   Nghiên cứu đa quốc gia (capstone) + replication/ + submission/
├── data_wbes/             # Dữ liệu World Bank Enterprise Surveys
│   ├── raw_dta/           #   139 tệp .dta thô (đã version-control trên nhánh)
│   └── p7/                #   Tệp phân tích đã hợp nhất (p7_pooled_clean.csv) + manifest
├── meta_analysis_2025/    # Dữ liệu & mã meta-analysis (P6, PRISMA)
├── latex/                 # Nguồn LaTeX (CTU) cho luận án và papers
├── dist/                  # Sản phẩm biên dịch (DOCX luận án, gói OSF P3–P11)
├── reviews/               # Báo cáo rà soát phương pháp & biến số
├── scripts/               # Script biên dịch & tiện ích
├── templates/             # Mẫu DOCX/định dạng CTU
└── references/            # Thư mục tài liệu tham khảo (APA7)
```

## 🧪 Các nghiên cứu thành phần

| Mã | Bối cảnh | Trọng tâm |
|----|----------|-----------|
| **P3** | Việt Nam | Chữ U ngược I–P, ba sóng WBES |
| **P4** | Singapore | Quan hệ gần tuyến tính; "lá chắn số" DAI |
| **P5** | Trung Quốc | Độ bền cấu trúc điểm uốn qua hai sóng |
| **P6** | Meta-analysis | Tổng hợp văn liệu I–P (PRISMA) |
| **P7** | Đa quốc gia (capstone) | 50 nền Asia-Pacific (gồm Japan), U-ngược + điều tiết |
| **P8** | Pacific SIDS | Construct FIP (gánh nặng quốc tế hóa bắt buộc) |
| **P9** | Ấn Độ | Mô hình ngưỡng |
| **P10** | Nhật Bản | Kiểm định chuyên sâu I–P biên trên |
| **P11** | JED | Bài báo phái sinh |

---

## 🔁 Tái lập nghiên cứu P7 (đa quốc gia)

Pipeline đọc trực tiếp `.dta` thô WBES → tệp phân tích → ước lượng:

```bash
# 1) Hợp nhất .dta thô thành tệp phân tích (50 nền Asia-Pacific, gồm Japan-2025)
python3 p7/replication/01_build_p7_dataset.py \
        --raw-dir data_wbes/raw_dta --out-dir data_wbes/p7

# 2) Ước lượng chuỗi mô hình hồi quy (FE hai chiều, SE robust)
python3 p7/replication/02_run_p7_models.py \
        --data data_wbes/p7/p7_pooled_clean.csv \
        --out-dir p7/replication/results_incl_japan
```

**Biến chính (P7):**
- `tci_z` — Năng lực công nghệ (TCI) = z-chuẩn hóa của hai mục: **b8** (chứng chỉ chất lượng) + **e6** (công nghệ nước ngoài).
- `dai_z` — Chấp nhận số (DAI); `fsts` — cường độ quốc tế hóa; `ln_labor_prod` — năng suất lao động.

> **Yêu cầu:** Python 3.11+, `pandas`, `pyreadstat`, `statsmodels`, `scipy`.

---

## 📄 Biên dịch tài liệu

```bash
bash scripts/build_dissertation_docx.sh   # → dist/luan_an_ctu/LUAN_AN_FULL_vi.docx
bash scripts/build_latex_ctu.sh           # → latex/ctu/LUAN_AN_CTU.tex (PDF qua xelatex)
bash scripts/build_latex_papers.sh        # Biên dịch LaTeX các bài báo
```

> **Yêu cầu:** `pandoc`; (tùy chọn) TeX Live + `xelatex`/`biber` cho PDF.

---

## 📊 Dữ liệu

- **Nguồn:** World Bank Enterprise Surveys (WBES), khung 50 nền kinh tế châu Á–Thái Bình Dương, 2006–2025, **gồm Nhật Bản (khảo sát lần đầu 2025)**.
- **Hài hòa hóa:** ba thế hệ schema (PICS3, Standardized, BREADY/BEE) được hợp nhất theo quy trình tại `thesis/phu_luc_A_hop_nhat_du_lieu_vi.md`.
- **Phạm vi phân tích:** loại các điều tra phi chính thức/siêu nhỏ/ISES và nền ngoài Asia-Pacific (Comoros) khỏi khung ước lượng.

---

## 🛠️ Nhánh `claude/phd-thesis-review-L9Gml` — đã thực hiện

Nhánh này rà soát phương pháp & biến số và làm tươi pipeline P7:

- **Xác minh TCI = b8 + e6** (2 mục) trên `.dta` thật; sửa lỗi mã biến P5 (`b4,b7a → h1,h8`); hợp nhất định nghĩa thin/full ở §3.3.4.
- **Sửa 2 lỗi tooling tái lập P7:** parser tên file không đọc được tên nước gạch nối (rớt 11 nền); biến kiểm soát `foreign_own_pct` (41% phủ) cắt đôi mẫu mô hình.
- **Thêm Japan-2025 + chạy lại bằng `.dta` thật:** khung 50 nền Asia-Pacific; kết luận U-ngược + TCI dương giữ vững (M5 điểm uốn 33,4%, p<0,001; TCI +0,19, p<0,001).
- Chi tiết: `reviews/METHODOLOGY_VARIABLE_REVIEW_2026-06-15.md`.

---

## 📌 Ghi chú

- Số liệu báo cáo trong text luận án là số đã khóa từ bộ dữ liệu canonical của tác giả; mã trong `p7/replication/` dùng để kiểm chứng độ vững và minh bạch quy trình.
- Không commit: tệp bí mật/khóa API, `.claude/settings.local.json`.
