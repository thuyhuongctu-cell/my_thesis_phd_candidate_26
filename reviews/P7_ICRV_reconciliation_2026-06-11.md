# Đối chiếu sơ đồ ICRV của P7 — 5-regime (nháp) vs 6-group (thực chạy)

**Ngày:** 2026-06-11 · **Yêu cầu:** đối chiếu xem P7 thực sự chạy 5 hay 6 nhóm ICRV, giải quyết lệch giữa docs thiết kế và manuscript.

---

## Kết luận: P7 chạy **6 nhóm** — Group 5 = Emerging, Group 6 = SIDS. "Frontier" không tồn tại trong phân tích thật.

### Bằng chứng (ground truth)

**1. Master analytic data** (`data_wbes/p7/p7_pooled_clean.csv`, đã commit) — phân bố `icrv_group` ↔ `icrv_label`:

| icrv_group | icrv_label | n firms |
|:--:|---|--:|
| 1 | Advanced_innovation | 4.708 |
| 2 | Advanced_resource | 2.269 |
| 3 | Upper_mid | 17.905 |
| 4 | Lower_mid_transition | 50.926 |
| 5 | **Emerging** | 18.569 |
| 6 | **SIDS_small** | 2.038 |
| (trống) | (chưa gán) | 10.350 |

→ 6 nhóm; **không có nhãn "Frontier"**; **SIDS = Nhóm 6** (không phải 4).

**2. Script build** (`p7/replication/01_build_p7_dataset.py`):
```python
ICRV_LABEL = {1:"Advanced_innovation", 2:"Advanced_resource", 3:"Upper_mid",
              4:"Lower_mid_transition", 5:"Emerging", 6:"SIDS_small"}
# comment: IV=7 lower-mid, V=17 emerging, VI=7 SIDS/small
```

**3. Script model** (`p7/replication/02_run_p7_models.py`): tạo dummy `icrv_g1,g2,g4,g5,g6` (Group 3 = reference); Afghanistan/Myanmar ∈ Group 5 (Emerging). M10/M11 dùng `icrv_group` liên tục 1–6.

**4. Manuscript P7**: nêu rõ "six ICRV groups (Group I–VI)" — khớp.

### Nguồn gây nhầm (đã xử lý)

| File | Nội dung sai | Trạng thái |
|---|---|---|
| `p7/08_..._harmonization_protocol_vi.md` §4.6 (dòng 114–236) | Sơ đồ **5-regime nháp**: VN/Ấn Độ/TQ gộp regime 2; SIDS=4; Frontier=5; `label define ICRV ... 4 "SIDS" 5 "Frontier"` | Gắn banner **ĐÃ THAY THẾ** trỏ về script Python chuẩn (giữ khối cũ để truy vết lịch sử, không viết lại bản đồ 49 nước) |
| `p7/07_..._design_vi.md` dòng 117 | "categorical I/II/III/SIDS/Frontier" (5 nhóm) | Sửa thành 6 nhóm I/II/III/IV/V/VI + nhãn chuẩn |
| `p7` manuscripts (clean + ibr/apjm/jibs + vi) | "Group V–VI (Frontier/SIDS)" | Đã đổi → "(Emerging/SIDS)" + tái tạo docx (commit trước) |

## Hệ quả cho tính nhất quán
- Nhãn dữ liệu chuẩn 6 nhóm nay thống nhất xuyên: master data, script, manuscript P7, luận án Ch1–Ch5, CĐ2.
- P6 giữ taxonomy 5-regime meta riêng (đã có ghi chú phân biệt ở luận án §4.2) — đúng theo thiết kế của P6, không trộn với hệ 6 nhóm cấp doanh nghiệp.

## Không thay đổi (có chủ đích)
- Khối Stata cũ trong `08_*` được giữ nguyên dưới banner (truy vết lịch sử thiết kế); tham chiếu chuẩn là `01_build_p7_dataset.py`.
- CĐ1 vẫn ở bản khóa mô tả riêng (crosswalk đã thêm); số liệu chờ re-lock 43 raw `.dta`.
