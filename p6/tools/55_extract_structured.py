#!/usr/bin/env python3
"""
55_extract_structured.py — Enhanced PDF extraction with PyMuPDF + optional GROBID
Replaces: 41_auto_extract_from_pdfs.py (fixes doi-in-I_KEYWORDS bug, adds confidence tiers)

For each PDF in p6/pdfs/ (filename must contain seq number, e.g. "0900_Smith2014.pdf"):
  1. Try GROBID for structured metadata if GROBID_URL is set
  2. Extract text via PyMuPDF (with OCR fallback via pdfminer.six)
  3. Extract: sample N, I→P coefficient, t-stat, p-value, conversion
  4. Compute converted_r with confidence tier
  5. Write to audit CSV (28 cols) — never auto-writes to tracker

Confidence tiers:
  AUTO_HIGH      — native text, GROBID header OK, 1 candidate effect, |r_doi_chieu| < 1
  AUTO_REVIEW    — beta approximation, OCR, or N inferred from multiple values
  MANUAL_REQUIRED — nonlinear only, multiple competing models, p-value only (no sign/df)
  BLOCKED_NO_PDF — PDF missing

Usage:
  python3 55_extract_structured.py [--pdf-dir p6/pdfs] [--output p6/tools/results]
  GROBID_URL=http://localhost:8070 python3 55_extract_structured.py

Requirements:
  pip install pymupdf pdfminer.six lxml requests pyyaml
"""
from __future__ import annotations

import csv, math, re, sys, os, argparse
from datetime import date
from pathlib import Path
from typing import Optional, Tuple
from collections import defaultdict

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: pip install pymupdf")
    sys.exit(1)

try:
    from pdfminer.high_level import extract_text as pdfminer_extract_text
except ImportError:
    pdfminer_extract_text = None

TODAY = date.today().strftime('%Y%m%d')
BASE = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'

# ─── DO NOT include 'doi' here — causes false positives on DOI strings ─────
I_KEYWORDS = [
    "fsts", "foreign sales", "export intensity", "export ratio",
    "internationalization", "internationalisation", "degree of int",
    "multinationality", "foreign revenue", "overseas sales",
    "export sales", "geographic diversif", "entropy",
    "n_countries", "number of countries", "foreign subsid",
    "foreign direct invest", "fdi intensity", "import intensity",
]

P_KEYWORDS = [
    "roa", "return on asset", "roe", "return on equity",
    "ros", "return on sales", "tobin", "profit margin",
    "sales growth", "revenue growth", "productivity", "performance",
    "financial performance", "firm performance", "labor productivity",
    "total factor productivity", "tfp",
]


# ─── Effect size conversion functions ─────────────────────────────────────
def r_from_t(t_value: float, df_value: float) -> float:
    return t_value / math.sqrt(t_value * t_value + df_value)


def r_from_f(f_value: float, df_error: float, sign: int = 1) -> float:
    r = math.sqrt(f_value / (f_value + df_error))
    return r if sign >= 0 else -r


def turning_point(beta1: float, beta2: float) -> Optional[float]:
    if beta2 == 0:
        return None
    return -beta1 / (2.0 * beta2)


def normalize_effect(
    reported_r: Optional[float] = None,
    beta: Optional[float] = None,
    t_value: Optional[float] = None,
    f_value: Optional[float] = None,
    df_value: Optional[float] = None,
    df_error: Optional[float] = None,
    sign: int = 1,
) -> Tuple[Optional[float], str]:
    if reported_r is not None:
        return round(reported_r, 4), "direct"
    if t_value is not None and df_value is not None:
        return round(r_from_t(t_value, df_value), 4), "t_to_r"
    if f_value is not None and df_error is not None:
        return round(r_from_f(f_value, df_error, sign), 4), "F_to_r"
    if beta is not None:
        return round(beta, 4), "beta"  # low-confidence approximation
    return None, ""


