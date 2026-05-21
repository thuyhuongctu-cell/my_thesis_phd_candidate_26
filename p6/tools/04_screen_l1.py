#!/usr/bin/env python3
"""
04_screen_l1.py — Automated Level-1 (title + abstract) screening for P6 meta-analysis.

L1 inclusion/exclusion criteria (from p6/p6_wos_search_guide.md):

EXCLUDE if any of:
  not_IP       — does not examine internationalization → firm performance relationship
  not_firm     — country-level, industry-level, or macro analysis (not firm-level)
  qualitative  — purely qualitative or conceptual (no quantitative relationship)
  meta         — is itself a meta-analysis or systematic review (not primary study)
  language     — non-English title/abstract detected
  non_peer     — dissertation, working paper, conference proceeding, book chapter,
                 institutional report (not peer-reviewed journal article)

INCLUDE if clearly:
  - Examines DOI → performance at firm level
  - Reports quantitative relationship (r, β, regression)

UNSURE when insufficient information from title + abstract alone.
  → Researcher reviews manually.

Output columns match p6/p6_wos_screening_template.csv:
  study_id, wos_id, authors, year, title, journal, doi,
  n_sample, country, screen_l1, screen_l1_reason,
  screen_l2, screen_l2_reason, eligible,
  doi_measure, fp_measure, r_reported, n_used, notes

Usage:
  python3 04_screen_l1.py --input results/merged_unique_20260517.csv
  python3 04_screen_l1.py --input results/merged_unique_20260517.csv \\
      --output results/l1_screening_20260517.csv
"""

import argparse
import csv
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Keyword lists for heuristic L1 screening
# ---------------------------------------------------------------------------

# Signals that the paper is NOT about internationalization → firm performance
EXCLUDE_NOT_IP = [
    r"\bforeign direct investment inflow",
    r"\bfdi inflow",
    r"\bhost country",
    r"\bnational competitiveness",
    r"\bregional integration",
    r"\bgravity model",
    r"\btrade flow",
    r"\bbalance of payment",
    r"\bexchange rate",
    r"\btariff",
]

# Signals country/macro level (not firm)
EXCLUDE_NOT_FIRM = [
    r"\bcountry[\s-]level",
    r"\bnational[\s-]level",
    r"\bregional[\s-]level",
    r"\bindustry[\s-]level",
    r"\bsector[\s-]level",
    r"\bmacro[\s-]level",
    r"\bgdp\b",
    r"\bgross domestic product",
    r"\bnation(?:al)? performance",
    r"\bcross[\s-]country analysis",
]

# Signals qualitative / conceptual
EXCLUDE_QUALITATIVE = [
    r"\bqualitative study",
    r"\bcase study approach",
    r"\bconceptual framework",
    r"\bconceptual paper",
    r"\bconceptual model\b",
    r"\bgrounded theory",
    r"\binterviews?\b.*\bonly\b",
    r"\bno quantitative",
    r"\btheoretical paper",
    r"\btheoretical framework\b.*\bproposed\b",
]

# Signals meta-analysis / systematic review
EXCLUDE_META = [
    r"\bmeta[\s-]analys",
    r"\bsystematic review",
    r"\bliterature review\b",
    r"\bbibliometric",
    r"\bscoping review",
    r"\bnarrative review",
]

# Non-English signals in title/abstract
EXCLUDE_LANGUAGE = [
    r"[àáâãäåæçèéêëìíîïðñòóôõöùúûüýþÿ]{3,}",   # accented clusters
    r"\b(?:dans|avec|pour|une|les|des|sur|par)\b",  # French
    r"\b(?:und|der|die|das|für|mit|von|bei)\b",     # German
    r"\b(?:und|oder|auch|wird|sind)\b",
    r"\b(?:del|los|las|para|como|por|una)\b",        # Spanish
    r"\b(?:nella|delle|degli|questo|questa)\b",      # Italian
]

