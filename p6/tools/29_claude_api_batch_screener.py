#!/usr/bin/env python3
"""
29_claude_api_batch_screener.py — Claude API-powered L2 screening assistant.

Uses claude-haiku-4-5 (cheap, fast) to assess each title for I→P eligibility.
Processes all UNSURE and unscreened rows from the extraction worklist.

Requirements:
    pip install anthropic

Usage (run on local machine with internet access):
    python3 29_claude_api_batch_screener.py \\
        --input  p6/tools/results/l2_prescreened_v1_20260519.csv \\
        --output p6/tools/results/l2_ai_screened_20260519.csv \\
        --api-key sk-ant-YOUR_KEY_HERE \\
        --mode unsure          # process only UNSURE rows
        --batch-size 20        # papers per API call (haiku handles 20 well)
        --dry-run              # print first batch prompt without calling API

Cost estimate:
    163 UNSURE papers × ~250 tokens input + ~80 tokens output ≈ $0.02 total with haiku

Output columns added:
    ai_flag        — Y / N / UNSURE (Claude's recommendation)
    ai_reason      — 1-sentence explanation
    ai_confidence  — high / medium / low

Eligibility criteria for P6 I→P meta-analysis:
  INCLUDE (Y):
    - Firm-level unit of analysis
    - Quantitative: reports Pearson r, regression coefficient, or convertible stat
    - Relationship: internationalization (FSTS, DOI, export intensity) → firm performance
      (financial: ROA, ROE, profit, Tobin's Q; or operational: productivity, TFP, growth)
  EXCLUDE (N):
    - Macro/country-level analysis
    - Export performance as DV with non-internationalization IV (wrong direction)
    - Qualitative / conceptual / review-only
    - Health/medical domain
    - Book chapters, dissertations
    - No quantitative I→P relationship
  UNSURE:
    - Cannot determine from title alone; abstract/full-text needed
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

SYSTEM_PROMPT = """You are an expert meta-analyst screening papers for a systematic review on
internationalization-firm performance (I→P) relationships in Asia-Pacific.

ELIGIBILITY CRITERIA — INCLUDE (Y):
  1. Firm-level unit of analysis (NOT country-level or macro)
  2. Reports a quantitative relationship (r, beta, t-stat, F-stat, or similar)
  3. Relationship direction: internationalization (e.g., FSTS, export intensity, DOI,
     multinationality, FDI) → firm performance (financial: ROA, ROE, profit, Tobin's Q;
     OR operational: productivity, TFP, efficiency, growth, survival)
  Note: "export performance" CAN be a valid DV if measured as export profitability/growth,
  but NOT if the paper studies what capabilities/strategies improve export outcomes.

EXCLUDE (N):
  - IV is capability/strategy/resources and DV is export performance → WRONG DIRECTION
  - Determinants/antecedents of exporting behavior (exporting as DV)
  - Macro-level / country-level analysis
  - Qualitative, conceptual, or review papers
  - Health/medical/agricultural domains
  - Book chapters, dissertations (non-peer-reviewed)
  - Papers about innovation or technology adoption without I→P link

UNSURE: Cannot determine from title alone; abstract needed.

