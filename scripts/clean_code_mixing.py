#!/usr/bin/env python3
"""Làm sạch code-mixing tiếng Anh lẫn trong câu tiếng Việt (Ch2-Ch4...).

Nguyên tắc an toàn:
- KHÔNG thay trong: `inline code`, $...$, $$...$$, và (trong ngoặc đơn).
  (Giữ nguyên định nghĩa thuật ngữ lần đầu trong ngoặc — đúng chuẩn học thuật,
   không phải "lẫn trong câu".)
- Thay theo cụm dài trước, cụm ngắn sau.
- Bảo toàn viết hoa đầu câu.
Dùng:  python3 scripts/clean_code_mixing.py thesis/chuong_2_tong_quan_tai_lieu_vi.md [--apply]
"""
import re, sys

# (pattern, replacement). Áp dụng theo thứ tự. Dùng \b cho an toàn biên từ.
RULES = [
    # cụm nhiều từ (an toàn nhất)
    (r"I[–-]P relationship", "quan hệ quốc tế hóa và hiệu quả"),
    (r"\bmeta[- ]analyses\b", "các phân tích tổng hợp"),
    (r"\bmeta[- ]analysis\b", "phân tích tổng hợp"),
    (r"\bmeta[- ]analytic\b", "phân tích tổng hợp"),
    (r"\bmeta[- ]regression\b", "hồi quy phân tích tổng hợp"),
    (r"\bpublication bias\b", "lệch lạc công bố"),
    (r"\btrim[- ]and[- ]fill\b", "cắt và điền"),
    (r"\bleave[- ]one[- ]out\b", "bỏ một nghiên cứu lần lượt"),
    (r"\blabou?r productivity\b", "năng suất lao động"),
    (r"\bfirm performance\b", "hiệu quả doanh nghiệp"),
    (r"\bdigital capability lens\b", "lăng kính năng lực số"),
    (r"\bdigital adoption index\b", "chỉ số chấp nhận số"),
    (r"\bdigital shield( effect)?\b", "hiệu ứng lá chắn số"),
    (r"\binstitutional voids\b", "khoảng trống thể chế"),
    (r"\binstitutional theory\b", "lý thuyết thể chế"),
    (r"\binstitutional obstacles\b", "rào cản thể chế"),
    (r"\bupper echelons( theory)?\b", "lý thuyết thượng tầng quản trị"),
    (r"\bdynamic capabilities\b", "năng lực động"),
    (r"\babsorptive capacity\b", "năng lực hấp thụ"),
    (r"\bboundary conditions?\b", "điều kiện biên"),
    (r"\blevel[- ]shifters?\b", "yếu tố nâng mặt bằng"),
    (r"\bPacific SIDS\b", "đảo nhỏ Thái Bình Dương"),
    (r"\bAdvanced Innovation([- ]Driven)?\b", "tiên tiến đổi mới"),
    (r"\bAdvanced Resource\b", "tiên tiến tài nguyên"),
    (r"\bLower[- ]mid(dle)?( transition)?\b", "chuyển đổi thu nhập trung bình thấp"),
    (r"\bUpper[- ]mid(dle)?\b", "trung bình cao"),
    (r"\breverse causality\b", "nhân quả ngược"),
    (r"\bcountry[- ]year\b", "cặp nền kinh tế và năm"),
    (r"\bcross[- ]country\b", "đa quốc gia"),
    (r"\bChinese economies\b", "Đại Trung Hoa"),
    (r"\bSouth Asia\b", "Nam Á"),
    (r"\bresource[- ]based view\b", "lý thuyết dựa trên nguồn lực"),
    (r"\bTier[- ]?1\b", "Tầng 1"),
    (r"\bTier[- ]?2\b", "Tầng 2"),
    (r"\bTier[- ]?3\b", "Tầng 3"),
    (r"\bmisallocation\b", "phân bổ sai nguồn lực"),
    (r"\binternationali[sz]ation\b", "quốc tế hóa"),
    (r"\bz[- ]scores?\b", "điểm z"),
    (r"\bz[- ]std\b", "chuẩn hóa z"),
    # cụm có "I–P" còn lại (sau khi đã xử lý "relationship")
    (r"\b(quan hệ|mối quan hệ|đường cong|văn liệu|kết quả|dị biệt|gradient) I[–-]P\b",
     lambda m: ("văn liệu về quan hệ quốc tế hóa và hiệu quả" if m.group(1)=="văn liệu"
                else m.group(1)+" quốc tế hóa và hiệu quả")),
    (r"\bI[–-]P\b", "quốc tế hóa và hiệu quả"),
    # acronym/nhãn ngắn (uppercase, an toàn vì tiếng Việt thường không có)
    (r"\bRBV\b", "lý thuyết dựa trên nguồn lực"),
    (r"\bEMNEs\b", "doanh nghiệp đa quốc gia thị trường mới nổi"),
    # bổ sung đợt 2 (thuật ngữ còn sót trong văn xuôi)
    (r"emerging Asia", "châu Á mới nổi"),
    (r"Foundational Digital Adoption Framework", "Khung chấp nhận số nền tảng"),
    (r"robust standard errors", "sai số chuẩn vững"),
    (r"\bRobust SE\b", "sai số chuẩn vững"),
    (r"phase empirical", "giai đoạn thực nghiệm"),
    (r"gộp effect", "hiệu ứng gộp"),
    (r"\bcapstone\b", "tổng hợp"),
    (r"\bpooled\b", "gộp"),
    (r"\bpool\b", "mẫu gộp"),
    (r"\bwaves\b", "các đợt"),
    (r"\bwave\b", "đợt"),
    (r"\bSpecification\b", "Đặc tả"),
    # bổ sung đợt 3 (chuyên đề CĐ1/CĐ2 — văn xuôi ngoài ngoặc/đậm/mã)
    (r"\bPatterns?\b", "Khuôn mẫu"),
    (r"\bpatterns?\b", "khuôn mẫu"),
    (r"\bvoids\b", "khoảng trống"),
    (r"\bin press\b", "sắp xuất bản"),
]