# Signals non-peer-reviewed document types
EXCLUDE_NON_PEER = [
    r"\bworking paper\b",
    r"\bdiscussion paper\b",
    r"\bpreprint\b",
    r"\bdissertation\b",
    r"\bthesis\b",
    r"\bconference proceedings?\b",
    r"\bbook chapter\b",
    r"\binstitutional report\b",
    r"\btechnical report\b",
]

# Positive signals for inclusion
INCLUDE_DOI = [
    r"\binternational(?:iz|is)ation\b",
    r"\bforeign sales\b",
    r"\bexport int(?:en)?sit",
    r"\bFSTS\b",
    r"\bFATA\b",
    r"\bdegree of internationaliz",
    r"\bDOI\b.*\bperformance\b",
    r"\bmultinational",
    r"\bexport performance\b",
    r"\bexport propensit",
    r"\bgeographic diversif",
]

INCLUDE_FP = [
    r"\bfirm performance\b",
    r"\bfinancial performance\b",
    r"\bROA\b",
    r"\bROE\b",
    r"\bTobin.s Q\b",
    r"\bROS\b",
    r"\blabour productivity\b",
    r"\bproductivity\b",
    r"\bprofitab",
    r"\bsales growth\b",
]

INCLUDE_FIRM = [
    r"\bfirm[\s-]level\b",
    r"\benterprise[\s-]level\b",
    r"\bcompany[\s-]level\b",
    r"\bSME\b",
    r"\bsmall and medium",
    r"\bmanufacturing firm",
    r"\bexporting firm",
    r"\bMNE\b",
    r"\bMNC\b",
]

INCLUDE_QUANT = [
    r"\bregression\b",
    r"\bOLS\b",
    r"\bGMM\b",
    r"\bfixed effect",
    r"\bpanel data\b",
    r"\bpearson\b",
    r"\bcorrelation\b",
    r"\bcoefficient\b",
    r"\bquantitative\b",
]


def _any_match(patterns: list[str], text: str) -> bool:
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def screen_record(rec: dict) -> tuple[str, str]:
    """
    Returns (decision, reason) where decision ∈ {Y, N, UNSURE}.
    Reason is one of the exclusion codes or 'pass_l1'.
    """
    title = rec.get("title", "")
    abstract = rec.get("abstract", "")
    journal = rec.get("journal", "")
    combined = f"{title} {abstract}"
    combined_lower = combined.lower()

    # --- Hard exclusions (applied to title + abstract + journal) ---

    # Non-peer-reviewed
    full_text = f"{title} {abstract} {journal}"
    if _any_match(EXCLUDE_NON_PEER, full_text):
        return "N", "non_peer"

    # Meta-analysis / systematic review
    if _any_match(EXCLUDE_META, combined):
        return "N", "meta"

    # Qualitative / conceptual
    if _any_match(EXCLUDE_QUALITATIVE, combined):
        return "N", "qualitative"

    # Country/macro level
    if _any_match(EXCLUDE_NOT_FIRM, combined):
        # If strong firm-level signals override, move to UNSURE rather than exclude
        if _any_match(INCLUDE_FIRM, combined):
            return "UNSURE", "possible_not_firm"
        return "N", "not_firm"

    # Not about I→P (only exclude if abstract is non-empty; otherwise UNSURE)
    if abstract and _any_match(EXCLUDE_NOT_IP, combined):
        if not _any_match(INCLUDE_DOI, combined):
            return "N", "not_IP"

    # Language check (only if abstract present and long enough)
    if len(abstract) > 50 and _any_match(EXCLUDE_LANGUAGE, combined):
        return "N", "language"

    # --- Positive inclusion signals ---
    has_doi_signal = _any_match(INCLUDE_DOI, combined)
    has_fp_signal = _any_match(INCLUDE_FP, combined)
    has_firm_signal = _any_match(INCLUDE_FIRM, combined)
    has_quant_signal = _any_match(INCLUDE_QUANT, combined)

    # If abstract is empty: always UNSURE (insufficient info)
    if not abstract.strip():
        return "UNSURE", "no_abstract"

    # Clear include: DOI + FP + quantitative method
    if has_doi_signal and has_fp_signal and has_quant_signal:
        return "Y", "pass_l1"

    # Partial match: DOI + FP but no explicit method mention
    if has_doi_signal and has_fp_signal:
        return "UNSURE", "needs_fulltext_method_check"

    # DOI signal only
    if has_doi_signal:
        return "UNSURE", "needs_fulltext_fp_check"

    # No DOI signal at all
    return "UNSURE", "needs_fulltext_doi_check"


