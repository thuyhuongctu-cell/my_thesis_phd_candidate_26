#!/usr/bin/env bash
# =============================================================================
# P6 Meta-Analysis Pipeline Runner
# =============================================================================
# Step 1: Parse markdown database → CSV  (Python)
# Step 2: Run three-level MARA           (R / metafor)
#
# Requires: Python 3.8+ (no extra packages)
# Option A: R + metafor + readr + dplyr installed locally
# Option B: Docker (rocker/tidyverse) — see docker-compose.yml
# =============================================================================

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
P6_DIR="$(dirname "$SCRIPT_DIR")"

DATA_CSV="$P6_DIR/data/p6_study_database.csv"

echo "=== Step 1: Study database ==="
# The committed CSV (k=238, K=288) is the authoritative coded dataset that the
# manuscript and validated results depend on. Re-parsing the markdown is only
# done on explicit request (--parse) or when the CSV is missing, to avoid
# silently regressing the dataset.
if [[ "${1:-}" == "--parse" || ! -f "$DATA_CSV" ]]; then
  echo "Parsing markdown -> CSV"
  python3 "$SCRIPT_DIR/p6_parse_database.py" \
    --input  "$P6_DIR/p6_study_database_coded.md" \
    --output "$DATA_CSV"
else
  echo "Using existing $DATA_CSV (pass --parse to regenerate from markdown)"
fi

echo ""
echo "=== Step 2: Run three-level MARA ==="
# Prefer R/metafor (reference); fall back to Docker, then the pure-Python port.
# The Python port reproduces the R results tables byte-for-byte (validated).
mkdir -p "$P6_DIR/results"
docker_ready() { command -v docker &>/dev/null && docker info &>/dev/null; }
if command -v Rscript &>/dev/null; then
  echo "Using local Rscript + metafor"
  Rscript "$SCRIPT_DIR/p6_real_mara.R" 2>&1 | tee "$P6_DIR/results/mara_output.txt"
elif docker_ready; then
  echo "Rscript not found. Running via Docker (rocker/tidyverse)..."
  docker run --rm \
    -v "$P6_DIR":/analysis/p6 \
    -w /analysis \
    rocker/tidyverse:4.3.2 \
    Rscript /analysis/p6/scripts/p6_real_mara.R 2>&1 | tee "$P6_DIR/results/mara_output.txt"
else
  echo "Neither Rscript nor a running Docker daemon found."
  echo "Using pure-Python port (no R needed)."
  python3 "$SCRIPT_DIR/p6_real_mara.py" 2>&1 | tee "$P6_DIR/results/mara_output.txt"
fi

echo ""
echo "=== Step 3: Regenerate manuscript figures ==="
python3 "$SCRIPT_DIR/generate_p6_figures.py" 2>&1 | tee -a "$P6_DIR/results/mara_output.txt" || \
  echo "Figure generation skipped (matplotlib unavailable)."

echo ""
echo "=== Pipeline complete ==="
echo "Results: $P6_DIR/results/"
ls -lh "$P6_DIR/results/" 2>/dev/null || true
