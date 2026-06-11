# Systematic Review — Skill para Claude Code

> Pipeline asistido por IA para hacer **revisiones sistemáticas formales PRISMA 2020 + PROSPERO** con la máxima automatización metodológicamente honesta posible.
>
> Pensado para **clínicos e investigadores en cualquier hospital**. No necesitas saber programar.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![PRISMA 2020](https://img.shields.io/badge/PRISMA-2020-blue)
![PROSPERO compatible](https://img.shields.io/badge/PROSPERO-compatible-green)

---

## ¿Qué hace esta skill?

Convierte tu petición *"quiero hacer una revisión sistemática sobre X"* en un pipeline guiado de 14 fases:

| Fase | Qué hace |
|------|----------|
| 0 | **Preflight** — verifica que tu Mac tiene todo lo necesario y te ayuda a instalar lo que falte |
| 1 | **Briefing** — una sola pantalla de preguntas (tema, PICO, idioma, acceso institucional…) |
| 2 | **Estrategia de búsqueda** — genera las cadenas Booleanas para cada base, tú las editas |
| 3 | **Búsquedas multi-base** — PubMed + Semantic Scholar + OpenAlex automáticas; WoS + Embase semiautomatizadas con tu login institucional |
| 4 | **Master Excel** — consolida todo en un `.xlsx` con DOIs clickables |
| 5 | **Deduplicación** — por DOI exacto y título fuzzy |
| 6 | **Cribado Pass 1** — automático por reglas keyword |
| 7 | **Cribado Pass 2** — la IA propone, tú firmas (esto NO se automatiza por rigor metodológico) |
| 8 | **Risk of Bias** — tool adecuado al design (RoB 2, ROBINS-I, NOS, AMSTAR 2…) |
| 9 | **Meta-análisis opcional** — R + metafor (forest, funnel, RoB summary) |
| 10 | **Diagrama PRISMA 2020** — generado con contadores reales |
| 11 | **Borrador PROSPERO** — los 37 campos del formulario prerellenos |
| 12 | **Recomendación de revistas** — JANE + Scimago |
| 13 | **Manuscrito Word con Zotero** — marcadores RTF/ODF Scan vinculados a tu colección Zotero |
| 14 | **Checklist PRISMA-trAIce** — reporte de uso de IA, 17 items |

**Resultado realista**: una RS que normalmente lleva 6 meses queda **lista en 3-4 semanas de trabajo concentrado**, manteniendo el rigor para publicación en revista indexada.

> Versión narrativa de cómo funciona en cristiano para no-técnicos: ver [docs/COMO_FUNCIONA.md](docs/COMO_FUNCIONA.md).

---

## ¿Qué NO hace?

- **No decide qué estudios incluir.** En el cribado fino (Fase 7), la IA te propone una decisión razonada, pero tú firmas cada una. Es la línea metodológica.
- **No sube nada a PROSPERO automáticamente.** Te entrega un borrador para que tú lo pegues en el formulario web.
- **No escribe tu Discusión sola.** Te deja la estructura, tú aportas la interpretación clínica.
- **No reemplaza al segundo revisor.** Para publicar en revistas serias necesitas dos humanos revisando independientemente.

---

## Requisitos

Antes de instalar, necesitas:

1. **Mac con macOS** (la skill está optimizada para macOS; en Linux/Windows funciona con ajustes).
2. **[Claude Code](https://docs.claude.com/en/docs/claude-code/overview)** — la CLI oficial de Anthropic. Es gratis instalar, pero usa la API de Claude (de pago por uso, ~5-15 € por una RS completa).
3. **Python 3.10 o superior** (probablemente ya lo tienes; el preflight lo comprueba).
4. **Cuenta en GitHub** (para clonar este repo; gratis).
5. **Acceso institucional a WoS y Embase** si los quieres incluir (vía FECYT en España, OpenAthens/Shibboleth en otros sitios). La skill funciona sin ellos si solo usas las bases gratuitas.

**Opcional pero recomendado**:
- **Zotero** instalado (gratis, https://www.zotero.org/) con plugin de Word.
- **R + metafor** si vas a hacer meta-análisis cuantitativo.

---

## Instalación paso a paso (para no-técnicos)

### Paso 1 — Abre el Terminal

En tu Mac, pulsa `Cmd + Espacio`, escribe **Terminal** y dale Enter. Verás una ventana negra con texto. No te asustes: solo vas a pegar comandos.

### Paso 2 — Comprueba que tienes Claude Code instalado

Pega esto y dale Enter:

```bash
which claude
```

- Si te devuelve una ruta (algo como `/usr/local/bin/claude`), está instalado. ✅
- Si dice "not found", instálalo siguiendo la guía oficial: https://docs.claude.com/en/docs/claude-code/setup

### Paso 3 — Descarga la skill desde GitHub

Pega esto en el Terminal (todo en una línea):

```bash
git clone https://github.com/Drignacioalcala/systematic-review-skill.git ~/.claude/skills/systematic-review
```

Esto descarga la skill en la carpeta donde Claude Code busca skills.

> **Si te dice "git: command not found"**: instala git con `xcode-select --install` (aparecerá un popup, dale OK, espera 5 min).

### Paso 4 — Instala las herramientas que necesita

Pega esto en el Terminal:

```bash
python3 ~/.claude/skills/systematic-review/scripts/preflight.py
```

Esto comprueba qué falta en tu Mac. Si todo está OK, verás un JSON con `"ok": true`. Si falta algo, te dará el comando para instalarlo. Normalmente basta con:

```bash
pip3 install requests openpyxl rispy rapidfuzz python-docx lxml pyyaml playwright matplotlib
```

> **Si dice "permission denied"**: añade `--user` al final: `pip3 install --user ...`

### Paso 5 — Instala el navegador para WoS/Embase (opcional)

Si vas a usar Web of Science o Embase, necesitas que Claude pueda abrir un navegador controlado:

```bash
python3 -m playwright install chromium
```

(Tarda unos 2-3 minutos, descarga un navegador en miniatura, ~150 MB).

### Paso 6 — Conecta los MCPs (servicios externos) en Claude Code

Los MCPs son "enchufes" que conectan Claude con servicios como PubMed o Zotero. Estos son los necesarios:

| MCP | Para qué | Obligatorio | Cómo se instala |
|-----|----------|-------------|-----------------|
| **PubMed** | Búsquedas en PubMed | Sí | Desde la app claude.ai → Connectors → "PubMed" |
| **Zotero** | Sincronizar referencias | Recomendado | https://github.com/54yyyu/zotero-mcp |
| **Playwright** | Controlar navegador para WoS/Embase | Recomendado | `claude mcp add playwright npx '@playwright/mcp@latest'` |
| **Consensus** | Búsqueda semántica adicional | Opcional | Desde claude.ai → Connectors → "Consensus" |
| **NotebookLM** | Audio overview de la RS | Opcional | https://github.com/yairfried/notebooklm-mcp |

Después de añadir un MCP, reinicia Claude Code (`exit` en el terminal y vuelve a entrar) para que lo detecte.

### Paso 7 — Arranca

Abre Claude Code en tu Mac:

```bash
claude
```

Y escribe algo como:

```
quiero hacer una revisión sistemática sobre [tu tema]
```

La skill se activa sola, te pide el briefing en una pantalla, y arranca el pipeline.

---

## Tu primera revisión sistemática — paso a paso

### En el chat con Claude

1. **Tú dices**: *"Quiero hacer una RS sobre dupilumab en poliposis nasal."*
2. **Claude responde**: detecta que esto es una revisión sistemática, activa la skill, y empieza por la **Fase 0**: comprueba que tu Mac tiene todo. Si falta algo, te lo dice y te ofrece instalarlo con `[Y/n]`.
3. **Fase 1 — Briefing**: te muestra una pantalla con preguntas. Contestas en bloque (tema, PICO, idioma, acceso institucional). Si dices *"lo demás como tú veas"*, aplica defaults razonables.
4. **Fase 2 — Estrategia**: te enseña las cadenas Booleanas para PubMed, S2, OpenAlex, WoS, Embase. Las editas si quieres. Confirmas.
5. **Fase 3 — Búsquedas**:
   - PubMed, S2, OpenAlex: se ejecutan automáticas. Te informa de los conteos.
   - WoS/Embase: **se abre una ventana de Chrome controlada**. Tú haces login con tus credenciales (FECYT, hospital, OpenAthens), dices *"listo"* en el chat, y Claude mueve el ratón para hacer la búsqueda y exportar el RIS.
6. **Fase 4 — Excel maestro**: abre `~/Desktop/terminal/Publicaciones/<tema>/master_corpus.xlsx`. Verás todos los artículos consolidados con DOIs clickables.
7. **Fase 5-6 — Dedup + Pass 1**: automático. Te dice cuántos eliminó y cuántos quedan.
8. **Fase 7 — Pass 2**: **aquí es donde TÚ trabajas**. Claude te presenta lotes de 20 abstracts y para cada uno te propone "incluir/excluir + razón". Tú marcas `i`, `e`, o `m`. Esto puede llevarte varias horas o días según el volumen.
9. **Fase 8-9 — RoB y MA**: Claude te guía dominio a dominio.
10. **Fase 10-14 — Cierre**: PRISMA flow, PROSPERO borrador, recomendación de revistas, manuscrito Word, checklist PRISMA-trAIce.

### Al final tienes

```
~/Desktop/terminal/Publicaciones/<tu-tema>/
├── master_corpus.xlsx                  ← tu base de datos
├── prisma_flow.png                     ← diagrama PRISMA
├── manuscript/
│   ├── protocol_prospero.md            ← pegar en PROSPERO
│   ├── journal_recommendations.md      ← revistas a considerar
│   ├── manuscript.docx                 ← manuscrito Word
│   └── prisma_traice_checklist.md      ← declaración de uso IA
├── meta_analysis/                      ← gráficos si pediste MA
├── searches/                           ← queries y resultados crudos
├── duplicates_log.csv
├── screening_pass1_log.csv
└── screening_pass2_log.csv
```

---

## Acceso a Web of Science y Embase

Si tu hospital tiene licencia institucional pero no API (lo habitual):

### Web of Science
- En España, vía **FECYT**: https://www.recursoscientificos.fecyt.es/
- Login con credenciales de tu institución (HUFJD, Sant Pau, La Paz, etc.).
- La skill abre WoS, tú haces login una sola vez, y luego automatiza la búsqueda y exportación RIS.

### Embase
- Acceso vía Elsevier institucional (OpenAthens, IP institucional, Shibboleth).
- URL típica: https://www.embase.com/landing
- Mismo flujo: tú logueas, Claude automatiza.

### Si tu hospital NO tiene WoS/Embase
La skill funciona perfectamente con solo PubMed + Semantic Scholar + OpenAlex (todo gratis). Cubre el 80-90% de la literatura biomédica. Marca `wos: false` y `embase: false` en el briefing.

---

## Estructura del repositorio

```
systematic-review-skill/
├── SKILL.md                          # Skill principal (orquestador 14 fases)
├── scripts/                          # Helpers Python + R
│   ├── preflight.py                  # Verifica herramientas
│   ├── init_project.py               # Crea estructura del proyecto
│   ├── search_pubmed.py              # E-utilities + paginación
│   ├── search_semantic_scholar.py    # Graph API
│   ├── search_openalex.py            # OpenAlex API
│   ├── wos_embase_helper.py          # Validador RIS post-Playwright
│   ├── parse_ris.py                  # Parser RIS común
│   ├── dedup.py                      # DOI + fuzzy título
│   ├── verify_doi.py                 # CrossRef
│   ├── build_master_xlsx.py          # Excel con DOIs hipervínculo
│   ├── screen_pass1.py               # Reglas keyword
│   ├── prisma_flow.py                # Diagrama PRISMA 2020
│   ├── prospero_form.py              # Borrador PROSPERO
│   ├── journal_recommender.py        # JANE + Scimago
│   ├── compile_docx.py               # Manuscrito Word + marcadores Zotero
│   └── meta_analysis.R               # Forest/funnel con metafor
├── references/                       # Plantillas y checklists
│   ├── prisma-2020-checklist.md      # 27 items (Page 2021)
│   ├── prisma-traice-checklist.md    # 17 items (Holst 2025)
│   ├── prospero-template.md          # 37 campos PROSPERO 2024
│   ├── manuscript-template.md        # Estructura PRISMA journal
│   └── tool-tips.md                  # Sintaxis por base de datos
├── docs/
│   └── COMO_FUNCIONA.md              # Explicación narrativa no-técnica
├── LICENSE                           # MIT
└── README.md                         # Este archivo
```

---

## Resolución de problemas frecuentes

### "ModuleNotFoundError: No module named X"
Falta una librería Python. Re-corre el preflight:
```bash
python3 ~/.claude/skills/systematic-review/scripts/preflight.py
```
Y ejecuta el `pip install` que te recomiende.

### "Playwright dice: browser not found"
Ejecuta:
```bash
python3 -m playwright install chromium
```

### "El login de WoS expira a mitad de la búsqueda"
Es normal. Vuelve a hacer login en la ventana de Chrome y di *"listo"* a Claude. El pipeline se reanuda desde donde estaba.

### "Conflicto NumPy / matplotlib"
Si tienes anaconda instalado y matplotlib se queja:
```bash
pip3 install --upgrade matplotlib
```

### "PubMed devuelve 0 resultados"
Lo más probable: la query tiene un MeSH inexistente o una errata. Pídele a Claude que la revise: *"reescribe la query de PubMed simplificando los MeSH"*.

### "El cribado Pass 2 es demasiado lento"
Es lo normal cuando tienes >300 abstracts. Estrategias:
- Sube el `min_include_hits` en `project_config.yaml` para que el Pass 1 descarte más.
- Añade exclude_keywords más específicas.
- Divide la RS en sub-preguntas.

### "Zotero RTF/ODF Scan no encuentra los marcadores"
Asegúrate de que:
1. Has corrido la sincronización a Zotero (Fase 13.1) antes de generar el manuscrito.
2. La colección Zotero se llama exactamente `"SR — <slug>"`.
3. Estás usando Zotero 6 o superior.

---

## Filosofía y rigor metodológico

Esta skill se diseñó después de auditar 6 proyectos similares (slr-prisma, davila7 literature-review, prisma-review-tool, academic-research-skills, co-researcher, agent-research-skills) y leer literatura sobre el uso de IA en revisiones sistemáticas.

### Lo que automatizamos
- Búsquedas (incluido el manejo de rate limits y paginación).
- Deduplicación.
- Verificación de DOIs.
- Cribado grueso por reglas keyword.
- Generación de diagramas, formularios y manuscritos.

### Lo que NO automatizamos (por rigor)
- Cribado fino de title/abstract: la IA propone, tú firmas.
- Lectura de full-text e inclusión final.
- Evaluación de RoB (tú decides cada dominio).
- Interpretación clínica en Discusión.

### Reporte transparente de uso de IA
La skill genera automáticamente el **checklist PRISMA-trAIce** (Holst et al. 2025, JMIR AI, [10.2196/80247](https://doi.org/10.2196/80247)) para que adjuntes con tu manuscrito. Cada vez más revistas (BMJ AI, Lancet Digital Health, JMIR AI) lo exigen.

---

## Inspirado en y agradecimientos

Esta skill **integra ideas** de varios proyectos open-source previos:

- **[slr-prisma](https://github.com/keemanxp/slr-prisma)** (Chuah Kee Man) — estructura PRISMA 2020 y entrevista inicial.
- **[davila7/claude-code-templates literature-review](https://github.com/davila7/claude-code-templates)** — scripts de búsqueda multi-base y verificación CrossRef.
- **[Black-Lights/prisma-review-tool](https://github.com/Black-Lights/prisma-review-tool)** — two-pass screening y rate-limit honesto.
- **[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)** — checklist PRISMA-trAIce.
- **[poemswe/co-researcher](https://github.com/poemswe/co-researcher)** — PICOTS y RoB framework.

Gracias a esos autores por compartir su trabajo. Esta skill aporta:
- Integración 14 fases end-to-end sin saltos.
- WoS/Embase semiautomatizado vía Playwright (no requiere API de pago).
- Hoja Excel maestra con DOIs clickables y verificación CrossRef.
- Sincronización Zotero con marcadores RTF/ODF Scan.
- Preflight check con auto-instalación.
- Pensado en español para hospitales hispanohablantes.

---

## Licencia

MIT — usa, modifica y redistribuye libremente. Ver [LICENSE](LICENSE).

Si la usas en una publicación, una cita o mención sería apreciada:

```
Alcalá-Rueda I. Systematic Review Skill for Claude Code. 2026.
https://github.com/Drignacioalcala/systematic-review-skill
```

---

## Contribuir

Issues y pull requests bienvenidos en https://github.com/Drignacioalcala/systematic-review-skill/issues

Ideas concretas para futuras versiones:
- Soporte para PubMed Central full-text fetching.
- Integración con Rayyan/Covidence import-export.
- Selectores Playwright probados contra UI actual de WoS/Embase.
- Modo "scoping review" siguiendo PRISMA-ScR.
- Plantilla específica para Cochrane Reviews.

---

## Autor

**Dr. Ignacio Alcalá-Rueda** — Médico ORL, Hospital Universitario Fundación Jiménez Díaz (Madrid).
Cofundador de [red sanitarIA](https://redsanitaria.es).

Construido con [Claude Code](https://claude.com/claude-code) (Anthropic).
