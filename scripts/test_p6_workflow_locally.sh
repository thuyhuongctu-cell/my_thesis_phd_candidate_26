#!/usr/bin/env bash
# test_p6_workflow_locally.sh
#
# Locally simulate the P6 GitHub Actions workflows
# (pdf_download_extract.yml, doi_enrichment.yml, abstract_fetch.yml,
#  scopus_api_search.yml, p6_full_search.yml) without committing to a
# branch — useful to verify pip deps + script paths + CSV inputs
# before triggering a real workflow run from the Actions tab.
#
# Prerequisites:
#   - Checked out on branch claude/edit-vietnamese-academic-standards-xcAmn
#     (or any branch with p6/tools/ present)
#   - python3 with pip
#   - API keys exported as env vars:  WOS_API_KEY, SCOPUS_API_KEY,
#     OPENALEX_API_KEY  (or pass on the command line)
#
# Usage:
#   bash scripts/test_p6_workflow_locally.sh <workflow_name>
#
# Workflow names accepted:
#   pdf_download_extract
#   doi_enrichment
#   abstract_fetch
#   scopus_api_search
#   p6_full_search

set -uo pipefail

WORKFLOW="${1:-pdf_download_extract}"
TODAY="$(date +%Y%m%d)"
cd "$(dirname "$0")/.."

PROJECT_ROOT="$(pwd)"
P6_DIR="$PROJECT_ROOT/p6"
TOOLS="$P6_DIR/tools"
RESULTS="$TOOLS/results"

if [[ ! -d "$TOOLS" ]]; then
  echo "ERROR: $TOOLS not found. Switch to the branch that contains p6/ (e.g.,"
  echo "       claude/edit-vietnamese-academic-standards-xcAmn) and re-run." >&2
  exit 1
fi

mkdir -p "$RESULTS"

# ── Helper: install pip deps once per workflow ──────────────────────────
ensure_deps() {
  for pkg in "$@"; do
    if ! python3 -c "import $pkg" >/dev/null 2>&1; then
      echo "[deps] installing $pkg"
      pip install --quiet "$pkg"
    fi
  done
}

# ── Workflow: pdf_download_extract ──────────────────────────────────────
run_pdf_download_extract() {
  echo "=== Simulating workflow: pdf_download_extract ==="
  ensure_deps requests pdfplumber
  local queue="${QUEUE_FILE:-extraction_queue_y_${TODAY}.csv}"
  local limit="${LIMIT:-0}"
  local run_extract="${RUN_EXTRACT:-true}"

  if [[ ! -f "$RESULTS/$queue" ]]; then
    echo "WARN: $RESULTS/$queue not found — listing available extraction queues:"
    ls "$RESULTS"/extraction_queue_*.csv 2>/dev/null || echo "  (none)"
    return 1
  fi

  mkdir -p /tmp/p6_pdfs
  python3 "$TOOLS/48_download_repo_pdfs.py" \
    --queue "$RESULTS/$queue" \
    --output-dir /tmp/p6_pdfs \
    --limit "$limit" || echo "WARN: 48_download_repo_pdfs.py exited non-zero"

  echo "PDFs downloaded to /tmp/p6_pdfs: $(ls /tmp/p6_pdfs/*.pdf 2>/dev/null | wc -l)"

  if [[ "$run_extract" == "true" && -f "$TOOLS/41_auto_extract_from_pdfs.py" ]]; then
    python3 "$TOOLS/41_auto_extract_from_pdfs.py" \
      --pdf-dir /tmp/p6_pdfs \
      --tracker "$RESULTS/fulltext_to_extraction_tracker_v3.csv" \
      || echo "WARN: 41_auto_extract_from_pdfs.py exited non-zero"
  fi
}

# ── Workflow: doi_enrichment ────────────────────────────────────────────
run_doi_enrichment() {
  echo "=== Simulating workflow: doi_enrichment ==="
  ensure_deps requests
  local input="${INPUT_FILE:-new_candidates_${TODAY}.csv}"
  local output="${OUTPUT_FILE:-new_candidates_${TODAY}_doi_enriched.csv}"
  local max="${MAX_RECORDS:-0}"

  if [[ ! -f "$RESULTS/$input" ]]; then
    echo "WARN: $RESULTS/$input not found — listing available candidate CSVs:"
    ls "$RESULTS"/new_candidates_*.csv 2>/dev/null || echo "  (none)"
    return 1
  fi

  python3 "$TOOLS/07_enrich_doi_crossref.py" \
    --input "$RESULTS/$input" \
    --output "$RESULTS/$output" \
    --email huongp1323001@gstudent.ctu.edu.vn \
    --max "$max"
}

