# Báo cáo Peer Review — Chuyên đề Tiến sĩ Số 1 (CĐ1)

**Bản thảo:** "Thực trạng về hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á" · Đỗ Thùy Hương · HD: TS. Nguyễn Minh Cảnh
**Ngày review:** 2026-06-10 · **Chế độ:** full (5 reviewers + Editorial Decision) · **Skill:** academic-paper-reviewer v1.10
**File:** `chuyen_de/cd1/00_cd1_ctu_final_vi.md` (1.042 dòng) · **Read-only** (không chỉnh bản thảo)

> ⚠️ Lưu ý phạm vi: đây là **review học thuật** (cấu trúc/lập luận/nhất quán/citation). Số liệu CĐ1 vs luận án (47 nền/101.185 ↔ 49 nền/91.982) đã được xác minh là *hai bản khóa dữ liệu hợp lệ* trong `THESIS_CHUYENDE_DATA_INTEGRITY_2026-06-10.md`. Review này phát hiện thêm các mâu thuẫn **NỘI BỘ CĐ1** (giữa các bảng trong cùng chuyên đề) — đây là vấn đề mới, khác.

---

## Phase 0 — Phân tích lĩnh vực & cấu hình hội đồng
- **Lĩnh vực chính:** Kinh doanh quốc tế (IB) — quan hệ quốc tế hóa–hiệu quả; **phụ:** Kinh tế phát triển/thể chế.
- **Paradigm:** thực chứng, mô tả–chẩn đoán (descriptive-diagnostic); WBES microdata, không mô hình nhân quả.
- **Loại:** chuyên đề tiến sĩ (foundation cho luận án + CĐ2); độ chín: **bản thảo nâng cao**.
- **Chuẩn:** hội đồng chấm chuyên đề CTU + định hướng Scopus/WoS (vì kế thừa vào paper).

**Hội đồng (5):** EIC (IB landscape/WBES) · R1 Phương pháp (thống kê mô tả đa quốc gia, hài hòa schema) · R2 Lĩnh vực (IB thể chế, meta-analysis I-P) · R3 Liên ngành (kinh tế phát triển/SIDS) · Devil's Advocate.

---

## 🟥 PHÁT HIỆN HỘI TỤ (CRITICAL — cả hội đồng đồng thuận): bảng số liệu KHÔNG khớp nhau

Đây là vấn đề **nghiêm trọng nhất** — các bảng trong cùng CĐ1 đưa ra số doanh nghiệp theo nhóm ICRV **mâu thuẫn nhau**, hội đồng chấm sẽ bắt ngay.

### C1. n_firms theo nhóm ICRV: Bảng 2.3.2.1 (thân bài) ≠ Bảng A.1 (phụ lục) — cùng pool 101.185
| Nhóm | Bảng 2.3.2.1 (dòng 418-424) | Bảng A.1 (dòng 1017-1023) | Lệch |
|---|---|---|---|
| I Advanced-innov | ~4.220 | ~8.200 | **×1,9** |
| II Advanced-resource | ~1.932 | ~4.100 | **×2,1** |
| III Upper-middle | ~16.693 | ~12.300 | −4.393 |
| IV Emerging | ~47.803 | ~21.000 | **−26.803** |
| V Frontier | ~28.678 | ~53.200 | **+24.522** |
| VI SIDS | ~1.371 | ~2.385 | **+1.014** |
| **Tổng** | 101.185 | 101.185 | (cùng tổng, khác hoàn toàn phá) |
→ **Hai bảng cùng tả pool 101.185 nhưng phá theo nhóm hoàn toàn khác.** Bắt buộc thống nhất (Bảng A.1 dường như là bản nháp cũ — IV/V đảo ngược bất hợp lý: Frontier 53.200 > Emerging 21.000 mâu thuẫn mọi bảng khác).

### C2. Số nước "châu Á thuần": text ghi **41**, nhưng 5 nhóm chính cộng lại = **40**
§2.1.2/2.1.3/2.1.5 nói "41 nước châu Á thuần". Nhưng I(5)+II(5)+III(6)+IV(7)+V(17) = **40**. Và 40+7 SIDS = 47 ✓ (khớp tổng). → "**41**" sai, phải là **40**. (Nếu giữ 41 thì tổng thành 48 ≠ 47.)

### C3. SIDS có 3 con số khác nhau
- **1.371** (pool — §2.1.3, 2.3.2, 2.3.7, Bảng 2.3.2.1) — khớp dữ liệu thật 7 Pacific.
- **1.097** (analytic sau lọc missing — Bảng 2.3.3.1, có giải thích) — OK.
- **2.385** (Bảng A.1 phụ lục) — **mâu thuẫn**, không giải thích được.
- Thêm: §2.1.4(6) "9/~52 SIDS theo UNCTAD" — số "9" gây nhầm (CĐ1 dùng 7 Pacific xuyên suốt); làm rõ "9" là gì hoặc sửa.

