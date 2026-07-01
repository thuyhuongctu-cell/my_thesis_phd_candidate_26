---
name: latex-ctu-pdf-build
description: >
  Cài đặt và vận hành môi trường LaTeX (xelatex/pdflatex) ngay trong container
  Claude Code để biên dịch luận án/chuyên đề định dạng CTU (QĐ 1799/SH) và các
  bài báo P3–P9 ra PDF. Dùng khi cần: biên dịch .tex, sinh PDF luận án, compile
  paper, cài texlive, sửa lỗi biên dịch LaTeX tiếng Việt, build defense slides.
  Triggers: pdflatex, xelatex, biên dịch latex, compile pdf, build luận án pdf,
  texlive, biber, CTU format.
---

# Biên dịch LaTeX trong container này

## 1. Cài đặt (đã kiểm chứng hoạt động trong môi trường web container)

```bash
apt-get update -qq
apt-get install -y -qq texlive-xetex texlive-latex-extra \
  texlive-fonts-recommended texlive-bibtex-extra biber \
  fonts-liberation lmodern poppler-utils
```
~10 phút, chạy nền bằng `run_in_background`. Kết quả: XeTeX + pdfTeX (TeX Live 2023),
biber/bibtex, pdftotext.

**Font**: container KHÔNG có Times New Roman. Dùng **TeX Gyre Termes**
(metric tương đương, có sẵn trong texlive): sinh .tex với
`MAINFONT="TeX Gyre Termes"`. Trên máy NCS có TNR thật thì bỏ biến này.

## 2. Quy trình chuẩn (sinh .tex → biên dịch → kiểm lỗi)

```bash
# Sinh nguồn .tex từ markdown (định dạng CTU: TNR 13pt, giãn 1.2, lề 3/2/2/2)
MAINFONT="TeX Gyre Termes" bash scripts/build_latex_ctu.sh      # luận án + CĐ1 + CĐ2
MAINFONT="TeX Gyre Termes" bash scripts/build_latex_papers.sh   # P7/P8/P9 (journal)

# Biên dịch (2 lượt cho mục lục/tham chiếu chéo)
cd latex/ctu
xelatex -interaction=nonstopmode -halt-on-error LUAN_AN_CTU.tex
xelatex -interaction=nonstopmode LUAN_AN_CTU.tex
```

**Engine theo tài liệu**:
| Tài liệu | Engine | Lý do |
|---|---|---|
| LUAN_AN_CTU, CD1_CTU, CD2_CTU | xelatex | tiếng Việt Unicode + fontspec |
| latex/p7, p8, p9 | xelatex | ký tự toán Unicode (β, ≈, ₁) |
| latex/p3..p6 (hand-crafted) | pdflatex + **biber** ×1 + pdflatex ×2 | biblatex style=apa |

## 3. Kiểm lỗi — LUÔN làm sau mỗi lượt biên dịch

```bash
grep -E '^!' <file>.log | head        # lỗi fatal (trống = sạch)
grep -c "LaTeX Warning" <file>.log     # cảnh báo (tham chiếu chéo, overfull...)
grep -oE 'Output written on [^,]*\([0-9]+ pages' <file>.log   # xác nhận PDF + số trang
```
Không bao giờ báo "đã có PDF" nếu chưa thấy dòng `Output written on ...`.

## 4. Lỗi thường gặp

| Lỗi | Cách xử lý |
|---|---|
| `! LaTeX Error: File 'biblatex.sty' not found` | `apt-get install texlive-bibtex-extra biber` |
| `! Package fontspec: The font "Times New Roman" cannot be found` | dùng `MAINFONT="TeX Gyre Termes"` rồi sinh lại .tex |
| Ký tự Việt vỡ/thiếu dấu | đang dùng pdflatex — chuyển sang xelatex |
| `Undefined control sequence \tightlist` | .tex sinh tay từ fragment pandoc — phải sinh bằng `--standalone` |
| Bảng tràn lề (longtable quá rộng) | thu gọn nội dung ô trong nguồn .md, hoặc thêm `\small` trước longtable trong .tex |
| Mục lục trống/sai số trang | chạy xelatex lượt 2 |

## 5. Benchmark đã xác minh (2026-06-12, container web)

| File | Kết quả |
|---|---|
| LUAN_AN_CTU.tex | PDF 92 trang ✓ |
| CD1_CTU.tex | PDF 49 trang ✓ |
| CD2_CTU.tex | PDF 35 trang ✓ |
| p7_jibs / p8_worlddev / p9_ijoem | PDF 32 / 31 / 46 trang ✓ |

PDF không commit vào git (đã gitignore); gửi cho NCS bằng SendUserFile hoặc
NCS tự biên dịch trên máy theo `latex/README.md`.
