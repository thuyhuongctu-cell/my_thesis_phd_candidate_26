# Sàng lọc tài liệu PDF cho meta-analysis P6 — 2026-06-24

> Mục đích: phân loại ~16 tài liệu NCS tải lên thành (A) **ứng viên study sơ cấp** để thêm
> vào meta-analysis ba cấp của P6 (hiện **k = 238**, r̄ = 0,074, I² = 62,4 %, Q_M = 17,35,
> df = 4, p = ,002), (B) **chỉ dùng lập luận / tam giác hóa** (đối chiếu ngoài), hay (C)
> **không đưa vào**. Tài liệu này KHÔNG tự ý thêm study vào P6 — mọi việc thêm phải qua
> bước kiểm tra trùng lặp với k = 238 và quy đổi về hệ số tương quan r. Số liệu trích từ
> bản digest của 4 agent đọc song song; không có con số tự chế.

## Tiêu chí đưa vào P6 (nhắc lại)
1. **Đơn vị quan sát cấp doanh nghiệp** (firm-level), không phải cấp ngành/quốc gia.
2. Có **hiệu ứng quốc tế hóa ↔ hiệu quả** có thể **quy đổi về r** (báo cáo r, ρ Spearman,
   hoặc β chuẩn hóa + N đủ để chuyển đổi).
3. **Chưa nằm trong k = 238** (kiểm tra trùng nguồn/mẫu).
4. Là **study sơ cấp**, không phải meta-analysis (tránh đếm trùng hiệu ứng).

---

## A — Ứng viên STUDY SƠ CẤP để THÊM vào P6 (có điều kiện)

| Study | Mẫu / bối cảnh | Hiệu ứng báo cáo | Quy đổi r | Cảnh báo |
|---|---|---|---|---|
| **Vithessonthi & Racela 2016** | DN Đông Nam Á | DOI/FSTS → ROA ≈ **null** | Cần từ bảng hồi quy + N | Đặc tả tuyến tính; kiểm tra mẫu có nằm trong k=238 (WBES SE Asia) không |
| **Bukalska et al. 2025** | DN công nghệ cao Ba Lan | FSTS → ROA **+0,051 (p<,10)**; Spearman **ρ = 0,147** | ρ dùng trực tiếp như r | Đơn quốc gia, subset công nghệ cao; tuyến tính |

**Khuyến nghị quy trình trước khi thêm:**
1. **Kiểm tra trùng lặp** với 238 hiệu ứng hiện có (so nguồn dữ liệu, quốc gia, năm, mẫu).
   Vithessonthi & Racela dùng dữ liệu SE Asia — nếu chồng lấn WBES/Worldscope đã có trong
   P6 thì **loại** để tránh đếm trùng.
2. **Quy đổi về r**: Bukalska có ρ Spearman = 0,147 → dùng được ngay; Vithessonthi cần
   trích t/β + N để chuyển. Nếu không quy đổi được → chuyển sang nhóm B.
3. **Phân tích nhạy leave-in / leave-out**: thêm tối đa 2 hiệu ứng này (k → 240) rồi
   so r̄ và I². Nếu r̄ và I² gần như không đổi → ghi nhận là *robustness* (mẫu mở rộng
   không đổi kết luận). Nếu đổi đáng kể → báo cáo minh bạch, không ép vào.
4. Cả hai đều **tuyến tính** → chỉ bổ sung cho hiệu ứng *tổng thể* (overall r), KHÔNG dùng
   để hỗ trợ luận điểm phi tuyến (chữ U ngược) của luận án.

> Kết luận nhóm A: **đủ điều kiện sàng lọc**, nhưng **chỉ thêm sau** bước 1–2 ở trên.
> Lợi ích biên nhỏ (k=238 → tối đa 240); giá trị chính là cho thấy P6 *bao phủ được*
> bằng chứng mới nhất (2016, 2025) mà kết luận không đổi.

---

## B — CHỈ dùng LẬP LUẬN / tam giác hóa (meta-analysis ngoài, không phải study sơ cấp)

