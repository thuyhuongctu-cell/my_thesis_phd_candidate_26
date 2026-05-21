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

echo "=== Step 1: Parse study database ==="
python3 "$SCRIPT_DIR/p6_parse_database.py" \
  --input  "$P6_DIR/p6_study_database_coded.md" \
  --output "$P6_DIR/data/p6_study_database.csv"

echo ""
echo "=== Step 2: Run MARA (R required) ==="

if command -v Rscript &>/dev/null; then
  Rscript "$SCRIPT_DIR/p6_real_mara.R" 2>&1 | tee "$P6_DIR/results/mara_output.txt"
else
  echo "Rscript not found. Running via Docker..."
  docker run --rm \
    -v "$P6_DIR":/analysis/p6 \
    -w /analysis \
    rocker/tidyverse:4.3.2 \
    Rscript /analysis/p6/scripts/p6_real_mara.R 2>&1 | tee "$P6_DIR/results/mara_output.txt"
fi

echo ""
echo "=== Pipeline complete ==="
echo "Results: $P6_DIR/results/"
ls -lh "$P6_DIR/results/" 2>/dev/null || true
