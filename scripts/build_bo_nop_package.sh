#!/usr/bin/env bash
# build_bo_nop_package.sh — Dựng lại TOÀN BỘ bộ nộp hoàn chỉnh từ nguồn Markdown
# đã hiệu chỉnh (khung canonical 50 nền / 84.998 LP-valid / 107 cặp nền-năm).
#
# Sinh ra MỘT thư mục nộp duy nhất: dist/BO_NOP_HOAN_CHINH_2026-06/
#   1_papers/                 (giữ nguyên — bundle P3..P10 không đổi ở lượt này)
#   2_chuyen_de/              CD1_CTU.{pdf,docx}, CD2_CTU.{pdf,docx}
#   3_luan_an_chuong_phu_luc/ LUAN_AN_CTU_full.pdf + chương 1..5 (.pdf/.docx)
#                             + front/refs/phụ lục (.docx)
#
# Toàn bộ định dạng theo chuẩn CTU (QĐ 1799/SH): TeX Gyre Termes 13pt
# (metric tương đương Times New Roman), lề 3/2/2/2cm, giãn dòng 1,2.
# PDF biên dịch bằng XeLaTeX trong container; DOCX dùng template CTU.
#
# Dùng:  bash scripts/build_bo_nop_package.sh
set -euo pipefail
cd "$(dirname "$0")/.."

PKG="dist/BO_NOP_HOAN_CHINH_2026-06"
THESIS_TPL="templates/ctu_thesis_reference.docx"
HEADER="templates/ctu_xelatex_header.tex"
LATEX_OUT="latex/ctu"
MAINFONT="${MAINFONT:-TeX Gyre Termes}"

mkdir -p "$PKG/2_chuyen_de" "$PKG/3_luan_an_chuong_phu_luc"

REF=(); [[ -f "$THESIS_TPL" ]] && REF=(--reference-doc="$THESIS_TPL")
RP="--resource-path=thesis:chuyen_de/cd1:chuyen_de/cd2:latex/ctu:."

# Biến CTU dùng chung cho mọi .tex biên dịch riêng lẻ (đồng bộ build_latex_ctu.sh)
CTU_VARS=(
  -V documentclass=extreport -V classoption=13pt -V mainfont="$MAINFONT"
  -V papersize=a4
  -V geometry:left=3cm -V geometry:right=2cm -V geometry:top=2cm -V geometry:bottom=2cm
  -V geometry:headsep=1cm -V geometry:footskip=1cm
  -V linestretch=1.2 -V lang=vi
  -V colorlinks=true -V linkcolor=black -V urlcolor=blue -V citecolor=black -V indent=true
)
COMMON_TEX=(--standalone --pdf-engine=xelatex
  --resource-path=thesis:chuyen_de/cd1:chuyen_de/cd2:. -H "$HEADER")

xe() { # compile <texbasename> inside $LATEX_OUT, 2 passes, quiet
  ( cd "$LATEX_OUT" && \
    xelatex -interaction=nonstopmode -halt-on-error "$1.tex" >/dev/null 2>&1 || true && \
    xelatex -interaction=nonstopmode -halt-on-error "$1.tex" >/dev/null 2>&1 || true )
}

echo "==================================================================="
echo " [1/4] Sinh .tex (full LA + CĐ1 + CĐ2) và biên dịch PDF"
echo "==================================================================="
MAINFONT="$MAINFONT" bash scripts/build_latex_ctu.sh >/dev/null
for t in LUAN_AN_CTU CD1_CTU CD2_CTU; do
  echo "  [pdf] $t"; xe "$t"
done
LA_PAGES=$(pdfinfo "$LATEX_OUT/LUAN_AN_CTU.pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
cp "$LATEX_OUT/LUAN_AN_CTU.pdf" "$PKG/3_luan_an_chuong_phu_luc/LUAN_AN_CTU_full.pdf"
cp "$LATEX_OUT/CD1_CTU.pdf"     "$PKG/2_chuyen_de/CD1_CTU.pdf"
cp "$LATEX_OUT/CD2_CTU.pdf"     "$PKG/2_chuyen_de/CD2_CTU.pdf"
echo "  Luận án đầy đủ: ${LA_PAGES:-?} trang"

echo "==================================================================="
echo " [2/4] Chương 1..5 — PDF (xelatex) + DOCX (pandoc)"
echo "==================================================================="
CHAPTERS=(
  chuong_1_gioi_thieu_vi
  chuong_2_tong_quan_tai_lieu_vi
  chuong_3_phuong_phap_vi
  chuong_4_ket_qua_vi
  chuong_5_ket_luan_de_xuat_vi
)
for ch in "${CHAPTERS[@]}"; do
  src="thesis/$ch.md"
  # PDF: .tex riêng (# -> \chapter), biên dịch trong latex/ctu để figures/ phân giải
  pandoc "${COMMON_TEX[@]}" "${CTU_VARS[@]}" --top-level-division=chapter \
    -f markdown-yaml_metadata_block+autolink_bare_uris -t latex "$src" -o "$LATEX_OUT/$ch.tex"
  echo "  [pdf] $ch"; xe "$ch"
  [[ -f "$LATEX_OUT/$ch.pdf" ]] && cp "$LATEX_OUT/$ch.pdf" "$PKG/3_luan_an_chuong_phu_luc/$ch.pdf"
  # DOCX
  echo "  [docx] $ch"
  pandoc -f markdown-yaml_metadata_block "${REF[@]}" $RP "$src" \
    -o "$PKG/3_luan_an_chuong_phu_luc/$ch.docx"
done

echo "==================================================================="
echo " [3/4] Front-matter / References / Phụ lục — DOCX"
echo "==================================================================="
DOCX_ONLY=(
  00_phan_dau_vi
  04_references_apa7
  phu_luc_A_hop_nhat_du_lieu_vi
  phu_luc_B_maida_vi
)
for f in "${DOCX_ONLY[@]}"; do
  src="thesis/$f.md"
  [[ -f "$src" ]] || { echo "  WARN missing $src"; continue; }
  echo "  [docx] $f"
  pandoc -f markdown-yaml_metadata_block "${REF[@]}" $RP "$src" \
    -o "$PKG/3_luan_an_chuong_phu_luc/$f.docx"
done

echo "==================================================================="
echo " [4/4] Chuyên đề 1 & 2 — DOCX"
echo "==================================================================="
pandoc -f markdown-yaml_metadata_block "${REF[@]}" $RP --toc --toc-depth=3 \
  chuyen_de/cd1/00_cd1_ctu_final_vi.md -o "$PKG/2_chuyen_de/CD1_CTU.docx"
echo "  [docx] CD1_CTU"
pandoc -f markdown-yaml_metadata_block "${REF[@]}" $RP --toc --toc-depth=3 \
  chuyen_de/cd2/00_cd2_ctu_final_vi.md -o "$PKG/2_chuyen_de/CD2_CTU.docx"
echo "  [docx] CD2_CTU"

# Dọn file phụ trợ LaTeX
( cd "$LATEX_OUT" && rm -f ./*.aux ./*.log ./*.out ./*.toc ./*.lof ./*.lot \
    ./*.synctex.gz compile_*.log 2>/dev/null || true )

echo ""
echo "=== Hoàn tất. Bộ nộp tại: $PKG ==="
find "$PKG" -type f \( -name '*.pdf' -o -name '*.docx' \) | sort
