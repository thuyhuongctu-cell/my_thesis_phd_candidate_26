#!/usr/bin/env python3
"""
44_auto_screen_l2_titles.py — Automated L2 pre-screening for 1,526 blank tracker rows

Uses title (+ abstract where available from abstracts_20260520.csv) to flag:
  - N (EXCLUDE): meta-analyses / reviews / bibliometrics of I→P; wrong-field papers;
                 country-level-only; qualitative; antecedent-direction studies
  - Y (tentative INCLUDE): firm-level I→P with quantitative language in abstract
  - UNSURE: everything else (default — conservative)

IMPORTANT: Auto-N decisions should still be spot-checked (10% sample).
Auto-Y decisions still require human confirmation before ready_for_r=1.

Usage:
  python3 p6/tools/44_auto_screen_l2_titles.py
  python3 p6/tools/44_auto_screen_l2_titles.py --dry-run
  python3 p6/tools/44_auto_screen_l2_titles.py --min-confidence 0.85
"""
import csv, re, argparse, sys
from pathlib import Path
from datetime import date
from collections import Counter

DEFAULT_TRACKER   = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
DEFAULT_ABSTRACTS = "p6/tools/results/abstracts_20260520.csv"
DEFAULT_LOG       = f"p6/tools/results/auto_screen_l2_log_{date.today().strftime('%Y%m%d')}.csv"

# ── Patterns: clear EXCLUDE ──────────────────────────────────────────────────

EXCLUDE_TITLE = [
    # Reviews / meta-analyses
    (r'\bmeta.anal', "meta-analysis_paper"),
    (r'\bsystematic.review\b', "systematic_review"),
    (r'\bliterature.review\b', "literature_review"),
    (r'\bbibliometric', "bibliometric"),
    (r'\bscoping.review\b', "scoping_review"),
    # Country-level / macro
    (r'\bcountry.level\s+(FDI|investment|analysis|study)', "country_level_macro"),
    (r'\bnational.level\b.{0,40}(performance|growth)', "national_level"),
    (r'\bmacroeconomic\b', "macroeconomic"),
    # Wrong field
    (r'\b(hospital|patient|clinical|health.care|medical.device|pharmaceutical)\b', "health_field"),
    (r'\bcarbon.emission|greenhouse.gas|air.pollution\b', "environment_emissions"),
    # Wrong direction
    (r'\bdeterminant.{0,10}(export|internationali)', "antecedent_direction"),
    (r'\bantecedent.{0,10}internationali', "antecedent_direction"),
    (r'\bpredictors?.{0,15}internationali', "antecedent_direction"),
    (r'\bdrivers?.{0,15}internationali(zation|sation)\b(?!.*performance)', "antecedent_direction"),
    # Simulation / non-empirical
    (r'\bagent.based.model|\bsimulation.stud', "computational_simulation"),
    # Conference proceeding / book chapter indicators in title
    (r'\bconference.proceedings?\b|\bworking.paper\b', "non_journal"),
]

EXCLUDE_ABSTRACT = [
    # Explicit review/synthesis statements
    (r'\bwe (review|synthesize|analyse|survey) (the |existing |prior )(literature|studies|research)', "review_statement"),
    (r'\bthis (paper|study|article) (reviews?|synthesizes?|surveys?|provides a review)', "review_statement"),
    # Qualitative methods
    (r'\b(case study|grounded theory|ethnograph|discourse analysis|thematic analysis)\b', "qualitative_method"),
    (r'\b(semi.structured interview|in.depth interview|focus group)\b', "qualitative_method"),
    # Wrong-direction explicit
    (r'\bwhat (drives?|predicts?|determines?) internationali', "antecedent_direction"),
    (r'\bantecedents? of (firm )?internationali', "antecedent_direction"),
    # Macro/country-level explicit
    (r'\bour (sample|analysis) (covers?|includes?) (\d+ )?countries\b(?!.*firm)', "macro_country"),
    (r'\bcountry.level (data|sample|panel)\b(?!.*firm.level)', "macro_country"),
]

# ── Patterns: tentative INCLUDE (only with abstract evidence) ────────────────

INCLUDE_ABSTRACT = [
    # Firm-level + quantitative + I→P
    (r'\b(OLS|panel (data|regression)|fixed.effects?|random.effects?|GMM|2SLS|IV)\b', "quantitative_method"),
    (r'\b(regression|coefficient|correlation|R-squared|robust)\b', "quantitative_stat"),
    (r'\b(ROA|ROE|ROS|Tobin.s Q|firm performance|financial performance|profitability)\b', "ip_performance"),
    (r'\b(FSTS|foreign sales|export intensity|degree of internationali|multinationality)\b', "ip_internationaliz"),
]

INCLUDE_TITLE = [
    # Very explicit I→P relationship in title — must be FINANCIAL performance, not environmental
    (r'internationali[sz]ation.{1,30}(firm|financial|corporate|business).{0,15}performance', "ip_explicit"),
    (r'(firm|financial|corporate).{0,15}performance.{1,30}internationali[sz]ation', "ip_explicit"),
    (r'\b(export|multinational).{1,30}(profitability|ROA|ROE|Tobin|sales growth)', "ip_explicit"),
    (r'(internationali[sz]ation|multinationality) and (firm|corporate|financial) performance', "ip_explicit"),
    (r'(FSTS|foreign sales|export intensity).{1,40}(performance|profitability|ROA)', "ip_explicit"),
]