def protect(text):
    """Tách text thành các đoạn, đánh dấu đoạn được bảo vệ.

    Bảo vệ: `code`, $math$, (ngoặc đơn), *in nghiêng*/**in đậm**
    (tên tạp chí, tiêu đề tiếng Anh, tên cấu trúc lý thuyết)."""
    pat = re.compile(
        r"(`[^`]*`|\$\$.*?\$\$|\$[^$\n]*\$|\([^()]*\)|\*\*[^*\n]+\*\*|\*[^*\n]+\*)", re.S)
    parts = []
    last = 0
    for m in pat.finditer(text):
        if m.start() > last:
            parts.append(("T", text[last:m.start()]))
        parts.append(("P", m.group(0)))  # protected
        last = m.end()
    if last < len(text):
        parts.append(("T", text[last:]))
    return parts

def apply_rules(seg):
    for pat, rep in RULES:
        seg = re.sub(pat, rep, seg, flags=re.IGNORECASE if isinstance(rep,str) and pat.islower() else 0)
    return seg

def fix_sentence_initial(text):
    # viết hoa lại sau dấu kết câu nếu ký tự đầu là thường (do thay thế)
    def cap(m):
        return m.group(1) + m.group(2).upper()
    return re.sub(r"([.!?]\s+|^|\n\n)([a-zà-ỹ])", lambda m: m.group(1)+m.group(2).upper(), text)

def process(text):
    # KHÔNG xử lý phần danh mục tài liệu tham khảo (giữ nguyên tiêu đề tiếng Anh).
    m = re.search(r"\n#{1,6}\s*Tài liệu tham khảo|\n#{1,6}\s*Danh mục tham khảo", text, re.IGNORECASE)
    if m:
        head, tail = text[:m.start()], text[m.start():]
    else:
        head, tail = text, ""
    parts = protect(head)
    out = []
    n = 0
    for kind, seg in parts:
        if kind == "T":
            new = apply_rules(seg)
            if new != seg: n += 1
            out.append(new)
        else:
            out.append(seg)
    result = "".join(out) + tail
    return result, n

if __name__ == "__main__":
    path = sys.argv[1]
    apply = "--apply" in sys.argv
    txt = open(path, encoding="utf-8").read()
    new, n = process(txt)
    if apply:
        open(path, "w", encoding="utf-8").write(new)
        print(f"APPLIED to {path}: {n} text-segments changed")
    else:
        # show a sample of changed lines
        import difflib
        old_lines = txt.splitlines()
        new_lines = new.splitlines()
        shown = 0
        for ol, nl in zip(old_lines, new_lines):
            if ol != nl and shown < 15:
                print("--- ", ol[:160])
                print("+++ ", nl[:160])
                shown += 1
        print(f"[dry-run] {path}: {shown} sample diffs shown")
