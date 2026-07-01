---
name: systematic-review
version: 1.0.0
description: |
  Revisión sistemática PRISMA 2020 con la máxima automatización posible. Una sola
  invocación con el tema y la skill: (0) hace preflight de herramientas e instala
  lo que falte, (1) recoge briefing con UNA pregunta, (2) propone estrategia de
  búsqueda editable, (3) ejecuta búsquedas en PubMed + Semantic Scholar + OpenAlex
  + Consensus (si MCP disponible) + WoS/Embase (semiautomatizado vía Playwright
  con login del usuario), (4) consolida en master_corpus.xlsx con DOIs hipervínculo
  + verificación CrossRef, (5) dedupea por DOI y título fuzzy, (6) cribado Pass 1
  automático por reglas keyword, (7) cribado Pass 2 asistido (IA propone, usuario
  firma), (8) RoB con tool adecuado al design, (9) meta-análisis opcional con R+metafor,
  (10) diagrama PRISMA 2020, (11) borrador PROSPERO listo para pegar, (12) recomendación
  de revistas con SJR/IF/JANE, (13) manuscrito Word con marcadores Zotero RTF/ODF
  Scan, (14) checklist PRISMA-trAIce si se usó IA. Invocar cuando el usuario diga
  "revisión sistemática", "RS PRISMA", "PROSPERO", "meta-análisis sobre X". NO
  para revisiones narrativas — usa consensus-research para eso.
license: MIT
allowed-tools:
  - mcp__claude_ai_PubMed__search_articles
  - mcp__claude_ai_PubMed__get_article_metadata
  - mcp__claude_ai_PubMed__lookup_article_by_citation
  - mcp__claude_ai_PubMed__find_related_articles
  - mcp__claude_ai_Consensus__search
  - mcp__zotero__zotero_create_collection
  - mcp__zotero__zotero_add_by_doi
  - mcp__zotero__zotero_search_items
  - mcp__zotero__zotero_get_collections
  - mcp__notebooklm-mcp__notebook_create
  - mcp__notebooklm-mcp__source_add
  - mcp__playwright__browser_navigate
  - mcp__playwright__browser_snapshot
  - mcp__playwright__browser_click
  - mcp__playwright__browser_type
  - mcp__playwright__browser_press_key
  - mcp__playwright__browser_wait_for
  - mcp__playwright__browser_fill_form
  - mcp__playwright__browser_select_option
  - mcp__playwright__browser_evaluate
  - mcp__playwright__browser_tabs
  - mcp__playwright__browser_file_upload
  - Read
  - Write
  - Edit
  - Bash
  - AskUserQuestion
  - WebFetch
  - WebSearch
---

# Systematic Review v1.0

Skill para **revisiones sistemáticas formales PRISMA 2020** con registro PROSPERO.
Hermana de `consensus-research` (que es narrativa, no sistemática).

Comunicación con el usuario siempre en **español**, salvo que pida lo contrario.
Citas a papers en idioma original. Prosa larga del manuscrito pasada por la skill
**`humanizer`** antes de presentarla.

---

## Reglas operativas (todas las fases)

1. **Nunca fabricar DOIs, PMIDs ni metadatos.** Si no se verifica, se etiqueta como `unverified`.
2. **Persistencia antes de procesado.** Toda respuesta de API se guarda en disco como JSON crudo antes de transformarse — si algo cae a mitad, se reanuda.
3. **Cribado de full-text NO se automatiza.** La IA propone, el usuario firma. Es la línea metodológica.
4. **Una sola `AskUserQuestion` cuando se necesitan N datos del usuario.** Nunca dos asks consecutivos.
5. **Idioma:** conversación en español; manuscrito en el idioma que pida el usuario; títulos de papers en idioma original.
6. **PRISMA-trAIce:** si la skill ejecuta cribado asistido por IA, al final se genera la checklist PRISMA-trAIce (17 items, Holst 2025) para que se incluya en el manuscrito.

---

## Carpeta del proyecto

Todo lo de una RS vive en `~/Desktop/terminal/Publicaciones/<slug-tema>/`:

