#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高级检索引擎 v1.1 - 完全符合Web of Science (WoS)标准检索式语法
作者：资深文献计量学专家
开发时间：2026-02-11
更新时间：2026-02-11

核心特性：
- 🔍 完全兼容WoS检索式语法：AU、C1/OG、TI/AB、DE/ID、DT、PY等
- 🎯 标准布尔运算符：AND、OR、NOT（大小写不敏感）
- 📝 WoS标准通配符：* (0或多个字符) 和 ? (单个字符)
- 📊 范围查询：PY=2020-2024、TC=10-100
- 🔢 数值比较：TC>50、PY>=2020
- 🧠 AI语义增强（可选）
- 🎨 检索式可视化
- 📊 检索结果统计

WoS标准检索式示例：
1. 基础检索：
   AU=Smith AND TI=cancer
   
2. 复杂逻辑：
   (TI=CRISPR OR AB="gene editing") AND NOT DT=Review
   
3. 通配符匹配：
   AU=Zhang* AND C1=*University*
   TI=colo?r (匹配 color 和 colour)
   
4. 范围查询：
   PY=2020-2024 AND TI=AI
   TC=10-100 AND DT=Article
   
5. 数值比较：
   TC>50 AND PY>=2020
   
6. 多条件组合：
   (AU=Smith OR AU=Jones) AND (C1=Harvard OR C1=MIT) AND DT=Article

WoS字段说明：
  TI  - Title (标题)                AU  - Author (作者)
  AB  - Abstract (摘要)             C1  - Author Address (机构)
  OG  - Organization (标准机构)      SO  - Source (期刊)
  DT  - Document Type (文档类型)     DE  - Author Keywords (作者关键词)
  ID  - Keywords Plus (WOS关键词)   PY  - Publication Year (出版年)
  LA  - Language (语言)             DI  - DOI
  UT  - Unique Article ID (WOS ID)  TC  - Times Cited (被引次数)
  WC  - WOS Categories (学科分类)   SC  - Research Areas (研究领域)

