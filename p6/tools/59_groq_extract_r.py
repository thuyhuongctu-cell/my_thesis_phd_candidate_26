#!/usr/bin/env python3
"""
59_groq_extract_r.py — Groq API batch r-extraction from PDFs (free tier)

Same workflow as 57_claude_api_extract_r.py but uses Groq's free LLM API.
For each paper in the extraction queue with fulltext_screening_decision=='Y'
and no converted_r yet:
  1. Locates PDF in pdf-dir (or downloads from OA manifest URL)
  2. Extracts text with pdfplumber
  3. Asks Groq LLM to identify the I→P effect size and convert to r
  4. Writes result back to fulltext_to_extraction_tracker_v3.csv

Usage:
    python3 59_groq_extract_r.py \
        --queue   p6/tools/results/extraction_queue_20260520.csv \
        --tracker p6/tools/results/fulltext_to_extraction_tracker_v3.csv \
        --pdf-dir p6/pdfs \
        --log     p6/tools/results/groq_extract_log_20260523_1200.csv \
        --limit   50 \
        [--manifest p6/tools/results/oa_manifest_20260520.csv] \
        [--model llama-3.3-70b-versatile] \
        [--dry-run]

Requires:  pip install groq pdfplumber requests
Secret:    GROQ_API_KEY env variable (free at console.groq.com)
"""

import csv, json, os, re, sys, argparse, time
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("ERROR: pip install pdfplumber"); sys.exit(1)

try:
    from groq import Groq
except ImportError:
    print("ERROR: pip install groq"); sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: pip install requests"); sys.exit(1)

# ─── Configuration ────────────────────────────────────────────────────────────
DEFAULT_MODEL  = "llama-3.3-70b-versatile"
MAX_TOKENS     = 512
PDF_TEXT_CHARS = 16_000   # ~4k tokens: head + results window, safe for Groq free tier

EXTRACTION_PROMPT = """\
You are a meta-analysis research assistant. Extract the main \
internationalization → firm performance effect size from the paper excerpt below.

TASK:
1. Identify the primary regression coefficient or correlation for the \
   internationalization → firm performance relationship (e.g. FSTS→ROA, \
   export intensity→productivity, DOI→Tobin's Q).
2. Convert it to a Pearson r using these formulas:
   - If r is directly reported: use it as-is.
   - If β (OLS) and SD ratio unavailable: r ≈ β (approximation).
   - If t-statistic and df known: r = t / sqrt(t² + df).
   - If F-statistic (df1=1) and df_error known: r = sqrt(F / (F + df_error)).
3. Report the sample size N.
4. Note whether the relationship is linear or nonlinear (U-shape, inverted-U).

RESPOND in this exact JSON format (no markdown, no prose outside JSON):
{{
  "converted_r": <float or null>,
  "conversion_formula": "<direct|beta|t_to_r|F_to_r|not_found>",
  "sample_size_n": <integer or null>,
  "t_value": <float or null>,
  "p_value": <float or null>,
  "effect_direction": "<+|->",
  "curve_type": "<linear|inverted_u|u_shape|other|unknown>",
  "turning_point": <float or null>,
  "notes": "<brief 1-line extraction note>"
}}

If no I→P relationship can be found, set converted_r to null and \
conversion_formula to "not_found".

PAPER EXCERPT:
---
{text}
---
"""

# ─── Helpers ──────────────────────────────────────────────────────────────────

def pdf_text(pdf_path: Path) -> str:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full = "\n".join(p.extract_text() or "" for p in pdf.pages)
    except Exception:
        return ""
    if len(full) <= PDF_TEXT_CHARS:
        return full
    # Long paper: effect sizes live in the results/correlation tables, which a
    # naive head-truncation misses. Keep the head (abstract/intro/methods) plus
    # a window anchored where results statistics usually start.
    half = PDF_TEXT_CHARS // 2
    head = full[:half]
    low = full.lower()
    anchor = -1
    for kw in ("correlation", "table 2", "table 3", "regression results", "results"):
        anchor = low.find(kw, half)
        if anchor != -1:
            break
    if anchor == -1:
        anchor = len(full) // 2
    tail = full[anchor:anchor + half]
    return head + "\n...\n" + tail


