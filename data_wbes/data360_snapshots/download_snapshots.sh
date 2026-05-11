#!/usr/bin/env bash
# download_snapshots.sh — Download Prosperity Data360 FCI Snapshots for all ICRV countries
#
# Usage: Run on a machine with unrestricted internet access.
#   chmod +x download_snapshots.sh
#   ./download_snapshots.sh
#
# Output: PDFs saved to subdirectories per economy under data_wbes/data360_snapshots/
# After download: update 00_registry.md status from "profile-only" to "saved"
#
# NOTE: This script navigates the Prosperity Data360 portal profile pages.
# Since PDFs are served from documents1.worldbank.org with per-document IDs,
# automated curl download requires knowing the document ID first.
# Use the --list-profiles flag to open profile pages for manual download,
# or run the --curl flag once you have added document IDs to DOCUMENT_IDS below.

set -euo pipefail

OUTDIR="$(cd "$(dirname "$0")" && pwd)"

# ── Known direct PDF URLs (add document IDs here as you find them) ──────────
# Format: [ISO3]="<full URL to PDF>"
declare -A KNOWN_PDF_URLS=(
    [VNM]="https://documents1.worldbank.org/curated/en/099063024172020869/pdf/IDUe54dba0590464b14888fe2ca18eba2c8.pdf"
    # Add more as discovered, e.g.:
    # [SGP]="https://documents1.worldbank.org/curated/en/XXXXXXXXX/pdf/IDU-XXXXXXXX.pdf"
    # [CHN]="https://documents1.worldbank.org/curated/en/XXXXXXXXX/pdf/IDU-XXXXXXXX.pdf"
    # [IND]="https://documents1.worldbank.org/curated/en/XXXXXXXXX/pdf/IDU-XXXXXXXX.pdf"
)

# ── All ICRV economies ───────────────────────────────────────────────────────
declare -A ECONOMIES=(
    # Group I — Advanced Innovation-Driven
    [SGP]="Singapore"
    [HKG]="Hong_Kong_SAR"
    [KOR]="Korea"
    [TWN]="Taiwan"
    [ISR]="Israel"
    # Group II — Advanced Resource-Driven
    [SAU]="Saudi_Arabia"
    [QAT]="Qatar"
    [KWT]="Kuwait"
    [BHR]="Bahrain"
    [BRN]="Brunei"
    # Group III — Upper-Middle
    [CHN]="China"
    [MYS]="Malaysia"
    [THA]="Thailand"
    [KAZ]="Kazakhstan"
    [ARM]="Armenia"
    [GEO]="Georgia"
    # Group IV — Emerging
    [VNM]="Vietnam"
    [IDN]="Indonesia"
    [PHL]="Philippines"
    [IND]="India"
    [LKA]="Sri_Lanka"
    [JOR]="Jordan"
    [MNG]="Mongolia"
    # Group V — Frontier
    [BGD]="Bangladesh"
    [PAK]="Pakistan"
    [LAO]="Lao_PDR"
    [KHM]="Cambodia"
    [MMR]="Myanmar"
    [NPL]="Nepal"
    [BTN]="Bhutan"
    [MDV]="Maldives"
    [UZB]="Uzbekistan"
    [TJK]="Tajikistan"
    [KGZ]="Kyrgyz_Republic"
    [TKM]="Turkmenistan"
    [AFG]="Afghanistan"
    [TLS]="Timor-Leste"
    [IRQ]="Iraq"
    [LBN]="Lebanon"
    [YEM]="Yemen"
    # Group VI — SIDS Pacific
    [FJI]="Fiji"
    [PNG]="Papua_New_Guinea"
    [SLB]="Solomon_Islands"
    [TON]="Tonga"
    [VUT]="Vanuatu"
    [WSM]="Samoa"
    [KIR]="Kiribati"
)

# ── Functions ────────────────────────────────────────────────────────────────

list_profiles() {
    echo ""
    echo "Prosperity Data360 Economy Profile URLs (open each to find FCI snapshot):"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    for iso3 in $(echo "${!ECONOMIES[@]}" | tr ' ' '\n' | sort); do
        echo "  ${iso3}  ${ECONOMIES[$iso3]}"
        echo "       https://prosperitydata360.worldbank.org/en/economy/${iso3}"
    done
    echo ""
    echo "Steps to get the PDF URL:"
    echo "  1. Open the profile URL above"
    echo "  2. Click 'Economy Snapshot' tab"
    echo "  3. Select 'Finance, Competitiveness & Innovation'"
    echo "  4. Right-click 'Download PDF' → 'Copy link address'"
    echo "  5. Add the URL to KNOWN_PDF_URLS in this script"
    echo "  6. Re-run: ./download_snapshots.sh --curl"
}

download_known() {
    echo ""
    echo "Downloading PDFs for economies with known URLs..."
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    local count=0
    for iso3 in "${!KNOWN_PDF_URLS[@]}"; do
        local name="${ECONOMIES[$iso3]:-$iso3}"
        local name_lower
        name_lower=$(echo "$name" | tr '[:upper:]' '[:lower:]')
        local outsubdir="${OUTDIR}/${name_lower}"
        mkdir -p "$outsubdir"
        local outfile="${outsubdir}/${name_lower}_fci_snapshot.pdf"
        if [[ -f "$outfile" ]]; then
            echo "  ✓  ${iso3} — already exists, skipping"
        else
            echo "  ↓  ${iso3} — ${ECONOMIES[$iso3]}"
            curl -L --retry 3 --retry-delay 2 \
                 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
                 -o "$outfile" \
                 "${KNOWN_PDF_URLS[$iso3]}" \
                 && echo "     saved → ${outfile}" \
                 || echo "     ❌ FAILED — check URL"
            count=$((count + 1))
            sleep 1  # polite delay
        fi
    done
    echo ""
    echo "Done. ${count} file(s) downloaded."
}

# ── Main ─────────────────────────────────────────────────────────────────────

case "${1:-}" in
    --list-profiles | -l)
        list_profiles
        ;;
    --curl | -d)
        download_known
        ;;
    "")
        echo ""
        echo "Prosperity Data360 FCI Snapshot Downloader"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "  ${#ECONOMIES[@]} ICRV economies  |  ${#KNOWN_PDF_URLS[@]} known PDF URL(s)"
        echo ""
        echo "Usage:"
        echo "  ./download_snapshots.sh --list-profiles   # show all 47 profile URLs"
        echo "  ./download_snapshots.sh --curl            # download PDFs with known URLs"
        echo ""
        echo "Vietnam FCI snapshot is already saved to:"
        echo "  vietnam/vietnam_fci_snapshot_oct2025.pdf"
        echo ""
        echo "To get remaining snapshots:"
        echo "  1. Run: ./download_snapshots.sh --list-profiles"
        echo "  2. Visit each URL, locate the FCI snapshot PDF link"
        echo "  3. Add URL to KNOWN_PDF_URLS in this script"
        echo "  4. Run: ./download_snapshots.sh --curl"
        ;;
    *)
        echo "Unknown option: $1"
        echo "Use --list-profiles or --curl"
        exit 1
        ;;
esac
