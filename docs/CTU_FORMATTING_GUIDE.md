# CTU PhD Dissertation — Formatting Guide

> Áp dụng cho luận án tiến sĩ tại **Trường Đại học Cần Thơ (CTU)**.
> **Nguồn chính thức**: Quyết định số **1799/QĐ-ĐHCT ngày 18/6/2021** của Hiệu trưởng Trường Đại học Cần Thơ — "Hướng dẫn viết và trình bày Luận văn Thạc sĩ và Luận án Tiến sĩ".
>
> Cập nhật cuối: 2026-06-04 sau khi đọc đầy đủ tài liệu QĐ 1799 do NCS share.

---

## 1. Quy cách trình bày chung (LATS — §2.2.1)

| Mục | Quy chuẩn QĐ 1799 | Trong repo |
|---|---|:-:|
| Khổ giấy | A4 (210 × 297 mm) | ✅ |
| Phần mềm | Microsoft Word | ✅ pandoc → docx |
| Mực in | Đen (trừ hình ảnh) | ✅ |
| Hướng giấy | Portrait (trừ hình/bảng lớn → landscape) | ✅ |
| **Font** | **Times New Roman** (Unicode TCVN 6909:2001) | ✅ |
| **Cỡ chữ body** | **13 pt** | ✅ |
| **Cách dòng (line spacing)** | **1.2** (KHÔNG phải 1.5) | ✅ `ctu_thesis_strict.docx` |
| Mật độ chữ | Bình thường (không nén/giãn) | ✅ |
| **Footnotes** | **Cỡ 10 pt** | ⚠ cần verify |
| **Cỡ chữ bảng/hình** (caption + nội dung) | **12 pt** (đặc biệt 11pt) | ⚠ cần verify |
| In đậm | Các mục, tiểu mục | ✅ |

---

## 2. Lề trang (§2.2.2)

| Lề | Quy chuẩn |
|---|:-:|
| **Lề trái** (đóng bìa) | **3.0 cm** |
| Lề trên | 2.0 cm |
| Lề dưới | 2.0 cm |
| Lề phải | 2.0 cm |
| **Tab** | **1.0 cm** |
| Header/footer | 1.0 cm |

---

## 3. Cách dòng + thụt đầu dòng (§2.2.3)

| Trường hợp | Cách dòng |
|---|:-:|
| **Mặc định** | **1.2** |
| Tài liệu tham khảo | 1.0 |
| Bảng và hình | 1.0 |
| Phụ lục | 1.0 |
| Ghi chú cho bảng | 1.0 |
| Giữa tiểu mục và đoạn phía trên | **before 6pt, after 0** |
| Liệt kê nhiều dòng liên tục | before 0, after 0, spacing 1.2 |
| **Thụt đầu dòng** (tiểu mục đánh số + đoạn văn) | **1.0 cm** (tab = 1cm) |

---

## 4. Đánh số trang (§2.2.4)

- Vị trí: **giữa trang, phía dưới**
- Cỡ + font: 13pt Times New Roman (giống nội dung)
- **Phần mở đầu** (mục lục, danh sách bảng/hình/từ viết tắt, lời cảm ơn): **chữ số La-mã thường** (i, ii, iii, iv, v, ...)
- **KHÔNG đánh số** trang bìa và trang phụ bìa
- **Bắt đầu chữ số Ả Rập** (1, 2, 3, ...) từ Chương 1 đến hết phần Tài liệu tham khảo

---

## 5. Cách ghi mục, tiểu mục (§2.2.5)

- Đánh số theo cấp xuất hiện
- **Tối đa 3 cấp** (4 chữ số)
- Ví dụ: 4.1.2.1 = chương 4, cấp 1 (4.1), cấp 2 (4.1.2), cấp 3 (4.1.2.1)
- Phải có ít nhất 2 tiểu mục (không thể có 2.1.1 mà không có 2.1.2 tiếp)
- **KHÔNG có dấu chấm hoặc dấu hai chấm** sau mục/tiểu mục
- **KHÔNG đặt tiểu mục ở cuối trang**
- Dấu câu (`. , ; :`) nằm liền với từ cuối cùng + cách 1 space với từ kế tiếp
- Trong ngoặc: dấu ngoặc phải dính liền (không có khoảng trắng) với từ đầu/cuối

---

## 6. Bảng biểu, hình vẽ, phương trình (§2.2.6)