```
project_config.yaml         # tema, PICO, queries, thresholds (editable)
project_state.json          # estado del pipeline (resumible)
searches/
  pubmed_query.txt          # query final pubmed
  semantic_scholar_query.txt
  openalex_query.txt
  consensus_queries.json
  wos_query.txt             # listo para pegar / Playwright lo usa
  embase_query.txt
  raw_pubmed.json           # respuestas crudas paginadas
  raw_semantic_scholar.json
  raw_openalex.json
  raw_consensus.json
  raw_wos.ris               # exportado vía Playwright o manual
  raw_embase.ris
master_corpus.xlsx          # HOJA MAESTRA — pieza central del usuario
duplicates_log.csv
screening_pass1_log.csv
screening_pass2_log.csv
rob_assessments.xlsx
prisma_flow.png             # diagrama PRISMA 2020
prisma_flow.json            # contadores
meta_analysis/              # solo si hay MA
  forest_plot.png
  funnel_plot.png
  rob_summary.png
  ma_script.R               # editable
manuscript/
  protocol_prospero.md      # borrador PROSPERO para copiar/pegar
  journal_recommendations.md
  manuscript.docx           # PRISMA 2020 con marcadores RTF/ODF Scan
  prisma_traice_checklist.md
```

---

## FASE 0 — Preflight de herramientas (obligatoria, antes de TODO)

Antes de pedir nada al usuario, lanza:

```bash
python ~/.claude/skills/systematic-review/scripts/preflight.py
```

El script comprueba:

| Categoría | Comprobación |
|-----------|--------------|
| Python | versión ≥ 3.10 |
| Pip packages | `requests`, `openpyxl`, `rispy`, `rapidfuzz`, `python-docx`, `lxml`, `pyyaml` |
| Pandoc | `pandoc --version` (para .docx) |
| R + metafor | `Rscript -e 'library(metafor)'` (solo si el usuario quiere MA — preguntar en Fase 1) |
| Playwright Python | `python -c "import playwright"` + `playwright install chromium` |
| MCPs de Claude | inventariar tools disponibles: PubMed, Zotero, NotebookLM, Playwright, Consensus |

El script devuelve JSON a stdout con `ok` / `missing` / `install_cmd` por cada ítem.

**Si falta algo:**
- Para pip packages: presenta el `pip install ...` agregado y ofrece ejecutarlo con permiso del usuario.
- Para pandoc: propone `brew install pandoc`.
- Para R + metafor: propone `brew install --cask r` + `Rscript -e 'install.packages("metafor")'`. Solo si el usuario va a hacer MA.
- Para Playwright: ofrece `pip install playwright && python -m playwright install chromium`.
- Para MCPs faltantes (e.g. Consensus): muestra el link de instalación pero **no bloquea** — degrada con aviso.

**No avances a Fase 1** hasta que el preflight pase (o el usuario decida saltarse partes opcionales).

---

## FASE 1 — Briefing (UNA AskUserQuestion)

Una sola llamada con todas las preguntas agrupadas:

1. **Tema y pregunta de investigación** (texto libre).
2. **PICO** (intervención, comparador, outcome — o "scoping" si no aplica).
3. **¿Acceso institucional a WoS/Embase?** (sí/no → si no, esas bases se omiten con aviso).
4. **¿API key Semantic Scholar?** (opcional, mejora rate limit).
5. **¿Vas a hacer meta-análisis?** (sí/no → si sí, preflight R+metafor).
6. **Idioma del manuscrito** (es/en por defecto).
7. **Ventana temporal** (e.g. 2015–2026; vacío = sin filtro).

Si el usuario solo da el tema y dice "lo demás como tú veas", aplica defaults:
- PICO: deja la skill inferirlo del tema y mostrar la propuesta en Fase 2.
- WoS/Embase: asume sí (la mayoría con licencia FECYT lo tienen).
- API S2: no (degrada a rate más bajo).
- MA: no (la mayoría de RS no lo requieren).
- Idioma: español.
- Ventana: 10 años atrás → hoy.

Tras el briefing, llama:
```bash
python ~/.claude/skills/systematic-review/scripts/init_project.py "<slug-tema>" --config-stdin
```
pasándole el YAML del briefing por stdin. El script crea la carpeta del proyecto, `project_config.yaml` y `project_state.json` inicial.

