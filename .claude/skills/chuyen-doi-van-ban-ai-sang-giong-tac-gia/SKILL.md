---
name: chuyen-doi-van-ban-ai-sang-giong-tac-gia
description: >
  Điều chỉnh văn bản có dấu hiệu AI viết thành giọng văn tự nhiên của tác giả học thuật. Sử dụng khi cần humanize văn bản AI, chuyển đổi văn bản AI-generated sang phong cách cá nhân, điều chỉnh bài viết học thuật, paper, thesis, hoặc bất kỳ văn bản nào cần giọng điệu tự nhiên hơn dựa trên các công trình trước đây của tác giả. Phù hợp cho academic writing, scholarly papers, research articles, và mọi tình huống cần văn phong nhất quán với identity của tác giả.
---

# Chuyển Đổi Văn Bản AI Sang Giọng Tác Giả

## Tổng Quan

Skill này giúp chuyển đổi văn bản có dấu hiệu AI-generated thành văn bản mang giọng văn tự nhiên và nhất quán với phong cách viết của tác giả, đặc biệt trong bối cảnh học thuật. Thay vì chỉ đơn thuần "làm cho văn bản nghe tự nhiên hơn", skill tập trung vào việc phân tích và tái tạo authorial voice dựa trên các công trình trước đây của tác giả.

## Quy Trình Làm Việc

### Calibration cho dự án này (Đỗ Thùy Hương)

Profile giọng tác giả đã được dựng sẵn từ chính công trình của tác giả — dùng
trực tiếp, không cần dựng lại:
- Tài liệu **tiếng Anh** → `references/author-voice-do-thuy-huong.md`
  (từ paper meta-analysis + book chapter UK 2025).
- Tài liệu **tiếng Việt** → `references/author-voice-do-thuy-huong-vi.md`
  (từ tiểu luận tổng quan NCS).

Chọn profile theo ngôn ngữ của văn bản đích; giữ nhất quán trong từng tài liệu.

### Bước 1: Thu Thập Thông Tin Tác Giả

Yêu cầu người dùng cung cấp:
- Các papers/bài viết trước đây của tác giả (ưu tiên 2-3 bài gần nhất)
- Thông tin về tác giả: lĩnh vực nghiên cứu, trường/tổ chức (ví dụ: Do Thuy Huong, CTU scholars)
- Văn bản cần chuyển đổi

Nếu chỉ có tên tác giả và tổ chức, tìm kiếm công trình công bố của họ để xây dựng profile phong cách viết.

### Bước 2: Phân Tích Authorial Voice

Xác định các đặc điểm authorial voice từ văn bản tham khảo:

**Linguistic Markers:**
- Sử dụng đại từ (tôi/chúng tôi, we/I trong tiếng Anh)
- Mức độ hedging (có thể, có lẽ, might, may)
- Stance markers (rõ ràng, tất nhiên, clearly, importantly)
- Metadiscourse (như đã đề cập, as mentioned, in this section)

**Cấu Trúc Câu:**
- Độ dài câu trung bình
- Tỷ lệ câu đơn/câu phức
- Sử dụng câu bị động vs chủ động
- Mẫu câu đặc trưng

**Phong Cách Trích Dẫn:**
- Integral citations (Tác giả A (năm) cho rằng...) vs non-integral (... (Tác giả A, năm))
- Mức độ đánh giá nguồn trích dẫn
- Cách xây dựng literature review

**Tone và Register:**
- Mức độ formality (formal, semi-formal)
- Cảm xúc và engagement với người đọc
- Mức độ assertiveness trong argument

### Bước 3: Nhận Diện Dấu Hiệu AI

Văn bản AI thường có:
- Câu có độ dài đồng đều bất thường
- Cấu trúc lặp lại (Firstly... Secondly... Finally...)
- Từ vựng generic và neutral quá mức
- Thiếu variation trong sentence starters
- Overuse của transition words
- Tone quá formal hoặc robotic
- Thiếu personal perspective và critical voice

### Bước 4: Chuyển Đổi Văn Bản

Áp dụng các nguyên tắc:

**Vary Sentence Structure:**
- Mix câu ngắn với câu dài theo pattern của tác giả
- Sử dụng các sentence starters đa dạng
- Thêm subordinate clauses nếu tác giả thường dùng

**Inject Authorial Voice:**
- Thêm stance markers phù hợp với style của tác giả
- Điều chỉnh mức độ hedging cho nhất quán
- Sử dụng metadiscourse theo thói quen của tác giả
- Thêm critical evaluation nếu tác giả có xu hướng đó

**Adjust Vocabulary:**
- Thay generic words bằng field-specific terminology tác giả thường dùng
- Giữ từ vựng academic nhưng không quá formal
- Sử dụng collocations đặc trưng của tác giả

