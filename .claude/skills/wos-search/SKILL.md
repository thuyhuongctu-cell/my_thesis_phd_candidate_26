---
name: wos-search
description: Search Web of Science by topic, author, title, DOI, or advanced query. Supports edition/database filtering. Always sorts by relevance.
argument-hint: "[search keywords] [--edition SCI/SSCI/...] [--db woscc|alldb|...]"
user-invocable: true
disable-model-invocation: false
---

# WoS Search

Search Web of Science via internal API. Supports edition filtering, sorting, and multiple databases — all in a single `evaluate_script` call.

## Important: Browser Prerequisite

This skill calls the WoS internal API directly via `fetch` inside the MCP-controlled Chrome. A valid login session in **that same Chrome instance** is required — DO NOT start a separate Chrome with `--remote-debugging-port`; the `chrome-devtools` MCP launches its own browser, and any Chrome you start manually will not be the one running the API call.

### Pre-flight (run ONCE per session, ≤2 tool calls)

Before any search, perform a single login bootstrap. Do **not** repeat this on follow-up searches in the same session.

1. **Check whether the MCP browser is already on WoS and logged in.** Call `mcp__chrome-devtools__list_pages` once. Look for any page whose URL contains `webofscience.com`.
   - If such a page exists → select it with `select_page` and skip to Step 0. Do NOT open new tabs.
   - If no WoS page exists → continue to step 2.

2. **Open WoS in the MCP browser ONCE.** Call `mcp__chrome-devtools__new_page` (or `navigate_page` on the active tab) with URL `https://www.webofscience.com/wos/woscc/basic-search`. This is the only Chrome window the skill will ever touch.

3. **Hand control to the user for manual login, then STOP.** Print exactly:

   > Chrome 已打开 Web of Science 登录页。请在该窗口里完成登录（机构 SSO / 账号密码均可）。登录成功并看到检索首页后，回复"已登录"或"继续"，我再继续执行检索。

   **Do not call any further tools until the user confirms.** Do not poll, do not re-open pages, do not retry — wait for the user's text reply.

4. **After user confirmation**, verify session is live with ONE `evaluate_script` call that reads `localStorage.getItem('wos_sid')`. If the SID can be extracted, proceed to Step 0. If not, tell the user the login did not register and ask them to refresh that tab and reply again — still no extra `new_page` calls.

### Hard rules to avoid "Chrome keeps reopening"

- **Never** call `new_page` more than once per session. If a WoS tab already exists, reuse it via `select_page`.
- **Never** call `navigate_page` proactively to "refresh" the session unless an API call has just returned `no_session`. Even then, navigate the **existing** WoS tab — do not open a new one.
- **Never** instruct the user to launch Chrome with `--remote-debugging-port`. The MCP server owns the browser lifecycle.
- If `mcp__chrome-devtools__evaluate_script` is missing from the tool list, tell the user the `chrome-devtools` MCP server is not connected and stop — do not work around it by launching Chrome yourself.

## Language Guidance

WoS databases (especially SCI/SSCI) primarily index English-language literature. If the user provides Chinese keywords, translate to English (e.g., "价值共创" → "value co-creation"). Inform the user about the translation.

## Parameter Reference

### Database (`product`)

| User says | product | Description |
|-----------|---------|-------------|
| "core collection" / default | `WOSCC` | WoS Core Collection |
| "all databases" | `ALLDB` | All databases combined |
| "medline" | `MEDLINE` | Biomedical literature |
| "preprint" | `PPRN` | Preprint Citation Index |
| "scielo" | `SCIELO` | SciELO Citation Index |

### Edition filtering (Core Collection only)

| User says | editions value |
|-----------|---------------|
| "SCI" / "science" | `WOS.SCI` |
| "SSCI" / "social science" | `WOS.SSCI` |
| "CPCI" / "conference" | `WOS.CPCI-S`, `WOS.CPCI-SSH` |
| "all" / default | omit `editions` field (or include all) |

