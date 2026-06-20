# Kiểm định độ vững: Timor-Leste CÓ vs KHÔNG (P7 + P8)

Cùng quy trình hài hòa hóa P7 (lp_z, FE nền+năm, CRV1 cụm theo nền); chỉ bật/tắt Timor-Leste.

## P7 — khung đa quốc gia
> *Số nền là số nền có dữ liệu raw trong kho đã commit; khung danh nghĩa là 50 nền (CÓ Timor) → 49 nền (KHÔNG Timor), gồm Nhật Bản.*

| Trường hợp | Số nền (raw) | N (M2) | β₂ độ cong (M2) | Điểm uốn M2 | Điểm uốn M5 |
|---|--:|--:|--:|--:|--:|
| CÓ Timor | 49 | 80,814 | -1.399 | 51.5% | 43.6% |
| KHÔNG Timor | 48 | 80,373 | -1.404 | 51.5% | 43.5% |

## P8 — nhóm SIDS
| Trường hợp | Số nền | N | Độ dốc tuyến tính (M1) | p | Độ cong (M2) | p |
|---|--:|--:|--:|--:|--:|--:|
| CÓ Timor | 8 | 1,867 | -0.088 | 0.392 | 0.598 | 0.056 |
| KHÔNG Timor | 7 | 1,434 | -0.085 | 0.592 | 0.696 | 0.098 |

**Đọc kết quả:** Headline P7 (điểm uốn, độ cong) gần như không đổi giữa hai trường hợp — Timor chỉ ~0,5% mẫu. Ở P8, dù CÓ hay KHÔNG Timor, kết luận lõi giữ nguyên: dạng chữ U ngược **tan rã** (độ dốc và độ cong không có ý nghĩa thống kê), không có điểm uốn nội vùng. Việc loại Timor là do **phân loại** (không phải quốc đảo Thái Bình Dương theo WB/UN), và kiểm định này xác nhận kết luận không phụ thuộc vào lựa chọn đó.

*Tái lập: `python3 scripts/timor_sensitivity.py`.*