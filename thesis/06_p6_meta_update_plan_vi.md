# Kế hoạch triển khai P6 — Meta-Analytic Regression Analysis (MARA) update 1982–2026

> **NCS**: Đỗ Thùy Hương · **HD**: PGS.TS. Phan Anh Tú
>
> **Phiên bản 1.0 (10/05/2026)** — Kế hoạch triển khai 14 tuần cho P6 UPDATED. Tham chiếu toàn văn bản thảo luận án tại `thesis/21_p6_meta_vi.md` và so sánh ICBEF 2025 vs UPDATED tại tài liệu nội bộ NCS.
>
> **Lineage**: Phân tích gốc (18/07/2023, MetaEssentials 1.5) → Tiểu luận tổng quan (31/12/2024) → ICBEF 2025 ($k=113$, $r=0.07$, $I^2=87.92\%$) → **P6 UPDATED cho luận án** (three-level MARA + 3 moderator mới)

---

## 1. Định vị và đóng góp chính

P6 UPDATED **không phải** là bản tái bản của ICBEF 2025 mà là nâng cấp methodological + theoretical trên ba trục:

| Trục | ICBEF 2025 | P6 UPDATED |
|---|---|---|
| **Phương pháp** | Random-effects pooled (DerSimonian-Laird) | **Three-level MARA** (Cheung, 2014; Van den Noortgate et al., 2013) |
| **Lý thuyết** | Tổng hợp 6 meta trước | **3 lý thuyết mới**: Capability–Institution Mismatch, Digital Paradox Lifecycle, ICRV 5-regime |
| **Thực nghiệm** | $k=113$, 2 moderators | **$k\approx130$**, 5 moderators (thêm cDAI, ICRV, DPL phase) |

---

## 2. Ưu tiên triển khai

| Ưu tiên | Công việc | Lý do |
|---|---|---|
| **P0 — Cao nhất** | Verify + recode 113 baseline + 17 new = ~130 với 3 moderator mới (ICRV, cDAI, DPL) | Đóng góp lý thuyết cốt lõi |
| **P1 — Trung bình** | Three-level MARA + consistency check với bản 2023 | Nâng cấp methodological |
| **P2 — Tùy điều kiện** | Backward citation scan + run 28 queries Consensus | Sau khi P0–P1 hoàn thành |

**Nguyên tắc**: P6 được đánh giá bởi **chất lượng coding 3 moderator mới**, không phải pool size thuần túy. $k=130$ với quality coding cho 3 moderator mới là publishable và có đóng góp đáng kể.

---

## 3. Ba khoảng trống nghiên cứu (P0 — cốt lõi)

### Gap 1: Country-level Digital Adoption (cDAI)

Chỉ số áp dụng số cấp quốc gia (World Bank Digital Adoption Index hoặc ITU Digital Development Index theo country-year) chưa từng được kiểm định meta-analytic như country-level moderator của quan hệ I→P.

**Mã hóa**: high/medium/low theo cDAI quartile + continuous score theo country-year.

### Gap 2: ICRV 5-regime (Asian Institutional Heterogeneity)

Phân loại 5 nhóm thể chế theo WGI Rule of Law với thresholds $+0.80$ và $-0.50$:
- **Regime I**: WGI > $+0.80$ (Advanced)
- **Regime II**: $0 \leq$ WGI $\leq +0.80$ (Upper-middle)
- **Regime III**: $-0.50 <$ WGI $< 0$ (Emerging)
- **SIDS**: Quốc đảo Thái Bình Dương (boundary case)
- **Frontier**: WGI $< -0.50$

Marano et al. (2016) chỉ phân tách 6 nhóm tổng quát; chưa có meta nào áp dụng 5-regime cho riêng châu Á + Pacific.

### Gap 3: Digital Paradox Lifecycle (DPL)

Mã hóa study theo mốc 2009 inflection point — năm xuất hiện productivity J-curve của digital technology (Brynjolfsson et al., 2021; David, 1990):
- **Precede** (data trước 2009): chưa có hiệu ứng số rõ
- **Span** (data 2005–2014): pha chuyển đổi
- **Follow** (data sau 2014): hiệu ứng số đầy đủ

---

## 4. Lộ trình 14 tuần

### Tuần 1–2: Audit + OSF Preregistration

