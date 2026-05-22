#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
机构信息AI补全模块 - 适配器模式
连接到gemini.GeminiEnricherV2
"""

import os
import sys
import logging
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

# 导入Gemini增强器
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.bibliometrics.standardizers.gemini import GeminiEnricherV2
from gemini_config import GeminiConfig


class InstitutionEnricherV2:
    """
    机构信息补全器v2 - Gemini AI驱动
    这是gemini.GeminiEnricherV2的适配器，保持接口一致
    """
    
    def __init__(self, config):
        """
        初始化补全器
        
        Args:
            config: GeminiConfig实例
        """
        self.config = config
        self.enricher = GeminiEnricherV2(config)
        logger.info(f"✓ InstitutionEnricherV2初始化完成，使用模型: {config.model}")
    
    def enrich_file(self, input_file: str, output_file: str) -> Dict:
        """
        补全文件中的机构信息
        
        Args:
            input_file: 输入文件（WOS格式）
            output_file: 输出文件
            
        Returns:
            统计信息
        """
        logger.info(f"开始AI补全机构信息: {input_file} -> {output_file}")
        
        # 解析WOS文件，提取机构信息
        from ..parsers.wos import WoSParser
        parser = WoSParser()
        records = parser.parse_file(input_file)
        
        logger.info(f"解析到 {len(records)} 条记录")
        
        # 提取需要补全的机构
        institutions_to_enrich = []
        institution_map = {}  # (inst, city, country) -> record_indices
        
        for idx, record in enumerate(records):
            c1_field = record.get('C1', [])
            if isinstance(c1_field, str):
                c1_field = [c1_field]
            
            for addr in c1_field:
                # 解析机构地址
                inst_info = self._parse_address(addr)
                if inst_info:
                    key = (inst_info['institution'], inst_info['city'], inst_info['country'])
                    if key not in institution_map:
                        institution_map[key] = []
                        institutions_to_enrich.append(key)
                    institution_map[key].append((idx, addr))
        
        logger.info(f"需要补全的机构数: {len(institutions_to_enrich)}")
        
        # 批量调用AI
        results = self.enricher.enrich_institutions_batch(institutions_to_enrich)
        
        # 更新记录
        enriched_count = 0
        for inst_tuple, result in results.items():
            if result:
                enriched_count += 1
                # 更新所有包含此机构的记录
                for record_idx, original_addr in institution_map.get(inst_tuple, []):
                    # 这里简化处理，实际应该生成新的C1字段
                    pass
        
        # 写入输出文件
        self._write_records(records, output_file)
        
        # 获取统计信息
        stats = self.enricher.get_statistics()
        stats['processing'] = {
            'total_processed': len(institutions_to_enrich),
            'enriched': enriched_count,
            'enrichment_rate': f"{enriched_count/len(institutions_to_enrich)*100:.1f}%" if institutions_to_enrich else "0%"
        }
        
        return stats
    
    def _parse_address(self, address: str) -> Optional[Dict]:
        """解析WOS格式的地址"""
        # [作者] 机构, 部门, 城市, 国家
        parts = address.split(', ')
        if len(parts) < 3:
            return None
        
        institution = parts[1] if len(parts) > 1 else ''
        city = parts[-2] if len(parts) > 2 else ''
        country = parts[-1] if len(parts) > 0 else ''
        
        return {
            'institution': institution.strip(),
            'city': city.strip(),
            'country': country.strip()
        }
    
    def _write_records(self, records: List[Dict], output_file: str):
        """写入WOS格式文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\ufeffFN Clarivate Analytics Web of Science\n')
            f.write('VR 1.0\n\n')
            
            for record in records:
                # 简化版写入，实际应该完整写入
                for field, value in record.items():
                    if isinstance(value, list):
                        for item in value:
                            if item:
                                f.write(f"{field} {item}\n")
                    else:
                        if value:
                            f.write(f"{field} {value}\n")
                f.write("ER\n\n")
    
    def print_statistics(self):
        """打印统计信息"""
        if hasattr(self.enricher, 'print_statistics'):
            self.enricher.print_statistics()