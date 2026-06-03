# Supplement S-MAIDA: Cấu hình và đánh giá quy trình trích xuất dữ liệu hỗ trợ LLM

**Phụ lục bổ sung cho Chương 3, Mục 3.2.4 (Quy trình trích xuất dữ liệu hỗ trợ bằng mô hình ngôn ngữ lớn).**

> ⚠️ **TRẠNG THÁI: TEMPLATE — NCS CẦN ĐIỀN TRƯỚC KHI NỘP DEFENSE / SUBMIT P6.**
>
> File này hiện ở dạng *khung* (template) với các trường `[TO FILL]` chưa có giá trị thực tế. Đây *không phải nội dung bịa hay nội dung giả định* — các trường yêu cầu dữ liệu *log thực tế* từ phiên trích xuất M-AIDA và đánh giá *gold-standard* mà chỉ NCS truy cập được. Trước khi nộp định bản (defense hoặc P6 submission), NCS phải điền đầy đủ:
> - §S-MAIDA.1: Cấu hình LLM (model, version, provider, temperature, ngày bắt đầu/kết thúc) — từ log API
> - §S-MAIDA.2: Prompt template thực tế đã dùng — từ M-AIDA source / NCS notes
> - §S-MAIDA.4: Cỡ tập gold-standard + chiến lược chọn mẫu + người trích xuất tham chiếu
> - §S-MAIDA.5: Inter-rater agreement metrics (Cohen's κ hoặc Krippendorff's α)
> - §S-MAIDA.6: Error rate phân tích (false positive / false negative / mismatch)
>
> Tham chiếu chéo: Chương 3 §3.2.4 + P6 §3.2 đều giả định Supplement S-MAIDA đã hoàn tất. Trạng thái template hiện tại là *nguy cơ desk-reject* nếu P6 nộp APJM trước khi điền xong, đồng thời là *nguy cơ phản biện* tại defense về độ tin cậy của quy trình trích xuất.
>
> **Đối chiếu nhất quán với hệ thống M-AIDA:**
> - Phiên bản phần mềm: M-AIDA v7.0.0 (SHA-256: `bd74600cc909e396daf0b33549debd081b6c990904f96a5976e9186c2e18d696`)
> - Corpus cuối: k = 238 nghiên cứu / K = 288 cỡ hiệu ứng (`p6_study_database.csv` trên OSF z37kn)
> - Khung moderator P6: ICRV / cDAI / DPL — ánh xạ vào khung phân tầng CIMT–ICRV–CDCM tại Chương 2 §2.5

---

## S-MAIDA.1 Cấu hình mô hình ngôn ngữ lớn

| Thành phần | Giá trị |
|---|---|
| Mô hình | `[TO FILL: ví dụ "Claude 3.5 Sonnet", "GPT-4o", "Llama 3 70B"]` |
| Phiên bản / build date | `[TO FILL: ví dụ "claude-3-5-sonnet-20241022"]` |
| Nhà cung cấp | `[TO FILL: Anthropic / OpenAI / Meta / khác]` |
| Phương thức truy cập | `[TO FILL: API trực tiếp / web interface / local inference]` |
| Tham số sampling | `[TO FILL: temperature, top_p, max_tokens]` |
| Cửa sổ ngữ cảnh | `[TO FILL: ví dụ 200K tokens]` |
| Ngày bắt đầu sử dụng | `[TO FILL: dd/mm/yyyy]` |
| Ngày kết thúc trích xuất | `[TO FILL: dd/mm/yyyy]` |

---

## S-MAIDA.2 Prompt template

Phiên bản prompt đã sử dụng để tạo bản nháp trích xuất:

```
[TO FILL: Dán nguyên văn prompt template đã dùng. Nên gồm:
 - System message định nghĩa vai trò
 - Instructions về đại lượng cần trích xuất
 - Schema đầu ra (JSON / cấu trúc bảng)
 - Quy tắc chuyển đổi β → r nếu áp dụng
 - Few-shot examples nếu có
]
```

