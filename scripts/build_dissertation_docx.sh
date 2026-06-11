#!/usr/bin/env bash
# build_dissertation_docx.sh
#
# Assemble the complete dissertation into a single CTU-formatted .docx:
#   front matter -> Ch1..Ch5 -> References (APA7) -> Appendix A
# Uses templates/ctu_paper_reference.docx for CTU styling (TNR 12pt, 2.5cm
# margins, 1.15 line spacing). Output: dist/luan_an_ctu/LUAN_AN_FULL_vi.docx
#
# Usage: bash scripts/build_dissertation_docx.sh
set -euo pipefail
cd "$(dirname "$0")/.."

TPL="templates/ctu_paper_reference.docx"
OUT="dist/luan_an_ctu/LUAN_AN_FULL_vi.docx"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Ordered source list (page break between major parts)
PARTS=(
  "thesis/00_phan_dau_vi.md"
  "thesis/chuong_1_gioi_thieu_vi.md"
  "thesis/chuong_2_tong_quan_tai_lieu_vi.md"
  "thesis/chuong_3_phuong_phap_vi.md"
  "thesis/chuong_4_ket_qua_vi.md"
  "thesis/chuong_5_ket_luan_de_xuat_vi.md"
  "thesis/04_references_apa7.md"
  "thesis/phu_luc_A_hop_nhat_du_lieu_vi.md"
)

MERGED="$TMP/merged.md"
: > "$MERGED"
for p in "${PARTS[@]}"; do
  if [[ ! -f "$p" ]]; then echo "WARN: missing $p, skipping" >&2; continue; fi
  cat "$p" >> "$MERGED"
  printf '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n' >> "$MERGED"
done

REF=()
[[ -f "$TPL" ]] && REF=(--reference-doc="$TPL")

pandoc -f markdown-yaml_metadata_block "${REF[@]}" \
  --toc --toc-depth=2 --resource-path=thesis:. \
  "$MERGED" -o "$OUT"

echo "Built $OUT ($(stat -c%s "$OUT" 2>/dev/null || stat -f%z "$OUT") bytes)"
