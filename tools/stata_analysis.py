#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stata Data Analysis Script

Script tự động để đọc và phân tích dữ liệu Stata (.dta files).
Có thể chạy từ command line với các options khác nhau.

Usage:
    python stata_analysis.py input.dta --summary
    python stata_analysis.py input.dta --regress "y ~ x1 + x2 + x3"
    python stata_analysis.py input.dta --describe --output report.txt
"""

import argparse
import sys
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def read_stata_file(filepath):
    """Đọc file Stata với error handling."""
    try:
        df = pd.read_stata(filepath)
        print(f"Đọc thành công: {filepath}")
        print(f"Số quan sát: {len(df)}")
        print(f"Số biến: {len(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        sys.exit(1)


def describe_data(df, output_file=None):
    """In thông tin mô tả về dataset."""
    output = []
    output.append("=" * 80)
    output.append("THÔNG TIN DỮ LIỆU")
    output.append("=" * 80)
    output.append(f"\nSố quan sát: {len(df)}")
    output.append(f"Số biến: {len(df.columns)}")
    
    output.append("\n" + "=" * 80)
    output.append("CẤU TRÚC DỮ LIỆU")
    output.append("=" * 80)
    
    info_str = df.info(buf=None)
    
    output.append("\n" + "=" * 80)
    output.append("THỐNG KÊ MÔ TẢ")
    output.append("=" * 80)
    output.append("\n" + str(df.describe()))
    
    output.append("\n" + "=" * 80)
    output.append("MISSING VALUES")
    output.append("=" * 80)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Percentage': missing_pct
    })
    output.append("\n" + str(missing_df[missing_df['Missing Count'] > 0]))
    
    result = "\n".join(output)
    print(result)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\nĐã lưu kết quả vào: {output_file}")
    
    return result


def summary_statistics(df, variables=None, output_file=None):
    """Tạo bảng thống kê tóm tắt."""
    if variables:
        df_subset = df[variables]
    else:
        df_subset = df.select_dtypes(include=[np.number])
    
    summary = df_subset.describe().T
    summary['missing'] = df_subset.isnull().sum()
    summary['missing_pct'] = (summary['missing'] / len(df)) * 100
    
    print("\n" + "=" * 80)
    print("THỐNG KÊ TÓM TẮT")
    print("=" * 80)
    print(summary)
    
    if output_file:
        summary.to_csv(output_file)
        print(f"\nĐã lưu vào: {output_file}")
    
    return summary


def run_regression(df, formula, output_file=None):
    """Chạy OLS regression."""
    try:
        model = smf.ols(formula, data=df).fit()
        
        print("\n" + "=" * 80)
        print("KẾT QUẢ HỒI QUY OLS")
        print("=" * 80)
        print(f"Formula: {formula}")
        print("\n" + str(model.summary()))
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Formula: {formula}\n\n")
                f.write(model.summary().as_text())
            print(f"\nĐã lưu kết quả vào: {output_file}")
        
        return model
    except Exception as e:
        print(f"Lỗi khi chạy regression: {e}")
        return None


def create_correlation_matrix(df, variables=None, output_file=None):
    """Tạo ma trận tương quan."""
    if variables:
        df_subset = df[variables]
    else:
        df_subset = df.select_dtypes(include=[np.number])
    
    corr = df_subset.corr()
    
    print("\n" + "=" * 80)
    print("MA TRẬN TƯƠNG QUAN")
    print("=" * 80)
    print(corr)
    
    # Tạo heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix')
    plt.tight_layout()
    
    if output_file:
        corr.to_csv(output_file)
        plot_file = output_file.replace('.csv', '_heatmap.png')
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"\nĐã lưu ma trận vào: {output_file}")
        print(f"Đã lưu heatmap vào: {plot_file}")
    else:
        plt.show()
    
    return corr


def export_to_csv(df, output_file):
    """Xuất dữ liệu sang CSV."""
    try:
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"\nĐã xuất dữ liệu sang: {output_file}")
    except Exception as e:
        print(f"Lỗi khi xuất file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Phân tích dữ liệu Stata (.dta files)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  %(prog)s data.dta --describe
  %(prog)s data.dta --summary --output summary.csv
  %(prog)s data.dta --regress "income ~ age + education"
  %(prog)s data.dta --correlation --vars age income education
        """
    )
    
    parser.add_argument('input', help='File .dta đầu vào')
    parser.add_argument('--describe', action='store_true',
                        help='Hiển thị thông tin mô tả dataset')
    parser.add_argument('--summary', action='store_true',
                        help='Tạo bảng thống kê tóm tắt')
    parser.add_argument('--regress', type=str, metavar='FORMULA',
                        help='Chạy OLS regression với formula (VD: "y ~ x1 + x2")')
    parser.add_argument('--correlation', action='store_true',
                        help='Tạo ma trận tương quan')
    parser.add_argument('--vars', nargs='+', metavar='VAR',
                        help='Danh sách biến để phân tích')
    parser.add_argument('--output', '-o', type=str,
                        help='File output để lưu kết quả')
    parser.add_argument('--export-csv', type=str, metavar='FILE',
                        help='Xuất dữ liệu sang CSV')
    
    args = parser.parse_args()
    
    # Kiểm tra có ít nhất một action
    if not any([args.describe, args.summary, args.regress, 
                args.correlation, args.export_csv]):
        parser.print_help()
        print("\nLỗi: Cần chọn ít nhất một action (--describe, --summary, v.v.)")
        sys.exit(1)
    
    # Đọc dữ liệu
    df = read_stata_file(args.input)
    
    # Thực hiện các phân tích
    if args.describe:
        describe_data(df, args.output)
    
    if args.summary:
        summary_statistics(df, args.vars, args.output)
    
    if args.regress:
        run_regression(df, args.regress, args.output)
    
    if args.correlation:
        create_correlation_matrix(df, args.vars, args.output)
    
    if args.export_csv:
        export_to_csv(df, args.export_csv)
    
    print("\nHoàn tất!")


if __name__ == '__main__':
    main()
