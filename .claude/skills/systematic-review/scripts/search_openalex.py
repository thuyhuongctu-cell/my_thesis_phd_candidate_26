#!/usr/bin/env python3
"""Busca OpenAlex con cursor pagination. Libre, sin API key.

Lee `<project_dir>/searches/openalex_query.txt`. Escribe `raw_openalex.json`.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests
import yaml

API = "https://api.openalex.org/works"
USER_AGENT = "systematic-review-skill/1.0"


def normalize(w: dict) -> dict:
    ids = w.get("ids") or {}
    auths = [(a.get("author") or {}).get("display_name", "") for a in (w.get("authorships") or [])]
    abst_inv = w.get("abstract_inverted_index") or {}
    if abst_inv:
        pos_map: dict[int, str] = {}
        for word, positions in abst_inv.items():
            for pos in positions:
                pos_map[pos] = word
        abstract = " ".join(pos_map[k] for k in sorted(pos_map))
    else:
        abstract = ""

    return {
        "source": "openalex",
        "source_id": w.get("id", "").split("/")[-1],
        "doi": (ids.get("doi", "") or "").replace("https://doi.org/", ""),
        "title": w.get("title") or w.get("display_name") or "",
        "authors": auths,
        "year": str(w.get("publication_year") or ""),
        "journal": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "") or "",
        "abstract": abstract,
        "keywords": [c.get("display_name", "") for c in (w.get("concepts") or [])[:8]],
        "url": w.get("id", ""),
        "citation_count": w.get("cited_by_count", 0),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    ap.add_argument("--max", type=int, default=10000)
    args = ap.parse_args()

    proj = Path(args.project_dir)
    query = (proj / "searches" / "openalex_query.txt").read_text(encoding="utf-8").strip()
    cfg = yaml.safe_load((proj / "project_config.yaml").read_text())
    yr = cfg.get("review", {}).get("time_window") or {}
    email = (cfg.get("api_keys") or {}).get("ncbi_email") or ""

    state_path = proj / "project_state.json"
    state = json.loads(state_path.read_text())
    cursor = state.get("search_cursors", {}).get("openalex") or "*"
    if cursor == "complete":
        print("[oa] ya completado", file=sys.stderr)
        return 0

    raw_path = proj / "searches" / "raw_openalex.json"
    records: list[dict] = json.loads(raw_path.read_text()) if raw_path.exists() else []

    filters = []
    if yr.get("start"):
        filters.append(f"from_publication_date:{yr['start']}-01-01")
    if yr.get("end"):
        filters.append(f"to_publication_date:{yr['end']}-12-31")

    params = {
        "search": query,
        "per-page": 200,
        "cursor": cursor,
    }
    if filters:
        params["filter"] = ",".join(filters)
    if email:
        params["mailto"] = email

    headers = {"User-Agent": USER_AGENT}

    while True:
        for attempt in range(5):
            r = requests.get(API, params=params, headers=headers, timeout=60)
            if r.status_code == 200:
                break
            time.sleep(2 ** attempt)
        else:
            print("[oa] error persistente", file=sys.stderr)
            return 1

        body = r.json()
        results = body.get("results", [])
        records.extend(normalize(w) for w in results)
        raw_path.write_text(json.dumps(records, indent=2, ensure_ascii=False))

        meta = body.get("meta", {})
        next_cursor = meta.get("next_cursor")
        state["search_cursors"]["openalex"] = next_cursor or "complete"
        state_path.write_text(json.dumps(state, indent=2))

        print(f"[oa] acumulado {len(records)}/{meta.get('count', '?')}", file=sys.stderr)
        if not next_cursor or len(records) >= args.max or not results:
            break
        params["cursor"] = next_cursor
        time.sleep(0.5)

    state["search_cursors"]["openalex"] = "complete"
    state.setdefault("counts", {})["identificados_openalex"] = len(records)
    state_path.write_text(json.dumps(state, indent=2))
    print(json.dumps({"ok": True, "count": len(records)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
