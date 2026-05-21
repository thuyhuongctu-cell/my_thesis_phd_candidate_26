#!/usr/bin/env python3
"""
49_fill_icrv_dpl_gaps.py — Fill remaining blank ICRV and DPL codes.

Actions:
  1. Fix 'I' artifact ICRV → '3' (India = Emerging)
  2. Fill blank DPL from publication year (conservative heuristic)
  3. Infer ICRV for blank rows via title country-mention patterns
     — only assigns when a clear single country is detectable
     — marks as icrv_inferred='1' for manual verification

Output:
  - Updates tracker in-place (atomic write)
  - Writes p6/tools/results/icrv_dpl_fill_log_YYYYMMDD.csv
"""
import csv, re, os, sys
from datetime import date
from pathlib import Path

TRACKER = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
LOG_OUT  = f"p6/tools/results/icrv_dpl_fill_log_{date.today().strftime('%Y%m%d')}.csv"

# ── DPL from publication year ──────────────────────────────────────────────────
# Data midpoint ≈ pub_year − 3 (conservative estimate)
# DPL 1: midpoint < 2000 → pub_year ≤ 2002
# DPL 2: midpoint 2000–2009 → 2003 ≤ pub_year ≤ 2012
# DPL 3: midpoint ≥ 2010 → pub_year ≥ 2013

def dpl_from_year(yr_str: str) -> str:
    try:
        y = int(yr_str.strip())
    except (ValueError, AttributeError):
        return ""
    if y <= 2002:
        return "1"
    elif y <= 2012:
        return "2"
    return "3"


# ── ICRV from title/journal (conservative — single country signals only) ───────
# Only fire when exactly ONE country group is detected in the text.
# Multi-country indicators → ICRV = 0.

MULTI_PATTERNS = [
    r'\bmulti.countr(y|ies)\b',
    r'\bcross.countr(y|ies)\b',
    r'\bcross.national\b',
    r'\bseveral countries\b',
    r'\bmultiple countries\b',
    r'\b(ASEAN|OECD|EU|G20|BRICs?|Asia.Pacific|Asia-Pacific)\b',
    r'\b(advanced economies|emerging (markets|economies))\b',
    r'\b(developed and developing)\b',
    r'\b\d{2,3} (countries|economies|nations)\b',
]

COUNTRY_ICRV = [
    # ICRV 1 — Advanced
    (r'\b(South Korea[n]?|Korean?)\b(?!.*\bChinese?\b)',     1, "Korea"),
    (r'\b(Japan(ese)?)\b(?!.*\bChina\b)',                     1, "Japan"),
    (r'\b(Taiwan(ese)?)\b',                                   1, "Taiwan"),
    (r'\b(Singapore[an]?)\b',                                 1, "Singapore"),
    (r'\b(Hong Kong)\b',                                      1, "HongKong"),
    (r'\b(Australia[n]?|New Zealand[ers]?)\b',                1, "Aus/NZ"),
    (r'\b(United Kingdom|British|UK)\b',                      1, "UK"),
    (r'\b(Germany|German|Deutschland)\b',                     1, "Germany"),
    (r'\b(France|French)\b',                                  1, "France"),
    (r'\b(United States|US(A)?|American)\b',                  1, "USA"),
    (r'\b(Canada[ian]?)\b',                                   1, "Canada"),
    (r'\b(Sweden|Swedish|Finland|Finnish|Norway|Norwegian|Denmark|Danish)\b', 1, "Nordic"),
    (r'\b(Italy|Italian|Spain|Spanish|Portugal(ese)?)\b',     1, "SouthEU"),
    (r'\b(Israel[i]?)\b',                                     1, "Israel"),
    # ICRV 2 — Upper-middle
    (r'\b(China|Chinese|PRC)\b',                              2, "China"),
    (r'\b(Malaysia[n]?)\b',                                   2, "Malaysia"),
    (r'\b(Thailand|Thai)\b',                                  2, "Thailand"),
    (r'\b(Brazil(ian)?)\b',                                   2, "Brazil"),
    (r'\b(Turkey|Turkish|Türkiye)\b',                         2, "Turkey"),
    (r'\b(Mexico|Mexican)\b',                                 2, "Mexico"),
    (r'\b(South Africa[n]?)\b',                               2, "SouthAfrica"),
    (r'\b(Colombia[n]?)\b',                                   2, "Colombia"),
    (r'\b(Poland|Polish)\b',                                   2, "Poland"),
    (r'\b(Russia[n]?|Russian Federation)\b',                  2, "Russia"),
    (r'\b(Argentina[n]?)\b',                                  2, "Argentina"),
    (r'\b(Romania[n]?)\b',                                    2, "Romania"),
    # ICRV 3 — Emerging
    (r'\b(Vietnam(ese)?)\b',                                  3, "Vietnam"),
    (r'\b(India[n]?)\b',                                      3, "India"),
    (r'\b(Indonesia[n]?)\b',                                  3, "Indonesia"),
    (r'\b(Philippines|Filipino|Philippine)\b',                3, "Philippines"),
    (r'\b(Pakistan[i]?)\b',                                   3, "Pakistan"),
    (r'\b(Bangladesh[i]?)\b',                                 3, "Bangladesh"),
    (r'\b(Sri Lanka[n]?)\b',                                  3, "SriLanka"),
    (r'\b(Ghana[ian]?)\b',                                    3, "Ghana"),
    (r'\b(Kenya[n]?)\b',                                      3, "Kenya"),
    (r'\b(Ethiopia[n]?)\b',                                   3, "Ethiopia"),
    (r'\b(Nigeria[n]?)\b',                                    3, "Nigeria"),
    (r'\b(Egypt(ian)?)\b',                                    3, "Egypt"),
    (r'\b(Morocco|Moroccan)\b',                               3, "Morocco"),
    # ICRV 4 — GCC/Resource-rich
    (r'\b(Saudi Arabia[n]?|KSA)\b',                          4, "SaudiArabia"),
    (r'\b(UAE|United Arab Emirates|Emirati)\b',               4, "UAE"),
    (r'\b(Qatar[i]?)\b',                                      4, "Qatar"),
    (r'\b(Kuwait[i]?)\b',                                     4, "Kuwait"),
    (r'\b(Kazakhstan[i]?)\b',                                 4, "Kazakhstan"),
    # ICRV 5 — SIDS
    (r'\b(Malta[ese]?)\b',                                    5, "Malta"),
    (r'\b(Mauritius|Mauritian)\b',                            5, "Mauritius"),
    (r'\b(Cyprus|Cypriot)\b',                                 5, "Cyprus"),
    # ICRV 6 — Frontier/LDC
    (r'\b(Cambodia[n]?|Khmer)\b',                            6, "Cambodia"),
    (r'\b(Myanmar|Burmese)\b',                                6, "Myanmar"),
    (r'\b(Mali(an)?)\b',                                      6, "Mali"),
    (r'\b(Mozambique[an]?)\b',                                6, "Mozambique"),
]


