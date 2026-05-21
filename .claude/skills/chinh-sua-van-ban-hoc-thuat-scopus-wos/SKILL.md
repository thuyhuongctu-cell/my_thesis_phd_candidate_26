---
name: chinh-sua-van-ban-hoc-thuat-scopus-wos
description: >
  Chỉnh sửa và chuẩn hóa bản thảo học thuật cho các tạp chí Scopus và Web of Science (WoS). 
  Sử dụng kỹ năng này khi cần xóa bỏ các biểu tượng không chuẩn (§, ¶, mũi tên, v.v.), 
  thay thế ký hiệu bằng diễn đạt chữ, chuẩn hóa ký tự đặc biệt, định dạng văn bản học thuật, 
  chuẩn bị bản thảo để nộp tạp chí quốc tế, kiểm tra định dạng ký tự, hoặc đảm bảo tuân thủ 
  các tiêu chuẩn xuất bản học thuật. Áp dụng cho các bản thảo nghiên cứu, bài báo khoa học, 
  luận văn, hoặc bất kỳ văn bản học thuật nào cần đạt tiêu chuẩn Scopus/WoS.
---

# Chỉnh Sửa Văn Bản Học Thuật Scopus/WoS

## Tổng Quan

Các tạp chí Scopus và Web of Science yêu cầu định dạng văn bản nghiêm ngặt. Các biểu tượng không chuẩn, ký tự đặc biệt sai, hoặc ký hiệu không phù hợp có thể dẫn đến từ chối bản thảo hoặc làm chậm quá trình biên tập. Kỹ năng này giúp chuẩn hóa văn bản học thuật theo các tiêu chuẩn quốc tế, đảm bảo bản thảo sẵn sàng nộp cho các tạp chí uy tín.

## Nguyên Tắc Chuẩn Hóa

### 1. Xóa Bỏ Biểu Tượng Không Chuẩn

Các biểu tượng sau thường xuất hiện trong bản thảo tiếng Việt nhưng không phù hợp với tiêu chuẩn Scopus/WoS:

- **§ (section sign)**: Chỉ dùng trong trường hợp đặc biệt (ví dụ: ký hiệu tác giả trong một số tạp chí). Thay bằng "Section" hoặc "Phần".
- **¶ (pilcrow)**: Không dùng trong văn bản chính. Nếu cần chỉ đoạn văn, viết rõ "đoạn" hoặc "paragraph".
- **→, ←, ↑, ↓ (mũi tên)**: Thay bằng diễn đạt chữ: "dẫn đến", "chuyển sang", "tăng", "giảm", "implies", "leads to", "increases", "decreases".
- **≠, ≈, ≤, ≥**: Giữ lại trong công thức toán học, nhưng trong văn bản chính thay bằng "không bằng", "xấp xỉ", "nhỏ hơn hoặc bằng", "lớn hơn hoặc bằng" (hoặc "not equal to", "approximately", "less than or equal to", "greater than or equal to").
- **∞, ∑, ∏, ∫**: Giữ trong công thức toán, nhưng trong văn bản thay bằng "vô cực", "tổng", "tích", "tích phân" ("infinity", "sum", "product", "integral").
- **★, ☆, •, ◦, ■, □**: Không dùng làm dấu đầu dòng. Dùng số thứ tự (1, 2, 3) hoặc chữ cái (a, b, c).

**Lý do**: Các tạp chí quốc tế ưu tiên văn bản rõ ràng, dễ đọc, và tương thích với hệ thống biên tập điện tử. Biểu tượng không chuẩn có thể gây lỗi khi chuyển đổi file hoặc làm khó hiểu cho người đọc quốc tế.

### 2. Chuẩn Hóa Ký Tự Đặc Biệt

**Ký tự toán học và khoa học**: Dùng Unicode chuẩn hoặc LaTeX/MathType cho công thức phức tạp.
- Sử dụng font Times New Roman hoặc Arial Unicode cho ký tự đặc biệt.
- Ký hiệu độ: Dùng ° (U+00B7) chứ không phải chữ "o" hoặc số "0" viết trên.
- Ký hiệu nhân: Dùng × (U+00D7) chứ không phải chữ "x".
- Ký hiệu micro: Dùng µ (U+00B5) chứ không phải chữ "u".