### C4. Phá thế hệ schema có 2 bộ số, đều cộng = 101.185
- §2.1.3: PICS3 **14.335** / Standardized **25.046** / BREADY **61.804**.
- §2.2 + Hình 2.3.3.1 + Phụ lục: PICS3 **14.171** / Standardized **24.564** / BREADY **62.450**.
→ Chọn 1 bộ chuẩn, sửa bộ kia.

### C5. Tổng Emerging: 47.803 (Bảng 2.3.6.4, đa số bảng) vs **42.278** (§2.3.7.5 "Tổng hợp Emerging Asia n=42.278")
Hai tổng Emerging khác nhau ~5.500. Nếu 42.278 loại Mongolia/wave nào đó thì phải nêu rõ.

---

## 🟧 R1 — Reviewer Phương pháp (MAJOR)

1. **(MAJOR)** Bảng 2.3.8.1 ghi "Pearson … HC1 robust SE" — **hệ số tương quan Pearson không dùng HC1** (HC1 là cho SE hồi quy). Sửa nhãn (bỏ HC1 hoặc đổi thành hồi quy đơn biến có HC1).
2. **(MAJOR)** Claim "loại ICT → hệ số DAI −0,129 **biến mất**" (§2.3.4.3) là trụ cột lập luận "Nghịch lý bão hòa số" nhưng **không có con số hậu-loại-trừ**. Cần báo cáo hệ số sau khi loại ICT (vd −0,129 → −0,0xx, n.s.).
3. **(MINOR)** Phân tán analytic (Bảng 2.3.3.1): Frontier rớt 28.678→18.877 (−35%) trong khi Emerging chỉ rớt 47.803→45.388 (−5%). Chênh lệch tỷ lệ missing lớn bất thường — cần 1 câu giải thích (vì sao Frontier mất nhiều biến năng suất hơn).
4. **(MINOR)** "winsorize 1/99 trong cụm quốc gia×năm" tốt, nhưng với cụm SIDS n nhỏ (Kiribati 150) winsorize 1/99 gần như vô hiệu — nêu rõ ngưỡng tối thiểu cụm.

## 🟧 R2 — Reviewer Lĩnh vực (MAJOR — citation/APA7)

1. **(MAJOR) Citation ≠ reference (lỗi APA7 hội đồng dễ bắt):**
   - §2.3.1.3 trích "**Wu, Fan & Chen (2022)**" (meta-analysis) nhưng reference list chỉ có "**Wu, J., Li, S., & Selover, D. D. (2022)**" (FDI vs trade) — **khác tác giả, khác chủ đề**. Hoặc sai tên, hoặc thiếu 1 reference.
   - "**Arte & Larimo (2022)**" (dòng 254) trích in-text nhưng **không có** trong reference list.
   - Đỗ & Phan (2026) trích với **nhiều venue** in-text: "VEFR" (dòng 39, 199), "JABS, JFAR, MIR under review" (dòng 441), "JFAR" (dòng 688) — nhưng reference list chỉ 1 entry "JABS (under review)". Phải khớp 1-1 (mỗi venue = 1 entry, hoặc thống nhất 1 venue).
2. **(MINOR)** Contractor et al. (2003) trong reference list — kiểm tra có được trích in-text không (nếu không → orphan reference, bỏ).
3. **(STRENGTH)** Khung 5 meta-analysis (Bausch&Krist, Kirca, Marano, Schwens, Wu) + 3 khung lý thuyết nền + điều kiện biên U-curve là phần lý luận **mạnh, mạch lạc**, đủ tầm chuyên đề tiến sĩ.

## 🟨 R3 — Reviewer Liên ngành (MINOR)

1. **(MINOR)** Singapore turning point mâu thuẫn: **~82%** (§2.3.1.6, Bảng 2.3.2.2) vs **~88,6%** (§2.3.7.1, KL1) — thống nhất (P4 dùng 88,6%).
2. **(STRENGTH)** Phát hiện **phân nhóm con Advanced** (innovation 1,03 vs resource 0,49) và **chi phí buộc phải quốc tế hóa** ở SIDS là đóng góp định hướng tốt, kết nối chặt sang CĐ2/luận án.
3. **(MINOR)** Hàm ý chính sách (§2.4.2) rất phong phú (8 điểm) nhưng một số đi xa khỏi "thực trạng" (vd PLMS/RSE lao động di chuyển) — cân nhắc gọn lại cho đúng phạm vi chuyên đề mô tả.

