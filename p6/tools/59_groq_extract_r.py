#!/usr/bin/env python3
"""
59_groq_extract_r.py — Batch r-extraction using Groq FREE API (llama-3.3-70b)

PDF resolution order:
  1. Local PDF already in pdf_dir (pdf_filename column)
  2. OA manifest (oa_manifest_*.csv) keyed by seq
  3. source_url_or_pdf_path column in queue
  4. Unpaywall API (free, email-based) — best_oa_location.url_for_pdf
  5. Semantic Scholar openAccessPdf

Cách lấy Groq API key miễn phí:
  1. Vào console.groq.com → Sign up (chỉ cần email)
  2. API Keys → Create API Key
  3. Set env var: set GROQ_API_KEY=gsk_xxxxxx  (Windows CMD)

Cách chạy (Windows CMD):
  cd C:\\path\\to\\PAPERS_IN_PHD_2026
  pip install groq pdfplumber requests
  set GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx
  python p6\\tools\\59_groq_extract_r.py --limit 50

Chạy thử trước (không ghi tracker):
  python p6\\tools\\59_groq_extract_r.py --limit 5 --dry-run

Dependencies: pip install groq pdfplumber requests
"""
import csv, json, math, os, re, sys, time, argparse
from datetime import date
from pathlib import Path

try:
    from groq import Groq
except ImportError:
    print("ERROR: pip install groq"); sys.exit(1)

try:
    import pdfplumber
except ImportError:
    print("ERROR: pip install pdfplumber"); sys.exit(1)

import requests

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE    = Path(__file__).resolve().parents[2]
TODAY   = date.today().strftime('%Y%m%d')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
DEFAULT_QUEUE   = BASE / f'p6/tools/results/extraction_queue_v2_20260521.csv'
DEFAULT_PDF_DIR = BASE / 'p6/pdfs'
DEFAULT_LOG     = BASE / f'p6/tools/results/groq_extract_log_{TODAY}.csv'

MAX_TEXT_CHARS   = 24_000
GROQ_MODEL       = 'llama-3.3-70b-versatile'
DOWNLOAD_TIMEOUT = 30
SLEEP_BETWEEN    = 1.2   # Groq free: 30 req/min
SLEEP_UNPAYWALL  = 0.5   # be polite to Unpaywall
UNPAYWALL_EMAIL  = 'huongdt@vlute.edu.vn'

# ── Math helpers ───────────────────────────────────────────────────────────────
def r_from_t(t: float, n: int) -> float:
    df = max(n - 2, 1)
    return t / math.sqrt(t**2 + df)

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
            headers={'User-Agent': 'Mozilla/5.0 (meta-analysis-research; huongdt@vlute.edu.vn)'}
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

def try_unpaywall(doi: str) -> str:
    """Return best OA PDF URL from Unpaywall, or empty string."""
    if not doi:
        return ''
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email={UNPAYWALL_EMAIL}"
        resp = requests.get(url, timeout=10,
                            headers={'User-Agent': f'meta-analysis-research {UNPAYWALL_EMAIL}'})
        if resp.status_code != 200:
            return ''
        data = resp.json()
        best = data.get('best_oa_location') or {}
        return best.get('url_for_pdf') or best.get('url') or ''
    except Exception:
        return ''

def try_semantic_scholar(doi: str) -> str:
    """Return OA PDF URL from Semantic Scholar."""
    if not doi:
        return ''
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}?fields=openAccessPdf"
        resp = requests.get(url, timeout=10,
                            headers={'User-Agent': f'meta-analysis-research {UNPAYWALL_EMAIL}'})
        if resp.status_code != 200:
            return ''
        data = resp.json()
        oa = data.get('openAccessPdf') or {}
        return oa.get('url') or ''
    except Exception:
        return ''

def pdf_to_text(pdf_path: Path, max_chars: int = MAX_TEXT_CHARS) -> str:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            parts = []
            total = 0
            for page in pdf.pages:
                t = page.extract_text() or ''
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

