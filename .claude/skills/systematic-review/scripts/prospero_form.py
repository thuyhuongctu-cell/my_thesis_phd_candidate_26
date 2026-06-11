#!/usr/bin/env python3
"""Genera borrador PROSPERO 2024 prerellenado desde project_config.yaml.

El usuario lo copia/pega en https://www.crd.york.ac.uk/PROSPERO/.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from textwrap import dedent

import yaml


TEMPLATE = """# PROSPERO — Borrador de protocolo

> Pega cada bloque en el campo correspondiente del formulario web de PROSPERO.
> Generado el {gen_date} desde `project_config.yaml`.

## 1. Title
{title}

## 2. Original language title
{title}

## 3. Anticipated or actual start date
{start_date}

## 4. Anticipated completion date
{end_date}

## 5. Stage of review at time of this submission
{stage}

## 6. Named contact
- Name: {contact_name}
- Email: {contact_email}
- Organisation: {organisation}
- ORCID: {orcid}

## 7. Named contact address
{address}

## 8. Named contact phone
{phone}

## 9. Organisational affiliation of the review
{organisation}

## 10. Review team members and their organisational affiliations
{team}

## 11. Funding sources/sponsors
{funding}

## 12. Conflicts of interest
{coi}

## 13. Collaborators
{collaborators}

## 14. Review question
{review_question}

## 15. Searches
**Databases**: {databases}

**Date of last search**: {search_date}

**Search strategy** (resumen):

```
{search_strategy}
```

Full search strategies por base en `searches/*_query.txt` del repositorio del proyecto.

## 16. URL to search strategy
{search_url}

## 17. Condition or domain being studied
{condition}

## 18. Participants/population
**Inclusion**: {population_inc}

**Exclusion**: {population_exc}

## 19. Intervention(s), exposure(s)
{intervention}

## 20. Comparator(s)/control
{comparator}

## 21. Types of study to be included
{study_types}

## 22. Context
{context}

## 23. Main outcome(s)
{main_outcomes}

## 24. Additional outcome(s)
{additional_outcomes}

## 25. Data extraction (selection and coding)
{data_extraction}

## 26. Risk of bias (quality) assessment
{rob}

## 27. Strategy for data synthesis
{synthesis}

## 28. Analysis of subgroups or subsets
{subgroups}

## 29. Type and method of review
{review_type}

## 30. Language
{language}

## 31. Country
{country}

## 32. Other registration details
{other_registrations}

## 33. Reference and/or URL for published protocol
N/A

## 34. Dissemination plans
{dissemination}

## 35. Keywords
{keywords}

## 36. Details of any existing review of the same topic by the same authors
{existing_reviews}

## 37. Current review status
Ongoing
"""


def get(d: dict, *path, default=""):
    cur = d
    for p in path:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(p, default)
    return cur if cur else default


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    args = p.parse_args()

    proj = Path(args.project_dir)
    cfg = yaml.safe_load((proj / "project_config.yaml").read_text())

    pico = get(cfg, "review", "pico", default={}) or {}
    yr = get(cfg, "review", "time_window", default={}) or {}

    dbs = [k for k, v in (get(cfg, "databases", default={}) or {}).items() if v]

    md = TEMPLATE.format(
        gen_date=datetime.utcnow().strftime("%Y-%m-%d"),
        title=get(cfg, "manuscript", "title") or get(cfg, "project", "name"),
        start_date=yr.get("start") or "[a rellenar]",
        end_date=yr.get("end") or "[a rellenar]",
        stage="Ongoing — preliminary searches completed",
        contact_name="[a rellenar]",
        contact_email="[a rellenar]",
        organisation="[a rellenar]",
        orcid="[a rellenar]",
        address="[a rellenar]",
        phone="[a rellenar]",
        team="[a rellenar]",
        funding="[a rellenar]",
        coi="None declared / [a rellenar]",
        collaborators="[a rellenar]",
        review_question=get(cfg, "review", "research_question") or "[a rellenar]",
        databases=", ".join(dbs) or "[a rellenar]",
        search_date="[fecha de la última búsqueda]",
        search_strategy="Ver searches/pubmed_query.txt y traducciones por base",
        search_url="[opcional, si protocol se publica]",
        condition="[a rellenar]",
        population_inc=pico.get("population") or "[a rellenar]",
        population_exc="[a rellenar]",
        intervention=pico.get("intervention") or "[a rellenar]",
        comparator=pico.get("comparator") or "[a rellenar]",
        study_types="RCTs, observacionales / [a rellenar]",
        context="[a rellenar]",
        main_outcomes=pico.get("outcome") or "[a rellenar]",
        additional_outcomes="[a rellenar]",
        data_extraction="Dual extraction, datos a hoja Excel (master_corpus.xlsx), discrepancias por consenso",
        rob=get(cfg, "rob_tool") or "Cochrane RoB 2 (RCTs) / ROBINS-I (no aleatorizados)",
        synthesis="Narrativa + meta-análisis si procede (random effects, metafor R)" if get(cfg, "meta_analysis", "enabled") else "Síntesis narrativa",
        subgroups="[a rellenar]",
        review_type="Systematic review",
        language=get(cfg, "manuscript", "language") or "Spanish/English",
        country="Spain",
        other_registrations="None / [a rellenar]",
        dissemination="Publicación en revista indexada y presentación en congreso",
        keywords=get(cfg, "review", "research_question") or "[a rellenar]",
        existing_reviews="None / [a rellenar]",
    )

    out = proj / "manuscript" / "protocol_prospero.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(md, encoding="utf-8")

    print(json.dumps({"ok": True, "path": str(out)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
