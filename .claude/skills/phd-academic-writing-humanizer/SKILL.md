---
name: phd-academic-writing-humanizer
description: >
  Chỉnh sửa văn bản học thuật để loại bỏ dấu hiệu AI, đặc biệt là dấu gạch nối (em dash) quá dài
  và các mẫu văn phong công thức. Sử dụng khi viết hoặc chỉnh sửa luận án tiến sĩ, bài báo học thuật,
  đặc biệt trong lĩnh vực kinh doanh quốc tế, internationalization, firm performance, hoặc bất kỳ văn bản
  nghiên cứu nào cần tránh phát hiện AI. Hỗ trợ cho các tác giả muốn văn bản có giọng điệu tự nhiên hơn,
  giảm thiểu các dấu hiệu như em dash (—), câu văn công thức, và các mẫu từ vựng điển hình của LLM.
  Dùng cho dissertation, journal paper, conference paper, thesis, và mọi văn bản học thuật cần chất lượng cao.
---

# PhD Academic Writing Humanizer

## Tổng quan

Công cụ này giúp chỉnh sửa văn bản học thuật để loại bỏ các dấu hiệu điển hình của AI-generated text, đặc biệt trong bối cảnh viết luận án tiến sĩ về kinh doanh quốc tế. Các hệ thống phát hiện AI (GPTZero, Originality.ai, Copyleaks) thường tìm kiếm các mẫu như: em dash (—) quá nhiều, câu văn công thức, thiếu biến đổi về cú pháp, và từ vựng lặp lại theo pattern.

## Khi nào cần sử dụng

Kích hoạt khi người dùng:
- Đang viết hoặc chỉnh sửa luận án tiến sĩ, bài báo học thuật
- Đề cập đến "dấu gạch nối", "em dash", "hyphen", "—"
- Muốn "humanize", "tự nhiên hóa", hoặc "giảm dấu hiệu AI"
- Làm việc với văn bản về internationalization, firm performance, international business
- Cần vượt qua AI detector hoặc tránh bị gắn cờ là AI-generated
- Đang chuẩn bị nộp dissertation, journal submission, hoặc conference paper

## Quy trình chỉnh sửa

### Bước 1: Phân tích văn bản gốc

Trước khi chỉnh sửa, xác định:
- Mật độ em dash (—) trong văn bản (nếu >3 lần/đoạn = dấu hiệu AI mạnh)
- Các cụm từ công thức: "it is important to note that", "furthermore", "moreover", "in conclusion"
- Độ đồng đều về cấu trúc câu (AI thường tạo câu có độ dài và cấu trúc tương đồng)
- Các parallelism quá đối xứng hoặc list items quá cân đối

### Bước 2: Xóa hoặc thay thế em dash

Em dash (—) là một trong những dấu hiệu rõ nhất của AI writing. Chiến lược:

**Thay thế bằng dấu câu khác:**
- Em dash → dấu phẩy: "The findings—which were significant—suggest..." → "The findings, which were significant, suggest..."
- Em dash → dấu chấm: "Firms expanded rapidly—their performance improved" → "Firms expanded rapidly. Their performance improved."
- Em dash → dấu hai chấm: "One factor matters most—market entry timing" → "One factor matters most: market entry timing."
- Em dash → dấu ngoặc đơn: "The study—conducted in 2024—shows..." → "The study (conducted in 2024) shows..."

**Viết lại câu hoàn toàn:**
- Tách thành hai câu độc lập
- Dùng liên từ phụ thuộc (because, although, while)
- Nhúng thông tin vào cấu trúc câu chính

### Bước 3: Phá vỡ các pattern công thức

**Loại bỏ transition words thừa:**
- "Furthermore" → bỏ hoặc thay bằng "Also", hoặc không dùng gì
- "Moreover" → bỏ hoặc viết lại câu để ý tưởng tự nhiên nối tiếp
- "In addition" → thay bằng "And" hoặc bỏ
- "It is important to note that" → bỏ hoàn toàn, đi thẳng vào nội dung

**Thay đổi cấu trúc câu:**
- Trộn câu ngắn và câu dài (AI thường tạo câu có độ dài đồng đều)
- Dùng câu bị động thỉnh thoảng (không quá nhiều, nhưng một vài câu bị động tạo sự tự nhiên)
- Bắt đầu câu bằng nhiều cách khác nhau (không lặp lại pattern "The X shows that...")

**Tăng biến đổi từ vựng:**
- Thay các từ quá formal hoặc quá "perfect": "utilize" → "use", "facilitate" → "help", "demonstrate" → "show"
- Dùng từ đồng nghĩa nhưng không theo pattern (AI thường chọn từ formal nhất)

### Bước 4: Tăng tính tự nhiên của giọng văn

**Thêm biến đổi về nhịp điệu:**
- Chèn câu ngắn giữa các câu dài: "This matters. Firms that ignore this risk failure."
- Dùng câu hỏi tu từ (rhetorical questions) thỉnh thoảng
- Thỉnh thoảng bắt đầu câu bằng "But" hoặc "And" (trong academic writing hiện đại, điều này được chấp nhận)