# ─── Text extraction layer ─────────────────────────────────────────────────
def extract_text_layer(pdf_path: Path, language: str = "eng") -> Tuple[str, str]:
    """Returns (text, mode) where mode in {pymupdf_native, pymupdf_ocr, pdfminer_fallback}"""
    doc = fitz.open(pdf_path)
    chunks = []
    mode = "pymupdf_native"
    for page in doc:
        text = page.get_text("text", sort=True)
        if len(text.strip()) < 80:
            # Try OCR fallback via pdfminer.six
            mode = "pdfminer_fallback"
        else:
            chunks.append(text)

    joined = "\n".join(chunks).strip()
    if len(joined) < 200 and pdfminer_extract_text is not None:
        joined = pdfminer_extract_text(str(pdf_path))
        mode = "pdfminer_fallback"

    return joined, mode


# ─── GROBID wrapper (optional) ─────────────────────────────────────────────
def parse_grobid_header(pdf_path: Path, grobid_url: str) -> dict:
    """Returns {title, authors, journal, doi, year} from GROBID TEI XML."""
    try:
        import requests
        from lxml import etree
        NS = {"tei": "http://www.tei-c.org/ns/1.0"}

        with pdf_path.open("rb") as fh:
            resp = requests.post(
                f"{grobid_url}/api/processHeaderDocument",
                files={"input": fh},
                headers={"Accept": "application/xml"},
                data={"consolidateHeader": "1", "includeRawAffiliations": "1"},
                timeout=180,
            )
        resp.raise_for_status()
        root = etree.fromstring(resp.content)

        authors = []
        for a in root.xpath(".//tei:titleStmt//tei:author", namespaces=NS):
            given = " ".join(x.strip() for x in a.xpath(".//tei:forename/text()", namespaces=NS) if x.strip())
            family = " ".join(x.strip() for x in a.xpath(".//tei:surname/text()", namespaces=NS) if x.strip())
            full = " ".join(x for x in [given, family] if x)
            if full:
                authors.append(full)

        return {
            "title": root.xpath("string(.//tei:titleStmt/tei:title[1])", namespaces=NS).strip(),
            "authors": "; ".join(authors),
            "journal": root.xpath("string(.//tei:monogr/tei:title[1])", namespaces=NS).strip(),
            "doi": root.xpath("string(.//tei:idno[@type='DOI'][1])", namespaces=NS).strip(),
            "year": root.xpath("string(.//tei:date/@when)", namespaces=NS)[:4],
        }
    except Exception as e:
        return {"grobid_error": str(e)}


# ─── Pattern extraction from text ─────────────────────────────────────────
def find_sample_n(text: str) -> Optional[int]:
    patterns = [
        r'\bN\s*=\s*([0-9,]+)',
        r'\bn\s*=\s*([0-9,]+)',
        r'sample\s+(?:size\s+)?(?:of\s+)?([0-9,]+)\s+(?:firms?|observations?|companies)',
        r'([0-9,]+)\s+(?:firms?|observations?|firm-year)',
    ]
    candidates = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            try:
                val = int(m.group(1).replace(',', ''))
                if 10 <= val <= 500000:
                    candidates.append(val)
            except ValueError:
                pass
    if not candidates:
        return None
    # Return most frequent or largest
    from collections import Counter
    freq = Counter(candidates)
    return freq.most_common(1)[0][0]


def find_ip_coefficient(text: str) -> dict:
    """Find I→P coefficient near I_KEYWORDS and P_KEYWORDS."""
    result = {"r": None, "t": None, "f": None, "beta": None, "p": None, "df": None, "sign": 1, "page_hint": ""}

    # Look for lines containing I→P keywords
    lines = text.lower().split('\n')
    for i, line in enumerate(lines):
        has_i = any(kw in line for kw in I_KEYWORDS)
        has_p = any(kw in line for kw in P_KEYWORDS)
        context = "\n".join(lines[max(0, i-2):i+3])

        if has_i or has_p:
            # Try to extract r
            m = re.search(r'r\s*=\s*([+-]?0?\.\d+)', context)
            if m:
                result["r"] = float(m.group(1))
                result["page_hint"] = f"line~{i}"
                break

            # Try t-stat
            m = re.search(r't\s*[\(=]\s*([+-]?\d+\.?\d*)', context)
            if m:
                result["t"] = float(m.group(1))
                result["sign"] = -1 if result["t"] < 0 else 1

            # Try beta/coefficient
            m = re.search(r'(?:β|beta|b)\s*=\s*([+-]?\d*\.?\d+)', context)
            if m:
                result["beta"] = float(m.group(1))

            # Try p-value
            m = re.search(r'p\s*[<=]\s*\.?0?(\d+)', context)
            if m:
                result["p"] = float("0." + m.group(1)) if '.' not in m.group(0).split('=')[-1] else float(m.group(0).split('=')[-1])

        if result["r"] or result["t"] or result["beta"]:
            break

    return result


