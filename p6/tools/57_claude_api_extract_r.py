#!/usr/bin/env python3
"""
57_claude_api_extract_r.py — Claude API batch r-extraction from PDF text

For each Y paper in the extraction queue:
  1. Resolves PDF URL via Unpaywall manifest (if available)
  2. Downloads PDF + converts to text (pdfplumber)
  3. Sends PDF text to Claude claude-haiku-4-5-20251001 with structured extraction prompt
  4. Parses structured JSON response: r, n, SE, t, p, conversion_formula, notes
  5. Validates and writes to tracker (only rows where converted_r is empty)

Usage:
  # Requires ANTHROPIC_API_KEY env var
  python3 p6/tools/57_claude_api_extract_r.py
  python3 p6/tools/57_claude_api_extract_r.py --limit 20 --dry-run
  python3 p6/tools/57_claude_api_extract_r.py --pdf-dir p6/pdfs/ --queue p6/tools/results/extraction_queue_v2_20260521.csv

Dependencies: pip install anthropic pdfplumber requests
"""
import csv, json, math, os, re, sys, time, argparse, hashlib
from datetime import date
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: pip install anthropic"); sys.exit(1)

try:
    import pdfplumber
except ImportError:
    print("ERROR: pip install pdfplumber"); sys.exit(1)

import requests

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE    = Path('/home/user/PAPERS_IN_PHD_2026')
TODAY   = date.today().strftime('%Y%m%d')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
DEFAULT_QUEUE   = BASE / f'p6/tools/results/extraction_queue_v2_{TODAY}.csv'
DEFAULT_PDF_DIR = BASE / 'p6/pdfs'
DEFAULT_MANIFEST = BASE / f'p6/tools/results/oa_manifest_{TODAY}.csv'
DEFAULT_LOG      = BASE / f'p6/tools/results/claude_extract_log_{TODAY}.csv'

MAX_TEXT_CHARS = 28_000   # ~7k tokens; leave room for system+output
HAIKU_MODEL    = 'claude-haiku-4-5-20251001'
DOWNLOAD_TIMEOUT = 25
SLEEP_BETWEEN  = 0.5

# ── Effect-size conversion helpers ────────────────────────────────────────────
def r_from_t(t: float, n: int) -> float:
    df = max(n - 2, 1)
    return t / math.sqrt(t**2 + df)

def r_from_beta_std(beta: float) -> float:
    """Approximation: standardised β ≈ r in simple bivariate OLS"""
    return beta

def fisher_z(r: float) -> float:
    r = max(min(r, 0.9999), -0.9999)
    return 0.5 * math.log((1 + r) / (1 - r))

def variance_z(n: int) -> float:
    return 1.0 / max(n - 3, 1)

# ── PDF utilities ──────────────────────────────────────────────────────────────
def download_pdf(url: str, dest: Path, timeout: int = DOWNLOAD_TIMEOUT) -> bool:
    if dest.exists() and dest.stat().st_size > 5_000:
        return True
    try:
        resp = requests.get(
            url, timeout=timeout, stream=True,
            headers={'User-Agent': 'Mozilla/5.0 (meta-analysis; huongdt@vlute.edu.vn)'}
        )
        if resp.status_code != 200:
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, 'wb') as f:
            for chunk in resp.iter_content(65_536):
                f.write(chunk)
        return dest.stat().st_size > 5_000
    except Exception:
        return False

def pdf_to_text(pdf_path: Path, max_chars: int = MAX_TEXT_CHARS) -> str:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            parts = []
            total = 0
            for page in pdf.pages:
                t = page.extract_text() or ''
                # Also try to extract tables
                for tbl in page.extract_tables() or []:
                    for row in tbl:
                        if row:
                            parts.append(' | '.join(str(c or '') for c in row))
                parts.append(t)
                total += len(t)
                if total >= max_chars:
                    break
            return '\n'.join(parts)[:max_chars]
    except Exception as e:
        return f"PDF_READ_ERROR: {e}"

# ── Claude prompt ──────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """\
You are a meta-analysis research assistant. Your task: extract the Pearson r effect size
(or a convertible statistic) for the internationalization → firm performance (I→P) relationship
from the full text of an empirical paper.

DEFINITIONS
- Internationalization (I) IV: FSTS, export intensity, export ratio, degree of internationalization (DOI),
  number of foreign countries, foreign sales, multinationality, FDI stock/outward FDI, geographic scope.
- Performance (P) DV: ROA, ROE, ROS, Tobin's Q, sales growth, profit margin, productivity (TFP/LP), market return.

EXTRACTION PRIORITY (use the FIRST available)
1. Pearson r reported directly → use as-is.
2. Partial correlation → use as-is (flag is_partial=true).
3. Standardized β (OLS/panel, firm-level) → r ≈ β (flag is_estimated=true).
4. t-statistic + sample N → r = t / sqrt(t² + (N−2)).
5. F-statistic (df₁=1) + N → r = sqrt(F / (F + (N−2))).
6. p-value + N only → skip (insufficient).

