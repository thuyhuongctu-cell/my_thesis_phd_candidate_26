# Cómo funciona la skill, contado en cristiano

> Para clínicos e investigadores sin background técnico. Si quieres detalles de implementación, mira [SKILL.md](../SKILL.md).

Imagina que tienes que hacer una revisión sistemática (RS) de un tema médico. Normalmente eso te lleva entre **6 meses y 2 años** de trabajo manual: buscar en cada base por separado, copiar resultados a Excel, leer miles de abstracts, eliminar duplicados, rellenar el formulario PROSPERO a mano, etc. Esta skill no quita el trabajo intelectual, pero **automatiza todo lo mecánico** y te lleva de la mano paso a paso.

Funciona así: tú abres una conversación con Claude, dices algo como *"quiero hacer una revisión sistemática sobre dupilumab en poliposis nasal"* y la skill se activa sola. A partir de ahí pasan estas cosas, una detrás de otra:

---

## Paso 1 — La skill comprueba que tu ordenador tiene lo necesario

Antes de hacer nada, abre la "caja de herramientas" y revisa que estén todas las piezas: que el Python esté actualizado, que tenga librerías para leer Excel, para hacer búsquedas, para mover navegadores... Si falta algo, **te lo dice y te ofrece instalarlo con un solo botón**. No tienes que saber qué es cada cosa, solo decir "sí, instálalo".

*Analogía clínica*: es como cuando enchufas un ecógrafo nuevo y comprueba que tiene gel, la sonda conectada y el cable de corriente antes de dejarte usarlo.

---

## Paso 2 — Te hace UNA tanda de preguntas (no te bombardea)

Una sola vez, en una sola pantalla, te pregunta lo esencial: tema, pregunta clínica (PICO), si tienes acceso a Web of Science y Embase desde tu hospital, en qué idioma quieres el manuscrito, si quieres hacer meta-análisis. Si dices *"lo demás como tú veas"*, ella aplica valores razonables y arranca.

---

## Paso 3 — Te propone la estrategia de búsqueda y tú la corriges

La skill **construye las cadenas de búsqueda Booleanas** para cada base (PubMed con MeSH, WoS con su sintaxis, Embase con Emtree...) y te las enseña en una tabla. Tú las lees, le dices *"cambia esto, quita aquello"*, y ella las regenera. Nada se busca sin tu visto bueno — esto es importante porque las búsquedas mal hechas arruinan una RS entera.

---

## Paso 4 — Hace las búsquedas en todas las bases

Aquí pasa lo interesante:

**En PubMed, Semantic Scholar y OpenAlex** (que son gratis y abiertas) — la skill lanza las búsquedas sola. Si una devuelve 5.000 resultados, los va descargando en lotes de 200 y guardando en disco a medida que avanza. Si en algún momento la web se cae o pone "espera un minuto", la skill espera, reintenta, y si tienes que cerrar el ordenador, **recuerda dónde se quedó y sigue cuando vuelvas**.

**En Web of Science y Embase** (que requieren tu login institucional FECYT/hospital) — aquí está el truco más bonito: la skill **abre un navegador en una pestaña separada**, te dice *"haz tú el login con tus credenciales"*, esperas a entrar, le dices "listo", y a partir de ahí ella mueve el ratón, pega la búsqueda, clica "Exportar como RIS", descarga el archivo, repite si hay más de 1000 resultados. **Tu seguridad no se compromete** — la skill nunca ve tu contraseña.

---

## Paso 5 — Crea tu hoja maestra Excel

Junta TODOS los resultados de TODAS las bases en un único Excel llamado `master_corpus.xlsx`. Cada fila es un artículo, con columnas para: título, autores, año, revista, DOI, abstract, palabras clave...

**Lo importante**: cada DOI es un enlace clickable. Si abres el Excel y le das al DOI, te lleva directamente al artículo en la web. Y además la skill comprueba con CrossRef (la base de datos oficial de DOIs) que cada DOI es real — los que no, los marca con una bandera roja para que sepas que el dato venía mal de origen.

---

## Paso 6 — Quita los duplicados

Si un mismo artículo apareció en PubMed y en Embase, la skill lo detecta y lo marca como duplicado (no lo borra — lo deja para auditoría, pero ya no cuenta). Lo hace primero por DOI exacto, y si no hay DOI, comparando títulos con un algoritmo que tolera pequeñas diferencias de puntuación o mayúsculas.

---

## Paso 7 — Primer cribado automático

Tú le has dicho qué palabras clave indican "INCLUIR" (e.g. "dupilumab", "biological therapy") y cuáles indican "EXCLUIR" (e.g. "in vitro", "animal model"). La skill aplica esas reglas a todos los abstracts y deja cada artículo etiquetado como INCLUIR, EXCLUIR o DUDOSO.

Esto **no decide nada definitivo** — es un primer filtro grueso. Si te deja 800 artículos en INCLUIR, te dice *"esto es mucho, ajustamos los criterios"*. Si te deja 3, también te avisa.

---

## Paso 8 — Segundo cribado con confirmación humana