For each paper, respond with exactly this JSON structure (one object per paper, in an array):
{"seq": N, "ai_flag": "Y|N|UNSURE", "ai_confidence": "high|medium|low", "ai_reason": "one sentence"}"""


def build_batch_prompt(rows: list[dict]) -> str:
    lines = ["Screen these papers for I→P eligibility. Respond with a JSON array.\n"]
    for r in rows:
        lines.append(f'[{r["seq"]}] Title: "{r["title"]}"')
        if r.get("journal"):
            lines.append(f'    Journal: {r["journal"][:60]}')
        if r.get("year"):
            lines.append(f'    Year: {r["year"]}')
        if r.get("abstract", "").strip():
            ab = r["abstract"].strip()[:300]
            lines.append(f'    Abstract: {ab}')
    return "\n".join(lines)


# Project model resolution chain: ANTHROPIC_MODEL -> ANTHROPIC_DEFAULT_FABLE_MODEL
# -> cheap default. NOTE: this is a bulk screener over thousands of abstracts;
# with the project-wide Fable default the cost is ~10x Haiku. Pass
# ANTHROPIC_MODEL=claude-haiku-4-5 for a cheap run.
SCREENING_MODEL = (
    os.environ.get("ANTHROPIC_MODEL")
    or os.environ.get("ANTHROPIC_DEFAULT_FABLE_MODEL")
    or "claude-haiku-4-5-20251001"
)


def call_claude_api(client, prompt: str, retries: int = 3) -> list[dict]:
    for attempt in range(retries):
        try:
            msg = client.messages.create(
                model=SCREENING_MODEL,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            text = next(
                (b.text for b in msg.content if b.type == "text"), ""
            ).strip()
            # Extract JSON array from response
            if "```" in text:
                text = text.split("```")[1].strip()
                if text.startswith("json"):
                    text = text[4:].strip()
            return json.loads(text)
        except json.JSONDecodeError as e:
            print(f"  [WARNING] JSON parse error (attempt {attempt+1}): {e}", file=sys.stderr)
            if attempt < retries - 1:
                time.sleep(2)
        except Exception as e:
            print(f"  [ERROR] API call failed (attempt {attempt+1}): {e}", file=sys.stderr)
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    return []


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")
    ap.add_argument("--mode", choices=["all", "unsure", "unscreened"],
                    default="unsure",
                    help="Which rows to process: all, unsure (prescreen_flag=UNSURE), "
                         "or unscreened (no prescreen_flag)")
    ap.add_argument("--batch-size", type=int, default=15,
                    help="Papers per API call (default: 15)")
    ap.add_argument("--delay", type=float, default=1.0,
                    help="Seconds between API calls (default: 1.0)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print first batch prompt without calling API")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.input, encoding="utf-8")))
    print(f"Loaded {len(rows)} rows from {args.input}")

    if args.mode == "unsure":
        to_process = [r for r in rows if r.get("prescreen_flag") == "UNSURE"]
    elif args.mode == "unscreened":
        to_process = [r for r in rows if not r.get("prescreen_flag")]
    else:
        to_process = rows
    print(f"Mode '{args.mode}': {len(to_process)} rows to process")

    if args.dry_run:
        sample = to_process[:args.batch_size]
        print("\n── DRY RUN: First batch prompt ──")
        print(build_batch_prompt(sample))
        print("\n── END DRY RUN ──")
        return

    # Initialize Anthropic client
    import os
    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Provide --api-key or set ANTHROPIC_API_KEY env var", file=sys.stderr)
        sys.exit(1)
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
    except ImportError:
        print("ERROR: Run 'pip install anthropic' first", file=sys.stderr)
        sys.exit(1)

    # Build index for quick lookup
    results: dict[str, dict] = {}

    # Process in batches
    batches = [to_process[i:i+args.batch_size]
               for i in range(0, len(to_process), args.batch_size)]
    print(f"Processing {len(batches)} batches of ≤{args.batch_size} papers...")

    for i, batch in enumerate(batches, 1):
        print(f"  Batch {i}/{len(batches)} (seqs {batch[0]['seq']}–{batch[-1]['seq']})...",
              end=" ", flush=True)
        prompt = build_batch_prompt(batch)
        api_results = call_claude_api(client, prompt)
        for res in api_results:
            seq = str(res.get("seq", ""))
            results[seq] = res
        hits = len([r for r in api_results if r.get("ai_flag") == "Y"])
        excl = len([r for r in api_results if r.get("ai_flag") == "N"])
        print(f"Y={hits}, N={excl}, UNSURE={len(api_results)-hits-excl}")
        if i < len(batches):
            time.sleep(args.delay)

    # Merge results back into rows
    out_fieldnames = list(rows[0].keys())
    for col in ("ai_flag", "ai_reason", "ai_confidence"):
        if col not in out_fieldnames:
            out_fieldnames.append(col)

    outpath = Path(args.output)
    outpath.parent.mkdir(parents=True, exist_ok=True)
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fieldnames)
        writer.writeheader()
        for row in rows:
            seq = str(row.get("seq", ""))
            if seq in results:
                row["ai_flag"] = results[seq].get("ai_flag", "")
                row["ai_reason"] = results[seq].get("ai_reason", "")
                row["ai_confidence"] = results[seq].get("ai_confidence", "")
            else:
                row.setdefault("ai_flag", "")
                row.setdefault("ai_reason", "")
                row.setdefault("ai_confidence", "")
            writer.writerow(row)

    # Summary
    ai_y = sum(1 for r in results.values() if r.get("ai_flag") == "Y")
    ai_n = sum(1 for r in results.values() if r.get("ai_flag") == "N")
    ai_u = sum(1 for r in results.values() if r.get("ai_flag") == "UNSURE")
    print(f"\nResults: AI-Y={ai_y}, AI-N={ai_n}, AI-UNSURE={ai_u}, no-result={len(to_process)-len(results)}")
    print(f"Output written to: {outpath}")


if __name__ == "__main__":
    main()