Multiple editions can be combined: `["WOS.SCI", "WOS.SSCI"]`

### Sort

This skill always uses `relevance` sort. Other sorts (citations, date, usage) are intentionally not exposed — multi-round searches and the 100-record cap rely on relevance ordering.

### Field mapping (for query rows)

| User says | rowField |
|-----------|----------|
| topic / keyword / about | TS |
| title | TI |
| author | AU |
| DOI | DO |
| journal / source | SO |
| year | PY |
| affiliation / institution | OG |
| abstract | AB |
| funding | FO |
| country | CU |

## Steps

### Step 0: Analyze Research Question

When the user provides a natural language research question (in Chinese or English), extract the core conceptual elements before constructing any query.

1. **Identify core concepts**: Parse the question into its constituent research concepts. A typical research question has 1-3 core concepts.
   - Example: "学前教育阶段家长教养方式对幼儿依恋行为的影响" → concepts: (1) parenting style (教养方式), (2) attachment behavior (依恋行为), (3) preschool children (学前儿童, as population context)
   - Example: "impact of AI on student learning outcomes" → concepts: (1) artificial intelligence, (2) student learning outcomes

2. **Determine concept count and search strategy**:
   - 1 concept → single search round
   - 2 concepts → 3 rounds (concept A, concept B, A AND B)
   - 3+ concepts → identify the 2 most central concepts for the 3-round strategy; treat remaining concepts as contextual filters applied to all rounds

3. **Detect implicit constraints**: Extract population, setting, methodology, or time constraints from the question (e.g., "preschool" → age filter, "higher education" → context, "in China" → geographic scope).

### Step 0.5: Expand Search Terms

For each core concept, generate English search term variants.

**Translation**: If the user provides Chinese terms, translate to English first. Inform the user of the translation.

**Variant generation rules**:
- Generate 3-6 English variants per concept, covering:
  - **Synonyms**: "parenting style" → "parenting pattern", "child-rearing practice"
  - **Related terms**: "parenting" → "parental behavior", "parent-child interaction"
  - **Broader/narrower terms**: "attachment" → "attachment security" (narrower), "bonding" (broader)
  - **Common academic variants**: "preschool" → "early childhood", "kindergarten", "young children"
  - **Truncation for coverage**: Use wildcard `*` where appropriate (e.g., "preschool*" covers preschool, preschooler, preschoolers)

**Population/context terms**: For contextual concepts (e.g., population), generate a focused set of 2-4 variants.

### Step 0.6: Construct Multi-Round Query Plan

Build a query plan based on the concept count determined in Step 0. **Results across rounds are merged by UNION (deduplicated by WoS ID), not intersected.** A 2-concept question can therefore yield up to 200 unique records (2 rounds × 100 cap), and a 3-concept question up to 300.

**Two-concept question (most common)**: 3 rounds
- Round 1: Concept A only (TS = expanded variants for concept A)
- Round 2: Concept B only (TS = expanded variants for concept B)
- Round 3: Concept A AND Concept B (TS = variants A) AND (TS = variants B)

For each round, combine variants within a concept with OR:
```
query: [
  {"rowField": "TS", "rowText": "(concept_a_var1 OR concept_a_var2 OR concept_a_var3)"},
  // if Round 3: add {"rowBoolean": "AND", "rowField": "TS", "rowText": "(concept_b_var1 OR concept_b_var2)"}
]
```

**Single-concept question**: 1 round with the concept's expanded terms.

**Three-concept question**: 3 rounds as above, with the third concept added as an AND condition to all rounds (e.g., `{"rowBoolean": "AND", "rowField": "TS", "rowText": "(context_var1 OR context_var2)"}`).

**Scoping**: All rounds use `"product": "WOSCC"` and `"database": "WOSCC"`. Sort is always `relevance`.

