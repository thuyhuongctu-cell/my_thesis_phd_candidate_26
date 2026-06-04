#!/usr/bin/env bash
# Build all CTU thesis chapters + summary + chuyên đề with STRICT CTU format.
# Source MD files in thesis/ use _vi.md suffix; output preserves _vi.docx
# but dist/SUBMISSION_FINAL/Thesis_LuanAn/ uses cleaner names (no _vi).
#
# Template: templates/ctu_thesis_strict.docx (1.5 line spacing, 1cm first-line
#           indent, 16pt centered chapter headings, 14pt section headings)
#
# Usage from repo root:
#   bash scripts/build_ctu_thesis_strict.sh

set -e
cd "$(dirname "$0")/.."

TEMPLATE="templates/ctu_thesis_strict.docx"
OUT_DIR="dist/SUBMISSION_FINAL/Thesis_LuanAn"

if [ ! -f "$TEMPLATE" ]; then
  echo "ERROR: $TEMPLATE not found"
  exit 1
fi

mkdir -p "$OUT_DIR"

# Function: build_one <source_md_relative_to_thesis> <dist_basename>
#   - writes thesis/<src_stem>.docx (same stem as MD)
#   - copies to dist as <dist_basename>.docx (cleaner name)
build_one() {
  local src_md="$1"        # e.g. chuong_1_gioi_thieu_vi.md
  local dist_name="$2"     # e.g. chuong_1_gioi_thieu
  local src_path="thesis/${src_md}"

  if [ ! -f "$src_path" ]; then
    echo "  SKIP: $src_path not found"
    return
  fi

  local src_stem="${src_md%.md}"
  local out_thesis="thesis/${src_stem}.docx"
  local out_dist="$OUT_DIR/${dist_name}.docx"

  # Build inside thesis/ so figure paths resolve
  (cd thesis && pandoc "$src_md" -o "${src_stem}.docx" \
    --reference-doc="../$TEMPLATE" 2>&1) | grep -v "^$" | tail -2
  cp "$out_thesis" "$out_dist"

  local kb
  kb=$(stat -c%s "$out_thesis" | awk '{print int($1/1024)}')
  echo "  ✓ ${dist_name}.docx (${kb} KB)"
}

echo "=== Build all luận án chapters + tóm tắt + 3 CĐ1 parts + CĐ2 with STRICT CTU format ==="

# 5 chapters of luận án
build_one "chuong_1_gioi_thieu_vi.md"          "chuong_1_gioi_thieu"
build_one "chuong_2_tong_quan_tai_lieu_vi.md"   "chuong_2_tong_quan_tai_lieu"
build_one "chuong_3_phuong_phap_vi.md"          "chuong_3_phuong_phap"
build_one "chuong_4_ket_qua_vi.md"              "chuong_4_ket_qua"
build_one "chuong_5_ket_luan_de_xuat_vi.md"     "chuong_5_ket_luan_de_xuat"

# Summary
build_one "tom_tat_noi_dung_vi.md"              "tom_tat_noi_dung"

# CĐ1 (3 parts)
build_one "14_cd1_part1_intro_theory_vi.md"     "cd1_part1_intro_theory"
build_one "15_cd1_part2_findings_vi.md"         "cd1_part2_findings"
build_one "16_cd1_part3_cases_conclusion_vi.md" "cd1_part3_cases_conclusion"

# CĐ2 (theoretical framework)
build_one "02_theoretical_framework_vi.md"      "cd2_theoretical_framework"

echo ""
echo "=== Build summary ==="
ls -la "$OUT_DIR"/*.docx 2>/dev/null | awk '{printf "  %-65s %5d KB\n", $NF, $5/1024}'
echo ""
echo "Done. All DOCX use templates/ctu_thesis_strict.docx (1.5 line spacing)."
