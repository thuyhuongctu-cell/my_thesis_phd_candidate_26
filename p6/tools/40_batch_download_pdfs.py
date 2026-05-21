#!/usr/bin/env python3
"""
40_batch_download_pdfs.py — Batch download PDFs from Unpaywall OA manifest
Run LOCALLY (your machine has internet; server blocks external APIs).

Usage:
  python3 p6/tools/40_batch_download_pdfs.py
  python3 p6/tools/40_batch_download_pdfs.py --manifest p6/tools/results/oa_manifest_20260520.csv
  python3 p6/tools/40_batch_download_pdfs.py --output-dir /path/to/pdfs --limit 50

Input:  p6/tools/results/oa_manifest_20260520.csv  (from Unpaywall workflow)
Output: p6/pdfs/{seq}_{slug}.pdf + p6/tools/results/download_log_YYYYMMDD.csv
"""
import csv, sys, time, os, re, requests, argparse
from datetime import date
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

DEFAULT_MANIFEST  = "p6/tools/results/oa_manifest_20260520.csv"
DEFAULT_OUTPUT_DIR = "p6/pdfs"
DEFAULT_LOG       = f"p6/tools/results/download_log_{date.today().strftime('%Y%m%d')}.csv"
DELAY = 0.5        # seconds between requests (polite)
TIMEOUT = 30       # seconds per download
MAX_WORKERS = 3    # parallel downloads

HEADERS = {
    "User-Agent": "Mozilla/5.0 (research; meta-analysis download; huongp1323001@gstudent.ctu.edu.vn)"
}


def slugify(text: str, maxlen=40) -> str:
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '_', text).strip('_')
    return text[:maxlen]


def download_pdf(row: dict, output_dir: Path) -> dict:
    seq      = row.get("seq", "")
    title    = row.get("title", "")
    year     = row.get("year", "")
    pdf_url  = row.get("pdf_url", "").strip()
    repo_url = row.get("repo_url", "").strip()
    is_oa    = row.get("is_oa", "False")

    result = {
        "seq": seq, "title": title[:60], "year": year,
        "is_oa": is_oa, "pdf_url": pdf_url,
        "filename": "", "status": "", "bytes": 0, "note": ""
    }

    url = pdf_url or repo_url
    if not url:
        result["status"] = "SKIP_NO_URL"
        return result

    slug = slugify(title) or f"paper_{seq}"
    filename = f"{seq}_{slug}_{year}.pdf"
    filepath = output_dir / filename

    if filepath.exists() and filepath.stat().st_size > 5000:
        result.update({"filename": filename, "status": "ALREADY_EXISTS",
                        "bytes": filepath.stat().st_size})
        return result

    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT,
                         allow_redirects=True, stream=True)
        content_type = r.headers.get("content-type", "")

        if r.status_code != 200:
            result.update({"status": f"HTTP_{r.status_code}", "note": url[:80]})
            return result

        if "pdf" not in content_type and "octet-stream" not in content_type:
            # May be an HTML landing page, not a direct PDF
            result.update({"status": "NOT_PDF", "note": f"content-type={content_type[:40]}"})
            return result

        content = b"".join(r.iter_content(chunk_size=8192))
        if len(content) < 2000:
            result.update({"status": "TOO_SMALL", "bytes": len(content)})
            return result

        filepath.write_bytes(content)
        result.update({"filename": filename, "status": "OK", "bytes": len(content)})

    except requests.Timeout:
        result["status"] = "TIMEOUT"
    except Exception as e:
        result.update({"status": "ERROR", "note": str(e)[:80]})

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest",    default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir",  default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--log",         default=DEFAULT_LOG)
    parser.add_argument("--limit",       type=int, default=0,
                        help="Max papers to attempt (0 = all with pdf_url)")
    parser.add_argument("--oa-only",     action="store_true",
                        help="Only download gold/green/hybrid OA (skip bronze/closed)")
    parser.add_argument("--workers",     type=int, default=MAX_WORKERS)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)

    with open(args.manifest, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Filter to rows with a PDF URL
    candidates = [r for r in rows if r.get("pdf_url", "").strip()]

    if args.oa_only:
        candidates = [r for r in candidates
                      if r.get("oa_status", "") in ("gold", "green", "hybrid")]

    if args.limit:
        candidates = candidates[:args.limit]

    print(f"PDFs to download: {len(candidates)} (output: {output_dir})", flush=True)
    if not candidates:
        print("Nothing to download — run the Unpaywall workflow first.")
        return

    results = []
    ok = already = skip = error = 0

    # Download with limited parallelism
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(download_pdf, row, output_dir): row for row in candidates}
        for i, fut in enumerate(as_completed(futures), 1):
            res = fut.result()
            results.append(res)
            s = res["status"]
            if s == "OK":           ok += 1
            elif s == "ALREADY_EXISTS": already += 1
            elif s == "SKIP_NO_URL": skip += 1
            else:                   error += 1

            if i % 20 == 0 or i == len(candidates):
                pct = 100 * i / len(candidates)
                print(f"  {i}/{len(candidates)} ({pct:.0f}%) | OK={ok} cached={already} err={error}",
                      flush=True)

            time.sleep(DELAY / args.workers)

    # Write log
    log_cols = ["seq", "title", "year", "is_oa", "pdf_url",
                "filename", "status", "bytes", "note"]
    with open(args.log, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=log_cols)
        w.writeheader()
        # sort by seq for readability
        results.sort(key=lambda r: int(r["seq"]) if str(r["seq"]).isdigit() else 9999)
        w.writerows(results)

    print(f"\n=== DOWNLOAD SUMMARY ===")
    print(f"Downloaded (new): {ok}")
    print(f"Already existed:  {already}")
    print(f"Errors/skipped:   {error + skip}")
    print(f"Log:              {args.log}")
    print(f"PDF folder:       {output_dir}/")
    total_mb = sum(r["bytes"] for r in results if isinstance(r["bytes"], int)) / 1e6
    print(f"Total size:       {total_mb:.1f} MB")

    # Summarize errors for follow-up
    errors = [r for r in results if r["status"] not in ("OK", "ALREADY_EXISTS", "SKIP_NO_URL")]
    if errors:
        print(f"\n--- {len(errors)} failed downloads (check manually) ---")
        for r in errors[:10]:
            print(f"  seq={r['seq']} | {r['status']} | {r['note'][:60]}")
        if len(errors) > 10:
            print(f"  ... and {len(errors)-10} more (see {args.log})")


if __name__ == "__main__":
    main()
