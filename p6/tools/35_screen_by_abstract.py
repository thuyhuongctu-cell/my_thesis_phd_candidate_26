#!/usr/bin/env python3
"""
35_screen_by_abstract.py — Re-screen UNSURE records using abstracts.

Inherits all HARD_EXCL / STRONG_INCL patterns from title screener.
Abstract gives more signal → fewer UNSURE remaining.

Input:  p6/tools/results/abstracts_YYYYMMDD.csv
Output: p6/tools/results/abstract_screened_YYYYMMDD.csv
        p6/tools/results/abstract_screen_summary_YYYYMMDD.txt
"""

import csv
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
import argparse

TODAY = datetime.now().strftime("%Y%m%d")

# ── HARD EXCLUSION (topic is definitively out-of-scope) ─────────────────────
HARD_EXCL = [
    # OOB: health / medicine / environment
    (r"\b(health|clinical|hospital|patient|disease|mortality|obesity|BMI|medical|"
     r"physician|nutriti|pandemic(?! econ)|COVID(?! econ)|malnutri|maternal|child "
     r"health|environmental compliance|carbon emission|pollution abatement|"
     r"biodiversity)\b", "oob:health"),
    (r"\b(deforestation|ecological|species diversity|marine|fisheries|"
     r"water quality|soil|agricultural yield)\b", "oob:environment"),
    # OOB: individual / household
    (r"\b(household income|personal income|individual earnings|wage inequality|"
     r"labour supply|human capital accumulation|school enroll|student perform)\b",
     "oob:individual"),
    # Antecedents (I as DV)
    (r"\b(determinants? of (export|FDI|internationali|outward)|"
     r"drivers? of (export|internationali|FDI)|"
     r"factors? (affecting|influencing) (export|internationali|FDI)|"
     r"antecedents? of (export|internationali)|"
     r"what (drives?|explains?) (export|internationali)|"
     r"propensity to (export|internationali)|"
     r"likelihood of (exporting|internationaliz))\b", "ant:determinants"),
    (r"\b(entry mode (choice|select|decision|determin)|"
     r"choice of entry|mode of entry|foreign market entry (mode|decision|select))\b",
     "ant:entry_mode"),
    (r"\b(export (start-up|start up|initiation|decision to export|inception)|"
     r"(decision|propensity|intention) to (export|go international)|"
     r"export participation decision)\b", "ant:export_decision"),
    # Process / strategy (not I→P link)
    (r"\b(supply chain (resilience|disruption|risk|vulnerability|collabor|integr)|"
     r"global supply chain|supply chain management)\b", "proc:supply_chain"),
    (r"\b(global value chain|GVC (participat|integr|position|upgrading)|"
     r"value chain upgrading)\b", "proc:GVC"),
    (r"\b(internationalization (process|speed|pace|sequence|pathway|pattern|"
     r"trajectory|mode|stage|decision)|stages? of internationalization|"
     r"gradual internationalization|Uppsala model test)\b", "proc:intl_process"),
    (r"\b(location (choice|decision|selection|strategy)|"
     r"where to (invest|locate|expand))\b", "strat:location"),
    # Governance / CSR / ESG as DV
    (r"\b(corporate governance|board (composition|diversity|independence|size)|"
     r"CEO (duality|turnover|compensation)|managerial (entrenchment|ownership)|"
     r"earnings management|audit quality|transparency|disclosure quality)\b",
     "gov:corp_gov"),
    (r"\b(CSR (reporting|disclosure|performance|rating)|"
     r"sustainability report|ESG (score|rating|disclosure|reporting))\b",
     "gov:csr_esg_dv"),
    # Innovation as sole DV
    (r"\b(innovation (output|performance|capability|activity) (as|is) (the |a )?"
     r"(dependent|outcome)|R&D (output|productivity|success)|"
     r"patent (count|productivity|output))\b", "DV:innovation_only"),
    # Theory / bibliometric / meta-review papers
    (r"\b(bibliometric (analysis|review|mapping|study)|"
     r"systematic (literature review|review of|mapping)|"
     r"meta-analysis of (determinants|antecedents|entry)|"
     r"literature review (on|of) (determinants|antecedents)|"
     r"conceptual (framework|model|paper) (for|of) internationali)\b",
     "meth:bibliometric"),
    (r"\b(case study (of|approach)|qualitative (research|study|approach|method)|"
     r"grounded theory|ethnograph|interview(s| data))\b", "qual:case_study"),
    # Financial structure as DV
    (r"\b(capital structure|debt (ratio|level|maturity)|leverage (ratio|decision)|"
     r"optimal (debt|leverage|capital)|financial (distress|risk) (as|is))\b",
     "fin:capital_structure"),
]

