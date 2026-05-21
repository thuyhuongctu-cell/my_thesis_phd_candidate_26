# Final Submission Packages — 2026-05-21

5 ready-to-submit packages. Open each ZIP, follow the per-package SUBMISSION_README.md.

## Journal manuscripts (3 papers × 2 language versions)

| Package | Target journal | Status |
|---|---|---|
| `P3_Vietnam_APJM_20260521.zip` | Asia Pacific Journal of Management (APJM, Springer Q1) | ✅ Ready |
| `P4_Singapore_MIR_20260521.zip` | Management International Review (MIR, Springer Q1) | ✅ Ready |
| `P5_China_IJOEM_20260521.zip` | International Journal of Emerging Markets (IJOEM, Emerald) | ✅ Ready |

Each contains: EN + VN DOCX/PDF/TEX + cover-letter template + submission README.

## CTU thesis dossier (2 chuyên đề)

| Package | Status | Note |
|---|---|---|
| `CD1_ChuyenDe1_20260521.zip` | ✅ Ready | Bảng 4.1 + 4.5.6 đã computed từ P7 |
| `CD2_ChuyenDe2_20260521.zip` | ⚠ Ready with PENDING note | §2.4.3 P6 numbers wait on pipeline |

## What to do next

1. Test-open each ZIP and confirm DOCX/PDF render correctly in Word/Acrobat.
2. For journal submissions: fill in `COVER_LETTER_TEMPLATE.md` with your name + institution + suggested reviewers.
3. For CTU submission: submit CD1 + CD2 DOCX (the .pdf can accompany as reference copy).
4. CD2 will be updated with final P6 numbers when the meta-analysis pipeline finishes.

## Build provenance

- Source markdown: `manuscripts/p[3-5]_*_{en,vi}_clean.md` + `thesis/14-16_cd1_*.md` + `thesis/17_cd2_full_vi.md`
- Build script: `scripts/build_submission_package.sh` (pandoc + xelatex 3-pass)
- Templates: `templates/ctu_paper_reference.docx` (journal), `templates/ctu_thesis_reference.docx` (CTU), `templates/springer_paper.tex`
- All 8 build artifacts: zero LaTeX errors, zero missing-character warnings
