#!/usr/bin/env python3
"""
EndNote格式WOS文件专用解析器
处理格式："AU Li, H"  "   Jia, YD" 等
"""

import re
from typing import Dict, List, Optional

class EndNoteWoSParser:
    """专门解析EndNote导出的WOS格式"""
    
    def __init__(self):
        self.records = []
        self.file_header = {}
    
    def parse_file(self, filepath: str) -> List[Dict]:
        """解析EndNote格式的WOS文件"""
        records = []
        current_record = {}
        current_field = None
        
        print(f"📖 解析EndNote格式: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if not line:
                i += 1
                continue
            
            # 移除外层引号
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1]
            
            # ===== 识别字段标签 =====
            # EndNote格式：字段标签在行首，可能带引号，后面没有固定空格
            field_match = False
            field_tag = None
            field_value = None
            
            # 常见WOS字段标签
            wos_fields = ['PT', 'AU', 'AF', 'TI', 'SO', 'LA', 'DT', 'DE', 'ID', 'AB',
                         'C1', 'RP', 'EM', 'RI', 'OI', 'FU', 'FX', 'CR', 'NR',
                         'TC', 'Z9', 'PY', 'VL', 'IS', 'BP', 'EP', 'DI', 'PG',
                         'WC', 'SC', 'UT', 'ER']
            
            # 检查行首是否是字段标签
            for field in wos_fields:
                if line.startswith(field):
                    # 字段标签后可能有空格，也可能直接跟内容
                    remainder = line[len(field):]
                    if remainder.startswith(' '):
                        field_value = remainder[1:].strip()
                    else:
                        field_value = remainder.strip()
                    field_tag = field
                    field_match = True
                    break
            
            if field_match:
                current_field = field_tag
                
                # 处理多值字段
                if field_tag in ['AU', 'AF', 'C1', 'CR']:
                    if field_tag not in current_record:
                        current_record[field_tag] = []
                    
                    # 收集这个字段的所有续行
                    full_value = field_value
                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j].strip()
                        if next_line.startswith('"') and next_line.endswith('"'):
                            next_line = next_line[1:-1]
                        
                        # 续行特征：以3个空格开头或者是带引号的续行
                        if next_line.startswith('   ') or '   ' in next_line[:10]:
                            # 提取续行内容
                            cont_value = next_line.strip()
                            if cont_value.startswith('"'):
                                cont_value = cont_value[1:]
                            if cont_value.endswith('"'):
                                cont_value = cont_value[:-1]
                            full_value += ' ' + cont_value.strip()
                            j += 1
                        else:
                            break
                    
                    current_record[field_tag].append(full_value)
                    i = j
                    continue
                
                # 普通字段
                else:
                    full_value = field_value
                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j].strip()
                        if next_line.startswith('"') and next_line.endswith('"'):
                            next_line = next_line[1:-1]
                        
                        if next_line.startswith('   '):
                            cont_value = next_line.strip()
                            full_value += ' ' + cont_value
                            j += 1
                        else:
                            break
                    
                    current_record[field_tag] = full_value
                    i = j
                    continue
            
            # 记录结束
            elif line == 'ER' or line == '"ER"':
                if current_record:
                    records.append(current_record)
                    current_record = {}
                    current_field = None
                i += 1
                continue
            
            else:
                i += 1
        
        print(f"✅ 解析完成: {len(records)} 条记录")
        return records


# 替换merge_with_repair.py中的WoSParser
import merge_with_repair
merge_with_repair.WoSParser = EndNoteWoSParser

print("✅ EndNote解析器已激活")