| Mục | Quy chuẩn |
|---|---|
| **Đánh số** | Theo chương: Hình 3.4 = hình thứ 4 của chương 3 |
| **Trích nguồn** | Bảng/hình từ nguồn khác phải trích dẫn đầy đủ (vd: nguồn Bộ Tài chính 1996) |
| **Caption bảng** | **TRÊN bảng** + canh lề trái |
| **Caption hình** | **DƯỚI hình** + canh giữa, KHÔNG in đậm/in nghiêng |
| **Cỡ caption** | **12 pt** |
| **Vị trí** | Đặt ngay sau text mô tả (KHÔNG đặt ngay sau mục/tiểu mục) |
| **Tên bảng/hình** | Mô tả nội dung đầy đủ; tránh "kết quả của thí nghiệm 1" |

### Bảng cụ thể (Phụ lục 7)

- Nội dung cột chữ → lề trái; nội dung cột số → lề phải
- Độ dày đường gạch ngang: **1pt**
- **Không tách giữa số và dấu** ± (đúng: `0,18±0,02`; sai: `0,18 ± 0,02`)
- **Không làm khung** cho bảng — chỉ gạch trên/dưới tiêu đề và cuối bảng

### Hình cụ thể (Phụ lục 8)

- Cân đối, center
- Dùng đậm/nhạt/texture thay vì màu (để in trắng đen)
- Độ dày line: 1.5–2pt
- Font: Times New Roman
- **Không đặt tựa cho hình** (vì đã có tên hình phía dưới)
- **Không làm khung** cho hình
- Subfigure: Hình 1a, 1b (không đặt số mới)
- 5 loại hình: line (xu hướng) · bar (so sánh) · line+bar (xu hướng tương quan) · scatter (phân bố) · pie (tỉ lệ %)

---

## 7. Trình bày tên các chương (§1.2.7 + Phụ lục 6)

- **Tiêu đề chương**: đặt đầu trang, **giữa dòng (center)**, **cỡ chữ 14 pt** in hoa in đậm
- Mục/tiểu mục đánh số theo số chương
- Tiểu mục chỉ đến cấp thứ 3; nhỏ hơn dùng chữ cái a, b, c

---

## 8. Công thức (§1.2.8)

- Đánh số theo chương: (2.1), (2.2), ...
- **Cỡ 12 pt**
- **Canh lề phải**

---

## 9. Trích dẫn + Tài liệu tham khảo APA (Phụ lục 9, đã cập nhật)

### Trích dẫn trong văn bản

| Trường hợp | Vd VN | Vd EN |
|---|---|---|
| 1 tác giả | (Nguyễn Văn A, 2020) hoặc Nguyễn Văn A (2020) | (Smith, 2019) hoặc Smith (2019) |
| 2 tác giả | (Nguyễn Văn A & Trần Thị B, 2019) | (Smith & Brown, 2019) |
| 3+ tác giả | (Nguyễn Văn A và *ctv.*, 1999) | (Michell *et al.*, 2017) |
| Nhiều nguồn 1 ý | (Smith, 1959; Thomson & Jones, 1982; Green, 1990) | sort theo thời gian |
| Cùng tác giả nhiều năm | Nguyễn Văn A (1996, 2001) hoặc Lê Văn C (2000a, 2000b) | |
| Chấp nhận xuất bản nhưng chưa in | Nguyễn Văn A và ctv. (đang in) | |
| Cơ quan/tổ chức | (Bộ Công thương, 2010) hoặc WHO (2015) | |
| Nguyên văn | (Obama, 2014, tr.97-98) | |

### Danh mục TLTK (hanging indent từ dòng 2)

**Sách**:
- VN: Tên tác giả. (Năm xuất bản). *Tên sách in nghiêng*. Nơi xuất bản: Nhà xuất bản.
- EN: Author(s). (Year). *Title of book*. Place of publication: Publisher.

**Bài báo tạp chí**:
- VN: Tên tác giả (Năm xuất bản). Tên bài báo. *Tên tạp chí, tập in nghiêng*(số), trang. DOI: xx.xxxxxxxxxx
- EN: Author(s). (Year). Title of paper. *Journal name, Volume* (Issue), page numbers. DOI: xx.xxxxxxxxxx
- **Sau DOI/URL KHÔNG có dấu chấm**

**Bài hội thảo**:
- Tên tác giả (Năm). Tên bài viết. *Tên kỷ yếu, nơi tổ chức, năm tổ chức in nghiêng* (tr. trang số). Nơi xuất bản: Nhà xuất bản.

**Luận văn/Luận án**:
- Tên tác giả. (Năm). *Tiêu đề luận văn/luận án in nghiêng* (Luận văn/Luận án, Cơ sở đào tạo, Địa điểm).

**Tài liệu internet**:
- Tên tác giả. (Năm). *Tên tài liệu in nghiêng*. Truy cập ngày/tháng/năm, từ http://...

### Tên tác giả trong TLTK

- VN: viết đầy đủ họ và tên (vd: Trương Văn Dũ)
- Nước ngoài: viết trước họ + viết tắt chữ đệm (vd: Vladimir Ilyich Lenin → Lenin, V.I.)
- Các tác giả: cách nhau bằng dấu phẩy, thêm `&` trước tác giả cuối