**Sai số phiên bản prompt:** `[TO FILL: nếu đã thay đổi prompt giữa các đợt trích xuất, liệt kê các phiên bản và lý do]`

---

## S-MAIDA.3 Quy trình HITL ba bước

| Bước | Thao tác | Người thực hiện | Sản phẩm |
|---|---|---|---|
| 1. Bản nháp tự động | PDF → LLM → đề xuất $N$, $r$, $\beta$, $t$, $df$, vị trí | Hệ thống | JSON bản nháp + đoạn trích nguyên văn |
| 2. Rà soát thủ công | Đối chiếu từng đại lượng với PDF; hiệu chỉnh; xác nhận | Nghiên cứu sinh | Bản ghi đã hiệu chỉnh + log thay đổi |
| 3. Khóa bản ghi | Đóng dấu thời gian; bản ghi không thể sửa đổi nếu không tạo phiên bản mới | Hệ thống | Bản ghi khóa với hash + timestamp |

**Vết kiểm toán:** Mỗi bản ghi khóa lưu (i) bản nháp gốc, (ii) bản sau hiệu chỉnh, (iii) diff giữa hai bản, (iv) ID người rà soát, (v) timestamp ISO 8601.

---

## S-MAIDA.4 Đánh giá chất lượng trên tập gold-standard

### Thiết kế kiểm chứng

- **Cỡ tập gold-standard:** `[TO FILL: ví dụ 30 nghiên cứu chọn ngẫu nhiên từ corpus k=238]`
- **Chiến lược chọn mẫu:** `[TO FILL: ví dụ stratified random theo ICRV regime + năm công bố]`
- **Người trích xuất thủ công tham chiếu:** `[TO FILL: ai (vai trò), có độc lập với người vận hành LLM không]`
- **Đại lượng được đánh giá:** $N$, $r$ (hoặc $\beta$/$t$/$F$ trước quy đổi), $df$, năm dữ liệu trung vị, quốc gia, loại đo DOI, loại đo hiệu quả

### Chỉ số đánh giá

| Đại lượng | Loại | Tiêu chí đồng nhất | Kết quả (LLM nháp vs thủ công) |
|---|---|---|---|
| Cỡ mẫu $N$ | Số nguyên | Bằng nhau tuyệt đối | `[TO FILL: % đồng nhất, ví dụ 28/30 = 93,3%]` |
| Hệ số $r$ (hoặc tiền chuyển đổi) | Số thực | $\|\Delta\| \leq 0,005$ | `[TO FILL]` |
| Bậc tự do $df$ | Số nguyên | Bằng nhau tuyệt đối | `[TO FILL]` |
| Năm dữ liệu trung vị | Số nguyên | Bằng nhau tuyệt đối | `[TO FILL]` |
| Quốc gia (ISO-3) | Phân loại | Cohen's $\kappa$ | `[TO FILL: $\kappa$ = ?]` |
| Loại đo DOI (FSTS/Entropy/...) | Phân loại 4 nhóm | Cohen's $\kappa$ | `[TO FILL: $\kappa$ = ?]` |
| Loại đo hiệu quả (ACC/MKT/LAB/MIX) | Phân loại 4 nhóm | Cohen's $\kappa$ | `[TO FILL: $\kappa$ = ?]` |

**Diễn giải tổng thể:** `[TO FILL: 2-3 câu đánh giá độ tin cậy bản nháp LLM; trường hợp đại lượng nào LLM yếu nhất; lý do tại sao HITL là bắt buộc]`

### Ngưỡng chấp nhận

Theo tiền đăng ký OSF: tập dữ liệu trích xuất chỉ được sử dụng cho phân tích chính nếu (i) Cohen's $\kappa \geq 0,70$ cho mọi đại lượng phân loại, (ii) phần trăm đồng nhất số $\geq 90\%$ cho mọi đại lượng số trong khoảng dung sai. Nếu một đại lượng dưới ngưỡng, đại lượng đó bắt buộc trích xuất hoàn toàn thủ công cho toàn corpus.