**Ký tự đặc biệt cho tác giả**: Các tạp chí như Science, Nature, và Wiley có thứ tự chuẩn:
- Tác giả liên hệ: * (asterisk)
- Các ký hiệu khác theo thứ tự: †, ‡, §, ¶, #, **, ††, ‡‡, §§

**Lý do**: Ký tự không chuẩn có thể hiển thị sai hoặc mất đi khi xuất bản, gây hiểu nhầm về kết quả nghiên cứu.

### 3. Thay Thế Ký Hiệu Bằng Diễn Đạt Chữ

Khi ký hiệu không cần thiết hoặc gây khó hiểu, ưu tiên diễn đạt bằng chữ:

**Ví dụ thay thế**:
- "A → B" → "A dẫn đến B" hoặc "A leads to B"
- "X ≈ Y" → "X xấp xỉ bằng Y" hoặc "X is approximately equal to Y"
- "Nhiệt độ ↑" → "Nhiệt độ tăng" hoặc "Temperature increases"
- "§3.2" → "Section 3.2" hoặc "Phần 3.2"
- "p < 0.05 (*)" → "p < 0.05 (có ý nghĩa thống kê)" hoặc "p < 0.05 (statistically significant)"

**Nguyên tắc**: Trong văn bản chính, rõ ràng quan trọng hơn ngắn gọn. Trong bảng biểu và công thức, ký hiệu được phép nếu giải thích rõ trong chú thích.

## Quy Trình Chỉnh Sửa

### Bước 1: Quét Toàn Bộ Văn Bản

Đọc kỹ toàn bộ bản thảo và đánh dấu:
- Tất cả các biểu tượng không chuẩn (§, ¶, mũi tên, dấu đầu dòng đặc biệt)
- Ký tự đặc biệt có thể gây nhầm lẫn (độ, micro, nhân)
- Các đoạn dùng ký hiệu thay vì chữ

### Bước 2: Phân Loại và Xử Lý

**Loại 1 - Xóa bỏ hoàn toàn**: Các ký hiệu trang trí, dấu đầu dòng không chuẩn
- Thay bằng số thứ tự hoặc bullet point chuẩn

**Loại 2 - Thay thế bằng chữ**: Mũi tên, ký hiệu quan hệ trong văn bản chính
- Viết rõ ý nghĩa bằng từ ngữ chính xác

**Loại 3 - Chuẩn hóa**: Ký tự toán học và khoa học cần thiết
- Đảm bảo dùng Unicode chuẩn hoặc công cụ soạn thảo công thức (MathType, Equation Editor)

### Bước 3: Kiểm Tra Nhất Quán

Đảm bảo:
- Cùng một khái niệm được diễn đạt nhất quán trong toàn bộ văn bản
- Ký hiệu toán học tuân theo quy ước của lĩnh vực (italic cho biến, roman cho hằng số)
- Đơn vị đo lường có ký hiệu chuẩn và khoảng cách đúng (ví dụ: "25 °C" chứ không phải "25°C" hoặc "25 oC")

### Bước 4: Xác Minh Font và Mã Hóa

- Font chính: Times New Roman 12pt (khuyến nghị của hầu hết tạp chí)
- Ký tự đặc biệt: Times New Roman hoặc Arial Unicode
- Công thức: MathType hoặc Word Equation Editor
- Tránh dùng Symbol font trừ khi cần thiết

## Ví Dụ Cụ Thể

### Ví Dụ 1: Văn Bản Mô Tả Quy Trình

**Trước**:
```
Quy trình gồm 3 bước: ① Chuẩn bị mẫu → ② Phân tích → ③ Kết luận.
Nhiệt độ ↑ từ 20°C đến 100°C (§2.3).
```