# ── Workflow: abstract_fetch ────────────────────────────────────────────
run_abstract_fetch() {
  echo "=== Simulating workflow: abstract_fetch ==="
  ensure_deps requests
  local input="${INPUT_FILE:-new_candidates_screened_${TODAY}.csv}"
  local output="${OUTPUT_FILE:-abstracts_${TODAY}.csv}"
  local max="${MAX_RECORDS:-0}"
  local delay="${DELAY:-0.25}"

  if [[ ! -f "$RESULTS/$input" ]]; then
    echo "WARN: $RESULTS/$input not found — listing available screened CSVs:"
    ls "$RESULTS"/*_screened_*.csv 2>/dev/null || echo "  (none)"
    return 1
  fi

  python3 "$TOOLS/34_fetch_abstracts.py" \
    --input "$RESULTS/$input" \
    --output "$RESULTS/$output" \
    --max-records "$max" \
    --delay "$delay"
}

# ── Workflow: scopus_api_search ─────────────────────────────────────────
run_scopus_api_search() {
  echo "=== Simulating workflow: scopus_api_search ==="
  ensure_deps requests
  if [[ -z "${SCOPUS_API_KEY:-}" ]]; then
    echo "ERROR: SCOPUS_API_KEY env var not set." >&2
    return 1
  fi
  local max="${MAX_RECORDS:-5000}"
  SCOPUS_API_KEY="$SCOPUS_API_KEY" python3 "$TOOLS/05_scopus_api_search.py" \
    --max "$max" \
    --output "$RESULTS/scopus_api_${TODAY}.csv"
}

# ── Workflow: p6_full_search (all three providers) ──────────────────────
run_p6_full_search() {
  echo "=== Simulating workflow: p6_full_search ==="
  ensure_deps requests
  local max_wos="${MAX_WOS:-2500}"
  local max_scopus="${MAX_SCOPUS:-5000}"

  if [[ -n "${WOS_API_KEY:-}" ]]; then
    WOS_API_KEY="$WOS_API_KEY" python3 "$TOOLS/06_wos_api_search.py" \
      --max "$max_wos" \
      --output "$RESULTS/wos_api_${TODAY}.csv" \
      || echo "WARN: WoS step exited non-zero"
  else
    echo "[skip] WOS_API_KEY not set"
  fi

  if [[ -n "${SCOPUS_API_KEY:-}" ]]; then
    SCOPUS_API_KEY="$SCOPUS_API_KEY" python3 "$TOOLS/05_scopus_api_search.py" \
      --max "$max_scopus" \
      --output "$RESULTS/scopus_api_${TODAY}.csv" \
      || echo "WARN: Scopus step exited non-zero"
  else
    echo "[skip] SCOPUS_API_KEY not set"
  fi

  echo "[info] OpenAlex step intentionally not run locally (use real workflow for the inline Python heredoc)"

  echo ""
  echo "========= LOCAL SEARCH SUMMARY ========="
  for f in "$RESULTS"/wos_api_${TODAY}.csv \
           "$RESULTS"/scopus_api_${TODAY}.csv; do
    if [[ -f "$f" ]]; then
      n=$(tail -n +2 "$f" | wc -l)
      echo "  OK  $(basename "$f"): $n records"
    else
      echo "  --  $(basename "$f"): not produced"
    fi
  done
}

case "$WORKFLOW" in
  pdf_download_extract)   run_pdf_download_extract ;;
  doi_enrichment)         run_doi_enrichment ;;
  abstract_fetch)         run_abstract_fetch ;;
  scopus_api_search)      run_scopus_api_search ;;
  p6_full_search)         run_p6_full_search ;;
  *)
    echo "Unknown workflow: $WORKFLOW" >&2
    echo "Valid: pdf_download_extract | doi_enrichment | abstract_fetch | scopus_api_search | p6_full_search" >&2
    exit 1
    ;;
esac