# Phrases in title that override auto-Y (environmental/social performance ≠ financial)
OVERRIDE_Y_TO_UNSURE_TITLE = [
    r'environmental performance',
    r'social performance',
    r'sustainability performance',
    r'CSR performance',
    r'ESG performance',
]


def check_patterns(text: str, patterns: list) -> tuple[bool, str]:
    t = text.lower()
    for pattern, reason in patterns:
        if re.search(pattern, t, re.IGNORECASE):
            return True, reason
    return False, ""


def auto_screen(row: dict, abstract: str) -> tuple[str, str]:
    title = row.get("title", "")
    text = title + " " + abstract

    # 1. Check EXCLUDE patterns on title
    hit, reason = check_patterns(title, EXCLUDE_TITLE)
    if hit:
        return "N", f"auto_title:{reason}"

    # 2. Check EXCLUDE patterns on abstract (if available)
    if abstract.strip():
        hit, reason = check_patterns(abstract, EXCLUDE_ABSTRACT)
        if hit:
            return "N", f"auto_abstract:{reason}"

    # 3. Check tentative INCLUDE (only when abstract available)
    if abstract.strip():
        include_signals = []
        for pattern, reason in INCLUDE_ABSTRACT:
            if re.search(pattern, abstract, re.IGNORECASE):
                include_signals.append(reason)
        if len(include_signals) >= 2:
            return "Y", f"auto_abstract:{','.join(include_signals[:3])}"

    # 4. Check title-only include (very explicit titles)
    hit, reason = check_patterns(title, INCLUDE_TITLE)
    if hit:
        # Override if title signals non-financial performance
        for pat in OVERRIDE_Y_TO_UNSURE_TITLE:
            if re.search(pat, title, re.IGNORECASE):
                return "UNSURE", "auto_title:non_financial_performance"
        return "Y", f"auto_title:{reason}"

    return "UNSURE", "auto:insufficient_evidence"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracker",   default=DEFAULT_TRACKER)
    parser.add_argument("--abstracts", default=DEFAULT_ABSTRACTS)
    parser.add_argument("--log",       default=DEFAULT_LOG)
    parser.add_argument("--dry-run",   action="store_true")
    args = parser.parse_args()

    # Load abstracts index
    abs_map = {}
    if Path(args.abstracts).exists():
        with open(args.abstracts, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("abstract", "").strip():
                    abs_map[r["seq"]] = r["abstract"].strip()
    print(f"Abstracts loaded: {len(abs_map)}", flush=True)

    # Load tracker
    with open(args.tracker, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())

    # Only process blank rows
    blank = [r for r in rows if not r.get("fulltext_screening_decision", "").strip()]
    print(f"Blank rows to process: {len(blank)}", flush=True)

    decisions = Counter()
    log_rows = []

    for row in blank:
        abstract = abs_map.get(row["seq"], "")
        decision, reason = auto_screen(row, abstract)

        log_rows.append({
            "seq":        row["seq"],
            "title":      row.get("title", "")[:80],
            "decision":   decision,
            "reason":     reason,
            "has_abstract": "Y" if abstract else "N",
        })
        decisions[decision] += 1

        if not args.dry_run:
            row["fulltext_screening_decision"] = decision
            row["exclusion_reason"] = reason if decision == "N" else row.get("exclusion_reason", "")
            row["prescreen_reason"] = reason

    print(f"\n=== AUTO-SCREEN L2 RESULTS ===")
    print(f"N (auto-exclude):  {decisions['N']}")
    print(f"Y (auto-include):  {decisions['Y']}")
    print(f"UNSURE (default):  {decisions['UNSURE']}")
    print(f"Total processed:   {len(blank)}")
    print(f"Abstracts enriched: {sum(1 for l in log_rows if l['has_abstract']=='Y')}")

    if args.dry_run:
        print("\n[DRY RUN] No files modified.")
        print("Sample N rows:")
        for r in [l for l in log_rows if l["decision"] == "N"][:5]:
            print(f"  seq={r['seq']}: {r['title'][:60]} | {r['reason']}")
        print("Sample Y rows:")
        for r in [l for l in log_rows if l["decision"] == "Y"][:5]:
            print(f"  seq={r['seq']}: {r['title'][:60]} | {r['reason']}")
        return

    # Write updated tracker
    with open(args.tracker, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    # Write log
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)
    with open(args.log, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["seq", "title", "decision", "reason", "has_abstract"])
        w.writeheader()
        w.writerows(log_rows)

    print(f"\nTracker updated: {args.tracker}")
    print(f"Log written:     {args.log}")
    print(f"\nNEXT:")
    print(f"  1. Review auto-N rows (spot-check ~10%): p6/tools/results/auto_screen_l2_log_*.csv")
    print(f"  2. Review auto-Y rows for false positives")
    print(f"  3. UNSURE rows still need manual full-text judgment")


if __name__ == "__main__":
    main()
