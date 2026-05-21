# AI Detection Patterns - Tài liệu tham khảo

## Các dấu hiệu AI phổ biến trong academic writing (2026)

Dựa trên nghiên cứu từ các công cụ phát hiện AI hàng đầu và phân tích từ Wikipedia, Copyleaks, và các nguồn học thuật.

### 1. Em dash (—) overuse

**Tần suất bình thường:** 0-2 lần mỗi 1000 từ trong human writing
**Tần suất AI:** 5-15 lần mỗi 1000 từ

**Tại sao AI dùng nhiều em dash:**
- LLMs học từ văn bản "punched up" (sales writing, marketing copy)
- Em dash tạo cảm giác dramatic và emphasize clauses
- AI thích dùng em dash để nối các ý parallelism

**Cách nhận biết:**
- Em dash xuất hiện ở vị trí có thể thay bằng dấu phẩy hoặc dấu chấm
- Em dash dùng để emphasize thông tin không thực sự quan trọng
- Nhiều em dash trong cùng một đoạn

### 2. Formulaic transition words

**Các từ/cụm từ điển hình:**
- Furthermore (AI dùng 3-4x nhiều hơn human)
- Moreover (đặc biệt khi bắt đầu câu)
- In addition
- It is important to note that
- It is worth mentioning that
- Additionally
- Consequently

**Tại sao đây là dấu hiệu AI:**
- Human writers thường dùng transition ngầm định (implicit) hoặc đơn giản hơn
- AI được train để "connect ideas clearly", nên overuse explicit transitions
- Pattern: mỗi đoạn bắt đầu bằng transition word = dấu hiệu rất mạnh

### 3. Low perplexity (predictability)

**Định nghĩa:** Perplexity đo "surprise" của văn bản. Low perplexity = văn bản predictable.

**Dấu hiệu:**
- Mỗi câu theo cấu trúc tương tự: Subject + Verb + Object
- Từ vựng "safe" và formal: utilize thay vì use, demonstrate thay vì show
- Không có unexpected word choices hoặc creative phrasing

**Cách tăng perplexity:**
- Dùng từ đồng nghĩa ít phổ biến hơn (nhưng vẫn chính xác)
- Thay đổi cấu trúc câu (inverted sentences, fragments)
- Thêm một vài colloquialisms (phù hợp với academic writing)

### 4. Low burstiness (uniform sentence length)

**Định nghĩa:** Burstiness đo sự biến đổi về độ dài và complexity của câu.

**AI pattern:**
- Hầu hết câu dài 15-25 từ
- Ít câu rất ngắn (<10 từ) hoặc rất dài (>30 từ)
- Độ phức tạp của câu đồng đều

**Human pattern:**
- Trộn câu ngắn (5-10 từ) với câu dài (25-35 từ)
- Thỉnh thoảng có sentence fragments cho emphasis
- Complexity thay đổi theo content (giải thích phức tạp = câu dài, conclusion = câu ngắn)

### 5. Parallel structures quá đối xứng

**Ví dụ AI:**
"First, internationalization increases market access. Second, it enhances competitive advantage. Third, it improves financial performance. Fourth, it strengthens organizational learning."

**Ví dụ human:**
"Internationalization increases market access. It also enhances competitive advantage and improves financial performance. Organizational learning strengthens as a result."

**Giải thích:** AI thích tạo lists hoàn hảo với cấu trúc song song. Humans thường break pattern sau 2-3 items.

### 6. Hedging language patterns

**AI overuses:**
- "may potentially"
- "could possibly"
- "might suggest"
- "appears to indicate"

**Human style:** Dùng hedging khi cần, nhưng không stack nhiều hedging words.

### 7. Syllable dispersion issues

**AI pattern:** Syllable distribution quá đều (mỗi từ có 2-3 syllables trung bình)
**Human pattern:** Biến đổi nhiều hơn (từ 1-syllable trộn với từ 4-5 syllables)

## Strategies để tránh detection

### Strategy 1: "Messy it up" slightly

Văn bản quá perfect = suspicious. Thêm một chút "imperfection":
- Một vài câu hơi dài hoặc hơi ngắn bất thường
- Một từ slightly informal (nhưng vẫn acceptable trong academic writing)
- Không sửa 100% các minor style issues

### Strategy 2: Vary sentence openings

**Tránh:** Mỗi câu bắt đầu bằng "The X", "This Y"
**Thay bằng:**
- Prepositional phrases: "In this context, ..."
- Adverbs: "Surprisingly, ..."
- Dependent clauses: "Although previous research suggests X, ..."
- Questions: "How does this affect Y?"

### Strategy 3: Break academic "rules" occasionally

**Acceptable trong modern academic writing:**
- Bắt đầu câu bằng "And" hoặc "But"
- Dùng contractions trong một số contexts (it's, don't)
- Sentence fragments cho emphasis
- First-person ("We argue that...")

### Strategy 4: Add domain-specific nuance

AI thường generic. Thêm chi tiết specific:
- Tên các theories cụ thể
- Tham chiếu đến specific studies với details
- Nuances về methodology hoặc context

## False positives và bias

### Non-native English writers

**Vấn đề:** AI detectors có false positive rate rất cao (61.3%) với non-native writers.

**Lý do:**
- Non-native writers dùng simpler sentence structures
- Từ vựng limited hơn = low perplexity
- Grammar quá correct (vì check carefully) = giống AI

**Giải pháp:**
- Cố ý thêm complexity và variation
- Dùng một vài idioms hoặc less formal words
- Không sợ một vài minor errors (thực ra tạo tính human)

### Discipline-specific writing

Một số lĩnh vực (STEM, business) có writing style naturally "AI-like":
- Formal và structured
- Technical terminology
- Clear và direct

Đây không phải lỗi, nhưng cần aware và compensate bằng cách tăng variation.

## Tools và resources

### AI Detectors phổ biến (2026)

1. **GPTZero** - 8.4% false positive rate, phổ biến trong academia
2. **Originality.ai** - 4.0% false positive rate, dùng nhiều trong publishing
3. **Copyleaks** - Phân tích hyphen usage và syllable dispersion
4. **Turnitin AI Detector** - Integrated với plagiarism checking

### Cách test văn bản của bạn

1. Run qua 2-3 detectors khác nhau
2. Nếu >50% AI probability = cần chỉnh sửa
3. Focus vào sections bị flag nhiều nhất
4. Chỉnh sửa và test lại

### Lưu ý về ethics

Mục tiêu không phải là "cheat" detectors, mà là:
- Cải thiện chất lượng writing (AI-generated text thường không tốt bằng human-edited)
- Tránh false positives (bị cáo buộc sai khi văn bản thực sự do bạn viết)
- Học cách viết tự nhiên và effective hơn

Nếu bạn thực sự dùng AI để generate toàn bộ văn bản mà không edit, đó là vấn đề academic integrity, không phải vấn đề detection.