**Maintain Coherence:**
- Giữ ý nghĩa và argument structure gốc
- Đảm bảo logic flow tự nhiên
- Không thay đổi nội dung chuyên môn

### Bước 5: Kiểm Tra và Tinh Chỉnh

Đọc lại và tự hỏi:
- Văn bản có nghe như tác giả viết không?
- Có còn dấu hiệu AI rõ ràng không?
- Tone có nhất quán với papers trước không?
- Authorial presence có rõ ràng không?

## Ví Dụ Cụ Thể

### Văn Bản AI Gốc:

"Climate change presents significant challenges to agricultural productivity. Firstly, rising temperatures affect crop yields. Secondly, changing precipitation patterns impact water availability. Finally, extreme weather events cause substantial damage to farming infrastructure. Therefore, it is important to develop adaptive strategies."

### Sau Khi Phân Tích Tác Giả (giả sử tác giả có phong cách critical, sử dụng hedging, và personal voice):

"Biến đổi khí hậu đang tạo ra những thách thức nghiêm trọng cho năng suất nông nghiệp, mặc dù mức độ tác động có thể khác nhau tùy vùng. Nhiệt độ gia tăng không chỉ ảnh hưởng trực tiếp đến năng suất cây trồng mà còn làm thay đổi cơ bản các mô hình mưa, dẫn đến tình trạng khan hiếm nước ngày càng trầm trọng ở nhiều khu vực. Đáng lo ngại hơn, các hiện tượng thời tiết cực đoan—từ lũ lụt đến hạn hán—đã gây thiệt hại đáng kể cho cơ sở hạ tầng nông nghiệp. Trong bối cảnh đó, việc phát triển các chiến lược thích ứng không chỉ quan trọng mà còn cấp bách."

**Những thay đổi chính:**
- Loại bỏ "Firstly, Secondly, Finally" structure
- Thêm hedging ("có thể khác nhau", "mặc dù")
- Thêm critical voice ("Đáng lo ngại hơn", "không chỉ... mà còn")
- Vary sentence length và structure
- Thêm emphasis ("không chỉ quan trọng mà còn cấp bách")

## Nguyên Tắc Quan Trọng

### Tôn Trọng Authorial Identity

Authorial voice không chỉ là style—nó phản ánh intellectual identity, research perspective, và cultural background của tác giả. Việc chuyển đổi phải giữ được authenticity này.

### Context-Dependent Adjustment

Cùng một tác giả có thể có voice khác nhau trong:
- Research articles vs conference papers
- Introduction vs Discussion sections
- Solo-authored vs co-authored papers

Điều chỉnh phù hợp với context cụ thể.

### Cân Bằng Giữa Naturalness và Academic Rigor

Văn bản sau khi chuyển đổi phải:
- Nghe tự nhiên như người viết
- Giữ được academic standards
- Không mất đi credibility vì quá casual
- Không quá formal đến mức robotic

### Đặc Điểm Văn Phong Việt Nam

Khi làm việc với tác giả Việt Nam viết tiếng Việt:
- Chú ý đến mức độ sử dụng từ Hán-Việt vs từ thuần Việt
- Cấu trúc câu tiếng Việt có xu hướng linh hoạt hơn tiếng Anh
- Tone thường formal hơn trong academic writing Việt Nam
- Sử dụng "chúng tôi" vs "tôi" phản ánh cultural norms

## Xử Lý Các Tình Huống Đặc Biệt

### Khi Thiếu Thông Tin Tác Giả

Nếu không có papers trước:
- Hỏi về field, seniority level, preferred style
- Sử dụng discipline conventions làm baseline
- Tạo consistent voice dựa trên thông tin có sẵn
- Giải thích limitations cho người dùng

### Khi Văn Bản Quá Dài

Xử lý từng section:
- Ưu tiên Introduction và Discussion (nơi voice rõ nhất)
- Maintain consistency across sections
- Có thể giữ Methods section formal hơn (discipline convention)

### Khi Tác Giả Có Multiple Voices

Nếu papers tham khảo có styles khác nhau:
- Hỏi người dùng về preferred style
- Xác định voice nào phù hợp với current context
- Document style choices để maintain consistency

## Output Format

Khi hoàn thành, cung cấp:

1. **Văn bản đã chuyển đổi** - ready to use
2. **Summary of changes** - giải thích những điều chỉnh chính
3. **Voice profile** - tóm tắt authorial voice đã áp dụng
4. **Suggestions** - đề xuất cho lần viết sau (nếu có)

Luôn giải thích reasoning đằng sau các thay đổi để người dùng học được cách tự duy trì voice trong tương lai.