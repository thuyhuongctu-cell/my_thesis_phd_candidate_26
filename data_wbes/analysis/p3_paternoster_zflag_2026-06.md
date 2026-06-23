# P3 Paternoster z-flag — verification (2026-06-19)

**Question.** Ch4 reports two Paternoster z near 3.35 — line 356 z=3,353 (turning-point shift,
2009 vs 2015) and line 374 z=3,35 (DAI-coefficient shift, 2009 vs 2015). Are these a copy-paste
duplication of one statistic, or two genuinely distinct tests?

**Method.** Independent recompute on the same prebuilt data the committed R replication uses
(`data_wbes/analysis/pooled_wbes_6waves.csv`, VNM subset; HC1 SE), reproducing the per-wave specs.

**Result.**

| Test | spec | 2009 | 2015 | Paternoster z (2009v2015) |
|---|---|---|---|---|
| TP shift (FSTS linear) | M2 exporters: lnLP~FSTSc+FSTScsq+ctrls | FSTSc −1.85 | FSTSc +1.21 | z_lin = −3.53 (p<.001) |
| TP shift (FSTS²) | (same) | FSTScsq +0.98 | FSTScsq −2.91 | z_sq = +3.22 (p=.001) |
| DAI shift | lnLP~FSTSc+FSTScsq+DAI+ctrls | DAI +0.70 | DAI +0.20 | z = +3.10 (p=.002) |

**Conclusion.**
1. The two reported values are **two genuinely different tests** (one on the FSTS quadratic
   coefficients, one on the DAI coefficient) that coincidentally both fall near 3.3 — **not a
   duplication error**. The thesis values (3,353 and 3,35) are legitimate and stand.
2. The recompute confirms the substantive claims independently: the turning-point shift 2009→2015
   is strongly significant (|z|≈3.2–3.5), and the DAI trajectory is non-monotonic (strong 2009 →
   dip 2015 → recover 2023) with a significant 2009→2015 shift.
3. **Spec caveat (for the candidate).** The thesis's reported DAI *coefficient magnitudes*
   (+0.175 in 2009 etc.) come from a different DAI specification than this simple replication
   (which yields +0.70 in 2009); the non-monotonic *pattern* and the *significance* of the shift
   reproduce, but the candidate should confirm the exact DAI model spec (standardised vs raw;
   nested moderation vs main effect) against her P3 Stata output so the printed coefficient
   magnitudes match the spec described in §4.5.6.

---

## Follow-up: §4.5.6 DAI per-wave coefficient spec (reviewed 2026-06-19)

**Finding.** The §4.5.6 DAI coefficients (DAI_z: 2009 +0.175, 2015 −0.044, 2023 +0.095,
pooled +0.078) are **not reproducible from the committed harmonised replication**
(`pooled_wbes_6waves.csv`, the data the committed P3 R script reads). Recomputes on that CSV:

| Spec (VNM, HC1) | 2009 | 2015 | 2023 | pooled |
|---|--:|--:|--:|--:|
| DAI_z only (lnLP~FSTSc+FSTScsq+DAI_z+ctrls) | +0.262 | +0.080 | +0.179 | +0.171 |
| M8 full (TCI_z+DAI_z+interactions) | +0.057 | +0.077 | +0.102 | — |
| **Thesis §4.5.6** | **+0.175** | **−0.044** | **+0.095** | **+0.078** |

**Diagnosis.** The thesis numbers derive from the **P3 manuscript Stata build**
(`p3/replication/do/01_build_vietnam.do` → `02_run_models.do`), which differs from the
committed harmonised CSV path in (a) FSTS = **direct exports only** (`d3c`) vs the pooled
`export_pct`; (b) **wave-specific** raw-`.dta` field mappings; (c) winsorise **within wave**;
(d) the DAI estimation sample (`dai_samp`). A direct raw-`.dta` port was attempted but the
per-wave PICS3/Standardized/BREADY schemas differ (the 2009 file lacks `b1_d`; the 2015 file
has a string-encoding issue), so the manuscript build cannot be reproduced here without the
original Stata environment.

