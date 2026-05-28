#!/usr/bin/env bash
# build_submission_package.sh
#
# Build journal-ready submission artefacts for P3 (APJM), P4 (MIR), and
# P5 (IJOEM):
#   - DOCX  via pandoc + ctu_paper_reference.docx (TNR 12pt, 2.5cm, 1.15 line)
#   - TEX   via pandoc + templates/springer_paper.tex (Springer-compatible
#           article class; APA7 references via natbib)
#   - PDF   via pdflatex on the .tex (optional, falls back gracefully)
#
# - P3, P4, and P5 all build from their single-file clean Markdown sources
#   under manuscripts/. The 7-part IJOEM split for P5 lives under
#   manuscripts/p5_china/ijoem/ and shares the same content (modulo figure
#   embeds); it is preserved for the original IJOEM build_docx.sh workflow.
#
# Outputs land under dist/submission/ (gitignored).
#
# Prerequisites:
#   - pandoc >= 3.0
#   - python-docx
#   - templates/ctu_paper_reference.docx (generated via build_ctu_reference.py)
#   - templates/springer_paper.tex (committed to repo)
#   - pdflatex (texlive-latex-base + texlive-latex-extra) — optional for PDF
#
# Usage:  bash scripts/build_submission_package.sh

set -euo pipefail
cd "$(dirname "$0")/.."

OUT_DIR="dist/submission"
DOCX_TEMPLATE="templates/ctu_paper_reference.docx"
TEX_TEMPLATE="templates/springer_paper.tex"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc not installed." >&2
  exit 1
fi

if [[ ! -f "$DOCX_TEMPLATE" ]]; then
  echo "ERROR: $DOCX_TEMPLATE missing. Run: python3 scripts/build_ctu_reference.py /tmp/pandoc_default.docx templates/" >&2
  exit 1
fi

if [[ ! -f "$TEX_TEMPLATE" ]]; then
  echo "ERROR: $TEX_TEMPLATE missing." >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

PANDOC_DOCX_OPTS=(
  --from "gfm+tex_math_dollars"
  --to docx
  --reference-doc "$DOCX_TEMPLATE"
  --resource-path "manuscripts"
  --highlight-style tango
)

PANDOC_TEX_OPTS=(
  --from "gfm+tex_math_dollars"
  --to latex
  --template "$TEX_TEMPLATE"
  --resource-path "manuscripts"
  --standalone
)

build_one() {
  local label="$1"
  local source="$2"
  local journal="$3"
  local out_docx="$OUT_DIR/${label}_${journal}.docx"
  local out_tex="$OUT_DIR/${label}_${journal}.tex"

  echo "[docx] $label -> $out_docx"
  pandoc "${PANDOC_DOCX_OPTS[@]}" "$source" -o "$out_docx"
  echo "       $(du -h "$out_docx" | cut -f1) written"

  echo "[tex]  $label -> $out_tex"
  pandoc "${PANDOC_TEX_OPTS[@]}" \
    --metadata title="$label submission to $journal (blind review)" \
    --metadata date="$(date +%Y-%m-%d)" \
    "$source" -o "$out_tex"
  echo "       $(du -h "$out_tex" | cut -f1) written"
}

build_one "p3_vietnam"      "manuscripts/p3_vietnam_en_clean.md"   "APJM"
build_one "p4_singapore"    "manuscripts/p4_singapore_en_clean.md" "MIR"
build_one "p5_china"        "manuscripts/p5_china_en_clean.md"     "IJOEM"

