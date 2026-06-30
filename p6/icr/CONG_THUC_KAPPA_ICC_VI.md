# P6 — Công thức κ / ICC và hướng dẫn nhập số (Inter-Coder Reliability)

> Mục đích: điền **6 ô `[insert after dual-coding]`** trong Bảng 3.1 của P6 (4 package
> jwb/jim/apjm/ibr + bản dịch VI) bằng số **thật** từ mã hóa kép. Tài liệu này giải thích
> công thức để khi bảo vệ/biên tập hỏi, cô trả lời được; phần tính toán đã tự động hóa trong
> `02_compute_icr.py` — cô chỉ cần **nhập mã của Coder 2** rồi chạy một lệnh.

---

## 1. Thiết kế (theo Mục 3.3.2 bản thảo)

- Hai người mã hóa **độc lập, mù lẫn nhau** trên **20% mẫu phân tầng = k = 47 nghiên cứu**
  (rút từ 238 nghiên cứu, seed 2026, phân tầng theo ICRV: I = 21, III = 16, MX = 5, II = 4, FR = 1).
- Coder 1 = NCS (đã có sẵn trong `icr_subsample_master.csv`).
- Coder 2 = GVHD (thầy Tú) — mã hóa vào phiếu trống, **không xem** file master.
- 5 biến mã hóa: `icrv`, `dpl`, `doi_type`, `fp_type` (định danh) + `cdai` (thứ bậc L/M/H).

---

## 2. Công thức Cohen's kappa (κ) — biến định danh

κ đo mức đồng thuận giữa hai người **đã loại trừ phần đồng thuận do may rủi**:

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

- $p_o$ = tỷ lệ đồng thuận quan sát (số nghiên cứu hai người mã giống nhau ÷ k).
- $p_e$ = tỷ lệ đồng thuận **kỳ vọng do ngẫu nhiên** = $\sum_i (p_{i\cdot}\, p_{\cdot i})$,
  với $p_{i\cdot}$, $p_{\cdot i}$ là tỷ lệ biên của hạng $i$ ở Coder 1 và Coder 2.

Dạng tổng quát có trọng số (script dùng ma trận trọng số $W$):

$$\kappa = 1 - \frac{\sum_{ij} w_{ij}\,O_{ij}}{\sum_{ij} w_{ij}\,E_{ij}}$$

- $O_{ij}$ = số quan sát ở ô (Coder 1 = $i$, Coder 2 = $j$); $E_{ij}$ = tần số kỳ vọng.
- **Không trọng số (định danh):** $w_{ij} = 0$ nếu $i = j$, $= 1$ nếu khác → mọi bất đồng phạt như nhau.

## 3. Weighted κ (κ có trọng số tuyến tính) — biến thứ bậc `cdai` (L < M < H)

Với biến **thứ bậc**, bất đồng L↔H nặng hơn L↔M. Dùng trọng số tuyến tính:

$$w_{ij} = \frac{|i - j|}{k - 1}$$

(ví dụ k = 3 hạng: L↔M có $w = 0{,}5$; L↔H có $w = 1$). Script in **cả** κ không trọng số
lẫn κ trọng số tuyến tính cho `cdai`.

## 4. ICC(2,1) — chỉ dùng nếu cDAI là điểm liên tục 0–1

Nếu sau này cô bổ sung **cột điểm cDAI liên tục (0–1)** thay cho mã L/M/H, độ tin cậy đo bằng
**Intraclass Correlation, hai chiều ngẫu nhiên, đồng thuận tuyệt đối, một người đánh** = ICC(2,1):

$$\text{ICC}(2,1) = \frac{MS_R - MS_E}{MS_R + (k-1)MS_E + \dfrac{k}{n}(MS_C - MS_E)}$$

- $MS_R$ = trung bình bình phương giữa các nghiên cứu (rows);
- $MS_C$ = giữa hai người mã (columns); $MS_E$ = sai số; $n$ = số nghiên cứu, $k = 2$ người.

Script tự phát hiện: nếu `cdai` chỉ chứa L/M/H → tính κ; nếu là số 0–1 → tính ICC(2,1).

---

## 5. Ngưỡng diễn giải (điền vào bản thảo)

| Thống kê | Ngưỡng đạt | Diễn giải (Landis & Koch 1977) |
|---|---|---|
| Cohen κ | **≥ 0,70** | 0,61–0,80 = "đáng kể (substantial)"; > 0,80 = "gần như hoàn hảo" |
| Weighted κ | ≥ 0,70 | như trên |
| ICC(2,1) | **≥ 0,80** | > 0,75 = "xuất sắc" |

Nếu một biến < 0,70: hai người **thảo luận giải quyết bất đồng**, cập nhật `notes` trong database,
mã lại nếu cần, rồi chạy lại script. (Script tự liệt kê các `study_id` bất đồng theo từng biến.)

---

## 6. Quy trình nhập số (cô chỉ làm 3 bước)

**Bước 1 — Coder 2 mã hóa.** Mở **`icr_coding_sheet_coder2_BLANK.xlsx`** (có sẵn dropdown,
ô vàng = cần điền, sheet *Codebook* nhắc giá trị hợp lệ). Với mỗi nghiên cứu, chọn giá trị 5 cột.
Lưu thành **`icr_coding_sheet_coder2_FILLED.xlsx`** (cùng thư mục `p6/icr/`).
*(Nếu quen CSV hơn, dùng `icr_coding_sheet_coder2_BLANK.csv` rồi lưu `..._FILLED.csv` — script đọc cả hai.)*

**Bước 2 — Chạy một lệnh:**
```bash
python3 p6/icr/02_compute_icr.py
```
Script in bảng κ cho 4 biến định danh + κ (thường & trọng số) cho `cdai`, kèm danh sách bất đồng.
Script **từ chối chạy** nếu phiếu thiếu ô → không thể tạo số liệu từ dữ liệu khống.

**Bước 3 — Dán κ vào bản thảo.** Chép 6 giá trị κ vào 6 ô `[insert after dual-coding]` của Bảng 3.1
trong cả 4 package + bản VI, rồi dựng lại docx. (Hoặc gửi kết quả cho Claude — Phase C — để nhập + tái sinh.)

---

## 7. File liên quan

| File | Vai trò |
|---|---|
| `icr_subsample_master.csv` | Mã Coder 1 (NCS) — **Coder 2 không xem** |
| `icr_coding_sheet_coder2_BLANK.xlsx` | Phiếu Excel có dropdown cho Coder 2 (khuyến nghị) |
| `icr_coding_sheet_coder2_BLANK.csv` | Phiếu CSV trống (phương án thay thế) |
| `make_coder2_workbook.py` | Sinh lại file .xlsx từ .csv (nếu cần) |
| `02_compute_icr.py` | Tính κ/ICC (đọc FILLED .xlsx hoặc .csv) |
| `CONG_THUC_KAPPA_ICC_VI.md` | Tài liệu này |

> ⚠️ 3 điểm lệch mô tả Bảng 3.1 ↔ database (DOI 4 vs 6 nhóm; cDAI liên tục vs L/M/H;
> dòng "Industry sector") — xem `README_ICR_VI.md` mục cuối, cô quyết trước khi nộp.