def download_pdf(url: str, dest: Path) -> bool:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; meta-analysis-research)"}
    try:
        r = requests.get(url, timeout=30, allow_redirects=True, headers=headers)
        if r.status_code != 200:
            return False
        ctype = r.headers.get("Content-Type", "").lower()
        head = r.content[:1024]
        # Accept by magic bytes anywhere near the start OR by Content-Type;
        # many OA hosts serve valid PDFs without %PDF at byte 0.
        if b"%PDF" in head or "application/pdf" in ctype:
            dest.write_bytes(r.content)
            return True
        # Landing page: try to find a direct PDF link and fetch it once.
        if "text/html" in ctype:
            m = re.search(rb'href=["\']([^"\']+\.pdf[^"\']*)["\']', r.content, re.I)
            if m:
                pdf_url = m.group(1).decode("utf-8", "ignore")
                if pdf_url.startswith("/"):
                    from urllib.parse import urljoin
                    pdf_url = urljoin(r.url, pdf_url)
                r2 = requests.get(pdf_url, timeout=30, allow_redirects=True, headers=headers)
                if r2.status_code == 200 and (
                    b"%PDF" in r2.content[:1024]
                    or "application/pdf" in r2.headers.get("Content-Type", "").lower()
                ):
                    dest.write_bytes(r2.content)
                    return True
    except Exception:
        pass
    return False


