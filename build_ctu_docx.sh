#!/bin/bash
# Build CTU-formatted DOCX + PDF deliverables from dissertation Markdown sources.
# Output: dist/downloads/  (thesis chapters, CĐ1/CĐ2, P3-P8 manuscripts, references)
#
# Pipeline notes:
#   - DOCX uses pandoc's `markdown` reader (NOT gfm) so $...$ and \begin{equation}
#     render as native Word equations (OMML). yaml_metadata_block is disabled so a
#     leading `---` is treated as a horizontal rule, not YAML front matter.
#   - PDF uses XeLaTeX with FreeSerif (full Vietnamese + math + ✓/✗ glyph coverage).
#
# Prerequisites: pandoc >= 3.0, xelatex (texlive-xetex), fonts-freefont-ttf,
#   python3 (+ python-docx only if rebuilding reference templates).
#
# Usage: bash build_ctu_docx.sh              # uses existing templates in templates/
#        bash build_ctu_docx.sh --templates  # also rebuild CTU reference .docx

set -u
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATES="${SCRIPT_DIR}/templates"
DIST="${SCRIPT_DIR}/dist/downloads"
THESIS_REF="${TEMPLATES}/ctu_thesis_reference.docx"
PAPER_REF="${TEMPLATES}/ctu_paper_reference.docx"

READER="markdown-yaml_metadata_block"
PDF_OPTS=(--pdf-engine=xelatex -V mainfont="FreeSerif" -V geometry:margin=2.5cm -V fontsize=12pt)

if [[ "${1:-}" == "--templates" ]]; then
  echo "[0] Building CTU reference templates..."
  pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx
  python3 ~/.claude/skills/ctu-thesis-dossier-build/scripts/build_ctu_reference.py \
    /tmp/pandoc_default.docx "${TEMPLATES}" || echo "  (skill missing; using existing templates)"
fi

mkdir -p "${DIST}/manuscripts_vi" "${DIST}/manuscripts_en"

# build <output_basename> <source_md> <reference_doc> <resource_path>
build() {
  local name="$1" md="$2" ref="$3" rp="$4"
  [ -f "$md" ] || { echo "  SKIP (missing): $md"; return; }
  pandoc -f "$READER" -t docx --resource-path="$rp" --reference-doc="$ref" \
    "$md" -o "${DIST}/${name}.docx" 2>/dev/null \
    && echo "  docx: ${name}.docx" || echo "  ERR docx: ${name}"
  pandoc -f "$READER" "${PDF_OPTS[@]}" --resource-path="$rp" \
    "$md" -o "${DIST}/${name}.pdf" 2>/dev/null \
    && echo "  pdf : ${name}.pdf" || echo "  ERR pdf : ${name}"
}

echo "[1] Chuyên đề (CĐ1, CĐ2)..."
build "CD1_chuyen_de_1" "${SCRIPT_DIR}/chuyen_de/cd1/00_cd1_ctu_final_vi.md" "$THESIS_REF" "${SCRIPT_DIR}/chuyen_de/cd1"
build "CD2_chuyen_de_2" "${SCRIPT_DIR}/chuyen_de/cd2/00_cd2_ctu_final_vi.md" "$THESIS_REF" "${SCRIPT_DIR}/chuyen_de/cd2"

echo "[2] Luận án 5 chương..."
for f in chuong_1_gioi_thieu chuong_2_tong_quan_tai_lieu chuong_3_phuong_phap chuong_4_ket_qua chuong_5_ket_luan_de_xuat; do
  build "$f" "${SCRIPT_DIR}/thesis/${f}_vi.md" "$THESIS_REF" "${SCRIPT_DIR}/thesis"
done

echo "[3] Bản thảo tiếng Việt (P3-P8)..."
build "manuscripts_vi/p3_vietnam_vi"      "${SCRIPT_DIR}/p3/submission/p3_vietnam_vi.md"   "$THESIS_REF" "${SCRIPT_DIR}/p3"
build "manuscripts_vi/p4_singapore_vi"    "${SCRIPT_DIR}/p4/submission/p4_singapore_vi.md" "$THESIS_REF" "${SCRIPT_DIR}/p4"
build "manuscripts_vi/p5_china_vi"        "${SCRIPT_DIR}/p5/submission/p5_china_vi.md"     "$THESIS_REF" "${SCRIPT_DIR}/p5"
build "manuscripts_vi/p6_meta_vi"         "${SCRIPT_DIR}/p6/21_p6_meta_vi.md"              "$THESIS_REF" "${SCRIPT_DIR}/p6"
build "manuscripts_vi/p7_capstone_vi"     "${SCRIPT_DIR}/p7/submission/jibs_package/p7_capstone_vi.md" "$THESIS_REF" "${SCRIPT_DIR}/p7:${SCRIPT_DIR}/p7/figures"
build "manuscripts_vi/p8_pacific_sids_vi" "${SCRIPT_DIR}/p8/submission/world_development_package/p8_pacific_sids_vi.md" "$THESIS_REF" "${SCRIPT_DIR}/p8:${SCRIPT_DIR}/p8/figures"

echo "[4] Bản thảo tiếng Anh (P3-P8)..."
build "manuscripts_en/p3_vietnam_en"      "${SCRIPT_DIR}/p3/p3_vietnam_en_clean.md"   "$PAPER_REF" "${SCRIPT_DIR}/p3"
build "manuscripts_en/p4_singapore_en"    "${SCRIPT_DIR}/p4/p4_singapore_en_clean.md" "$PAPER_REF" "${SCRIPT_DIR}/p4"
build "manuscripts_en/p5_china_en"        "${SCRIPT_DIR}/p5/p5_china_en_clean.md"     "$PAPER_REF" "${SCRIPT_DIR}/p5"
build "manuscripts_en/p6_meta_en"         "${SCRIPT_DIR}/p6/p6_meta_manuscript_en.md" "$PAPER_REF" "${SCRIPT_DIR}/p6"
build "manuscripts_en/p7_capstone_en"     "${SCRIPT_DIR}/p7/p7_capstone_en_clean.md"  "$PAPER_REF" "${SCRIPT_DIR}/p7"
build "manuscripts_en/p8_pacific_sids_en" "${SCRIPT_DIR}/p8/p8_pacific_sids_en_clean.md" "$PAPER_REF" "${SCRIPT_DIR}/p8"

echo "[5] Tài liệu tham khảo..."
build "04_references_apa7" "${SCRIPT_DIR}/thesis/04_references_apa7.md" "$THESIS_REF" "${SCRIPT_DIR}/thesis"

echo ""
echo "=== Build complete ==="
echo "DOCX: $(find "${DIST}" -name '*.docx' | wc -l)  |  PDF: $(find "${DIST}" -name '*.pdf' | wc -l)"
echo "Output: ${DIST}/"