### Step 0.7: Confirm Query Plan with User (BLOCKING)

**Before executing any search**, present the full query plan to the user and wait for explicit approval or revision. Do not call `evaluate_script` for the search until the user replies.

Print exactly this template (filled in):

```
## 检索计划

**研究问题**：{user's original question}

**核心概念**：
- 概念 A — {concept A label}：{var_a1, var_a2, var_a3, ...}
- 概念 B — {concept B label}：{var_b1, var_b2, var_b3, ...}
（如有第三个上下文概念也列出）

**检索策略**（汇总合并，不取交集）：
| 轮次 | 检索式 | 预计上限 |
|------|--------|---------|
| 1 | TS = (var_a1 OR var_a2 OR ...) | 100 |
| 2 | TS = (var_b1 OR var_b2 OR ...) | 100 |
| 3 | TS = (concept A vars) AND TS = (concept B vars) | 100 |

**排序**：relevance（固定）
**数据库**：WoS Core Collection
**文献类型筛选**：Article + Review，英文摘要

请确认或补充检索词。回复"开始检索"我即执行；或者告诉我要增删/替换哪些词。
```

Wait for the user's reply. If they ask to change terms, update the plan and re-print it for re-confirmation. Only after explicit approval ("开始检索" / "确认" / "go" / similar) proceed to Step 1.

### Step 1: Build API Request Body

```json
{
  "product": "WOSCC",
  "searchMode": "general",
  "viewType": "search",
  "serviceMode": "summary",
  "search": {
    "mode": "general",
    "database": "WOSCC",
    "query": [
      {"rowField": "TS", "rowText": "USER_QUERY"}
    ],
    "editions": ["WOS.SSCI"]
  },
  "retrieve": {
    "count": 50,
    "history": true,
    "jcr": true,
    "sort": "relevance",
    "analyzes": [],
    "locale": "en"
  },
  "eventMode": null
}
```

- `query`: array of `{rowField, rowText}` objects. For multiple conditions, add `rowBoolean` (`AND`/`OR`/`NOT`) to subsequent rows.
- `editions`: optional, omit for all editions.
- `count`: 50 per page (max). Pagination via `wos-navigate-pages` collects up to 100 records per round.
- `sort`: always `relevance`.

### Step 2: Execute API Call via evaluate_script

**For each query round** (1, 2, or 3 depending on concept count): one `evaluate_script` call for the first 50 records. If `RecordsFound > 50`, hand off to `wos-navigate-pages` to fetch page 2 (records 51–100). Cap each round at **100 records**.

Across rounds, **merge by union of `wosId`** — deduplicate but preserve every unique record. Do NOT intersect rounds.

If a previous follow-up action moved the existing WoS tab to an external site and SID has been lost, navigate **that same tab** back to `https://www.webofscience.com/wos/woscc/basic-search` (do NOT open a new tab) and retry. Step 2B remains available as a URL-based fallback.