Aquí está la **línea roja metodológica**: para que tu RS sea publicable, **tú tienes que firmar cada inclusión final**. La IA no decide sola.

La skill te presenta los abstracts de 20 en 20. Para cada uno te dice *"propuesta: incluir, porque cumple población X, intervención Y, outcome Z"*. Tú lees y dices `i` (incluir), `e` (excluir + razón), o `m` (mantener dudoso). Esto es el único punto del proceso donde tu cerebro **tiene que estar al 100%** — pero al menos vas guiado y todo se registra.

---

## Paso 9 — Evaluación de calidad (Risk of Bias)

Para cada estudio que has incluido, la skill te dice *"este es un ensayo clínico → usamos la herramienta Cochrane RoB 2; estos son los 5 dominios; valoremos uno por uno"*. Tú contestas, ella va rellenando una hoja Excel paralela, y al final tienes la evaluación de sesgo lista.

---

## Paso 10 — Meta-análisis (opcional, si tu tema lo permite)

Si pediste meta-análisis, la skill abre R por debajo, calcula el efecto combinado (modelo de efectos aleatorios), y te genera el **forest plot** (gráfico clásico con la línea vertical y los rombos), el **funnel plot** (para detectar sesgo de publicación) y un resumen de heterogeneidad (I²).

Si los estudios son demasiado distintos para combinarlos, la skill **no insiste** — te dice *"no procede meta-análisis, hacemos síntesis narrativa"*.

---

## Paso 11 — Diagrama PRISMA 2020

Ese cuadro con cajas conectadas por flechas que sale en toda revisión sistemática moderna. La skill lo dibuja sola con los números reales: cuántos encontró en cada base, cuántos duplicados quitó, cuántos cribó, cuántos excluyó en cada fase, cuántos quedan al final. Te lo deja como imagen `.png` lista para meter en el manuscrito.

---

## Paso 12 — Borrador del formulario PROSPERO

PROSPERO es el registro oficial de protocolos de RS — sin él, tu revisión pierde mucho valor. Tiene **37 campos** que normalmente tienes que rellenar a mano y te lleva horas. La skill genera un documento Markdown con los 37 campos **ya prerrellenados** desde la información que recogió al principio. Tú lo abres, ajustas detalles, y **copias-y-pegas** cada bloque en el formulario web de PROSPERO. La skill no sube nada por ti — eso lo haces tú, porque tu nombre va a quedar registrado y tienes que firmar.

---

## Paso 13 — Recomendación de revistas

Coge tu título y abstract, los pasa por JANE (Journal Author Name Estimator, una web que sugiere revistas según el contenido) y por Scimago (que da impacto, cuartil, scope). Te entrega un listado con las 5 revistas que mejor encajan, con su factor de impacto, tiempo de revisión típico y si cobran APC. Tú eliges.

---

## Paso 14 — Manuscrito Word con citas Zotero

La skill te entrega un `.docx` con la estructura PRISMA 2020 completa: Title, Abstract, Introducción, Métodos (con los 12 subapartados), Resultados, Discusión, Conclusiones, Declaraciones, etc. Las citas aparecen como marcadores tipo `{|Smith 2023|}`.

**El truco con Zotero**: tú abres ese Word, vas a Zotero, eliges la opción "RTF/ODF Scan", y Zotero **convierte automáticamente cada marcador en una cita viva** vinculada a tu biblioteca. A partir de ahí editas las referencias desde Zotero como en cualquier paper — cambias estilo APA por Vancouver con dos clics, añades una cita nueva, etc.

---

## Paso 15 — Checklist PRISMA-trAIce

Como has usado IA para parte del proceso, las revistas serias te van a pedir un checklist de **17 items** explicando exactamente qué hizo la IA, con qué versión, con qué supervisión humana. La skill te lo deja prerelleno también.

---

## Lo que te queda al final, en una carpeta

Todo aterriza en `~/Desktop/terminal/Publicaciones/<tema>/`:

- `master_corpus.xlsx` — la base de datos de tu RS
- `prisma_flow.png` — el diagrama oficial
- `manuscript/protocol_prospero.md` — para pegar en PROSPERO
- `manuscript/journal_recommendations.md` — qué revistas considerar
- `manuscript/manuscript.docx` — el manuscrito casi listo
- `manuscript/prisma_traice_checklist.md` — la declaración de uso de IA
- `meta_analysis/` con los gráficos (si lo pediste)

---

## Lo importante de entender

**La skill no escribe tu revisión sistemática por ti.** Lo que hace es:
- Automatizar lo aburrido (buscar, descargar, deduplicar, tabular, formatear).
- Guiarte por los puntos donde tienes que decidir tú (cribado fino, RoB, redacción crítica).
- Recordarte los estándares (PRISMA 2020, PROSPERO, PRISMA-trAIce) sin que tengas que mirarlos cada vez.
- Recuperarse si algo se cae a mitad del proceso.

**Resultado realista**: una RS que normalmente te llevaría 6 meses se puede dejar lista en **3-4 semanas de trabajo concentrado**, manteniendo el rigor para que sea publicable en revista indexada.