---

## FASE 2 — Estrategia de búsqueda (propuesta, EDITABLE)

Genera y muestra al usuario:

1. **Master query Boolean** estructurado por *concept blocks* (P AND I AND C AND O, cada bloque con OR de sinónimos).
2. **Traducciones por base:**
   - **PubMed**: con MeSH terms (e.g. `"Sinusitis"[MeSH]`) y field tags.
   - **Semantic Scholar**: free text + año.
   - **OpenAlex**: free text + filtros.
   - **WoS**: sintaxis `TS=("X" OR "Y") AND TS=("A" OR "B")`.
   - **Embase**: sintaxis Emtree con `/exp` para explosión y `/de` para descriptor exacto.
   - **Consensus** (si MCP disponible): 3–5 queries en lenguaje natural.

Presenta en tabla. **Pide confirmación o ediciones** antes de gastar API calls. Escribe los queries finales en `searches/*_query.txt`.

Si el usuario edita, regenera la traducción a cada base preservando su intención.

---

## FASE 3 — Ejecución de búsquedas

### 3.1 Detección de MCPs

Antes de buscar, lista MCPs disponibles. Para Consensus, comprueba si `mcp__claude_ai_Consensus__search` está en tu toolset.
- Si no está, di al usuario: *"No tengo conector con Consensus. ¿Quieres que te muestre cómo añadirlo en Claude Code o seguimos sin él?"* — y sigue sin él si no quiere instalarlo.

### 3.2 Búsquedas con API libre (paralelo, con rate-limit honesto)

```bash
python ~/.claude/skills/systematic-review/scripts/search_pubmed.py "<project_dir>"
python ~/.claude/skills/systematic-review/scripts/search_semantic_scholar.py "<project_dir>"
python ~/.claude/skills/systematic-review/scripts/search_openalex.py "<project_dir>"
```

Estos scripts:
- Leen `searches/<base>_query.txt`.
- Paginan en lotes (PubMed retmax=200, S2 cursor, OpenAlex cursor).
- Persisten cada lote a `raw_<base>.json` antes de seguir.
- Reintentan con backoff exponencial en 429.
- Si se interrumpe, retoman desde el último cursor guardado en `project_state.json`.

Para **Consensus** (si MCP disponible), ejecuta los queries del JSON de `consensus_queries.json` desde Claude (no script), máximo 3 paralelos, espera 30 s si rate-limit, guarda resultados en `raw_consensus.json` con el formato común.

### 3.3 WoS y Embase semiautomatizados (Playwright MCP)

Solo si el usuario marcó "sí, tengo acceso". Flujo:

1. La skill abre WoS (o Embase) con `mcp__playwright__browser_navigate` a la URL de la institución del usuario (preguntar la primera vez, guardar en `project_config.yaml`).
2. **Le pide al usuario que haga el login (SSO/FECYT/OpenAthens) en la ventana de Playwright** y diga "listo" cuando esté dentro.
3. La skill toma el control vía Playwright:
   - Pega el query (`browser_type` en el campo de Advanced Search).
   - Espera a la página de resultados (`browser_wait_for`).
   - Marca "Select all" → Export → RIS (o "Plain text full record" en WoS) → descarga.
   - Si hay paginación (WoS exporta 1000/vez), itera.
4. Mueve el archivo descargado a `searches/raw_wos.ris` o `raw_embase.ris`.
5. Llama:
   ```bash
   python ~/.claude/skills/systematic-review/scripts/parse_ris.py "<project_dir>" --source wos
   python ~/.claude/skills/systematic-review/scripts/parse_ris.py "<project_dir>" --source embase
   ```
   Que parsea el RIS y normaliza al schema común (igual que pubmed/s2).

**Fallback si Playwright falla:** muestra al usuario el query y las instrucciones manuales paso a paso. La skill solo necesita el archivo `.ris` en la carpeta para seguir.

### 3.4 Estado tras Fase 3

`project_state.json` registra cuántos hits por fuente. Si una fuente devuelve >2000, avisa: "demasiado amplio, propón refinar o sigue con todos". Si <10, avisa: "puede que el query sea muy estrecho".

