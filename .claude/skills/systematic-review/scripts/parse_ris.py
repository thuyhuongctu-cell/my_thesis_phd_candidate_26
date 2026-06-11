#!/usr/bin/env python3
"""Parsea archivos RIS exportados de WoS o Embase y normaliza al schema común.

Uso:
    python parse_ris.py <project_dir> --source wos|embase
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import rispy


def normalize_ris_entry(e: dict, source: str) -> dict:
    doi = (e.get("doi") or "").strip()
    if not doi:
        for k in ("DO", "M3", "L3"):
            if e.get(k):
                doi = str(e[k]).strip()
                break
    authors = e.get("authors") or e.get("first_authors") or []
    if isinstance(authors, str):
        authors = [authors]

    year = ""
    for k in ("year", "publication_year", "date"):
        v = e.get(k)
        if v:
            s = str(v)
            if len(s) >= 4 and s[:4].isdigit():
                year = s[:4]
                break

    source_id = e.get("accession_number") or e.get("id") or e.get("primary_title", "")[:50] or ""

    return {
        "source": source,
        "source_id": str(source_id),
        "doi": doi,
        "title": (e.get("title") or e.get("primary_title") or "").strip(),
        "authors": authors,
        "year": year,
        "journal": (e.get("journal_name") or e.get("secondary_title") or e.get("alternate_title1") or "").strip(),
        "abstract": (e.get("abstract") or e.get("notes_abstract") or "").strip(),
        "keywords": e.get("keywords") or [],
        "url": (e.get("url") or "").strip(),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--source", choices=["wos", "embase", "cochrane"], required=True)
    args = p.parse_args()

    proj = Path(args.project_dir)
    ris_path = proj / "searches" / f"raw_{args.source}.ris"
    if not ris_path.exists():
        print(json.dumps({"ok": False, "error": f"no encuentro {ris_path}"}))
        return 1

    with ris_path.open("r", encoding="utf-8", errors="replace") as f:
        try:
            entries = rispy.load(f)
        except Exception as e:  # noqa: BLE001 (rispy lanza varios tipos)
            print(json.dumps({"ok": False, "error": f"RIS parse: {e}"}))
            return 1

    records = [normalize_ris_entry(e, args.source) for e in entries]
    out = proj / "searches" / f"raw_{args.source}.json"
    out.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")

    state_path = proj / "project_state.json"
    state = json.loads(state_path.read_text())
    state.setdefault("counts", {})[f"identificados_{args.source}"] = len(records)
    state.setdefault("search_cursors", {})[args.source] = "complete"
    state_path.write_text(json.dumps(state, indent=2))

    print(json.dumps({"ok": True, "count": len(records), "out": str(out)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
