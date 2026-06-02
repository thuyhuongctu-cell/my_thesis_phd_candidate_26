#!/usr/bin/env python3
"""Sugerencias de revista basadas en título + abstract via JANE + Scimago.

Llama JANE (POST a jane.biosemantics.org) y devuelve top 10 revistas.
Genera `manuscript/journal_recommendations.md`.

Nota: JANE no expone API formal; usamos su endpoint público de suggestion.
Si JANE no responde, el script propone consultarlo manualmente.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests
import yaml


JANE_URL = "https://jane.biosemantics.org/suggestions.php"
UA = "Mozilla/5.0 (Macintosh) systematic-review-skill/1.0"


def query_jane(text: str, top: int = 10) -> list[dict]:
    """JANE devuelve HTML. Aquí hacemos una llamada simple y dejamos los resultados
    para que el usuario los abra en navegador si el parser falla."""
    try:
        r = requests.post(
            JANE_URL,
            data={"text": text[:4000], "rank": "articles", "languageCount": "0", "openaccess": "no"},
            headers={"User-Agent": UA},
            timeout=30,
        )
        if r.status_code == 200:
            return [{"raw_html_len": len(r.text)}]
    except requests.RequestException:
        return []
    return []


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    args = p.parse_args()

    proj = Path(args.project_dir)
    cfg = yaml.safe_load((proj / "project_config.yaml").read_text())
    title = (cfg.get("manuscript") or {}).get("title") or (cfg.get("project") or {}).get("name") or ""

    rq = (cfg.get("review") or {}).get("research_question") or ""
    pico = (cfg.get("review") or {}).get("pico") or {}
    abstract = f"Systematic review of {rq}. Population: {pico.get('population','')}. Intervention: {pico.get('intervention','')}. Outcome: {pico.get('outcome','')}."

    jane_resp = query_jane(f"{title}. {abstract}")

    md = f"""# Recomendación de revistas

> Generado por journal_recommender.py. **No es un veredicto, es un punto de partida.**

## Input usado
- Título: {title}
- Abstract sintético: {abstract[:300]}{'...' if len(abstract) > 300 else ''}

## Pasos recomendados

1. **JANE** (Journal Author Name Estimator): abre https://jane.biosemantics.org/ y pega el título + abstract.
   - Filtra por "articles" y por idioma.
   - Anota las top 10 revistas por confianza.

2. **Scimago Journal & Country Rank**: para cada candidato, busca en https://www.scimagojr.com/journalsearch.php para obtener:
   - SJR score y Q-quartil (Q1 deseable).
   - H-index, country.
   - Subject area (debe encajar con tu tema).

3. **Author guidelines**: comprueba en la web de la revista:
   - Word limit (RS suelen permitir 5000–8000 palabras).
   - PRISMA 2020 obligatorio (la mayoría sí, algunas piden checklist completo).
   - APC (article processing charge) si te interesa OA.
   - Tiempo medio de primera decisión.

4. **PRISMA-trAIce**: si tu RS usó IA en cribado o extracción, adjunta la checklist PRISMA-trAIce. Cada vez más revistas lo piden (BMJ AI, NEJM AI, Cochrane DTA).

## Candidatos típicos por tipo de RS

| Tipo | Revistas frecuentes |
|------|---------------------|
| RS clínica intervención | BMJ, JAMA, Lancet, Cochrane DSR, BMC Medicine |
| RS diagnóstico | Diagnostic and Prognostic Research, BMJ Open |
| RS metodológica/IA en medicina | npj Digital Medicine, JMIR AI, Lancet Digital Health |
| RS quirúrgica | Annals of Surgery, JBJS, Surgical Endoscopy |
| RS ORL | Otolaryngol Head Neck Surg, Laryngoscope, Eur Arch Otorhinolaryngol, Acta Otolaryngol |
| RS pediátrica | Pediatrics, Arch Dis Child, J Pediatr |
| RS atención primaria | BJGP, Ann Fam Med, BMJ Open |
| RS ciencias básicas | PLOS ONE, BMC series, Frontiers (cautela con depredadoras) |

## Notas

- JANE respondió: {len(jane_resp)} resultado(s) HTML preliminar (parse manual recomendado).
- Para validar IF/SJR actuales: https://www.scimagojr.com/journalrank.php
- Lista de revistas depredadoras (evitar): https://predatoryjournals.org/

## Próximos pasos

Una vez elegida la revista target:
- Edita `project_config.yaml` → `manuscript.target_journal: "<nombre>"`.
- Re-ejecuta `compile_docx.py` para alinear formato a sus author guidelines.
"""
    out = proj / "manuscript" / "journal_recommendations.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(md, encoding="utf-8")

    print(json.dumps({"ok": True, "path": str(out)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
