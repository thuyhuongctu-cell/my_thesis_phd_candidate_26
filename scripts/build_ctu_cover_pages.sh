#!/usr/bin/env bash
# Build all CTU cover-page templates (10 templates) to DOCX
# Source: templates/cover_pages/[0-9]*.md
# Output: templates/cover_pages/[0-9]*.docx
#
# Templates conform to QĐ 1799/QĐ-ĐHCT (18/6/2021) appendices
# NCS info pre-filled per QĐ 4768 + 4769/QĐ-ĐHCT (15/10/2024)
#
# Usage from repo root:
#   bash scripts/build_ctu_cover_pages.sh

set -e
cd "$(dirname "$0")/.."

TEMPLATE="templates/ctu_thesis_strict.docx"
SRC_DIR="templates/cover_pages"

if [ ! -f "$TEMPLATE" ]; then
  echo "ERROR: $TEMPLATE not found"
  exit 1
fi

echo "=== Build 10 CTU cover-page templates ==="

count=0
for md in "$SRC_DIR"/[0-9]*.md; do
  base="$(basename "$md" .md)"
  out="${SRC_DIR}/${base}.docx"
  pandoc "$md" -o "$out" --reference-doc="$TEMPLATE" 2>&1 | grep -v "^$" | tail -1
  kb=$(stat -c%s "$out" | awk '{print int($1/1024)}')
  printf "  ✓ %-50s %4d KB\n" "${base}.docx" "$kb"
  count=$((count+1))
done

echo ""
echo "Built $count cover-page DOCX files in $SRC_DIR/"
echo "Template used: $TEMPLATE (CTU-strict, 1.2 line spacing, 14pt H1)"