### Xếp thứ tự TLTK

- Alphabet theo TÊN tác giả (hoặc tác giả đứng đầu nếu nhiều)
- Cùng tác giả: theo chữ tiếp trong tên
- Cùng tác giả + năm khác: tăng dần năm
- Cùng tác giả + cùng năm: alphabet tên bài + thêm a, b, c sau năm
- Cùng cách ghi tác giả + cùng năm: theo tên bài viết

---

## 10. Cấu trúc 15 phần bắt buộc của LATS (§2.3)

| # | Phần | Đánh số trang |
|---|---|---|
| 1 | Trang bìa chính | (không số) |
| 2 | Trang phụ bìa | (không số) |
| 3 | Trang xác nhận của Hội đồng | i (La-mã) |
| 4 | Lời cảm ơn | ii |
| 5 | Trang tóm tắt tiếng Việt | iii |
| 6 | Trang tóm tắt tiếng Anh | iv |
| 7 | Trang cam đoan kết quả nghiên cứu | v |
| 8 | Mục lục | vi-... |
| 9 | Danh sách bảng | ... |
| 10 | Danh sách hình | ... |
| 11 | Danh mục từ viết tắt | ... |
| 12 | **Phần nội dung chính** (5 chương) | **1, 2, 3, ... Ả Rập** |
| 13 | Tài liệu tham khảo | ... |
| 14 | Danh mục các bài báo đã công bố | ... |
| 15 | Phụ lục | ... |

**Số trang tối thiểu nội dung chính: 100 trang** (không kể các phần khác).

---

## 11. Trang bìa chính LATS (Phụ lục 1b)

**Màu bìa**: **ĐỎ BORDEAUX** (bordeau). Chữ trên bìa cứng: **chữ nhũ màu vàng**, in hoa.

```
                 BỘ GIÁO DỤC VÀ ĐÀO TẠO        (cỡ 14, in đậm)
               TRƯỜNG ĐẠI HỌC CẦN THƠ          (cỡ 14, in đậm)


                       HỌ TÊN NCS              (cỡ 14, in đậm)


                  TÊN LUẬN ÁN TIẾN SĨ          (cỡ 20, in đậm)
              (in hoa, có thể nhiều dòng)


                    LUẬN ÁN TIẾN SĨ
                 NGÀNH ...........             (cỡ 14, in đậm)
                 MÃ SỐ ...........             (cỡ 14, in đậm)


                       NĂM ...                 (cỡ 14, in đậm, canh giữa)
```

### Gáy bìa (§2.3.1.1)

- Kiểu chữ in hoa đậm
- **Cỡ 14**
- Format: `Họ tên NCS – Luận án tiến sĩ – Năm thực hiện`

---

## 12. Trang phụ bìa LATS (Phụ lục 2b)

Giống trang bìa chính + thêm:
- **MÃ SỐ NCS** sau Họ tên
- **NGƯỜI HƯỚNG DẪN** (cỡ 13, in đậm) + tên các thầy hướng dẫn

---

## 13. Trang xác nhận của Hội đồng (Phụ lục 3b)

- Tiêu đề: **CHẤP THUẬN CỦA HỘI ĐỒNG** (cỡ 14)
- 7 chữ ký:
  - Thư ký (Ghi đầy đủ học hàm, học vị và họ tên)
  - 3 Ủy viên
  - 3 Phản biện (Phản biện 1, 2, 3)
  - Người hướng dẫn
  - Chủ tịch Hội đồng

---

## 14. Lời cam đoan (Phụ lục 10)

```
                    LỜI CAM ĐOAN
                    (cỡ chữ 14, in đậm, canh giữa)

   Tôi tên là [Họ tên], là NCS ngành ..., khóa 20xx. Tôi xin
cam đoan luận án này là công trình nghiên cứu khoa học thực sự
của bản thân tôi được sự hướng dẫn của [PGS.TS./TS. ...].

   Các thông tin được sử dụng tham khảo trong đề tài luận án
được thu thập từ các nguồn đáng tin cậy, đã được kiểm chứng,
được công bố rộng rãi và được tôi trích dẫn nguồn gốc rõ ràng
ở phần Danh mục Tài liệu tham khảo. Các kết quả nghiên cứu
được trình bày trong luận án này là do chính tôi thực hiện một
cách nghiêm túc, trung thực và không trùng lặp với các đề tài
khác đã được công bố trước đây.

   Tôi xin lấy danh dự và uy tín của bản thân để đảm bảo cho
lời cam đoan này.

                       Cần Thơ, ngày... tháng... năm...

Người hướng dẫn                              Tác giả thực hiện
   (ký tên)                                     (ký tên)

  Lê Văn X                                    Nguyễn Văn A
```

