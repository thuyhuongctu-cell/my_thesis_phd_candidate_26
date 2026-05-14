---
name: chinh-sua-tai-lieu-latex-khoa-hoc
description: >
  Chỉnh sửa và định dạng tài liệu nghiên cứu, bài báo khoa học, luận án bằng LaTeX với công thức toán học đẹp, rõ ràng. Sử dụng khi cần chỉnh sửa paper, bài báo, luận án, dissertation, thesis, chương luận văn, tài liệu nghiên cứu khoa học, công thức toán, mathematical equations, xuất file PDF hoặc Word, chuyển đổi LaTeX sang Word/PDF, định dạng tài liệu xuất bản, journal submission, IEEE, ACM, Springer templates, academic writing, scientific papers.
---

# Tổng quan

Kỹ năng này giúp chỉnh sửa, định dạng và hoàn thiện tài liệu nghiên cứu khoa học bằng LaTeX — từ bài báo đơn lẻ đến luận án đa chương. Tập trung vào việc trình bày công thức toán học chuyên nghiệp, cấu trúc tài liệu rõ ràng, và xuất file PDF hoặc Word phù hợp với yêu cầu xuất bản.

## Khi nào sử dụng kỹ năng này

- Chỉnh sửa bài báo nghiên cứu (research paper, journal article)
- Định dạng luận án (thesis, dissertation) hoặc các chương riêng lẻ
- Cải thiện trình bày công thức toán học trong LaTeX
- Chuyển đổi từ LaTeX sang Word (.docx) hoặc PDF
- Chuẩn bị tài liệu theo template của tạp chí (IEEE, ACM, Springer, AAAI, v.v.)
- Sửa lỗi biên dịch LaTeX, cải thiện cấu trúc code
- Tối ưu hóa typography và layout cho tài liệu khoa học

---

# Nguyên tắc chỉnh sửa LaTeX

## 1. Công thức toán học đẹp và rõ ràng

LaTeX được tạo ra để trình bày toán học chuyên nghiệp. Tuân theo các quy ước này:

### Biến và ký hiệu
- **Biến luôn in nghiêng**: Dùng chế độ math `$x$`, không dùng `\textit{x}` trong văn bản
- **Vector in đậm**: `\mathbf{v}` hoặc `\boldsymbol{v}` (tùy package)
- **Ma trận viết hoa in đậm**: `\mathbf{A}`
- **Hàm toán học dùng roman**: `\sin`, `\cos`, `\log`, `\max` — không bao giờ `sin` (nghiêng)
- **Số và dấu câu thông thường**: `3.5\%` trong text và `$3.5\%$` trong math nên giống nhau

### Môi trường equation
- **Inline math**: `$...$` cho công thức ngắn trong câu
- **Display math**: `\[...\]` hoặc `\begin{equation}...\end{equation}` cho công thức độc lập
- **Tránh `$$...$$`**: Cú pháp cũ, gây lỗi với AMS-LaTeX
- **Dùng `align` cho nhiều dòng**:
```latex
\begin{align}
  E &= mc^2 \\
  F &= ma
\end{align}
```
- **Chỉ đánh số equation khi tham chiếu**: Dùng `equation*` hoặc `\[...\]` nếu không cần số

### Khoảng trắng và căn chỉnh
- LaTeX tự động xử lý khoảng trắng trong math mode
- Chỉ thêm `\,` (thin space) trước differential: `\int f(x)\,dx`
- Căn chỉnh theo toán tử (`=`, `\leq`) trong `align`, không căn theo `+` hay `-`
- Equation không được dài hơn chiều rộng text — chia thành nhiều dòng hoặc định nghĩa ký hiệu phụ

### Ví dụ tốt và xấu

**Xấu**:
```latex
The variable x is related to y.
We have sin(theta) = 0.5.
```

**Tốt**:
```latex
The variable $x$ is related to $y$.
We have $\sin(\theta) = 0.5$.
```

**Xấu**:
```latex
$$x^2 + y^2 = r^2$$
```

**Tốt**:
```latex
\begin{equation}
  x^2 + y^2 = r^2
  \label{eq:circle}
\end{equation}
```

---

## 2. Cấu trúc tài liệu rõ ràng

### Preamble gọn và có tổ chức
```latex
\documentclass[12pt,a4paper]{article}

% Packages toán học
\usepackage{amsmath,amssymb,amsthm}

% Hình ảnh và đồ họa
\usepackage{graphicx}

% Tài liệu tham khảo
\usepackage[style=authoryear,backend=biber]{biblatex}
\addbibresource{references.bib}

% Hyperlinks
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue}

% Font (tùy chọn)
\usepackage{lmodern}
```

### Cấu trúc phân cấp
- `\section{}` → `\subsection{}` → `\subsubsection{}`
- Dùng `\label{}` và `\ref{}` cho cross-reference tự động
- Đặt label có ý nghĩa: `\label{sec:methods}`, `\label{eq:main-result}`

