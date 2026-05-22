#!/usr/bin/env python3
"""
59_groq_extract_r.py — Batch r-extraction using Groq FREE API (llama-3.3-70b)

PDF resolution order per paper:
  1. Local PDF already in pdf_dir (pdf_filename column)
  2. OA manifest (oa_manifest_*.csv) keyed by seq
  3. source_url_or_pdf_path column in queue
  4. Unpaywall API (free, email-based) — best_oa_location.url_for_pdf
  5. Semantic Scholar openAccessPdf

Candidate selection order (maximise PDF hit rate):
  Priority 0 — seq in OA manifest (guaranteed PDF URL)
  Priority 1 — queue source_url_or_pdf_path starts with http
  Priority 2 — local pdf_filename exists
  Priority 3 — needs Unpaywall/S2 lookup on-the-fly

Effect-size conversion paths (in priority order):
  1.  Pearson r direct
  2.  Partial correlation r (flag is_partial=true)
  3.  Standardized β → r ≈ β
  4.  t-statistic + N → r = t / sqrt(t²+(N-2))
  5.  F-statistic (df1=1) + N → r = sqrt(F/(F+(N-2)))
  6.  Chi-square (df=1) + N → r = sqrt(χ²/N)
  7.  Cohen's d → r = d / sqrt(d²+4)
  8.  η² or partial η² → r = sqrt(η²)
  9.  Log-odds ratio → r via logit-probit: r = log_or·√3/π / sqrt(1+(log_or·√3/π)²)
  10. Z-score + N → r = z / sqrt(N)
  11. Unstandardized b + SE_b → t = b/SE_b → r

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
SLEEP_UNPAYWALL  = 0.5
UNPAYWALL_EMAIL  = 'huongdt@vlute.edu.vn'

# ── Effect-size math ───────────────────────────────────────────────────────────
def r_from_t(t: float, n: int) -> float:
    df = max(n - 2, 1)
    return t / math.sqrt(t**2 + df)

def r_from_F(F: float, n: int) -> float:
    df_e = max(n - 2, 1)
    return math.sqrt(F / (F + df_e))

def r_from_chi2(chi2: float, n: int) -> float:
    return math.sqrt(chi2 / max(n, 1))

def r_from_d(d: float) -> float:
    return d / math.sqrt(d**2 + 4)

def r_from_eta_sq(eta_sq: float) -> float:
    return math.sqrt(max(eta_sq, 0.0))

def r_from_log_or(log_or: float) -> float:
    # logit-probit approximation (Borenstein 2009 appendix B)
    x = log_or * math.sqrt(3) / math.pi
    return x / math.sqrt(1 + x**2)

def r_from_z(z: float, n: int) -> float:
    return z / math.sqrt(max(n, 1))

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
You are a meta-analysis research assistant. Extract ANY statistic that can be converted
to Pearson r for the internationalization → firm performance (I→P) relationship.

INTERNATIONALIZATION (IV): FSTS, export intensity, export ratio, degree of internationalization (DOI),
number of foreign countries, foreign sales, multinationality, FDI stock, geographic scope.

PERFORMANCE (DV): ROA, ROE, ROS, Tobin's Q, sales growth, profit margin, productivity (TFP/LP).

EXTRACTION PRIORITY — use the FIRST available:
  1.  Pearson r (direct correlation)                    → r as-is
  2.  Partial correlation r                             → r as-is, is_partial=true
  3.  Standardized β (OLS / panel)                      → r ≈ β, is_estimated=true
  4.  t-statistic + N                                   → r = t/sqrt(t²+(N-2))
  5.  F-statistic (df1=1) + N                           → r = sqrt(F/(F+(N-2)))
  6.  Chi-square (df=1) + N                             → r = sqrt(χ²/N)
  7.  Cohen's d                                         → r = d/sqrt(d²+4)
  8.  η² or partial η²                                  → r = sqrt(η²)
  9.  Log-odds ratio (logit coefficient)                → r ≈ log_or·√3/π / sqrt(1+(log_or·√3/π)²)
  10. Z-score + N                                       → r = z/sqrt(N)
  11. Unstandardized b + SE_b (→ t=b/SE → r)           → conversion_formula="b_se_to_r"

RULES:
- Always use the FULL model (most control variables) if multiple models shown.
- For quadratic I→P models, extract the LINEAR term (β₁ / coefficient on I, not I²).
- N = firm-year observations for panel data; firm count for cross-section.
- Never invent numbers. If no convertible statistic exists, return r=null.
- Report the raw statistic in the matching field even when you compute r.

RESPOND WITH ONLY VALID JSON (no markdown, no explanation):
{
  "r": <float|null>,
  "n": <int|null>,
  "beta": <float|null>,
  "se": <float|null>,
  "t_stat": <float|null>,
  "f_stat": <float|null>,
  "chi_sq": <float|null>,
  "cohen_d": <float|null>,
  "eta_sq": <float|null>,
  "log_or": <float|null>,
  "z_score": <float|null>,
  "b_unstand": <float|null>,
  "se_b": <float|null>,
  "p_value": <float|null>,
  "is_estimated": <bool>,
  "is_partial": <bool>,
  "conversion_formula": "direct|beta|t_to_r|F_to_r|chi2_to_r|d_to_r|eta_to_r|log_or_to_r|z_to_r|b_se_to_r|none",
  "iv_measure": "<FSTS|DOI|export|FDI|entropy|n_countries|other>",
  "dv_measure": "<ROA|ROE|ROS|TobinQ|sales_growth|productivity|other>",
  "model_type": "<OLS|panel_FE|panel_RE|GMM|logit|probit|other>",
  "icrv_hint": "<country or multi>",
  "effect_direction": "<positive|negative|unclear>",
  "notes": "<max 200 chars>"
}"""