---

## FASE 4 — Master corpus Excel

```bash
python ~/.claude/skills/systematic-review/scripts/build_master_xlsx.py "<project_dir>"
```

El script:
- Lee todos los `raw_*.json` y normaliza al schema común.
- Genera `master_corpus.xlsx` con `openpyxl`.
- Cada DOI es **hyperlink real de Excel** apuntando a `https://doi.org/<DOI>`.
- Columnas: `id, source, source_id, doi, doi_url, doi_verified, title, authors, year, journal, abstract, keywords, duplicate_of, screen_pass1, screen_pass1_reason, screen_pass2, screen_pass2_reason, full_text_obtained, rob_tool, rob_overall, included_final`.
- Lanza verificación CrossRef en background (en lotes de 50 con backoff) → marca `doi_verified` TRUE/FALSE.

Tras el build, presenta al usuario: "He encontrado N registros únicos. Master corpus en `<path>`. Sigo con dedup."

---

## FASE 5 — Deduplicación

```bash
python ~/.claude/skills/systematic-review/scripts/dedup.py "<project_dir>"
```

- Match exacto por DOI normalizado (lowercase, strip).
- Fallback fuzzy título (RapidFuzz ratio ≥ 90).
- Fallback PMID si existe.
- Actualiza `master_corpus.xlsx` poblando `duplicate_of` con el `id` del primario.
- Escribe `duplicates_log.csv` con todas las parejas.
- Reporta al usuario: "X duplicados detectados, Y registros únicos para cribar".

---

## FASE 6 — Cribado Pass 1 (automático, reglas keyword)

```bash
python ~/.claude/skills/systematic-review/scripts/screen_pass1.py "<project_dir>"
```

Lee `project_config.yaml` que tiene:
```yaml
screening:
  include_keywords: [...]
  exclude_keywords: [...]
  min_include_hits: 2
```

Aplica:
- `INCLUDE` si ≥`min_include_hits` include AND 0 exclude.
- `EXCLUDE` si ≥1 exclude.
- `MAYBE` en el resto.

Llena columnas `screen_pass1` y `screen_pass1_reason` en `master_corpus.xlsx`. Escribe `screening_pass1_log.csv`.

**Si Pass 1 no es razonable** (>1000 INCLUDE o <5), ofrece al usuario ajustar threshold/keywords y re-ejecutar.

---

## FASE 7 — Cribado Pass 2 (asistido por IA, confirmado por el usuario)

Para cada paper con `screen_pass1` en `{INCLUDE, MAYBE}`, la skill:
1. Presenta lotes de **20 papers** al usuario en chat.
2. Para cada paper muestra: título, año, journal, abstract resumido, decisión propuesta basada en PICO + criterios + abstract, razón concreta.
3. El usuario marca cada uno con `i` (include), `e` (exclude + razón), `m` (mantener maybe).
4. La skill registra en `screening_pass2_log.csv` y actualiza `master_corpus.xlsx`.

**Esta es la única fase no automatizada.** El usuario decide cada inclusión final. Esto preserva rigor metodológico.

---

## FASE 8 — Riesgo de sesgo

Propón el tool adecuado al design predominante:

| Design | Tool |
|--------|------|
| RCT | Cochrane RoB 2 |
| No aleatorizado de intervenciones | ROBINS-I |
| Cohortes / caso-control | Newcastle-Ottawa Scale (NOS) |
| RS / meta-análisis | AMSTAR 2 |
| Diagnóstico | QUADAS-2 |
| Cualitativos | CASP / JBI |

Para cada estudio incluido, abre los dominios del tool y guía al usuario por cada uno. Persiste en `rob_assessments.xlsx`. Llena columnas `rob_tool` y `rob_overall` en `master_corpus.xlsx`.

---

## FASE 9 — Meta-análisis (opcional)

Solo si el usuario lo pidió en Fase 1 Y hay ≥3 estudios con outcome común cuantitativo.

```bash
Rscript ~/.claude/skills/systematic-review/scripts/meta_analysis.R "<project_dir>"
```

