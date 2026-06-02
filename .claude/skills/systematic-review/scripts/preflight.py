#!/usr/bin/env python3
"""Preflight check para systematic-review skill.

Comprueba Python, pip packages, pandoc, R+metafor, Playwright, y emite JSON a stdout
con `ok`/`missing` por categoría. La skill lee el JSON y decide qué instalar.

Uso:
    python preflight.py [--with-r] [--json-only]
"""
from __future__ import annotations

import importlib
import json
import shutil
import subprocess
import sys
from typing import Any


PIP_PACKAGES = [
    "requests",
    "openpyxl",
    "rispy",
    "rapidfuzz",
    "docx",        # python-docx
    "lxml",
    "yaml",        # pyyaml
    "playwright",
    "matplotlib",
]

PIP_INSTALL_NAMES = {
    "docx": "python-docx",
    "yaml": "pyyaml",
}


def check_python() -> dict[str, Any]:
    v = sys.version_info
    ok = (v.major, v.minor) >= (3, 10)
    return {
        "ok": ok,
        "version": f"{v.major}.{v.minor}.{v.micro}",
        "install_cmd": "brew install python@3.12" if not ok else None,
    }


def check_pip_package(mod: str) -> dict[str, Any]:
    try:
        importlib.import_module(mod)
        return {"ok": True}
    except ImportError:
        return {
            "ok": False,
            "install_cmd": f"pip install {PIP_INSTALL_NAMES.get(mod, mod)}",
        }


def check_pandoc() -> dict[str, Any]:
    path = shutil.which("pandoc")
    if not path:
        return {"ok": False, "install_cmd": "brew install pandoc"}
    try:
        out = subprocess.check_output(["pandoc", "--version"], text=True).split("\n")[0]
        return {"ok": True, "version": out, "path": path}
    except subprocess.SubprocessError as e:
        return {"ok": False, "error": str(e), "install_cmd": "brew install pandoc"}


def check_r_metafor() -> dict[str, Any]:
    rscript = shutil.which("Rscript")
    if not rscript:
        return {
            "ok": False,
            "r_installed": False,
            "install_cmd": "brew install --cask r",
        }
    try:
        subprocess.check_output(
            ["Rscript", "-e", 'suppressMessages(library(metafor))'],
            stderr=subprocess.STDOUT,
            text=True,
        )
        return {"ok": True, "r_installed": True}
    except subprocess.CalledProcessError:
        return {
            "ok": False,
            "r_installed": True,
            "install_cmd": 'Rscript -e \'install.packages("metafor", repos="https://cloud.r-project.org")\'',
        }


def check_playwright_browser() -> dict[str, Any]:
    try:
        importlib.import_module("playwright")
    except ImportError:
        return {"ok": False, "package": False, "install_cmd": "pip install playwright && python -m playwright install chromium"}
    try:
        out = subprocess.run(
            [sys.executable, "-m", "playwright", "install", "--dry-run", "chromium"],
            capture_output=True, text=True, timeout=20,
        )
        installed = "is already installed" in (out.stdout + out.stderr).lower() or out.returncode == 0
        return {"ok": installed, "package": True, "install_cmd": None if installed else "python -m playwright install chromium"}
    except (subprocess.SubprocessError, FileNotFoundError):
        return {"ok": False, "package": True, "install_cmd": "python -m playwright install chromium"}


def check_mcp_inventory() -> dict[str, Any]:
    """Reporta los MCPs que esperamos. Claude (no este script) sabe cuáles tiene."""
    return {
        "expected": [
            "mcp__claude_ai_PubMed__*",
            "mcp__zotero__*",
            "mcp__notebooklm-mcp__*",
            "mcp__playwright__*",
            "mcp__claude_ai_Consensus__*  (opcional)",
        ],
        "note": "Claude debe inventariar tools disponibles. Consensus no es bloqueante.",
    }


def main() -> int:
    with_r = "--with-r" in sys.argv
    json_only = "--json-only" in sys.argv

    report: dict[str, Any] = {
        "python": check_python(),
        "pip": {mod: check_pip_package(mod) for mod in PIP_PACKAGES},
        "pandoc": check_pandoc(),
        "playwright": check_playwright_browser(),
        "mcp": check_mcp_inventory(),
    }
    if with_r:
        report["r_metafor"] = check_r_metafor()

    missing_pip = [m for m, v in report["pip"].items() if not v["ok"]]
    blockers = []
    warnings = []
    if not report["python"]["ok"]:
        blockers.append("python>=3.10")
    if missing_pip:
        blockers.append(f"pip:{','.join(missing_pip)}")
    if not report["pandoc"]["ok"]:
        warnings.append("pandoc (opcional — no necesario para .docx vía python-docx)")
    if not report["playwright"]["ok"]:
        blockers.append("playwright-browser")
    if with_r and not report["r_metafor"]["ok"]:
        blockers.append("R+metafor")

    report["summary"] = {
        "ok": len(blockers) == 0,
        "blockers": blockers,
        "warnings": warnings,
        "aggregated_pip_install": (
            f"pip install {' '.join(PIP_INSTALL_NAMES.get(m, m) for m in missing_pip)}"
            if missing_pip else None
        ),
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not json_only and blockers:
        print(f"\n[preflight] Bloqueantes: {', '.join(blockers)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
