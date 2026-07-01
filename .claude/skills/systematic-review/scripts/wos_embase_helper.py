#!/usr/bin/env python3
"""Helper para WoS/Embase semi-automatizado vía Playwright.

El flujo Playwright real lo orquesta la skill con los tools `mcp__playwright__*`
porque requiere intervención del usuario (login SSO/2FA).

Este script solo:
  1. Verifica que existe el archivo descargado en la carpeta del proyecto.
  2. Valida que es un RIS parseable (cuenta entradas).
  3. Renombra/mueve a `searches/raw_<source>.ris`.
  4. Reporta a stdout.

Uso:
    python wos_embase_helper.py <project_dir> --source wos|embase --downloaded-file <path>
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import rispy


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--source", choices=["wos", "embase"], required=True)
    p.add_argument("--downloaded-file", required=True, help="Path al archivo recién descargado")
    args = p.parse_args()

    src_file = Path(args.downloaded_file).expanduser()
    if not src_file.exists():
        print(json.dumps({"ok": False, "error": f"no existe {src_file}"}))
        return 1

    proj = Path(args.project_dir)
    searches = proj / "searches"
    searches.mkdir(parents=True, exist_ok=True)
    target = searches / f"raw_{args.source}.ris"

    # Si ya existe, hacemos append-merge
    if target.exists():
        existing = target.read_text(encoding="utf-8", errors="replace")
        new = src_file.read_text(encoding="utf-8", errors="replace")
        target.write_text(existing + "\n" + new, encoding="utf-8")
    else:
        shutil.copy2(src_file, target)

    # Validar parseable
    with target.open("r", encoding="utf-8", errors="replace") as f:
        try:
            entries = rispy.load(f)
        except Exception as e:  # noqa: BLE001
            print(json.dumps({"ok": False, "error": f"RIS no parseable: {e}", "path": str(target)}))
            return 1

    print(json.dumps({"ok": True, "path": str(target), "entries": len(entries)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
