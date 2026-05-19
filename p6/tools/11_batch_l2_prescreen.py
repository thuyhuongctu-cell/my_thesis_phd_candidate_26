#!/usr/bin/env python3
"""
11_batch_l2_prescreen.py — Batch L2 pre-screening assistant.

Reads the L2 extraction template and applies keyword rules to:
  1. Suggest include_flag (Y / N / UNSURE) with reason
  2. Pre-code icrv from country mentions in title/journal
  3. Pre-code doi_type from title keywords
  4. Pre-code fp_type from title keywords

This is a SUGGESTION ONLY — all decisions require human confirmation.
Saves meaningful time by pre-filling obvious cases.

Usage:
    python3 11_batch_l2_prescreen.py \
        --input  p6/tools/results/l2_extraction_template.csv \
        --output p6/tools/results/l2_prescreened.csv

    # Process only rows without existing include_flag:
    python3 11_batch_l2_prescreen.py --input l2_extraction_template.csv \
        --output l2_prescreened.csv --skip-coded

Columns added:
    prescreen_flag    — Y / N / UNSURE
    prescreen_reason  — pipe-separated list of rules triggered
    prescreen_icrv    — suggested icrv code (1–6 or blank)
    prescreen_doi_type — suggested doi_type
    prescreen_fp_type  — suggested fp_type
"""

import argparse
import csv
import re
import sys
from pathlib import Path


# ── Exclusion keyword rules ───────────────────────────────────────────────────
# (regex pattern, label, weight)
EXCLUDE_RULES = [
    (r"\breview\b.*\bmeta\b|\bmeta.analys",           "meta-analysis-paper",  3),
    (r"\bconceptual\b|\btheoretical\s+framework\b",    "conceptual-only",      3),
    (r"\bcase\s+stud",                                "case-study",           3),
    (r"\bqualitative\b|\bethnograph",                  "qualitative",          3),
    (r"\bbook\s+chapter\b|\bchapter\b",                "book-chapter",         3),
    (r"\bdissertation\b|\bthesis\b",                   "dissertation",         3),
    # Health/medical
    (r"\bhospital\b|\bclinic\b|\bmedical\b|\bhealth\s+care\b|\bpatient\b",
                                                       "health-domain",        3),
    # Pure macro
    (r"\bcountry.level\s+performance\b|\bnational\s+competitive",
                                                       "macro-level",          2),
    # Environment-only (no IB performance link)
    (r"\bcarbon\s+emission\b|\bco2\s+emission\b",      "emissions-focus",      2),
    # Sport / tourism (weak ICRV link)
    (r"\bsport\s+(?:club|organiz|team)\b",             "sport-sector",         2),
    # Wrong direction: capability/strategy → export performance as DV (NOT I→P)
    (r"(?:technolog|capabilit|resourc|knowledg|orientat|strateg|innovat|absorptiv"
     r"|human\s+capital|managerial|antecedent|determinant|driver|predictor)"
     r".*\bexport\s+performanc"
     r"|\bexport\s+performanc.*(?:technolog|capabilit|resourc|knowledg|orientat"
     r"|strateg|innovat|antecedent|determinant|driver|predictor|influenc)",
                                                       "wrong-dir-export-perf-DV", 3),
    # "Export performance" as DV in clear antecedent framing (not caught above)
    (r"(?:how|what)\b.{1,60}\bexport\s+performanc"           # How X impacts EP
     r"|\beffect\b.{1,40}\bexport\s+performanc"              # effect of X on EP
     r"|\bimpact\b.{1,40}\bexport\s+performanc"              # impact on EP
     r"|\bchallenge.{0,25}\bexport\s+performanc"             # challenges in EP
     r"|\bexport\s+performance\s+of\s+\b"                    # EP of firms/SMEs
     r"|\bapproach\b.{1,30}\bexport\s+performanc"            # approach to EP
     r"|\bexport\s+performance\b.*\bcase\s+of\b",            # EP: case of X
                                                       "antecedent-framing-export-perf", 3),
]

