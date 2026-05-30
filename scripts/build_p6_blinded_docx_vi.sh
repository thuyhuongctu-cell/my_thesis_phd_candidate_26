#!/usr/bin/env bash
# build_p6_blinded_docx_vi.sh
#
# Build the blinded P6 Vietnamese manuscript .docx for academic submission
# (defense, supervisor review, conference VI version), from the master
# Vietnamese Markdown source p6/p6_meta_manuscript_vi.md.
#
#   - Blinds author-identifying content (author block + PI name) for double-blind review.
#   - Renders via pandoc + templates/ctu_paper_reference.docx.
#   - Embeds Figures 1-6 from p6/figures/.
#
# Output: p6/submission/mir_package/01_manuscript_blinded_vi.docx
# Prereqs: pandoc >= 3.0, python3, templates/ctu_paper_reference.docx
#
# Usage: bash scripts/build_p6_blinded_docx_vi.sh

set -euo pipefail
cd "$(dirname "$0")/.."

SRC="p6/p6_meta_manuscript_vi.md"
OUT="p6/submission/mir_package/01_manuscript_blinded_vi.docx"
TEMPLATE="templates/ctu_paper_reference.docx"
TMP="$(mktemp /tmp/p6_blinded_vi_XXXXXX.md)"
trap 'rm -f "$TMP"' EXIT

command -v pandoc >/dev/null 2>&1 || { echo "ERROR: pandoc not installed." >&2; exit 1; }
[[ -f "$TEMPLATE" ]] || { echo "ERROR: $TEMPLATE missing." >&2; exit 1; }
[[ -f "$SRC" ]] || { echo "ERROR: $SRC missing." >&2; exit 1; }

# Blind author-identifying content
python3 - "$SRC" "$TMP" <<'PY'
import sys, re
src, tmp = sys.argv[1], sys.argv[2]
out = []
for ln in open(src, encoding="utf-8"):
    s = ln.rstrip("\n")
    if re.match(r'^\*\*(Đỗ|Phan).*(Cần Thơ|Can Tho)', s):
        continue
    s = s.replace('(do tác giả thứ nhất thực hiện)', '(do coder chính thực hiện)')
    out.append(s)
text = "\n".join(out)
text = re.sub(r'(^# .+\n)\n+(\*Bản thảo chuẩn bị)', r'\1\n\2', text, count=1, flags=re.M)
open(tmp, "w", encoding="utf-8").write(text + "\n")
PY

# Safety check: confirm no author tokens leaked
if grep -qiE "Đỗ Thị|Phan Anh Tú|Thúy Hương|Thùy Hương|huongdt|vlute" "$TMP"; then
  echo "ERROR: author-identifying token still present in blinded source, aborting." >&2
  grep -niE "Đỗ Thị|Phan Anh Tú|Thúy Hương|Thùy Hương|huongdt|vlute" "$TMP" >&2
  exit 1
fi

echo "[docx] P6 VI (blinded) -> $OUT"
pandoc \
  --from "gfm+tex_math_dollars" \
  --to docx \
  --reference-doc "$TEMPLATE" \
  --resource-path "p6:p6/submission/mir_package:." \
  --highlight-style tango \
  "$TMP" -o "$OUT"
echo "       $(du -h "$OUT" | cut -f1) written"
