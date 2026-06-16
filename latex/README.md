# Nguồn LaTeX — Luận án, Chuyên đề (CTU) và Bài báo

## 1. Yêu cầu chung
Container web **không có trình biên dịch TeX**; các file `.tex` ở đây được sinh/kiểm
sạch sẵn để **biên dịch trên máy NCS**. Cần cài TeX Live (hoặc MiKTeX) đầy đủ.

- **Luận án + Chuyên đề** dùng **xelatex** (bắt buộc: tiếng Việt Unicode + Times New Roman).
- Nếu máy **không có font Times New Roman**, đặt biến môi trường khi sinh lại:
  `MAINFONT="TeX Gyre Termes" bash scripts/build_latex_ctu.sh` (metric tương đương TNR).

## 2. Luận án & Chuyên đề — định dạng CTU (QĐ 1799/SH)
Đã mã hóa đúng chuẩn: **Times New Roman 13pt · giãn dòng 1,2 · lề trái 3cm / phải–trên–dưới 2cm**
(`extreport` 13pt + `geometry` + `setspace` + `babel` vietnamese).

| File | Nội dung |
|---|---|
| `ctu/LUAN_AN_CTU.tex` | Luận án đầy đủ (đầu mục đến 5 chương đến tài liệu tham khảo đến Phụ lục A) |
| `ctu/CD1_CTU.tex` | Chuyên đề 1 |
| `ctu/CD2_CTU.tex` | Chuyên đề 2 |
| `ctu/figures/` | Hình cho luận án (`fig_*`) và CĐ2 (`hinh_*`) — đã gom sẵn |

**Sinh lại:** `bash scripts/build_latex_ctu.sh`
**Biên dịch** (trong `latex/ctu/`):
```bash
xelatex LUAN_AN_CTU.tex && xelatex LUAN_AN_CTU.tex   # 2 lần cho mục lục
xelatex CD1_CTU.tex && xelatex CD1_CTU.tex
xelatex CD2_CTU.tex && xelatex CD2_CTU.tex
```
> Ghi chú toán: preamble (pandoc) nạp `unicode-math`; nếu muốn math khớp Times,
> thêm `\setmathfont{TeX Gyre Termes Math}` (hoặc `STIX Two Math`) vào đầu file.

## 3. Bài báo (định dạng tạp chí, không phải CTU)
Bài báo nộp theo template tạp chí (article 12pt, giãn dòng đôi).

| Bài | File | Biên dịch | Trạng thái |
|---|---|---|---|
| P3 Việt Nam (JABS) | `p3/p3_jabs_submission.tex` | pdflatex + biber | Hand-crafted, dùng `shared/macros.tex` |
| P4 Singapore (MIR) | `p4/p4_mir_submission.tex` | pdflatex + biber | Hand-crafted |
| P5 Trung Quốc (IJOEM) | `p5/p5_ijoem_submission.tex` | pdflatex + biber | Hand-crafted |
| P6 Meta (IBR) | `p6/p6_ibr_submission.tex` | pdflatex + biber | Hand-crafted |
| P7 Đa quốc gia (JIBS) | `p7/p7_jibs_submission.tex` | **xelatex** | Sinh từ bản thảo chuẩn |
| P8 SIDS (World Dev.) | `p8/p8_worlddev_submission.tex` | **xelatex** | Sinh từ bản thảo chuẩn |
| P9 Ấn Độ (IJOEM) | `p9/p9_ijoem_submission.tex` | **xelatex** | Sinh từ bản thảo chuẩn |

- P3–P6 dùng macro toán dùng chung trong `shared/macros.tex` (`\FSTS`, `\lnLP`, `\TCIz`…).
- P7–P9 dùng **xelatex** vì bản thảo chứa ký tự toán Unicode (β, ≈, ₁, ²). Nếu cần
  bản đẹp theo phong cách P3–P6, áp macro `shared/macros.tex` cho các công thức chính.
- **Sinh lại P7/P8/P9:** `bash scripts/build_latex_papers.sh`

## 4. Trạng thái biên dịch (xác minh trong container, TeX Live 2023)

| File | Kết quả |
|---|---|
| LUAN_AN_CTU.pdf | Có 92 trang |
| CD1_CTU.pdf / CD2_CTU.pdf | Có 49 / 36 trang |
| p7_jibs / p8_worlddev / p9_ijoem | Có 32 / 31 / 46 trang |
| p3_jabs / p5_ijoem / p6_ibr | Có 8 / 6 / 6 trang (bản tex rút gọn + biber) |
| p4_mir | ⚠️ Cần `svjour3.cls` — tải chính thức từ Springer (đi kèm hướng dẫn tác giả MIR), đặt cạnh file .tex |

Font trong container: `MAINFONT="TeX Gyre Termes"` (Times New Roman metric-equivalent).
Trên máy có TNR thật: bỏ biến MAINFONT rồi sinh lại.

## 5. Đối chiếu số liệu
Mọi `.tex` ở đây thống nhất với số khóa của luận án sau đợt đồng bộ FSTS:
P7 điểm uốn **40,0%** (M5; dải 33,8–40,0%); FSTS = d3b+d3c cho P7/P8/P9, d3c cho P3/P5;
P6 I²=62,4%; P8 β=−1,339; P9 N thô vs N phân tích ghi rõ.
