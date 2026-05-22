# Scholar Scraper

Herramienta de extracción y verificación de publicaciones académicas. Procesa resultados de Google Scholar, enriquece los registros con metadatos desde Crossref, y verifica la indexación de cada paper en Scopus y Web of Science (WOS).

## Flujo general

```
ScholarScraper (Firefox/Chrome) → queries/<carpeta>/page_N.html
       ↓
ParserScholarLite → Crossref (DOI) → Scopus API / WOS API
       ↓
output/<query>_output/<timestamp>/scraped_papers.xlsx
```

## Requisitos previos

- Python 3.11+ y [uv](https://docs.astral.sh/uv/) (`pip install uv`)
- Firefox Portable (incluido en `browser/`) con perfil de usuario preconfigurado
- Cuenta institucional UNAP con acceso a Clarivate WOS
- API keys de [Scopus Developer](https://dev.elsevier.com/) y Clarivate WOS

## Instalación

1. Instalar dependencias con uv:
   ```powershell
   uv venv
   uv pip install -r requirements.txt
   ```

2. Crear el archivo `.env` en la raíz del proyecto:
   ```
   SCOPUS_API_KEY=tu_api_key_de_scopus
   WOS_API_KEY=tu_api_key_de_wos
   ```

## Uso

### Pipeline completo (recomendado)

`run_pipeline.py` ejecuta el scraping y el parseo en un solo comando:

```powershell
# Scraping + parseo (Firefox portable, 100 resultados)
uv run --with selenium run_pipeline.py "machine learning healthcare"

# Más resultados con verificación WOS/Scopus
uv run --with selenium run_pipeline.py "deep learning NLP" --max 200 --indexers

# Usar Chrome en lugar de Firefox (mejor stealth, requiere Chrome instalado)
uv run --with nodriver run_pipeline.py "tu query" --backend chrome --max 100

# Re-parsear una carpeta existente sin volver a scrapear
uv run --with selenium run_pipeline.py "tu query" --skip-scrape --out MiQuery
```

El resultado queda en `output/<query>_output/<timestamp>/scraped_papers.xlsx`.

### Pasos por separado

#### 1. Scrapear Google Scholar

```powershell
uv run --with selenium scholar_scraper_test.py "tu query" --max 100 --out MiQuery
```

Los HTMLs se guardan en `queries/MiQuery/page_0.html`, `page_10.html`, etc.

#### 2. Autenticar sesión en WOS

Abrir `browser/FirefoxPortable/FirefoxPortable.exe` (incluye el perfil institucional). Desde Firefox, ingresar al portal de biblioteca UNAP y acceder a **Clarivate WOS**. Esta sesión puede expirar — renovarla antes de cada ejecución si se usa verificación de indexadores.

#### 3. Parsear HTMLs guardados

```powershell
python main_scrape.py
```

Itera sobre todas las subcarpetas de `queries/` y genera `scraped_papers.xlsx` en `output/`. El tiempo de ejecución puede extenderse hasta 3 horas según el volumen de papers.

### Tampermonkey (alternativa manual)

El script `tampermonkey/open_all_links.js` permite scrapear Scholar manualmente desde el navegador:
- **Tecla K**: descarga la página actual como HTML.
- **Botón de apertura masiva**: abre resultados en bloques de 100.

Instalar con la extensión Tampermonkey e importar `open_all_links.js`. Los HTMLs descargados deben colocarse en `queries/<subcarpeta>/` antes de ejecutar `main_scrape.py`.

## Backends disponibles para el scraping

| Backend | Comando | Requisito | Notas |
|---|---|---|---|
| `firefox` (default) | `--with selenium` | Firefox Portable incluido | Usa perfil portable preconfigurado |
| `chrome` | `--with nodriver` | Chrome instalado en el sistema | Mejor evasión de detección, no usa CDP |

## Problemas conocidos

| Problema | Causa | Solución |
|---|---|---|
| CAPTCHA en Google Scholar | Demasiadas consultas seguidas | El scraper pausa y pide resolución manual; usar delays más largos entre sesiones. |
| Error 504 en Crossref | Timeout por alta carga del servicio | El scraper reintenta automáticamente; si persiste, reducir el volumen de consultas. |
| No se genera el archivo Excel | Excel está abierto durante la ejecución | Cerrar Excel antes de ejecutar el scraper. |
| Disco lleno por archivos temporales de Firefox | Firefox no limpia sus temporales automáticamente | Ejecutar `delete_trash.bat` para limpiar la carpeta de temporales. |
| Alto consumo de RAM por Firefox | Comportamiento propio de Selenium con Firefox | Pendiente de optimización. |
