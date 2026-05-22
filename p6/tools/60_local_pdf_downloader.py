"""
60_local_pdf_downloader.py  — run LOCAL (not on server)
Tải PDF cho 310 DOI_FIRST papers trong tracker v2.
Nguồn: Unpaywall → OpenAlex → Semantic Scholar → arXiv → direct DOI

Usage:
    pip install requests
    python3 p6/tools/60_local_pdf_downloader.py

Output:
    p6/pdfs/seq_NNN.pdf       — downloaded PDFs
    p6/tools/results/download_log_v2_local.csv
"""

import csv, requests, time, re, json
from pathlib import Path
from urllib.parse import urlencode

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


def main():
    with open(TRACKER) as f:
        rows = list(csv.DictReader(f))

    doi_rows = [r for r in rows if r.get("extraction_priority") == "1_DOI_FIRST"
                and r.get("doi", "").strip()]
    print(f"Tracker v2: {len(rows)} total | DOI_FIRST with DOI: {len(doi_rows)}")

    log = []
    for i, row in enumerate(doi_rows):
        seq = row["seq"]
        doi = row["doi"].strip()
        dest = PDFS_DIR / f"seq_{seq}.pdf"

        if is_real_pdf(dest):
            print(f"[{i+1}/{len(doi_rows)}] seq={seq} CACHED")
            log.append({"seq": seq, "doi": doi, "status": "CACHED",
                        "source": "cache", "pdf_path": str(dest)})
            continue

        print(f"[{i+1}/{len(doi_rows)}] seq={seq} doi={doi[:50]}...")
        status, source, pdf_url = "NO_PDF", "", ""

        # Try each source
        for name, fn in [
            ("arxiv",  lambda: arxiv_from_doi(doi)),
            ("unpaywall", lambda: unpaywall(doi)),
            ("openalex",  lambda: openalex(doi)),
            ("s2",        lambda: semantic_scholar(doi)),
        ]:
            time.sleep(0.3)
            url = fn()
            if url:
                if try_url(url, dest):
                    status, source, pdf_url = "OK", name, url
                    print(f"  ✓ {name} {url[:60]}")
                    break
                else:
                    print(f"  ✗ {name} (got url but pdf download failed)")
            time.sleep(0.3)

        if status == "NO_PDF":
            print(f"  — no OA PDF found")

        log.append({"seq": seq, "doi": doi, "status": status,
                    "source": source, "pdf_url": pdf_url,
                    "pdf_path": str(dest) if status == "OK" else ""})
        time.sleep(SLEEP)

    # Write log
    with open(LOG_OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["seq","doi","status","source","pdf_url","pdf_path"])
        w.writeheader(); w.writerows(log)

    ok    = sum(1 for r in log if r["status"] == "OK")
    cache = sum(1 for r in log if r["status"] == "CACHED")
    print(f"\nDone: {ok} downloaded, {cache} cached, {len(log)-ok-cache} not found")
    print(f"Log: {LOG_OUT}")


if __name__ == "__main__":
    main()