### Quản lý file lớn (luận án)
```latex
% main.tex
\documentclass{book}
\begin{document}
\include{chapters/chapter1}
\include{chapters/chapter2}
\include{chapters/chapter3}
\end{document}
```
Mỗi chương là file riêng, dễ quản lý và biên dịch từng phần với `\includeonly{}`.

---

## 3. Định dạng theo template tạp chí

Hầu hết tạp chí khoa học cung cấp LaTeX template (IEEE, ACM, Springer, Elsevier, AAAI).

### Quy trình
1. **Tải template chính thức** từ website tạp chí hoặc Overleaf
2. **Không sửa document class**: `\documentclass[journal]{IEEEtran}` — giữ nguyên
3. **Tuân thủ hướng dẫn package**: Một số template cấm packages nhất định
4. **Kiểm tra font size, margins**: Thường đã được thiết lập sẵn
5. **Biên dịch thử nghiệm sớm**: Phát hiện lỗi trước khi viết nhiều

### Lưu ý phổ biến
- **IEEE**: Dùng `IEEEtran.cls`, bibliography style `IEEEtran.bst`
- **ACM**: Dùng `acmart.cls`, chế độ `\documentclass[sigconf]{acmart}`
- **Springer**: Dùng `svjour3.cls` hoặc `llncs.cls` (conference)
- **AAAI**: Dùng `aaai26.sty`, có yêu cầu nghiêm ngặt về packages

---

## 4. Tài liệu tham khảo (Bibliography)

### BibTeX vs BibLaTeX
- **BibTeX**: Truyền thống, dùng `\bibliographystyle{}` và `\bibliography{}`
- **BibLaTeX**: Hiện đại hơn, linh hoạt hơn, dùng `backend=biber`

### Quy trình BibLaTeX (khuyến nghị)
```latex
% Preamble
\usepackage[style=authoryear,backend=biber]{biblatex}
\addbibresource{references.bib}

% Trong document
\cite{Author2020}
\parencite{Author2020}

% Cuối document
\printbibliography
```

### Quản lý .bib file
- Dùng reference manager: Zotero, Mendeley, JabRef
- Export trực tiếp sang .bib format
- Kiểm tra DOI fields để tự động lấy metadata
- Giữ citation keys nhất quán: `Author2020`, `SmithJones2021`

---

# Xuất file PDF và Word

## Xuất PDF (tiêu chuẩn)

### Biên dịch LaTeX → PDF
```bash
pdflatex main.tex
biber main        # hoặc bibtex main
pdflatex main.tex
pdflatex main.tex  # Chạy 2 lần để cập nhật references
```

Hoặc dùng `latexmk` (tự động):
```bash
latexmk -pdf main.tex
```

### Tối ưu PDF output
- Dùng `hyperref` package để tạo PDF có bookmark và clickable links
- Tắt colored boxes: `\hypersetup{hidelinks}` nếu in ấn
- Embed fonts đầy đủ cho journal submission (thường tự động)

---

## Chuyển đổi LaTeX → Word

Nhiều tạp chí yêu cầu Word format. Có 3 phương pháp chính:

### Phương pháp 1: Pandoc (khuyến nghị)

Pandoc là công cụ command-line mạnh mẽ, miễn phí.

```bash
pandoc input.tex -o output.docx --bibliography=references.bib --csl=journal-style.csl
```

**Ưu điểm**: 
- Giữ được citations, equations, tables
- Hỗ trợ cross-references với `pandoc-crossref` filter
- Miễn phí, open-source

**Hạn chế**:
- Cần giữ LaTeX code đơn giản (tránh packages phức tạp)
- Equation references có thể cần sửa thủ công
- Formatting cần điều chỉnh trong Word sau khi convert

**Cải thiện kết quả**:
```bash
pandoc -F pandoc-crossref --citeproc -s input.tex -f latex -t docx -o output.docx --bibliography=references.bib --csl=apa.csl --reference-doc=template.docx
```

### Phương pháp 2: PDF → Word (Word 2016+)

1. Biên dịch LaTeX → PDF như bình thường
2. Mở Microsoft Word → File → Open → chọn PDF file
3. Word sẽ convert PDF sang định dạng có thể chỉnh sửa

**Ưu điểm**: 
- Không cần công cụ bên ngoài
- Giữ được layout tương đối tốt

**Hạn chế**:
- Equations trở thành hình ảnh hoặc text thông thường
- Cần reformat lại nhiều
- Ligatures (fi, fl) có thể bị lỗi

**Lưu ý**: Tắt ligatures khi compile PDF bằng XeLaTeX nếu dùng phương pháp này.

### Phương pháp 3: Dịch vụ chuyên dụng

- **GrindEQ LaTeX-to-Word**: Software thương mại, kết quả tốt
- **Docx2LaTeX** (ngược lại): Chuyển Word → LaTeX
- **Online converters**: Vertopal, Aspose (miễn phí nhưng hạn chế)

**Khi nào dùng**: Tài liệu phức tạp, nhiều equations, cần kết quả chính xác cao.

---

# Quy trình làm việc thực tế

## Bài báo nghiên cứu (Research Paper)