**Sau**:
```
Quy trình gồm 3 bước: (1) Chuẩn bị mẫu, (2) Phân tích, và (3) Kết luận.
Nhiệt độ tăng từ 20 °C đến 100 °C (xem Section 2.3).
```

### Ví Dụ 2: Bảng Kết Quả

**Trước**:
```
Nhóm A: 45.3 ± 2.1 (*)
Nhóm B: 38.7 ± 1.9 (ns)
(*) p < 0.05; (ns) không có ý nghĩa
```

**Sau**:
```
Nhóm A: 45.3 ± 2.1*
Nhóm B: 38.7 ± 1.9
*p < 0.05 (statistically significant)
```

### Ví Dụ 3: Diễn Đạt Quan Hệ

**Trước**:
```
Tăng nồng độ X → tăng hiệu suất (Y ≈ 2X)
```

**Sau**:
```
Tăng nồng độ X dẫn đến tăng hiệu suất, với mối quan hệ xấp xỉ Y ≈ 2X.
```

## Lưu Ý Đặc Biệt

### Trường Hợp Giữ Lại Ký Hiệu

Có một số trường hợp ký hiệu được phép và nên giữ lại:

1. **Công thức toán học**: Giữ nguyên ký hiệu chuẩn trong công thức
2. **Ký hiệu hóa học**: Giữ theo quy ước IUPAC (ví dụ: H₂O, CO₂)
3. **Ký hiệu thống kê**: p, α, β, R², F-value (theo quy ước lĩnh vực)
4. **Ký hiệu đơn vị SI**: m, kg, s, K, mol, cd, A
5. **Ký hiệu tác giả**: Theo yêu cầu của tạp chí cụ thể

### Kiểm Tra Cuối Cùng

Trước khi nộp bản thảo:
- Mở file trong PDF và kiểm tra tất cả ký tự hiển thị đúng
- Tìm kiếm các ký tự đặc biệt bằng chức năng Find trong Word (tìm §, ¶, →, v.v.)
- Đọc lại phần Methods và Results - nơi thường có nhiều ký hiệu nhất
- Kiểm tra figure legends và table footnotes - nơi dễ bỏ sót ký hiệu

### Công Cụ Hỗ Trợ

- **Character Map (Windows)**: Tìm và chèn ký tự Unicode chuẩn
- **Insert Symbol (Word/Google Docs)**: Chọn ký tự từ bộ ký tự chuẩn
- **Find & Replace**: Tìm và thay thế hàng loạt ký hiệu không chuẩn
- **MathType/Equation Editor**: Soạn thảo công thức toán học chuyên nghiệp

## Tiêu Chuẩn Theo Lĩnh Vực

### Khoa Học Tự Nhiên và Kỹ Thuật
- Ưu tiên công thức toán học rõ ràng với MathType
- Ký hiệu đơn vị SI nghiêm ngặt
- Italic cho biến số, roman cho hằng số và đơn vị

### Khoa Học Xã Hội
- Ít ký hiệu toán học hơn, nhiều diễn đạt bằng chữ
- Thống kê dùng ký hiệu chuẩn APA (p, t, F, χ²)

### Y Học và Sinh Học
- Ký hiệu gene và protein theo quy ước (italic cho gene, roman cho protein)
- Đơn vị đo lường y học chuẩn (mg/dL, mmHg, IU/L)

## Tóm Tắt Nhanh

**Khi gặp ký hiệu không chuẩn, tự hỏi**:
1. Ký hiệu này có cần thiết không?
2. Nếu cần, có phải ký hiệu chuẩn của lĩnh vực không?
3. Nếu không cần thiết, có thể diễn đạt bằng chữ rõ hơn không?
4. Nếu giữ lại, ký hiệu có hiển thị đúng trong mọi định dạng (Word, PDF) không?

**Nguyên tắc vàng**: Trong văn bản học thuật quốc tế, rõ ràng và chuẩn mực quan trọng hơn sáng tạo và ngắn gọn. Khi nghi ngờ, chọn diễn đạt bằng chữ.