**Status of the claim.** The **substantive** result — DAI follows a non-monotonic trajectory
(strong 2009 → weak/null 2015 → recovery 2023) — reproduces qualitatively across specs
(e.g., DAI_z-only: +0.262 → +0.080 → +0.179 still dips at 2015). Only the **exact magnitudes
and the 2015 sign** are build-dependent.

**Recommendation (candidate action, not auto-changed).** Reconcile the two paths so §4.5.6 is
reproducible for examiners/reviewers: either (a) re-run `01/02_*.do` in Stata, confirm the
printed coefficients, and commit the resulting `vietnam_*_analytic.dta` + an estimates table so
the numbers are auditable; or (b) if the harmonised CSV is the canonical path, update §4.5.6 to
the CSV-reproducible DAI_z values. No thesis number was changed pending the candidate's choice of
authoritative build.

---

## Real-.dta reproduction attempt (2026-06-19) — pattern reproduces, exact values do not

Built directly from the raw Vietnam WBES `.dta` (`scripts/p3_dai_reproduce.py`), porting
`01/02_*.do`. **Blocker found:** the committed `.do` denominates labour productivity by `b1_d`,
a field **absent** from the raw files; the WBES-standard worker field `l1` was substituted (the
P7 canonical also uses `l1`). With that substitution and the documented spec (FSTS=`d3c`,
winsorise-within-wave, `dai_samp`/`full_samp`):

| | 2009 | 2015 | 2023 | source model |
|---|--:|--:|--:|---|
| **M6 DAI-only** DAI_z | +0.273 | +0.045 (ns) | +0.153 | level |
| **M7 dual-direct** DAI_z | +0.201 | +0.014 (ns) | +0.128 | TCI_z+DAI_z (full_samp) |
| **Manuscript §4.5.6 / P3** | **+0.175** | **−0.044** | **+0.095** | M7 |
| M2 β₁ (FSTS) | +0.575 | +0.952 | +0.852 | quad |
| **Manuscript M2 β₁** | **1.045** | **1.159** | **0.962** | quad |

**Reading.** Including `TCI_z` (M7) pulls DAI_z down from +0.27 (M6) toward the manuscript's
+0.175 — confirming §4.5.6 reports the **M7 dual-direct** coefficient — and the
**sign/significance pattern reproduces** (2009 sig / 2015 ns / 2023 sig). However the **exact
magnitudes do not**: M2 β₁ is ~0.58 here vs 1.045 in the manuscript, a gap too large to be the
DAI control alone. The most likely cause is the **labour-productivity denominator** (`b1_d` in
the `.do` vs `l1` substituted here) and/or the FSTS-centering sample, which shift `lnLP` and the
FSTS slope and propagate through the whole M0–M8 web.

**Decision.** The thesis/P3-manuscript numbers were **not overwritten**: the candidate's figures
form a dense, internally consistent M0–M8 Stata web, and substituting an approximate Python build
that fails to match even M2 β₁ would introduce errors and break that consistency. The reproducible
pipeline is committed as an audit artifact showing the pattern holds.

**To finish option (a) faithfully, one input is needed from the candidate:** the exact
labour-productivity denominator used in the P3 Stata build (i.e., what `b1_d` maps to in the raw
WBES Vietnam files — `l1`? `l1`+temp? a derived employment variable?), plus confirmation of the
FSTS-centering sample. With that, the Python port can be aligned to reproduce the manuscript
numbers exactly, and §4.5.6 can be made fully auditable.

---

## RESOLUTION (2026-06-19, per author)

