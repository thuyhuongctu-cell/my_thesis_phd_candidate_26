#!/usr/bin/env bash
# build_p6_blinded_docx_mir.sh
#
# Build the blinded P6 manuscript .docx for Management International Review (MIR)
# submission, from the master Markdown source.
#
#   - Blinds author-identifying content (author block + PI name) for double-blind review.
#   - Renders via pandoc + templates/ctu_paper_reference.docx (TNR 12pt, 2.5cm, 1.15 line),
#     matching the P3/P4/P5 submission build.
#   - Embeds Figures 1-6 from p6/figures/.
#
# Output: p6/submission/mir_package/01_manuscript_blinded.docx
# Prereqs: pandoc >= 3.0, python3, templates/ctu_paper_reference.docx
#
# Usage: bash scripts/build_p6_blinded_docx_mir.sh

set -euo pipefail
cd "$(dirname "$0")/.."

SRC="p6/p6_meta_manuscript_en.md"
OUT="p6/submission/mir_package/01_manuscript_blinded.docx"
TEMPLATE="templates/ctu_paper_reference.docx"
TMP="$(mktemp /tmp/p6_blinded_mir_XXXXXX.md)"
trap 'rm -f "$TMP"' EXIT

command -v pandoc >/dev/null 2>&1 || { echo "ERROR: pandoc not installed." >&2; exit 1; }
[[ -f "$TEMPLATE" ]] || { echo "ERROR: $TEMPLATE missing." >&2; exit 1; }

# --- Blind author-identifying content ---
python3 - "$SRC" "$TMP" <<'PY'
import sys, re
src, tmp = sys.argv[1], sys.argv[2]
out = []
for ln in open(src, encoding="utf-8"):
    s = ln.rstrip("\n")
    if re.match(r'^\*\*(Đỗ|Phan).*Can Tho University', s):
        continue
    s = s.replace('(PI: Đỗ Thùy Hương)', '(by the first author)')
    out.append(s)
text = "\n".join(out)
text = re.sub(r'(^# .+\n)\n+(\*Manuscript prepared for)', r'\1\n\2', text, count=1, flags=re.M)
open(tmp, "w", encoding="utf-8").write(text + "\n")
PY

if grep -qiE "Đỗ |Phan Anh|Thúy Hương|Thùy Hương|huongdt|vlute" "$TMP"; then
  echo "ERROR: author-identifying token still present in blinded source — aborting." >&2
  grep -niE "Đỗ |Phan Anh|Thúy Hương|Thùy Hương|huongdt|vlute" "$TMP" >&2
  exit 1
fi

echo "[docx] P6 MIR (blinded) -> $OUT"
pandoc \
  --from "gfm+tex_math_dollars" \
  --to docx \
  --reference-doc "$TEMPLATE" \
  --resource-path "p6:p6/submission/mir_package:." \
  --highlight-style tango \
  "$TMP" -o "$OUT"
echo "       $(du -h "$OUT" | cut -f1) written"

for part in 02_title_page 03_cover_letter; do
  PART_SRC="p6/submission/mir_package/${part}.md"
  PART_OUT="p6/submission/mir_package/${part}.docx"
  if [[ -f "$PART_SRC" ]]; then
    echo "[docx] $part -> $PART_OUT"
    pandoc --from "gfm+tex_math_dollars" --to docx \
      --reference-doc "$TEMPLATE" --highlight-style tango \
      "$PART_SRC" -o "$PART_OUT"
    echo "       $(du -h "$PART_OUT" | cut -f1) written"
  fi
done
