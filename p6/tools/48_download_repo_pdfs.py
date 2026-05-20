#!/usr/bin/env python3
"""
48_download_repo_pdfs.py — Download PDFs from REPO_URL papers in extraction queue.

Handles:
  - Direct .pdf links (simple GET)
  - HAL (hal.science, hal.archives-ouvertes.fr) → append /document
  - figshare → API v2 to get download URL
  - SSRN → construct download URL from abstract ID
  - eprints repositories → try /1/ subpath patterns

Run via GitHub Actions (this server blocks external HTTP).

Usage:
  python3 p6/tools/48_download_repo_pdfs.py --output-dir /tmp/pdfs [--limit 10]

Output:
  - Downloaded PDFs in output-dir (named {seq}_{year}.pdf)
  - p6/tools/results/download_log_repo_YYYYMMDD.csv
"""
import csv, re, os, sys, time, json, argparse
import requests
from pathlib import Path
from datetime import date

DEFAULT_QUEUE   = "p6/tools/results/extraction_queue_y_20260520.csv"
DEFAULT_OUT_DIR = "/tmp/p6_pdfs"
LOG_OUT         = f"p6/tools/results/download_log_repo_{date.today().strftime('%Y%m%d')}.csv"
TIMEOUT         = 30
DELAY           = 1.5

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/pdf,*/*",
}


def resolve_hal(url: str) -> str:
    """HAL: https://hal.science/hal-XXXXX → /document for direct PDF."""
    # Normalize
    base = re.sub(r'/v\d+$', '', url.rstrip('/'))
    return base + "/document"


def resolve_figshare(url: str) -> str:
    """figshare: extract article ID → API v2 download URL."""
    m = re.search(r'/(\d{7,10})(?:/|$)', url)
    if not m:
        return ""
    article_id = m.group(1)
    try:
        r = requests.get(
            f"https://api.figshare.com/v2/articles/{article_id}",
            timeout=15, headers={"User-Agent": HEADERS["User-Agent"]}
        )
        if r.status_code == 200:
            data = r.json()
            files = data.get("files", [])
            for f in files:
                dl = f.get("download_url", "")
                if dl:
                    return dl
    except Exception:
        pass
    return ""


def resolve_ssrn(url: str) -> str:
    """SSRN: extract abstract_id and construct PDF URL."""
    # Direct PDF link already
    if url.lower().endswith('.pdf') or 'Delivery.cfm' in url:
        return url
    m = re.search(r'abstract(?:_id)?[=_](\d+)', url, re.I)
    if m:
        abs_id = m.group(1)
        return f"https://papers.ssrn.com/sol3/Delivery.cfm/paper_{abs_id}.pdf?abstractid={abs_id}&type=2"
    return ""


def resolve_eprints(url: str) -> list[str]:
    """eprints: try common PDF subpath patterns."""
    base = url.rstrip('/')
    candidates = [
        base + "/1/article.pdf",
        base + "/1/paper.pdf",
        base + "/2/article.pdf",
        base + "/document",
    ]
    # Also try extracting the handle number
    m = re.search(r'/(\d{4,7})/?$', base)
    if m:
        num = m.group(1)
        candidates.append(base + f"/1/{num}.pdf")
    return candidates


def try_download(url: str, dest: Path) -> tuple[bool, str]:
    """Try downloading a URL as PDF. Returns (success, note)."""
    if not url:
        return False, "no_url"
    try:
        r = requests.get(url, timeout=TIMEOUT, headers=HEADERS,
                         allow_redirects=True, stream=True)
        if r.status_code == 200:
            ct = r.headers.get("Content-Type", "")
            if "pdf" in ct or "octet-stream" in ct or url.lower().endswith(".pdf"):
                content = b"".join(r.iter_content(8192))
                if len(content) > 10_000 and content[:4] == b'%PDF':
                    dest.write_bytes(content)
                    return True, f"ok_{len(content)//1024}kb"
                return False, f"not_pdf_content({ct})"
            return False, f"wrong_content_type({ct})"
        return False, f"http_{r.status_code}"
    except Exception as e:
        return False, str(e)[:60]


def classify_url(url: str) -> str:
    u = url.lower()
    if u.endswith('.pdf') or '/bitstream/' in u or '/pdf/' in u:
        return 'direct'
    if 'hal.science' in u or 'hal.archives' in u or 'audencia.hal' in u:
        return 'hal'
    if 'figshare.com' in u:
        return 'figshare'
    if 'ssrn.com' in u or 'ssrn.959408' in u or 'abstractid=' in u:
        return 'ssrn'
    if 'eprints.' in u or 'lirias.' in u or 'shura.' in u or 'nrl.' in u:
        return 'eprints'
    return 'other'


def download_one(row: dict, out_dir: Path) -> dict:
    seq  = row.get("seq", "")
    url  = row.get("source_url_or_pdf_path", "").strip()
    year = row.get("year", "")
    dest = out_dir / f"{seq}_{year}.pdf"

    result = {
        "seq": seq, "title": row.get("title","")[:60],
        "url": url[:80], "status": "", "note": "", "filename": ""
    }

    if dest.exists() and dest.stat().st_size > 10_000:
        result.update(status="SKIP_EXISTS", note="already downloaded", filename=dest.name)
        return result

    kind = classify_url(url)

    candidates = []
    if kind == 'direct':
        candidates = [url]
    elif kind == 'hal':
        candidates = [resolve_hal(url)]
    elif kind == 'figshare':
        dl = resolve_figshare(url)
        candidates = [dl] if dl else []
    elif kind == 'ssrn':
        dl = resolve_ssrn(url)
        candidates = [dl] if dl else [url]
    elif kind == 'eprints':
        candidates = resolve_eprints(url)
    else:
        result.update(status="SKIP_UNSUPPORTED", note=f"kind={kind}")
        return result

    for cand in candidates:
        if not cand:
            continue
        ok, note = try_download(cand, dest)
        if ok:
            result.update(status="OK", note=note, filename=dest.name)
            return result
        time.sleep(0.3)

    result.update(status="FAIL", note=f"tried {len(candidates)} URLs")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue",      default=DEFAULT_QUEUE)
    parser.add_argument("--output-dir", default=DEFAULT_OUT_DIR)
    parser.add_argument("--limit",      type=int, default=0)
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(args.queue, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    targets = [r for r in rows if r.get("pdf_status", "") == "REPO_URL"]
    if args.limit:
        targets = targets[:args.limit]
    print(f"REPO_URL papers to attempt: {len(targets)}")

    log_rows = []
    ok_count = 0

    for i, row in enumerate(targets, 1):
        result = download_one(row, out_dir)
        log_rows.append(result)
        status = result["status"]
        if status == "OK":
            ok_count += 1
            print(f"  [{i}/{len(targets)}] OK   seq={row['seq']} → {result['filename']}", flush=True)
        elif status == "SKIP_EXISTS":
            ok_count += 1
            print(f"  [{i}/{len(targets)}] SKIP seq={row['seq']} (exists)", flush=True)
        else:
            print(f"  [{i}/{len(targets)}] FAIL seq={row['seq']} {result['note']}", flush=True)
        time.sleep(DELAY)

    print(f"\n=== DOWNLOAD RESULTS ===")
    print(f"  OK:   {ok_count}/{len(targets)}")
    print(f"  FAIL: {len(targets)-ok_count}/{len(targets)}")

    with open(LOG_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["seq","title","url","status","note","filename"])
        w.writeheader()
        w.writerows(log_rows)
    print(f"  Log:  {LOG_OUT}")

    return ok_count


if __name__ == "__main__":
    main()