Genera con `metafor`:
- `meta_analysis/forest_plot.png` — modelo random effects.
- `meta_analysis/funnel_plot.png` — sesgo de publicación.
- `meta_analysis/rob_summary.png` — traffic-light plot.
- `meta_analysis/ma_script.R` — script editable.

Si no hay suficiente homogeneidad, omite MA y avisa: "se hace síntesis narrativa".

---

## FASE 10 — Diagrama PRISMA 2020

```bash
python ~/.claude/skills/systematic-review/scripts/prisma_flow.py "<project_dir>"
```

Lee contadores de `project_state.json` (`identificados_<base>`, `duplicados`, `screened`, `excluded_pass1`, `excluded_pass2`, `full_text_obtained`, `full_text_excluded`, `incluidos_final`). Genera:
- `prisma_flow.png` — diagrama oficial PRISMA 2020 Template B (database + other sources).
- `prisma_flow.json` — contadores para auditoría.

---

## FASE 11 — Borrador PROSPERO

```bash
python ~/.claude/skills/systematic-review/scripts/prospero_form.py "<project_dir>"
```

Genera `manuscript/protocol_prospero.md` con TODOS los campos del formulario PROSPERO 2024 prerellenados desde `project_config.yaml`:

- Title, Anticipated start/end date, Stage of review at submission
- Named contact, organisation, country
- Funding sources, Conflicts of interest, Collaborators
- Review question (PICO formateado)
- Searches: bases, fechas de última búsqueda, search strategy URL
- Condition, participants, intervention, comparator, outcomes (main + additional)
- Types of study, Context
- Data extraction strategy
- Risk of bias assessment
- Strategy for data synthesis
- Subgroup analyses
- Type and method of review, Language, Country
- Dissemination plans, Keywords, Current review status

El usuario copia/pega en https://www.crd.york.ac.uk/PROSPERO/. La skill **NO** sube nada automáticamente.

---

## FASE 12 — Recomendación de revistas

```bash
python ~/.claude/skills/systematic-review/scripts/journal_recommender.py "<project_dir>"
```

- Llama JANE (jane.biosemantics.org) con título + abstract — devuelve top revistas por similitud.
- WebFetch a Scimago JR para Q-quartil e IF actuales de las top 10.
- Filtra por scope (debe encajar con el tema), idioma, OA fees.
- Genera `manuscript/journal_recommendations.md` con top 5 revistas: nombre, Q, IF, scope, tiempo medio de revisión, APC, link al author guidelines.

Recomienda explícitamente seguir **PRISMA 2020 Statement** + adjuntar **PRISMA-trAIce checklist** si se usó IA en el cribado.

---

## FASE 13 — Manuscrito Word con Zotero

### 13.1 Sincronizar a Zotero

Para cada paper `included_final=TRUE`:
- `mcp__zotero__zotero_create_collection` con nombre `"SR — <slug-tema>"`.
- `mcp__zotero__zotero_add_by_doi` para cada DOI.

### 13.2 Generar manuscrito con marcadores RTF/ODF Scan

```bash
python ~/.claude/skills/systematic-review/scripts/compile_docx.py "<project_dir>"
```

El script genera `manuscript/manuscript.docx` siguiendo estructura PRISMA 2020 (ver `references/manuscript-template.md`):
- Title page, Abstract estructurado (PRISMA Abstracts), Introduction (Rationale + Objectives), Methods (12 subsecciones cubriendo items 5–15), Results (items 16–22 incluyendo PRISMA flow embebido), Discussion (items 23a–d), Conclusions, Declarations, References (vacío de momento), Appendices.
- Todas las citas se insertan como **marcadores RTF/ODF Scan**: `{|Apellido Año|}`.
- Antes de escribir prosa larga (Discussion, Conclusions), invoca la skill `humanizer`.

### 13.3 Instrucciones de finalización para el usuario

La skill muestra al usuario:

> Manuscrito generado en `<path>`. Para convertir los marcadores en citas vivas de Zotero:
>
> 1. Abre el .docx en Word (con plugin de Zotero instalado).
> 2. En Zotero, menú **Edit → RTF/ODF Scan** (o "Preferences → Cite → RTF/ODF Scan" en versiones recientes).
> 3. Seleccionar archivo input (manuscript.docx) y carpeta output.
> 4. Zotero mapea cada `{|Author Year|}` a la entrada en la colección "SR — <slug-tema>" y los reemplaza por citas vivas + bibliografía al final.
> 5. A partir de ahí editas refs desde Zotero como en cualquier paper.

