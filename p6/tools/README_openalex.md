# Hướng dẫn chạy OpenAlex PRISMA Search cho P6

## Yêu cầu

```bash
pip install requests
```

Python 3.9+ (không cần thêm thư viện nào khác).

## Chạy script

Trên máy tính của bạn (có internet):

```bash
cd /path/to/PAPERS_IN_PHD_2026/p6/tools
python3 openalex_prisma_search.py
```

Script sẽ:
1. Chạy 5 queries trên OpenAlex API (~15–30 phút tùy số kết quả)
2. Deduplicate tự động theo OpenAlex ID
3. Xuất CSV: `results/openalex_raw_YYYYMMDD.csv`
4. Ghi log PRISMA: `results/search_log.jsonl`
5. In ra màn hình các con số cho PRISMA flow diagram

## Output mẫu (cuối script)

```
PRISMA IDENTIFICATION — OpenAlex counts to enter in flow diagram:
  Q1_main                              n =  12,345  (12,345 retrieved)
  Q2_internationalisation              n =   3,210  (3,210 retrieved)
  Q3_export_intensity                  n =   4,567  (4,567 retrieved)
  Q4_multinationality                  n =   2,890  (2,890 retrieved)
  Q5_geographic_diversification        n =   3,100  (3,100 retrieved)

  TOTAL UNIQUE (after deduplication)   n =  18,000

📋 Copy these numbers into:
   p6/p6_prisma_flow.md  — OpenAlex section (supplementary search)
   p6/p6_meta_manuscript_en.md  — §3.1 Information sources
```

## Sau khi có kết quả

### Bước 1: Ghi kết quả vào p6_prisma_flow.md
Mở `p6/p6_prisma_flow.md` và điền vào phần OpenAlex (đã có sẵn).

### Bước 2: Screening bằng Excel/Python
File CSV có các cột: `openalex_id, doi, title, first_author, year, journal, cited_by_count, is_oa, oa_url`

Để Title/Abstract screening nhanh:
- Lọc theo journal (chỉ giữ SSCI/SCIE journals)
- Sort theo `cited_by_count` giảm dần để xem papers quan trọng trước
- Đọc title đến xem có liên quan I–P không

### Bước 3: Cross-reference với k=238 database hiện có
So sánh DOIs trong CSV với DOIs trong `p6/p6_primary_studies_apa7.md` để tìm studies mới.

## Lưu ý

- **Không yêu cầu API key** — OpenAlex hoàn toàn miễn phí
- **Rate limit**: 10 req/giây với email, 1 req/giây không có email
- **Coverage**: ~250M+ publications, rộng hơn WoS/Scopus
- **Language filter**: `language:en` — chỉ tiếng Anh
- **Type filter**: `type:article` — chỉ journal articles (không conference, book chapter)

## Điều chỉnh queries

Nếu muốn narrow down (giảm kết quả không liên quan), chỉnh `QUERIES` trong script:

```python
# Ví dụ: thêm "meta-analysis" để loại trừ nếu cần
"filter": "type:article,...,concepts.id:C2778793908"  # concept ID cho "international trade"
```

Xem thêm: https://docs.openalex.org/api-entities/works/filter-works