**Kết quả ngưỡng:** `[TO FILL: đại lượng nào đạt / không đạt ngưỡng; biện pháp khắc phục đã áp dụng]`

---

## S-MAIDA.5 Phân tích lỗi theo loại đại lượng

| Loại lỗi | Tần suất | Ví dụ | Cơ chế khắc phục |
|---|---|---|---|
| Nhầm $N$ tổng vs $N$ nhóm | `[TO FILL]` | LLM lấy $N$ của subgroup khi paper báo cáo cả $N$ tổng và $N$ subgroup | Rà soát thủ công bắt buộc |
| Sai dấu $r$ | `[TO FILL]` | LLM trích xuất giá trị tuyệt đối từ bảng tương quan | Đối chiếu chiều hướng với mô tả trong text |
| Bỏ sót $df$ | `[TO FILL]` | Paper báo cáo $t$ không kèm $df$ rõ; LLM bỏ trống | Suy ra $df = N - k - 1$ với $k$ là số biến |
| Nhầm loại đo DOI | `[TO FILL]` | "Export intensity" được mã hóa FSTS thay vì EXP | Codebook chi tiết + double-entry |
| Nhầm năm dữ liệu | `[TO FILL]` | LLM lấy năm công bố thay vì năm trung vị dữ liệu | Đối chiếu Methods section bắt buộc |

---

## S-MAIDA.6 Hạn chế của quy trình

1. **Tính không tất định của LLM:** Cùng prompt + cùng PDF có thể cho bản nháp khác nhau giữa các lần chạy. Tính tái lập của nghiên cứu được bảo đảm qua **tập dữ liệu đã khóa**, không qua việc chạy lại bước nháp.
2. **Phụ thuộc chất lượng PDF nguồn:** PDF scan kém chất lượng (OCR sai, bảng phức tạp) làm tăng tỷ lệ bản nháp cần hiệu chỉnh sâu.
3. **Giới hạn cửa sổ ngữ cảnh:** Với nghiên cứu dài (> 50 trang), prompt cần chia chunk, có nguy cơ bỏ sót thông tin giữa các chunk.
4. **Bias của LLM:** LLM được huấn luyện trên corpus học thuật có thể có thiên kiến với các nghiên cứu tiếng Anh / publication bias cùng chiều với corpus.

Mọi hạn chế trên đã được công bố trong tiền đăng ký OSF (z37kn) và được nhắc lại trong phần Hạn chế của bài báo P6.

---

## S-MAIDA.7 Mở dữ liệu và mã

- **Bộ dữ liệu trích xuất đã khóa:** `https://osf.io/z37kn` (`p6_study_database.csv`, 238 nghiên cứu / 288 cỡ hiệu ứng)
- **Codebook chi tiết:** `[TO FILL: link OSF tới codebook file]`
- **Log vết kiểm toán (rà soát + hiệu chỉnh):** `[TO FILL: có công bố hay không; nếu có, link]`
- **Prompt template + cấu hình LLM:** mục S-MAIDA.1 và S-MAIDA.2 của tài liệu này
- **Tập gold-standard tham chiếu:** `[TO FILL: nội bộ hay công bố; nếu công bố, link OSF]`

---

## Checklist hoàn thiện trước khi nộp định bản

- [ ] S-MAIDA.1 — đã điền tên mô hình + phiên bản + tham số
- [ ] S-MAIDA.2 — đã dán prompt template
- [ ] S-MAIDA.4 — đã hoàn thành đánh giá gold-standard với mọi $\kappa$ và % đồng nhất
- [ ] S-MAIDA.4 — đã đạt ngưỡng tiền đăng ký HOẶC ghi rõ biện pháp khắc phục
- [ ] S-MAIDA.5 — đã phân tích lỗi với tần suất thực tế
- [ ] S-MAIDA.7 — đã upload codebook + (nếu được) log vết kiểm toán + gold-standard lên OSF
- [ ] Đã xóa mọi nhãn `[TO FILL]` còn lại
