#!/usr/bin/env bash
# build_submission_package.sh
#
# Build journal-ready DOCX submission packages for P3 (APJM), P4 (MIR),
# and P5 (APJM) from their respective Markdown sources.
#
# - P3, P4, and P5 all build from their single-file clean Markdown sources
#   under manuscripts/. The 7-part APJM split for P5 lives under
#   manuscripts/p5_china/apjm/ and shares the same content (modulo figure
#   embeds); it is preserved for the original APJM build_docx.sh workflow
#   which injects figures via regex.
# - All three are converted via pandoc with the CTU paper reference template
#   (TNR 12pt, 2.5cm margins, 1.15 line spacing, justified). Math is rendered
#   via OMML using --from gfm+tex_math_dollars.
#
# Outputs land under dist/submission/ (gitignored).
#
# Prerequisites:
#   - pandoc >= 3.0  (apt install pandoc / brew install pandoc)
#   - python-docx     (pip install python-docx)
#   - templates/ctu_paper_reference.docx generated via build_ctu_reference.py
#
# Usage:  bash scripts/build_submission_package.sh

set -euo pipefail
cd "$(dirname "$0")/.."

OUT_DIR="dist/submission"
TEMPLATE="templates/ctu_paper_reference.docx"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc not installed. Install via 'apt install pandoc' or 'brew install pandoc'." >&2
  exit 1
fi

if [[ ! -f "$TEMPLATE" ]]; then
  echo "ERROR: $TEMPLATE missing. Run: python3 scripts/build_ctu_reference.py /tmp/pandoc_default.docx templates/" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

PANDOC_OPTS=(
  --from "gfm+tex_math_dollars"
  --to docx
  --reference-doc "$TEMPLATE"
  --resource-path "manuscripts"
  --highlight-style tango
)

build_one() {
  local label="$1"
  local source="$2"
  local journal="$3"
  local out="$OUT_DIR/${label}_${journal}.docx"

  echo "[build] $label -> $out"
  pandoc "${PANDOC_OPTS[@]}" "$source" -o "$out"
  echo "        $(du -h "$out" | cut -f1) written"
}

# P3 Vietnam — single file, APJM target
build_one "p3_vietnam" "manuscripts/p3_vietnam_en_clean.md" "APJM"

# P4 Singapore — single file, MIR target
build_one "p4_singapore" "manuscripts/p4_singapore_en_clean.md" "MIR"

# P5 China — single-file build using the synced clean source (figures
# already embedded). The 7-part split under manuscripts/p5_china/apjm/ is
# kept for the original APJM build_docx.sh workflow which injects figures
# via regex; both sources contain the same content modulo figure embeds.
build_one "p5_china" "manuscripts/p5_china_en_clean.md" "APJM"

echo ""
echo "=== Submission package built ==="
ls -la "$OUT_DIR"
echo ""
echo "Upload to each journal's manuscript slot:"
echo "  P3 -> APJM  : $OUT_DIR/p3_vietnam_APJM.docx"
echo "  P4 -> MIR   : $OUT_DIR/p4_singapore_MIR.docx"
echo "  P5 -> APJM  : $OUT_DIR/p5_china_APJM.docx"