1. **Chọn template tạp chí**: Tải từ Overleaf hoặc website chính thức
2. **Thiết lập structure**:
   - Abstract
   - Introduction
   - Methods / Methodology
   - Results
   - Discussion
   - Conclusion
   - References
3. **Viết nội dung**: Tập trung vào content, không lo formatting
4. **Chèn equations**: Dùng `equation` hoặc `align`, đánh label rõ ràng
5. **Thêm figures/tables**: Dùng `\includegraphics` và `table` environment
6. **Quản lý citations**: Import .bib từ reference manager
7. **Biên dịch và kiểm tra**: Chạy pdflatex/biber nhiều lần
8. **Xuất PDF cuối cùng**: Kiểm tra fonts, links, page numbers

## Luận án (Thesis/Dissertation)

1. **Dùng document class `book` hoặc `report`**:
```latex
\documentclass[12pt,a4paper,twoside]{book}
```
2. **Tổ chức theo chapters**: Mỗi chương một file riêng
3. **Front matter**: Title page, abstract, acknowledgments, table of contents
4. **Main matter**: Chapters 1-N
5. **Back matter**: Appendices, bibliography
6. **Sử dụng `\include{}` và `\includeonly{}`**: Biên dịch nhanh từng chương khi sửa

### Ví dụ structure luận án
```
thesis/
├── main.tex
├── preamble.tex
├── chapters/
│   ├── chapter1.tex
│   ├── chapter2.tex
│   └── chapter3.tex
├── figures/
├── references.bib
└── appendices/
    └── appendixA.tex
```

---

# Sửa lỗi thường gặp

## Lỗi biên dịch

### "Undefined control sequence"
- Nguyên nhân: Dùng lệnh không tồn tại hoặc thiếu package
- Giải pháp: Kiểm tra typo, thêm package cần thiết (vd: `\usepackage{amsmath}`)

### "Missing $ inserted"
- Nguyên nhân: Ký hiệu toán học ngoài math mode
- Giải pháp: Bọc trong `$...$` hoặc `\[...\]`

### "File not found"
- Nguyên nhân: Đường dẫn hình ảnh hoặc .bib file sai
- Giải pháp: Kiểm tra relative path, đảm bảo file tồn tại

### Bibliography không hiển thị
- Nguyên nhân: Chưa chạy biber/bibtex hoặc không có `\cite{}` trong text
- Giải pháp: Chạy `biber main` (hoặc `bibtex main`), sau đó `pdflatex` lại 2 lần

## Vấn đề formatting

### Equations quá dài
- Dùng `align` hoặc `multline` để chia nhiều dòng
- Định nghĩa intermediate symbols để rút gọn

### Figures không ở đúng vị trí
- LaTeX tự động đặt figures theo thuật toán tối ưu
- Dùng `[h]`, `[t]`, `[b]` placement specifiers (nhưng đừng ép quá)
- Đọc thêm về float placement nếu cần kiểm soát chặt

### Table quá rộng
- Giảm font size: `{\small ...}`
- Xoay ngang: `\usepackage{rotating}`, dùng `sidewaystable`
- Chia thành nhiều tables nhỏ hơn

---

# Checklist chất lượng

Trước khi submit hoặc xuất file cuối cùng:

- [ ] Tất cả equations có label và được tham chiếu đúng
- [ ] Variables in nghiêng, functions roman, vectors bold
- [ ] Không còn lỗi biên dịch (warnings có thể chấp nhận được)
- [ ] Citations đầy đủ, bibliography hiển thị chính xác
- [ ] Figures và tables có captions rõ ràng
- [ ] Cross-references (Section X, Figure Y, Equation Z) cập nhật đúng
- [ ] Fonts embedded đầy đủ trong PDF (quan trọng cho submission)
- [ ] Hyperlinks hoạt động (nếu dùng `hyperref`)
- [ ] Tuân thủ template requirements của tạp chí (nếu có)
- [ ] Spell-check (dùng editor có spell checker hoặc external tool)

---

# Tài nguyên tham khảo

Khi cần tra cứu thêm:

- **Overleaf Templates**: Hàng nghìn templates cho journals, conferences, theses
- **CTAN** (Comprehensive TeX Archive Network): Kho packages chính thức
- **IEEE Math Typesetting Guide**: Quy ước chuẩn cho equations
- **LaTeX Wikibook**: Hướng dẫn toàn diện về math typesetting
- **Detexify**: Vẽ ký hiệu để tìm LaTeX command tương ứng
- **Pandoc documentation**: Hướng dẫn chi tiết về conversion options

---

# Lời khuyên cuối cùng

1. **Giữ code đơn giản**: Không tạo macros phức tạp trừ khi thực sự cần thiết
2. **Commit thường xuyên**: Dùng Git để version control (đặc biệt với luận án)
3. **Backup .bib file**: Reference database là tài sản quý giá
4. **Học từ templates tốt**: Đọc code của papers được format đẹp
5. **Hỏi khi cần**: LaTeX community rất hữu ích (StackExchange, Reddit r/LaTeX)

LaTeX có learning curve, nhưng kết quả chuyên nghiệp và khả năng tự động hóa hoàn toàn xứng đáng với công sức bỏ ra.
