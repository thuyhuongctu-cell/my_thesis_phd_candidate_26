# Kế hoạch thu đủ r cho 656 papers (P6 meta-analysis)

**Trạng thái hiện tại (21/05/2026):** Y=683 | r đã có=27 | **r còn thiếu=656**

---

## Tổng quan pipeline

```
656 Y papers cần r
│
├─ 474 có DOI ──────────────────────────────────────────────┐
│   ├─ ~35% OA ≈ 166 PDFs  ← [Bước 1: Unpaywall GitHub Action]
│   ├─ ~20% thêm via S2    ≈ +83 PDFs  ← [Bước 2: S2 GitHub Action]
│   └─ còn ~225 paywalled  ← [Bước 5: manual + Sci-Hub local]
│
├─ 68 có URL trực tiếp ─────────────────────────────────────┤
│   └─ download thẳng       ← [Bước 3: PDF Download Action]
│
└─ 182 không có DOI ─────────────────────────────────────────┘
    └─ manual Google Scholar ← [Bước 6: manual queue]

  Claude API extract r từ PDFs ← [Bước 4: Claude API Action]
  Expected yield: ~320-380 papers (~50-58% of 656)
```

---

## Bước 1: Unpaywall OA Manifest (GitHub Actions)

**Workflow:** `unpaywall_query.yml`

Chạy trên GitHub → Actions:
- Input file: `extraction_queue_v2_20260521.csv`
- Output: `oa_manifest_20260521.csv`
- Queries: 474 DOI papers × 0.15s = ~71 giây

```
Actions → Run workflow:
  queue_file: extraction_queue_v2_20260521.csv
  output_file: oa_manifest_20260521.csv
  priority: 1_DOI_FIRST
```

**Expected:** ~30-40% OA = 142–190 PDF links

---

## Bước 2: Semantic Scholar Fallback (GitHub Actions)

**Workflow:** `semantic_scholar_query.yml`

- Input: `oa_manifest_20260521.csv` (rows where `is_oa=False`)
- Tìm thêm PDF links qua S2 public PDFs

```
Actions → Run workflow:
  manifest_file: oa_manifest_20260521.csv
  output_file: s2_manifest_20260521.csv
```

---

## Bước 3: PDF Download + Regex Extract (GitHub Actions)

**Workflow:** `pdf_download_extract.yml`

- Downloads PDFs from Unpaywall + S2 URLs
- Runs `41_auto_extract_from_pdfs.py` (regex-based, fast)
- Expected: ~100-150 papers extracted

```
Actions → Run workflow:
  queue_file: extraction_queue_v2_20260521.csv
  limit: 0
  run_extract: true
```

---

## Bước 4: Claude API Deep Extraction (GitHub Actions)

**Workflow:** `claude_api_extract_r.yml`  ← MỚI (57_claude_api_extract_r.py)

**Requires:** `ANTHROPIC_API_KEY` secret trong GitHub repo settings

Thiết lập secret:
1. GitHub repo → Settings → Secrets and variables → Actions
2. New repository secret: `ANTHROPIC_API_KEY` = `sk-ant-...`

Chạy extraction:
```
Actions → Run workflow:
  queue_file: extraction_queue_v2_20260521.csv
  manifest_file: oa_manifest_20260521.csv
  limit: 50  ← tăng dần (50 → 100 → 200 mỗi lần)
```

**Chi phí ước tính:**
- Model: claude-haiku-4-5-20251001 ($0.25/M input, $1.25/M output)
- ~8k tokens/paper input, ~256 tokens output
- 100 papers ≈ $0.22
- 500 papers ≈ $1.10
- Toàn bộ 656 papers ≈ **< $2.00**

---

## Bước 5: Manual Download + Upload (Người dùng)

Cho những papers vẫn thiếu r sau Bước 1-4:

**Cách A: Upload PDF trực tiếp vào Claude Code**
```
/meta-analysis-coefficient-extractor
→ Đính kèm PDF → Claude trích xuất r
→ Điền vào tracker
```

**Cách B: Chạy script local**
```bash
# Trên máy cá nhân:
python3 p6/tools/40_batch_download_pdfs.py \
  --manifest p6/tools/results/oa_manifest_20260521.csv \
  --output-dir p6/pdfs/

# Rồi push PDFs về repo (hoặc upload ZIP)
```

**Cách C: Dùng WoS/Scopus có tài khoản**
- Login WoS/Scopus trên máy local
- Download PDF từ danh sách `manual_download_queue_20260521.csv`

---

## Bước 6: Điền tracker sau khi có r

Với mỗi r mới:
```python
# Script cập nhật hàng loạt:
python3 p6/tools/58_bulk_fill_r.py \
  --input p6/tools/results/r_batch_input.csv \
  --tracker p6/tools/results/fulltext_to_extraction_tracker_v3.csv
```

Hoặc dùng `/p6-l2-extraction-assistant` để điền trực tiếp.

---

## Bước 7: MARA re-run sau khi đủ r

Target: ≥ 400 papers với r (>50% of 656) → đủ để update k và meta-regression

```r
# p6/tools/meta_r_scripts/01_baseline_model.R
# sau khi có ≥ 400 r values
```

---

## Tracking progress

```bash
python3 -c "
import csv
from collections import Counter
rows = list(csv.DictReader(open('p6/tools/results/fulltext_to_extraction_tracker_v3.csv')))
y    = [r for r in rows if r.get('fulltext_screening_decision','')=='Y']
done = sum(1 for r in y if r.get('converted_r','').strip())
print(f'Y={len(y)} | r_done={done} | r_need={len(y)-done} ({round((len(y)-done)/len(y)*100,1)}%)')
"
```

---

## Files chính

| File | Mục đích |
|------|----------|
| `p6/tools/results/extraction_queue_v2_20260521.csv` | 656 papers cần r (queue input) |
| `p6/tools/results/oa_manifest_20260521.csv` | Unpaywall OA links (sau Bước 1) |
| `p6/tools/results/s2_manifest_20260521.csv` | S2 PDF links (sau Bước 2) |
| `p6/tools/results/claude_extract_log_*.csv` | Claude API extraction log |
| `p6/tools/results/auto_extract_log_*.csv` | Regex extraction log |
| `p6/tools/57_claude_api_extract_r.py` | Claude API extractor (MỚI) |
| `.github/workflows/claude_api_extract_r.yml` | GitHub Action (MỚI) |

---

## Thứ tự ưu tiên

| Ưu tiên | Nhóm | Số lượng | Phương pháp |
|---------|------|----------|-------------|
| 🟢 Cao | APAC rõ ràng (Korea/India/Malaysia/Taiwan) | ~50 | Claude API |
| 🟢 Cao | OA PDFs có link (Unpaywall/S2) | ~250 | GitHub Actions auto |
| 🟡 Trung bình | URL sẵn trong tracker | 68 | GitHub Actions |
| 🟡 Trung bình | Local PDFs (pdf_found=Y, 56 papers) | 56 | 41_auto_extract |
| 🔴 Thấp | Paywalled, không có DOI | ~182 | Manual/local |
