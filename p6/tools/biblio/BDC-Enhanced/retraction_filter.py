#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
撤稿文献筛选模块

功能:
1. 检测撤稿文献(Retracted Publication)
2. 支持多种检测方式:
   - 标题关键词检测
   - 文档类型检测
   - 在线数据库查询(可选)
3. 生成撤稿报告

作者: Meng Linghan
版本: v1.0.0
日期: 2026-02-11
"""

import os
import re
import json
import requests
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime


class RetractionDetector:
    """撤稿文献检测器"""
    
    # 撤稿相关关键词
    RETRACTION_KEYWORDS = [
        'retract',
        'retraction',
        'withdrawn',
        'withdrawal',
        'erratum',
        'corrigendum',
        'expression of concern',
        'duplicate publication',
    ]
    
    def __init__(self, use_online_check: bool = False):
        """
        初始化
        
        参数:
            use_online_check: 是否使用在线数据库查询
        """
        self.use_online_check = use_online_check
        self.stats = {
            'total_records': 0,
            'retracted_by_title': 0,
            'retracted_by_type': 0,
            'retracted_by_online': 0,
            'total_retracted': 0,
            'clean_records': 0
        }
        self.retracted_records = []
        self.retraction_details = []
    
    def check_title(self, title: str) -> bool:
        """检查标题是否包含撤稿关键词"""
        if not title:
            return False
        
        title_lower = title.lower()
        for keyword in self.RETRACTION_KEYWORDS:
            if keyword in title_lower:
                return True
        return False
    
    def check_document_type(self, doc_type: str) -> bool:
        """检查文档类型是否为撤稿"""
        if not doc_type:
            return False
        
        doc_type_lower = doc_type.lower()
        retraction_types = [
            'retraction',
            'retracted publication',
            'correction',
            'erratum',
        ]
        
        for ret_type in retraction_types:
            if ret_type in doc_type_lower:
                return True
        return False
    
    def check_online_database(self, doi: str = None, title: str = None) -> Tuple[bool, str]:
        """
        在线查询是否为撤稿文献
        
        使用Retraction Watch Database API (如果可用)
        或CrossRef API查询
        
        返回: (是否撤稿, 撤稿原因)
        """
        if not self.use_online_check:
            return False, ""
        
        # 优先使用DOI查询
        if doi:
            is_retracted, reason = self._check_crossref(doi)
            if is_retracted:
                return True, reason
        
        # TODO: 可以添加更多在线数据库查询
        # - Retraction Watch Database
        # - PubMed
        # - Europe PMC
        
        return False, ""
    
    def _check_crossref(self, doi: str) -> Tuple[bool, str]:
        """使用CrossRef API查询"""
        try:
            url = f"https://api.crossref.org/works/{doi}"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                message = data.get('message', {})
                
                # 检查是否有更新/撤回标记
                update = message.get('update-to', [])
                if update:
                    for item in update:
                        if item.get('type') == 'retraction':
                            return True, "Retracted by publisher"
                
                # 检查关系
                relation = message.get('relation', {})
                if 'is-retraction-of' in relation or 'has-retraction' in relation:
                    return True, "Retraction noted in CrossRef"
        
        except Exception as e:
            # 网络查询失败不影响本地检测
            pass
        
        return False, ""
    
    def detect_record(self, record: str) -> Tuple[bool, List[str]]:
        """
        检测单条记录是否为撤稿文献
        
        返回: (是否撤稿, 检测到的原因列表)
        """
        reasons = []
        
        # 提取字段
        title = self._extract_field(record, 'TI')
        doc_type = self._extract_field(record, 'DT')
        doi = self._extract_field(record, 'DI')
        
        # 标题检查
        if self.check_title(title):
            reasons.append(f"Title contains retraction keyword")
            self.stats['retracted_by_title'] += 1
        
        # 文档类型检查
        if self.check_document_type(doc_type):
            reasons.append(f"Document type indicates retraction: {doc_type}")
            self.stats['retracted_by_type'] += 1
        
        # 在线查询
        if self.use_online_check:
            is_retracted_online, online_reason = self.check_online_database(doi, title)
            if is_retracted_online:
                reasons.append(f"Online database: {online_reason}")
                self.stats['retracted_by_online'] += 1
        
        return len(reasons) > 0, reasons
    
    def _extract_field(self, record: str, field: str) -> str:
        """提取字段值"""
        pattern = rf'{field}\s+(.+?)(?=\n[A-Z]{{2}}\s|\nER|\nEF|\n$)'
        match = re.search(pattern, record, re.DOTALL)
        if not match:
            return ""
        
        value = match.group(1).strip()
        value = re.sub(r'\n\s{3}', ' ', value)
        return value
    
    def filter_file(self, input_file: str, output_file: str = None) -> str:
        """
        过滤文件,移除撤稿文献
        
        参数:
            input_file: 输入文件路径
            output_file: 输出文件路径(可选)
        
        返回:
            输出文件路径
        """
        print("\n" + "=" * 80)
        print("🔍 撤稿文献检测与过滤")
        print("=" * 80)
        
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"输入文件不存在: {input_file}")
        
        # 默认输出文件
        if not output_file:
            output_file = str(input_path.parent / f"{input_path.stem}_no_retractions.txt")
        
        # 读取文件
        print(f"\n📂 读取文件: {input_file}")
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 分割记录
        records = content.split('\nER\n')
        self.stats['total_records'] = len([r for r in records if r.strip()])
        
        # 过滤
        print(f"\n🔎 开始检测 {self.stats['total_records']} 条记录...")
        
        clean_records = []
        
        for i, record in enumerate(records):
            if not record.strip():
                continue
            
            is_retracted, reasons = self.detect_record(record)
            
            if is_retracted:
                # 记录撤稿信息
                self.retracted_records.append(record)
                self.retraction_details.append({
                    'record_number': i + 1,
                    'title': self._extract_field(record, 'TI'),
                    'doi': self._extract_field(record, 'DI'),
                    'reasons': reasons
                })
                self.stats['total_retracted'] += 1
            else:
                clean_records.append(record)
                self.stats['clean_records'] += 1
            
            # 进度显示
            if (i + 1) % 100 == 0:
                print(f"  已检测 {i + 1}/{self.stats['total_records']} 条记录")
        
        # 保存清洁数据
        print(f"\n💾 保存过滤后数据到: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\nER\n'.join(clean_records))
            if not content.endswith('\nEF'):
                f.write('\nEF')
        
        # 保存撤稿报告
        self._save_retraction_report(input_path)
        
        # 打印统计
        self._print_statistics()
        
        return output_file
    
    def _save_retraction_report(self, input_path: Path):
        """保存撤稿报告"""
        report_file = input_path.parent / f"{input_path.stem}_retraction_report.json"
        
        report_data = {
            'scan_date': datetime.now().isoformat(),
            'input_file': str(input_path),
            'statistics': self.stats,
            'retracted_records': self.retraction_details
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"📋 撤稿报告已保存: {report_file}")
        
        # 也保存文本版本
        txt_report = input_path.parent / f"{input_path.stem}_retraction_report.txt"
        with open(txt_report, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("撤稿文献检测报告\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"输入文件: {input_path}\n\n")
            
            f.write("统计摘要:\n")
            f.write(f"  总记录数: {self.stats['total_records']}\n")
            f.write(f"  撤稿记录: {self.stats['total_retracted']}\n")
            f.write(f"  清洁记录: {self.stats['clean_records']}\n\n")
            
            f.write("检测详情:\n")
            f.write(f"  标题关键词检测: {self.stats['retracted_by_title']}\n")
            f.write(f"  文档类型检测: {self.stats['retracted_by_type']}\n")
            if self.use_online_check:
                f.write(f"  在线数据库查询: {self.stats['retracted_by_online']}\n")
            f.write("\n")
            
            if self.retraction_details:
                f.write("撤稿记录列表:\n")
                f.write("-" * 80 + "\n")
                for detail in self.retraction_details:
                    f.write(f"\n记录 #{detail['record_number']}:\n")
                    f.write(f"  标题: {detail['title']}\n")
                    if detail['doi']:
                        f.write(f"  DOI: {detail['doi']}\n")
                    f.write(f"  检测原因:\n")
                    for reason in detail['reasons']:
                        f.write(f"    - {reason}\n")
        
        print(f"📋 文本报告已保存: {txt_report}")
    
    def _print_statistics(self):
        """打印统计信息"""
        print("\n" + "=" * 80)
        print("📊 撤稿检测统计")
        print("=" * 80)
        print(f"   总记录数: {self.stats['total_records']}")
        print(f"   检测到撤稿: {self.stats['total_retracted']} ({self.stats['total_retracted']/max(1,self.stats['total_records'])*100:.2f}%)")
        print(f"   清洁记录: {self.stats['clean_records']} ({self.stats['clean_records']/max(1,self.stats['total_records'])*100:.2f}%)")
        print(f"\n检测方式统计:")
        print(f"   标题关键词: {self.stats['retracted_by_title']} 条")
        print(f"   文档类型: {self.stats['retracted_by_type']} 条")
        if self.use_online_check:
            print(f"   在线查询: {self.stats['retracted_by_online']} 条")
        print("=" * 80)
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        return self.stats.copy()


class RetractionFilter:
    """GUI包装类"""
    
    def __init__(self):
        self.detector = None
        self.stats = {}
    
    def filter_retractions(self, input_file: str, output_file: str = None,
                          use_online_check: bool = False) -> str:
        """
        过滤撤稿文献
        
        参数:
            input_file: 输入文件
            output_file: 输出文件
            use_online_check: 是否使用在线查询
        
        返回:
            输出文件路径
        """
        self.detector = RetractionDetector(use_online_check=use_online_check)
        
        try:
            result_file = self.detector.filter_file(input_file, output_file)
            self.stats = self.detector.get_statistics()
            return result_file
        
        except Exception as e:
            print(f"\n❌ 撤稿过滤失败: {e}")
            raise
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        default_stats = {
            'total_records': 0,
            'retracted_by_title': 0,
            'retracted_by_type': 0,
            'retracted_by_online': 0,
            'total_retracted': 0,
            'clean_records': 0
        }
        default_stats.update(self.stats)
        return default_stats


def main():
    """命令行使用示例"""
    import sys
    
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n使用方法:")
        print("  python retraction_filter.py <input_file> [--online]")
        print("\n参数:")
        print("  input_file    输入文件路径")
        print("  --online      启用在线数据库查询(可选)")
        print("\n示例:")
        print("  python retraction_filter.py merged_data.txt")
        print("  python retraction_filter.py merged_data.txt --online")
        return
    
    input_file = sys.argv[1]
    use_online = '--online' in sys.argv
    
    filter_tool = RetractionFilter()
    output_file = filter_tool.filter_retractions(
        input_file=input_file,
        use_online_check=use_online
    )
    
    print(f"\n✅ 过滤完成!")
    print(f"   输出文件: {output_file}")
    print(f"   检测到撤稿: {filter_tool.stats['total_retracted']} 条")


if __name__ == '__main__':
    main()
