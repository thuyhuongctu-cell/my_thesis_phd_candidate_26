# Kế hoạch rút gọn P3 → ≤ 8.500 từ cho JED (Emerald) — CHỜ DUYỆT

Hiện tại: **20.975 từ** (kể cả mọi thứ). Mục tiêu JED: **≤ 8.500 từ** (gồm abstract, references, toàn bộ chữ trong bảng, hình, phụ lục).
Nguyên tắc: **không thay đổi bất kỳ số liệu/kết quả nào**; chỉ cô đọng diễn đạt, gộp ý trùng, và **chuyển nội dung robustness/chi tiết sang Supplementary (host trên Emerald Insight)**.
Đầu ra: tạo **bản song song** `01_manuscript_blinded_8500.md/.docx` + `Supplementary_material_robustness.docx`. Bản đầy đủ giữ nguyên.

| Mục | Hiện tại | → Mục tiêu | Hành động cụ thể |
|---|---:|---:|---|
| Abstract | 221 | **221** | Giữ nguyên (đã đạt ≤250) |
| Highlights | 334 | **0** | **Bỏ** (JED không yêu cầu; nội dung đã nằm trong abstract/kết quả) |
| §1.1 Bối cảnh | 716 | 300 | Gộp đoạn bối cảnh WTO/CPTPP/COVID; bỏ lặp số liệu vĩ mô đã có ở §3 |
| §1.2 Khoảng trống | 461 | 180 | Cô đọng còn 1 đoạn nêu 3 gap |
| §1.3 Đóng góp | 416 | 170 | Liệt kê 3 đóng góp ngắn gọn |
| §1.4 Roadmap | 45 | 0 | **Bỏ** (không bắt buộc) |
| §2.1 I–P | 742 | 320 | Giữ lập luận H1; nén tổng quan lý thuyết |
| §2.2 Năng lực CN | 419 | 220 | Giữ H2; nén |
| §2.3 Hiện diện web | 729 | 250 | Nén; giữ H4 (proxy obsolescence) |
| §2.4 Giá trị số theo giai đoạn | 1056 | 280 | **Cắt mạnh**; chuyển phần mở rộng lý thuyết số sang Supplementary |
| §3.1 Dữ liệu | 116 | 100 | Giữ |
| §3.2 Biến số | 1262 | 350 | **Chuyển định nghĩa biến chi tiết → Bảng I (file bảng riêng)**; chỉ giữ mô tả ngắn |
| §3.3 Chuỗi mô hình | 517 | 280 | Nén; phương trình giữ |
| §3.4 Nội sinh/nhận dạng | 324 | 220 | Nén |
| §3.5 Tái lập | 147 | 80 | Nén |
| §4.1 Theo đợt | 1216 | 600 | Giữ Bảng kết quả chính; chuyển bảng phụ → Supplementary; nén tường thuật |
| §4.2 Gộp | 950 | 500 | Tương tự |
| §4.3 Diễn giải giả thuyết | 796 | 350 | Nén |
| §4.4 Tham gia × cường độ | 233 | 200 | Giữ (phát hiện cốt lõi) |
| **§4.5 Robustness** | **4735** | **180** | **CHUYỂN TOÀN BỘ sang Supplementary**; giữ 1 đoạn tóm tắt + dẫn chiếu file |
| §5.1–5.5 Thảo luận | 2818 | 1300 | Nén từng tiểu mục; gộp hàm ý quản trị + chính sách |
| §6 Hạn chế | 639 | 300 | Nén |
| §7 Kết luận | 285 | 220 | Nén nhẹ |
| Declarations (CoI, Funding, Data, Ethics, AI, Ack) | 300 | 300 | Giữ (bắt buộc) |
| Supplementary materials (ghi chú) | 72 | 60 | Cập nhật danh mục file supplementary |
| **References** | 1517 | ~1350 | Giữ; cân nhắc bỏ 4–6 trích dẫn ngoại vi (kèm gỡ nhắc trong text) để vừa trần |
| **TỔNG** | **20.975** | **≈ 8.430** | ✅ Đạt ≤ 8.500 |

## Bảng & hình (theo yêu cầu JED)
- **Tách bảng ra file riêng**, đánh số **La Mã**: Bảng I (định nghĩa biến), Bảng II (thống kê mô tả), Bảng III (hệ số trọng tâm theo đợt + gộp), Bảng IV (điểm ngưỡng Lind–Mehlum). Trong text chèn `[Insert Table I about here]`.
- Các bảng robustness (panel A–G, Heckman/control-function, Paternoster z-tests) → **Supplementary**.
- Hình: giữ Hình 1 (mô hình), Hình 2 (inverted-U tổng hợp), Hình 3 (tác động biên điều tiết) trong bài; Hình 2a–2d theo đợt → Supplementary. Nộp .tif/.eps/.jpeg độ phân giải cao.

## Sang Supplementary (Insight): `Supplementary_material_robustness.docx`
- Toàn bộ §4.5 (panel robustness, alternative specifications, sub-samples).
- Bảng robustness chi tiết + Heckman/control-function + Paternoster.
- Phần mở rộng lý thuyết số của §2.4.
- Hình theo đợt 2a–2d.

## Cam kết
- **Không** đổi bất kỳ hệ số, p-value, N, điểm ngưỡng nào.
- Mọi nội dung cắt khỏi bài chính đều **được bảo toàn trong Supplementary** (không mất dữ liệu).
- Bản đầy đủ `01_manuscript_blinded.md` giữ nguyên để đối chiếu.

> **Cần bạn duyệt**: (a) đồng ý mức cắt từng mục như trên? (b) đồng ý chuyển §4.5 + bảng robustness + §2.4 mở rộng sang Supplementary? (c) có ref nào bắt buộc phải giữ dù cắt phần khác không?