def infer_icrv(title: str, journal: str) -> tuple[str, str]:
    """Returns (icrv_code, reason) or ('', '') if not inferrable."""
    text = f"{title} {journal}".strip()

    # Check multi-country first → ICRV = 0
    for pat in MULTI_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return "0", f"multi:{pat[:30]}"

    # Single country check
    hits = []
    for pat, code, label in COUNTRY_ICRV:
        if re.search(pat, text, re.IGNORECASE):
            hits.append((code, label))

    if len(hits) == 0:
        return "", ""
    if len(hits) == 1:
        return str(hits[0][0]), f"title_inferred:{hits[0][1]}"
    # Multiple countries → multi
    labels = "+".join(h[1] for h in hits)
    return "0", f"multi_inferred:{labels}"


def main():
    path = Path(TRACKER)
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cols = list(rows[0].keys())

    has_icrv_inferred = "icrv_inferred" in cols

    log_rows = []
    counts = {"I_fix": 0, "dpl_fill": 0, "icrv_title": 0, "icrv_multi": 0, "no_change": 0}

    for row in rows:
        dec = row.get("fulltext_screening_decision", "").strip()
        if dec != "Y":
            continue

        changed = []
        icrv = row.get("icrv", "").strip()
        dpl  = row.get("dpl", "").strip()
        yr   = row.get("year", "").strip()

        # 1. Fix "I" artifact → "3" (India = Emerging)
        if icrv == "I":
            row["icrv"] = "3"
            changed.append("I→3(India)")
            counts["I_fix"] += 1
            icrv = "3"

        # 2. Fill blank DPL from year
        if not dpl and yr:
            new_dpl = dpl_from_year(yr)
            if new_dpl:
                row["dpl"] = new_dpl
                changed.append(f"dpl←{new_dpl}(yr={yr})")
                counts["dpl_fill"] += 1

        # 3. Infer ICRV from title/journal for blank rows
        if not icrv:
            title   = row.get("title", "")
            journal = row.get("journal", "")
            new_icrv, reason = infer_icrv(title, journal)
            if new_icrv:
                row["icrv"] = new_icrv
                if has_icrv_inferred:
                    row["icrv_inferred"] = "1"
                changed.append(f"icrv←{new_icrv}({reason})")
                if new_icrv == "0":
                    counts["icrv_multi"] += 1
                else:
                    counts["icrv_title"] += 1

        if changed:
            log_rows.append({
                "seq":     row.get("seq", ""),
                "title":   row.get("title", "")[:70],
                "changes": "; ".join(changed),
            })
        else:
            counts["no_change"] += 1

    print(f"=== ICRV / DPL GAP FILL ===")
    print(f"  I→3 (India fix):         {counts['I_fix']}")
    print(f"  DPL filled from year:    {counts['dpl_fill']}")
    print(f"  ICRV from title (non-0): {counts['icrv_title']}")
    print(f"  ICRV→0 (multi inferred): {counts['icrv_multi']}")
    print(f"  No change:               {counts['no_change']}")

    # Atomic write
    tmp = str(path) + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, str(path))
    print(f"  Tracker updated: {path}")

    # Log
    with open(LOG_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["seq", "title", "changes"])
        w.writeheader()
        w.writerows(log_rows)
    print(f"  Log: {LOG_OUT}")


if __name__ == "__main__":
    main()