def load_manifest(manifest_path: str | None) -> dict:
    """Returns doi → pdf_url mapping from OA manifest CSV."""
    if not manifest_path or not Path(manifest_path).exists():
        return {}
    out = {}
    with open(manifest_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            doi = (row.get("doi") or "").strip().lower()
            url = (row.get("pdf_url") or row.get("oa_url") or "").strip()
            if doi and url:
                out[doi] = url
    return out


def ask_groq(client: Groq, text: str, model: str, max_retries: int = 5) -> dict:
    """Send excerpt to Groq and parse JSON response, retrying on rate limits."""
    prompt = EXTRACTION_PROMPT.format(text=text)
    for attempt in range(max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=MAX_TOKENS,
                temperature=0.1,   # low temp for structured extraction
            )
            raw = response.choices[0].message.content.strip()
            # Strip markdown code fences if present
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            return json.loads(raw)
        except Exception as e:
            msg = str(e)
            # Groq free tier throttles by tokens/min; back off and retry on 429.
            if ("429" in msg or "rate limit" in msg.lower()) and attempt < max_retries:
                time.sleep(min(5 * (2 ** attempt), 60))
                continue
            return {"converted_r": None, "conversion_formula": "error",
                    "sample_size_n": None, "notes": f"Groq error: {e}"}


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Groq API batch r-extraction")
    parser.add_argument("--queue",    required=True,  help="Extraction queue CSV")
    parser.add_argument("--tracker",  required=True,  help="Tracker v3 CSV (updated in place)")
    parser.add_argument("--pdf-dir",  default="p6/pdfs", help="PDF download directory")
    parser.add_argument("--log",      required=True,  help="Output extraction log CSV")
    parser.add_argument("--limit",    type=int, default=50, help="Max papers per run (0=all)")
    parser.add_argument("--manifest", default="",     help="OA manifest CSV (doi→pdf_url)")
    parser.add_argument("--model",    default=DEFAULT_MODEL, help="Groq model name")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Print what would happen without modifying tracker")
    args = parser.parse_args()

    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        print("ERROR: GROQ_API_KEY not set. Get a free key at console.groq.com")
        sys.exit(1)

    client = Groq(api_key=api_key)
    pdf_dir = Path(args.pdf_dir)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(args.manifest or None)

    # ── Load queue ──────────────────────────────────────────────────────────
    queue_path = Path(args.queue)
    if not queue_path.exists():
        print(f"ERROR: Queue file not found: {queue_path}"); sys.exit(1)

    with open(queue_path, newline="", encoding="utf-8") as f:
        queue_rows = list(csv.DictReader(f))

    # Filter: Y decision, no r yet.
    # Curated queue files (e.g. extraction_queue_pdf_*.csv) omit the
    # fulltext_screening_decision column — all rows are pre-filtered to Y.
    # Default to "Y" so those files work without modification.
    pending = [r for r in queue_rows
               if r.get("fulltext_screening_decision", "Y").strip() != "N"
               and not r.get("converted_r", "").strip()]

    if args.limit > 0:
        pending = pending[:args.limit]

    print(f"Queue: {len(queue_rows)} total | {len(pending)} pending (limit={args.limit})",
          flush=True)
    print(f"Model: {args.model}", flush=True)

    # ── Load tracker ─────────────────────────────────────────────────────────
    tracker_path = Path(args.tracker)
    if not tracker_path.exists():
        print(f"ERROR: Tracker not found: {tracker_path}"); sys.exit(1)

    with open(tracker_path, newline="", encoding="utf-8") as f:
        tracker_rows = list(csv.DictReader(f))
    fieldnames = list(tracker_rows[0].keys()) if tracker_rows else []

    # Build lookup: seq → tracker row
    seq_index = {r.get("seq", "").strip(): r for r in tracker_rows}

    # ── Process papers ────────────────────────────────────────────────────────
    log_entries = []
    updated = 0
    skipped_manual = 0
    no_pdf = 0
    no_text = 0
    not_found = 0
    api_errors = 0
    auth_failed = False

    for i, qrow in enumerate(pending, 1):
        seq   = str(qrow.get("seq", "")).strip()
        doi   = (qrow.get("doi") or "").strip().lower()
        title = (qrow.get("title") or "")[:60]

        log = {"seq": seq, "doi": doi, "title": title[:50],
               "status": "", "converted_r": "", "conversion_formula": "",
               "sample_size_n": "", "t_value": "", "p_value": "",
               "effect_direction": "", "curve_type": "", "notes": ""}

        # Check if already manually filled in tracker
        tracker_row = seq_index.get(seq)
        if tracker_row and tracker_row.get("converted_r", "").strip():
            skipped_manual += 1
            log["status"] = "SKIP_MANUAL"
            log_entries.append(log)
            continue

        # Locate PDF
        existing = list(pdf_dir.glob(f"{seq}_*.pdf")) + list(pdf_dir.glob(f"{seq}.pdf"))
        pdf_path: Path | None = existing[0] if existing else None

        # Try downloading if not found
        if not pdf_path:
            oa_url = manifest.get(doi, "") or qrow.get("pdf_url", "") or qrow.get("best_url", "")
            if oa_url:
                safe = re.sub(r"[^\w]", "_", title[:30])
                dest = pdf_dir / f"{seq}_{safe}.pdf"
                if download_pdf(oa_url, dest):
                    pdf_path = dest
                    print(f"  [{i}/{len(pending)}] Downloaded: {dest.name}", flush=True)

        if not pdf_path:
            no_pdf += 1
            log["status"] = "NO_PDF"
            log["notes"] = "no PDF: download failed (paywall/landing page) or no OA URL"
            log_entries.append(log)
            continue

        # Extract text
        text = pdf_text(pdf_path)
        if not text.strip():
            no_text += 1
            log["status"] = "NO_TEXT"
            log["notes"] = "PDF is scan/image — no extractable text"
            log_entries.append(log)
            continue

        # Ask Groq
        result = ask_groq(client, text, args.model)
        time.sleep(0.5)   # Groq free tier: ~30 req/min; 0.5s gap is safe

        r_val = result.get("converted_r")
        conv  = result.get("conversion_formula", "not_found")
        n_val = result.get("sample_size_n")

        # LLMs often return numbers as strings ("0.34") or placeholders
        # ("N/A", null); coerce safely so round() never crashes the run.
        try:
            s = str(r_val).strip().lower()
            r_val = float(r_val) if r_val is not None and s not in ("", "null", "none", "n/a", "na") else None
        except (TypeError, ValueError):
            r_val = None
        try:
            n_val = int(float(n_val)) if n_val not in (None, "", "null") else None
        except (TypeError, ValueError):
            n_val = None

        log["converted_r"]        = str(round(r_val, 4)) if r_val is not None else ""
        log["conversion_formula"] = conv
        log["sample_size_n"]      = str(n_val) if n_val else ""
        log["t_value"]            = str(result.get("t_value") or "")
        log["p_value"]            = str(result.get("p_value") or "")
        log["effect_direction"]   = str(result.get("effect_direction") or "")
        log["curve_type"]         = str(result.get("curve_type") or "")
        log["notes"]              = str(result.get("notes") or "")[:120]

        if r_val is None:
            note = str(result.get("notes") or "")
            if conv == "error" or note.startswith("Groq error"):
                api_errors += 1
                log["status"] = "API_ERROR"
                log_entries.append(log)
                # A 401 affects every call — abort now instead of burning the batch.
                if "401" in note or "invalid api key" in note.lower():
                    auth_failed = True
                    print(f"\nFATAL: Groq rejected the API key (401 Invalid API Key).",
                          flush=True)
                    break
                print(f"  [{i}/{len(pending)}] seq={seq} — API error: {note[:70]}", flush=True)
                continue
            not_found += 1
            log["status"] = "NOT_FOUND"
            log_entries.append(log)
            print(f"  [{i}/{len(pending)}] seq={seq} — no I→P coeff found", flush=True)
            continue

        log["status"] = "EXTRACTED"
        log_entries.append(log)

        # Update tracker (never overwrite manual work)
        if tracker_row and not args.dry_run:
            if not tracker_row.get("converted_r", "").strip():
                tracker_row["converted_r"]        = log["converted_r"]
                tracker_row["conversion_formula"] = conv
                tracker_row["sample_size_n"]      = log["sample_size_n"]
                tracker_row["t_value"]            = log["t_value"]
                tracker_row["p_value"]            = log["p_value"]
                tracker_row["effect_direction"]   = log["effect_direction"]
                if "curve_type" in tracker_row:
                    tracker_row["curve_type"]     = log["curve_type"]
                notes_key = "notes_for_extractor"
                if notes_key in tracker_row:
                    existing_note = tracker_row.get(notes_key, "")
                    tracker_row[notes_key] = (
                        existing_note + " | GROQ: " + log["notes"]
                    ).strip(" |")
                if "ready_for_r" in tracker_row and not tracker_row.get("ready_for_r","").strip():
                    tracker_row["ready_for_r"] = "1"
                updated += 1

        if i % 10 == 0:
            print(f"  progress: {i}/{len(pending)} | extracted={updated} "
                  f"no_pdf={no_pdf} not_found={not_found}", flush=True)

    # ── Write tracker ────────────────────────────────────────────────────────
    if not args.dry_run and updated:
        with open(tracker_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(tracker_rows)
        print(f"\nTracker updated: {tracker_path} ({updated} rows)")
    elif args.dry_run:
        print(f"\nDRY RUN — tracker NOT modified ({updated} would be updated)")

    # ── Write log ─────────────────────────────────────────────────────────────
    log_path = Path(args.log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_cols = ["seq", "doi", "title", "status", "converted_r", "conversion_formula",
                "sample_size_n", "t_value", "p_value", "effect_direction", "curve_type", "notes"]
    with open(log_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=log_cols)
        w.writeheader()
        w.writerows(log_entries)

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n=== GROQ r-EXTRACTION SUMMARY ===")
    print(f"Model:            {args.model}")
    print(f"Papers attempted: {len(pending)}")
    print(f"r extracted:      {updated}" + (" (DRY RUN)" if args.dry_run else ""))
    print(f"No PDF:           {no_pdf}")
    print(f"No text (scan):   {no_text}")
    print(f"No I→P coeff:     {not_found}")
    print(f"API errors:       {api_errors}")
    print(f"Skipped (manual): {skipped_manual}")
    print(f"Log:              {log_path}")

    if auth_failed:
        print("\nFATAL: the Groq API key is invalid (401). No papers could be"
              " processed.\nGet a fresh key at console.groq.com, set it via the"
              " GROQ_API_KEY secret or the\ngroq_api_key run input, then re-run.")
        sys.exit(1)
    print(f"\nNEXT: Review GROQ: entries in notes_for_extractor, then set ready_for_r=1")


if __name__ == "__main__":
    main()