Đây đều là **meta-analysis** → không đưa hiệu ứng vào k=238 (sẽ đếm trùng), nhưng là
**mốc đối chiếu ngoài** mạnh cho phần Thảo luận P6 và Chương 4–5.

| Tài liệu | Mốc số | Vai trò lập luận |
|---|---|---|
| **Wu, Fan & Chen 2022** (EMNE) | Zr ≈ 0,017–0,077; I² > 95 % | **Cặp song sinh gần nhất** của P6: cùng EMNE, hiệu ứng nhỏ + dị biệt cực cao → P6 r̄=0,074/I²=62 % nằm cùng "vùng" nhưng I² thấp hơn (do mô hình 3 cấp) |
| **Kirca et al. 2010 (AMJ)** | r ≈ 0,09–0,19 | **Mốc ngoài mạnh nhất** cho quan hệ đa quốc gia–hiệu quả; định vị r̄ của P6 ở cận dưới |
| **Schulze et al. 2016** (Chindia) | r ≈ 0,12 | Mốc trực tiếp cho **Trung Quốc + Ấn Độ** — đối chiếu với mẫu châu Á của luận án |
| **Debicki et al. 2020** (DN gia đình) | r = 0,15; điều tiết *cường độ xuất khẩu làm yếu đi* | Hỗ trợ luận điểm "biên tham gia vs cường độ" (mục 4/Addendum VN) |
| **Beugelsdijk et al. 2018** (khoảng cách văn hóa) | — | Điều kiện biên (boundary condition) cho dị biệt theo thể chế/văn hóa |
| Yang & Driffield; Ruigrok & Wagner; JKM/Fan 2024; innovation–export; PIS speed inverted-U | — | Tam giác hóa bổ trợ: hình dạng phi tuyến, tốc độ quốc tế hóa, kênh đổi mới–xuất khẩu |

**Cách dùng trong luận án:** chèn các mốc r của Kirca (0,09–0,19), Schulze (0,12),
Wu-Fan-Chen (Zr 0,017–0,077) vào câu định vị r̄ = 0,074 của P6 ("nằm ở cận dưới của dải
meta-analysis quốc tế, nhất quán với mẫu EMNE châu Á dị biệt cao"). Debicki dùng ở chỗ
lập luận biên tham gia (Ch5 §5.1.7). KHÔNG cộng các hiệu ứng này vào k.

---

## C — KHÔNG đưa vào

| Tài liệu | Lý do |
|---|---|
| **Freixanet & Federo 2022** | Phương pháp **fsQCA** (set-theoretic), không có effect size quy đổi về r → không tương thích meta-analysis |

---

## Checklist hành động cho NCS
- [ ] Chạy **kiểm tra trùng lặp** Vithessonthi & Racela 2016 + Bukalska et al. 2025 với
      238 hiệu ứng hiện có (nguồn/quốc gia/năm/mẫu).
- [ ] **Quy đổi r**: Bukalska ρ=0,147 → r trực tiếp; Vithessonthi → trích t/β + N rồi chuyển.
- [ ] Nếu cả hai qua được: chạy **leave-in/leave-out** (k=238 → ≤240), báo cáo Δr̄, ΔI².
- [ ] Nếu không qua quy đổi/trùng lặp: **hạ xuống nhóm B** (chỉ lập luận).
- [ ] Chèn mốc đối chiếu nhóm B (Kirca, Schulze, Wu-Fan-Chen, Debicki) vào Thảo luận P6 +
      Ch4–5 ở các vị trí định vị r̄ và lập luận biên tham gia.
- [ ] **Không** dùng nhóm A (tuyến tính) để hỗ trợ luận điểm phi tuyến.

> Lưu ý liêm chính: tài liệu này chỉ *khuyến nghị* — k=238 và r̄=0,074/I²=62,4 % chỉ thay đổi
> sau khi chạy thực bước leave-in/leave-out, không bao giờ chỉnh số bằng tay.