```javascript
async () => {
  // PRIMARY: SID is stored in localStorage as key 'wos_sid' (with surrounding quotes)
  let sid = (localStorage.getItem('wos_sid') || '').replace(/"/g, '');

  // Fallback 1: performance entries
  if (!sid) {
    sid = performance.getEntriesByType('resource')
      .filter(r => r.name.includes('SID='))
      .map(r => r.name.match(/SID=([^&]+)/)?.[1])
      .filter(Boolean)[0] || '';
  }

  // Fallback 2: DOM links
  if (!sid) {
    const links = document.querySelectorAll('a[href*="SrcAppSID="]');
    for (const a of links) {
      const m = a.href.match(/SrcAppSID=([^&]+)/);
      if (m) { sid = m[1]; break; }
    }
  }

  if (!sid) return { status: 'no_session', message: 'SID lost. Navigate to any WoS page first, then retry.' };

  const response = await fetch(`/api/wosnx/core/runQuerySearch?SID=${sid}`, {
    method: 'POST',
    headers: { 'Content-Type': 'text/plain;charset=UTF-8', 'Accept': 'application/x-ndjson' },
    body: JSON.stringify({
      "product": "{PRODUCT}",
      "searchMode": "general",
      "viewType": "search",
      "serviceMode": "summary",
      "search": {
        "mode": "general",
        "database": "{PRODUCT}",
        "query": [{QUERY_ROWS}],
        "editions": [{EDITIONS}]
      },
      "retrieve": {
        "count": 50,
        "history": true,
        "jcr": true,
        "sort": "relevance",
        "analyzes": [],
        "locale": "en"
      },
      "eventMode": null
    })
  });

  const text = await response.text();
  const lines = text.trim().split('\n').map(line => {
    try { return JSON.parse(line); } catch(e) { return null; }
  }).filter(Boolean);

  const searchInfo = lines.find(l => l.key === 'searchInfo')?.payload;

  // Merge ALL records lines (API splits 50 records across multiple NDJSON lines)
  const allRecords = {};
  lines.filter(l => l.key === 'records').forEach(l => {
    if (l.payload) Object.assign(allRecords, l.payload);
  });

  // Parse JCR data
  const jcrData = lines.find(l => l.key === 'jcr')?.payload || {};

  // Filter: only English-language Article or Review
  const allowedTypes = ['Article', 'Review'];
  let records = [];
  let filteredCount = 0;
  if (Object.keys(allRecords).length > 0) {
    const mapped = Object.entries(allRecords).map(([idx, rec]) => {
      const jcrInfo = jcrData[rec.jcrKey] || {};
      const catData = jcrInfo.CategoryIFData || [];
      const primaryCat = catData[0] || {};

      return {
        idx: parseInt(idx),
        wosId: rec.colluid,
        title: rec.titles?.item?.en?.[0]?.title || '',
        authors: rec.names?.author?.en?.filter(Boolean).map(a => a.wos_standard).join('; ') || '',
        source: rec.titles?.source?.en?.[0]?.title || '',
        year: rec.pub_info?.pubyear || '',
        vol: rec.pub_info?.vol || '',
        issue: rec.pub_info?.issue || '',
        pages: rec.pub_info?.page_no || '',
        doi: rec.doi || '',
        citations: rec.citation_related?.counts?.WOSCC || 0,
        citationsAll: rec.citation_related?.counts?.ALLDB || 0,
        refCount: rec.ref_count || 0,
        abstract: (rec.abstract?.basic?.en?.abstract || '').replace(/<[^>]*>/g, ''),
        docType: rec.doctypes?.[0] || '',
        oa: rec.oa || false,
        impactFactor: jcrInfo.ImpactFactor || '',
        jifQuartile: primaryCat.JifQuartile || '',
        jifRank: primaryCat.JifRank || '',
        jifPercentile: primaryCat.JifPercentile || '',
        category: primaryCat.CategoryName || '',
        edition: primaryCat.Edition || ''
      };
    });
    // Apply filters: English language (abstract exists) + Article/Review
    records = mapped.filter(r => {
      const isEnglish = r.abstract.length > 0;
      const isArticleOrReview = allowedTypes.includes(r.docType);
      if (!isEnglish || !isArticleOrReview) { filteredCount++; return false; }
      return true;
    });
    // Re-index after filtering
    records.forEach((r, i) => { r.idx = i + 1; });
  }

  return {
    status: 'ok',
    totalResults: searchInfo?.RecordsFound || 0,
    recordsSearched: searchInfo?.RecordsSearched || 0,
    queryId: searchInfo?.QueryID || '',
    records,
    filteredCount
  };
}
```

### Step 2.5: Per-Round Retention and Cross-Round Union

After Step 2 returns for a given round:

1. **Retention policy** (per round): keep **all** records the API returns (up to 100 after pagination). Do not truncate to "top N" inside a round. The Article/Review + English filter still applies, but no further trimming.
2. **If `searchInfo.RecordsFound > 50`**, call `wos-navigate-pages` to fetch page 2 (offset 51, count 50). Combine page-1 + page-2 records for this round, max 100.
3. **If `RecordsFound > 100`**, log the truth (`totalAvailable: RecordsFound`, `retrieved: 100`) — do NOT issue more pagination calls. Relevance sort guarantees the kept 100 are the most relevant.
4. After all rounds finish, **union by `wosId`**: take the deduplicated set of every record across rounds. For each unique record, also annotate which round(s) it appeared in (e.g., `foundIn: ["A", "B", "AB"]`) — this lets the user see overlap without dropping anything.

Maximum unique records:
- 1 concept: 100
- 2 concepts: 200 (rounds A, B, AB; some overlap typical)
- 3 concepts: 300


### Step 3: Present Results

Display search strategy and results. For multi-round searches, present each round's summary then the merged (union) result.

```
## Search: {research question summary}

### Search Terms Used
- **Concept A**: {concept_a_variants}
- **Concept B**: {concept_b_variants}
- **Strategy**: {multi-round description}, union merge across rounds

### Results
Found **{unique_total}** unique records across all rounds (union, deduplicated by WoS ID).
Database: WoS Core Collection. Document types: Article + Review only, English. Sort: relevance (fixed).

| # | Title | Year | Cited | IF | Q | Found In | WoS ID |
|---|------|------|-------|----|---|----------|--------|
| 1 | {title} | {year} | {citations} | {impactFactor} | {jifQuartile} | A,AB | {wosId} |
| ... |
```

For multi-round searches, also show per-round statistics:

```
### Per-Round Summary
| Round | Search Terms | API totalAvailable | Retrieved (≤100) | After Filter |
|-------|-------------|--------------------|------------------|--------------|
| A     | {terms_a}   | {n_a}             | {r_a}            | {f_a}        |
| B     | {terms_b}   | {n_b}             | {r_b}            | {f_b}        |
| A AND B | {terms_ab} | {n_ab}            | {r_ab}           | {f_ab}       |
| **Union (unique by wosId)** | | | | **{unique_total}** |
```

Offer next actions:
- "Use `/wos-paper-detail {WoS ID}` for detailed information"
- "Use `/wos-export` to export results"
- Results have been auto-saved (see Step 4).

### Step 4: Auto-Save Results (mandatory, no user prompt)

After presenting results, **always** save the full union-merged result set to a fixed JSON file. Do NOT ask the user — this step runs automatically.

**Output path**: `wos_search_results.json` in the current working directory.

**Output format**: A single JSON array of record objects. Each object has these fields (all values are strings unless noted):

| Field | Type | Source |
|-------|------|--------|
| `idx` | integer | 1-based index after union merge (re-numbered) |
| `wosId` | string | `rec.colluid` |
| `title` | string | `rec.titles.item.en[0].title` |
| `authors` | string | WoS standard format, `; ` separated |
| `source` | string | Journal/book title |
| `year` | string | Publication year |
| `vol` | string | Volume |
| `issue` | string | Issue |
| `pages` | string | Page range |
| `doi` | string | DOI (no prefix) |
| `citations` | integer | WOSCC citation count |
| `citationsAll` | integer | ALLDB citation count |
| `refCount` | integer | Reference count |
| `abstract` | string | Full abstract, HTML tags stripped |
| `docType` | string | Document type (Article / Review) |
| `oa` | boolean | Open Access flag |
| `impactFactor` | string | JCR Impact Factor |
| `jifQuartile` | string | JIF Quartile (Q1-Q4) |
| `jifRank` | string | JIF Rank (e.g. "34/94") |
| `jifPercentile` | string | JIF Percentile |
| `category` | string | Primary WoS category |
| `edition` | string | Edition (SSCI / SCI) |
| `foundIn` | array of strings | Which rounds the record appeared in (e.g. `["R1","R3"]`) |

