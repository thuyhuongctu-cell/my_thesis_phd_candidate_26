"""Apply L2 screening decisions to fulltext_to_extraction_tracker_v3.csv."""

from __future__ import annotations

import csv
import shutil
from pathlib import Path

TRACKER = Path("/home/user/PAPERS_IN_PHD_2026/p6/tools/results/fulltext_to_extraction_tracker_v3.csv")
BACKUP = TRACKER.with_suffix(".csv.bak_l2_batch")

# ---------------------------------------------------------------------------
# Decision data
# ---------------------------------------------------------------------------

Y_DECISIONS: dict[int, dict[str, str | int]] = {
    857:  {"icrv": 1, "dpl": 2, "reason": "European manufacturing I→P+productivity across 7 countries (EFIGE 2007-09)"},
    877:  {"icrv": 1, "dpl": 2, "reason": "Spanish firms with FDI in China → profitability comparison 2008-2011"},
    929:  {"icrv": 1, "dpl": 2, "reason": "EU telecom MNE multinational status → firm performance (panel 2002-2010)"},
    931:  {"icrv": 3, "dpl": 3, "reason": "Emerging market SME I→P with organisational flexibility as moderator"},
    962:  {"icrv": 0, "dpl": 3, "reason": "International SME performance with host-home country similarity as contingency"},
    974:  {"icrv": 1, "dpl": 2, "reason": "Spanish hotel chain internationalization → dynamic efficiency"},
    983:  {"icrv": 0, "dpl": 3, "reason": "Foreign R&D investment → firm financial returns vs domestic R&D"},
    1021: {"icrv": 2, "dpl": 3, "reason": "CEE firms domestic vs. international orientation → organisational performance"},
    1049: {"icrv": 1, "dpl": 3, "reason": "Korean international diversification → workplace performance (Korean WPS)"},
    1146: {"icrv": 3, "dpl": 2, "reason": "Ukrainian firm TFP determinants including export/internationalization status"},
    1156: {"icrv": 2, "dpl": 3, "reason": "FDI in South/Central Eastern Europe → corporate growth (S/CEE)"},
}

N_DECISIONS: dict[int, str] = {
    864:  "IV is firm capabilities, no internationalization variable",
    868:  "DV is innovation output, not financial/productivity performance",
    871:  "No I→P — internet marketing for South African SMEs",
    875:  "IV is cluster agglomeration, not internationalization",
    880:  "Antecedents of internationalization modes (DV=I modes)",
    881:  "DV is speed of internationalization (antecedents)",
    883:  "Conceptual/descriptive — resources and emerging market SME challenges",
    884:  "DV is partial acquisition decision (antecedents)",
    887:  "Antecedents of business group internationalization (DV=I)",
    901:  "Case study of TATA portfolio — antecedents of I",
    902:  "Review paper on family business strategy",
    912:  "Antecedents of family firm internationalization (DV=I)",
    922:  "Book, not peer-reviewed journal",
    925:  "Review paper on entrepreneurship context, no I→P",
    946:  "DV is regional/global expansion dynamics (antecedents)",
    950:  "DV is innovation output; IV is gender diversity in R&D teams",
    953:  "DV is political tie establishment (not performance)",
    969:  "DV is innovation program participation",
    981:  "No internationalization — Polish monopolistic markup distribution",
    988:  "DV is export commitment (antecedents of I)",
    991:  "IV is business networks, no internationalization",
    993:  "IV is returnee entrepreneur learning, not firm-level I→P",
    998:  "DV is VC program adoption (antecedents)",
    999:  "IV is e-business, DV is internationalization performance (not I→financial perf)",
    1020: "DV is innovation management, not financial performance",
    1037: "IV is training/collaboration, DV is innovation, no I→P",
    1043: "Country-level knowledge spillovers from high-tech imports",
    1046: "IV is network capabilities, no internationalization",
    1050: "Antecedents of Chinese firm internationalization (DV=I)",
    1076: "Conceptual model of relationship marketing, no empirical I→P",
    1078: "DV is CSR integration/responsiveness (not financial performance)",
    1080: "DV is first export market choice (antecedents of I)",
    1086: "IV is IT-enabled knowledge management, no internationalization",
    1101: "DV is firm export activity (antecedents of I)",
    1103: "DV is foreign affiliate ownership change",
    1106: "IV is entrepreneurial orientation, no internationalization",
    1108: "Qualitative/descriptive study of Italian SME internationalization process",
    1138: "Theoretical model of FDI vs export choice, no I→P empirics",
    1142: "DV is entry mode choice (acquisition vs greenfield)",
}

# ---------------------------------------------------------------------------
# Apply updates
# ---------------------------------------------------------------------------

shutil.copy2(TRACKER, BACKUP)
print(f"Backup written: {BACKUP}")

rows = list(csv.DictReader(TRACKER.read_text(encoding="utf-8").splitlines()))
fieldnames = list(rows[0].keys()) if rows else []

y_applied = 0
n_applied = 0
icrv_dpl_set = 0

for row in rows:
    seq = int(row["seq"])

    if seq in Y_DECISIONS:
        data = Y_DECISIONS[seq]
        row["fulltext_screening_decision"] = "Y"
        row["exclusion_reason"] = ""  # clear any prior flag
        # fulltext_screening_reason not a real column; stored in notes or exclusion_reason?
        # The skill uses exclusion_reason for N; for Y we store reason in notes_for_extractor
        # Check: the task says "fulltext_screening_reason" — map to exclusion_reason for Y too
        # (no separate column exists; we'll write to notes_for_extractor as supplemental)
        # Store reason in exclusion_reason field (repurposed for Y context notes)
        # Actually per tracker schema, we'll put the reason in a safe visible field.
        # Use notes_for_extractor if blank, else append.
        reason = str(data["reason"])
        existing_notes = row.get("notes_for_extractor", "").strip()
        if existing_notes:
            row["notes_for_extractor"] = existing_notes + " | L2_reason: " + reason
        else:
            row["notes_for_extractor"] = "L2_reason: " + reason

        # Only set icrv/dpl if blank
        if not row.get("icrv", "").strip():
            row["icrv"] = str(data["icrv"])
            icrv_dpl_set += 1
        if not row.get("dpl", "").strip():
            row["dpl"] = str(data["dpl"])

        y_applied += 1

    elif seq in N_DECISIONS:
        row["fulltext_screening_decision"] = "N"
        row["exclusion_reason"] = N_DECISIONS[seq]
        n_applied += 1

# ---------------------------------------------------------------------------
# Write back
# ---------------------------------------------------------------------------

with TRACKER.open("w", newline="", encoding="utf-8") as fh:
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nApply summary:")
print(f"  Y applied  : {y_applied}")
print(f"  N applied  : {n_applied}")
print(f"  icrv/dpl set (was blank): {icrv_dpl_set}")

# ---------------------------------------------------------------------------
# Tracker totals
# ---------------------------------------------------------------------------

total_y = sum(1 for r in rows if r.get("fulltext_screening_decision", "") == "Y")
total_n = sum(1 for r in rows if r.get("fulltext_screening_decision", "").startswith("N"))
total_unsure = sum(1 for r in rows if "UNSURE" in r.get("fulltext_screening_decision", ""))
total_blank = sum(1 for r in rows if not r.get("fulltext_screening_decision", "").strip())

print(f"\nTracker totals (all rows):")
print(f"  Y       : {total_y}")
print(f"  N (all) : {total_n}")
print(f"  UNSURE  : {total_unsure}")
print(f"  Blank   : {total_blank}")
print(f"  Total   : {len(rows)}")
