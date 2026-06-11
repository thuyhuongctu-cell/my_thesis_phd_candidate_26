#!/usr/bin/env bash
# Run a Stata do-file in batch mode and surface errors. Falls back with a clear
# message when no Stata binary is present (use the Python pipelines in scripts/).
# Usage: run_stata.sh path/to/file.do
set -euo pipefail
DO="${1:?usage: run_stata.sh <file.do>}"
BIN="$(command -v stata-mp || command -v stata-se || command -v stata || command -v xstata || true)"
if [[ -z "$BIN" ]]; then
  echo "No Stata binary found. Use the Python fallback:"
  echo "  python3 scripts/build_pooled_dataset.py"
  echo "  python3 scripts/p7_reestimate_check.py"
  exit 3
fi
"$BIN" -b do "$DO"
LOG="${DO%.do}.log"
if grep -qE "^r\([0-9]+\);" "$LOG"; then
  echo "STATA ERROR in $LOG:"; grep -nE "^r\([0-9]+\);" "$LOG"; tail -30 "$LOG"; exit 1
fi
echo "OK -> $LOG"; tail -25 "$LOG"
