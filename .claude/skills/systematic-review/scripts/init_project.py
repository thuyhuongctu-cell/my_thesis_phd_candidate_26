#!/usr/bin/env python3
"""Crea estructura de carpetas de proyecto para una RS.

Uso:
    python init_project.py <slug-tema> --config-stdin
    (recibe YAML del briefing por stdin)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml  # pyyaml


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[áàä]", "a", s)
    s = re.sub(r"[éèë]", "e", s)
    s = re.sub(r"[íìï]", "i", s)
    s = re.sub(r"[óòö]", "o", s)
    s = re.sub(r"[úùü]", "u", s)
    s = re.sub(r"ñ", "n", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s[:60] or "sr-untitled"


DEFAULT_CONFIG: dict = {
    "project": {
        "name": "",
        "slug": "",
        "created_at": None,
        "language": "es",
    },
    "review": {
        "research_question": "",
        "pico": {
            "population": "",
            "intervention": "",
            "comparator": "",
            "outcome": "",
        },
        "type": "intervention",  # intervention|diagnostic|qualitative|scoping
        "time_window": {"start": None, "end": None},
    },
    "databases": {
        "pubmed": True,
        "semantic_scholar": True,
        "openalex": True,
        "consensus": "auto",  # auto = si MCP disponible
        "wos": False,         # se setea por el usuario en Fase 1
        "embase": False,
    },
    "api_keys": {
        "semantic_scholar": "",
        "ncbi_email": "",
        "ncbi_api_key": "",
    },
    "institutional_access": {
        "wos_url": "",        # rellena en primera ejecución de Fase 3.3
        "embase_url": "",
    },
    "screening": {
        "include_keywords": [],
        "exclude_keywords": [],
        "min_include_hits": 2,
    },
    "meta_analysis": {
        "enabled": False,
        "effect_measure": "",   # OR, RR, MD, SMD
    },
    "rob_tool": "",  # se elige en Fase 8
    "manuscript": {
        "title": "",
        "target_journal": "",
        "language": "es",
    },
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("slug_or_title", help="Slug o título de la RS")
    p.add_argument("--config-stdin", action="store_true")
    p.add_argument("--base-dir", default=None, help="Override carpeta destino")
    args = p.parse_args()

    base = Path(args.base_dir) if args.base_dir else Path.home() / "Desktop" / "terminal" / "Publicaciones"
    slug = slugify(args.slug_or_title)
    proj = base / slug

    if proj.exists():
        print(f"[init] Proyecto ya existe en {proj}", file=sys.stderr)
        # No sobreescribimos — la skill decide qué hacer
        print(json.dumps({"ok": False, "exists": True, "path": str(proj)}))
        return 2

    proj.mkdir(parents=True, exist_ok=False)
    (proj / "searches").mkdir()
    (proj / "manuscript").mkdir()

    cfg = json.loads(json.dumps(DEFAULT_CONFIG))  # deep copy
    cfg["project"]["name"] = args.slug_or_title
    cfg["project"]["slug"] = slug
    cfg["project"]["created_at"] = datetime.utcnow().isoformat() + "Z"

    if args.config_stdin:
        try:
            patch = yaml.safe_load(sys.stdin.read()) or {}
            # merge superficial
            for k, v in patch.items():
                if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                    cfg[k].update(v)
                else:
                    cfg[k] = v
        except yaml.YAMLError as e:
            print(f"[init] YAML inválido: {e}", file=sys.stderr)
            return 1

    (proj / "project_config.yaml").write_text(
        yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    state = {
        "current_phase": 1,
        "completed_phases": [0],
        "search_cursors": {},
        "counts": {},
        "errors": [],
    }
    (proj / "project_state.json").write_text(json.dumps(state, indent=2), encoding="utf-8")

    print(json.dumps({"ok": True, "path": str(proj), "slug": slug}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
