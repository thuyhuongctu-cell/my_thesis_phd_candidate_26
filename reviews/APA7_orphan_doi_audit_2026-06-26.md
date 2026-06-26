# APA7 Audit — Tham chiếu mồ côi (orphan) + DOI

**Ngày:** 2026-06-26 · **Phạm vi:** `thesis/04_references_apa7.md` (303 mục) đối chiếu toàn bộ corpus luận án.
**Công cụ:** đối sánh (họ tác giả thứ nhất + năm) accent-folded; corpus gồm 5 chương + phụ lục A/B/C + front-matter + bản tiếng Anh + CĐ1/CĐ2 + bảng nghiên cứu gốc P6 (`p6_primary_studies_apa7.md`, `p6_study_database_coded.md`).
**Tính chất:** báo cáo *cố vấn* — danh sách để NCS rà *cite-or-remove*, không tự ý xóa/sửa nội dung.

---

## 1. Tổng quan

| Nhóm | Số | Diễn giải |
|---|---:|---|
| Trích dẫn bình thường | ~178 | OK |
| Nghiên cứu gốc meta-analysis P6 | ~95 | **Đúng chuẩn** — nằm trong danh mục, trích trong bảng nghiên cứu, KHÔNG phải lỗi |
| **Orphan thật (không xuất hiện ở đâu)** | **27** | Cần *cite-or-remove* (xem §3) |
| Year-off (nhiễu — cùng họ, khác bài) | 6 | Phần lớn noise (Liu/Zhang/Tran cùng họ, khác tác giả); bỏ qua |

**Đã xử lý trong đợt này (2 mục, không còn mồ côi):**
- **Johanson & Vahlne (2009)** — trích ở Ch2 nhưng thiếu mục → đã **thêm vào danh mục** (commit `3702c35`).
- **Sasabuchi (1980)** và **MacKinnon & Webb (2017)** — phương pháp *thực sự được dùng* (kiểm định U Sasabuchi; wild-cluster bootstrap cụm-nhỏ cho SIDS) nhưng chưa trích đích danh → đã **bổ sung trích dẫn** ở Ch3 §3 và Ch4 §4.7.

---

## 2. DOI

- **Offline:** 244 DOI — **0 trùng lặp**, **0 malformed/empty-suffix**. Cấu trúc sạch.
- **Online (Crossref):** **BỊ CHẶN** trong container (network policy 403). Bước này — bắt DOI *trỏ nhầm bài* — phải chạy trên máy có mạng:
  ```
  python3 scripts/verify_dois.py        # → reviews/doi_verification_report.md
  ```

---

## 3. Danh sách 27 orphan thật (cite-or-remove)

### A. Phương pháp meta-analysis / thống kê (10) — thường thuộc bản thảo P6; cân nhắc giữ trong danh mục hợp nhất hoặc trích ở Ch3 nếu dùng
- Cooper, H. (2010). *Research synthesis and meta-analysis* (4th ed.). Sage.
- Hedges, L. V., & Olkin, I. (1985). *Statistical methods for meta-analysis*. Academic Press.
- Rosenthal, R. (1991). *Meta-analytic procedures for social research* (rev. ed.). Sage.
- Rosenthal, R. (1994). Parametric measures of effect size. In *The handbook of research synthesis*. Sage.
- Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models* (2nd ed.). Sage.
- Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression approximations… *Research Synthesis Methods, 5*(1).
- Suurmond, R., van Rhee, H., & Hak, T. (2017). Meta-Essentials… *Research Synthesis Methods, 8*(4).
- Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *JSS, 36*(3).
- Lakens, D., Scheel, A. M., & Isager, P. M. (2018). Equivalence testing… *AMPPS, 1*(2).
- Landis, J. R., & Koch, G. G. (1977). Observer agreement for categorical data (kappa/ICR). *Biometrics, 33*(1).

### B. Báo cáo WB/IMF — bối cảnh số/AI/tài chính (8)
- Abreha, K., & Lopez Acevedo, G. (2024). *Trade restructuring* (WB PRWP 10955).
- Banerjee, A. V., & Duflo, E. (2014). Do firms want to borrow more? *Review of Economic Studies, 81*(2).
- Boeddu, G., et al. (2025). *AI for Financial Sector Supervision (EMDE)*. World Bank.
- Buchhave, H., et al. (2026). *Care for growth: industrial jobs for women in Viet Nam*. World Bank & Australian Aid.
- Cazzaniga, M., et al. (2024). Gen-AI and the future of work. *IMF SDN/2024/001*.
- Chodorow-Reich, G., et al. (2020). India's demonetization. *QJE, 135*(1).
- Geginat, C., & Ramalho, R. (2015). *Electricity connections and firm performance* (WB PRWP 7460).
- Sahay, R., et al. (2020). *The promise of fintech* (IMF DP/2020/09).

### C. Bài thực nghiệm IB / lý thuyết (9)
- Al-Najjar, B., Salama, A., & Abed, A. (2025). Gender & cultural diversity on boards… *IJHRM, 36*(13).
- Anil, K., & Misra, A. (2022). AI in P2P lending in India. *IJOEM, 17*(4).
- Bello, D. C., & Kostova, T. (2012). From the editors: high-impact IB research. *JIBS, 43*(6).
- Falahat, M., et al. (2020). SMEs internationalization… *Technological Forecasting & Social Change, 152*.
- Gallegos Mardones, J., & Ibáñez, M. J. (2025). Women in top management & internationalization. *SAGE Open, 15*(2).
- Jacquemin, A. P., & Berry, C. H. (1979). Entropy measure of diversification. *J. Industrial Economics, 27*(4).
- Kraus, S., et al. (2022). Literature reviews as independent studies. *Review of Managerial Science, 16*(8).
- Leung, T., & Sharma, P. (2021). R&D intensity vs R&D internationalization. *J. Business Research, 131*.
- Malerba, F., & Orsenigo, L. (1995). Schumpeterian patterns of innovation. *Cambridge J. Economics, 19*(1).

---

## 4. Khuyến nghị

1. **Nhóm A (method):** nếu các phương pháp/khái niệm này được dùng trong bản thảo P6 và NCS muốn một danh mục hợp nhất, có thể **giữ**; nếu theo APA chặt cho riêng luận án, **trích đích danh** ở Ch3 (nơi mô tả meta-analysis) hoặc **bỏ**.
2. **Nhóm B & C:** rà từng mục — hoặc bổ sung 1 câu trích dẫn ở chỗ phù hợp (Ch1 bối cảnh AI/số; Ch2 tổng quan; Ch5 hàm ý), hoặc **bỏ khỏi danh mục** nếu không còn dùng.
3. **DOI online:** chạy `scripts/verify_dois.py` trên máy có mạng để đóng nốt khâu kiểm tra DOI trỏ đúng bài.

> Ghi chú: MacKinnon & White (1985) — HC covariance — sau khi thêm "MacKinnon và Webb (2017)" thì họ "MacKinnon" đã xuất hiện trong văn; mục 1985 vẫn nên được trích đích danh ở chỗ mô tả sai số chuẩn vững HC1 (Ch3) hoặc bỏ nếu trùng vai trò với Long & Ervin (2000)/White (1980) đã trích.