# ── Inclusion keyword rules ───────────────────────────────────────────────────
INCLUDE_RULES = [
    # Strong I measures
    (r"\bexport\s+intensit\b|\bexport\s+ratio\b|\bexport\s+propensit",
                                                       "export-intensity",     3),
    (r"\bfsts\b|\bforeign\s+sales\s+to\s+total",       "FSTS",                 3),
    (r"\binternationaliz|\binternationalis",            "internationalization", 3),
    (r"\bmultinational",                               "MNE",                  3),
    (r"\bforeign\s+direct\s+invest|\bfdi\b",           "FDI",                  3),
    (r"\bgeographic\s+diversif|\binternational\s+diversif",
                                                       "geo-diversification",  3),
    (r"\bdegree\s+of\s+internationaliz",               "DOI",                  3),
    (r"\bexport(?:er|ing)\b",                          "exporter",             2),
    (r"\bforeign\s+market\s+entr|\bentry\s+mode\b",    "entry-mode",           2),
    (r"\bforeign\s+subsidiari|\boffshoring\b",         "subsidiaries",         2),
    # Strong P measures in title
    (r"\bfirm\s+performance\b|\bcorporate\s+performance\b|\benterp.*perform",
                                                       "firm-performance",     3),
    (r"\bfinancial\s+performance\b|\bprofitabilit",    "financial-perf",       2),
    (r"\blabou?r\s+productivit|\btotal\s+factor\s+product|\btfp\b",
                                                       "productivity",         2),
    (r"\breturn\s+on\s+asset|\broa\b|\breturn\s+on\s+equit|\broe\b",
                                                       "ROA/ROE",              2),
    (r"\btobin.?s?\s+q\b|\bmarket\s+value\b",          "Tobin-Q",              2),
    (r"\bsales\s+growth\b|\brevenue\s+growth\b",       "sales-growth",         2),
    # Export-productivity / learning-by-exporting (valid I→P direction)
    (r"\b(?:export|internation).*\bproductivit|\bproductivit.*\b(?:export|internation)"
     r"|\blearning.by.export",
                                                       "export-productivity",   3),
]

# ── ICRV country/region patterns ─────────────────────────────────────────────
ICRV_PATTERNS = [
    # 1 — Advanced
    (1, r"\b(?:usa?|u\.s\.a?|united\s+states|american\s+firm|american\s+compan"
         r"|german|germany|japan(?:ese)?\b|australia|canada|france|uk\b|"
         r"united\s+kingdom|nether|norway|sweden|denmark|finland|austria|"
         r"switzerland|new\s+zealand|south\s+korea|korea(?:n)?\b|taiwan|"
         r"advanced\s+econom|developed\s+econom|oecd)"),
    # 2 — Emerging
    (2, r"\bchina|chinese|india(?:n)?\b|brazil(?:ian)?\b|russia(?:n)?\b|"
         r"turkey|turkish\b|mexico|mexican|indonesia(?:n)?\b|vietnam(?:ese)?\b|"
         r"thailand|thai\b|malaysia(?:n)?\b|philippines|emerging\s+(?:market|econom|economy)"),
    # 3 — Transition
    (3, r"\btransition\s+econom|eastern\s+europe|poland|polish\b|czech|"
         r"hungary|romanian|ukraine|kazakhstan|central\s+asia"),
    # 4 — Resource-rich / GCC
    (4, r"\bgcc\b|saudi|qatar|kuwait|uae\b|bahrain|oman\b|nigeria|"
         r"angola|resource.rich|resource\s+abundan"),
    # 5 — SIDS
    (5, r"\bsingapore(?:an)?\b|malta\b|mauritius\b|caribbean\b|"
         r"small\s+island|pacific\s+island"),
    # 6 — Frontier / LDC
    (6, r"\bbangladesh\b|ethiopia\b|myanmar\b|cambodia\b|ldc\b|"
         r"least.developed|sub.saharan|frontier\s+(?:market|econom)"),
]

# ── DOI-type patterns ─────────────────────────────────────────────────────────
DOI_TYPE_PATTERNS = [
    ("FSTS",               r"\bfsts\b|\bforeign\s+sales\s+to\s+total"),
    ("export_ratio",       r"\bexport\s+intensit|\bexport\s+ratio|\bexport\s+propensit"),
    ("FDI",                r"\bfdi\b|\bforeign\s+direct\s+invest"),
    ("DOI",                r"\bdegree\s+of\s+internationaliz"),
    ("geographic_diversification", r"\bgeographic\s+diversif|\binternational\s+diversif"),
    ("entry_mode",         r"\bentry\s+mode|\bforeign\s+market\s+entr"),
    ("subsidiaries",       r"\bforeign\s+subsidiari"),
    ("other",              r"\binternationaliz|\binternationalis|\bmultinational"),
]

# ── FP-type patterns ──────────────────────────────────────────────────────────
FP_TYPE_PATTERNS = [
    ("ROA",             r"\breturn\s+on\s+assets?\b|\broa\b"),
    ("ROE",             r"\breturn\s+on\s+equit|\broe\b"),
    ("ROS",             r"\breturn\s+on\s+sales|\bros\b"),
    ("Tobin_Q",         r"\btobin.?s?\s+q\b|\bmarket.to.book"),
    ("labor_productivity", r"\blabou?r\s+productivit|\bworker\s+productivit"),
    ("TFP",             r"\btotal\s+factor\s+product|\btfp\b"),
    ("sales_growth",    r"\bsales\s+growth|\brevenue\s+growth"),
    ("financial_perf",  r"\bfinancial\s+performance|\bprofitabilit"),
    ("firm_performance", r"\bfirm\s+performance|\bcorporate\s+performance"),
]


