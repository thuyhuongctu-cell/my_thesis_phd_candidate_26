#!/usr/bin/env python3
"""
04b_screen_l1_title.py — Title-based L1 screener for P6 meta-analysis.

WoS Starter API returns no abstracts, so this script screens on title alone
using keyword rules calibrated for internationalization→performance research.

Decision logic (per title, case-insensitive):
  EXCLUDE (N)  → title matches any hard-exclude pattern
  INCLUDE (Y)  → title matches ≥1 I→P signal AND ≥1 firm-level signal
  UNSURE       → everything else (advances to full-text review)

Usage:
  python3 04b_screen_l1_title.py \
      --input  p6/tools/results/l1_screening_20260518.csv \
      --output p6/tools/results/l1_title_20260518.csv
"""

import argparse
import csv
import re
import sys
from datetime import datetime
from pathlib import Path

# ── Exclusion patterns (any match → N) ─────────────────────────────────────
EXCLUDE_PATTERNS = [
    # Study-type exclusions
    r"\bmeta.anal",          r"\bsystematic review\b",   r"\bliterature review\b",
    r"\bbibliometric\b",     r"\bscoping review\b",       r"\bevidence synthesis\b",
    r"\beditorial\b",        r"\bbook review\b",          r"\bcommentary\b",
    r"\bconceptual\b",       r"\btheoretical framework\b",r"\bthought experiment\b",

    # Country/macro-level outcomes (not firm-level performance)
    r"\bnational competitiveness\b", r"\bcountry.level\b",
    r"\bgdp\b",              r"\bgross domestic\b",       r"\bmacroeconomic\b",
    r"\bnational economy\b", r"\bbalance of (payments|trade)\b",
    r"\bcurrent account\b",  r"\btrade balance\b",

    # Health / non-business fields
    r"\bclinical\b",         r"\bpatient\b",              r"\bmedical\b",
    r"\bhospital\b",         r"\bhealth(care)?\b",        r"\bepidemi\b",
    r"\bpublic health\b",    r"\bnursing\b",              r"\bpsychiatry\b",

    # Non-firm public-sector
    r"\bgovernment polic\b", r"\bpublic sector\b",        r"\bngo\b",
    r"\bnot.for.profit\b",

    # Pure economics / irrelevant topic
    r"\breal exchange rate\b",r"\bmonetary policy\b",     r"\binflation\b",
    r"\belectoral\b",         r"\bpolitical party\b",
]

# ── I→P signal patterns (need ≥1) ──────────────────────────────────────────
IP_SIGNAL = [
    r"\binternational[is]", r"\binternationali[sz]ation\b",
    r"\bmultinational",      r"\bmulti.national",
    r"\bexport(ing|er|s)?\b",r"\bexport.intensi",        r"\bexport performance\b",
    r"\bfsts\b",             r"\bforeign sales\b",
    r"\bfdi\b",              r"\bforeign direct invest",
    r"\bglobaliz",           r"\bglobali[sz]ation\b",
    r"\bcross.border",       r"\boffshoring\b",           r"\boutward fdi\b",
    r"\binward fdi\b",       r"\bmne\b",                  r"\bmnc\b",
    r"\bdegree of internation",r"\bdoi\b",
    r"\bborn.global\b",      r"\bearly internation",
]

# ── Performance/outcome signal patterns (need ≥1) ──────────────────────────
PERF_SIGNAL = [
    r"\bperformance\b",      r"\bprofitabilit",           r"\bproductivit",
    r"\bfinancial performance\b",r"\bfirm performance\b", r"\bcompetitiveness\b",
    r"\breturn on (asset|equity|invest|sales)",            r"\broa\b",r"\broe\b",
    r"\btobin",              r"\bmarket value\b",         r"\bsurvival\b",
    r"\bgrowth\b",           r"\brevenue\b",              r"\bsales performance\b",
    r"\beconomic performance\b",r"\boperating performance\b",
    r"\binnovation (performance|output)\b",
    r"\brisk.return\b",      r"\bvalue creation\b",       r"\bshareholder value\b",
    r"\befficienc",          r"\bprofit(s|ability)?\b",   r"\bearning",
]

# ── Firm-level signal (need ≥1) ─────────────────────────────────────────────
FIRM_SIGNAL = [
    r"\bfirm\b",             r"\benterprise\b",           r"\bcompan",
    r"\bcorporat",           r"\bsme\b",                  r"\bsmall.medium",
    r"\bmanufactur",         r"\bindustr",                r"\bsubsidiar",
    r"\bmanager",            r"\borganiz",                r"\bbusiness",
    r"\bventure\b",          r"\bstart.?up\b",            r"\binvestor\b",
    r"\bstrateg",
]

EXCLUDE_RE  = [re.compile(p, re.IGNORECASE) for p in EXCLUDE_PATTERNS]
IP_RE       = [re.compile(p, re.IGNORECASE) for p in IP_SIGNAL]
PERF_RE     = [re.compile(p, re.IGNORECASE) for p in PERF_SIGNAL]
FIRM_RE     = [re.compile(p, re.IGNORECASE) for p in FIRM_SIGNAL]


def screen_title(title: str) -> tuple[str, str]:
    t = title or ""

    # 1. Hard excludes
    for rx in EXCLUDE_RE:
        if rx.search(t):
            return "N", rx.pattern.replace(r"\b", "").strip()

    has_ip   = any(rx.search(t) for rx in IP_RE)
    has_perf = any(rx.search(t) for rx in PERF_RE)
    has_firm = any(rx.search(t) for rx in FIRM_RE)

    # 2. Clear include: I signal + performance signal (firm implied by context)
    if has_ip and has_perf:
        return "Y", "ip_perf_match"

    # 3. I signal + firm signal (performance inferred from context)
    if has_ip and has_firm:
        return "Y", "ip_firm_match"

    # 4. Anything else → UNSURE for manual review
    return "UNSURE", "title_insufficient"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    in_path  = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with open(in_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    counts = {"Y": 0, "N": 0, "UNSURE": 0}
    reasons = {}

    for row in rows:
        # Only re-screen UNSURE rows; keep already-decided rows
        if row.get("screen_l1") in ("Y", "N"):
            counts[row["screen_l1"]] += 1
            continue

        decision, reason = screen_title(row.get("title", ""))
        row["screen_l1"]        = decision
        row["screen_l1_reason"] = reason
        counts[decision] += 1
        reasons[reason]  = reasons.get(reason, 0) + 1

    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    total = sum(counts.values())
    print(f"L1 title-screening — {in_path.name}")
    print(f"  Total records : {total:,}")
    print(f"  INCLUDE  (Y)  : {counts['Y']:,}  ({counts['Y']/total*100:.1f}%)")
    print(f"  EXCLUDE  (N)  : {counts['N']:,}  ({counts['N']/total*100:.1f}%)")
    print(f"  UNSURE        : {counts['UNSURE']:,}  ({counts['UNSURE']/total*100:.1f}%)")
    print(f"\nNew exclusion reasons (title-based):")
    for r, n in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f"  {r:40s}: {n:,}")
    print(f"\nOutput: {out_path}")


if __name__ == "__main__":
    main()