def extract_r_via_groq(client: Groq, text: str, title: str, model: str) -> dict:
    user_msg = f"Paper title: {title}\n\nFull text (truncated to {MAX_TEXT_CHARS} chars):\n\n{text}"
    try:
        resp = client.chat.completions.create(
            model=model,
            max_tokens=600,
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

def _safe_float(v) -> float | None:
    try:
        return float(v) if v is not None else None
    except (ValueError, TypeError):
        return None

def _safe_int(v) -> int | None:
    try:
        return int(float(v)) if v is not None else None
    except (ValueError, TypeError):
        return None

def compute_final_r(result: dict) -> tuple[float | None, str]:
    """
    Try all conversion paths in priority order.
    Returns (r_value, conversion_formula_string) or (None, 'none').
    """
    n = _safe_int(result.get('n'))

    # 1. Direct Pearson r
    r = _safe_float(result.get('r'))
    if r is not None and abs(r) <= 1.0:
        return r, 'direct'

    # 2. Standardized beta
    beta = _safe_float(result.get('beta'))
    if beta is not None and abs(beta) <= 1.5:
        return beta, 'beta'

    # 3. t-statistic
    t = _safe_float(result.get('t_stat'))
    if t is not None and n and n > 2:
        return r_from_t(t, n), 't_to_r'

    # 4. F-statistic (df1=1)
    F = _safe_float(result.get('f_stat'))
    if F is not None and F >= 0 and n and n > 2:
        return r_from_F(F, n), 'F_to_r'

    # 5. Chi-square (df=1)
    chi2 = _safe_float(result.get('chi_sq'))
    if chi2 is not None and chi2 >= 0 and n and n > 0:
        r_chi = r_from_chi2(chi2, n)
        if r_chi <= 1.0:
            return r_chi, 'chi2_to_r'

    # 6. Cohen's d
    d = _safe_float(result.get('cohen_d'))
    if d is not None:
        return r_from_d(d), 'd_to_r'

    # 7. Eta-squared / partial eta-squared
    eta = _safe_float(result.get('eta_sq'))
    if eta is not None and 0.0 <= eta <= 1.0:
        return r_from_eta_sq(eta), 'eta_to_r'

    # 8. Log-odds ratio
    log_or = _safe_float(result.get('log_or'))
    if log_or is not None:
        r_lor = r_from_log_or(log_or)
        if abs(r_lor) <= 1.0:
            return r_lor, 'log_or_to_r'

    # 9. Z-score
    z = _safe_float(result.get('z_score'))
    if z is not None and n and n > 0:
        r_z = r_from_z(z, n)
        if abs(r_z) <= 1.0:
            return r_z, 'z_to_r'

    # 10. Unstandardized b + SE_b → t → r
    b = _safe_float(result.get('b_unstand'))
    se_b = _safe_float(result.get('se_b'))
    if b is not None and se_b and se_b > 0 and n and n > 2:
        t_derived = b / se_b
        return r_from_t(t_derived, n), 'b_se_to_r'

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
    parser.add_argument('--manifest', default=None)
    parser.add_argument('--log',      default=str(DEFAULT_LOG))
    parser.add_argument('--limit',    type=int, default=50)
    parser.add_argument('--dry-run',  action='store_true')
    parser.add_argument('--model',    default=GROQ_MODEL)
    parser.add_argument('--no-unpaywall', action='store_true')
    args = parser.parse_args()

    api_key = os.environ.get('GROQ_API_KEY', '')
    if not api_key:
        print("ERROR: set GROQ_API_KEY env var first"); sys.exit(1)

    client = Groq(api_key=api_key)
    pdf_dir = Path(args.pdf_dir)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    # Load manifests
    manifest = {}
    if args.manifest:
        manifest.update(load_oa_manifest(Path(args.manifest)))
    for mf in [BASE / 's2_manifest_20260521.csv',
                BASE / 'p6/tools/results/s2_manifest_20260521.csv',
                BASE / 'p6/tools/results/oa_manifest_20260521.csv']:
        if mf.exists() and not manifest:
            manifest.update(load_oa_manifest(mf))

    # Load tracker
    with open(args.tracker, encoding='utf-8') as f:
        tracker_rows = list(csv.DictReader(f))
    tracker_fieldnames = list(tracker_rows[0].keys())
    tracker_by_seq = {r['seq']: r for r in tracker_rows}
    already_done = {r['seq'] for r in tracker_rows if r.get('converted_r', '').strip()}

    # Load queue and sort by PDF availability
    with open(args.queue, encoding='utf-8') as f:
        queue = list(csv.DictReader(f))

    all_candidates = [
        r for r in queue
        if r.get('seq', '') not in already_done
        and r.get('fulltext_screening_decision', '') != 'N'
    ]

    def _pdf_priority(row):
        if row.get('seq', '') in manifest:
            return 0
        src = row.get('source_url_or_pdf_path', '').strip()
        if src.startswith('http'):
            return 1
        if row.get('pdf_filename', '').strip():
            return 2
        return 3

    all_candidates.sort(key=_pdf_priority)
    candidates = all_candidates[:args.limit]

    use_unpaywall = not args.no_unpaywall
    n_manifest = sum(1 for r in candidates if r.get('seq', '') in manifest)
    n_url = sum(1 for r in candidates
                if r.get('seq', '') not in manifest
                and r.get('source_url_or_pdf_path', '').strip().startswith('http'))
    print(f"Queue: {len(queue)} | Done: {len(already_done)} | "
          f"Candidates: {len(all_candidates)} | Batch: {len(candidates)}")
    print(f"  manifest={n_manifest} | queue_url={n_url} | "
          f"needs_lookup={len(candidates)-n_manifest-n_url}")
    print(f"Model: {args.model} | Dry-run: {args.dry_run} | Unpaywall: {use_unpaywall}\n")

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

        local_pdf = qrow.get('pdf_filename', '').strip()
        if local_pdf:
            cand = pdf_dir / local_pdf
            if cand.exists():
                pdf_path = cand; pdf_source = 'local'

        if pdf_path is None:
            manifest_url = manifest.get(seq, '')
            if manifest_url:
                safe = re.sub(r'[^\w\-.]', '_', seq) + '.pdf'
                dest = pdf_dir / safe
                if download_pdf(manifest_url, dest):
                    pdf_path = dest; pdf_source = 'manifest'
                    print(f"  Manifest OK: {manifest_url[:70]}")

        if pdf_path is None and src.startswith('http'):
            safe = re.sub(r'[^\w\-.]', '_', seq) + '_src.pdf'
            dest = pdf_dir / safe
            if download_pdf(src, dest):
                pdf_path = dest; pdf_source = 'queue_url'
                print(f"  Queue URL OK: {src[:70]}")

        if pdf_path is None and doi and use_unpaywall:
            time.sleep(SLEEP_UNPAYWALL)
            unp_url = try_unpaywall(doi)
            if unp_url.startswith('http'):
                safe = re.sub(r'[^\w\-.]', '_', seq) + '_unp.pdf'
                dest = pdf_dir / safe
                if download_pdf(unp_url, dest):
                    pdf_path = dest; pdf_source = 'unpaywall'
                    print(f"  Unpaywall OK: {unp_url[:70]}")

        if pdf_path is None and doi and use_unpaywall:
            s2_url = try_semantic_scholar(doi)
            if s2_url.startswith('http'):
                safe = re.sub(r'[^\w\-.]', '_', seq) + '_s2.pdf'
                dest = pdf_dir / safe
                if download_pdf(s2_url, dest):
                    pdf_path = dest; pdf_source = 'semantic_scholar'
                    print(f"  S2 OK: {s2_url[:70]}")

        if pdf_path is None:
            print(f"  SKIP: no PDF")
            log_rows.append({'seq': seq, 'title': title, 'year': year, 'doi': doi,
                             'pdf_url': src, 'status': 'NO_PDF', 'converted_r': '',
                             'n': '', 'conversion_formula': '', 'notes': '', 'error': ''})
            continue

        text = pdf_to_text(pdf_path)
        if text.startswith('PDF_READ_ERROR'):
            print(f"  SKIP: {text[:80]}")
            log_rows.append({'seq': seq, 'title': title, 'year': year, 'doi': doi,
                             'pdf_url': pdf_source, 'status': 'PDF_ERROR', 'converted_r': '',
                             'n': '', 'conversion_formula': '', 'notes': '', 'error': text})
            continue

        if args.dry_run:
            print(f"  [DRY-RUN] {len(text)} chars from {pdf_source}")
            log_rows.append({'seq': seq, 'title': title, 'year': year, 'doi': doi,
                             'pdf_url': pdf_source, 'status': 'DRY_RUN', 'converted_r': '',
                             'n': '', 'conversion_formula': '', 'notes': '', 'error': ''})
            continue

        result = extract_r_via_groq(client, text, title, args.model)

        if 'error' in result:
            print(f"  ERROR: {result['error']}")
            log_rows.append({'seq': seq, 'title': title, 'year': year, 'doi': doi,
                             'pdf_url': pdf_source, 'status': 'API_ERROR', 'converted_r': '',
                             'n': '', 'conversion_formula': '', 'notes': '',
                             'error': result['error']})
            time.sleep(SLEEP_BETWEEN)
            continue

        final_r, formula = compute_final_r(result)
        n_val = result.get('n')

        if final_r is None:
            print(f"  NO_R: {result.get('notes','')[:80]}")
            status = 'NO_R_FOUND'
        else:
            print(f"  r={final_r:.4f} | n={n_val} | formula={formula} | "
                  f"iv={result.get('iv_measure','')} | dv={result.get('dv_measure','')}")
            status = 'SUCCESS'
            updated += 1

            trow = tracker_by_seq.get(seq)
            if trow and not trow.get('converted_r', '').strip():
                trow['converted_r']        = str(round(final_r, 6))
                trow['conversion_formula'] = formula
                trow['ready_for_r']        = '1'
                if n_val:
                    try:
                        ni = int(float(n_val))
                        trow['sample_size_n'] = str(ni)
                        trow['fisher_z']      = str(round(fisher_z(final_r), 6))
                        trow['variance_z']    = str(round(variance_z(ni), 8))
                    except (ValueError, TypeError):
                        pass
                for fld, col in [('t_stat','t_value'), ('p_value','p_value'),
                                  ('beta','reported_coefficient'), ('se','standard_error'),
                                  ('f_stat','f_stat'), ('chi_sq','chi_sq'),
                                  ('cohen_d','cohen_d'), ('eta_sq','eta_sq'),
                                  ('log_or','log_or'), ('z_score','z_score'),
                                  ('b_unstand','b_unstand'), ('se_b','se_b')]:
                    v = result.get(fld)
                    if v is not None and col in trow:
                        trow[col] = str(v)
                notes_add = result.get('notes', '')
                if notes_add:
                    existing = trow.get('notes_for_extractor', '')
                    trow['notes_for_extractor'] = (existing + ' | ' + notes_add).strip(' | ')
                trow['extracted_by'] = f'groq-{args.model[:20]}'

        log_rows.append({
            'seq': seq, 'title': title, 'year': year, 'doi': doi,
            'pdf_url': pdf_source, 'status': status,
            'converted_r': str(final_r) if final_r is not None else '',
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
    for k, v in sorted(Counter(r['status'] for r in log_rows).items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

if __name__ == '__main__':
    main()