def apply_rules(text: str, rules: list) -> list[tuple[str, int]]:
    """Return list of (label, weight) for matched rules."""
    matched = []
    t = text.lower()
    for pattern, label, weight in rules:
        if re.search(pattern, t):
            matched.append((label, weight))
    return matched


def prescreen_row(row: dict) -> dict:
    title   = row.get("title", "") or ""
    journal = row.get("journal", "") or ""
    text    = f"{title} {journal}"

    excl = apply_rules(text, EXCLUDE_RULES)
    incl = apply_rules(text, INCLUDE_RULES)

    excl_score = sum(w for _, w in excl)
    incl_score = sum(w for _, w in incl)

    # Decision logic
    if excl_score >= 3:
        flag   = "N"
        reason = "EXCL:" + "|".join(l for l, _ in excl)
    elif incl_score >= 3:
        flag   = "Y"
        reason = "INCL:" + "|".join(l for l, _ in incl)
    elif incl_score >= 2:
        flag   = "UNSURE"
        reason = "WEAK-INCL:" + "|".join(l for l, _ in incl)
    else:
        flag   = "UNSURE"
        reason = "NO-CLEAR-SIGNAL"

    # ICRV
    icrv = ""
    t_lower = text.lower()
    for code, pattern in ICRV_PATTERNS:
        if re.search(pattern, t_lower):
            icrv = str(code)
            break

    # doi_type
    doi_type = ""
    for dtype, pattern in DOI_TYPE_PATTERNS:
        if re.search(pattern, t_lower):
            doi_type = dtype
            break

    # fp_type
    fp_type = ""
    for ftype, pattern in FP_TYPE_PATTERNS:
        if re.search(pattern, t_lower):
            fp_type = ftype
            break

    return {
        "prescreen_flag":     flag,
        "prescreen_reason":   reason,
        "prescreen_icrv":     icrv,
        "prescreen_doi_type": doi_type,
        "prescreen_fp_type":  fp_type,
    }


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--input",       required=True)
    p.add_argument("--output",      required=True)
    p.add_argument("--skip-coded",  action="store_true",
                   help="Skip rows that already have include_flag filled")
    return p.parse_args()


def main():
    args = parse_args()
    src  = Path(args.input)
    dst  = Path(args.output)
    dst.parent.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(open(src, encoding="utf-8")))
    if not rows:
        print("Empty input file.", file=sys.stderr)
        sys.exit(1)

    results   = []
    n_y = n_n = n_unsure = n_skip = 0

    for row in rows:
        existing_flag = row.get("include_flag", "").strip()
        if args.skip_coded and existing_flag:
            row["prescreen_flag"]     = existing_flag
            row["prescreen_reason"]   = "already-coded"
            row["prescreen_icrv"]     = row.get("icrv", "")
            row["prescreen_doi_type"] = row.get("doi_type", "")
            row["prescreen_fp_type"]  = row.get("fp_type", "")
            n_skip += 1
        else:
            ps = prescreen_row(row)
            row.update(ps)
            if ps["prescreen_flag"] == "Y":
                n_y += 1
            elif ps["prescreen_flag"] == "N":
                n_n += 1
            else:
                n_unsure += 1
        results.append(row)

    # Add prescreen columns to fieldnames
    new_fields = ["prescreen_flag", "prescreen_reason",
                  "prescreen_icrv", "prescreen_doi_type", "prescreen_fp_type"]
    base_fields = list(rows[0].keys())
    for f in new_fields:
        if f not in base_fields:
            base_fields.append(f)

    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=base_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    total = len(rows) - n_skip
    print(f"Processed  : {total} rows ({n_skip} skipped — already coded)")
    print(f"  Pre-Y    : {n_y}  ({n_y/max(1,total)*100:.1f}%) — likely INCLUDE")
    print(f"  Pre-N    : {n_n}  ({n_n/max(1,total)*100:.1f}%) — likely EXCLUDE")
    print(f"  UNSURE   : {n_unsure}  ({n_unsure/max(1,total)*100:.1f}%) — needs full-text review")
    print(f"\nOutput     : {dst}")
    print()
    print("WORKFLOW:")
    print("  1. Open the output CSV in Excel/Google Sheets")
    print("  2. Sort by prescreen_flag: review N first (fast dismissals)")
    print("  3. For each UNSURE: retrieve full text, apply codebook criteria")
    print("  4. Copy prescreen_flag → include_flag when confirmed")
    print("  5. Fill blank effect-size columns (r, n, icrv, etc.) for include_flag==Y")


if __name__ == "__main__":
    main()
