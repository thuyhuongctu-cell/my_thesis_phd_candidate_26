# Final Submission Packages — 2026-05-21

5 ZIP packages chia thành **2 loại tài liệu khác nhau** với mục đích, định dạng và quy trình nộp riêng biệt.

## Loại 1 — Journal papers (3 bản thảo)

Bản thảo nộp tạp chí quốc tế Scopus/WoS theo quy trình bình duyệt ẩn danh (blind review).

| Package | Target journal | Indexing | Status |
|---|---|---|---|
| `P3_Vietnam_APJM_20260521.zip` | Asia Pacific Journal of Management (APJM) | Springer · Scopus Q1 · ABS 3 | ✅ Ready |
| `P4_Singapore_MIR_20260521.zip` | Management International Review (MIR) | Springer · Scopus Q1 · ABS 3 | ✅ Ready |
| `P5_China_IJOEM_20260521.zip` | International Journal of Emerging Markets (IJOEM) | Emerald · Scopus Q2 · ABS 2 | ✅ Ready |

Mỗi package chứa:
- `*_manuscript_EN.docx` — Upload chính lên portal tạp chí
- `*_manuscript_EN.pdf` — Preview
- `*_manuscript_EN.tex` — LaTeX source (cho journal accept LaTeX)
- `*_manuscript_VN.docx` — Bản tiếng Việt (lưu trữ nội bộ + CTU dossier)
- `*_manuscript_VN.pdf` — Preview tiếng Việt
- `SUBMISSION_README.md` — Compliance checklist
- `COVER_LETTER_TEMPLATE.md` — Cover letter điền tên + tổ chức + reviewers

**Format**: Springer/Emerald journal style (TNR 12pt, 1.15 line spacing, lề 2.5 cm).

## Loại 2 — Chuyên đề tiến sĩ (2 chuyên đề)

Tài liệu trong khuôn khổ chương trình NCS tại Trường Đại học Cần Thơ (theo Quyết định 4769/QĐ-ĐHCT, 15/10/2024). Trình bày trước Hội đồng đánh giá — KHÔNG phải bản thảo nộp tạp chí.

| Package | Status | Nội dung |
|---|---|---|
| `CD1_ChuyenDe1_20260521.zip` | ✅ Ready | Thực trạng hiệu quả hoạt động kinh doanh ở châu Á (mô tả-chẩn đoán) |
| `CD2_ChuyenDe2_20260521.zip` | ⚠ Ready w/ PENDING | Mô hình lý thuyết và thực nghiệm (§2.4.3 P6 numbers chờ pipeline) |

Mỗi package chứa:
- `CD{n}_ChuyenDe{n}_VN.docx` — Nộp lên Hội đồng
- `CD{n}_ChuyenDe{n}_VN.pdf` — Preview
- `CD{n}_ChuyenDe{n}_VN.tex` — LaTeX source
- `SUBMISSION_README.md` — Overview + PENDING notes nếu có

**Format**: CTU thesis template (TNR 13pt, 1.5 line spacing, lề 3-2-2-2 cm).

## Phân biệt 2 loại

| Tiêu chí | Journal papers (P3/P4/P5) | Chuyên đề tiến sĩ (CD1/CD2) |
|---|---|---|
| **Người nhận** | Editorial board tạp chí quốc tế | Hội đồng đánh giá CTU |
| **Quy trình** | Blind peer review | Bảo vệ trước Hội đồng |
| **Ngôn ngữ chính** | Tiếng Anh | Tiếng Việt (có ABSTRACT EN song ngữ) |
| **Định dạng** | Journal style (Springer/Emerald) | CTU thesis style |
| **Cấu trúc** | Abstract, Introduction, Theory, Data, Results, Discussion, References | TÓM TẮT/ABSTRACT, 7 chương (CD1) hoặc 4 phần §2.1-2.4 (CD2) |
| **Độ dài** | 8-12k từ (body) | 15-25k từ |
| **Mục đích** | Công bố Scopus/WoS | Coursework PhD program |

## What to do next

1. **Mở 5 ZIP**, confirm DOCX/PDF render correctly trong Word/Acrobat.
2. **Journal papers (P3/P4/P5)**:
   - Điền `COVER_LETTER_TEMPLATE.md` với tên + tổ chức + 3 reviewer gợi ý
   - Upload manuscript DOCX lên portal tương ứng
3. **Chuyên đề (CD1/CD2)**:
   - Nộp DOCX cho Hội đồng đánh giá CTU
   - PDF accompanies như reference copy
4. **CD2 P6 update**: Khi pipeline P6 meta-analysis chạy xong, rebuild + re-zip CD2 với final numbers (k=238, r=0.074, Q_M=17.35, τ=−0.134 sẽ replace placeholder).

## Build provenance

- Source markdown:
  - Journal: `manuscripts/p[3-5]_*_{en,vi}_clean.md`
  - Chuyên đề: `thesis/14-16_cd1_*.md` + `thesis/17_cd2_full_vi.md`
- Build script: `scripts/build_submission_package.sh` (pandoc + xelatex 3-pass)
- Templates:
  - `templates/ctu_paper_reference.docx` (journal — TNR 12pt 1.15-line)
  - `templates/ctu_thesis_reference.docx` (chuyên đề — TNR 13pt 1.5-line, lề 3-2-2-2 cm)
  - `templates/springer_paper.tex` (LaTeX article class, Liberation Serif full Vietnamese)
- Build verification: 8/8 artifacts, 0 LaTeX errors, 0 missing-character warnings