# ── Groq extraction prompt ─────────────────────────────────────────────────────
SYSTEM_PROMPT = """\
You are a meta-analysis research assistant. Extract the Pearson r effect size
(or a convertible statistic) for the internationalization → firm performance (I→P)
relationship from the full text of an empirical paper.

INTERNATIONALIZATION (IV): FSTS, export intensity, export ratio, degree of internationalization (DOI),
number of foreign countries, foreign sales, multinationality, FDI stock, geographic scope.

PERFORMANCE (DV): ROA, ROE, ROS, Tobin's Q, sales growth, profit margin, productivity (TFP/LP).

EXTRACTION PRIORITY (use first available):
1. Pearson r direct → use as-is
2. Partial correlation → use as-is (flag is_partial=true)
3. Standardized β (OLS/panel, firm-level) → r ≈ β (flag is_estimated=true)
4. t-statistic + N → r = t / sqrt(t² + (N-2))
5. F-statistic (df1=1) + N → r = sqrt(F / (F + (N-2)))
6. p-value + N only → skip (insufficient)

RULES:
- Extract coefficient for MAIN I→P linear term (β1 if quadratic model)
- Use FULL model (most controls) if multiple models reported
- Never invent numbers. If no convertible stat exists, return r=null
- N = firm-year observations for panel data

RESPOND WITH ONLY VALID JSON (no markdown, no explanation):
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
  "model_type": "<OLS|panel_FE|panel_RE|GMM|other>",
  "icrv_hint": "<country or multi>",
  "effect_direction": "<positive|negative|unclear>",
  "notes": "<max 200 chars>"
}"""

def extract_r_via_groq(client: Groq, text: str, title: str, model: str) -> dict:
    user_msg = f"Paper title: {title}\n\nFull text (truncated to {MAX_TEXT_CHARS} chars):\n\n{text}"
    try:
        resp = client.chat.completions.create(
            model=model,
            max_tokens=512,
            temperature=0.0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_msg},
            ]
        )
        raw = resp.choices[0].message.content.strip()
        raw = re.sub(r'^```(?:json)?\s*', '', raw)
        raw = re.sub(r'\s*```$', '', raw)
        return json.loads(raw)
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse: {e}", "r": None}
    except Exception as e:
        return {"error": str(e), "r": None}

def compute_final_r(result: dict) -> tuple:
    r = result.get('r')
    if r is not None:
        try:
            r = float(r)
            if abs(r) <= 1.0:
                return r, result.get('conversion_formula', 'direct')
        except (ValueError, TypeError):
            pass
    return None, 'none'

