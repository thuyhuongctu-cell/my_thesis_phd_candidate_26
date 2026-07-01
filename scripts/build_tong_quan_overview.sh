#!/usr/bin/env bash
# build_tong_quan_overview.sh — dựng gói "Tổng quan luận án" ra DOCX + PDF (CTU).
#
# Gộp 4 tài liệu trong tong_quan_luan_an/ (xem preprocess_tong_quan.py: gỡ sơ đồ
# Mermaid chỉ-dành-cho-GitHub, nhúng 2 ảnh tĩnh PNG làm hình có chú thích), rồi:
#   - DOCX: dùng templates/ctu_thesis_reference.docx (style CTU).
#   - PDF : xelatex + templates/ctu_xelatex_header.tex, lề/giãn dòng chuẩn CTU.
#
# Font: container không có Times New Roman -> TeX Gyre Termes (metric tương đương).
# Trên máy NCS có TNR thật, đặt MAINFONT="Times New Roman".
#
# Output: dist/tong_quan_luan_an/{TONG_QUAN_LUAN_AN.docx,.pdf}  (dist/ bị gitignore)
# Cách dùng: bash scripts/build_tong_quan_overview.sh
set -euo pipefail
cd "$(dirname "$0")/.."

OUT_DIR="dist/tong_quan_luan_an"
mkdir -p "$OUT_DIR"
DOCX="$OUT_DIR/TONG_QUAN_LUAN_AN.docx"
PDF="$OUT_DIR/TONG_QUAN_LUAN_AN.pdf"
MAINFONT="${MAINFONT:-TeX Gyre Termes}"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
MERGED="$TMP/merged.md"

python3 scripts/preprocess_tong_quan.py > "$MERGED"

# Ảnh tham chiếu theo đường dẫn từ gốc repo -> resource-path là gốc repo.
RESPATH="."

# ---------- DOCX ----------
DOCX_REF=()
[[ -f templates/ctu_thesis_reference.docx ]] && DOCX_REF=(--reference-doc=templates/ctu_thesis_reference.docx)
pandoc -f markdown-yaml_metadata_block+autolink_bare_uris "${DOCX_REF[@]}" \
  --toc --toc-depth=2 --resource-path="$RESPATH" \
  "$MERGED" -o "$DOCX"
echo "DOCX: $DOCX ($(stat -c%s "$DOCX") bytes)"

# ---------- PDF (xelatex, định dạng CTU) ----------
# labelformat=empty: dùng nhãn hình thủ công ("Hình 2.1.") khớp số mục, tránh
# pandoc tự thêm "Hình 1:" gây nhãn kép. Đồng bộ với bản DOCX.
pandoc -f markdown-yaml_metadata_block+autolink_bare_uris \
  --standalone --pdf-engine=xelatex \
  -H templates/ctu_xelatex_header.tex \
  -V header-includes='\usepackage{caption}\captionsetup{labelformat=empty}\usepackage{float}\floatplacement{figure}{H}' \
  --toc --toc-depth=2 --resource-path="$RESPATH" \
  -V documentclass=extarticle -V classoption=13pt \
  -V mainfont="$MAINFONT" -V papersize=a4 \
  -V geometry:left=3cm -V geometry:right=2cm -V geometry:top=2cm -V geometry:bottom=2cm \
  -V linestretch=1.2 -V lang=vi \
  -V colorlinks=true -V linkcolor=black -V urlcolor=blue -V citecolor=black \
  "$MERGED" -o "$PDF"
echo "PDF:  $PDF ($(stat -c%s "$PDF") bytes)"
