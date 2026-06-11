---
name: stata-thuc-thi-batch
description: >
  Chạy Stata, Stata-MP, hoặc xStata trong môi trường dòng lệnh với các tệp .dta và .do.
  Sử dụng kỹ năng này khi bạn cần thực thi Stata trong batch mode, chạy các do-files,
  xử lý dữ liệu .dta, tự động hóa phân tích thống kê, chạy Stata trên server hoặc cluster,
  hoặc làm việc với Stata trong môi trường không có giao diện đồ họa. Phù hợp cho các trường hợp:
  phân tích dữ liệu Stata, xử lý batch, tự động hóa workflow, chạy Stata trên HPC,
  làm việc với do-files, và mọi tác vụ liên quan đến việc thực thi Stata từ command line
  hoặc trong môi trường lập trình.
---

# Thực Thi Stata Batch

## Tổng Quan

Kỹ năng này giúp bạn chạy Stata (bao gồm Stata-MP và xStata) trong môi trường dòng lệnh, đặc biệt hữu ích khi làm việc với môi trường code như Claude Code, terminal, hoặc các hệ thống HPC. Bạn sẽ học cách thực thi do-files, xử lý dữ liệu .dta, và tự động hóa các quy trình phân tích thống kê.

## Các Phiên Bản Stata

### Stata Standard (Console)
- **Lệnh**: `stata`
- **Sử dụng**: Phiên bản console cơ bản, đơn luồng
- **Khi nào dùng**: Phân tích nhỏ, dữ liệu vừa phải

### Stata-MP (Multiprocessor)
- **Lệnh**: `stata-mp`
- **Sử dụng**: Phiên bản đa xử lý, tận dụng nhiều CPU cores
- **Khi nào dùng**: Dữ liệu lớn, phân tích phức tạp, cần tốc độ cao
- **Lưu ý**: Cần giấy phép Stata-MP và phải chỉ định số cores trong SLURM/batch script

### xStata (GUI Version)
- **Lệnh**: `xstata`, `xstata-mp`, `xstata-se`
- **Sử dụng**: Phiên bản giao diện đồ họa
- **Khi nào dùng**: Khi cần GUI, làm việc qua X11 forwarding
- **Yêu cầu**: X11 server (XQuartz trên Mac, Xming/MobaXterm trên Windows)

## Cấu Trúc Do-File

Do-file là tệp văn bản chứa các lệnh Stata, thường có phần mở rộng `.do`.

### Cấu Trúc Cơ Bản

```stata
* Tắt tạm dừng output
set more off

* Bắt đầu log file
log using analysis.log, replace

* Load dữ liệu
use "data/mydata.dta", clear

* Phân tích
describe
summarize
regress y x1 x2 x3

* Lưu kết quả
save "output/results.dta", replace

* Đóng log
log close

* Bật lại more
set more on
```

### Best Practices cho Do-Files

1. **Luôn dùng `set more off`** ở đầu file để tránh tạm dừng output trong batch mode
2. **Sử dụng `clear` hoặc `, clear` option** để tránh lỗi khi dataset đã tồn tại trong memory
3. **Sử dụng đường dẫn tương đối** hoặc macros để code có thể tái sử dụng
4. **Comment rõ ràng** với `*` hoặc `//` hoặc `/* */`
5. **Luôn đóng log file** với `log close` ở cuối
6. **Sử dụng `replace` option** khi save file để ghi đè an toàn trong workflow tự động

## Các Phương Thức Thực Thi

### 1. Batch Mode Cơ Bản (Unix/Linux/Mac)

```bash
# Phương thức 1: Batch mode với output tự động
stata -b do analysis.do

# Stata sẽ tự động:
# - Thực thi các lệnh trong analysis.do
# - Lưu output vào analysis.log
# - Không hiển thị output ra màn hình
```

```bash
# Phương thức 2: Chạy nền với &
stata -b do analysis.do &

# Cho phép bạn tiếp tục làm việc trong terminal
```

### 2. Stata-MP Batch Mode

```bash
# Chạy với Stata-MP (tận dụng nhiều cores)
stata-mp -b do analysis.do

# Hoặc chạy nền
stata-mp -b do analysis.do &
```

### 3. Batch Mode với SMCL Log

```bash
# Sử dụng -s thay vì -b để lưu log dạng SMCL (Stata Markup Control Language)
stata -s do analysis.do

# Output sẽ được lưu trong analysis.smcl
```

### 4. Chạy với Nohup (Không bị ngắt khi đăng xuất)

```bash
# Sử dụng nohup để job tiếp tục chạy khi bạn logout
nohup stata -b do analysis.do &

# Hoặc với Stata-MP
nohup stata-mp -b do analysis.do &

# Output sẽ được lưu trong nohup.out
```

### 5. Chạy trên Windows

```cmd
REM Từ Command Prompt hoặc Run dialog
"C:\Program Files\Stata17\StataMP" /b do "C:\data\analysis.do"

REM /b: batch mode, yêu cầu click OK để thoát
REM /e: batch mode, tự động thoát khi hoàn thành
"C:\Program Files\Stata17\StataMP" /e do "C:\data\analysis.do"
```

## Làm Việc với Dữ Liệu .dta

### Load Dữ Liệu

```stata
* Load từ file local
use "path/to/data.dta", clear

* Load từ URL
use "https://www.stata-press.com/data/r17/auto.dta", clear

* Load chỉ một số biến
use mpg price weight using auto.dta, clear

* Load với điều kiện
use if foreign==1 using auto.dta, clear
```

### Lưu Dữ Liệu

```stata
* Lưu dataset
save "output/results.dta"

* Lưu và ghi đè
save "output/results.dta", replace

* Lưu chỉ một số biến
keep mpg price weight
save "output/subset.dta", replace
```