def load_oa_manifest(manifest_path: Path) -> dict:
    manifest = {}
    if not manifest_path.exists():
        return manifest
    with open(manifest_path, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            seq = row.get('seq', '').strip()
            pdf_url = row.get('pdf_url', '').strip()
            if seq and pdf_url:
                manifest[seq] = pdf_url
    return manifest

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='Groq-based r-extraction (free API)')
    parser.add_argument('--queue',    default=str(DEFAULT_QUEUE))
    parser.add_argument('--tracker',  default=str(TRACKER))
    parser.add_argument('--pdf-dir',  default=str(DEFAULT_PDF_DIR))
    parser.add_argument('--manifest', default=None,
                        help='OA manifest CSV (oa_manifest_*.csv or s2_manifest_*.csv)')
    parser.add_argument('--log',      default=str(DEFAULT_LOG))
    parser.add_argument('--limit',    type=int, default=50)
    parser.add_argument('--dry-run',  action='store_true')
    parser.add_argument('--model',    default=GROQ_MODEL)
    parser.add_argument('--no-unpaywall', action='store_true',
                        help='Skip Unpaywall/S2 fallback lookup')
    args = parser.parse_args()

    api_key = os.environ.get('GROQ_API_KEY', '')
    if not api_key:
        print("ERROR: set GROQ_API_KEY env var first")
        print("  Get free key: https://console.groq.com → API Keys")
        sys.exit(1)

    client = Groq(api_key=api_key)
    pdf_dir = Path(args.pdf_dir)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    # Load manifests
    manifest = {}
    if args.manifest:
        manifest.update(load_oa_manifest(Path(args.manifest)))
    # Also try default manifest paths
    for mf in [BASE / 's2_manifest_20260521.csv',
                BASE / 'p6/tools/results/s2_manifest_20260521.csv',
                BASE / 'p6/tools/results/oa_manifest_20260521.csv']:
        if mf.exists() and not manifest:
            manifest.update(load_oa_manifest(mf))

    # Load tracker to know which seqs already have r
    with open(args.tracker, encoding='utf-8') as f:
        tracker_rows = list(csv.DictReader(f))
    tracker_fieldnames = list(tracker_rows[0].keys())
    tracker_by_seq = {r['seq']: r for r in tracker_rows}
    already_done = {r['seq'] for r in tracker_rows if r.get('converted_r', '').strip()}

    # Load queue
    with open(args.queue, encoding='utf-8') as f:
        queue = list(csv.DictReader(f))

    candidates = [
        r for r in queue
        if r.get('seq', '') not in already_done
        and r.get('fulltext_screening_decision', '') != 'N'
    ][:args.limit]

    use_unpaywall = not args.no_unpaywall
    print(f"Queue: {len(queue)} | Already done: {len(already_done)} | "
          f"To process: {len(candidates)} (limit={args.limit})")
    print(f"Model: {args.model} | Dry-run: {args.dry_run} | "
          f"Unpaywall fallback: {use_unpaywall}\n")

    log_rows = []
    updated = 0

    for i, qrow in enumerate(candidates, 1):
        seq   = qrow.get('seq', '')
        title = qrow.get('title', '')[:100]
        doi   = qrow.get('doi', '').strip()
        src   = qrow.get('source_url_or_pdf_path', '').strip()
        year  = qrow.get('year', '')

        print(f"[{i}/{len(candidates)}] seq={seq} | {title[:60]}...")

        # ── Resolve PDF ────────────────────────────────────────────────────────
        pdf_path = None
        pdf_source = ''

        # 1. Local PDF (pdf_filename column or already downloaded)
        local_pdf = qrow.get('pdf_filename', '').strip()
        if local_pdf:
            candidate = pdf_dir / local_pdf
            if candidate.exists():
                pdf_path = candidate
                pdf_source = 'local'

        # 2. OA manifest (keyed by seq)
        if pdf_path is None:
            manifest_url = manifest.get(seq, '')
            if manifest_url:
                safe_name = re.sub(r'[^\w\-.]', '_', seq) + '.pdf'
                dest = pdf_dir / safe_name
                if download_pdf(manifest_url, dest):
                    pdf_path = dest
                    pdf_source = 'manifest'
                    print(f"  Manifest URL OK: {manifest_url[:70]}")

        # 3. source_url_or_pdf_path from queue
        if pdf_path is None and src and src.startswith('http'):
            safe_name = re.sub(r'[^\w\-.]', '_', seq) + '_src.pdf'
            dest = pdf_dir / safe_name
            if download_pdf(src, dest):
                pdf_path = dest
                pdf_source = 'queue_url'
                print(f"  Queue URL OK: {src[:70]}")

        # 4. Unpaywall fallback (by DOI)
        if pdf_path is None and doi and use_unpaywall:
            time.sleep(SLEEP_UNPAYWALL)
            unp_url = try_unpaywall(doi)
            if unp_url and unp_url.startswith('http'):
                safe_name = re.sub(r'[^\w\-.]', '_', seq) + '_unp.pdf'
                dest = pdf_dir / safe_name
                if download_pdf(unp_url, dest):
                    pdf_path = dest
                    pdf_source = 'unpaywall'
                    print(f"  Unpaywall OK: {unp_url[:70]}")
                else:
                    print(f"  Unpaywall URL found but download failed: {unp_url[:60]}")
            else:
                print(f"  Unpaywall: no OA PDF for doi={doi[:40]}")

        # 5. Semantic Scholar fallback
        if pdf_path is None and doi and use_unpaywall:
            s2_url = try_semantic_scholar(doi)
            if s2_url and s2_url.startswith('http'):
                safe_name = re.sub(r'[^\w\-.]', '_', seq) + '_s2.pdf'
                dest = pdf_dir / safe_name
                if download_pdf(s2_url, dest):
                    pdf_path = dest
                    pdf_source = 'semantic_scholar'
                    print(f"  Semantic Scholar OK: {s2_url[:70]}")

        if pdf_path is None:
            print(f"  SKIP: no PDF available (manifest={bool(manifest.get(seq))}, "
                  f"doi={bool(doi)}, unpaywall={use_unpaywall})")
            log_rows.append({'seq': seq, 'title': title, 'year': year,
                             'doi': doi, 'pdf_url': src or manifest.get(seq, ''),
                             'status': 'NO_PDF', 'converted_r': '', 'n': '',
                             'conversion_formula': '', 'notes': '', 'error': ''})
            continue

        # ── Extract text ───────────────────────────────────────────────────────
        text = pdf_to_text(pdf_path)
        if text.startswith('PDF_READ_ERROR'):
            print(f"  SKIP: {text}")
            log_rows.append({'seq': seq, 'title': title, 'year': year,
                             'doi': doi, 'pdf_url': src or manifest.get(seq, ''),
                             'status': 'PDF_ERROR', 'converted_r': '', 'n': '',
                             'conversion_formula': '', 'notes': '', 'error': text})
            continue

        if args.dry_run:
            print(f"  [DRY-RUN] PDF text {len(text)} chars from {pdf_source} — would send to Groq")
            log_rows.append({'seq': seq, 'title': title, 'year': year,
                             'doi': doi, 'pdf_url': pdf_source,
                             'status': 'DRY_RUN', 'converted_r': '', 'n': '',
                             'conversion_formula': '', 'notes': '', 'error': ''})
            continue

        # ── Call Groq ──────────────────────────────────────────────────────────
        result = extract_r_via_groq(client, text, title, args.model)

        if 'error' in result:
            print(f"  ERROR: {result['error']}")
            log_rows.append({'seq': seq, 'title': title, 'year': year,
                             'doi': doi, 'pdf_url': pdf_source,
                             'status': 'API_ERROR', 'converted_r': '', 'n': '',
                             'conversion_formula': '', 'notes': '', 'error': result['error']})
            time.sleep(SLEEP_BETWEEN)
            continue

        final_r, formula = compute_final_r(result)
        n_val = result.get('n')

        if final_r is None:
            print(f"  NO_R: {result.get('notes', '')[:80]}")
            status = 'NO_R_FOUND'
        else:
            print(f"  r={final_r:.4f} | n={n_val} | formula={formula} | "
                  f"iv={result.get('iv_measure','')} | dv={result.get('dv_measure','')}")
            status = 'SUCCESS'
            updated += 1

            # Update tracker row
            trow = tracker_by_seq.get(seq)
            if trow and not trow.get('converted_r', '').strip():
                trow['converted_r']        = str(round(final_r, 6))
                trow['conversion_formula'] = formula
                trow['ready_for_r']        = '1'
                if n_val:
                    trow['sample_size_n'] = str(n_val)
                    trow['fisher_z']      = str(round(fisher_z(final_r), 6))
                    trow['variance_z']    = str(round(variance_z(int(n_val)), 8))
                if result.get('t_stat'):
                    trow['t_value'] = str(result['t_stat'])
                if result.get('p_value'):
                    trow['p_value'] = str(result['p_value'])
                if result.get('beta'):
                    trow['reported_coefficient'] = str(result['beta'])
                if result.get('se'):
                    trow['standard_error'] = str(result['se'])
                notes_add = result.get('notes', '')
                if notes_add:
                    existing = trow.get('notes_for_extractor', '')
                    trow['notes_for_extractor'] = (existing + ' | ' + notes_add).strip(' | ')
                trow['extracted_by'] = f'groq-{args.model[:20]}'

        log_rows.append({
            'seq': seq, 'title': title, 'year': year, 'doi': doi,
            'pdf_url': pdf_source, 'status': status,
            'converted_r': str(final_r) if final_r else '',
            'n': str(n_val) if n_val else '',
            'conversion_formula': formula,
            'notes': result.get('notes', ''),
            'error': result.get('error', '')
        })

        time.sleep(SLEEP_BETWEEN)

    # ── Write outputs ──────────────────────────────────────────────────────────
    if not args.dry_run and updated > 0:
        with open(args.tracker, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=tracker_fieldnames)
            w.writeheader()
            w.writerows(tracker_rows)
        print(f"\nTracker updated: {updated} rows → {args.tracker}")

    log_path = Path(args.log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['seq','title','year','doi','pdf_url',
                                          'status','converted_r','n',
                                          'conversion_formula','notes','error'])
        w.writeheader()
        w.writerows(log_rows)

    print(f"\n{'='*60}")
    print(f"Processed: {len(candidates)} | Updated: {updated} | Log: {log_path}")

    from collections import Counter
    counts = Counter(r['status'] for r in log_rows)
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

if __name__ == '__main__':
    main()