- [ ] Verify 113 baseline studies trong MetaEssentials xlsx — kiểm tra DOI, complete coding
- [ ] Reconcile với 46-study new database (`data/study_database.json`)
- [ ] Lên danh sách ~130 deliverable studies (90 đã có + 30 cần re-extract + 10 full text)
- [ ] Điền `P6_OSF_Preregistration_Template.md` (RQs, hypotheses, eligibility, search strategy, coding protocol, analysis plan)
- [ ] **Submit OSF preregistration** — lock hypotheses trước khi extract effect sizes mới
- [ ] Setup R environment: `metafor`, `dplyr`, `ggplot2`
- [ ] Tải WGI Rule of Law data (World Bank) + ITU DDI/WB DAI cho cDAI

### Tuần 3–6: Recode 3 Moderator Mới (~130 studies)

- [ ] **Batch 1** (tuần 3, 40 studies): ICRV regime + cDAI level + DPL phase — coder chính
- [ ] **Batch 2** (tuần 4, 40 studies): tương tự batch 1
- [ ] **Batch 3** (tuần 5, 40 studies): tương tự + re-extract 10 studies khó
- [ ] **Batch 4** (tuần 6): verify hoàn thiện, final check 4 fields: effect_size, ICRV, cDAI, DPL
- [ ] Double-code 20% subset (26 studies), tính Cohen's $\kappa \geq 0.7$ — resolve disagreements
- [ ] Update `data/study_database.json` với 3 moderator fields mới

### Tuần 7–8: Convert MetaEssentials → `metafor`

- [ ] Import database vào R, tính Fisher's $z$ cho từng effect size
- [ ] Setup `rma.mv()` cho three-level model
- [ ] Re-run baseline pooled effect — so sánh consistency với bản 2023 ($r=0.07$, $I^2=87.92\%$)
- [ ] Estimate nested structure: $\sigma^2_{level2}$ (within-study), $\sigma^2_{level3}$ (between-study)
- [ ] Forest plot tổng hợp baseline

### Tuần 9–10: Moderator Analysis + Robustness

- [ ] ICRV regime subgroup (5 regimes) — pooled effect trong từng regime
- [ ] cDAI moderation (categorical: high/med/low + continuous score)
- [ ] DPL phase comparison (precede/span/follow)
- [ ] Egger's test, Begg-Mazumdar, trim-and-fill, fail-safe N, funnel plot
- [ ] Leave-one-out sensitivity; Asian-only subset; alternative ICRV thresholds ($+0.5/-0.3$)
- [ ] REML vs DerSimonian-Laird estimator comparison

### Tuần 11–14: Viết Manuscript

- [ ] **Tuần 11**: Introduction (differentiation từ ICBEF 2025 + 3 gaps) + Method (PRISMA flow, three-level MARA, coding protocol)
- [ ] **Tuần 12**: Results (forest plot, moderator tables, interaction plots) + publication bias
- [ ] **Tuần 13**: Discussion (đối thoại 6 meta trước + cDAI/ICRV/DPL interpretation)
- [ ] **Tuần 14**: Conclusion + verify citations + fill cover letter + abstract + OSF deviation log

---

## 5. Risks và Mitigation

| Risk | Mitigation |
|---|---|
| Pool < $k=130$ | Quality > quantity; chấp nhận $k=113$ baseline nếu cần |
| Inconsistency với bản 2023 | Document trong Appendix C; giải thích estimator + data updates |
| Three-level MARA không hội tụ | Fallback two-level random-effects với cluster-robust SE |
| Inter-coder reliability thấp | Double-code 20%, target $\kappa \geq 0.7$; resolve disagreements iteratively |
| cDAI proxy variation | ITU DDI + WB DAI làm dual proxy; rationale minh bạch |
| ICRV thresholds cần biện minh | Robustness với alternative thresholds ($+0.5/-0.3$ vs $+0.8/-0.5$) |
| Reverse causality | Coding study design (cross-section vs panel) + lag structure |

---

## 6. Kết nối các file luận án

| File | Vai trò |
|---|---|
| `thesis/21_p6_meta_vi.md` | Bản thảo manuscript P6 UPDATED đầy đủ |
| `thesis/02_theoretical_framework_vi.md` | P6 cung cấp evidence cho H1, H6 |
| `thesis/03_methodology_vi.md` | Mục 4.1 chi tiết three-level MARA |
| `thesis/04_references_apa7.md` | Tất cả reference APA 7th |
| `thesis/07_p7_capstone_design_vi.md` | P6 (synthesis) + P7 (empirical) → Ch.4 |
| `thesis/17_cd2_part1_intro_theory_vi.md` | P6 được tham chiếu trong §1.4 |

---

*Kế hoạch v1.0 (10/05/2026). NCS: Đỗ Thùy Hương. HD: PGS.TS. Phan Anh Tú. Cần Thơ.*