The P3 (and companion) papers have been run repeatedly in Stata; the manuscript figures are
**author-authoritative**. The §4.5.6 numbers are therefore **retained unchanged**. The committed
Python pipeline (`scripts/p3_dai_reproduce.py`) stands as a **pattern-confirming cross-check** —
it reproduces the DAI sign/significance trajectory (2009 sig / 2015 ns / 2023 sig) and shows that
including TCI_z (M7) pulls DAI_z toward the reported magnitude — not as a replacement for the
Stata estimates. For a fully auditable replication package the candidate need only (i) commit the
Stata estimates table + analytic `.dta`, and (ii) annotate that the `.do` `b1_d` denominator maps
to her labour-productivity worker field. No thesis/manuscript number is changed.

---

## Dò mẫu số `b1_d` bằng dữ liệu thực (2026-06-23)

Để tìm "input còn thiếu" (`b1_d` ánh xạ sang biến lao động nào), đã thử lại M2 β₁ với 7 mẫu số ứng
viên trên 3 đợt Vietnam thô (LP = ln(d2/DENOM), winsorize 1/99 trong đợt, M2 = FSTSc+FSTSc²+lnEmp+
firmage+foreign, HC1):

| DENOM | 2009 (tgt 1,045) | 2015 (tgt 1,159) | 2023 (tgt 0,962) |
|---|---|---|---|
| **l1** (baseline) | +0,575 | +0,952 | +0,852 |
| l2 | +0,358 | +0,981 | +0,849 |
| l6 | −0,931 | +0,423 | −1,729 |
| l5 | +4,279 | +0,934 | +7,774 |
| n2a | −0,034 | +1,017 | +0,409 |
| l10 | +0,681 | +1,182 | +1,183 |
| l1+l2 | +0,479 | +1,027 | +0,822 |

**Kết luận:** **không mẫu số đơn lẻ nào** tái lập đồng thời cả ba β₁ bản thảo. `l10` khớp 2015 nhưng
lệch 2009/2023; `l1` lệch đều ~+0,2…+0,5. → Gap **đa yếu tố** (mẫu số + mẫu định tâm FSTS/exporters +
winsorize/sample), không thể đảo ngược chỉ bằng đổi mẫu số. Xác nhận khuyến nghị: cần **bảng estimate
Stata + `.dta` phân tích** của NCS (Option a), hoặc chuyển §4.5.6 sang giá trị tái lập được từ CSV
(Option b). Số bản thảo **giữ nguyên** (author-authoritative, đã chốt 19/06).

---

## Giải mã `b1_d` bằng bảng hỏi + dữ liệu thô NCS gửi (2026-06-23)

NCS cung cấp dữ liệu thô đầy đủ (Vietnam 2009/2015/2023, ~287–355 biến) + **bảng hỏi chính thức**
(`ES_BEE_Questionnaire_Viet_Nam_2023.pdf`) + Implementation Report.

**Phát hiện 1 — `b1_d` = `l1`.** Không file nào có biến tên `b1_d` (chỉ có `b1`=tình trạng pháp lý,
`b1x`). Do-file `01_build_vietnam.do` dùng `ln(d2/b1_d)` với chú thích "// number of workers". Nhãn
biến trong dữ liệu xác nhận **`l1` = "L1. End of fiscal year, how many permanent, full-time
employees"** (cả 3 đợt). Vậy `b1_d` trong do-file **ánh xạ sang `l1`** (số lao động thường xuyên toàn
thời gian) — đây chính là "input còn thiếu".

**Phát hiện 2 — do-file KHÔNG winsorize lnLP.** `01_build_vietnam.do` không có lệnh winsor; script
`scripts/p3_dai_reproduce.py` đã **tự thêm** winsorize 1/99 (sai lệch so với do-file).

**Tái lập faithful (l1, KHÔNG winsor, FSTS=d3c định tâm trong đợt, base sample, controls
lnEmp+firmage(b4)+foreign(b2b≥10)) trên dữ liệu NCS gửi:**