def assign_confidence(coeff: dict, mode: str, grobid_ok: bool) -> str:
    has_r = coeff.get("r") is not None
    has_t = coeff.get("t") is not None
    has_beta = coeff.get("beta") is not None
    has_p_only = coeff.get("p") is not None and not has_r and not has_t

    if has_p_only:
        return "MANUAL_REQUIRED"
    if has_beta and not has_r and not has_t:
        return "AUTO_REVIEW"
    if mode == "pdfminer_fallback":
        return "AUTO_REVIEW"
    if has_r or has_t:
        r_val = coeff.get("r") or (r_from_t(coeff["t"], 100) if coeff.get("t") else None)
        if r_val and abs(r_val) < 1 and grobid_ok:
            return "AUTO_HIGH"
        return "AUTO_REVIEW"
    return "MANUAL_REQUIRED"


# ─── Main extraction loop ──────────────────────────────────────────────────
def process_pdf(pdf_path: Path, tracker_row: dict, grobid_url: Optional[str]) -> dict:
    result = {
        "seq": tracker_row.get("seq", ""),
        "year": tracker_row.get("year", ""),
        "authors": tracker_row.get("authors", ""),
        "title": tracker_row.get("title", ""),
        "journal": tracker_row.get("journal", ""),
        "doi": tracker_row.get("doi", ""),
        "file_path": str(pdf_path),
        "extraction_source": "",
        "effect_size_type": "",
        "fp_type": tracker_row.get("fp_type", ""),
        "r_bao_cao": "",
        "loai_r": "",
        "n_mau": tracker_row.get("sample_size_n", ""),
        "r_doi_chieu": tracker_row.get("converted_r", ""),
        "t_value": "",
        "f_value": "",
        "df_value": "",
        "p_value": "",
        "ci_low": "",
        "ci_high": "",
        "phi_tuyen": "0",
        "turning_point": "",
        "ICRV": tracker_row.get("icrv", ""),
        "DPL": tracker_row.get("dpl", ""),
        "sample_characteristics": "",
        "page_or_table": "",
        "confidence": "",
        "review_status": "BLOCKED_NO_PDF",
        "ghi_chu": "",
    }

    if not pdf_path.exists():
        return result

    # Extract text
    try:
        text, mode = extract_text_layer(pdf_path)
        result["extraction_source"] = mode
    except Exception as e:
        result["ghi_chu"] = f"Text extraction failed: {e}"
        result["review_status"] = "MANUAL_REQUIRED"
        return result

    # GROBID metadata (optional)
    grobid_ok = False
    if grobid_url:
        meta = parse_grobid_header(pdf_path, grobid_url)
        if "grobid_error" not in meta:
            grobid_ok = True
            for k in ("title", "authors", "journal", "doi", "year"):
                if meta.get(k):
                    result[k] = meta[k]
            result["extraction_source"] = f"grobid_native+{mode}"

    # Sample N
    n = find_sample_n(text)
    if n and not result["n_mau"]:
        result["n_mau"] = str(n)

    # I→P coefficient
    coeff = find_ip_coefficient(text)
    r_val, conv = normalize_effect(
        reported_r=coeff.get("r"),
        beta=coeff.get("beta"),
        t_value=coeff.get("t"),
        df_value=coeff.get("df"),
        sign=coeff.get("sign", 1),
    )

    if r_val is not None:
        result["r_doi_chieu"] = str(r_val)
        result["loai_r"] = conv
        result["r_bao_cao"] = str(coeff.get("r") or coeff.get("t") or coeff.get("beta") or "")
        result["effect_size_type"] = conv
    if coeff.get("t"):
        result["t_value"] = str(coeff["t"])
    if coeff.get("p"):
        result["p_value"] = str(coeff["p"])
    if coeff.get("page_hint"):
        result["page_or_table"] = coeff["page_hint"]

    # Confidence tier
    confidence = assign_confidence(coeff, mode, grobid_ok)
    result["review_status"] = confidence
    result["confidence"] = {"AUTO_HIGH": "0.9", "AUTO_REVIEW": "0.6", "MANUAL_REQUIRED": "0.2"}.get(confidence, "0.1")

    return result