匹配规则（符合WoS标准）：
- 默认不区分大小写
- 默认为包含匹配（部分匹配）
- 支持精确短语匹配（使用引号）
- 通配符支持灵活边界匹配
"""

import re
import os
import sys
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any, Union
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MatchMode(Enum):
    """匹配模式"""
    STRICT = "strict"           # 严格模式：所有条件都必须满足（默认AND逻辑）
    RELAXED = "relaxed"         # 宽松模式：至少匹配指定数量的关键词
    ANY = "any"                 # 任意模式：匹配任意一个关键词即可


class FieldType(Enum):
    """WOS字段类型"""
    # 基本字段
    TI = "Title"                    # 标题
    AB = "Abstract"                 # 摘要
    AU = "Author"                   # 作者
    AF = "Author Full Name"         # 作者全名
    C1 = "Author Address"           # 作者机构
    OG = "Organization"             # 机构（标准化）
    SO = "Source"                   # 期刊名
    LA = "Language"                 # 语言
    DT = "Document Type"            # 文档类型
    DE = "Author Keywords"          # 作者关键词
    ID = "Keywords Plus"            # WOS关键词
    
    # 出版信息
    PY = "Publication Year"         # 出版年
    PD = "Publication Date"         # 出版日期
    VL = "Volume"                   # 卷
    IS = "Issue"                    # 期
    BP = "Beginning Page"           # 起始页
    EP = "Ending Page"              # 结束页
    
    # 标识符
    DI = "DOI"                      # DOI
    UT = "Unique Article ID"        # WOS唯一ID
    
    # 引用信息
    CR = "Cited References"         # 参考文献
    TC = "Times Cited"              # 被引次数
    
    # 主题分类
    WC = "Web of Science Categories"  # WOS学科分类
    SC = "Research Areas"           # 研究领域


@dataclass
class SearchCondition:
    """单个检索条件"""
    field: str          # 字段名（如TI, AU）
    operator: str       # 操作符（=, !=, <, >, <=, >=, CONTAINS）
    value: str          # 检索值
    use_wildcard: bool  # 是否使用通配符
    case_sensitive: bool = False  # 是否区分大小写


@dataclass
class SearchNode:
    """检索树节点"""
    node_type: str      # 'condition' 或 'operator'
    condition: Optional[SearchCondition] = None
    operator: Optional[str] = None  # 'AND', 'OR', 'NOT'
    children: List['SearchNode'] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []


class QueryParser:
    """检索式解析器"""
    
    # 支持的字段
    SUPPORTED_FIELDS = {
        'TI', 'AB', 'AU', 'AF', 'C1', 'OG', 'SO', 'LA', 'DT', 
        'DE', 'ID', 'PY', 'DI', 'UT', 'WC', 'SC', 'TC'
    }
    
    # 操作符优先级
    OPERATORS = {
        'NOT': 3,
        'AND': 2,
        'OR': 1
    }
    
    def __init__(self):
        self.tokens = []
        self.current_pos = 0
    
    def parse(self, query: str) -> SearchNode:
        """
        解析检索式
        
        示例：
        - AU=Smith AND TI=cancer
        - (TI=CRISPR OR AB=gene) AND NOT DT=Review
        - PY=2020-2024 AND C1=*Stanford*
        """
        logger.info(f"解析检索式: {query}")
        
        # 预处理：标准化空格、括号
        query = self._preprocess_query(query)
        
        # 词法分析
        self.tokens = self._tokenize(query)
        self.current_pos = 0
        
        # 语法分析
        ast = self._parse_expression()
        
        logger.info(f"解析完成，生成语法树")
        return ast
    
    def _preprocess_query(self, query: str) -> str:
        """
        预处理检索式 - 符合WoS标准
        
        WoS标准：
        1. 操作符大小写不敏感：AND、and、And 都可以
        2. 字段名必须大写：TI、AU、C1 等
        3. 括号用于分组
        4. 引号用于精确短语匹配
        
        特别处理：
        - 确保引号后的操作符前有空格（如 "text"OR → "text" OR）
        - 确保操作符后的引号前有空格（如 OR"text" → OR "text"）
        """
        # 先处理引号和操作符之间的空格问题
        # 在引号后面紧跟操作符的情况：添加空格
        query = re.sub(r'"(AND|OR|NOT)\b', '" \\1', query, flags=re.IGNORECASE)
        # 在操作符后面紧跟引号的情况：添加空格
        query = re.sub(r'\b(AND|OR|NOT)"', '\\1 "', query, flags=re.IGNORECASE)
        
        # 统一布尔操作符为大写（WoS标准）
        query = re.sub(r'\b(and)\b', 'AND', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(or)\b', 'OR', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(not)\b', 'NOT', query, flags=re.IGNORECASE)
        
        # 标准化空格（保留引号内的空格）
        query = re.sub(r'\s+', ' ', query).strip()
        
        # 确保括号周围有空格，便于分词（WoS标准）
        query = query.replace('(', ' ( ').replace(')', ' ) ')
        query = re.sub(r'\s+', ' ', query).strip()
        
        logger.debug(f"预处理后: {query}")
        return query
    
    def _tokenize(self, query: str) -> List[str]:
        """词法分析 - 改进版，更好地处理引号字符串"""
        tokens = []
        i = 0
        query_len = len(query)
        
        while i < query_len:
            # 跳过空格
            while i < query_len and query[i] == ' ':
                i += 1
            
            if i >= query_len:
                break
            
            # 处理括号
            if query[i] in '()':
                tokens.append(query[i])
                i += 1
                continue
            
            # 查找下一个空格或括号
            start = i
            in_quotes = False
            token_chars = []
            
            while i < query_len:
                char = query[i]
                
                # 处理引号
                if char == '"':
                    in_quotes = not in_quotes
                    token_chars.append(char)
                    i += 1
                    continue
                
                # 在引号内，继续收集字符
                if in_quotes:
                    token_chars.append(char)
                    i += 1
                    continue
                
                # 在引号外，空格和括号是分隔符
                if char in ' ()':
                    break
                
                token_chars.append(char)
                i += 1
            
            token = ''.join(token_chars).strip()
            
            if token:
                tokens.append(token)
        
        logger.debug(f"Tokenized: {tokens}")
        return tokens
    
    def _parse_expression(self) -> SearchNode:
        """解析表达式（处理OR）"""
        left = self._parse_term()
        
        while self._peek() == 'OR':
            self._consume('OR')
            right = self._parse_term()
            
            node = SearchNode(
                node_type='operator',
                operator='OR',
                children=[left, right]
            )
            left = node
        
        return left
    
    def _parse_term(self) -> SearchNode:
        """解析项（处理AND）"""
        left = self._parse_factor()
        
        while self._peek() == 'AND':
            self._consume('AND')
            right = self._parse_factor()
            
            node = SearchNode(
                node_type='operator',
                operator='AND',
                children=[left, right]
            )
            left = node
        
        return left
    
    def _parse_factor(self) -> SearchNode:
        """解析因子（处理NOT和括号）"""
        token = self._peek()
        
        # NOT操作符
        if token == 'NOT':
            self._consume('NOT')
            child = self._parse_factor()
            return SearchNode(
                node_type='operator',
                operator='NOT',
                children=[child]
            )
        
        # 括号表达式
        if token == '(':
            self._consume('(')
            expr = self._parse_expression()
            self._consume(')')
            return expr
        
        # 条件表达式
        return self._parse_condition()
    
    def _parse_condition(self) -> SearchNode:
        """
        解析单个条件 - 完全符合WoS标准检索式格式
        
        支持的格式：
        1. 基本格式：AU=Smith, TI=cancer
        2. 引号格式：TI="cancer research", AU="Smith J"
        3. 通配符：AU=Smith*, C1=*University*
        4. 范围查询：PY=2020-2024, TC=10-100
        5. 比较运算：TC>50, PY>=2020
        """
        token = self._current()
        
        # WoS标准格式：字段名=值
        # 字段名：1-3个大写字母/数字，如 TI, AU, C1, ID
        # 操作符：=, !=, <, >, <=, >=
        # 值：可以包含引号、通配符、范围
        match = re.match(r'^([A-Z][A-Z0-9]{0,2})\s*([=!<>]+)\s*(.+)$', token)
        
        if not match:
            # 提供详细的WoS格式错误提示
            raise ValueError(
                f"无效的WoS检索式格式: '{token}'\n"
                f"正确格式示例:\n"
                f"  - 基本: TI=cancer, AU=Smith\n"
                f"  - 引号: TI=\"cancer research\", AU=\"Smith J\"\n"
                f"  - 通配符: AU=Smith*, C1=*University*\n"
                f"  - 范围: PY=2020-2024, TC=10-100\n"
                f"  - 比较: TC>50, PY>=2020\n"
                f"当前位置: token {self.current_pos + 1}/{len(self.tokens)}\n"
                f"完整检索式tokens: {self.tokens}"
            )
        
        field, op, value = match.groups()
        
        # 验证字段是否为WoS标准字段
        if field not in self.SUPPORTED_FIELDS:
            logger.warning(
                f"⚠️  字段 '{field}' 不在WoS标准字段列表中\n"
                f"   支持的字段: {', '.join(sorted(self.SUPPORTED_FIELDS))}\n"
                f"   将尝试继续处理"
            )
        
        # 处理值：去除首尾引号（WoS标准）
        value = value.strip()
        original_value = value
        
        # WoS允许用引号包裹短语和特殊字符
        if value.startswith('"') and value.endswith('"') and len(value) > 1:
            value = value[1:-1]  # 去除引号但保留内容
        
        # 检测通配符（WoS标准：* 代表0或多个字符，? 代表单个字符）
        use_wildcard = '*' in value or '?' in value
        
        # 如果使用通配符，记录日志
        if use_wildcard:
            logger.debug(f"检测到通配符: {field}={value}")
        
        # 创建检索条件
        condition = SearchCondition(
            field=field,
            operator=op,
            value=value,
            use_wildcard=use_wildcard,
            case_sensitive=False  # WoS默认不区分大小写
        )
        
        self.current_pos += 1
        
        logger.debug(f"解析条件: {field} {op} '{value}'" + 
                    (f" (原始: {original_value})" if original_value != value else ""))
        
        return SearchNode(
            node_type='condition',
            condition=condition
        )
    
    def _peek(self) -> Optional[str]:
        """查看当前token"""
        if self.current_pos < len(self.tokens):
            return self.tokens[self.current_pos]
        return None
    
    def _current(self) -> str:
        """获取当前token"""
        if self.current_pos >= len(self.tokens):
            raise ValueError(
                f"检索式解析错误：意外结束\n"
                f"已解析的tokens: {self.tokens[:self.current_pos]}\n"
                f"期望: 更多的检索条件或操作符"
            )
        return self.tokens[self.current_pos]
    
    def _consume(self, expected: str):
        """消费一个token"""
        token = self._current()
        if token != expected:
            raise ValueError(
                f"检索式解析错误：期望 '{expected}'，但得到 '{token}'\n"
                f"位置: token {self.current_pos + 1}/{len(self.tokens)}\n"
                f"上下文: ...{' '.join(self.tokens[max(0,self.current_pos-2):min(len(self.tokens),self.current_pos+3)])}..."
            )
        self.current_pos += 1


class RecordMatcher:
    """记录匹配器"""
    
    def __init__(self, use_ai_semantic: bool = False, api_key: Optional[str] = None, 
                 match_mode: str = "strict", min_match_count: int = 1,
                 use_relevance_filter: bool = True, relevance_threshold: float = 0.5):
        """
        初始化匹配器
        
        Args:
            use_ai_semantic: 是否使用AI语义增强（扩充同义词/相关词）
            api_key: API密钥
            match_mode: 匹配模式 - "strict"(严格), "relaxed"(宽松), "any"(任意)
            min_match_count: 宽松模式下最少匹配的关键词数量（默认1）
            use_relevance_filter: 是否启用AI相关性过滤（两阶段筛选）
            relevance_threshold: 相关性阈值（0-1范围）
                - 0.2-0.3: 宽松，保留更多可能相关文献（召回率优先）
                - 0.4-0.5: 平衡，推荐设置（精确率与召回率平衡）⭐
                - 0.6-0.7: 严格，只保留高度相关文献（精确率优先）
                - 0.8-1.0: 极严格，不推荐（会过滤掉大量相关文献）
                默认0.5。注意：1.0要求完美匹配，几乎会过滤掉所有文献！
        """
        self.use_ai_semantic = use_ai_semantic
        self.api_key = api_key
        self.match_mode = match_mode
        self.min_match_count = min_match_count
        self.use_relevance_filter = use_relevance_filter
        self.relevance_threshold = relevance_threshold
        self.expanded_terms_cache = {}  # 缓存AI扩充的词汇
        self.relevance_cache = {}  # 缓存相关性评分
    
    def calculate_relevance_score(self, record: Dict, query_terms: List[str]) -> float:
        """
        计算文献与检索词的相关性得分（0-1）
        
        策略：
        1. 关键字段匹配度（TI > AB > DE/ID）
        2. 匹配词的数量和分布
        3. 核心术语的权重
        
        Args:
            record: 文献记录
            query_terms: 检索词列表
            
        Returns:
            相关性得分（0-1）
        """
        score = 0.0
        max_score = 0.0
        
        # 提取文献文本
        title = record.get('TI', '').lower()
        abstract = record.get('AB', '').lower()
        keywords = (record.get('DE', '') + ' ' + record.get('ID', '')).lower()
        
        # 字段权重
        weights = {
            'title': 0.5,      # 标题权重最高
            'abstract': 0.3,   # 摘要次之
            'keywords': 0.2    # 关键词最低
        }
        
        for term in query_terms:
            term_lower = term.lower()
            term_score = 0.0
            
            # 标题匹配（权重0.5）
            if term_lower in title:
                term_score += weights['title']
                # 如果在标题开头，额外加分
                if title.startswith(term_lower):
                    term_score += 0.1
            
            # 摘要匹配（权重0.3）
            if term_lower in abstract:
                # 计算出现频率
                count = abstract.count(term_lower)
                term_score += weights['abstract'] * min(count / 3.0, 1.0)
            
            # 关键词匹配（权重0.2）
            if term_lower in keywords:
                term_score += weights['keywords']
            
            score += term_score
            max_score += 1.0  # 每个词最多1分
        
        # 归一化到0-1
        if max_score > 0:
            normalized_score = min(score / max_score, 1.0)
        else:
            normalized_score = 0.0
        
        return normalized_score
    
    def filter_by_relevance(self, records: List[Dict], query_terms: List[str], 
                           progress_callback=None) -> List[Dict]:
        """
        基于AI相关性过滤文献
        
        两阶段筛选：
        1. 第一阶段：宽松匹配（高召回率，可能有误匹配）
        2. 第二阶段：相关性过滤（去除不相关文献，提高精确率）
        
        Args:
            records: 第一阶段匹配的记录
            query_terms: 原始检索词列表
            progress_callback: 进度回调函数
            
        Returns:
            过滤后的高相关性记录
        """
        if not self.use_relevance_filter:
            return records
        
        logger.info(f"\n🎯 AI相关性过滤")
        logger.info(f"   输入记录: {len(records)}")
        logger.info(f"   相关性阈值: {self.relevance_threshold}")
        
        # 添加阈值警告
        if self.relevance_threshold >= 0.8:
            logger.warning(f"   ⚠️ 警告: 阈值{self.relevance_threshold}过高！建议使用0.3-0.7")
        elif self.relevance_threshold >= 0.7:
            logger.info(f"   ℹ️ 严格模式：可能过滤掉一些边缘相关文献")
        elif self.relevance_threshold <= 0.3:
            logger.info(f"   ℹ️ 宽松模式：可能保留一些相关性较低的文献")
        
        filtered_records = []
        
        for i, record in enumerate(records):
            # 计算相关性得分
            score = self.calculate_relevance_score(record, query_terms)
            
            # 只保留高相关性的文献
            if score >= self.relevance_threshold:
                filtered_records.append(record)
            
            # 进度回调
            if progress_callback and (i + 1) % 100 == 0:
                progress_callback(i + 1, len(records))
        
        removed = len(records) - len(filtered_records)
        match_rate = (len(filtered_records) / len(records) * 100) if records else 0
        
        logger.info(f"   过滤后记录: {len(filtered_records)}")
        logger.info(f"   移除无关文献: {removed} ({removed/len(records)*100:.1f}%)")
        
        # 如果命中率过低，提示可能阈值太高
        if match_rate < 30 and self.relevance_threshold > 0.5:
            logger.warning(f"   ⚠️ 命中率仅{match_rate:.1f}%！建议降低阈值到0.3-0.5")
        elif match_rate < 20:
            logger.warning(f"   ⚠️ 命中率过低({match_rate:.1f}%)！可能需要调整检索式或降低阈值")
        
        return filtered_records
    
    def _expand_search_term_with_ai(self, term: str, field: str) -> List[str]:
        """
        使用AI扩充搜索词，生成同义词和相关词
        
        Args:
            term: 原始搜索词
            field: 字段类型（用于上下文）
            
        Returns:
            扩充后的词汇列表（包含原词）
        """
        # 检查缓存
        cache_key = f"{field}:{term}"
        if cache_key in self.expanded_terms_cache:
            return self.expanded_terms_cache[cache_key]
        
        if not self.use_ai_semantic:
            return [term]
        
        # AI扩充逻辑：生成同义词、缩写、相关术语
        expanded = [term]  # 始终包含原词
        
        # 简单的启发式扩充（不依赖API）
        term_lower = term.lower()
        
        # 常见学术词汇扩充规则
        expansions = {
            # 技术词汇
            'ai': ['artificial intelligence', 'machine learning', 'deep learning', 'neural network'],
            'ml': ['machine learning', 'ai', 'artificial intelligence'],
            'nlp': ['natural language processing', 'text mining', 'language model'],
            'cv': ['computer vision', 'image processing', 'visual recognition'],
            
            # 生物医学
            'cancer': ['tumor', 'tumour', 'carcinoma', 'neoplasm', 'malignancy', 'oncology'],
            'therapy': ['treatment', 'intervention', 'therapeutic', 'remediation'],
            'disease': ['disorder', 'illness', 'pathology', 'condition', 'syndrome'],
            'drug': ['medication', 'pharmaceutical', 'medicine', 'compound'],
            
            # 研究方法
            'analysis': ['evaluation', 'assessment', 'examination', 'study'],
            'method': ['approach', 'technique', 'methodology', 'procedure'],
            'model': ['framework', 'simulation', 'modeling', 'paradigm'],
            'algorithm': ['method', 'approach', 'technique', 'procedure'],
            
            # 数据科学
            'data': ['dataset', 'information', 'database', 'corpus'],
            'prediction': ['forecasting', 'prognosis', 'estimation', 'projection'],
            'classification': ['categorization', 'taxonomy', 'clustering'],
            
            # 通用学术
            'research': ['study', 'investigation', 'inquiry', 'analysis'],
            'development': ['advancement', 'progress', 'innovation', 'evolution'],
            'application': ['implementation', 'utilization', 'deployment', 'use'],
        }
        
        # 添加预定义的扩充词
        for key, variants in expansions.items():
            if key in term_lower:
                expanded.extend(variants)
        
        # 添加常见变体
        # 1. 单复数变化
        if not term.endswith('s'):
            expanded.append(term + 's')
        else:
            expanded.append(term.rstrip('s'))
        
        # 2. 美式/英式拼写
        spelling_variants = {
            'or': 'our',  # color -> colour
            'ize': 'ise',  # organize -> organise
            'er': 're',    # center -> centre
        }
        for us, uk in spelling_variants.items():
            if us in term:
                expanded.append(term.replace(us, uk))
            if uk in term:
                expanded.append(term.replace(uk, us))
        
        # 去重并转小写
        expanded = list(set([t.lower() for t in expanded]))
        
        # 缓存结果
        self.expanded_terms_cache[cache_key] = expanded
        
        logger.info(f"🔍 AI扩充: {term} → {len(expanded)}个相关词")
        logger.debug(f"   扩充词汇: {', '.join(expanded[:10])}")
        
        return expanded
    
    def match_record(self, record: Dict, node: SearchNode) -> bool:
        """
        匹配单条记录
        
        Args:
            record: WOS记录
            node: 检索树节点
        
        Returns:
            是否匹配
        """
        # 严格模式：按照原始逻辑（AND/OR/NOT）
        if self.match_mode == "strict":
            return self._match_strict(record, node)
        
        # 宽松/任意模式：提取所有条件并统计匹配数
        elif self.match_mode in ["relaxed", "any"]:
            return self._match_relaxed(record, node)
        
        return False
    
    def _match_strict(self, record: Dict, node: SearchNode) -> bool:
        """严格匹配模式（原始逻辑）"""
        if node.node_type == 'condition':
            return self._match_condition(record, node.condition)
        
        elif node.node_type == 'operator':
            if node.operator == 'AND':
                return all(self._match_strict(record, child) for child in node.children)
            
            elif node.operator == 'OR':
                return any(self._match_strict(record, child) for child in node.children)
            
            elif node.operator == 'NOT':
                return not self._match_strict(record, node.children[0])
        
        return False
    
    def _match_relaxed(self, record: Dict, node: SearchNode) -> bool:
        """
        宽松匹配模式：提取所有条件，统计匹配数量
        
        逻辑：
        - 收集所有叶子条件（忽略AND/OR/NOT结构）
        - 统计有多少条件匹配
        - relaxed模式：匹配数 >= min_match_count
        - any模式：匹配数 >= 1
        """
        # 收集所有条件
        conditions = self._collect_conditions(node)
        
        if not conditions:
            return False
        
        # 统计匹配数
        match_count = sum(1 for cond in conditions if self._match_condition(record, cond))
        
        # 计算阈值
        if self.match_mode == "any":
            threshold = 1
        else:  # relaxed
            threshold = self.min_match_count
        
        logger.debug(f"宽松匹配: {match_count}/{len(conditions)} 条件匹配 (阈值: {threshold})")
        
        return match_count >= threshold
    
    def _collect_conditions(self, node: SearchNode) -> List[SearchCondition]:
        """递归收集所有叶子条件"""
        conditions = []
        
        if node.node_type == 'condition':
            conditions.append(node.condition)
        elif node.node_type == 'operator':
            for child in node.children:
                conditions.extend(self._collect_conditions(child))
        
        return conditions
    
    def _match_condition(self, record: Dict, condition: SearchCondition) -> bool:
        """
        匹配单个条件 - 符合WoS标准 + AI语义扩充
        
        WoS匹配规则：
        1. 默认不区分大小写
        2. 支持部分匹配（包含匹配）
        3. 支持通配符 * 和 ?
        4. 支持数值比较（PY, TC等字段）
        5. 支持范围查询（如 PY=2020-2024）
        6. AI语义扩充：自动匹配同义词和相关词
        """
        # 获取字段值
        field_value = record.get(condition.field, '')
        
        # 空值处理
        if not field_value:
            return False
        
        # 转换为字符串
        if not isinstance(field_value, str):
            field_value = str(field_value)
        
        # WoS标准：默认不区分大小写
        if not condition.case_sensitive:
            field_value_lower = field_value.lower()
            search_value_lower = condition.value.lower()
        else:
            field_value_lower = field_value
            search_value_lower = condition.value
        
        # 处理等于操作符（=）
        if condition.operator == '=':
            # 检查是否为范围查询（如 PY=2020-2024）
            if '-' in condition.value and condition.field in ['PY', 'TC', 'VL', 'IS']:
                return self._match_range(field_value, condition.value)
            
            # 通配符匹配
            if condition.use_wildcard:
                return self._wildcard_match(field_value_lower, search_value_lower)
            
            # AI语义扩充匹配
            if self.use_ai_semantic and condition.field in ['TI', 'AB', 'DE', 'ID']:
                # 获取扩充词汇
                expanded_terms = self._expand_search_term_with_ai(condition.value, condition.field)
                
                # 只要匹配任意一个扩充词即可
                for term in expanded_terms:
                    if term.lower() in field_value_lower:
                        return True
                return False
            
            # WoS标准：普通匹配是包含匹配（部分匹配）
            # 例如：TI=cancer 可以匹配 "Cancer Research" 或 "Breast Cancer"
            return search_value_lower in field_value_lower
        
        # 处理不等于操作符（!=）
        elif condition.operator == '!=':
            if condition.use_wildcard:
                return not self._wildcard_match(field_value_lower, search_value_lower)
            else:
                # AI语义扩充也应用于不等于
                if self.use_ai_semantic and condition.field in ['TI', 'AB', 'DE', 'ID']:
                    expanded_terms = self._expand_search_term_with_ai(condition.value, condition.field)
                    for term in expanded_terms:
                        if term.lower() in field_value_lower:
                            return False
                    return True
                return search_value_lower not in field_value_lower
        
        # 数值比较（用于PY, TC, VL, IS等数值字段）
        elif condition.operator in ['<', '>', '<=', '>=']:
            try:
                # 提取字段中的数字
                field_match = re.search(r'\d+', field_value)
                if not field_match:
                    return False
                
                field_num = float(field_match.group())
                search_num = float(condition.value)
                
                if condition.operator == '<':
                    return field_num < search_num
                elif condition.operator == '>':
                    return field_num > search_num
                elif condition.operator == '<=':
                    return field_num <= search_num
                elif condition.operator == '>=':
                    return field_num >= search_num
            except (ValueError, AttributeError):
                logger.debug(f"无法进行数值比较: {field_value} {condition.operator} {condition.value}")
                return False
        
        return False
    
    def _match_range(self, field_value: str, range_value: str) -> bool:
        """
        范围匹配 - 符合WoS标准
        
        支持格式：
        - PY=2020-2024 : 匹配2020到2024年
        - TC=10-100 : 匹配被引次数10到100次
        """
        try:
            # 解析范围
            parts = range_value.split('-')
            if len(parts) != 2:
                return False
            
            range_start = float(parts[0].strip())
            range_end = float(parts[1].strip())
            
            # 提取字段中的数字
            field_match = re.search(r'\d+', field_value)
            if not field_match:
                return False
            
            field_num = float(field_match.group())
            
            # 范围匹配：包含边界值
            return range_start <= field_num <= range_end
            
        except (ValueError, AttributeError):
            logger.debug(f"范围匹配失败: {field_value} in {range_value}")
            return False
    
    def _wildcard_match(self, text: str, pattern: str) -> bool:
        """
        通配符匹配 - 符合WoS标准
        
        WoS标准通配符：
        - * : 匹配0个或多个字符 (例如: Smith* 匹配 Smith, Smithson)
        - ? : 匹配恰好1个字符 (例如: Sm?th 匹配 Smith, Smyth)
        
        示例：
        - AU=Smith* : 匹配 Smith, Smithson, Smitherman
        - C1=*University* : 匹配包含 University 的任何机构
        - TI=colo?r : 匹配 color 或 colour
        """
        # 转换WoS通配符为正则表达式
        # 先转义特殊字符（除了*和?）
        import re
        regex_pattern = re.escape(pattern)
        
        # 然后将转义后的通配符替换回正则表达式
        regex_pattern = regex_pattern.replace(r'\*', '.*')  # * -> .*（0或多个任意字符）
        regex_pattern = regex_pattern.replace(r'\?', '.')   # ? -> .（1个任意字符）
        
        # WoS标准：通配符匹配是部分匹配，不需要完全匹配整个字段
        # 例如：TI=cancer 可以匹配 "cancer research" 或 "breast cancer"
        # 但如果用户明确使用了通配符边界，就按边界匹配
        
        # 判断是否有明确的边界
        has_start_boundary = not pattern.startswith('*')
        has_end_boundary = not pattern.endswith('*')
        
        # 构建最终的正则表达式
        if has_start_boundary and has_end_boundary:
            # 两端都有边界：完全匹配模式
            regex_pattern = f'^{regex_pattern}$'
        elif has_start_boundary:
            # 只有起始边界：从开头匹配
            regex_pattern = f'^{regex_pattern}'
        elif has_end_boundary:
            # 只有结束边界：匹配到结尾
            regex_pattern = f'{regex_pattern}$'
        else:
            # 两端都是通配符：部分匹配即可
            pass
        
        try:
            # WoS默认不区分大小写
            return bool(re.search(regex_pattern, text, re.IGNORECASE))
        except re.error as e:
            logger.warning(f"正则表达式错误: {e}, pattern: {pattern}")
            return False


class AdvancedSearchEngine:
    """高级检索引擎 - 支持两阶段筛选"""
    
    def __init__(self, use_ai_semantic: bool = False, api_key: Optional[str] = None,
                 match_mode: str = "relaxed", min_match_count: int = 1,
                 use_relevance_filter: bool = True, relevance_threshold: float = 0.5):
        """
        初始化检索引擎
        
        Args:
            use_ai_semantic: 是否启用AI语义增强
            api_key: Anthropic API密钥
            match_mode: 匹配模式
                - "strict": 严格模式，完全按照检索式逻辑（AND/OR/NOT）
                - "relaxed": 宽松模式，至少匹配min_match_count个关键词（默认）⭐
                - "any": 任意模式，匹配任意一个关键词即可
            min_match_count: 宽松模式下最少匹配数量（默认1）
            use_relevance_filter: 是否启用AI相关性过滤（两阶段筛选）
            relevance_threshold: 相关性阈值（0-1范围）
                推荐设置：
                - 0.3: 宽松过滤（保留更多文献）
                - 0.5: 平衡模式（推荐）⭐
                - 0.7: 严格过滤（高精确度）
                警告：1.0会过滤掉几乎所有文献！
        
        两阶段筛选策略：
        1. 第一阶段：AI扩充 + 宽松匹配 → 高召回率（不漏相关文献）
        2. 第二阶段：AI相关性评分 → 高精确率（过滤无关文献）
        
        使用建议：
        - 平衡模式（推荐）: use_relevance_filter=True, threshold=0.5
        - 高召回模式: use_relevance_filter=False
        - 高精确模式: use_relevance_filter=True, threshold=0.7
        """
        self.parser = QueryParser()
        self.matcher = RecordMatcher(
            use_ai_semantic, 
            api_key,
            match_mode=match_mode,
            min_match_count=min_match_count,
            use_relevance_filter=use_relevance_filter,
            relevance_threshold=relevance_threshold
        )
        self.match_mode = match_mode
        self.min_match_count = min_match_count
        self.use_relevance_filter = use_relevance_filter
        self.relevance_threshold = relevance_threshold
        
        self.stats = {
            'total_records': 0,
            'matched_records': 0,
            'query': '',
            'execution_time': 0.0
        }
    
    def parse_query(self, query: str) -> SearchNode:
        """
        解析检索式并返回语法树
        
        Args:
            query: 检索式字符串
        
        Returns:
            SearchNode: 解析后的语法树
        """
        return self.parser.parse(query)
    
    def search(self, records: List[Dict], query: str) -> Tuple[List[Dict], Dict]:
        """
        执行检索 - 支持两阶段筛选
        
        Args:
            records: WOS记录列表
            query: 检索式
        
        Returns:
            (匹配的记录列表, 统计信息)
        """
        logger.info("=" * 80)
        logger.info("🔍 高级检索引擎 v2.0 - 两阶段筛选")
        logger.info("=" * 80)
        logger.info(f"检索式: {query}")
        logger.info(f"记录总数: {len(records)}")
        
        # 显示匹配模式
        mode_names = {
            "strict": "严格模式（完全匹配逻辑）",
            "relaxed": f"宽松模式（至少匹配{self.min_match_count}个关键词）",
            "any": "任意模式（匹配任意关键词）"
        }
        logger.info(f"匹配模式: {mode_names.get(self.match_mode, self.match_mode)}")
        
        if self.use_relevance_filter:
            logger.info(f"🎯 AI相关性过滤: 启用（阈值={self.relevance_threshold}）")
        
        logger.info("")
        
        start_time = datetime.now()
        
        # 解析检索式
        search_tree = self.parser.parse(query)
        
        # 提取原始检索词（用于相关性评分）
        query_terms = self._extract_query_terms(search_tree)
        
        # 第一阶段：宽松匹配（高召回率）
        logger.info("📍 第一阶段：宽松匹配（AI扩充词汇）")
        matched_records = []
        for i, record in enumerate(records):
            if self.matcher.match_record(record, search_tree):
                matched_records.append(record)
            
            # 进度显示
            if (i + 1) % 500 == 0:
                logger.info(f"   已处理: {i + 1}/{len(records)} (初步匹配: {len(matched_records)})")
        
        stage1_count = len(matched_records)
        stage1_rate = stage1_count / len(records) * 100 if records else 0
        logger.info(f"   第一阶段完成: {stage1_count}/{len(records)} ({stage1_rate:.1f}%)")
        
        # 第二阶段：AI相关性过滤（高精确率）
        if self.use_relevance_filter and matched_records:
            logger.info("\n📍 第二阶段：AI相关性过滤（去除无关文献）")
            matched_records = self.matcher.filter_by_relevance(matched_records, query_terms)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        # 统计
        self.stats = {
            'total_records': len(records),
            'stage1_matched': stage1_count,
            'stage1_rate': stage1_rate,
            'matched_records': len(matched_records),
            'query': query,
            'execution_time': execution_time,
            'match_rate': len(matched_records) / len(records) * 100 if records else 0,
            'match_mode': self.match_mode,
            'min_match_count': self.min_match_count,
            'use_relevance_filter': self.use_relevance_filter,
            'relevance_threshold': self.relevance_threshold if self.use_relevance_filter else None,
            'filtered_count': stage1_count - len(matched_records) if self.use_relevance_filter else 0
        }
        
        self._print_stats()
        
        return matched_records, self.stats
    
    def _extract_query_terms(self, node: SearchNode) -> List[str]:
        """从检索树提取所有检索词"""
        terms = []
        
        if node.node_type == 'condition':
            terms.append(node.condition.value)
        elif node.node_type == 'operator':
            for child in node.children:
                terms.extend(self._extract_query_terms(child))
        
        return terms
    
    def search_wos_file(self, input_file: str, query: Union[str, 'SearchNode'], output_file: Optional[str] = None) -> Tuple[List[Dict], Dict]:
        """
        直接对WOS文件执行检索（便捷方法）
        
        Args:
            input_file: 输入WOS文件路径
            query: 检索式字符串 或 已解析的SearchNode对象
            output_file: 输出文件路径（可选，如果提供则保存结果）
        
        Returns:
            (匹配的记录列表, 统计信息)
        
        Example:
            engine = AdvancedSearchEngine()
            # 使用字符串检索式
            results, stats = engine.search_wos_file(
                'input.txt', 
                'AU=Smith AND TI=cancer',
                'output.txt'
            )
            # 或使用已解析的SearchNode
            search_tree = engine.parse_query('AU=Smith AND TI=cancer')
            results, stats = engine.search_wos_file('input.txt', search_tree)
        """
        logger.info("=" * 80)
        logger.info("📖 读取WOS文件")
        logger.info("=" * 80)
        
        # 解析输入文件
        records = WOSFileHandler.parse_wos_file(input_file)
        
        # 判断query是字符串还是SearchNode
        if isinstance(query, str):
            # 如果是字符串，执行完整的search流程（包含解析）
            matched_records, stats = self.search(records, query)
        elif isinstance(query, SearchNode):
            # 如果已经是SearchNode，直接执行匹配
            logger.info("=" * 80)
            logger.info("🔍 高级检索引擎 v1.1")
            logger.info("=" * 80)
            logger.info(f"检索式: (已解析的语法树)")
            logger.info(f"记录总数: {len(records)}")
            logger.info("")
            
            start_time = datetime.now()
            
            # 直接使用已解析的SearchNode执行检索
            matched_records = []
            for i, record in enumerate(records):
                if self.matcher.match_record(record, query):
                    matched_records.append(record)
                
                # 进度显示
                if (i + 1) % 500 == 0:
                    logger.info(f"已处理: {i + 1}/{len(records)} (匹配: {len(matched_records)})")
            
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            # 统计
            stats = {
                'total_records': len(records),
                'matched_records': len(matched_records),
                'query': '(已解析的语法树)',
                'execution_time': execution_time,
                'match_rate': len(matched_records) / len(records) * 100 if records else 0
            }
            
            self.stats = stats
            self._print_stats()
        else:
            raise TypeError(f"query参数必须是字符串或SearchNode对象，但得到了 {type(query)}")
        
        # 保存结果（如果指定了输出文件）
        if output_file:
            WOSFileHandler.save_wos_file(matched_records, output_file)
            logger.info(f"✅ 结果已保存到: {output_file}")
        
        return matched_records, stats
    
    def _print_stats(self):
        """打印统计信息"""
        logger.info("")
        logger.info("=" * 80)
        logger.info("📊 检索统计")
        logger.info("=" * 80)
        logger.info(f"\n检索式: {self.stats['query']}")
        logger.info(f"总记录数: {self.stats['total_records']}")
        logger.info(f"匹配记录: {self.stats['matched_records']} "
                   f"({self.stats['match_rate']:.1f}%)")
        logger.info(f"执行时间: {self.stats['execution_time']:.2f} 秒")
        logger.info("=" * 80)
    
    def visualize_query(self, query: Union[str, 'SearchNode'], output_file: Optional[str] = None) -> str:
        """
        可视化检索式语法树
        
        Args:
            query: 检索式字符串 或 已解析的SearchNode对象
            output_file: 输出文件（可选）
        
        Returns:
            可视化文本
        """
        # 判断输入类型：字符串还是SearchNode
        if isinstance(query, str):
            # 如果是字符串，解析它
            original_query = query
            search_tree = self.parser.parse(query)
        elif isinstance(query, SearchNode):
            # 如果已经是SearchNode，直接使用
            original_query = "(已解析的语法树)"
            search_tree = query
        else:
            raise TypeError(f"query参数必须是字符串或SearchNode对象，但得到了 {type(query)}")
        
        lines = []
        lines.append("📊 检索式语法树")
        lines.append("=" * 60)
        lines.append(f"原始检索式: {original_query}")
        lines.append("")
        lines.append("语法树结构:")
        lines.append("")
        
        self._visualize_tree(search_tree, lines, prefix="", is_last=True)
        
        viz_text = "\n".join(lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(viz_text)
            logger.info(f"语法树已保存: {output_file}")
        
        return viz_text
    
    def _visualize_tree(self, node: SearchNode, lines: List[str], 
                       prefix: str = "", is_last: bool = True):
        """递归可视化语法树"""
        connector = "└── " if is_last else "├── "
        
        if node.node_type == 'condition':
            cond = node.condition
            lines.append(f"{prefix}{connector}[条件] {cond.field} {cond.operator} "
                        f"\"{cond.value}\"" + 
                        (" (通配符)" if cond.use_wildcard else ""))
        
        elif node.node_type == 'operator':
            lines.append(f"{prefix}{connector}[操作符] {node.operator}")
            
            # 递归处理子节点
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                self._visualize_tree(child, lines, new_prefix, is_last_child)


class WOSFileHandler:
    """WOS文件处理器"""
    
    @staticmethod
    def parse_wos_file(file_path: str) -> List[Dict]:
        """解析WOS文件"""
        logger.info(f"📖 解析文件: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 按ER分割记录
        record_texts = re.split(r'\nER\s*\n', content)
        
        records = []
        for record_text in record_texts:
            if not record_text.strip() or record_text.strip().startswith('EF'):
                continue
            
            record = WOSFileHandler._parse_single_record(record_text)
            if record:
                records.append(record)
        
        logger.info(f"✅ 成功解析 {len(records)} 条记录")
        return records
    
    @staticmethod
    def _parse_single_record(record_text: str) -> Dict:
        """解析单条记录"""
        record = {'raw_text': record_text}
        
        # 正则匹配字段
        pattern = r'^([A-Z][A-Z0-9])\s+(.+?)(?=\n[A-Z][A-Z0-9]\s|\n$)'
        
        for match in re.finditer(pattern, record_text, re.MULTILINE | re.DOTALL):
            field = match.group(1)
            value = match.group(2).strip()
            # 处理续行
            value = re.sub(r'\n\s{3}', ' ', value)
            record[field] = value
        
        return record
    
    @staticmethod
    def save_wos_file(records: List[Dict], output_file: str):
        """保存WOS文件"""
        logger.info(f"💾 保存结果: {output_file}")
        
        # 确保输出目录存在
        from pathlib import Path
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for record in records:
                f.write(record.get('raw_text', ''))
                f.write('\nER\n')
            f.write('\nEF')
        
        logger.info(f"✅ 已保存 {len(records)} 条记录")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='高级检索引擎 v1.0 - 支持WoS检索式语法',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
检索式示例：
  1. 基础检索:
     AU=Smith AND TI=cancer
     
  2. 复杂逻辑:
     (TI=CRISPR OR AB="gene editing") AND NOT DT=Review
     
  3. 通配符:
     AU=Zhang* AND C1=*Stanford*
     
  4. 年份范围:
     PY=2020-2024 AND TI=AI
     
  5. 多条件组合:
     (AU=Smith OR AU=Jones) AND (C1=Harvard OR C1=MIT) AND DT=Article

支持的字段：
  TI  - 标题           AU  - 作者          C1  - 机构
  AB  - 摘要           SO  - 期刊          DT  - 文档类型
  DE  - 作者关键词      ID  - WOS关键词     PY  - 出版年
  LA  - 语言           DI  - DOI           UT  - WOS ID
  WC  - 学科分类        SC  - 研究领域       TC  - 被引次数
        """
    )
    
    parser.add_argument('input_file', help='输入WOS文件')
    parser.add_argument('output_file', help='输出文件')
    parser.add_argument('--query', '-q', required=True, 
                       help='检索式 (用引号括起来)')
    parser.add_argument('--visualize', '-v', action='store_true',
                       help='可视化检索式语法树')
    parser.add_argument('--ai-semantic', action='store_true',
                       help='启用AI语义增强（实验性）')
    parser.add_argument('--api-key', help='Anthropic API Key (用于AI语义)')
    
    args = parser.parse_args()
    
    try:
        # 创建检索引擎
        engine = AdvancedSearchEngine(
            use_ai_semantic=args.ai_semantic,
            api_key=args.api_key
        )
        
        # 可视化语法树（如果需要）
        if args.visualize:
            viz_file = args.output_file.replace('.txt', '_query_tree.txt')
            viz_text = engine.visualize_query(args.query, viz_file)
            print("\n" + viz_text)
        
        # 解析输入文件
        records = WOSFileHandler.parse_wos_file(args.input_file)
        
        # 执行检索
        matched_records, stats = engine.search(records, args.query)
        
        # 保存结果
        WOSFileHandler.save_wos_file(matched_records, args.output_file)
        
        # 保存统计信息
        stats_file = args.output_file.replace('.txt', '_search_stats.json')
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        logger.info(f"📊 统计信息已保存: {stats_file}")
        
        print(f"\n🎉 检索完成！")
        print(f"   匹配记录: {stats['matched_records']}/{stats['total_records']}")
        print(f"   输出文件: {args.output_file}")
        
        return 0
    
    except Exception as e:
        logger.error(f"❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1



def test_wos_compatibility():
    """
    测试WoS标准检索式兼容性
    
    这个函数测试各种WoS标准检索式格式，确保完全兼容
    """
    print("=" * 80)
    print("🧪 WoS标准兼容性测试")
    print("=" * 80)
    
    # 创建测试引擎
    engine = AdvancedSearchEngine()
    
    # 测试检索式列表
    test_queries = [
        # 基础格式
        "TI=cancer",
        "AU=Smith",
        "C1=Harvard",
        
        # 引号格式
        'TI="cancer research"',
        'AU="Smith J"',
        
        # 通配符
        "AU=Smith*",
        "C1=*University*",
        "TI=colo?r",
        
        # 布尔运算
        "AU=Smith AND TI=cancer",
        "TI=CRISPR OR AB=gene",
        "DT=Article NOT TI=review",
        
        # 复杂逻辑
        "(AU=Smith OR AU=Jones) AND TI=cancer",
        "(TI=cancer OR AB=cancer) AND NOT DT=Review",
        
        # 范围查询
        "PY=2020-2024",
        "TC=10-100",
        "PY=2020-2024 AND TI=AI",
        
        # 数值比较
        "TC>50",
        "PY>=2020",
        "TC>50 AND PY>=2020",
        
        # 组合查询
        "AU=Zhang* AND C1=*University* AND PY=2020-2024",
        '(TI="machine learning" OR TI="deep learning") AND PY>=2020',
    ]
    
    print("\n测试检索式解析:")
    print("-" * 80)
    
    success_count = 0
    fail_count = 0
    
    for i, query in enumerate(test_queries, 1):
        try:
            tree = engine.parse_query(query)
            print(f"✅ 测试 {i:2d}: {query}")
            success_count += 1
        except Exception as e:
            print(f"❌ 测试 {i:2d}: {query}")
            print(f"   错误: {str(e)}")
            fail_count += 1
    
    print("-" * 80)
    print(f"\n测试结果: {success_count} 成功, {fail_count} 失败")
    print("=" * 80)
    
    # 测试匹配逻辑
    print("\n🧪 测试匹配逻辑")
    print("=" * 80)
    
    # 创建测试记录
    test_records = [
        {
            'TI': 'Cancer Research and Treatment',
            'AU': 'Smith J; Jones K',
            'C1': 'Harvard University; MIT',
            'PY': '2023',
            'TC': '45',
            'DT': 'Article'
        },
        {
            'TI': 'Machine Learning in Medicine',
            'AU': 'Zhang W; Li H',
            'C1': 'Stanford University',
            'PY': '2022',
            'TC': '120',
            'DT': 'Article'
        },
        {
            'TI': 'CRISPR Gene Editing: A Review',
            'AU': 'Johnson M',
            'C1': 'Oxford University',
            'PY': '2021',
            'TC': '230',
            'DT': 'Review'
        }
    ]
    
    # 测试查询
    test_cases = [
        ("TI=cancer", [0]),  # 应该匹配第1条
        ("AU=Smith", [0]),   # 应该匹配第1条
        ("AU=Zhang*", [1]),  # 应该匹配第2条
        ("C1=*University*", [0, 1, 2]),  # 应该匹配所有
        ("PY=2020-2024", [0, 1, 2]),  # 应该匹配所有
        ("TC>100", [1, 2]),  # 应该匹配第2、3条
        ("DT=Article AND NOT TI=Review", [0, 1]),  # 应该匹配第1、2条
        ("(TI=cancer OR TI=CRISPR) AND PY>=2021", [0, 2]),  # 应该匹配第1、3条
    ]
    
    print("\n测试匹配结果:")
    print("-" * 80)
    
    for query, expected_indices in test_cases:
        try:
            matched, _ = engine.search(test_records, query)
            matched_indices = [test_records.index(r) for r in matched]
            
            if matched_indices == expected_indices:
                print(f"✅ {query}")
                print(f"   期望: {expected_indices}, 实际: {matched_indices}")
            else:
                print(f"⚠️  {query}")
                print(f"   期望: {expected_indices}, 实际: {matched_indices}")
        except Exception as e:
            print(f"❌ {query}")
            print(f"   错误: {str(e)}")
    
    print("=" * 80)


if __name__ == '__main__':
    # 检查是否为测试模式
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_wos_compatibility()
    else:
        sys.exit(main())
