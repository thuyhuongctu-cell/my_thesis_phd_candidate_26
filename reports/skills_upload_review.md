# Đánh giá 6 ZIP skills upload — 30/05/2026

## Tóm tắt quyết định

| # | File ZIP | Nội dung | Loại | Đánh giá | Hành động |
|---|---|---|---|---|---|
| 1 | `1774fb5d-humanizermain.zip` (20KB) | `humanizer-main/` — SKILL.md 32KB, 22+ pattern categories | **Claude skill** | ⭐⭐⭐⭐⭐ Rất phù hợp | **ĐÃ CÀI** vào `.claude/skills/humanizer/` |
| 2 | `8e747c42-WRITING.mdmain.zip` (36KB) | `WRITING.md-main/skills/writing/` — 14 rules, oriented blog/marketing | Claude skill | ⭐⭐ Không phù hợp | **BỎ** (general-purpose, không academic) |
| 3 | `18933e6b-phphumanizer5.x_1.zip` (76KB) | `php-humanizer-5.x/` — PHP Composer library (Coduo) | **Không phải skill** | — | **BỎ** (PHP code library) |
| 4 | `246ce336-phphumanizer5.x.zip` (76KB) | Trùng #3 (cùng MD5) | — | — | **BỎ** (duplicate) |
| 5 | `5e4f5f5d-Humanizermain_1.zip` (1.7MB) | `Humanizer-main/` — .NET C# i18n localization library | Project (không phải Claude skill) | ⭐ Không liên quan | **BỎ** |
| 6 | `fdfcaeb2-Humanizermain_2.zip` (1.7MB) | Trùng #5 (cùng MD5) | — | — | **BỎ** (duplicate) |

→ **6 ZIP = 4 unique = 1 skill có giá trị**

---

## Chi tiết đánh giá

### ✅ 1. `humanizer` (CÀI ĐẶT THÀNH CÔNG)

**Source:** `humanizer-main/SKILL.md` v2.7.0 (MIT License, Anthropic-style frontmatter)
**Quy mô:** 582 dòng / 32KB — **2.9× lớn hơn** `phd-academic-writing-humanizer` hiện có (201 dòng)
**Cài đặt tại:** `.claude/skills/humanizer/`

**Cấu trúc nội dung (22+ sections):**
1. PERSONALITY AND SOUL — phát hiện "văn bản không có hồn"
2. Voice Calibration (Optional) — căn chỉnh giọng văn từ sample
3. CONTENT PATTERNS (6 patterns):
   - Undue Emphasis on Significance, Legacy, Broader Trends
   - Undue Emphasis on Notability and Media Coverage
   - Superficial Analyses with -ing Endings
   - Promotional and Advertisement-like Language
   - Vague Attributions and Weasel Words
   - Outline-like "Challenges and Future Prospects" Sections
4. LANGUAGE AND GRAMMAR PATTERNS (7 patterns):
   - Overused "AI Vocabulary" Words
   - Avoidance of "is"/"are" (Copula Avoidance)
   - Negative Parallelisms and Tailing Negations
   - Rule of Three Overuse
   - Elegant Variation (Synonym Cycling)
   - False Ranges
   - Passive Voice and Subjectless Fragments
5. STYLE PATTERNS (6+ patterns):
   - Em Dashes (and En Dashes): Cut Them
   - Overuse of Boldface
   - Inline-Header Vertical Lists
   - Title Case in Headings
   - Emojis
   - Curly Quotation Marks

**So sánh với skill hiện có:**

| Aspect | `phd-academic-writing-humanizer` (hiện có) | `humanizer` (mới) |
|---|---|---|
| Số dòng | 201 | 582 |
| Pattern categories | ~5 (em-dash focus) | 22+ |
| Có "soulless writing" detection | Không | Có |
| Có voice calibration từ sample | Không | Có |
| Before/after examples | Có (ít) | Có (nhiều, chi tiết) |
| Tiếng Việt | Có | Không (EN-only) |
| Phù hợp luận án | Có | Có (cần dùng kết hợp) |

**Khuyến nghị sử dụng:**
- **Polish round cuối cho P3–P8 EN manuscripts**: Apply `humanizer` skill để quét 22+ pattern → loại bỏ AI tells còn sót.
- **Vẫn giữ `phd-academic-writing-humanizer`** cho VI content (em-dash focus + tiếng Việt).
- **`stop-slop`** vẫn dùng cho quick AI-pattern cleanup.

---

### ❌ 2. `writing` (BỎ)

**Source:** `WRITING.md-main/skills/writing/SKILL.md` v1.3.1 (author: Anbeeld, MIT)
**Quy mô:** 214 dòng / 17KB
**Phạm vi tự khai báo:**
> "Drafting and revising prose that readers will see: **blog posts, articles, documentation, criticism, long-form, emails, marketing, SEO copy, UI text**. Not for code comments, commit messages, or private notes."

**Lý do bỏ:** Phạm vi rõ ràng là *general/commercial writing* — không đề cập academic, dissertation, journal manuscripts. 14 core rules của nó tập trung vào "fit format to medium", "earned specificity", "show concrete things before generalizing" — đều là rules tốt cho blog/marketing nhưng đã được chuẩn academic IB hardener (top-1% reviewer review) cover ở mức nghiêm ngặt hơn.

**Tuy nhiên:** WRITING.md (28KB) bản đầy đủ có thể dùng làm tham khảo style guide nếu sau này viết blog/op-ed về luận án — không cần cài như skill ngay.

---

### ❌ 3 + 4. `php-humanizer-5.x` (BỎ, DUPLICATE)

**Source:** `Coduo/PHPHumanizer` — Composer PHP library, không phải Claude skill.
**Mục đích:** Format numbers/dates/file-sizes ("2 hours ago", "1.5 GB") cho PHP applications.
**Lý do bỏ:** Không liên quan dự án luận án (không có PHP backend). 2 zip này là duplicate của nhau (cùng MD5).

---

### ❌ 5 + 6. `Humanizer-main` .NET (BỎ, DUPLICATE)

**Source:** Humanizer library cho .NET (C#) — tương tự PHP humanizer nhưng cho .NET.
**Mục đích:** Internationalization (i18n) — "turning numbers, dates, times, enums, quantities, etc. into human-friendly text across many locales".
**Skills bên trong:** `add-locale`, `add-locale-batch` — hướng dẫn add locale parity cho library này.
**Lý do bỏ:** Dự án luận án không phải .NET; 2 skill kèm theo (add-locale) chỉ áp dụng cho việc bảo trì chính library Humanizer-main, không có ứng dụng cho academic writing. 2 zip này là duplicate (cùng MD5).

---

## Hành động kế tiếp (tùy chọn)

1. **Test humanizer skill** trên 1 paper EN bất kỳ:
   - User invoke `/humanizer` (hoặc Claude sẽ tự gợi ý khi edit prose)
   - Check kết quả có phát hiện thêm pattern nào mà `phd-academic-writing-humanizer` đã bỏ sót không.
2. Nếu humanizer skill phát hiện nhiều issue → chạy polish round cuối cho P3/P4/P5/P6/P7/P8 EN manuscripts trước khi submit.

---

*Generated: 2026-05-31, sau commit `c7e6620`.*