AUDIT_COLS = [
    "seq", "year", "authors", "title", "journal", "doi", "file_path",
    "extraction_source", "effect_size_type", "fp_type",
    "r_bao_cao", "loai_r", "n_mau", "r_doi_chieu",
    "t_value", "f_value", "df_value", "p_value", "ci_low", "ci_high",
    "phi_tuyen", "turning_point", "ICRV", "DPL",
    "sample_characteristics", "page_or_table", "confidence", "review_status", "ghi_chu",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-dir", default="p6/pdfs")
    ap.add_argument("--output", default="p6/tools/results")
    ap.add_argument("--grobid-url", default=os.environ.get("GROBID_URL", ""))
    ap.add_argument("--limit", type=int, default=0, help="Process max N PDFs (0=all)")
    args = ap.parse_args()

    pdf_dir = BASE / args.pdf_dir
    output_dir = BASE / args.output
    output_dir.mkdir(parents=True, exist_ok=True)
    audit_path = output_dir / f"structured_extraction_{TODAY}.csv"

    if not pdf_dir.exists():
        print(f"PDF directory not found: {pdf_dir}")
        print("Download PDFs first with: python3 p6/tools/40_batch_download_pdfs.py")
        sys.exit(1)

    # Load tracker
    with open(TRACKER, newline='', encoding='utf-8') as f:
        tracker_rows = {r['seq'].strip(): r for r in csv.DictReader(f)}

    # Find PDFs
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if args.limit:
        pdfs = pdfs[:args.limit]

    print(f"Processing {len(pdfs)} PDFs → {audit_path.name}")
    if args.grobid_url:
        print(f"GROBID: {args.grobid_url}")
    else:
        print("GROBID: not configured (set GROBID_URL=http://localhost:8070 to enable)")

    results = []
    stats = {"AUTO_HIGH": 0, "AUTO_REVIEW": 0, "MANUAL_REQUIRED": 0, "BLOCKED_NO_PDF": 0}

    for pdf in pdfs:
        # Extract seq from filename (expects leading digits, e.g. 0900_Smith2014.pdf or seq900.pdf)
        m = re.search(r'(?:^|seq|_)0*(\d+)', pdf.stem, re.IGNORECASE)
        seq = m.group(1) if m else pdf.stem
        row = tracker_rows.get(seq, {"seq": seq})

        rec = process_pdf(pdf, row, args.grobid_url or None)
        results.append(rec)
        stats[rec["review_status"]] = stats.get(rec["review_status"], 0) + 1
        print(f"  seq={seq:>5} | {rec['review_status']:<20} | r={rec['r_doi_chieu'] or '—':>7} | n={rec['n_mau'] or '—':>6} | {rec['extraction_source']}")

    with open(audit_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=AUDIT_COLS, extrasaction='ignore')
        w.writeheader()
        w.writerows(results)

    print(f"\nAudit CSV: {audit_path}")
    print(f"Summary: AUTO_HIGH={stats['AUTO_HIGH']} | AUTO_REVIEW={stats['AUTO_REVIEW']} | MANUAL_REQUIRED={stats['MANUAL_REQUIRED']}")
    print("\nTo update tracker with AUTO_HIGH results, run:")
    print(f"  python3 p6/tools/56_apply_extraction_audit.py --input {audit_path.name} --min-confidence AUTO_HIGH")


if __name__ == "__main__":
    main()
