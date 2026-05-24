#!/bin/bash
# Build CTU-formatted DOCX from dissertation Markdown sources.
# Output: dist/chuyen_de_1/, dist/luan_an/, dist/manuscripts/
#
# Prerequisites: pandoc >= 3.0, python3 python-docx
#   pip install python-docx
#
# Usage: bash build_ctu_docx.sh [--no-templates]

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATES="${SCRIPT_DIR}/templates"
DIST="${SCRIPT_DIR}/dist"
THESIS_REF="${TEMPLATES}/ctu_thesis_reference.docx"
PAPER_REF="${TEMPLATES}/ctu_paper_reference.docx"

# Build reference templates unless --no-templates passed
if [[ "$1" != "--no-templates" ]]; then
  echo "[0] Building CTU reference templates..."
  pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx
  python3 ~/.claude/skills/ctu-thesis-dossier-build/scripts/build_ctu_reference.py \
    /tmp/pandoc_default.docx "${TEMPLATES}"
fi

PANDOC_VI="pandoc -f gfm -t docx --resource-path=.:thesis --reference-doc=${THESIS_REF}"
PANDOC_EN="pandoc -f gfm -t docx --reference-doc=${PAPER_REF}"

mkdir -p "${DIST}"/{chuyen_de_1/source_md,luan_an/source_md,manuscripts/vi,manuscripts/en}

echo "[1] CĐ1 (14/15/16)..."
${PANDOC_VI} thesis/14_cd1_part1_intro_theory_vi.md   -o "${DIST}/chuyen_de_1/14_part1_intro_theory.docx"
${PANDOC_VI} thesis/15_cd1_part2_findings_vi.md        -o "${DIST}/chuyen_de_1/15_part2_findings.docx"
${PANDOC_VI} thesis/16_cd1_part3_cases_conclusion_vi.md -o "${DIST}/chuyen_de_1/16_part3_cases_conclusion.docx"
cp thesis/14_cd1_part1_intro_theory_vi.md thesis/15_cd1_part2_findings_vi.md \
   thesis/16_cd1_part3_cases_conclusion_vi.md "${DIST}/chuyen_de_1/source_md/"

echo "[2] Luận án thesis files (source/draft)..."
for f in 00_optimal_plan_vi 01_chapter_outline_vi 02_theoretical_framework_vi 03_methodology_vi 04_05_chapters_results_discussion_vi 04_references_apa7 11_dissertation_positioning_vi; do
  [ -f "thesis/${f}.md" ] && ${PANDOC_VI} "thesis/${f}.md" -o "${DIST}/luan_an/${f}.docx" && \
    cp "thesis/${f}.md" "${DIST}/luan_an/source_md/"
done

echo "[2b] Luận án 5 chương theo khung CTU..."
mkdir -p "${DIST}/luan_an_ctu/source_md"
for f in chuong_1_gioi_thieu_vi chuong_2_tong_quan_tai_lieu_vi chuong_3_phuong_phap_vi chuong_4_ket_qua_vi chuong_5_ket_luan_de_xuat_vi; do
  [ -f "thesis/${f}.md" ] && ${PANDOC_VI} "thesis/${f}.md" -o "${DIST}/luan_an_ctu/${f}.docx" && \
    cp "thesis/${f}.md" "${DIST}/luan_an_ctu/source_md/"
done

echo "[3] Vietnamese manuscripts..."
# P3: figures in p3/figures/vietnam/ — run from p3/ dir so relative paths resolve
[ -f "${SCRIPT_DIR}/p3/submission/p3_vietnam_vi.md" ] && (
  cd "${SCRIPT_DIR}/p3" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${THESIS_REF}" \
    submission/p3_vietnam_vi.md \
    -o "${DIST}/manuscripts/vi/p3_vietnam_vi.docx"
)
# P4: figures in p4/figures/ — run from p4/ dir so relative paths resolve
[ -f "${SCRIPT_DIR}/p4/submission/p4_singapore_vi.md" ] && (
  cd "${SCRIPT_DIR}/p4" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${THESIS_REF}" \
    submission/p4_singapore_vi.md \
    -o "${DIST}/manuscripts/vi/p4_singapore_vi.docx"
)
# P5: figures in p5/figures/ — run from p5/ dir
[ -f "${SCRIPT_DIR}/p5/submission/p5_china_vi.md" ] && (
  cd "${SCRIPT_DIR}/p5" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${THESIS_REF}" \
    submission/p5_china_vi.md \
    -o "${DIST}/manuscripts/vi/p5_china_vi.docx"
)

echo "[4] English manuscripts..."
# P3: figures in p3/figures/vietnam/ — run from p3/ dir so relative paths resolve
[ -f "${SCRIPT_DIR}/p3/p3_vietnam_en_clean.md" ] && (
  cd "${SCRIPT_DIR}/p3" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${PAPER_REF}" \
    p3_vietnam_en_clean.md \
    -o "${DIST}/manuscripts/en/p3_vietnam_en_clean.docx"
)
# P4: figures in p4/figures/
[ -f "${SCRIPT_DIR}/p4/p4_singapore_en_clean.md" ] && (
  cd "${SCRIPT_DIR}/p4" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${PAPER_REF}" \
    p4_singapore_en_clean.md \
    -o "${DIST}/manuscripts/en/p4_singapore_en_clean.docx"
)
# P5: figures in p5/figures/
[ -f "${SCRIPT_DIR}/p5/p5_china_en_clean.md" ] && (
  cd "${SCRIPT_DIR}/p5" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${PAPER_REF}" \
    p5_china_en_clean.md \
    -o "${DIST}/manuscripts/en/p5_china_en_clean.docx"
)
# P6: meta-analysis manuscript — figures in p6/figures/ — run from p6/ dir
[ -f "${SCRIPT_DIR}/p6/p6_meta_manuscript_en.md" ] && (
  cd "${SCRIPT_DIR}/p6" && \
  pandoc -f gfm -t docx --resource-path=. \
    --reference-doc="${PAPER_REF}" \
    p6_meta_manuscript_en.md \
    -o "${DIST}/manuscripts/en/p6_meta_en_clean.docx"
)
# P7: capstone multi-country (no figures)
[ -f "${SCRIPT_DIR}/p7/p7_capstone_en_clean.md" ] && \
  ${PANDOC_EN} "${SCRIPT_DIR}/p7/p7_capstone_en_clean.md" \
    -o "${DIST}/manuscripts/en/p7_capstone_en_clean.docx"
# P8: Pacific SIDS boundary condition (no inline figures)
[ -f "${SCRIPT_DIR}/p8/p8_pacific_sids_en_clean.md" ] && \
  ${PANDOC_EN} "${SCRIPT_DIR}/p8/p8_pacific_sids_en_clean.md" \
    -o "${DIST}/manuscripts/en/p8_pacific_sids_en_clean.docx"

echo ""
echo "=== Build complete ==="
find "${DIST}" -name "*.docx" | wc -l
echo "DOCX files in dist/"
echo ""
echo "Verify CĐ1 margin:"
python3 -c "
from docx import Document
d = Document('${DIST}/chuyen_de_1/14_part1_intro_theory.docx')
s = d.sections[0]
print(f'  left={s.left_margin.cm:.1f}cm right={s.right_margin.cm:.1f}cm top={s.top_margin.cm:.1f}cm bottom={s.bottom_margin.cm:.1f}cm')
from docx.shared import Pt
style = d.styles[\"Normal\"]
print(f'  font={style.font.name} size={style.font.size.pt if style.font.size else \"(inherited)\"}pt')
"
