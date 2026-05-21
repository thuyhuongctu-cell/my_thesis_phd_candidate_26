# Final Submission Packages — 2026-05-21

7 ZIP packages chia thành **2 loại tài liệu khác nhau**.

## Loại 1 — Journal papers (5 bản thảo)

| Package | Target journal | Indexing | Status |
|---|---|---|---|
| `P3_Vietnam_APJM_20260521.zip` | Asia Pacific Journal of Management (APJM) | Springer · Scopus Q1 · ABS 3 | ✅ Ready |
| `P4_Singapore_MIR_20260521.zip` | Management International Review (MIR) | Springer · Scopus Q1 · ABS 3 | ✅ Ready |
| `P5_China_IJOEM_20260521.zip` | International Journal of Emerging Markets (IJOEM) | Emerald · Scopus Q2 · ABS 2 | ✅ Ready |
| `P7_Capstone_JIBS_20260521.zip` | Journal of International Business Studies (JIBS) | Palgrave · Scopus Q1 · ABS 4* | ✅ Ready |
| `P8_PacificSIDS_WorldDev_20260521.zip` | World Development | Elsevier · Scopus Q1 · ABS 3 | ✅ Ready |

Mỗi package chứa: EN/VN DOCX + PDF + TEX + COVER_LETTER_TEMPLATE.md + SUBMISSION_README.md.

**Format**: Springer/Emerald/Elsevier journal style (TNR 12pt, 1.15 line spacing, lề 2.5 cm).

## Loại 2 — Chuyên đề tiến sĩ (2 chuyên đề)

| Package | Status | Nội dung |
|---|---|---|
| `CD1_ChuyenDe1_20260521.zip` | ✅ Ready | Thực trạng hiệu quả hoạt động kinh doanh ở châu Á (mô tả-chẩn đoán) |
| `CD2_ChuyenDe2_20260521.zip` | ⚠ Ready w/ PENDING | Mô hình lý thuyết và thực nghiệm (§2.4.3 P6 numbers chờ pipeline) |

**Format**: CTU thesis template (TNR 13pt, 1.5 line spacing, lề 3-2-2-2 cm).

## Coverage map

| Paper | Sample | Country focus | ICRV group(s) | Hypothesis tested |
|---|---|---|---|---|
| P3 | n=2,958 firms, 3 waves | Vietnam | IV Emerging | H1 inverted-U + H3 DAI moderation |
| P4 | n~1,800 firms, 1 wave 2023 | Singapore | I Advanced innovation | H4 DAI×FSTS² (digital scaling) |
| P5 | n=4,559 firms, 2 waves | China | III Upper-middle | H2 threshold stability (Paternoster z-tests) |
| **P7** | **n=91,982 firms, 49 economies, 102 country-year waves** | **All Asia + Pacific pool** | **All 6 groups** | **H1-H6 (capstone)** |
| **P8** | **n=1,469 firms, 9 SIDS economies** | **Pacific SIDS** | **VI Boundary case** | **H1 inverted -U COLLAPSES; FIP** |
| CD1 | n=101,185 firms, 47 economies | Pool descriptive | All 6 (incl SIDS extension) | descriptive-diagnostic |
| CD2 | n=101,185 firms, 47 economies | Pool theoretical+empirical | All 6 + H1-H6 | M0-M7 model spec |

P7 = capstone JIBS paper unifying all H1-H6 across the pool. P8 = boundary-case paper establishing FIP for SIDS.

## What to do next

1. Mở 7 ZIP, confirm DOCX/PDF render correctly trong Word/Acrobat.
2. **Journal papers**: điền `COVER_LETTER_TEMPLATE.md` với tên + tổ chức + 3 reviewer gợi ý cho mỗi paper.
3. **Chuyên đề**: nộp DOCX cho Hội đồng đánh giá CTU.
4. **CD2 P6 update**: rebuild khi pipeline P6 chạy xong.

## Build provenance

- Source markdown:
  - Journal: `manuscripts/p[3-5,7,8]_*_{en,vi}_clean.md`
  - Chuyên đề: `thesis/14-16_cd1_*.md` + `thesis/17_cd2_full_vi.md`
- Build script: `scripts/build_submission_package.sh` (pandoc + xelatex 3-pass)
- Templates:
  - `templates/ctu_paper_reference.docx` (journal — TNR 12pt 1.15-line)
  - `templates/ctu_thesis_reference.docx` (chuyên đề — TNR 13pt 1.5-line, lề 3-2-2-2 cm)
  - `templates/springer_paper.tex` (LaTeX article class, Liberation Serif full Vietnamese)
- All 14 build artifacts (7 EN + 7 VN where applicable): ! errors = 0, missing chars = 0