def load_csv(filepath: Path) -> tuple[list[dict], list[str]]:
    with open(filepath, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    return rows, fieldnames


def write_screening_csv(rows: list[dict], output_path: Path) -> None:
    """Write output in the same column format as p6_wos_screening_template.csv."""
    columns = [
        "study_id", "wos_id", "authors", "year", "title", "journal", "doi",
        "n_sample", "country",
        "screen_l1", "screen_l1_reason",
        "screen_l2", "screen_l2_reason",
        "eligible", "doi_measure", "fp_measure", "r_reported", "n_used", "notes",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="L1 title+abstract screening for P6 systematic review."
    )
    parser.add_argument(
        "--input", required=True,
        help="merged_unique CSV from 03_deduplicate_merge.py"
    )
    parser.add_argument(
        "--output", default="",
        help="Output CSV path (default: results/l1_screening_YYYYMMDD.csv)"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = Path(args.output)
    else:
        datestamp = datetime.today().strftime("%Y%m%d")
        output_path = Path(__file__).parent / "results" / f"l1_screening_{datestamp}.csv"

    records, _ = load_csv(input_path)

    out_rows = []
    counts: dict[str, int] = {"Y": 0, "N": 0, "UNSURE": 0}
    reasons: dict[str, int] = {}

    for i, rec in enumerate(records, start=1):
        decision, reason = screen_record(rec)
        counts[decision] += 1
        reasons[reason] = reasons.get(reason, 0) + 1

        row: dict = {
            "study_id": f"S{i:04d}",
            "wos_id": rec.get("source_id", ""),
            "authors": rec.get("authors", ""),
            "year": rec.get("year", ""),
            "title": rec.get("title", ""),
            "journal": rec.get("journal", ""),
            "doi": rec.get("doi", ""),
            "n_sample": "",
            "country": "",
            "screen_l1": decision,
            "screen_l1_reason": reason,
            "screen_l2": "",
            "screen_l2_reason": "",
            "eligible": "",
            "doi_measure": "",
            "fp_measure": "",
            "r_reported": "",
            "n_used": "",
            "notes": rec.get("source", ""),  # preserve source label
        }
        out_rows.append(row)

    write_screening_csv(out_rows, output_path)

    # Summary
    n_total = len(records)
    print(f"\nL1 Screening summary ({input_path.name}):")
    print(f"  Total screened : {n_total}")
    print(f"  INCLUDE (Y)    : {counts['Y']:>5}  ({100*counts['Y']/max(n_total,1):.1f}%)")
    print(f"  EXCLUDE (N)    : {counts['N']:>5}  ({100*counts['N']/max(n_total,1):.1f}%)")
    print(f"  UNSURE         : {counts['UNSURE']:>5}  ({100*counts['UNSURE']/max(n_total,1):.1f}%)")
    print(f"\nExclusion reasons:")
    for reason, n in sorted(reasons.items(), key=lambda x: -x[1]):
        if reason != "pass_l1":
            print(f"  {reason:<40}: {n}")
    print(f"\nOutput written : {output_path}")
    print(
        f"\nNote: 'UNSURE' records require manual full-text review. "
        f"Do NOT rely on automated decisions alone for borderline cases."
    )


if __name__ == "__main__":
    main()