---

## FASE 14 — Checklist PRISMA-trAIce

Solo si la skill ha ejecutado cribado asistido por IA (Pass 1 automático cuenta).

Lee `references/prisma-traice-checklist.md` y genera `manuscript/prisma_traice_checklist.md` con los 17 items prerellenados:
- T1, A1, I1: posiciones del manuscrito que mencionan IA.
- M1–M10: tool name (Claude), version, developer (Anthropic), task (cribado por reglas + revisión asistida abstract), prompt completo (referenciar `project_config.yaml` y este SKILL.md), human oversight (cribado Pass 2 dual: IA propone, autor decide).
- R1: PRISMA flow distingue records IA-handled vs human-handled.
- R2, D1, D2: para que el usuario rellene tras correr el pipeline.

El usuario adjunta este checklist al manuscrito.

---

## Recuperación y reanudación

Cada fase actualiza `project_state.json` con su estado:
```json
{
  "current_phase": 7,
  "completed_phases": [0, 1, 2, 3, 4, 5, 6],
  "search_cursors": {"pubmed": "complete", "semantic_scholar": "complete", "openalex": "cursor_abc123"},
  "counts": {"identificados": 1240, "duplicados": 187, "screened": 1053, "pass1_include": 89}
}
```

Si el usuario invoca la skill con un proyecto ya iniciado:
1. Detecta `project_state.json` existente.
2. Pregunta: *"Encontré el proyecto '<slug>' en fase <N>. ¿Continúo desde ahí o reinicio?"*
3. Si continúa, reanuda desde la fase activa.

---

## Manejo de errores conocidos

| Error | Recuperación |
|-------|--------------|
| PubMed 429 | backoff exponencial 1s → 2s → 4s → 8s, máx 5 intentos |
| S2 0 hits con query válido | reintenta tras 60s (rate limit silencioso) |
| OpenAlex cursor inválido | reinicia desde el último cursor en `project_state.json` |
| Playwright WoS UI cambiada | fallback a manual con instrucciones paso a paso |
| Pandoc no instalado | propone `brew install pandoc` y ofrece ejecutarlo |
| Zotero no abierto | avisa: "abre Zotero y dime cuando esté listo" |
| CrossRef DOI no resuelve | marca `doi_verified=FALSE`, NO bloquea |
| Excel corrupto | regenera desde `raw_*.json` |

---

## Anti-patrones

- Saltarse el preflight de Fase 0.
- Aplicar filtros temporales/idioma sin permiso del usuario.
- Inventar PMID/DOI/journal name.
- Cribar Pass 2 automáticamente sin confirmación humana.
- Generar manuscrito sin pasar la prosa larga por `humanizer`.
- Subir nada a PROSPERO automáticamente (solo entregar borrador).
- Inventar revistas en Fase 12.
- Asumir que Embase tiene API (no la tiene libre).
- Mezclar idioma de conversación (siempre español) con idioma de entregable.

---

## Cierre de la skill

```
---
**Pipeline completado.**
- Registros identificados: N
- Tras dedup: M
- Tras Pass 1: P
- Tras Pass 2: Q
- Tras full-text: R
- **Incluidos finales: S**

**Entregables en `~/Desktop/terminal/Publicaciones/<slug>/`:**
- master_corpus.xlsx
- prisma_flow.png
- manuscript/protocol_prospero.md  ← pegar en PROSPERO
- manuscript/journal_recommendations.md
- manuscript/manuscript.docx  ← abrir en Word y correr Zotero RTF/ODF Scan
- manuscript/prisma_traice_checklist.md (si aplica)
- meta_analysis/ (si aplica)

**Próximos pasos:**
1. Subir el borrador PROSPERO a https://www.crd.york.ac.uk/PROSPERO/
2. Convertir marcadores Zotero en el .docx (Edit → RTF/ODF Scan)
3. Revisar journal_recommendations.md y elegir target
```
