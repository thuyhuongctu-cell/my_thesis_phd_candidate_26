#!/usr/bin/env python3
"""
62_build_review_sheet.py — Turn the OpenAlex enrichment output into a
click-through manual-review sheet.

For every study that still needs a human (verify_status in
doi_mismatch_check / author_year_guess / not_found) it emits one row with:
  * what we had (candidate_doi) and what OpenAlex returned (oa_doi/oa_title),
  * the expected title from the APA file (when known),
  * ready-made search links (OpenAlex web, OpenAlex API, Google Scholar),
  * blank columns for the reviewer: correct_doi, decision, notes.

So the reviewer just taps a link, finds the paper, and pastes the DOI back.

Usage:
  python3 62_build_review_sheet.py \
      --enriched ../data/p6_openalex_enriched.csv \
      --apa      ../p6_primary_studies_apa7.md \
      --out      ../data/p6_openalex_review.csv
"""

import argparse
import csv
import importlib.util
from pathlib import Path
from urllib.parse import quote_plus, quote

NEEDS_REVIEW = {"doi_mismatch_check", "author_year_guess", "not_found"}
MAILTO = "huongdt@vlute.edu.vn"

OUT_FIELDS = [
    "study_id", "author", "year", "verify_status",
    "candidate_doi", "oa_doi_returned", "oa_title_returned", "apa_title",
    "search_openalex_web", "search_openalex_api", "search_scholar",
    "correct_doi", "decision", "notes",
]


def load_module(path: Path):
    """Import 60_enrich_openalex_metadata.py to reuse parse_apa/surname."""
    spec = importlib.util.spec_from_file_location("enrich60", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def study_number(study_id: str) -> int | None:
    digits = "".join(ch for ch in study_id if ch.isdigit())
    return int(digits) if digits else None


def build_links(surname_q: str, title: str, year: str) -> tuple[str, str, str]:
    """(openalex_web, openalex_api, scholar). Prefer the title when we have it,
    else fall back to author surname; constrain by year +/-1 where possible."""
    yr = year if year.isdigit() else ""

    if title:
        web_filter = f"default.search:{title}"
        api = (f"https://api.openalex.org/works?filter=title.search:{quote(title)}"
               + (f",publication_year:{yr}" if yr else "")
               + f"&mailto={MAILTO}")
        scholar_q = f"{title} {year}".strip()
    else:
        web_filter = f"default.search:{surname_q}"
        api = (f"https://api.openalex.org/works?search={quote_plus(surname_q)}"
               + (f"&filter=publication_year:{yr}" if yr else "")
               + f"&mailto={MAILTO}")
        scholar_q = f"{surname_q} {year}".strip()

    if yr:
        web_filter += f",publication_year:{yr}"
    web = f"https://openalex.org/works?filter={quote(web_filter, safe=':,')}"
    scholar = f"https://scholar.google.com/scholar?q={quote_plus(scholar_q)}"
    return web, api, scholar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--enriched", required=True)
    ap.add_argument("--apa", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--module", default=str(Path(__file__).with_name("60_enrich_openalex_metadata.py")),
                    help="path to the enrichment script (for parse_apa/surname)")
    args = ap.parse_args()

    mod = load_module(Path(args.module))
    apa = mod.parse_apa(Path(args.apa)) if args.apa else {}

    with open(args.enriched, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    review = []
    for r in rows:
        if r.get("verify_status") not in NEEDS_REVIEW:
            continue
        num = study_number(r["study_id"])
        meta = apa.get(num, {}) if num is not None else {}
        title = meta.get("title", "")
        sn = mod.surname(r.get("author", ""))

        web, api, scholar = build_links(sn, title, r.get("year", ""))
        review.append({
            "study_id": r["study_id"],
            "author": r.get("author", ""),
            "year": r.get("year", ""),
            "verify_status": r.get("verify_status", ""),
            "candidate_doi": r.get("candidate_doi", ""),
            "oa_doi_returned": r.get("oa_doi", ""),
            "oa_title_returned": r.get("oa_title", ""),
            "apa_title": title,
            "search_openalex_web": web,
            "search_openalex_api": api,
            "search_scholar": scholar,
            "correct_doi": "",
            "decision": "",   # keep | replace | no_doi_exists
            "notes": "",
        })

    # group by status (mismatches first — most actionable), then study order
    order = {"doi_mismatch_check": 0, "author_year_guess": 1, "not_found": 2}
    review.sort(key=lambda x: (order.get(x["verify_status"], 9),
                               study_number(x["study_id"]) or 0))

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUT_FIELDS)
        writer.writeheader()
        writer.writerows(review)

    from collections import Counter
    by = Counter(x["verify_status"] for x in review)
    print(f"Review sheet written: {out_path}")
    print(f"  rows needing review : {len(review)}")
    for st in ("doi_mismatch_check", "author_year_guess", "not_found"):
        print(f"    {st:20}: {by.get(st, 0)}")
    print(f"  with known APA title: {sum(1 for x in review if x['apa_title'])}")
    print("\nReviewer fills: correct_doi, decision (keep | replace | no_doi_exists), notes.")


if __name__ == "__main__":
    main()
