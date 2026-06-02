#!/usr/bin/env python3
"""Verifica DOIs contra CrossRef. Marca cada record con doi_verified TRUE/FALSE.

Lee `<project_dir>/master_corpus.json` (generado por build_master_xlsx.py antes del xlsx)
y escribe `<project_dir>/master_corpus.json` ampliado. NO toca el .xlsx aquí.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests

CROSSREF = "https://api.crossref.org/works/"
UA = "systematic-review-skill/1.0 (mailto:dr.alcalarueda.orl@gmail.com)"


def verify_one(doi: str) -> bool:
    if not doi:
        return False
    try:
        r = requests.get(CROSSREF + doi, headers={"User-Agent": UA}, timeout=20)
        return r.status_code == 200
    except requests.RequestException:
        return False


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--batch-size", type=int, default=50)
    p.add_argument("--delay", type=float, default=0.2)
    args = p.parse_args()

    proj = Path(args.project_dir)
    corpus_json = proj / "master_corpus.json"
    if not corpus_json.exists():
        print(json.dumps({"ok": False, "error": "master_corpus.json no existe"}))
        return 1

    records = json.loads(corpus_json.read_text())
    n_verified = 0
    for i, rec in enumerate(records):
        if "doi_verified" in rec and rec["doi_verified"] is not None:
            if rec["doi_verified"]:
                n_verified += 1
            continue
        ok = verify_one(rec.get("doi", ""))
        rec["doi_verified"] = ok
        if ok:
            n_verified += 1
        if (i + 1) % args.batch_size == 0:
            corpus_json.write_text(json.dumps(records, indent=2, ensure_ascii=False))
            print(f"[crossref] {i+1}/{len(records)}", file=sys.stderr)
        time.sleep(args.delay)

    corpus_json.write_text(json.dumps(records, indent=2, ensure_ascii=False))
    print(json.dumps({"ok": True, "total": len(records), "verified": n_verified}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
