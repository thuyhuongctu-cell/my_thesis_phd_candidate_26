# CLAUDE.md — Bitácora del repo systematic-review-skill

> Notas internas de desarrollo. NO se publican como guía de usuario (eso vive en README.md).

## Estado actual (2026-05-16)

- **v1.0** publicada en https://github.com/Drignacioalcala/systematic-review-skill
- **MIT license** con disclaimer clínico ES/EN.
- Symlink activo: `~/.claude/skills/systematic-review` → este repo. Una sola fuente de verdad: editar aquí, commitear, push. La skill instalada se actualiza sola.

## Setup de desarrollo

```
~/Desktop/terminal/systematic-review-skill/   ← repo git (este)
~/.claude/skills/systematic-review            ← symlink al repo
```

Si futuro Claude o el usuario quieren modificar la skill:
1. Editar archivos aquí.
2. `git add -A && git commit -m "..."` desde este directorio.
3. `git push` para publicar.
4. La skill instalada (vía symlink) ya está actualizada — no requiere copia manual.

## Decisiones de arquitectura

- **Cribado Pass 2 no automatizado**: línea metodológica innegociable. La IA propone, el usuario firma.
- **WoS/Embase vía Playwright MCP con login manual**: respeta TOS y SSO/2FA. Patrón documentado en `pattern_apis_cerradas_playwright` de memoria global.
- **Excel con DOIs hipervínculo**: openpyxl con `cell.hyperlink`, no strings concatenados.
- **PROSPERO solo borrador**: nada se sube automáticamente (no hay API pública además).
- **Manuscrito con marcadores Zotero RTF/ODF Scan**: mejor que generar field codes binarios desde fuera.
- **PRISMA-trAIce auto**: si se usó cribado IA, el checklist se genera al final.

## Inventario

- **SKILL.md** — orquestador 14 fases.
- **scripts/** (16 archivos):
  - `preflight.py` — verifica Python ≥ 3.10, pip packages, pandoc (opcional), R+metafor (opcional), Playwright, MCPs esperados.
  - `init_project.py` — crea estructura en `~/Desktop/terminal/Publicaciones/<slug>/`.
  - `search_pubmed.py` — E-utilities, paginación retmax=200, backoff exponencial.
  - `search_semantic_scholar.py` — bulk endpoint + cursor + retry-after.
  - `search_openalex.py` — cursor, polite pool.
  - `wos_embase_helper.py` — valida RIS descargado post-Playwright.
  - `parse_ris.py` — rispy → schema común.
  - `dedup.py` — DOI exacto + fuzzy título RapidFuzz ≥90.
  - `verify_doi.py` — CrossRef GET /works/{doi}.
  - `build_master_xlsx.py` — openpyxl con DOIs hipervínculo, también genera `master_corpus.json` para downstream.
  - `screen_pass1.py` — keyword rules.
  - `prisma_flow.py` — matplotlib → PRISMA 2020 Template B.
  - `prospero_form.py` — borrador 37 campos PROSPERO 2024.
  - `journal_recommender.py` — JANE + Scimago.
  - `compile_docx.py` — python-docx con marcadores `{|Author Year|}`.
  - `meta_analysis.R` — metafor (SMD/OR/RR) + forest + funnel.
- **references/** (5 archivos):
  - `prisma-2020-checklist.md` — 27 items Page 2021 (CC BY 4.0).
  - `prisma-traice-checklist.md` — 17 items Holst 2025.
  - `prospero-template.md`, `manuscript-template.md`, `tool-tips.md`.
- **docs/**
  - `COMO_FUNCIONA.md` — explicación narrativa no-técnica.

## Próximos pasos prioritarios

1. ~~**Test end-to-end real**~~ ✅ HECHO 2026-05-26 (fases 0→7 contra protocolo PROSPERO real; ver bitácora). Pendiente probar fases 8→14 (RoB, MA, manuscrito, trAIce) con datos reales tras cribado humano.
2. **Selectores Playwright**: ✅ Embase (embase.com Advanced) y Cochrane CENTRAL probados y funcionando vía proxy institucional. **WoS (Clarivate) sigue sin probar** contra UI real.
3. **Forest plot real con metafor**: `meta_analysis.R` necesita un `meta_input.csv` que se rellena a mano. Mejorar: que `build_master_xlsx.py` deje una hoja `meta_input` vacía con columnas correctas para acelerar.
4. **Test con MCP Consensus presente**: comprobar detección automática y degradación si no está.

## Errores conocidos / limitaciones

- `journal_recommender.py` actualmente solo hace una llamada cosmética a JANE — la parseación real del HTML está pendiente. Por ahora entrega un MD con guía manual al usuario. Mejora posible: parser BeautifulSoup del HTML de JANE.
- `compile_docx.py` no inserta el `prisma_flow.png` automáticamente en el .docx — solo deja un placeholder textual. Mejora: `doc.add_picture(path)` cuando exista.
- Playwright selectors: Embase + Cochrane CENTRAL testados en vivo (OK); WoS aún no.

## Bitácora

- **2026-05-16 mañana** — Auditoría de 6 repos existentes (slr-prisma, davila7, prisma-review-tool, academic-research-skills, co-researcher, agent-research-skills). Confirmado que ninguno hace RS "one-prompt" porque no es metodológicamente posible sin sacrificar rigor.
- **2026-05-16 tarde** — Construcción de v1.0: SKILL.md (14 fases) + 16 scripts + 5 references. Preflight verde. Symlink establecido.
- **2026-05-16 tarde** — Publicación GitHub público bajo MIT. README extenso paso a paso para hospitales. Documento narrativo `COMO_FUNCIONA.md` para no-técnicos.
- **2026-05-26** — **Primer test end-to-end real** contra un protocolo PROSPERO ya registrado (RS de educación quirúrgica, 3 bases: PubMed + Embase + Cochrane CENTRAL). Pipeline ejecutado fases 0→7: preflight, init, estrategia, búsquedas, master corpus, dedup, pre-cribado. Resultado: 258 identificados → 177 únicos. **3 bugs encontrados y corregidos:**
  - `search_pubmed.py`: el año salía vacío. Causa: `art.find(".//PubDate/Year") or art.find(...)` — un Element `<Year>` sin hijos se evalúa como falsy (DeprecationWarning de ElementTree), así que el `or` saltaba al MedlineDate. Fix: comprobar `is None` explícito.
  - `parse_ris.py`: no recogía el abstract. Causa: rispy mapea la etiqueta RIS `N2` a `notes_abstract`, no a `abstract`. Fix: fallback `e.get("abstract") or e.get("notes_abstract")`. Añadido también `cochrane` como `--source`.
  - `build_master_xlsx.py`: `cochrane` no estaba en `SOURCES`, así que los RIS de Cochrane se ignoraban. Añadido.
  - Validado: Embase y Cochrane vía Playwright sobre navegador real con proxy institucional (login del usuario) funcionan. Selectores de Embase Advanced (`/search/advanced`) y export RIS (modal `#modalConfirmControl` → página `/search/download` → enlace records.ris) confirmados. Cochrane Advanced Search → filtro Trials → Export RIS (EndNote/Reference Manager) confirmado.

## Workflow de release

Cuando haya cambios listos para liberar:

```bash
cd ~/Desktop/terminal/systematic-review-skill
# editar archivos
git add -A
git commit -m "feat/fix/docs: descripción"
git push

# tag opcional para versiones
git tag v1.0.1 -m "1.0.1 — descripción"
git push --tags

# release con notas
gh release create v1.0.1 --notes "Notas de release"
```