**Giữ tính học thuật nhưng tự nhiên hơn:**
- Không cần loại bỏ tất cả formal language, nhưng tránh quá "polished"
- Giữ các thuật ngữ chuyên ngành (internationalization, firm performance) vì đây là văn bản học thuật
- Đảm bảo luận điểm rõ ràng, không bị "smoothed over" bởi quá nhiều hedging language

### Bước 5: Kiểm tra lại

Sau khi chỉnh sửa:
- Đếm lại em dash: nên còn 0-1 lần trong toàn bộ văn bản, hoặc tối đa 1 lần mỗi 2-3 đoạn
- Đọc to văn bản: nếu nghe như "robot", cần chỉnh sửa thêm
- Kiểm tra độ biến đổi về độ dài câu: nên có sự khác biệt rõ rệt
- Đảm bảo không mất ý nghĩa học thuật hoặc độ chính xác

## Ví dụ cụ thể

### Ví dụ 1: Xóa em dash

**Trước:**
"The internationalization process—a complex phenomenon involving multiple stages—significantly impacts firm performance. Previous studies—particularly those in emerging markets—have shown mixed results."

**Sau:**
"The internationalization process, a complex phenomenon involving multiple stages, significantly impacts firm performance. Previous studies have shown mixed results, particularly those in emerging markets."

**Giải thích:** Thay cả hai em dash bằng dấu phẩy, và viết lại câu thứ hai để tránh pattern lặp lại.

### Ví dụ 2: Phá vỡ pattern công thức

**Trước:**
"Furthermore, the results demonstrate that internationalization positively affects performance. Moreover, this relationship is moderated by firm size. In addition, institutional factors play a crucial role. It is important to note that these findings have significant implications."

**Sau:**
"The results show that internationalization positively affects performance. Firm size moderates this relationship. Institutional factors also play a crucial role, and these findings carry significant implications for practice."

**Giải thích:** Loại bỏ tất cả transition words thừa, viết gọn hơn, và kết hợp câu cuối để tạo flow tự nhiên.

### Ví dụ 3: Tăng biến đổi câu

**Trước:**
"This study examines the relationship between internationalization and firm performance. This research investigates how this relationship varies across contexts. This analysis explores the moderating factors that influence this effect."

**Sau:**
"This study examines the relationship between internationalization and firm performance. How does this relationship vary across contexts? We investigate moderating factors that influence this effect."

**Giải thích:** Phá vỡ pattern "This [noun] [verb]" bằng cách dùng câu hỏi và đổi chủ ngữ.

## Lưu ý quan trọng

### Không làm mất tính học thuật

Việc "humanize" không có nghĩa là làm văn bản kém chính xác hoặc mất tính chuyên nghiệp. Mục tiêu là:
- Giữ nguyên độ chính xác về mặt học thuật
- Giữ nguyên các thuật ngữ chuyên ngành
- Giữ nguyên cấu trúc luận điểm và bằng chứng
- Chỉ thay đổi cách diễn đạt để tự nhiên hơn

### Hiểu về AI detection

Các công cụ phát hiện AI (2026) tìm kiếm:
- **Perplexity thấp:** văn bản quá "predictable", không có surprise
- **Burstiness thấp:** độ biến đổi về độ dài câu và cấu trúc thấp
- **Pattern markers:** em dash, transition words, parallel structures quá đối xứng
- **Hyphen usage:** các pattern gạch nối không tự nhiên

Bằng cách tăng perplexity (thêm biến đổi) và burstiness (thay đổi nhịp điệu), văn bản sẽ "human" hơn.

### Đối với non-native English writers

Nghiên cứu cho thấy AI detectors có bias cao với non-native writers (tỷ lệ false positive lên đến 61.3% cho tác giả người Trung Quốc). Lý do: non-native writers thường viết với "low perplexity" (câu đơn giản, ít biến đổi). Để giảm thiểu:
- Cố ý thêm biến đổi về cấu trúc câu
- Dùng một số idioms hoặc colloquial expressions (phù hợp với academic writing)
- Tránh viết quá "perfect" - một vài lỗi nhỏ về style thực ra tạo tính tự nhiên

## Quy trình làm việc với người dùng

1. **Nhận văn bản:** Người dùng paste đoạn văn cần chỉnh sửa
2. **Phân tích nhanh:** Chỉ ra các dấu hiệu AI chính (em dash count, pattern words)
3. **Chỉnh sửa:** Áp dụng các kỹ thuật trên
4. **Trả về kết quả:** Văn bản đã chỉnh sửa + giải thích ngắn gọn về những gì đã thay đổi
5. **Tùy chọn:** Nếu người dùng muốn, cung cấp thêm gợi ý cho các đoạn khác

## Checklist cuối cùng

Trước khi hoàn tất:
- [ ] Em dash count: ≤1 mỗi 2-3 đoạn
- [ ] Không còn "Furthermore", "Moreover", "In addition" liên tiếp
- [ ] Độ dài câu biến đổi (có câu ngắn <10 từ, có câu dài >25 từ)
- [ ] Cấu trúc câu đa dạng (không lặp lại pattern)
- [ ] Giữ nguyên ý nghĩa học thuật và độ chính xác
- [ ] Văn bản đọc tự nhiên khi đọc to
- [ ] Các thuật ngữ chuyên ngành được giữ nguyên