RULES
- Extract the coefficient for the MAIN I→P term (linear, or β₁ if quadratic).
  If quadratic relationship found, also note β₂ and turning_point in notes.
- Use the FULL model (most controls) if multiple models reported.
- Never invent numbers. If no convertible stat exists, return r=null.
- Sample N = number of firm-year observations (or firms if cross-section).
- For panel data, N = observations (not unique firms).

OUTPUT: respond with ONLY valid JSON, no markdown, no explanation:
{
  "r": <float|null>,
  "n": <int|null>,
  "beta": <float|null>,
  "se": <float|null>,
  "t_stat": <float|null>,
  "p_value": <float|null>,
  "is_estimated": <bool>,
  "is_partial": <bool>,
  "conversion_formula": "direct|beta|t_to_r|F_to_r|none",
  "iv_measure": "<FSTS|DOI|export|FDI|entropy|n_countries|other>",
  "dv_measure": "<ROA|ROE|ROS|TobinQ|sales_growth|productivity|other>",
  "model_type": "<OLS|panel_FE|panel_RE|GMM|logit|other>",
  "icrv_hint": "<country or 'multi'>",
  "effect_direction": "<positive|negative|unclear>",
  "notes": "<max 200 chars — quadratic terms, turning point, control variables, sample details>"
}
"""

def extract_r_via_claude(client, text: str, title: str) -> dict:
    user_msg = f"Paper title: {title}\n\nFull text (truncated):\n\n{text}"
    try:
        msg = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )
        raw = msg.content[0].text.strip()
        # Strip markdown code fences if present
        raw = re.sub(r'^```(?:json)?\s*', '', raw)
        raw = re.sub(r'\s*```$', '', raw)
        return json.loads(raw)
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse: {e}", "r": None}
    except Exception as e:
        return {"error": str(e), "r": None}

# ── Validate and convert result ────────────────────────────────────────────────
def compute_final_r(result: dict, title: str) -> tuple[float | None, str]:
    """Return (converted_r, conversion_formula) from Claude JSON result."""
    r = result.get('r')
    if r is not None:
        try:
            r = float(r)
            if abs(r) <= 1.0:
                return r, result.get('conversion_formula', 'direct')
        except (ValueError, TypeError):
            pass
    return None, 'none'

# ── Manifest / URL resolution ──────────────────────────────────────────────────
def load_oa_manifest(manifest_path: Path) -> dict:
    """Returns {seq: pdf_url} from Unpaywall/S2 manifest."""
    manifest = {}
    if not manifest_path.exists():
        return manifest
    with open(manifest_path) as f:
        for row in csv.DictReader(f):
            seq = row.get('seq','').strip()
            pdf_url = row.get('pdf_url','').strip()
            if seq and pdf_url:
                manifest[seq] = pdf_url
    return manifest

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--queue',    default=str(DEFAULT_QUEUE))
    parser.add_argument('--tracker',  default=str(TRACKER))
    parser.add_argument('--manifest', default=str(DEFAULT_MANIFEST))
    parser.add_argument('--pdf-dir',  default=str(DEFAULT_PDF_DIR))
    parser.add_argument('--log',      default=str(DEFAULT_LOG))
    parser.add_argument('--limit',    type=int, default=0)
    parser.add_argument('--dry-run',  action='store_true')
    parser.add_argument('--no-download', action='store_true',
                        help='Only process pre-existing PDFs in pdf-dir')
    args = parser.parse_args()

    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if not api_key and not args.dry_run:
        print("ERROR: ANTHROPIC_API_KEY not set."); sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key) if not args.dry_run else None

    pdf_dir  = Path(args.pdf_dir);  pdf_dir.mkdir(parents=True, exist_ok=True)
    oa_map   = load_oa_manifest(Path(args.manifest))
    print(f"OA manifest loaded: {len(oa_map)} PDF URLs")

    # Load queue
    if not Path(args.queue).exists():
        print(f"ERROR: queue not found: {args.queue}"); sys.exit(1)
    with open(args.queue) as f:
        queue = list(csv.DictReader(f))
    print(f"Queue: {len(queue)} papers")

    # Load tracker into dict for updates
    with open(args.tracker) as f:
        tracker_rows = list(csv.DictReader(f))
        fieldnames = list(tracker_rows[0].keys())
    tracker_by_seq = {r['seq']: r for r in tracker_rows}

    # Process
    log_rows = []
    processed = 0
    errors = 0

    for row in queue:
        if args.limit and processed >= args.limit:
            break

        seq   = row.get('seq','').strip()
        title = row.get('title','').strip()
        doi   = row.get('doi','').strip()
        year  = row.get('year','').strip()

        # Skip if already has r
        tr = tracker_by_seq.get(seq)
        if tr and tr.get('converted_r','').strip():
            continue

        # Determine PDF source
        pdf_filename = f"{seq}_{year}.pdf"
        pdf_path = pdf_dir / pdf_filename

        # Try: 1) local PDF exists, 2) OA manifest URL, 3) source_url in queue
        url = None
        if pdf_path.exists() and pdf_path.stat().st_size > 5_000:
            url = None  # use existing
        elif seq in oa_map:
            url = oa_map[seq]
        else:
            url = row.get('source_url_or_pdf_path','').strip()
            if not url:
                url = row.get('doi_link','').strip()

        log_row = {
            'seq': seq, 'title': title[:80], 'year': year, 'doi': doi,
            'pdf_url': url or '', 'status': '', 'converted_r': '', 'n': '',
            'conversion_formula': '', 'notes': '', 'error': ''
        }

        # Download PDF if needed
        if url and not (pdf_path.exists() and pdf_path.stat().st_size > 5_000):
            if not args.no_download and not args.dry_run:
                ok = download_pdf(url, pdf_path)
                log_row['status'] = 'DL_OK' if ok else 'DL_FAIL'
                if not ok:
                    log_row['error'] = 'download failed'
                    log_rows.append(log_row)
                    errors += 1
                    continue
            elif args.dry_run:
                log_row['status'] = 'DRY_RUN'
                log_rows.append(log_row)
                processed += 1
                continue
            else:
                log_row['status'] = 'SKIP_NO_LOCAL'
                log_rows.append(log_row)
                continue
        elif not pdf_path.exists():
            log_row['status'] = 'SKIP_NO_PDF'
            log_rows.append(log_row)
            continue

        # Extract text
        text = pdf_to_text(pdf_path)
        if text.startswith('PDF_READ_ERROR'):
            log_row['status'] = 'READ_ERROR'
            log_row['error'] = text
            log_rows.append(log_row)
            errors += 1
            continue

        # Claude extraction
        if args.dry_run:
            log_row['status'] = 'DRY_RUN_EXTRACT'
            log_rows.append(log_row)
            processed += 1
            continue

        result = extract_r_via_claude(client, text, title)

        if 'error' in result and result.get('r') is None:
            log_row['status'] = 'CLAUDE_ERROR'
            log_row['error'] = result.get('error', '')[:120]
            log_rows.append(log_row)
            errors += 1
            time.sleep(SLEEP_BETWEEN)
            continue

        final_r, conv_formula = compute_final_r(result, title)
        n = result.get('n')
        try:
            n = int(n) if n is not None else None
        except (ValueError, TypeError):
            n = None

        # Update tracker
        if tr and final_r is not None:
            tr['converted_r']       = str(round(final_r, 6))
            tr['conversion_formula']= conv_formula
            tr['ready_for_r']       = '1'
            if n:
                tr['sample_size_n'] = str(n)
            if n and n > 3:
                fz = fisher_z(final_r)
                vz = variance_z(n)
                tr['fisher_z']   = str(round(fz, 6))
                tr['variance_z'] = str(round(vz, 8))
            tr['effect_size_type']  = result.get('conversion_formula', '')
            tr['reported_coefficient'] = str(result.get('beta') or result.get('r') or '')
            tr['t_value']           = str(result.get('t_stat') or '')
            tr['p_value']           = str(result.get('p_value') or '')
            tr['effect_direction']  = result.get('effect_direction', '')
            notes = result.get('notes','')
            if result.get('iv_measure'):
                notes += f" | IV={result['iv_measure']}"
            if result.get('dv_measure'):
                notes += f" | DV={result['dv_measure']}"
            tr['notes_for_extractor'] = notes[:250]
            if result.get('icrv_hint') and not tr.get('icrv','').strip():
                # Don't overwrite existing ICRV
                pass
            tr['pdf_filename'] = str(pdf_path.name)

        log_row.update({
            'status': 'OK' if final_r is not None else 'NO_R_FOUND',
            'converted_r': str(final_r) if final_r is not None else '',
            'n': str(n or ''),
            'conversion_formula': conv_formula,
            'notes': result.get('notes','')[:120],
        })
        log_rows.append(log_row)
        processed += 1

        if processed % 10 == 0:
            print(f"  [{processed}] done (errors={errors})")

        time.sleep(SLEEP_BETWEEN)

    # Write back tracker
    if not args.dry_run:
        with open(args.tracker, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(tracker_rows)
        print(f"\nTracker updated: {args.tracker}")

    # Write log
    log_path = Path(args.log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_cols = ['seq','title','year','doi','pdf_url','status','converted_r','n',
                'conversion_formula','notes','error']
    with open(log_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=log_cols)
        w.writeheader()
        w.writerows(log_rows)

    # Summary
    ok     = sum(1 for r in log_rows if r['status']=='OK')
    no_r   = sum(1 for r in log_rows if r['status']=='NO_R_FOUND')
    dl_ok  = sum(1 for r in log_rows if r['status']=='DL_OK')
    skips  = sum(1 for r in log_rows if 'SKIP' in r['status'])
    print(f"\n{'='*50}")
    print(f"Processed:   {processed}")
    print(f"r extracted: {ok}")
    print(f"No r found:  {no_r}")
    print(f"DL ok:       {dl_ok}")
    print(f"Skipped:     {skips}")
    print(f"Errors:      {errors}")
    print(f"Log: {log_path}")

if __name__ == '__main__':
    main()
