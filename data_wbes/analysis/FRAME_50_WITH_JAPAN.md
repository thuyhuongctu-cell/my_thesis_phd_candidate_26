# Khung 50 nền (gồm Nhật Bản) — số chuẩn cho lần đầu công bố

> Nhật Bản 2025 (khảo sát WBES lần đầu, n=2.168) là thành viên đầy đủ của Nhóm I.
> Pipeline: `cd1_descriptives_pipeline.py` (đã inject Japan -> Advanced_innovation).

## Pool mô tả
| | Cũ (49 nền) | Mới (50 nền, có Nhật) |
|---|--:|--:|
| Doanh nghiệp | 86.701 | **88.869** |
| Cặp nền×năm | 102 | **103** |
| Nền kinh tế | 49 | **50** |
| Nhóm I (số nền) | 5 | **6** |

## Nhóm I — Advanced đổi mới (6 nền: HongKong, Israel, Japan, Korea, Singapore, Taiwan)
| Chỉ tiêu | Cũ (5 nền) | Mới (6 nền, có Nhật) |
|---|--:|--:|
| n_firms | 4.222 | **6.390** |
| sd ln(LP) trong đợt (trung vị) | 1,04 | **1,00** |
| P90/P10 (trung vị) | 12,2 | **11,7** |
| Đổi mới sản phẩm % | 24,3 | **26,9** |
| Đổi mới quy trình % | 14,7 | **18,8** |
| R&D % | 20,5 | **21,0** |
| ISO % | 35,0 | **32,5** |
| Website % | 61,7 | **69,2** |
| Nữ quản lý cấp cao % | 27,5 | **20,7** |
| Nữ chủ sở hữu % | 32,5 | **33,8** |
| DN xuất khẩu % | 28,4 | **24,5** |
| FDI ≥10% % | 10,6 | **7,7** |
| SME % | 79,5 | **76,9** |
| Tham nhũng trở ngại lớn % | 2,9 | **4,2** |
| FSTS trung bình % | 13,4 | **10,3** |
| Tuổi DN TB (năm) | 23,0 | **32,2** |
| CAGR việc làm % | 3,0 | **2,4** |

## Nhóm I — Tương quan lp_z (Bảng 2.3.8.1)
| Yếu tố | Cũ | Mới (có Nhật) |
|---|--:|--:|
| FDI ≥10% | +0,130** | **+0,104** |
| FSTS | +0,163** | **+0,139** |
| TCI | +0,176** | **+0,158** |
| DAI | +0,098** | **+0,090** |

## Lưu ý econometric
Khung ước lượng P7/P8/P9 (master `p7_pooled_clean.csv`) KHÔNG có Nhật (dữ liệu đến
sau khi chốt mẫu ước lượng). Điểm uốn P7 = 40,0% (N M2=84.910, M5=38.342) giữ nguyên
như đã ước lượng; đưa Nhật vào ước lượng là vòng tái ước lượng tiếp theo (do-file gốc).
Các con số mô tả (50 nền) và ước lượng (49 nền vintage) khác nhau do data availability,
đúng như mọi mô hình có N khác nhau theo tính sẵn có của biến.