# Vietnamese translations (academic VN versions for CTU / thesis dossier).
# Use the CTU thesis reference template (TNR 13pt, 1.5 line spacing,
# margins 3-2-2-2 cm) since VN versions target Vietnamese academic /
# thesis review, not the international Springer paper format.
if [[ -f "templates/ctu_thesis_reference.docx" ]]; then
  PANDOC_DOCX_OPTS_VN=(
    --from "gfm+tex_math_dollars"
    --to docx
    --reference-doc "templates/ctu_thesis_reference.docx"
    --resource-path "manuscripts"
    --highlight-style tango
  )

  build_one_vn() {
    local label="$1"
    local source="$2"
    local out_docx="$OUT_DIR/${label}_VN.docx"
    local out_tex="$OUT_DIR/${label}_VN.tex"

    echo "[docx-vn] $label -> $out_docx"
    pandoc "${PANDOC_DOCX_OPTS_VN[@]}" "$source" -o "$out_docx"
    echo "          $(du -h "$out_docx" | cut -f1) written"

    echo "[tex-vn]  $label -> $out_tex"
    pandoc "${PANDOC_TEX_OPTS[@]}" \
      --metadata title="$label (bản dịch tiếng Việt)" \
      --metadata date="$(date +%Y-%m-%d)" \
      "$source" -o "$out_tex"
    echo "          $(du -h "$out_tex" | cut -f1) written"
  }

  [[ -f manuscripts/p3_vietnam_vi_clean.md   ]] && build_one_vn "p3_vietnam"   "manuscripts/p3_vietnam_vi_clean.md"
  [[ -f manuscripts/p4_singapore_vi_clean.md ]] && build_one_vn "p4_singapore" "manuscripts/p4_singapore_vi_clean.md"
  [[ -f manuscripts/p5_china_vi_clean.md     ]] && build_one_vn "p5_china"     "manuscripts/p5_china_vi_clean.md"
fi

echo ""
echo "=== Submission package built ==="
ls -la "$OUT_DIR" | grep -E "\.docx|\.tex|\.pdf" || true

# Optional PDF compilation. Prefer xelatex (native Unicode support for β, −,
# ×, Greek letters used in inline stats) when available; fall back to
# pdflatex (will fail on Unicode but useful as a portability check).
LATEX_ENGINE=""
if command -v xelatex >/dev/null 2>&1; then
  LATEX_ENGINE="xelatex"
elif command -v lualatex >/dev/null 2>&1; then
  LATEX_ENGINE="lualatex"
elif command -v pdflatex >/dev/null 2>&1; then
  LATEX_ENGINE="pdflatex"
fi

if [[ -n "$LATEX_ENGINE" ]]; then
  echo ""
  echo "=== Compiling PDF via $LATEX_ENGINE ==="
  # Copy figures into OUT_DIR so \includegraphics paths resolve.
  if [[ -d "manuscripts/figures" && ! -d "$OUT_DIR/figures" ]]; then
    cp -r manuscripts/figures "$OUT_DIR/"
  fi
  for tex in "$OUT_DIR"/*.tex; do
    base=$(basename "$tex" .tex)
    echo "[pdf]  $base (via $LATEX_ENGINE)"
    (
      cd "$OUT_DIR"
      "$LATEX_ENGINE" -interaction=nonstopmode "$(basename "$tex")" \
        > "${base}_latex.log" 2>&1 \
        || echo "       [warn] $LATEX_ENGINE emitted errors (see ${base}_latex.log)"
      "$LATEX_ENGINE" -interaction=nonstopmode "$(basename "$tex")" \
        >> "${base}_latex.log" 2>&1 || true
    )
    if [[ -f "$OUT_DIR/${base}.pdf" ]]; then
      echo "       $(du -h "$OUT_DIR/${base}.pdf" | cut -f1) written"
    fi
  done
  # Clean LaTeX auxiliary files
  (cd "$OUT_DIR" && rm -f *.aux *.out *.toc *.lof *.lot *.bbl *.blg *.synctex.gz *.fdb_latexmk *.fls)
fi

echo ""
echo "Upload to each journal's manuscript slot:"
echo "  P3 -> APJM  : $OUT_DIR/p3_vietnam_APJM.{docx,tex,pdf}"
echo "  P4 -> MIR   : $OUT_DIR/p4_singapore_MIR.{docx,tex,pdf}"
echo "  P5 -> IJOEM : $OUT_DIR/p5_china_IJOEM.{docx,tex,pdf}"
