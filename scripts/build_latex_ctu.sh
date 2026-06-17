#!/usr/bin/env bash
# build_latex_ctu.sh — Sinh nguồn LaTeX định dạng CTU (QĐ 1799/SH) từ Markdown.
#
# Chuẩn CTU (QĐ 1799/SH): Times New Roman 13pt, giãn dòng 1,2, lề trái 3,0cm / trên-dưới-phải 2,0cm.
# Yêu cầu biên dịch (trên máy NCS, KHÔNG chạy được trong container này):
#     xelatex <file>.tex   (chạy 2 lần để cập nhật mục lục)
# xelatex là bắt buộc: tiếng Việt Unicode + font Times New Roman.
# Nếu máy không cài Times New Roman, đổi MAINFONT="TeX Gyre Termes" (metric tương đương).
#
# Cách dùng: bash scripts/build_latex_ctu.sh
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="latex/ctu"
mkdir -p "$OUT"
MAINFONT="${MAINFONT:-Times New Roman}"

# Biến định dạng CTU dùng chung cho mọi tài liệu
CTU_VARS=(
  -V documentclass=extreport
  -V classoption=13pt
  -V mainfont="$MAINFONT"
  -V papersize=a4
  -V geometry:left=3cm -V geometry:right=2cm -V geometry:top=2cm -V geometry:bottom=2cm
  -V geometry:headsep=1cm -V geometry:footskip=1cm
  -V linestretch=1.2
  -V lang=vi
  -V colorlinks=true -V linkcolor=black -V urlcolor=blue -V citecolor=black
  -V indent=true
)
COMMON=(
  --standalone
  --pdf-engine=xelatex
  --resource-path=thesis:chuyen_de/cd1:chuyen_de/cd2:.
  -H templates/ctu_xelatex_header.tex
)

pagebreak() { printf '\n\n\\newpage\n\n'; }

# ---------- 1. Luận án đầy đủ (extreport, # -> \chapter) ----------
echo "==> Luận án (LUAN_AN_CTU.tex)"
TMP="$(mktemp)"
PARTS=(
  thesis/00_phan_dau_vi.md
  thesis/chuong_1_gioi_thieu_vi.md
  thesis/chuong_2_tong_quan_tai_lieu_vi.md
  thesis/chuong_3_phuong_phap_vi.md
  thesis/chuong_4_ket_qua_vi.md
  thesis/chuong_5_ket_luan_de_xuat_vi.md
  thesis/04_references_apa7.md
  thesis/phu_luc_A_hop_nhat_du_lieu_vi.md
)
: > "$TMP"
for p in "${PARTS[@]}"; do cat "$p" >> "$TMP"; pagebreak >> "$TMP"; done
pandoc "${COMMON[@]}" "${CTU_VARS[@]}" \
  --top-level-division=chapter \
  -f markdown-yaml_metadata_block+autolink_bare_uris -t latex "$TMP" -o "$OUT/LUAN_AN_CTU.tex"
rm -f "$TMP"

# ---------- 2 & 3. Chuyên đề 1 / 2 (extreport, ## -> section; không chapter) ----------
for cd in cd1 cd2; do
  src="chuyen_de/$cd/00_${cd}_ctu_final_vi.md"
  echo "==> Chuyên đề ${cd^^} (${cd^^}_CTU.tex)"
  pandoc "${COMMON[@]}" "${CTU_VARS[@]}" \
    --top-level-division=section \
    -f markdown-yaml_metadata_block+autolink_bare_uris -t latex "$src" -o "$OUT/${cd^^}_CTU.tex"
done

# ---------- 4. Gom hình để biên dịch turnkey ----------
mkdir -p "$OUT/figures"
cp -f thesis/figures/*.png "$OUT/figures/" 2>/dev/null || true       # luận án: fig_*
cp -f chuyen_de/cd1/figures/*.png "$OUT/figures/" 2>/dev/null || true # CĐ1: cd1_fig_*, hinh_*
cp -f chuyen_de/cd2/figures/*.png "$OUT/figures/" 2>/dev/null || true # CĐ2: hinh_*

echo
echo "Đã sinh: $OUT/{LUAN_AN_CTU,CD1_CTU,CD2_CTU}.tex (+ figures/)"
echo "Biên dịch (máy có TeX + xelatex), trong thư mục $OUT:"
echo "    xelatex LUAN_AN_CTU.tex && xelatex LUAN_AN_CTU.tex   # chạy 2 lần cho mục lục"
