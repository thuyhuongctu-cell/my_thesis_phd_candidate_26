#!/usr/bin/env python3
"""
60_enrich_openalex_metadata.py — Verify + enrich the k=238 P6 study database
with authoritative metadata (DOI, journal, year, citation count, OA status)
from the OpenAlex API.

WHY THIS EXISTS
---------------
`p6/p6_primary_studies_apa7.md` was built with a knowledge-based DOI fallback
because the sandbox has no outbound network ("0/62 confirmed via live API").
Those DOIs MUST be verified against a live source before the OSF dataset is
published. This script does exactly that — it never invents a DOI; it only
records what OpenAlex returns, and flags every disagreement for manual review.

This script CANNOT run inside the Claude Code sandbox (egress is blocked:
`api.openalex.org` → HTTP 403 "Host not in allowlist"). Run it on a machine
with internet access.

WHAT IT DOES (per study)
------------------------
1. DOI path     — if a candidate DOI exists, look it up exactly via
                  GET /works/https://doi.org/{doi}; cross-check the returned
                  year + first-author surname against what we expected.
2. Title path   — no candidate DOI but a known title: filter=title.search:...
                  constrained to publication_year +/-1; pick the best match by
                  title token overlap.
3. Author+year  — last resort: search by first author + year; low confidence,
                  always flagged needs_manual_check=yes.

OpenAlex best practices applied (per the searching guide):
  * `mailto=` for the polite pool (faster, higher limit)
  * `api_key=` appended when OPENALEX_API_KEY is set (current API may require it)
  * `select=` to return only needed fields
  * `title.search:` for precise title matching (title only, not abstract)
  * exact DOI lookup via the canonical /works/{doi-url} route

USAGE
-----
  export OPENALEX_MAILTO="huongdt@vlute.edu.vn"
  export OPENALEX_API_KEY="..."        # optional; only if your account needs it
  python3 60_enrich_openalex_metadata.py \
      --db   ../data/p6_study_database.csv \
      --apa  ../p6_primary_studies_apa7.md \
      --out  ../data/p6_openalex_enriched.csv

The script is RESUMABLE: study_ids already present in --out are skipped, so you
can stop/restart across days without burning the OpenAlex daily budget twice.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import datetime
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

OPENALEX_WORKS = "https://api.openalex.org/works"
RATE_WAIT = 0.2  # ~5 req/sec, comfortably within the polite-pool limit
TITLE_OVERLAP_MIN = 0.60  # min Jaccard-ish token overlap to accept a title match
SELECT_FIELDS = ",".join([
    "id", "doi", "display_name", "publication_year",
    "authorships", "primary_location", "cited_by_count", "open_access",
])

OUTPUT_FIELDS = [
    "study_id", "author", "year",
    "candidate_doi", "oa_doi", "oa_id",
    "oa_title", "oa_year", "oa_journal",
    "cited_by_count", "is_oa", "oa_url",
    "match_method", "title_overlap", "verify_status", "needs_manual_check",
]


# ── helpers ────────────────────────────────────────────────────────────────

def norm_doi(raw: str) -> str:
    """Strip URL prefix and lowercase a DOI; return '' if not a real DOI."""
    d = (raw or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d if d.startswith("10.") else ""


def study_num(study_id: str) -> int | None:
    """S01 / S-01 / S238 -> 1 / 1 / 238."""
    m = re.search(r"(\d+)", study_id or "")
    return int(m.group(1)) if m else None


def surname(author_field: str) -> str:
    """First author's surname, lowercased. Handles 'Siddharthan & Lall',
    'Capar, N., & Kotabe, M.', 'Chiao et al.', 'Hitt et al.'."""
    a = (author_field or "").split("&")[0].split(";")[0].strip()
    a = re.sub(r"\bet\s+al\.?", "", a, flags=re.IGNORECASE).strip()
    if "," in a:
        a = a.split(",")[0].strip()   # 'Capar, N.' -> 'Capar'
    elif a.split():
        a = a.split()[0]              # 'Chiao et al.' -> 'Chiao'
    return a.lower()


def title_tokens(text: str) -> set[str]:
    text = re.sub(r"[^a-z0-9 ]", " ", (text or "").lower())
    return {w for w in text.split() if len(w) > 2}


def title_overlap(t1: str, t2: str) -> float:
    a, b = title_tokens(t1), title_tokens(t2)
    if not a or not b:
        return 0.0
    return len(a & b) / max(len(a), len(b))


# ── parse candidate DOI/title/journal from the APA7 markdown ─────────────────

APA_LINE = re.compile(r"\*\*\[S-?0*(\d+)\]\*\*\s*(.*)")
APA_YEAR = re.compile(r"\((\d{4})[a-z]?\)\.")
# title = text between '). ' (after year) and the journal italics ' *'
APA_TITLE = re.compile(r"\(\d{4}[a-z]?\)\.\s*(.+?)\.\s*\*")
APA_JOURNAL = re.compile(r"\.\s*\*([^*]+?),?\s*\d*\*")
APA_DOI = re.compile(r"https?://doi\.org/(\S+)")


def parse_apa(apa_path: Path) -> dict[int, dict]:
    """Map study number -> {candidate_doi, title, journal} from the APA7 file."""
    out: dict[int, dict] = {}
    if not apa_path or not apa_path.exists():
        return out
    for line in apa_path.read_text(encoding="utf-8").splitlines():
        m = APA_LINE.match(line.strip())
        if not m:
            continue
        num = int(m.group(1))
        rest = m.group(2)
        doi_m = APA_DOI.search(rest)
        title_m = APA_TITLE.search(rest)
        journal_m = APA_JOURNAL.search(rest)
        out[num] = {
            "candidate_doi": norm_doi(doi_m.group(1)) if doi_m else "",
            "title": title_m.group(1).strip() if title_m else "",
            "journal": journal_m.group(1).strip() if journal_m else "",
        }
    return out


# ── load the canonical 238-study list (dedup by study_id) ────────────────────

def load_studies(db_path: Path) -> list[dict]:
    seen, studies = set(), []
    with open(db_path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            sid = (row.get("study_id") or "").strip()
            if not sid or sid in seen:
                continue
            seen.add(sid)
            studies.append({
                "study_id": sid,
                "author": (row.get("author") or "").strip(),
                "year": (row.get("year") or "").strip(),
            })
    return studies


# ── OpenAlex requests ────────────────────────────────────────────────────────

def base_params() -> dict:
    p = {"select": SELECT_FIELDS}
    mailto = os.environ.get("OPENALEX_MAILTO", "").strip()
    api_key = os.environ.get("OPENALEX_API_KEY", "").strip()
    if mailto:
        p["mailto"] = mailto
    if api_key:
        p["api_key"] = api_key
    return p


def get_json(url: str, params: dict, attempts: int = 3) -> dict | None:
    for i in range(attempts):
        try:
            r = requests.get(url, params=params, timeout=30)
            if r.status_code == 404:
                return None
            if r.status_code == 429:
                time.sleep(2 ** i * 2)
                continue
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            if i == attempts - 1:
                print(f"    ! request failed: {e}")
                return None
            time.sleep(2 ** i)
    return None


def fold(s: str) -> str:
    """Lowercase + strip diacritics so 'Çapar' matches 'Capar', 'Lundström'
    matches 'Lundstrom'. OpenAlex author names carry accents the DB does not."""
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def author_matches(study_author: str, hit: dict) -> bool:
    """True if the study's first-author surname appears among ANY OpenAlex
    author on the record (diacritic-insensitive). Matching against all authors
    (not just position 0) avoids false 'mismatch' flags from name-order or
    multi-author differences, while a genuinely wrong DOI — whose author list
    shares no surname — is still rejected."""
    sn = fold(surname(study_author))
    if not sn:
        return True
    return sn in fold(hit.get("_all_authors", ""))


def flatten(rec: dict) -> dict:
    doi = norm_doi(rec.get("doi") or "")
    auths = rec.get("authorships") or []
    loc = rec.get("primary_location") or {}
    src = loc.get("source") or {}
    oa = rec.get("open_access") or {}
    author_names = [a.get("author", {}).get("display_name", "") or "" for a in auths]
    return {
        "oa_id": rec.get("id", ""),
        "oa_doi": doi,
        "oa_title": rec.get("display_name", "") or "",
        "oa_year": rec.get("publication_year", "") or "",
        "oa_journal": src.get("display_name", "") or "",
        "cited_by_count": rec.get("cited_by_count", 0),
        "is_oa": oa.get("is_oa", False),
        "oa_url": oa.get("oa_url", "") or "",
        "_first_author": author_names[0] if author_names else "",
        "_all_authors": " | ".join(author_names),
    }


def lookup_by_doi(doi: str) -> dict | None:
    rec = get_json(f"{OPENALEX_WORKS}/https://doi.org/{doi}", base_params())
    return flatten(rec) if rec else None


def search_by_title(title: str, year: str) -> dict | None:
    flt = f"title.search:{title}"
    if year.isdigit():
        y = int(year)
        flt += f",publication_year:{y - 1}-{y + 1}"
    params = base_params() | {"filter": flt, "per-page": 5}
    data = get_json(OPENALEX_WORKS, params)
    if not data:
        return None
    best, best_ov = None, 0.0
    for rec in data.get("results", []):
        ov = title_overlap(title, rec.get("display_name", ""))
        if ov > best_ov:
            best, best_ov = flatten(rec), ov
    if best and best_ov >= TITLE_OVERLAP_MIN:
        best["_title_overlap"] = round(best_ov, 2)
        return best
    return None


def search_by_author_year(author: str, year: str) -> dict | None:
    sn = surname(author)
    if not sn or not year.isdigit():
        return None
    params = base_params() | {
        "search": sn,
        "filter": f"publication_year:{year}",
        "per-page": 5,
    }
    data = get_json(OPENALEX_WORKS, params)
    if not data:
        return None
    for rec in data.get("results", []):
        flat = flatten(rec)
        if fold(sn) in fold(flat["_all_authors"]):
            return flat
    return None


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="p6_study_database.csv")
    ap.add_argument("--apa", default="", help="p6_primary_studies_apa7.md (candidate DOIs/titles)")
    ap.add_argument("--out", required=True, help="enriched output CSV (resumable)")
    ap.add_argument("--log", default="", help="JSONL provenance log (default: <out>.log.jsonl)")
    ap.add_argument("--max", type=int, default=0, help="cap studies processed this run (0 = all)")
    args = ap.parse_args()

    db_path = Path(args.db)
    apa_path = Path(args.apa) if args.apa else None
    out_path = Path(args.out)
    log_path = Path(args.log) if args.log else out_path.with_suffix(".log.jsonl")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not (os.environ.get("OPENALEX_MAILTO") or os.environ.get("OPENALEX_API_KEY")):
        print("⚠ Set OPENALEX_MAILTO (polite pool) and/or OPENALEX_API_KEY before running.\n")

    studies = load_studies(db_path)
    apa = parse_apa(apa_path) if apa_path else {}
    print(f"Loaded {len(studies)} unique studies | {len(apa)} have APA candidate metadata")

    done = set()
    if out_path.exists():
        with open(out_path, newline="", encoding="utf-8") as fh:
            done = {r["study_id"] for r in csv.DictReader(fh)}
        print(f"Resuming: {len(done)} already enriched, will skip them")

    todo = [s for s in studies if s["study_id"] not in done]
    if args.max > 0:
        todo = todo[:args.max]

    write_header = not out_path.exists()
    out_fh = open(out_path, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(out_fh, fieldnames=OUTPUT_FIELDS, extrasaction="ignore")
    if write_header:
        writer.writeheader()
    log_fh = open(log_path, "a", encoding="utf-8")

    counts = {"doi_verified": 0, "doi_mismatch": 0, "title": 0,
              "author_year": 0, "not_found": 0}

    for i, s in enumerate(todo, 1):
        num = study_num(s["study_id"])
        cand = apa.get(num, {})
        cand_doi = cand.get("candidate_doi", "")
        cand_title = cand.get("title", "")

        row = {
            "study_id": s["study_id"], "author": s["author"], "year": s["year"],
            "candidate_doi": cand_doi,
            "oa_doi": "", "oa_id": "", "oa_title": "", "oa_year": "",
            "oa_journal": cand.get("journal", ""),
            "cited_by_count": "", "is_oa": "", "oa_url": "",
            "match_method": "", "title_overlap": "",
            "verify_status": "", "needs_manual_check": "no",
        }

        hit, method = None, ""
        if cand_doi:
            hit = lookup_by_doi(cand_doi); method = "doi"
            time.sleep(RATE_WAIT)
        if not hit and cand_title:
            hit = search_by_title(cand_title, s["year"]); method = "title"
            time.sleep(RATE_WAIT)
        if not hit:
            hit = search_by_author_year(s["author"], s["year"]); method = "author_year"
            time.sleep(RATE_WAIT)

        if hit:
            row.update({k: hit[k] for k in (
                "oa_doi", "oa_id", "oa_title", "oa_year",
                "oa_journal", "cited_by_count", "is_oa", "oa_url") if hit.get(k) != ""})
            row["match_method"] = method
            row["title_overlap"] = hit.get("_title_overlap", "")

            exp_year = s["year"] if s["year"].isdigit() else ""
            year_ok = (not exp_year) or (str(hit["oa_year"]) == exp_year) \
                or abs(int(hit["oa_year"] or 0) - int(exp_year or 0)) <= 1
            author_ok = author_matches(s["author"], hit)

            if method == "doi":
                if year_ok and author_ok:
                    row["verify_status"] = "verified"
                    counts["doi_verified"] += 1
                else:
                    row["verify_status"] = "doi_mismatch_check"
                    row["needs_manual_check"] = "yes"
                    counts["doi_mismatch"] += 1
            elif method == "title":
                row["verify_status"] = "title_match"
                row["needs_manual_check"] = "no" if author_ok else "yes"
                counts["title"] += 1
            else:  # author_year
                row["verify_status"] = "author_year_guess"
                row["needs_manual_check"] = "yes"
                counts["author_year"] += 1
        else:
            row["verify_status"] = "not_found"
            row["needs_manual_check"] = "yes"
            counts["not_found"] += 1

        writer.writerow(row)
        out_fh.flush()
        log_fh.write(json.dumps({
            "ts": datetime.datetime.utcnow().isoformat() + "Z",
            "study_id": s["study_id"], "method": method,
            "verify_status": row["verify_status"],
            "candidate_doi": cand_doi, "oa_doi": row["oa_doi"],
        }, ensure_ascii=False) + "\n")
        log_fh.flush()

        if i % 10 == 0 or i == len(todo):
            print(f"  {i}/{len(todo)} | verified={counts['doi_verified']} "
                  f"mismatch={counts['doi_mismatch']} title={counts['title']} "
                  f"authoryr={counts['author_year']} notfound={counts['not_found']}")

    out_fh.close()
    log_fh.close()

    print("\n" + "=" * 60)
    print("OpenAlex enrichment complete")
    for k, v in counts.items():
        print(f"  {k:18s}: {v}")
    print(f"\nOutput : {out_path}")
    print(f"Log    : {log_path}")
    print("\nNEXT: open the CSV, manually confirm every row where "
          "needs_manual_check=yes (DOI mismatches, author-year guesses, not-found).")


if __name__ == "__main__":
    main()
