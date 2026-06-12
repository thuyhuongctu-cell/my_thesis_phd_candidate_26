#!/usr/bin/env bash
# build_latex_papers.sh — Sinh LaTeX journal cho P7/P8/P9 từ bản thảo markdown chuẩn.
#
# P3–P6 đã có LaTeX hand-crafted chất lượng cao (latex/p3..p6/*.tex, dùng
# latex/shared/macros.tex, biên dịch pdflatex). Script này CHỈ sinh P7/P8/P9
# (vốn chưa có .tex) từ gói submission tạp chí mục tiêu hàng đầu.
#
# Toán trong bản thảo P7/P8/P9 ở dạng ký tự Unicode (β, ≈, ₁, ²) → cần
# xelatex (xử lý Unicode trực tiếp). Tiêu đề blinded giữ nguyên cho review.
# Biên dịch (máy có TeX): xelatex <file>.tex (x2 cho mục lục/tham chiếu).
set -euo pipefail
cd "$(dirname "$0")/.."

VARS=(
  --standalone --pdf-engine=xelatex
  -V documentclass=article -V classoption=12pt
  -V geometry:margin=2.5cm
  -V linestretch=2.0            # double-spacing chuẩn bản nộp tạp chí
  -V mainfont="${MAINFONT:-Times New Roman}"
  -V colorlinks=true -V linkcolor=black -V citecolor=black -V urlcolor=blue
  -V lang=en
)

gen() {  # gen <src.md> <out.tex>
  local src="$1" out="$2"
  mkdir -p "$(dirname "$out")"
  pandoc "${VARS[@]}" --shift-heading-level-by=-1 -f markdown-yaml_metadata_block -t latex "$src" -o "$out"
  echo "  ok  $out"
}

echo "==> P7 (đa quốc gia, JIBS)"
gen p7/submission/jibs_package/01_manuscript_blinded.md       latex/p7/p7_jibs_submission.tex
echo "==> P8 (SIDS, World Development)"
gen p8/submission/world_development_package/01_manuscript_blinded.md  latex/p8/p8_worlddev_submission.tex
echo "==> P9 (Ấn Độ, IJOEM)"
gen p9_india/submission/ijoem_package/01_manuscript_blinded.md latex/p9/p9_ijoem_submission.tex

echo
echo "Đã sinh latex/p{7,8,9}/*.tex — biên dịch bằng: xelatex <file>.tex (x2)"
