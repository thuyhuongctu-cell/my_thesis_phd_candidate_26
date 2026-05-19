# Hướng dẫn Thu thập Dữ liệu WoS + Scopus cho P6

> **Lưu ý quan trọng:** Server Claude Code không thể truy cập WoS/Scopus do hạn chế mạng.
> Bạn cần chạy script này trên **máy tính cá nhân** (Windows/Mac) có kết nối internet.

---

## Bước 1: Cài đặt (chỉ cần làm 1 lần)

```bash
pip install selenium
```

Python >= 3.8 và Chrome (hoặc Edge) phải đã được cài sẵn trên máy.

---

## Bước 2: Copy script về máy local

Tải file `28_extract_wos_scopus_locally.py` từ `p6/tools/` về máy tính của bạn.

---

## Bước 3: Chạy script

### Thu thập dữ liệu WoS:
```bash
python3 28_extract_wos_scopus_locally.py --wos
```
Script sẽ hỏi:
- Email WoS: `huongp1323001@gstudent.ctu.edu.vn`
- Password: (nhập password của bạn)

### Thu thập dữ liệu Scopus:
```bash
python3 28_extract_wos_scopus_locally.py --scopus
```
Script sẽ hỏi:
- Email Scopus: `thuyhuongctu@gmail.com`
- Password: (nhập password của bạn)

### Cả WoS và Scopus:
```bash
python3 28_extract_wos_scopus_locally.py --wos --scopus
```

---

## Bước 4: Quy trình Export WoS

Script sẽ mở Chrome, đăng nhập WoS (qua tài khoản tổ chức CTU), và:

1. **Nhập query P6** vào ô Advanced Search
2. **Nhắc bạn kiểm tra bộ lọc:**
   - Document Type: `Article`
   - Language: `English`
   - Timespan: `1977–2026`
3. **Export từng batch 500 bản ghi** (WoS giới hạn 500/lần)
   - Chọn format: `Excel`
   - Chọn content: `Full Record`
   - Đặt range: `1–500`, `501–1000`, v.v.
4. Hỏi bạn có muốn export thêm batch không

**Lưu ý export WoS:**
- Nếu > 500 kết quả: cần nhiều lần export
- Files tự động save vào thư mục: `wos_scopus_export_YYYYMMDD/`

---

## Bước 5: Quy trình Export Scopus

1. Script đăng nhập bằng Gmail (`thuyhuongctu@gmail.com`)
2. Nhập query Scopus tự động
3. Export CSV — Scopus cho phép đến 2000 bản ghi/lần với quyền institutional
4. Chọn: `All available information`

**Lưu ý Scopus:**
- Nếu CTU campus IP không thoả: login sẽ vào chế độ free
- Trong trường hợp đó, export bị giới hạn 2000 records
- Nhớ kiểm tra bộ lọc: Article, English, 1977–2026

---

## Bước 6: Upload files về server

Sau khi download xong, upload files lên server để tiếp tục xử lý:

```bash
# Option 1: Dùng scp (nếu có SSH access vào server)
scp wos_scopus_export_*/savedrecs*.xls user@server:/home/user/PAPERS_IN_PHD_2026/p6/tools/results/
scp wos_scopus_export_*/scopus*.csv user@server:/home/user/PAPERS_IN_PHD_2026/p6/tools/results/

# Option 2: Dùng Claude Code — kéo thả file vào chat
# Sau đó Claude sẽ xử lý tự động
```

---

## Bước 7: Xử lý files trên server (Claude Code sẽ làm)

Sau khi có files, chạy trên server:

```bash
# WoS export → CSV chuẩn
python3 p6/tools/01_parse_wos_export.py --input p6/tools/results/savedrecs*.xls

# Scopus export → CSV chuẩn
python3 p6/tools/02_parse_scopus_export.py --input p6/tools/results/scopus*.csv

# Dedup + merge
python3 p6/tools/03_deduplicate_merge.py

# L1 screening
python3 p6/tools/04_screen_l1.py
```

---

## Query Strings (để paste thủ công nếu cần)

### WoS Advanced Search:
```
TS=(internationaliz* OR internationalis* OR multinationality 
    OR "degree of internationalization" OR "degree of internationalisation"
    OR "international diversification" OR "geographic diversification"
    OR "foreign sales" OR "foreign sales to total sales" OR FSTS
    OR "foreign assets" OR "foreign assets to total assets" OR FATA
    OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND 
TS=("firm performance" OR "enterprise performance" OR "corporate performance"
    OR "financial performance" OR "business performance"
    OR "labor productivity" OR "labour productivity" OR profitability 
    OR "Tobin's q" OR "return on assets" OR ROA OR "return on equity"
    OR "return on sales" OR "total factor productivity" OR "firm efficiency")
AND
TS=(correlation OR regression OR coefficient OR "effect size" OR "r =")
```

**Filters:** Timespan=1977–2026, Document Type=Article, Language=English

### Scopus Advanced Search:
```
TITLE-ABS-KEY(internationaliz* OR internationalis*
    OR multinationality OR "degree of internationalization"
    OR "international diversification" OR "geographic diversification"
    OR "foreign sales" OR FSTS OR "foreign assets" OR FATA
    OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND
TITLE-ABS-KEY("firm performance" OR "enterprise performance"
    OR "corporate performance" OR "financial performance" OR "business performance"
    OR "labor productivity" OR "labour productivity" OR profitability
    OR "return on assets" OR Tobin OR "return on equity"
    OR "return on sales" OR "total factor productivity" OR "firm efficiency")
AND
TITLE-ABS-KEY(correlation OR regression OR coefficient OR "effect size")
AND PUBYEAR > 1976 AND PUBYEAR < 2027
AND DOCTYPE(ar)
AND LANGUAGE(english)
```

---

## OSF Pre-registration (đã hoàn thành)

URL: **https://osf.io/z37kn**  
DOI: `10.17605/OSF.IO/Z37KN`  
Status: REGISTERED — 2026-05-18

Chỉ cần mở URL trên để verify. Login không cần thiết vì pre-reg là public.

---

## Troubleshooting

**Script dừng ở "Sign In button not found":**
- Đăng nhập thủ công trong cửa sổ Chrome
- Nhấn Enter trong terminal để tiếp tục

**WoS yêu cầu xác thực 2 bước:**
- Hoàn thành xác thực trong browser
- Nhấn Enter trong terminal khi đã vào trang kết quả

**Scopus không nhận institutional access:**
- Vào campus CTU hoặc dùng VPN CTU
- Hoặc export bản thường (tối đa 2000 records)

**Không export được đủ records:**
- WoS: mỗi lần tối đa 500, cần nhiều batch
- Scopus: tối đa 2000 với institutional, 20 không có
