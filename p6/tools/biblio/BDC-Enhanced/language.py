#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文献语言筛选工具 - 强化版
================

筛选WOS格式文件中指定语言的文献记录
兼容标准WOS格式和带引号的EndNote格式
自动识别并跳过非数据文件
"""

import re
import os
import sys
import logging
from typing import List, Dict, Tuple, Optional
from collections import Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LanguageFilter:
    """WOS格式文件语言筛选器 - 强化版"""

    def __init__(self, input_file: str, output_file: str, target_language: str = "English"):
        self.input_file = input_file
        self.output_file = output_file
        self.target_language = target_language
        self.file_header = "FN Clarivate Analytics Web of Science\nVR 1.0\n"

        # 统计数据
        self.stats = {
            'total_records': 0,
            'filtered_records': 0,
            'no_language_field': 0,
            'language_distribution': Counter()
        }

    def is_valid_wos_data_file(self, filepath: str) -> bool:
        """检查是否是有效的WOS数据文件"""
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                first_lines = [f.readline() for _ in range(5)]
            
            # 检查是否包含WOS数据特征
            content = ' '.join(first_lines)
            
            # 数据文件特征：
            # 1. 包含FN/VR文件头
            # 2. 包含PT字段（记录开始）
            # 3. 不包含"报告"、"统计"等字样
            has_header = 'FN ' in content or 'VR ' in content
            has_pt = 'PT ' in content or '"PT "' in content
            is_report = '报告' in content or 'Report' in content or '统计' in content
            
            return has_header and has_pt and not is_report
        except:
            return False

    def parse_wos_file(self) -> List[Dict]:
        """
        解析WOS格式文件，兼容带引号的EndNote格式
        """
        logger.info(f"📖 解析文件: {self.input_file}")
        
        # 检查是否是有效的WOS数据文件
        if not self.is_valid_wos_data_file(self.input_file):
            logger.error(f"❌ 不是有效的WOS数据文件: {self.input_file}")
            logger.info("💡 提示: 请确保输入的是 merged_deduplicated_no_retractions.txt 这样的数据文件")
            return []
        
        records = []
        
        with open(self.input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # 提取文件头
        header_lines = []
        lines = content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('FN ') or line.startswith('VR ') or line.startswith('"FN ') or line.startswith('"VR '):
                header_lines.append(lines[i])
                i += 1
            else:
                break
        
        if header_lines:
            self.file_header = '\n'.join(header_lines) + '\n'
        
        # 按记录分割
        record_texts = []
        current_record = []
        in_record = False
        
        for line in lines[i:]:
            stripped = line.strip()
            
            # 记录开始（PT字段）
            if stripped.startswith('PT ') or stripped.startswith('"PT '):
                if current_record:
                    record_texts.append('\n'.join(current_record))
                    current_record = []
                in_record = True
                current_record.append(line)
            # 记录结束
            elif stripped == 'ER' or stripped == '"ER"':
                if current_record:
                    current_record.append(line)
                    record_texts.append('\n'.join(current_record))
                    current_record = []
                    in_record = False
            # 记录内容
            elif in_record:
                current_record.append(line)
        
        # 处理最后一条记录
        if current_record:
            record_texts.append('\n'.join(current_record))
        
        # 解析每条记录
        for record_text in record_texts:
            record = {
                'raw_text': record_text,
                'fields': {}
            }
            
            record_lines = record_text.split('\n')
            current_field = None
            current_value = []
            
            for line in record_lines:
                # 移除引号
                clean_line = line.strip()
                if clean_line.startswith('"'):
                    clean_line = clean_line[1:]
                if clean_line.endswith('"'):
                    clean_line = clean_line[:-1]
                
                # 新字段
                if len(clean_line) >= 3 and clean_line[2] == ' ' and clean_line[:2].isupper():
                    if current_field:
                        record['fields'][current_field] = '\n'.join(current_value).strip()
                    
                    current_field = clean_line[:2]
                    current_value = [clean_line[3:].strip()]
                # 续行
                elif line.startswith('   ') and current_field:
                    cont_value = line[3:].strip()
                    if cont_value.startswith('"'):
                        cont_value = cont_value[1:]
                    if cont_value.endswith('"'):
                        cont_value = cont_value[:-1]
                    current_value.append(cont_value)
                # 续行（带引号）
                elif line.startswith('"   ') and current_field:
                    cont_value = line[4:].strip()
                    if cont_value.endswith('"'):
                        cont_value = cont_value[:-1]
                    current_value.append(cont_value)
            
            # 保存最后一个字段
            if current_field and current_value:
                record['fields'][current_field] = '\n'.join(current_value).strip()
            
            records.append(record)
        
        logger.info(f"✅ 解析完成: {len(records)} 条记录")
        return records

    def filter_records(self, records: List[Dict]) -> List[Dict]:
        """
        筛选指定语言的记录
        """
        logger.info(f"🔤 筛选语言: {self.target_language}")
        
        filtered = []
        self.stats['total_records'] = len(records)
        
        for record in records:
            fields = record['fields']
            
            # 获取语言字段
            language = None
            if 'LA' in fields:
                language = fields['LA'].strip()
                # 去除可能的引号
                if language.startswith('"'):
                    language = language[1:]
                if language.endswith('"'):
                    language = language[:-1]
                
                self.stats['language_distribution'][language] += 1
                
                # 筛选目标语言
                if language.lower() == self.target_language.lower():
                    filtered.append(record)
                    self.stats['filtered_records'] += 1
            else:
                self.stats['no_language_field'] += 1
                # 没有语言字段的记录默认保留
                filtered.append(record)
        
        logger.info(f"✅ 筛选完成: 保留 {len(filtered)}/{len(records)} 条记录")
        return filtered

    def write_filtered_file(self, records: List[Dict]):
        """
        写入筛选后的WOS格式文件
        """
        logger.info(f"💾 写入文件: {self.output_file}")
        
        with open(self.output_file, 'w', encoding='utf-8-sig') as f:
            # 写入文件头
            f.write(self.file_header)
            f.write('\n')
            
            # 写入每条记录的原始文本
            for i, record in enumerate(records):
                f.write(record['raw_text'])
                if i < len(records) - 1:
                    f.write('\n\n')
            
            # 写入文件尾
            f.write('\nEF\n')
        
        logger.info(f"✅ 写入完成")

    def generate_report(self) -> str:
        """
        生成筛选报告
        """
        report = []
        report.append("=" * 80)
        report.append("📊 语言筛选报告")
        report.append("=" * 80)
        report.append("")
        report.append(f"输入文件: {self.input_file}")
        report.append(f"输出文件: {self.output_file}")
        report.append(f"目标语言: {self.target_language}")
        report.append("")
        report.append("-" * 80)
        report.append("筛选结果:")
        report.append("-" * 80)
        report.append(f"总记录数:           {self.stats['total_records']:>6}")
        report.append(f"筛选后记录数:       {self.stats['filtered_records']:>6}")
        report.append(f"无语言字段记录:     {self.stats['no_language_field']:>6}")
        
        if self.stats['total_records'] > 0:
            percentage = (self.stats['filtered_records'] / self.stats['total_records']) * 100
            report.append(f"保留比例:           {percentage:>5.1f}%")
        
        report.append("")
        report.append("-" * 80)
        report.append("语言分布:")
        report.append("-" * 80)
        
        for language, count in self.stats['language_distribution'].most_common():
            percentage = (count / self.stats['total_records']) * 100 if self.stats['total_records'] > 0 else 0
            marker = " ✓" if language.lower() == self.target_language.lower() else ""
            report.append(f"  {language:20s}: {count:>5} ({percentage:5.1f}%){marker}")
        
        report.append("")
        report.append("=" * 80)
        
        return '\n'.join(report)

    def save_report(self) -> str:
        """
        保存报告到文件
        """
        report_file = self.output_file.replace('.txt', '_filter_report.txt')
        report_text = self.generate_report()
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        logger.info(f"📋 报告已保存: {report_file}")
        return report_file

    def run(self) -> bool:
        """
        执行筛选流程
        """
        logger.info("=" * 80)
        logger.info("🚀 文献语言筛选工具启动")
        logger.info("=" * 80)
        
        try:
            # 1. 检查输入文件
            if not os.path.exists(self.input_file):
                logger.error(f"❌ 输入文件不存在: {self.input_file}")
                return False
            
            # 2. 检查是否是有效的WOS数据文件
            if not self.is_valid_wos_data_file(self.input_file):
                logger.error(f"❌ 不是有效的WOS数据文件: {self.input_file}")
                logger.info("💡 提示: 请确保输入的是包含PT字段的数据文件")
                return False
            
            # 3. 解析文件
            records = self.parse_wos_file()
            
            if not records:
                logger.error("❌ 未找到任何记录")
                return False
            
            # 4. 筛选记录
            filtered_records = self.filter_records(records)
            
            # 5. 写入文件
            self.write_filtered_file(filtered_records)
            
            # 6. 生成报告
            self.save_report()
            
            # 7. 打印报告
            print("\n" + self.generate_report())
            
            logger.info("=" * 80)
            logger.info("✅ 筛选完成!")
            logger.info("=" * 80)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ 筛选失败: {e}")
            logger.exception("详细错误:")
            return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='文献语言筛选工具 - 筛选指定语言的文献记录',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('input_file', help='输入的WOS格式文件路径')
    parser.add_argument('output_file', help='输出的筛选后文件路径')
    parser.add_argument('--language', '-l', default='English', help='目标语言 (默认: English)')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO')
    
    args = parser.parse_args()
    
    # 设置日志级别
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    # 执行筛选
    filter_tool = LanguageFilter(args.input_file, args.output_file, args.language)
    success = filter_tool.run()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