### Kiểm Tra và Khám Phá Dữ Liệu

```stata
* Xem thông tin dataset
describe

* Thống kê mô tả
summarize
summarize mpg price, detail

* Xem dữ liệu
list in 1/10
browse  // Chỉ hoạt động trong GUI mode
```

## Chạy Stata trên HPC/Cluster

### SLURM Script Example

```bash
#!/bin/bash
#SBATCH --job-name=stata-analysis
#SBATCH --output=stata-%j.out
#SBATCH --error=stata-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=02:00:00
#SBATCH --mem=32GB

# Load Stata module (nếu cần)
module load stata/17

# Chạy Stata-MP với do-file
stata-mp -b do analysis.do
```

Submit job:
```bash
sbatch stata_job.sh
```

### Kiểm Tra Job Status

```bash
# Xem jobs đang chạy
squeue -u $USER

# Xem output real-time
tail -f stata-JOBID.out

# Hủy job
scancel JOBID
```

## Xử Lý Lỗi Phổ Biến

### 1. File Already Exists

**Lỗi**: `file xxx.dta already exists`

**Giải pháp**: Thêm option `replace`
```stata
save "output.dta", replace
```

### 2. Variable Not Found

**Lỗi**: `variable xxx not found`

**Giải pháp**: Kiểm tra tên biến với `describe` hoặc `ds`
```stata
describe
ds  // list all variable names
```

### 3. No Data in Memory

**Lỗi**: `no data in memory`

**Giải pháp**: Load dữ liệu trước khi phân tích
```stata
use "data.dta", clear
```

### 4. Disk Full hoặc I/O Error

**Lỗi**: `I/O error writing .dta file`

**Nguyên nhân**: Thường do hết dung lượng disk hoặc /tmp đầy

**Giải pháp**:
- Kiểm tra quota: `quota -s` hoặc `df -h`
- Xóa files tạm: `rm -rf /tmp/stata_temp*`
- Đặt TMPDIR khác: `export TMPDIR=/path/to/larger/tmp`

### 5. Display Error với xStata

**Lỗi**: `cannot open display`

**Giải pháp**: Đảm bảo X11 forwarding được bật
```bash
# Kết nối với X11 forwarding
ssh -Y user@server

# Hoặc kiểm tra DISPLAY variable
echo $DISPLAY
```

## Tips và Tricks

### 1. Sử dụng Macros cho Paths

```stata
* Định nghĩa macros cho paths
local datadir "/path/to/data"
local outdir "/path/to/output"

* Sử dụng trong code
use "`datadir'/input.dta", clear
save "`outdir'/results.dta", replace
```

### 2. Chạy Multiple Do-Files

```stata
* Master do-file gọi các do-files khác
do "01_import.do"
do "02_clean.do"
do "03_analyze.do"
do "04_export.do"
```

### 3. Conditional Execution

```stata
* Chỉ chạy nếu file tồn tại
capture confirm file "data.dta"
if _rc==0 {
    use "data.dta", clear
    summarize
}
else {
    display "File not found"
}
```

### 4. Logging Best Practices

```stata
* Đóng log cũ nếu đang mở
capture log close

* Mở log mới
log using "analysis_`c(current_date)'.log", replace

* Your analysis here

* Đóng log
log close
```

### 5. Kiểm Tra Stata Version trong Do-File

```stata
* Đảm bảo code chạy với version cụ thể
version 17

* Hoặc kiểm tra version
if c(version) < 17 {
    display as error "This script requires Stata 17 or later"
    exit 198
}
```

## Workflow Tự Động Hóa

### Example: Complete Analysis Pipeline

```stata
/*==============================================================================
  Project: Monthly Sales Analysis
  Author: Your Name
  Date: 2026-05-14
  Description: Automated monthly analysis pipeline
==============================================================================*/

* Setup
clear all
set more off
capture log close
log using "monthly_analysis_`c(current_date)'.log", replace

* Define paths
local rawdata "data/raw"
local processed "data/processed"
local output "output"

* 1. Import and merge data
use "`rawdata'/sales.dta", clear
merge 1:1 id using "`rawdata'/customers.dta"
drop if _merge != 3
drop _merge

* 2. Data cleaning
drop if missing(sales_amount)
replace sales_amount = 0 if sales_amount < 0

* 3. Generate variables
gen log_sales = log(sales_amount + 1)
gen month = month(date)
gen year = year(date)

* 4. Analysis
bysort region: summarize sales_amount
regress log_sales i.region i.month

* 5. Save results
save "`processed'/analysis_ready.dta", replace

* 6. Export summary stats
tabstat sales_amount, by(region) statistics(mean median sd) save
return list

* Cleanup
log close
display "Analysis completed successfully at `c(current_time)'"
```

## Tích Hợp với Claude Code

Khi làm việc trong Claude Code environment:

1. **Tạo do-file**: Viết script Stata và lưu với extension `.do`
2. **Chuẩn bị dữ liệu**: Đảm bảo file `.dta` có sẵn hoặc sẽ được tạo
3. **Chạy từ terminal**:
   ```bash
   stata -b do your_script.do
   ```
4. **Kiểm tra output**: Đọc file `.log` để xem kết quả
5. **Debug nếu cần**: Sửa do-file và chạy lại

## Tài Nguyên Tham Khảo

- **Stata Manual**: [U] 16 Do-files
- **Batch Mode**: [GSW] B.5 Stata batch mode (Windows), [GSU] B.3 (Unix)
- **Command Reference**: `help command_name` trong Stata
- **Stata Journal**: https://www.stata-journal.com/
- **Statalist Forum**: https://www.statalist.org/
