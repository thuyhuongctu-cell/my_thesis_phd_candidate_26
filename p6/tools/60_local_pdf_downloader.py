"""
60_local_pdf_downloader.py  — run LOCAL (not on server)
Tải PDF cho 310 DOI_FIRST papers trong tracker v2.
Nguồn: arXiv → Unpaywall → OpenAlex → Semantic Scholar → Wayback Machine

Usage:
    pip install requests
    python3 p6/tools/60_local_pdf_downloader.py [--seq N] [--limit N]

    --seq N    start from seq N (resume after interruption)
    --limit N  process at most N papers this run

Output:
    p6/pdfs/seq_NNN.pdf       — downloaded PDFs
    p6/tools/results/download_log_v2_local.csv
"""

import argparse, csv, requests, time, re, json
from pathlib import Path
from urllib.parse import urlencode, quote

TRACKER   = Path("p6/tools/results/fulltext_to_extraction_tracker_v2.csv")
PDFS_DIR  = Path("p6/pdfs")
LOG_OUT   = Path("p6/tools/results/download_log_v2_local.csv")
EMAIL     = "huongdt@vlute.edu.vn"
TIMEOUT   = 30
SLEEP     = 1.5
HEADERS   = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/pdf,*/*",
}

PDFS_DIR.mkdir(parents=True, exist_ok=True)


def is_real_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 5_000:
        return False
    with open(path, "rb") as f:
        return f.read(4) == b"%PDF"


def save_pdf(resp, dest: Path) -> bool:
    first = b""
    for chunk in resp.iter_content(512):
        first = chunk
        break
    if not first.startswith(b"%PDF"):
        return False
    with open(dest, "wb") as f:
        f.write(first)
        for chunk in resp.iter_content(65_536):
            f.write(chunk)
    return is_real_pdf(dest)


def try_url(url: str, dest: Path) -> bool:
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, stream=True,
                         allow_redirects=True)
        if r.status_code == 200:
            return save_pdf(r, dest)
    except Exception:
        pass
    return False


def unpaywall(doi: str) -> str | None:
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            d = r.json()
            loc = d.get("best_oa_location") or {}
            return loc.get("url_for_pdf") or loc.get("url")
    except Exception:
        pass
    return None


def openalex(doi: str) -> str | None:
    try:
        url = f"https://api.openalex.org/works/doi:{doi}"
        r = requests.get(url, timeout=15,
                         headers={"User-Agent": f"mailto:{EMAIL}"})
        if r.status_code == 200:
            d = r.json()
            oa = d.get("open_access", {})
            return oa.get("oa_url")
    except Exception:
        pass
    return None


def semantic_scholar(doi: str) -> str | None:
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}?fields=openAccessPdf"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            d = r.json()
            oa = d.get("openAccessPdf") or {}
            return oa.get("url")
    except Exception:
        pass
    return None


def arxiv_from_doi(doi: str) -> str | None:
    """If DOI points to arXiv, build direct PDF URL."""
    m = re.search(r"arxiv[./](\d{4}\.\d{4,5})", doi, re.I)
    if m:
        return f"https://arxiv.org/pdf/{m.group(1)}"
    return None


def wayback_machine(doi: str) -> str | None:
    """Check Wayback Machine CDX for a cached PDF of this DOI's page."""
    doi_url = f"https://doi.org/{doi}"
    # Also try the direct paper URL pattern from common publishers
    cdx_url = (
        f"http://web.archive.org/cdx/search/cdx"
        f"?url={quote(doi_url, safe='')}&output=json&limit=3"
        f"&fl=timestamp,statuscode,mimetype,original&filter=statuscode:200"
        f"&filter=mimetype:application/pdf"
    )
    try:
        r = requests.get(cdx_url, timeout=15)
        if r.status_code == 200:
            rows = r.json()
            if len(rows) > 1:  # first row is header
                ts, _, _, orig = rows[1]
                return f"https://web.archive.org/web/{ts}if_/{orig}"
    except Exception:
        pass

    # Fallback: try the resolved DOI URL pattern
    try:
        # Get the resolved URL from DOI
        head = requests.head(doi_url, timeout=10, allow_redirects=True)
        if head.status_code == 200 and head.url != doi_url:
            resolved = head.url
            cdx2 = (
                f"http://web.archive.org/cdx/search/cdx"
                f"?url={quote(resolved, safe='')}&output=json&limit=3"
                f"&fl=timestamp,statuscode,mimetype,original&filter=statuscode:200"
                f"&filter=mimetype:application/pdf"
            )
            r2 = requests.get(cdx2, timeout=15)
            if r2.status_code == 200:
                rows2 = r2.json()
                if len(rows2) > 1:
                    ts, _, _, orig = rows2[1]
                    return f"https://web.archive.org/web/{ts}if_/{orig}"
    except Exception:
        pass
    return None


SOURCES = [
    ("arxiv",     lambda doi: arxiv_from_doi(doi)),
    ("unpaywall", lambda doi: unpaywall(doi)),
    ("openalex",  lambda doi: openalex(doi)),
    ("s2",        lambda doi: semantic_scholar(doi)),
    ("wayback",   lambda doi: wayback_machine(doi)),
]

LOG_FIELDS = ["seq", "doi", "status", "source", "pdf_url", "pdf_path"]


def main():
    parser = argparse.ArgumentParser(description="Download PDFs locally for tracker_v2 DOI papers")
    parser.add_argument("--seq",   type=int, default=0,  help="Start from this seq number (resume)")
    parser.add_argument("--limit", type=int, default=0,  help="Max papers to process (0=all)")
    args = parser.parse_args()

    with open(TRACKER) as f:
        rows = list(csv.DictReader(f))

    doi_rows = [r for r in rows
                if r.get("extraction_priority") == "1_DOI_FIRST"
                and r.get("doi", "").strip()]

    # Resume: skip seqs already logged
    already_done = set()
    if LOG_OUT.exists():
        with open(LOG_OUT) as f:
            for r in csv.DictReader(f):
                already_done.add(r["seq"])

    if args.seq:
        doi_rows = [r for r in doi_rows if int(r["seq"]) >= args.seq]

    doi_rows = [r for r in doi_rows if r["seq"] not in already_done]

    if args.limit:
        doi_rows = doi_rows[:args.limit]

    total_eligible = len([r for r in rows
                          if r.get("extraction_priority") == "1_DOI_FIRST"
                          and r.get("doi", "").strip()])
    print(f"Tracker v2: {len(rows)} total | DOI_FIRST: {total_eligible} | "
          f"Already done: {len(already_done)} | This run: {len(doi_rows)}")

    # Append to log (so resume works)
    need_header = not LOG_OUT.exists()
    log_f = open(LOG_OUT, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(log_f, fieldnames=LOG_FIELDS)
    if need_header:
        writer.writeheader()

    run_stats = {"ok": 0, "cached": 0, "miss": 0}

    for i, row in enumerate(doi_rows):
        seq = row["seq"]
        doi = row["doi"].strip()
        dest = PDFS_DIR / f"seq_{seq}.pdf"

        if is_real_pdf(dest):
            print(f"[{i+1}/{len(doi_rows)}] seq={seq} CACHED")
            writer.writerow({"seq": seq, "doi": doi, "status": "CACHED",
                             "source": "cache", "pdf_url": "", "pdf_path": str(dest)})
            run_stats["cached"] += 1
            continue

        print(f"[{i+1}/{len(doi_rows)}] seq={seq} doi={doi[:55]}...")
        status, source, pdf_url = "NO_PDF", "", ""

        for name, fn in SOURCES:
            time.sleep(0.3)
            url = fn(doi)
            if url:
                if try_url(url, dest):
                    status, source, pdf_url = "OK", name, url
                    print(f"  ✓ {name}: {url[:70]}")
                    break
                print(f"  ✗ {name}: URL found but PDF download failed")
            time.sleep(0.3)

        if status == "NO_PDF":
            print(f"  — no OA PDF found (all 5 sources exhausted)")
            run_stats["miss"] += 1
        else:
            run_stats["ok"] += 1

        writer.writerow({"seq": seq, "doi": doi, "status": status,
                         "source": source, "pdf_url": pdf_url,
                         "pdf_path": str(dest) if status == "OK" else ""})
        log_f.flush()
        time.sleep(SLEEP)

    log_f.close()
    print(f"\nRun complete: {run_stats['ok']} downloaded | "
          f"{run_stats['cached']} cached | {run_stats['miss']} not found")
    print(f"Log: {LOG_OUT}")
    print(f"\nTo resume from where you left off:")
    print(f"  python3 p6/tools/60_local_pdf_downloader.py")


if __name__ == "__main__":
    main()
