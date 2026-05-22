#!/usr/bin/env python3
"""
62_groq_l2_prescreen.py
Batch L2 pre-screening of tracker_v2 papers using Groq (llama-3.3-70b-versatile).
Uses title + abstract (from 61_enrich_abstracts_openalex.py) + metadata guesses.
Writes fulltext_screening_decision (Y/N/UNSURE) + fulltext_screening_reason back to tracker.

Usage:
    export GROQ_API_KEY=gsk_...
    python3 p6/tools/62_groq_l2_prescreen.py [--limit N] [--batch 20] [--dry-run]

Rate limit: 30 req/min free tier — script auto-throttles.
"""
import csv, os, sys, time, json, argparse, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime

TRACKER    = Path("p6/tools/results/fulltext_to_extraction_tracker_v2.csv")
ABSTRACTS  = Path("p6/tools/results/abstracts_enriched.csv")
LOG_OUT    = Path(f"p6/tools/results/groq_l2_prescreen_{datetime.now().strftime('%Y%m%d_%H%M')}.csv")

GROQ_URL   = "https://api.groqcloud.com/openai/v1/chat/completions"
MODEL      = "llama-3.3-70b-versatile"
MAX_TOKENS = 200
SLEEP_REQ  = 2.1   # ~28 req/min (free limit: 30)

SYSTEM_PROMPT = """You are a meta-analysis screening assistant for an internationalization→firm performance (I→P) meta-analysis covering Asia-Pacific firms.

L2 inclusion criteria (ALL must be YES to include):
1. FIRM-LEVEL unit of analysis (not country/industry/individual)
2. Internationalization MEASURED (FSTS, export intensity, FDI, DOI, entropy, n_markets, subsidiary count)
3. Firm PERFORMANCE measured (ROA, ROE, Tobin Q, ROS, sales growth, labor productivity, profit)
4. QUANTITATIVE I→P relationship reported (r, β, t, F, or convertible statistic)
5. PEER-REVIEWED journal article (not dissertation, WP, book chapter, conference only)

INSTANT EXCLUDE (any one → N):
- Country-level or macro-level analysis only
- Qualitative / purely conceptual / review-only
- Health, environment, CSR without financial performance
- Meta-analysis itself as the study (wrong design)
- "Antecedents of internationalization" or "determinants of export" (wrong direction — performance is IV not DV)
- No quantitative I→P relationship data reported

Respond in JSON only:
{"decision": "Y" or "N" or "UNSURE", "reason": "one short sentence"}

decision=Y: clearly meets all 5 criteria
decision=N: fails one or more (state which)
decision=UNSURE: cannot determine without full text"""

def build_user_msg(row: dict, abstract: str) -> str:
    parts = [
        f"Title: {row['title']}",
        f"Year: {row['year']}",
        f"Journal: {row['journal']}",
        f"Authors: {row.get('authors','')[:80]}",
        f"I-measure guess: {row.get('internationalization_measure_guess','')}",
        f"FP-measure guess: {row.get('performance_measure_guess','')}",
        f"Research design guess: {row.get('research_design_guess','')}",
        f"Country/region: {row.get('country_guess','')} / {row.get('region_guess','')}",
    ]
    if abstract:
        parts.append(f"\nAbstract: {abstract[:800]}")
    else:
        parts.append("\nAbstract: [not available — decide based on title and metadata]")
    return "\n".join(parts)

def groq_call(user_msg: str, api_key: str) -> tuple[str, str]:
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": 0.1,
        "response_format": {"type": "json_object"}
    }).encode()

    req = urllib.request.Request(
        GROQ_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
            content = data["choices"][0]["message"]["content"]
            result = json.loads(content)
            return result.get("decision", "UNSURE"), result.get("reason", "")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            return "RATE_LIMIT", "rate limit hit"
        return "API_ERROR", f"HTTP {e.code}"
    except Exception as ex:
        return "API_ERROR", str(ex)[:100]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--batch", type=int, default=50, help="Papers per run")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key and not args.dry_run:
        sys.exit("Set GROQ_API_KEY env var")

    # Load tracker
    tracker_rows = list(csv.DictReader(TRACKER.open(encoding="utf-8")))
    tracker_by_seq = {r["seq"]: r for r in tracker_rows}

    # Load abstracts
    abstracts = {}
    if ABSTRACTS.exists():
        for r in csv.DictReader(ABSTRACTS.open(encoding="utf-8")):
            abstracts[r["seq"]] = r.get("abstract", "")
    print(f"Abstracts available: {len([v for v in abstracts.values() if v])}/{len(tracker_rows)}")

    # Filter: only papers without decision yet
    todo = [r for r in tracker_rows if not r.get("fulltext_screening_decision", "").strip()]
    print(f"Papers needing L2 decision: {len(todo)}")

    if args.limit:
        todo = todo[:args.limit]
    if args.batch:
        todo = todo[:args.batch]
    print(f"Processing this run: {len(todo)}")

    log_fields = ["seq", "doi", "title", "decision", "reason", "had_abstract", "model"]
    log_writer = csv.DictWriter(LOG_OUT.open("w", newline="", encoding="utf-8"), fieldnames=log_fields)
    log_writer.writeheader()

    # Track decisions to apply back to tracker
    decisions = {}
    stats = {"Y": 0, "N": 0, "UNSURE": 0, "error": 0}

    for i, row in enumerate(todo):
        seq = row["seq"]
        abstract = abstracts.get(seq, "")
        had_abs = bool(abstract)

        user_msg = build_user_msg(row, abstract)

        if args.dry_run:
            print(f"[{i+1}/{len(todo)}] {seq} | abstract={'yes' if had_abs else 'no'} | {row['title'][:60]}")
            continue

        decision, reason = groq_call(user_msg, api_key)

        if decision == "RATE_LIMIT":
            print(f"Rate limit at {i+1}, waiting 60s...")
            time.sleep(60)
            decision, reason = groq_call(user_msg, api_key)

        if decision in ("API_ERROR", "RATE_LIMIT"):
            stats["error"] += 1
            decision = "UNSURE"
            reason = f"API error: {reason}"
        else:
            stats[decision] = stats.get(decision, 0) + 1

        decisions[seq] = (decision, reason)
        log_writer.writerow({
            "seq": seq, "doi": row.get("doi",""), "title": row["title"],
            "decision": decision, "reason": reason,
            "had_abstract": "yes" if had_abs else "no", "model": MODEL
        })

        print(f"[{i+1}/{len(todo)}] {seq} → {decision} | {reason[:60]}")
        time.sleep(SLEEP_REQ)

    if args.dry_run:
        return

    # Apply decisions back to tracker CSV
    if decisions:
        updated = 0
        for r in tracker_rows:
            if r["seq"] in decisions:
                dec, rsn = decisions[r["seq"]]
                r["fulltext_screening_decision"] = dec
                r["fulltext_screening_reason"] = rsn
                updated += 1

        with TRACKER.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=tracker_rows[0].keys())
            writer.writeheader()
            writer.writerows(tracker_rows)

        print(f"\nUpdated {updated} rows in tracker")

    print(f"\nStats: Y={stats.get('Y',0)} N={stats.get('N',0)} UNSURE={stats.get('UNSURE',0)} error={stats.get('error',0)}")
    print(f"Log: {LOG_OUT}")

if __name__ == "__main__":
    main()