---

## 15. Trang Tóm tắt (Abstract) (§2.3.1.2)

- 1 trang A4
- 3 phần: (1) tiêu đề Tóm tắt, (2) nội dung 1-2 đoạn 300-500 từ, (3) từ khóa
- 4 ý bắt buộc trong nội dung:
  - (i) Giới thiệu chủ đề + mục tiêu
  - (ii) Phương pháp + số liệu chính + tính mới
  - (iii) Tóm lược kết quả + nhận định chính
  - (iv) Kết luận + đóng góp mới + đề xuất
- **Không cần trích dẫn TLTK**
- **Từ khóa: tối đa 6 từ**, không có "của", "và", không viết tắt

---

## 16. Mục lục (Phụ lục 5)

- Tiêu đề: **MỤC LỤC** (cỡ 14)
- Liệt kê tới tiểu mục **thứ 2** (hoặc thứ 3 nếu tính cả tiểu mục chương)
- Vd: 2.2.3 (3 chữ số) là tiểu mục thứ 2
- KHÔNG liệt kê tiểu mục có ≥ 4 chữ số
- **Phụ lục KHÔNG cần liệt kê chi tiết**

---

## 17. Quyển Tóm tắt LATS (Chương 3 + Phụ lục 4)

- **Kích thước A5**: 140×210 mm (A4 gấp đôi)
- **Cỡ chữ 11 pt** Times New Roman
- **Cách dòng 1.2**
- **Lề trên/dưới/phải: 1.5 cm; Lề trái: 2.0 cm**
- Trình bày tối đa **24 trang**, in trên 2 mặt
- **Màu bìa: đỏ bordeaux**
- 3 phần:
  - Bìa 1: nội dung LATS (thông tin định danh)
  - Bìa 2: CÔNG TRÌNH ĐƯỢC HOÀN THÀNH TẠI TRƯỜNG ĐẠI HỌC CẦN THƠ + Người hướng dẫn + Phản biện + nơi bảo vệ
  - Bìa 3: **DANH MỤC CÁC CÔNG TRÌNH ĐÃ CÔNG BỐ** (Tạp chí quốc tế / trong nước / Kỷ yếu / Đề tài)

---

## 18. Báo cáo PowerPoint (Phụ lục 12)

- **Thời gian LATS: 30 phút**
- 01 phút/slide (≈ 30 slides max)
- Tên báo cáo: cỡ ≥ 32pt (tốt 36-40)
- Nội dung: cỡ ≥ 24pt
- ≤ 8-10 dòng chữ/slide; ≤ 8-10 từ/dòng
- KHÔNG dùng chữ có chân (sans-serif preferred)
- Slides: tựa bài + cấu trúc (4-6 dòng) + nội dung + kết luận + cảm tạ

---

## 19. Template DOCX trong repo

| File | Line spacing | First-line indent | Heading 1 size | Theo QĐ 1799 |
|---|:-:|:-:|:-:|:-:|
| `templates/ctu_thesis_reference.docx` (legacy) | 1.2 ✅ | 0 ❌ | 13pt ❌ | ⚠ Phần |
| **`templates/ctu_thesis_strict.docx`** | **1.2 ✅** | **1 cm ✅** | **14pt ✅** | **✅ Đúng QĐ** |

**Build script**: `bash scripts/build_ctu_thesis_strict.sh` — rebuild 10 documents (5 chương + tóm tắt + 3 CĐ1 + CĐ2).

---

## 20. Còn cần làm

Sau khi đọc QĐ 1799 đầy đủ, các template còn thiếu trong repo:

| # | Item | Cần tạo |
|---|---|:-:|
| 1 | Trang bìa chính LATS (mẫu Phụ lục 1b) | ☐ |
| 2 | Trang phụ bìa LATS (Phụ lục 2b) | ☐ |
| 3 | Trang chấp thuận Hội đồng (Phụ lục 3b) | ☐ |
| 4 | Lời cam đoan template (Phụ lục 10) | ☐ |
| 5 | Bìa 1/2/3 Tóm tắt LATS (Phụ lục 4a/4b/4c) | ☐ |
| 6 | Verify caption bảng/hình cỡ 12pt trong tất cả DOCX | ☐ |
| 7 | Verify footnote cỡ 10pt | ☐ |
| 8 | Compile mục lục auto (TOC) | ☐ |
| 9 | Danh sách bảng + danh sách hình auto | ☐ |
| 10 | Danh mục từ viết tắt (sắp theo ABC) | ☐ |

Các DOCX template chuyên đề mà NCS đã upload (60fabcff, fe7b3dbd, b344ed53, a58b557c, ea0d2f1d) sẽ được đọc + áp dụng trong commit tiếp theo.