# ── STRONG INCLUSION ─────────────────────────────────────────────────────────
STRONG_INCL = [
    # Direct I→P relationship language (title OR abstract)
    (r"\b(impact|effect|influence|consequence|implication|benefit|cost|"
     r"relationship|link|association|nexus) (of|between) "
     r"(internationali|export|FDI|multinational|foreign (sales|operation)|"
     r"outward FDI|degree of internationali)\b.*\b(performance|profitabil|"
     r"productiv|efficiency|return|value|growth)\b", "SI:intl_perf"),
    (r"\b(export|internationali|FDI|multinational) "
     r"(and|on|affect|determin|explain|predict)\b.*\b"
     r"(performance|profitabil|productiv|efficiency|return|value|growth)\b",
     "SI:intl_and_perf"),
    # Export–productivity / learning-by-exporting
    (r"\b(learning[- ]by[- ]exporting|export[- ]led (productivity|growth)|"
     r"self[- ]selection (and|vs) learning|export premium|exporter premium|"
     r"export status and productivity|productivity (of|among|for) exporters)\b",
     "SI:exp_prod"),
    (r"\b(export (intensity|performance|success|profitability|effectiveness)|"
     r"export.*profit|profit.*export)\b", "SI:exp_perf"),
    # MNE / FDI performance
    (r"\b(MNE performance|multinational performance|"
     r"subsidiary performance|affiliate performance|"
     r"FDI and (firm )?performance|outward FDI (and|on) performance)\b",
     "SI:mne_perf"),
    (r"\b(FDI (and|on|effect on) productiv|"
     r"foreign (direct )?investment (and|on) (firm )?productiv)\b",
     "SI:fdi_prod"),
    # Degree of internationalization / DOI
    (r"\b(degree of internationali|DOI (and|on)|"
     r"international diversific (and|on|effect) performance|"
     r"geographic diversific (and|on) (firm )?perform|"
     r"internationali[sz]ation[- ]performance (relationship|link|nexus))\b",
     "SI:doi_explicit"),
    # Curvilinear / inverted-U / U-shape
    (r"\b(inverted.?U|U.?shape[d]?|curvilinear|nonlinear|quadratic) "
     r"(relation|effect|impact|link).*(internationali|export|FDI|performance)\b",
     "SI:curvilinear"),
    (r"\b(optimal (level|degree) of internationali|"
     r"too (much|little) internationali|"
     r"limits? (of|to) internationali)\b", "SI:optimal_doi"),
    # Firm value
    (r"\b(firm value (and|of|for)|Tobin.s Q (and|of)|"
     r"shareholder value (and|of)|market value (of|and) (international|MNE|exporter))\b",
     "SI:firm_value"),
    # SME internationalization → performance
    (r"\b(SME (internationali|export) (and|on|effect) (performance|profitabil|growth)|"
     r"small (firm|business|enterprise) (export|internationali) performance)\b",
     "SI:sme_intl_perf"),
    # Asia-Pacific / emerging market context with I→P
    (r"\b(Asia[n-]? (firm|MNE|multinational|company)|"
     r"Chinese (firm|MNE|exporter|company)|"
     r"emerging market (firm|MNE|multinational)) (and|on|in) "
     r"(performance|productiv|profitabil)\b", "SI:apac_firm_perf"),
    # Performance consequences of going international
    (r"\b(performance (consequence|implication|outcome) of (internationali|export|FDI)|"
     r"going (international|abroad|global) (and|effect on) performance)\b",
     "SI:perf_consequence"),
    # ICRV-relevant institutional context + performance
    (r"\b(institutional (context|environment|quality|framework) (and|on|moderate|"
     r"contingent on)) .{0,80}(internationali|export).*perform\b",
     "SI:institutional_moderation"),
    # Digital adoption + internationalization + performance
    (r"\b(digital (adoption|transformation|technology|platform|e-commerce)) "
     r".{0,100}(internationali|export|FDI).{0,100}(performance|productiv)\b",
     "SI:digital_intl_perf"),
]

