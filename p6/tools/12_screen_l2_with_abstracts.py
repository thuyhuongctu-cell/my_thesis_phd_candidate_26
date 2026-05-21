#!/usr/bin/env python3
"""
12_screen_l2_with_abstracts.py
Apply L2 eligibility criteria to worklist records that have abstracts.
Outputs: screen_l2 = Y / N / UNSURE-FULLTEXT-NEEDED for each record.

L2 criteria (from p6/p6_wos_search_guide.md and p6/tools/p6_extraction_codebook.md):
  INCLUDE (Y):
    - Unit of analysis: firm-level (not country/industry/macro)
    - Reports quantitative I→P relationship (r, β, t, F, or convertible)
    - Internationalization → performance direction is causal claim or association
  EXCLUDE (N):
    - Country-level / macro / industry-level analysis
    - Qualitative, conceptual, or review-only
    - Health, environmental, psychology journals (non-IB)
    - No quantitative I→P data
    - Book chapter, dissertation (not peer-reviewed journal)
    - DV is antecedent of internationalization, not performance
    - EO (entrepreneurial orientation) as focal DV
    - Born-global dynamics/antecedents as focal DV
  UNSURE-FULLTEXT-NEEDED: abstract present but ambiguous on unit or stats

Usage:
    python3 p6/tools/12_screen_l2_with_abstracts.py \
        --input  p6/tools/results/worklist_with_abstracts_YYYYMMDD.csv \
        --output p6/tools/results/l2_screened_YYYYMMDD.csv
"""

import csv
import re
import argparse
from datetime import datetime
from pathlib import Path

# Hard exclude signals in abstract text (case-insensitive)
HARD_EXCL = [
    r"\bcountry.level\b", r"\bcross.country\b", r"\bnational.level\b",
    r"\bindustry.level\b", r"\bsector.level\b", r"\bmacro.level\b",
    r"\bqualitative\b", r"\bconceptual paper\b", r"\bconceptual framework\b",
    r"\bsystematic review\b", r"\bmeta.analysis\b", r"\bliterature review\b",
    r"\bhealth\b.*\bpatient\b", r"\bmedical\b", r"\bclinical trial\b",
    r"\bpsycholog\b", r"\bnurse\b", r"\bphysician\b",
    r"\bantecedents of export\b", r"\bdeterminants of export\b",
    r"\bdeterminants of internationali\b", r"\bwhat drives.*export\b",
    r"\bexport participation decision\b", r"\bexport entry\b",
    r"\bborn global.*antecedent\b", r"\bborn global.*determinant\b",
    r"\bentrepreneurial orientation.*dv\b",
    r"\bsurvival analysis\b.*\bfirm exit\b",
    r"\bknowledge spillover\b.*\bdomestic firm\b",
    r"\bM&A.*performance.*acquirer.*domestic\b",
    r"\binnovation as dependent\b", r"\binnovation output.*dv\b",
]

# Strong include signals (any of these + absence of hard excl → likely Y)
STRONG_INCL = [
    r"\bexport intensity\b.*\bperformance\b",
    r"\bfirm performance\b.*\binternationali\b",
    r"\binternationali\b.*\bfirm performance\b",
    r"\bFSTS\b", r"\bforeign sales.*total sales\b",
    r"\bdegree of internationali\b",
    r"\bU.shaped\b.*\bperformance\b",
    r"\binverted.U\b.*\bperformance\b",
    r"\bexport.performance relationship\b",
    r"\bROA\b.*\binternationali\b", r"\binternationali\b.*\bROA\b",
    r"\bTobin.*Q\b.*\binternationali\b",
    r"\bfirm.level.*panel\b.*\bexport\b",
    r"\bperformance consequences.*international\b",
    r"\bproductivity.*export\b", r"\bexport.*productivity\b",
    r"\blabor productivity\b.*\binternational\b",
    r"\bturnover.*export\b.*\bSME\b",
]

# Unit of analysis signals for firm-level confirmation
FIRM_LEVEL = [
    r"\bfirm.level\b", r"\bfirm data\b", r"\bpanel of firms\b",
    r"\bsurvey of firm\b", r"\bfirm survey\b", r"\bWBES\b",
    r"\bWorld Bank.*Enterprise Survey\b", r"\bSME\b", r"\bMNE\b",
    r"\bmanufacturing firm\b", r"\bexporting firm\b", r"\bpanel.*firms\b",
    r"\bfirms in\b", r"\bsample of firms\b", r"\bn\s*=\s*\d{2,}\b.*firm",
]


def classify_abstract(title: str, abstract: str) -> tuple:
    """Returns (decision, reason)."""
    combined = (title + " " + abstract).lower()

    # Hard exclude
    for pattern in HARD_EXCL:
        if re.search(pattern, combined, re.IGNORECASE):
            return "N", "HARD_EXCL:" + pattern[:40]

    if not abstract or len(abstract.strip()) < 50:
        return "UNSURE-FULLTEXT-NEEDED", "NO_ABSTRACT"

    # Strong include check
    has_incl = any(re.search(p, combined, re.IGNORECASE) for p in STRONG_INCL)
    has_firm = any(re.search(p, combined, re.IGNORECASE) for p in FIRM_LEVEL)

    if has_incl and has_firm:
        return "Y", "STRONG_INCL+FIRM_LEVEL"
    if has_incl:
        return "Y", "STRONG_INCL (firm level ambiguous)"
    if has_firm:
        return "UNSURE-FULLTEXT-NEEDED", "FIRM_LEVEL_OK but I→P signal weak"

    return "UNSURE-FULLTEXT-NEEDED", "INSUFFICIENT_SIGNAL"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",  required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = list(rows[0].keys()) if rows else []
    for col in ["screen_l2", "screen_l2_reason"]:
        if col not in fieldnames:
            fieldnames.append(col)

    counts = {"Y": 0, "N": 0, "UNSURE-FULLTEXT-NEEDED": 0, "SKIP": 0}

    for row in rows:
        existing = row.get("screen_l2", "").strip()
        # Don't overwrite already-decided records
        if existing and existing not in ("", "UNSURE"):
            counts["SKIP"] += 1
            continue

        title    = row.get("title", "")
        abstract = row.get("abstract", "")
        decision, reason = classify_abstract(title, abstract)

        row["screen_l2"]        = decision
        row["screen_l2_reason"] = reason
        counts[decision] += 1

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("=== L2 Screening Summary ===")
    print("Y (include)              : %d" % counts["Y"])
    print("N (exclude)              : %d" % counts["N"])
    print("UNSURE-FULLTEXT-NEEDED   : %d" % counts["UNSURE-FULLTEXT-NEEDED"])
    print("Skipped (already decided): %d" % counts["SKIP"])
    print("Output: %s" % out_path)


if __name__ == "__main__":
    main()