## 🟪 Devil's Advocate

1. **(MAJOR — phản biện lõi)** CĐ1 tuyên bố "**không thiết lập mô hình hồi quy nhân quả**" (§2.2) nhưng lại dùng nhiều **claim nhân quả** mượn từ component study: "TCI=0,179 nhân quả IV" (§2.4.2.1), "FSTS²×DAI=3,119 p=0,005" (§2.3.1.6, 2.3.8.3). → Phải **đóng khung nhất quán**: "theo nghiên cứu thành phần P3 Việt Nam / P4 Singapore" mỗi lần dùng, tránh người đọc hiểu CĐ1 tự ước lượng nhân quả.
2. **(MINOR)** "Fiji website 74,8% > Singapore 66,1%" được dùng làm bằng chứng nhảy vọt số/forced internationalization **nhiều lần** — nhưng chính CĐ1 lập luận Tier-1 (website) đã **bão hòa & vô nghĩa** ở Advanced. Dùng so sánh website thô để "gây ấn tượng" **tự mâu thuẫn** với luận điểm bão hòa Tier-1. Giữ làm minh họa tu từ thì OK, nhưng đừng nâng thành bằng chứng năng lực số.
3. **Quan sát (không lỗi):** dữ liệu 2025 (Kiribati/Nepal) còn rất mỏng (150/quốc gia, Nepal schema khác) — CĐ1 đã trung thực gắn cờ; tốt.

---

## 📋 EDITORIAL DECISION

**Quyết định: MAJOR REVISION** (về *nhất quán số liệu nội bộ* + *citation*, KHÔNG phải về nội dung khoa học).

**Lý do:** Nội dung khoa học, khung lý luận và đóng góp **vững, đủ tầm chuyên đề tiến sĩ** (EIC + R2 + R3 đồng thuận điểm mạnh). NHƯNG **5 mâu thuẫn số liệu nội bộ (C1–C5)** + **3 lỗi citation/APA7 (R2.1)** là loại lỗi hội đồng chấm bắt ngay và hạ điểm nặng. Devil's Advocate không nêu lỗi CRITICAL về lập luận lõi (chỉ cần đóng khung lại claim nhân quả) → không chặn Accept về mặt khoa học, nhưng số liệu phải sạch trước khi nộp.

### Revision Roadmap (ưu tiên)
| # | Mức | Việc | Vị trí |
|---|---|---|---|
| 1 | 🟥 | **Thống nhất n_firms theo nhóm ICRV** — chọn 1 bảng chuẩn (khuyến nghị Bảng 2.3.2.1 + Bảng 2.3.3.1 analytic), **sửa/bỏ Bảng A.1** | Bảng 2.3.2.1 ↔ A.1 |
| 2 | 🟥 | Sửa "41 nước châu Á" → **40** (5 nhóm chính = 40; 40+7=47) | §2.1.2, 2.1.3, 2.1.5 |
| 3 | 🟥 | Thống nhất **SIDS = 1.371 pool / 1.097 analytic**; sửa A.1 (2.385); làm rõ "9/52 SIDS" | §2.1.4(6), A.1 |
| 4 | 🟥 | Chọn 1 bộ số **schema generation** (14.335/25.046/61.804 **hoặc** 14.171/24.564/62.450) | §2.1.3 vs §2.2 |
| 5 | 🟧 | Thống nhất **tổng Emerging** (47.803 vs 42.278) | §2.3.7.5 |
| 6 | 🟧 | Sửa **citation**: Wu Fan&Chen↔Wu Li&Selover; thêm ref **Arte & Larimo (2022)**; khớp venue Đỗ&Phan (VEFR/JABS/JFAR/MIR) 1-1 với reference list | §2.3.1.3, 254, 441, refs |
| 7 | 🟧 | Bỏ nhãn "HC1" khỏi bảng tương quan Pearson; bổ sung hệ số DAI hậu-loại-ICT | Bảng 2.3.8.1, §2.3.4.3 |
| 8 | 🟨 | Thống nhất Singapore TP (82% → **88,6%**); đóng khung lại mọi claim nhân quả là "theo P3/P4" | §2.3.1.6, 2.4.2.1 |

**Ước lượng:** 1 vòng revision tập trung (số liệu + citation) là đủ → sau đó **sẵn sàng nộp/bảo vệ**. Nội dung không cần viết lại.

**So với review cũ (~65%):** nội dung/cấu trúc đã tốt hơn nhiều (front matter, lý luận, 7 tiểu cảnh đầy đủ); điểm nghẽn còn lại **dồn vào nhất quán bảng số + citation** — sửa cơ học, không phải sửa tư duy.