# Dual-signal: must match BOTH
INTL_RE = re.compile(
    r"\b(internationali[sz]|export(er|ing)?|FDI|foreign (sales|operation)|"
    r"multinational|MNE|transnational|outward investment|cross.?border)\b",
    re.I,
)
PERF_RE = re.compile(
    r"\b(performance|profitabilit|productivit|efficiency|ROA|ROE|Tobin|"
    r"return on (asset|equity|sales)|firm value|sales growth|revenue growth)\b",
    re.I,
)

def classify(title: str, abstract: str) -> tuple[str, str]:
    text = f"{title} {abstract}"
    text_l = text.lower()

    for pattern, tag in HARD_EXCL:
        if re.search(pattern, text, re.I):
            return "N", f"HARD:{tag}"

    for pattern, tag in STRONG_INCL:
        if re.search(pattern, text, re.I):
            return "Y", f"STRONG:{tag}"

    if INTL_RE.search(text) and PERF_RE.search(text):
        return "Y", "DUAL:intl+perf"

    return "UNSURE", "abstract_insufficient"


def run(input_path: Path, output_path: Path, summary_path: Path):
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        src_fields = list(reader.fieldnames)

    out_fields = src_fields + ["ab_decision", "ab_reason"]
    results = []
    counters = Counter()
    reason_counts = Counter()

    for row in rows:
        title = row.get("title", "")
        abstract = row.get("abstract", "")
        decision, reason = classify(title, abstract)
        row["ab_decision"] = decision
        row["ab_reason"] = reason
        counters[decision] += 1
        reason_counts[reason] += 1
        results.append(row)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(results)

    total = len(results)
    lines = [
        f"Abstract screening summary — {TODAY}",
        f"",
        f"Total processed: {total}",
        f"  Y  (include): {counters['Y']:>5}  ({counters['Y']/total*100:.1f}%)",
        f"  N  (exclude): {counters['N']:>5}  ({counters['N']/total*100:.1f}%)",
        f"  UNSURE:       {counters['UNSURE']:>5}  ({counters['UNSURE']/total*100:.1f}%)",
        f"",
        f"Top inclusion reasons:",
    ]
    for reason, cnt in reason_counts.most_common(15):
        if "STRONG" in reason or "DUAL" in reason:
            lines.append(f"  {cnt:>5}  {reason}")
    lines.append("")
    lines.append("Top exclusion reasons:")
    for reason, cnt in reason_counts.most_common(15):
        if "HARD" in reason:
            lines.append(f"  {cnt:>5}  {reason}")
    lines.append("")
    lines.append(f"Output: {output_path}")

    summary = "\n".join(lines)
    print(summary)
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=f"p6/tools/results/abstracts_{TODAY}.csv")
    parser.add_argument("--output", default=f"p6/tools/results/abstract_screened_{TODAY}.csv")
    parser.add_argument("--summary", default=f"p6/tools/results/abstract_screen_summary_{TODAY}.txt")
    args = parser.parse_args()
    run(Path(args.input), Path(args.output), Path(args.summary))
