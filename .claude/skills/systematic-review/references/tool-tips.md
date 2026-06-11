# Tips de operadores y sintaxis por base de datos

## PubMed (E-utilities)

- **MeSH explosion**: `"Sinusitis"[MeSH]` (incluye términos hijos).
- **MeSH sin explosión**: `"Sinusitis"[Mesh:NoExp]`.
- **Major topic**: `"Asthma"[MAJR]`.
- **Field tags**: `[Title]`, `[Title/Abstract]`, `[Author]`, `[Journal]`, `[Affiliation]`.
- **Date filter**: `2015:2026[Publication Date]`.
- **Type filter**: `Randomized Controlled Trial[Publication Type]`, `Systematic Review[Publication Type]`.
- **Boolean**: `AND` `OR` `NOT` en mayúsculas.
- **Truncamiento**: `child*` (busca child, children, childhood).
- **Frase exacta**: `"sleep apnea"`.

**Ejemplo (CRSwNP + biológicos)**:
```
("Sinusitis"[MeSH] OR "chronic rhinosinusitis"[Title/Abstract])
AND ("nasal polyps"[MeSH] OR "nasal polyps"[Title/Abstract])
AND (dupilumab[Title/Abstract] OR omalizumab[Title/Abstract] OR mepolizumab[Title/Abstract])
AND 2018:2026[Publication Date]
```

## Semantic Scholar Graph API

- Texto libre, sin sintaxis Boolean estricta — funciona como búsqueda semántica.
- Filtros en parámetro `year=2015-2026`, `fieldsOfStudy=Medicine`.
- `paper/search/bulk` permite paginación con `token` (cursor).

## OpenAlex

- Búsqueda completa: `?search=keywords`.
- Filtros: `from_publication_date:2015-01-01`, `to_publication_date:2026-12-31`.
- Tipo de obra: `type:journal-article`.
- Acceso: `is_oa:true`.

## Web of Science (Core Collection)

Sintaxis Advanced Search:
- `TS=` Topic (title + abstract + keywords + KeyWords Plus).
- `TI=` Title only.
- `AU=` Author.
- `SO=` Journal name.
- `PY=` Publication year.
- `DT=` Document type (`Article`, `Review`, `Meeting Abstract`).
- **Wildcards**: `*` cualquier cadena, `?` un caracter.
- **Proximidad**: `NEAR/3` (palabras a ≤3 de distancia).

**Ejemplo CRSwNP + biológicos**:
```
TS=("chronic rhinosinusitis" OR "nasal polyposis")
AND TS=(dupilumab OR omalizumab OR mepolizumab OR benralizumab)
AND PY=2018-2026
AND DT=(Article OR Review)
```

Export: marca todos → Export → "Other File Formats" → "RIS (for Reference Manager)" → "Full Record". Máximo 1000 records por export (itera si hay más).

## Embase (vía Ovid o Embase.com)

Sintaxis Emtree:
- `'term'/exp` — explosión (incluye términos hijos).
- `'term'/de` — descriptor exacto sin explosión.
- `'term'/mj` — major focus.
- `:ti` `:ab` `:ti,ab,kw` — campos.
- **Trunc**: `*` al final.
- **Adyacencia**: `NEXT/3`.

**Ejemplo**:
```
'chronic sinusitis'/exp AND 'nasal polyp'/exp
AND ('dupilumab'/exp OR 'omalizumab'/exp OR 'mepolizumab'/exp)
AND [2018-2026]/py
AND ('article'/it OR 'review'/it)
```

Export: results → ⋮ menu → Export → Format **"RIS"** → "Selected records" or "All". Máximo 10000 por export.

## Filtros de tipo de estudio recomendados por la Cochrane

- **Cochrane Highly Sensitive Search Strategy** (RCT filter PubMed): https://training.cochrane.org/handbook/current/chapter-04#section-4-4-7
- **SIGN search filters**: https://www.sign.ac.uk/what-we-do/methodology/search-filters/

## Manejo de paginación / rate limits

| Base | Limit (sin key) | Workaround |
|------|-----------------|------------|
| PubMed E-utilities | 3 req/s | API key NCBI gratis → 10 req/s |
| Semantic Scholar | 100 req/5min | API key → 1 req/s sostenido |
| OpenAlex | 100k/día con email | Añade `mailto=tu@email` para entrar en "polite pool" |
| WoS | UI sin límite documentado | Export 1000/vez, itera con paginación |
| Embase | UI sin límite | Export 10000/vez |
| CrossRef | 50 req/s polite | User-Agent con email |