| | 2009 | 2015 | 2023 |
|---|---|---|---|
| Python faithful (b1_d=l1) | +0,634 | +0,977 | +0,892 |
| **Manuscript M2 β₁** | **1,045** | **1,159** | **0,962** |

→ **2015 và 2023 tái lập hợp lý** (lệch ~0,15–0,18); **2009 vẫn lệch lớn (~0,41)**. Gap 2009 mang
tính **đặc thù đợt** — không phải do mẫu số (đã chốt l1) cũng không phải winsor. Nghi vấn còn lại cho
2009: biến `firmage` (b4 là *năm* hay *tuổi*?), tập biến kiểm soát đợt 2009, hoặc số manuscript 2009.

**Kết luận:** đã giải được mẫu số (`b1_d`=`l1`) và loại winsorize; 2/3 đợt khớp. Để khớp **đợt 2009**
chính xác, cần NCS xác nhận spec đợt 2009 (định nghĩa `firmage`/controls) hoặc dán bảng estimate Stata
2009. Số manuscript **giữ nguyên**.

---

## Truy đợt 2009 (2026-06-23, tiếp) — phát hiện lỗi `firmage = b4`

Đào sâu gap đợt 2009 (β₁ Python ~0,6 vs manuscript 1,045):

**Phát hiện 3 — `firmage = b4` là LỖI ánh xạ biến.** Trong cả ba file thô, **`b4` KHÔNG phải tuổi
doanh nghiệp** mà là nhãn *"Are any of the owners female?"* (giá trị 1/2). Do-file
`01_build_vietnam.do` gán `firmage = b4` → biến "tuổi DN" trong toàn bộ M0–M8 thực chất là **dummy
chủ sở hữu nữ**. Năm thành lập thật là **`b5`** ("Year Establishment Began Operation"). Đây là lỗi
spec trong do-file (không phải lỗi tái lập của em). *Cần NCS xác nhận:* trong bản dựng Stata của chị,
`b4` là tuổi hay "owners-female"? Nếu build dùng `b4` thì control "firm age" của P3 đang là biến giới
tính chủ sở hữu — ảnh hưởng nhãn/diễn giải toàn bộ P3 (số có thể vẫn đúng về mặt tính toán nhưng nhãn
biến sai).

**Đã thử mọi biến thể cho 2009** (β₁ mục tiêu 1,045):

| Biến thể (l1, FSTS=d3c định tâm, controls lnEmp+firmage+foreign) | 2009 | 2015 | 2023 |
|---|---|---|---|
| firmage = b4 (nguyên do-file), no winsor | +0,634 | +0,977 | +0,892 |
| firmage = surveyyear − b5 (tuổi đúng), no winsor | +0,595 | +1,008 | +0,834 |
| **Manuscript** | **1,045** | **1,159** | **0,962** |

**Kết luận P3 (chốt phiên này):**
- ✅ `b1_d` = `l1` (xác nhận bảng hỏi); do-file **không winsorize**; `controls` = lnEmp+firmage+foreign
  (không có sector FE).
- ⚠️ `firmage = b4` là **lỗi ánh xạ** (b4 = owners-female, không phải tuổi; tuổi đúng dùng `b5`).
- **2015 & 2023 tái lập hợp lý** (lệch ~0,15); **2009 không thể tái lập** từ file thô + spec hiện có
  (~0,6 vs 1,045) qua **mọi** biến thể mẫu số/winsor/firmage. → Gap 2009 **đặc thù file/mẫu**: nhiều
  khả năng **file phân tích 2009 NCS dùng khác** bản thô này (bộ lọc/sample khác), hoặc số 2009 từ một
  setting không nằm trong do-file committed.
- **Cần từ NCS để khớp 2009 chính xác:** bảng estimate Stata đợt 2009 + file `vietnam_2009_analytic.dta`
  (hoặc xác nhận bộ lọc mẫu 2009). Số manuscript **giữ nguyên** (author-authoritative).