**Sort order**: Relevance (preserved from WoS API). Records are sorted by the order they first appear during the union merge — earlier rounds take precedence, and within each round the API's relevance ranking is preserved. This means records from R1 come before R2, then R3, each group maintaining the original relevance order from the API response.

**Implementation**: Use `JSON.stringify()` via Node.js to ensure proper escaping of all special characters (double quotes, backslashes, newlines, Unicode). Write with `fs.writeFileSync`.

```bash
node -e "
const fs = require('fs');
// Preserve relevance order: earlier rounds first, within each round API relevance order
// allRecords should be a Map with insertion order preserved during union merge
const sorted = [...allRecords.values()];
sorted.forEach((r, i) => { r.idx = i + 1; });
fs.writeFileSync('wos_search_results.json', JSON.stringify(sorted, null, 2));
console.log('Saved ' + sorted.length + ' records to wos_search_results.json');
"
```

**Note**: Because `JSON.stringify` handles all escaping, special characters in abstracts (double quotes, backslashes, HTML entities, Unicode) will never corrupt the file. The output is always valid JSON, safe for downstream consumption by `JSON.parse()`, Python `json.load()`, or the Zotero export script.

### Step 2B: URL-based Fallback (when SID is lost)

If API returns `no_session` (e.g., after navigating to an external publisher site), fall back to URL navigation:

```
navigate_page({
  url: "https://www.webofscience.com/wos/{db}/general-summary?queryJson={ENCODED_QUERY_JSON}",
  initScript: "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})
```

Then extract results via `evaluate_script` with DOM selectors (see `wos-parse-results` Mode B), or re-attempt the API call (SID will be re-established after the navigation).

**When to use**: After the browser visited an external site (publisher, DOI link, etc.) and `performance.getEntriesByType('resource')` no longer contains WoS SID entries.

## Notes

- **Pre-flight**: 1 `list_pages` call, plus at most 1 `new_page`/`navigate_page` if no WoS tab exists — then a hard pause for manual login. After the user confirms, **the user-facing query plan (Step 0.7) is also gated by an explicit "开始检索" reply** before any search fires.
- **One Chrome only**: the skill operates on the single MCP-controlled Chrome instance. Never spawn extra tabs, never ask the user to launch Chrome themselves with `--remote-debugging-port`.
- **Sort is fixed to `relevance`**. The 100-records-per-round cap depends on relevance ordering — exposing other sorts would silently drop the most relevant items when `RecordsFound > 100`.
- API returns NDJSON (newline-delimited JSON); records are split across multiple `records` lines — merge all of them.
- **SID extraction**: primary source is `localStorage.getItem('wos_sid')` (the value is JSON-stringified, so strip surrounding `"`). Fallbacks: `performance.getEntriesByType('resource')` then DOM `a[href*="SrcAppSID="]`. The original `performance` path was unreliable because WoS does not consistently embed the SID in resource URLs.
- **SID loss after follow-up actions**: if a later step navigates the existing tab to a publisher site, recover by `navigate_page` on that **same** tab back to `https://www.webofscience.com/wos/woscc/basic-search`. Still do not open a new tab.
- `editions` field uses format `WOS.SCI`, `WOS.SSCI`, `WOS.CPCI-S`, etc.
- For Chinese keywords in SCI/SSCI, translate to English first.
- **Per-round retrieval**: 50 records per API call, paginate to 100 max via `wos-navigate-pages`. **Per-round cap is 100**, not 50. **Across rounds, results are union-merged** (deduplicated by `wosId`) — never intersected. Max unique records: 100 (1 concept) / 200 (2) / 300 (3).
- `history: true` saves the search to WoS session history.
- **Always included**: full abstract (no truncation), impact factor, JIF quartile, JIF rank, JIF percentile, category, edition.
