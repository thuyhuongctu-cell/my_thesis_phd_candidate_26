#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bibliometric Data Consolidation Tool - 完整整合版 v7.0.1
修复版本 - 增强错误处理和模块兼容性

整合所有功能模块：
- 📁 格式转换 (Scopus → WoS)
- 🔄 智能合并去重
- 🔧 字段智能修复 (基于源数据 + AI补全)
- 🚫 撤稿文献筛选
- 🔍 高级检索引擎 (WoS语法)
- 🌍 语言筛选
- 📅 年份范围筛选
- 🏛️ 机构名称清洗
- 📊 数据统计分析
- 📈 可视化图表生成

作者: Meng Linghan
版本: v7.0.1 (Fixed)
日期: 2026-02-11
修复: 模块导入和方法调用兼容性
"""

import os
import sys
import threading
import logging
import json
import traceback
import queue
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# GUI库
import customtkinter as ctk
from tkinter import filedialog, messagebox

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# CustomTkinter 主题设置
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# ============================================================================
# 辅助函数：智能模块导入
# ============================================================================

def import_batch_module():
    """
    智能导入batch模块 - 自动检测类名并支持多种项目结构
    """
    import importlib
    import_errors = []
    
    # 定义可能的类名组合
    possible_converter_names = [
        'BibliormetricBatchConverter',
        'BibliometricBatchConverter',
        'BatchConverter',
        'ScopusConverter'
    ]
    
    possible_merger_names = [
        'BibliormetricMerger',
        'BibliometricMerger', 
        'Merger',
        'DataMerger'
    ]
    
    def try_import_from_module(module):
        """尝试从模块中导入类"""
        # 获取模块中所有的类
        converter_class = None
        merger_class = None
        
        for name in dir(module):
            if name in possible_converter_names:
                converter_class = getattr(module, name)
            if name in possible_merger_names:
                merger_class = getattr(module, name)
        
        # 如果没找到已知名称,尝试查找包含Converter或Merger的类
        if not converter_class:
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and ('Converter' in name or 'Convert' in name):
                    converter_class = obj
                    break
        
        if not merger_class:
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and 'Merger' in name:
                    merger_class = obj
                    break
        
        return converter_class, merger_class
    
    # 尝试方式1: 标准包导入
    try:
        import src.bibliometrics.converters.batch as batch_module
        converter, merger = try_import_from_module(batch_module)
        if converter:
            logger.info(f"✅ Batch模块导入成功 (标准路径): Converter={converter.__name__}, Merger={merger.__name__ if merger else 'None'}")
            return converter, merger
    except Exception as e:
        import_errors.append(f"标准路径: {e}")
    
    # 尝试方式2: 直接导入
    try:
        import batch as batch_module
        converter, merger = try_import_from_module(batch_module)
        if converter:
            logger.info(f"✅ Batch模块导入成功 (直接导入): Converter={converter.__name__}, Merger={merger.__name__ if merger else 'None'}")
            return converter, merger
    except Exception as e:
        import_errors.append(f"直接导入: {e}")
    
    # 尝试方式3: 添加路径后导入
    try:
        script_dir = Path(__file__).parent.resolve()
        possible_paths = [
            script_dir / "src" / "bibliometrics" / "converters",
            script_dir.parent / "src" / "bibliometrics" / "converters",
            Path.cwd() / "src" / "bibliometrics" / "converters"
        ]
        
        for path in possible_paths:
            if path.exists() and (path / "batch.py").exists():
                sys.path.insert(0, str(path))
                try:
                    import batch as batch_module
                    converter, merger = try_import_from_module(batch_module)
                    if converter:
                        logger.info(f"✅ Batch模块导入成功 (路径 {path}): Converter={converter.__name__}, Merger={merger.__name__ if merger else 'None'}")
                        return converter, merger
                except Exception as e:
                    import_errors.append(f"路径 {path}: {e}")
    except Exception as e:
        import_errors.append(f"路径添加: {e}")
    
    # 所有尝试失败
    error_msg = "❌ 无法导入batch模块!\n\n尝试的方法:\n" + "\n".join(f"  - {err}" for err in import_errors)
    error_msg += "\n\n请确保 batch.py 文件位于以下任一位置:"
    error_msg += "\n  - src/bibliometrics/converters/batch.py"
    error_msg += "\n  - 与gui_app.py同目录的batch.py"
    error_msg += "\n\n提示: 请检查batch.py文件中是否有Converter或Merger相关的类定义"
    raise ImportError(error_msg)


def import_merge_module():
    """
    智能导入merge模块 - 自动检测类名
    """
    possible_module_names = [
        'merge_with_repair',
        'merge',
        'src.bibliometrics.merge_with_repair',
        'src.bibliometrics.merge'
    ]
    
    possible_class_names = [
        'BibliormetricMerger',
        'BibliometricMerger',
        'Merger',
        'DataMerger'
    ]
    
    for module_name in possible_module_names:
        try:
            module = __import__(module_name, fromlist=[''])
            
            # 尝试已知的类名
            for class_name in possible_class_names:
                if hasattr(module, class_name):
                    logger.info(f"✅ Merge模块导入成功: {module_name}.{class_name}")
                    return getattr(module, class_name)
            
            # 尝试查找包含Merger的类
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and 'Merger' in name:
                    logger.info(f"✅ Merge模块导入成功: {module_name}.{name}")
                    return obj
                    
        except (ImportError, AttributeError):
            continue
    
    # 如果merge_with_repair不可用，返回None，稍后会尝试使用batch模块
    logger.warning("⚠️ 未找到独立的merge模块,将尝试使用batch模块中的Merger")
    return None


def import_institutions_module():
    """
    智能导入机构清洗模块 - 自动搜索项目目录树中的 institutions.py
    支持的项目结构：
      - gui_app.py 同目录/institutions.py
      - src/bibliometrics/standardizers/institutions.py
      - 任何上级目录下的 src/bibliometrics/standardizers/institutions.py
    """
    import importlib.util

    gui_dir = Path(__file__).parent.resolve()

    # 候选路径列表（从最具体到最通用）
    candidate_paths = [
        # 同目录
        gui_dir / "institutions.py",
        # 标准子包路径（相对于 gui_app.py 所在目录）
        gui_dir / "src" / "bibliometrics" / "standardizers" / "institutions.py",
        # 上一级
        gui_dir.parent / "src" / "bibliometrics" / "standardizers" / "institutions.py",
        # 上两级
        gui_dir.parent.parent / "src" / "bibliometrics" / "standardizers" / "institutions.py",
        # 以当前工作目录为根
        Path.cwd() / "src" / "bibliometrics" / "standardizers" / "institutions.py",
        Path.cwd() / "institutions.py",
    ]

    for path in candidate_paths:
        if path.exists():
            try:
                spec = importlib.util.spec_from_file_location("institutions", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                logger.info(f"✅ institutions 模块导入成功: {path}")
                return module.InstitutionCleaner
            except Exception as e:
                logger.warning(f"⚠️ 加载 {path} 失败: {e}")
                continue

    # 最后尝试包导入（适用于已安装为包的情况）
    for pkg in [
        "src.bibliometrics.standardizers.institutions",
        "bibliometrics.standardizers.institutions",
        "institutions",
    ]:
        try:
            import importlib
            module = importlib.import_module(pkg)
            logger.info(f"✅ institutions 模块包导入成功: {pkg}")
            return module.InstitutionCleaner
        except ImportError:
            continue

    return None  # 调用方负责处理 None 的情况


def import_records_module():
    """
    智能导入统计分析模块 - 自动搜索项目目录树中的 records.py
    支持的项目结构：
      - gui_app.py 同目录/records.py
      - src/bibliometrics/analysis/records.py
      - 任何上级目录下的 src/bibliometrics/analysis/records.py
    """
    import importlib.util

    gui_dir = Path(__file__).parent.resolve()

    # 候选路径列表（从最具体到最通用）
    candidate_paths = [
        # 同目录
        gui_dir / "records.py",
        # 标准子包路径（相对于 gui_app.py 所在目录）
        gui_dir / "src" / "bibliometrics" / "analysis" / "records.py",
        gui_dir / "src" / "bibliometrics" / "standardizers" / "records.py",
        # 上一级
        gui_dir.parent / "src" / "bibliometrics" / "analysis" / "records.py",
        gui_dir.parent / "src" / "bibliometrics" / "standardizers" / "records.py",
        # 上两级
        gui_dir.parent.parent / "src" / "bibliometrics" / "analysis" / "records.py",
        gui_dir.parent.parent / "src" / "bibliometrics" / "standardizers" / "records.py",
        # 以当前工作目录为根
        Path.cwd() / "src" / "bibliometrics" / "analysis" / "records.py",
        Path.cwd() / "src" / "bibliometrics" / "standardizers" / "records.py",
        Path.cwd() / "records.py",
    ]

    for path in candidate_paths:
        if path.exists():
            try:
                spec = importlib.util.spec_from_file_location("records", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                logger.info(f"✅ records 模块导入成功: {path}")
                return module.RecordAnalyzer
            except Exception as e:
                logger.warning(f"⚠️ 加载 {path} 失败: {e}")
                continue

    # 最后尝试包导入（适用于已安装为包的情况）
    for pkg in [
        "src.bibliometrics.analysis.records",
        "src.bibliometrics.standardizers.records",
        "bibliometrics.analysis.records",
        "bibliometrics.standardizers.records",
        "records",
    ]:
        try:
            import importlib
            module = importlib.import_module(pkg)
            logger.info(f"✅ records 模块包导入成功: {pkg}")
            return module.RecordAnalyzer
        except ImportError:
            continue

    return None  # 调用方负责处理 None 的情况


def import_year_module():
    """
    智能导入年份过滤模块 - 自动搜索项目目录树中的 year.py
    支持的项目结构：
      - gui_app.py 同目录/year.py
      - src/bibliometrics/filters/year.py
      - 任何上级目录下的 src/bibliometrics/filters/year.py
    """
    import importlib.util

    gui_dir = Path(__file__).parent.resolve()

    # 候选路径列表（从最具体到最通用）
    candidate_paths = [
        # 同目录
        gui_dir / "year.py",
        # 标准子包路径
        gui_dir / "src" / "bibliometrics" / "filters" / "year.py",
        gui_dir / "src" / "bibliometrics" / "standardizers" / "year.py",
        # 上一级
        gui_dir.parent / "src" / "bibliometrics" / "filters" / "year.py",
        gui_dir.parent / "src" / "bibliometrics" / "standardizers" / "year.py",
        # 上两级
        gui_dir.parent.parent / "src" / "bibliometrics" / "filters" / "year.py",
        gui_dir.parent.parent / "src" / "bibliometrics" / "standardizers" / "year.py",
        # 以当前工作目录为根
        Path.cwd() / "src" / "bibliometrics" / "filters" / "year.py",
        Path.cwd() / "src" / "bibliometrics" / "standardizers" / "year.py",
        Path.cwd() / "year.py",
    ]

    for path in candidate_paths:
        if path.exists():
            try:
                spec = importlib.util.spec_from_file_location("year", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                logger.info(f"✅ year 模块导入成功: {path}")
                return module.YearFilter
            except Exception as e:
                logger.warning(f"⚠️ 加载 {path} 失败: {e}")
                continue

    # 最后尝试包导入
    for pkg in [
        "src.bibliometrics.filters.year",
        "src.bibliometrics.standardizers.year",
        "bibliometrics.filters.year",
        "bibliometrics.standardizers.year",
        "year",
    ]:
        try:
            import importlib
            module = importlib.import_module(pkg)
            logger.info(f"✅ year 模块包导入成功: {pkg}")
            return module.YearFilter
        except ImportError:
            continue

    return None  # 调用方负责处理 None 的情况


def import_visualization_modules():
    """
    智能导入可视化模块 - 自动搜索 plot_citations.py 和 plot_types.py
    """
    import importlib.util

    gui_dir = Path(__file__).parent.resolve()
    
    # 候选路径列表
    candidate_dirs = [
        gui_dir,  # 同目录
        gui_dir / "src" / "bibliometrics" / "visualization",
        gui_dir / "src" / "bibliometrics" / "analysis",
        gui_dir.parent / "src" / "bibliometrics" / "visualization",
        gui_dir.parent / "src" / "bibliometrics" / "analysis",
        gui_dir.parent.parent / "src" / "bibliometrics" / "visualization",
        gui_dir.parent.parent / "src" / "bibliometrics" / "analysis",
        Path.cwd() / "src" / "bibliometrics" / "visualization",
        Path.cwd() / "src" / "bibliometrics" / "analysis",
        Path.cwd(),
    ]
    
    modules = {}
    
    # 查找 plot_citations.py
    for dir_path in candidate_dirs:
        citations_path = dir_path / "plot_citations.py"
        if citations_path.exists():
            try:
                spec = importlib.util.spec_from_file_location("plot_citations", citations_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                modules['citations'] = module.PublicationCitationAnalyzer
                logger.info(f"✅ plot_citations 模块导入成功: {citations_path}")
                break
            except Exception as e:
                logger.warning(f"⚠️ 加载 {citations_path} 失败: {e}")
    
    # 查找 plot_types.py
    for dir_path in candidate_dirs:
        types_path = dir_path / "plot_types.py"
        if types_path.exists():
            try:
                spec = importlib.util.spec_from_file_location("plot_types", types_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                modules['types'] = module.DocumentTypeAnalyzer
                logger.info(f"✅ plot_types 模块导入成功: {types_path}")
                break
            except Exception as e:
                logger.warning(f"⚠️ 加载 {types_path} 失败: {e}")
    
    return modules if modules else None


# ============================================================================
# GUI组件类
# ============================================================================

class ModernCard(ctk.CTkFrame):
    """现代化卡片组件"""
    
    def __init__(self, master, title, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=("gray92", "gray17"),
            corner_radius=12,
            border_width=2,
            border_color=("gray80", "gray25")
        )
        
        # 卡片标题
        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("gray10", "gray90")
        )
        self.title_label.pack(padx=18, pady=(12, 8), anchor="w")
        
        # 分隔线
        separator = ctk.CTkFrame(self, height=2, fg_color=("gray70", "gray30"))
        separator.pack(fill="x", padx=18, pady=(0, 8))


class StatusBadge(ctk.CTkLabel):
    """状态徽章"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            corner_radius=6,
            font=ctk.CTkFont(size=11, weight="bold"),
            padx=12,
            pady=4
        )
    
    def set_status(self, status: str):
        """设置状态"""
        status_config = {
            'idle': ('⚪ 就绪', ("gray70", "gray30"), ("gray10", "gray90")),
            'running': ('🟢 运行中', ("green", "green"), ("white", "white")),
            'success': ('✅ 成功', ("green", "green"), ("white", "white")),
            'error': ('❌ 错误', ("red", "red"), ("white", "white")),
            'warning': ('⚠️ 警告', ("orange", "orange"), ("white", "white"))
        }
        
        text, bg, fg = status_config.get(status, status_config['idle'])
        self.configure(text=text, fg_color=bg, text_color=fg)


# ============================================================================
# 工作流引擎类
# ============================================================================

class WorkflowEngine:
    """工作流引擎 - 协调所有处理步骤"""
    
    def __init__(self, log_callback):
        self.log = log_callback
        self.stop_requested = False
    
    def stop(self):
        """停止处理"""
        self.stop_requested = True
        self.log("⏸️ 正在停止...")
    
    def format_conversion(self, params: Dict) -> Tuple[bool, str]:
        """步骤1: Scopus格式转换"""
        try:
            self.log("📁 步骤1: Scopus格式转换")
            self.log("=" * 80)
            
            data_dir = Path(params['data_dir'])
            output_dir = Path(params.get('output_dir', params['data_dir']))
            
            # 确保输出目录存在
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # 导入转换模块
            try:
                BatchConverter, _ = import_batch_module()
            except ImportError as e:
                return False, str(e)
            
            # 定义输入输出文件
            input_file = data_dir / "scopus.csv"
            output_file = output_dir / "scopus_converted_to_wos.txt"
            
            if not input_file.exists():
                return False, f"Scopus文件不存在: {input_file}"
            
            self.log(f"📥 输入: {input_file.name}")
            self.log(f"📤 输出: {output_file.name}")
            
            # 实例化时传入必需的参数
            converter = BatchConverter(str(input_file), str(output_file))
            
            # 尝试调用不同的可能方法名
            if hasattr(converter, 'convert_scopus_to_wos'):
                converter.convert_scopus_to_wos(str(input_file), str(output_file))
            elif hasattr(converter, 'convert'):
                converter.convert()
            elif hasattr(converter, 'run'):
                converter.run()
            elif hasattr(converter, 'process'):
                converter.process()
            elif hasattr(converter, 'batch_convert'):
                converter.batch_convert()
            else:
                # 如果没有找到合适的方法，可能在__init__中已经执行了转换
                self.log("⚠️ 使用默认转换流程（在初始化时自动执行）")
            
            self.log(f"✅ 转换完成: {output_file.name}")
            return True, str(output_file)
            
        except Exception as e:
            self.log(f"❌ 转换失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    
    def merge_and_deduplicate(self, params: Dict) -> Tuple[bool, str]:
        """步骤2: 合并去重"""
        try:
            self.log("🔄 步骤2: 合并去重")
            self.log("=" * 80)
            
            data_dir = Path(params['data_dir'])
            output_dir = Path(params.get('output_dir', params['data_dir']))
            
            # WoS文件在数据目录
            wos_file = data_dir / "wos.txt"
            # 转换后的Scopus文件在输出目录
            scopus_file = output_dir / "scopus_converted_to_wos.txt"
            # 合并结果也保存到输出目录
            output_file = output_dir / "merged_deduplicated.txt"
            
            if not wos_file.exists():
                return False, f"WoS文件不存在: {wos_file}"
            if not scopus_file.exists():
                return False, f"转换后的Scopus文件不存在: {scopus_file}"
            
            self.log(f"📥 WoS文件: {wos_file.name}")
            self.log(f"📥 Scopus文件: {scopus_file.name}")
            
            # 尝试导入专用的merge模块
            MergerClass = import_merge_module()
            
            if MergerClass is None:
                # 如果没有专用merge模块，尝试从batch导入
                self.log("⚠️ 未找到merge_with_repair模块，尝试使用batch模块...")
                try:
                    _, MergerClass = import_batch_module()
                except ImportError as e:
                    return False, f"无法导入合并模块: {e}"
            
            merger = MergerClass()
            
            # 尝试调用不同的方法名
            if hasattr(merger, 'merge_databases'):
                # merge_databases 接受: wos_file, scopus_file, output_dir, use_ai_repair, output_both_versions
                result_file = merger.merge_databases(
                    wos_file=str(wos_file),
                    scopus_file=str(scopus_file),
                    output_dir=str(output_dir),
                    use_ai_repair=params.get('enable_ai_repair', False),
                    output_both_versions=params.get('enable_both_versions', False)
                )
            elif hasattr(merger, 'merge_and_deduplicate'):
                result_file = merger.merge_and_deduplicate(
                    str(wos_file),
                    str(scopus_file),
                    str(output_file)
                )
            elif hasattr(merger, 'merge'):
                result_file = merger.merge(
                    str(wos_file),
                    str(scopus_file),
                    str(output_file)
                )
            elif hasattr(merger, 'process'):
                result_file = merger.process(
                    str(wos_file),
                    str(scopus_file),
                    str(output_file)
                )
            else:
                return False, f"合并类没有可用的方法。可用方法: {dir(merger)}"
            
            # 获取统计信息
            stats = {}
            if hasattr(merger, 'get_statistics'):
                stats = merger.get_statistics()
            elif hasattr(merger, 'stats'):
                stats = merger.stats
            elif hasattr(merger, 'get_stats'):
                stats = merger.get_stats()
            
            # 输出文件可能由merger返回，或者使用默认路径
            if result_file:
                actual_output = result_file
            else:
                actual_output = str(output_dir / "merged_deduplicated.txt")
            
            self.log(f"✅ 合并完成: {Path(actual_output).name}")
            if stats:
                self.log(f"   WoS原始: {stats.get('wos_original', 0)}")
                self.log(f"   Scopus原始: {stats.get('scopus_original', 0)}")
                self.log(f"   最终合并: {stats.get('final_merged', stats.get('final_records', '未知'))}")
                self.log(f"   源数据修复: {stats.get('source_repaired', 0)}")
                if stats.get('ai_repaired', 0) > 0:
                    self.log(f"   AI智能补全: {stats.get('ai_repaired', 0)}")
            
            return True, actual_output
            
        except Exception as e:
            self.log(f"❌ 合并失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    
    def field_repair(self, params: Dict) -> Tuple[bool, str]:
        """步骤3: 字段智能修复"""
        try:
            self.log("🔧 步骤3: 字段智能修复")
            self.log("=" * 80)
            
            # 字段修复已在merge_databases中完成
            if params.get('enable_repair'):
                self.log("✅ 字段修复已在合并步骤中完成")
                self.log(f"   - 基于源数据修复")
                if params.get('enable_ai_repair'):
                    self.log(f"   - AI智能补全已启用")
                if params.get('enable_both_versions'):
                    self.log(f"   - 已输出修复前后两个版本")
            else:
                self.log("⏭️ 字段修复未启用，跳过")
            
            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = self._get_latest_file(output_dir, ["merged"])
            
            return True, str(input_file) if input_file else ""
            
        except Exception as e:
            self.log(f"❌ 修复失败: {e}")
            return False, str(e)
    
    def retraction_filter(self, params: Dict) -> Tuple[bool, str]:
        """步骤4: 撤稿文献筛选"""
        try:
            self.log("🚫 步骤4: 撤稿文献筛选")
            self.log("=" * 80)
            
            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = self._get_latest_file(output_dir)
            
            if not input_file:
                return False, "未找到输入文件"
            
            self.log(f"📥 输入文件: {input_file.name}")
            
            # 导入撤稿筛选模块
            try:
                # 修复：直接导入当前目录的retraction_filter模块
                import sys
                import os
                current_dir = os.path.dirname(os.path.abspath(__file__))
                if current_dir not in sys.path:
                    sys.path.insert(0, current_dir)
                from retraction_filter import RetractionFilter
                
                # 创建筛选器
                filter_tool = RetractionFilter()
                
                # 输出文件
                output_file = output_dir / f"{input_file.stem}_no_retractions.txt"
                
                # 执行筛选
                use_online = params.get('enable_online_verification', False)
                result_file = filter_tool.filter_retractions(
                    input_file=str(input_file),
                    output_file=str(output_file),
                    use_online_check=use_online
                )
                
                # 获取统计
                stats = filter_tool.get_statistics()
                self.log(f"✅ 撤稿筛选完成")
                self.log(f"   总记录数: {stats['total_records']}")
                self.log(f"   检测到撤稿: {stats['total_retracted']}")
                self.log(f"   清洁记录: {stats['clean_records']}")
                
                return True, result_file
                
            except ImportError as e:
                self.log(f"⚠️ 撤稿筛选模块未找到: {e}")
                self.log(f"⏭️ 跳过撤稿筛选")
                return True, str(input_file)
            
        except Exception as e:
            self.log(f"❌ 筛选失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    
    def advanced_search(self, params: Dict) -> Tuple[bool, str]:
        """步骤5: 高级检索"""
        try:
            if not params.get('enable_advanced_search'):
                self.log("⏭️ 跳过高级检索")
                return True, ""
            
            self.log("🔍 步骤5: 高级检索")
            self.log("=" * 80)
            
            query = params.get('search_query', '')
            if not query:
                self.log("⚠️ 未提供检索式，跳过")
                return True, ""
            
            self.log(f"📝 检索式: {query}")
            self.log("⚠️ 高级检索模块未实现，跳过此步骤")
            
            return True, ""
            
        except Exception as e:
            self.log(f"❌ 检索失败: {e}")
            return False, str(e)
    
    def language_filter(self, params: Dict) -> Tuple[bool, str]:
        """步骤6: 语言筛选 - 使用测试通过的版本"""
        try:
            self.log("🌍 步骤6: 语言筛选")
            self.log("=" * 80)
            
            language = params.get('language', 'All')
            if language == 'All':
                self.log("⏭️ 不限语言，跳过筛选")
                return True, ""
            
            self.log(f"🔤 目标语言: {language}")
            
            # ===== 直接使用测试通过的路径 =====
            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = output_dir / "merged_deduplicated_no_retractions.txt"
            output_file = output_dir / "english_only.txt"
            
            self.log(f"📥 输入文件: {input_file}")
            self.log(f"📤 输出文件: {output_file}")
            
            # 检查文件是否存在
            if not input_file.exists():
                self.log(f"❌ 文件不存在: {input_file}")
                # 尝试查找其他可能的数据文件
                alternatives = list(output_dir.glob("merged_deduplicated*.txt"))
                data_files = [f for f in alternatives if 'report' not in f.name and 'retraction_report' not in f.name]
                if data_files:
                    input_file = data_files[0]
                    output_file = output_dir / f"{input_file.stem}_english.txt"
                    self.log(f"📋 使用替代文件: {input_file}")
                    self.log(f"📋 输出文件: {output_file}")
                else:
                    return False, "未找到数据文件"
            
            try:
                import sys
                import os
                current_dir = os.path.dirname(os.path.abspath(__file__))
                if current_dir not in sys.path:
                    sys.path.insert(0, current_dir)
                
                from language import LanguageFilter
                self.log(f"✅ 成功导入LanguageFilter")
                
                # 创建筛选器并执行
                filter_tool = LanguageFilter(
                    input_file=str(input_file),
                    output_file=str(output_file),
                    target_language=language
                )
                
                success = filter_tool.run()
                
                if success:
                    self.log(f"✅ 语言筛选完成")
                    self.log(f"   输出文件: {output_file}")
                    return True, str(output_file)
                else:
                    self.log(f"❌ 语言筛选失败")
                    return False, "语言筛选失败"
                    
            except ImportError as e:
                self.log(f"⚠️ 语言筛选模块导入失败: {e}")
                self.log("⏭️ 跳过语言筛选")
                return True, str(input_file)
            except Exception as e:
                self.log(f"⚠️ 语言筛选执行失败: {e}")
                self.log("⏭️ 跳过语言筛选")
                return True, str(input_file)
            
        except Exception as e:
            self.log(f"❌ 筛选失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    

    def year_filter(self, params: Dict) -> Tuple[bool, str]:
        """步骤7: 年份筛选"""
        try:
            self.log("📅 步骤7: 年份筛选")
            self.log("=" * 80)
            
            year_range = params.get('year_range', '')
            if not year_range or year_range == '全部':
                self.log("⏭️ 不限年份，跳过筛选")
                return True, ""
            
            self.log(f"📆 年份范围: {year_range}")
            
            output_dir = Path(params.get('output_dir', params['data_dir']))
            
            # 查找输入文件（排除报告文件）
            all_files = []
            for prefix in ["merged", "english_only", "scopus_converted", "wos"]:
                all_files.extend(output_dir.glob(f"{prefix}*.txt"))
            
            data_files = [
                f for f in all_files 
                if not any(exclude in f.name for exclude in [
                    '_report.txt',
                    '_cleaning_report.txt',
                    '_analysis_report.txt',
                    '_statistics.txt',
                    '.tmp'
                ])
            ]
            
            if not data_files:
                self.log("❌ 未找到输入文件")
                return False, "未找到输入文件"
            
            input_file = max(data_files, key=lambda f: f.stat().st_mtime)
            self.log(f"📥 输入文件: {input_file.name}")
            
            # 使用智能导入
            YearFilter = import_year_module()
            if YearFilter is None:
                self.log("⚠️ 年份过滤模块未找到")
                self.log("💡 提示: 可将 year.py 放在以下位置之一:")
                self.log("   - gui_app.py 同目录")
                self.log("   - src/bibliometrics/filters/year.py")
                self.log("   - src/bibliometrics/standardizers/year.py")
                self.log("⏭️ 跳过年份筛选")
                return True, str(input_file)
            
            # 解析年份范围
            try:
                years = year_range.split('-')
                if len(years) != 2:
                    self.log(f"⚠️ 年份范围格式错误: {year_range}（应为 YYYY-YYYY）")
                    return True, str(input_file)
                
                min_year = int(years[0].strip())
                max_year = int(years[1].strip())
                
                if min_year > max_year:
                    self.log(f"⚠️ 最小年份 ({min_year}) 不能大于最大年份 ({max_year})")
                    return True, str(input_file)
                
            except ValueError as e:
                self.log(f"⚠️ 年份解析错误: {e}")
                return True, str(input_file)
            
            # 生成输出文件名
            output_file = output_dir / f"{input_file.stem}_{min_year}-{max_year}.txt"
            report_file = output_dir / f"{input_file.stem}_{min_year}-{max_year}_year_filter_report.txt"
            
            self.log(f"📤 输出文件: {output_file.name}")
            
            # 执行过滤
            self.log("")
            self.log("🔍 开始年份过滤...")
            
            filter_tool = YearFilter(min_year=min_year, max_year=max_year)
            filter_tool.filter_file(
                input_file=str(input_file),
                output_file=str(output_file),
                report_file=str(report_file)
            )
            
            self.log("")
            self.log("✅ 年份筛选完成!")
            self.log(f"📄 过滤报告: {report_file.name}")
            self.log("")
            self.log("📊 筛选统计:")
            self.log(f"   原始记录: {filter_tool.stats['total_records']}")
            kept = filter_tool.stats['total_records'] - filter_tool.stats['filtered_records']
            self.log(f"   保留记录: {kept}")
            self.log(f"   过滤掉: {filter_tool.stats['filtered_records']}")
            
            if filter_tool.stats['total_records'] > 0:
                keep_rate = (kept / filter_tool.stats['total_records']) * 100
                self.log(f"   保留率: {keep_rate:.1f}%")
            
            return True, str(output_file)
            
        except Exception as e:
            self.log(f"❌ 年份筛选失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    def institution_cleaning(self, params: Dict) -> Tuple[bool, str]:
        """步骤8: 机构清洗 - 调用 institutions.py 中的 InstitutionCleaner"""
        try:
            if not params.get('enable_institution_cleaning'):
                self.log("⏭️ 跳过机构清洗")
                return True, ""

            self.log("🏛️ 步骤8: 机构清洗")
            self.log("=" * 80)

            # 导入模块
            InstitutionCleaner = import_institutions_module()
            if InstitutionCleaner is None:
                self.log("⚠️ 未找到 institutions.py，跳过机构清洗")
                self.log("   请确认文件存在于以下任一位置:")
                self.log("   - gui_app.py 同目录")
                self.log("   - src/bibliometrics/standardizers/institutions.py")
                return True, ""
            self.log("✅ 成功导入 InstitutionCleaner")

            # 找到上一步的输出文件作为输入
            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = self._get_latest_file(output_dir)
            if not input_file:
                self.log("❌ 未找到输入文件")
                return False, "未找到输入文件"

            self.log(f"📥 输入文件: {input_file.name}")

            output_file = output_dir / f"{input_file.stem}_institutions_cleaned.txt"
            self.log(f"📤 输出文件: {output_file.name}")

            # 定位配置文件（可选）
            gui_dir = Path(__file__).parent.resolve()
            config_candidates = [
                gui_dir / "config" / "institution_cleaning_rules.json",
                gui_dir.parent / "config" / "institution_cleaning_rules.json",
                gui_dir / "src" / "bibliometrics" / "standardizers" / "config" / "institution_cleaning_rules.json",
                Path(params.get('data_dir', '')) / "config" / "institution_cleaning_rules.json",
            ]
            config_file = next((str(p) for p in config_candidates if p.exists()),
                               "config/institution_cleaning_rules.json")
            self.log(f"📋 配置文件: {config_file}")

            # 执行清洗
            cleaner = InstitutionCleaner(config_file=config_file)
            cleaner.run(str(input_file), str(output_file))

            # 输出统计
            s = cleaner.stats
            unique_before = s.get('unique_before', 0)
            unique_after  = s.get('unique_after', 0)
            reduction = (1 - unique_after / unique_before) * 100 if unique_before > 0 else 0

            self.log("✅ 机构清洗完成")
            self.log(f"   总记录数:         {s.get('total_records', 0)}")
            self.log(f"   清洗前唯一机构数: {unique_before}")
            self.log(f"   清洗后唯一机构数: {unique_after}  (减少 {reduction:.1f}%)")
            self.log(f"   移除噪音:         {s.get('removed_noise', 0)}")
            self.log(f"   标准化名称:       {s.get('standardized', 0)}")
            self.log(f"   合并父子机构:     {s.get('merged_parent_child', 0)}")
            self.log(f"   移除独立部门:     {s.get('removed_departments', 0)}")
            report = str(output_file).replace('.txt', '_cleaning_report.txt')
            self.log(f"📋 清洗报告: {Path(report).name}")

            return True, str(output_file)

        except Exception as e:
            self.log(f"❌ 机构清洗失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    
    def restore_wos_standard_format(self, params: Dict) -> Tuple[bool, str]:
        """
        步骤8b: WoS 标准格式恢复（双版本输出）

        仅当用户同时勾选"字段修复"和"输出两种版本"时执行。
        对经过全部清洗步骤后的最终文件：
          - 原文件保留（repaired / cleaned 版本）
          - 生成 <原文件名>_wos_standard.txt（去除多余引号的纯净版）

        必须在所有清洗步骤（含机构清洗）完成后调用。
        """
        # ── 前置检查 ──────────────────────────────────────────────
        if not (params.get('enable_repair') and params.get('enable_both_versions')):
            self.log("⏭️ 跳过 WoS 格式恢复（未启用双版本输出）")
            return True, ""

        try:
            self.log("\n" + "=" * 80)
            self.log("📄 步骤8b: WoS 标准格式恢复（双版本输出）")
            self.log("=" * 80)

            output_dir = Path(params.get('output_dir', params['data_dir']))

            # 找到当前最新的清洗结果文件（即全部清洗步骤的最终输出）
            input_file = self._get_latest_file(output_dir)
            if not input_file:
                self.log("❌ 未找到可处理的数据文件，跳过 WoS 格式恢复")
                return True, ""

            self.log(f"📥 输入文件: {input_file.name}")
            self.log("🔧 正在去除字段行中的多余双引号，恢复 WoS 标准格式...")

            # ── 读取文件内容 ───────────────────────────────────────
            with open(input_file, "r", encoding="utf-8", errors="replace") as f:
                raw_text = f.read()

            # ── 核心还原逻辑 ───────────────────────────────────────
            # WoS 原始导出文件中，含逗号的字段行有时会被错误地用双引号包裹
            # （类似 CSV 转义），例如：
            #   "AU Deb, N"   →  AU Deb, N
            #   " Ali, MS"    →   Ali, MS
            # 规则：整行首尾各有一个 " 则去除，其余原样保留。
            restored_lines = []
            quoted_count = 0

            for line in raw_text.splitlines():
                if len(line) >= 2 and line.startswith('"') and line.endswith('"'):
                    restored_lines.append(line[1:-1])
                    quoted_count += 1
                else:
                    restored_lines.append(line)

            restored_text = "\n".join(restored_lines)

            # ── 写出 WoS 标准版 ────────────────────────────────────
            output_path = output_dir / (input_file.stem + "_wos_standard.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(restored_text)

            # ── 日志汇报 ───────────────────────────────────────────
            self.log(f"\n✅ WoS 格式恢复完成!")
            self.log(f"   去除多余引号行数: {quoted_count}")
            self.log(f"\n📌 双版本输出完成:")
            self.log(f"   ✨ Repaired 版 (AI补全+清洗): {input_file.name}")
            self.log(f"   📄 WoS 标准格式版:            {output_path.name}")

            return True, str(output_path)

        except Exception as e:
            self.log(f"❌ WoS 格式恢复失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)

    def convert_to_wos_format(self, params: Dict) -> Tuple[bool, str]:
        """
        步骤8c: 将清洗后文件转换为 VOSviewer 可正确解析的 WoS 原始格式

        核心修复：
          - AU/AF: 每个作者独立一行
          - CR:    每条引用独立一行（修复单行压缩导致VOSviewer无法建引用网络的问题）
          - C1:    每个机构独立一行（不折行）
          - 含逗号字段: 加双引号包裹
          - 长文本(AB/TI/FX等): 按70字符折行
          - 换行符: CRLF，编码: UTF-8 无 BOM

        仅当用户勾选"转换为WoS原始格式"时执行。
        """
        if not params.get('enable_wos_format_convert'):
            self.log("⏭️ 跳过 WoS 格式转换（未启用）")
            return True, ""

        import re as _re

        _W  = 70
        _C  = "   "
        _WF = {'AB','TI','DE','ID','FX','FU','C3','WC','SC','NF','CT','CY','CL','SP','HO','GP'}
        _LP = ('van','de','del','den','der','von','el','al','le','la','di','da','dos','du','bin','Abu','Al','El')
        _CR_SEP = _re.compile(
            r'\s+(?=(?:(?:' + '|'.join(_LP) + r')\s+)*[A-Z][A-Za-z\-\.\']+\s+[A-Z]{1,5},\s+\d{4})'
        )

        def _clean(v):
            v = v.rstrip('"').lstrip('"')                 .replace('""', '\x00DQ\x00').replace('"',"").replace('\x00DQ\x00','""')
            return v.strip()

        def _q(ln): return f'"{ln}"' if ',' in ln else ln

        def _wrap(tag, val):
            val = _clean(val)
            if not val: return []
            hc = ',' in val
            p1, pc = f"{tag} ", _C
            words, lns, cur, first = val.split(), [], "", True
            for w in words:
                cand = (cur+" "+w).strip() if cur else w
                lim = _W - len(p1 if first else pc)
                if len(cand) <= lim: cur = cand
                else:
                    if cur: lns.append((p1 if first else pc)+cur); first=False
                    cur = w
            if cur: lns.append((p1 if first else pc)+cur)
            return [f'"{ln}"' for ln in lns] if hc else lns

        def _authors(tag, val):
            val = _clean(val)
            if not val: return []
            tokens, authors, i = val.split(), [], 0
            while i < len(tokens):
                t = tokens[i]
                if t.endswith(','):
                    last=t.rstrip(','); fp,j=[],i+1
                    while j<len(tokens) and not tokens[j].endswith(','): fp.append(tokens[j]); j+=1
                    authors.append(f'{last}, {" ".join(fp)}' if fp else last); i=j
                elif i+1<len(tokens) and tokens[i+1].endswith(','):
                    comb=t+' '+tokens[i+1].rstrip(','); fp,j=[],i+2
                    while j<len(tokens) and not tokens[j].endswith(','): fp.append(tokens[j]); j+=1
                    authors.append(f'{comb}, {" ".join(fp)}' if fp else comb); i=j
                else: authors.append(t); i+=1
            result=[]
            for idx,a in enumerate(authors):
                if not a.strip(): continue
                result.append(_q((f"{tag} " if idx==0 else _C)+a.strip()))
            return result

        def _institutions(tag, val):
            val = _clean(val)
            if not val: return []
            parts = _re.split(r'\.\s+(?=\[)', val)
            if len(parts)==1:
                raw=_re.split(r'\.\s+', val)
                parts=[p+'.' if not p.endswith('.') and idx<len(raw)-1 else p for idx,p in enumerate(raw)]
            result=[]
            for idx,part in enumerate(parts):
                part=part.strip()
                if not part: continue
                result.append(_q((f"{tag} " if idx==0 else _C)+part))
            return result

        def _semicolon(tag, val):
            val = _clean(val)
            if not val: return []
            result=[]
            for idx,part in enumerate(p.strip() for p in val.split(';') if p.strip()):
                result.append(_q((f"{tag} " if idx==0 else _C)+part))
            return result

        def _cr(tag, val):
            val = _clean(val)
            if not val: return []
            raw = _CR_SEP.split(val.strip())
            merged,i=[],0
            while i<len(raw):
                p=raw[i].strip()
                if _re.search(r',\s+\d{4}',p): merged.append(p); i+=1
                else:
                    if i+1<len(raw): raw[i+1]=p+' '+raw[i+1]
                    i+=1
            cites=merged if merged else [val.strip()]
            result=[]
            for idx,cite in enumerate(cites):
                cite=cite.strip()
                if not cite: continue
                result.append(_q((f"{tag} " if idx==0 else _C)+cite))
            return result

        def _simple(tag, val):
            val=_clean(val)
            if not val: return []
            return [_q(f"{tag} {val}")]

        def _parse(text):
            records,current,ctag,cval=[],[],None,[]
            tag_re=_re.compile(r'^([A-Z][A-Z0-9])\s+(.*)')
            hdr_re=_re.compile(r'^(FN|VR)\s+')
            def flush():
                if ctag and cval: current.append((ctag,' '.join(cval).strip()))
            for line in text.splitlines():
                line=line.lstrip('\ufeff').rstrip()
                if line=='ER':
                    flush(); ctag,cval=None,[]
                    if current: records.append(current); current=[]
                    continue
                if hdr_re.match(line) or not line: continue
                m=tag_re.match(line)
                if m:
                    flush(); ctag=m.group(1); cval=[m.group(2).strip('"'). strip()]
                elif line.startswith(_C) or line.startswith(' '):
                    if ctag: cval.append(line.strip().strip('"'))
            flush()
            if current: records.append(current)
            return records

        def _fmt(record):
            out=[]
            for tag,val in record:
                val=val.strip()
                if tag in ('AU','AF'): out.extend(_authors(tag,val))
                elif tag=='C1':         out.extend(_institutions(tag,val))
                elif tag in ('OI','RI'): out.extend(_semicolon(tag,val))
                elif tag=='CR':          out.extend(_cr(tag,val))
                elif tag in _WF:          out.extend(_wrap(tag,val))
                else:                     out.extend(_simple(tag,val))
            return out

        try:
            self.log("\n"+"="*80)
            self.log("📋 步骤8c: 转换为 WoS 原始格式（VOSviewer 优化版）")
            self.log("="*80)

            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = self._get_latest_file(output_dir)
            if not input_file:
                self.log("❌ 未找到可处理的数据文件，跳过")
                return True, ""

            self.log(f"📥 输入文件: {input_file.name}")
            self.log("🔧 转换格式并修复 CR 引用字段...")

            with open(input_file, 'r', encoding='utf-8-sig') as f:
                text = f.read()

            records = _parse(text)
            self.log(f"   解析到 {len(records):,} 条记录")

            cr_count = sum(1 for r in records if any(t=='CR' for t,_ in r))
            total_cites = 0
            for r in records:
                for t,v in r:
                    if t=='CR':
                        raw=_CR_SEP.split(v.strip()); merged,i=[],0
                        while i<len(raw):
                            p=raw[i].strip()
                            if _re.search(r',\s+\d{4}',p): merged.append(p); i+=1
                            else:
                                if i+1<len(raw): raw[i+1]=p+' '+raw[i+1]
                                i+=1
                        total_cites+=len(merged) if merged else 1
            self.log(f"   含引用记录: {cr_count:,} | 总引用条目: {total_cites:,}")

            out_lines=["FN Clarivate Analytics Web of Science","VR 1.0"]
            for record in records:
                out_lines.append("")
                out_lines.extend(_fmt(record))
                out_lines.append("ER")
            out_lines.append("")

            output_path = output_dir / (input_file.stem + "_vosviewer.txt")
            with open(output_path, 'w', encoding='utf-8', newline='\r\n') as f:
                f.write('\n'.join(out_lines))

            self.log(f"\n✅ 格式转换完成!")
            self.log(f"   输出文件: {output_path.name}")
            self.log(f"   每作者独立行 ✓ | 每引用独立行 ✓ | CRLF ✓ | 无BOM ✓")
            self.log(f"   💡 导入 VOSviewer 时选择 'Web of Science' 格式")
            return True, str(output_path)

        except Exception as e:
            self.log(f"❌ WoS 格式转换失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)

    def statistical_analysis(self, params: Dict) -> Tuple[bool, str]:
        """步骤9: 统计分析"""
        try:
            self.log("📊 步骤9: 统计分析")
            self.log("=" * 80)
            
            output_dir = Path(params.get('output_dir', params['data_dir']))
            
            # 查找数据文件，排除报告文件
            all_files = []
            for prefix in ["merged", "scopus_converted", "wos"]:
                all_files.extend(output_dir.glob(f"{prefix}*.txt"))
            
            # 排除报告文件和临时文件
            data_files = [
                f for f in all_files 
                if not any(exclude in f.name for exclude in [
                    '_report.txt',
                    '_cleaning_report.txt',
                    '_analysis_report.txt',
                    '_statistics.txt',
                    '.tmp'
                ])
            ]
            
            if not data_files:
                self.log("⚠️ 未找到可分析的数据文件")
                return True, ""
            
            # 选择最新的数据文件
            input_file = max(data_files, key=lambda f: f.stat().st_mtime)
            
            self.log(f"📥 输入文件: {input_file.name}")
            
            # 使用智能导入函数
            RecordAnalyzer = import_records_module()
            if RecordAnalyzer is None:
                self.log("⚠️ 统计分析模块未找到")
                self.log("💡 提示: 可将 records.py 放在以下位置之一:")
                self.log("   - gui_app.py 同目录")
                self.log("   - src/bibliometrics/analysis/records.py")
                self.log("   - src/bibliometrics/standardizers/records.py")
                self.log("⏭️ 跳过统计分析")
                return True, ""
            
            try:
                # 查找配置目录
                config_dir = None
                possible_configs = [
                    Path(__file__).parent / "config",
                    Path(params['data_dir']) / "config",
                    Path.cwd() / "config",
                    Path(__file__).parent.parent / "config",
                ]
                
                for cfg_path in possible_configs:
                    if cfg_path.exists() and cfg_path.is_dir():
                        config_dir = cfg_path
                        break
                
                if config_dir is None:
                    config_dir = Path("config")
                    self.log(f"⚠️ 配置目录不存在，使用默认: {config_dir}")
                else:
                    self.log(f"📂 配置目录: {config_dir}")
                
                # 执行分析
                self.log("🔍 开始统计分析...")
                self.log("")
                
                analyzer = RecordAnalyzer(
                    wos_file=str(input_file),
                    config_dir=str(config_dir)
                )
                
                analyzer.analyze()
                
                # 生成报告文件名
                report_file = str(input_file).replace('.txt', '_analysis_report.txt')
                
                self.log("")
                self.log("✅ 统计分析完成!")
                self.log(f"📄 详细报告: {Path(report_file).name}")
                self.log("")
                
                # 显示关键统计
                stats = analyzer.stats
                self.log("📈 关键指标:")
                self.log(f"   总记录数: {stats['total_records']}")
                self.log(f"   覆盖年份: {len(stats['years'])} 年")
                self.log(f"   涉及国家: {len(stats['countries'])} 个")
                self.log(f"   涉及机构: {len(stats['institutions'])} 个")
                
                if stats['countries']:
                    top_country = stats['countries'].most_common(1)[0]
                    self.log(f"   最多国家: {top_country[0]} ({top_country[1]} 篇)")
                
                if stats['years']:
                    year_list = sorted(stats['years'].keys())
                    self.log(f"   年份跨度: {year_list[0]} - {year_list[-1]}")
                
                self.log("")
                
                return True, report_file
                
            except Exception as e:
                self.log(f"❌ 分析过程出错: {e}")
                self.log(traceback.format_exc())
                return False, str(e)
            
        except Exception as e:
            self.log(f"❌ 统计分析失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)
    
    def visualization(self, params: Dict) -> Tuple[bool, str]:
        """步骤10: 可视化图表生成"""
        try:
            self.log("📈 步骤10: 可视化图表")
            self.log("=" * 80)
            
            output_dir = Path(params.get('output_dir', params['data_dir']))
            
            # 查找数据文件（排除报告文件）
            all_files = []
            for prefix in ["merged", "scopus_converted", "wos"]:
                all_files.extend(output_dir.glob(f"{prefix}*.txt"))
            
            data_files = [
                f for f in all_files 
                if not any(exclude in f.name for exclude in [
                    '_report.txt',
                    '_cleaning_report.txt',
                    '_analysis_report.txt',
                    '_statistics.txt',
                    '.tmp'
                ])
            ]
            
            if not data_files:
                self.log("⚠️ 未找到可视化的数据文件")
                return True, ""
            
            input_file = max(data_files, key=lambda f: f.stat().st_mtime)
            self.log(f"📥 输入文件: {input_file.name}")
            
            # 导入可视化模块
            modules = import_visualization_modules()
            if not modules:
                self.log("⚠️ 可视化模块未找到")
                self.log("💡 提示: 可将 plot_citations.py 和 plot_types.py 放在以下位置:")
                self.log("   - gui_app.py 同目录")
                self.log("   - src/bibliometrics/visualization/")
                self.log("   - src/bibliometrics/analysis/")
                self.log("⏭️ 跳过可视化")
                return True, ""
            
            generated_charts = []
            
            # 1. 年度发文量和引用量分析
            if 'citations' in modules:
                try:
                    self.log("")
                    self.log("📊 生成年度发文量和引用量图表...")
                    
                    # 创建输出目录
                    charts_output_dir = output_dir / "Figures and Tables" / "02 各年发文及引文量"
                    charts_output_dir.mkdir(parents=True, exist_ok=True)
                    
                    # 使用实际的方法：parse_wos_file, create_dataframe, plot_*
                    analyzer = modules['citations']()
                    publications, citations = analyzer.parse_wos_file(str(input_file))
                    data = analyzer.create_dataframe(publications, citations)
                    
                    # 生成图表
                    analyzer.plot_publications(data, str(charts_output_dir))
                    analyzer.plot_citations(data, str(charts_output_dir))
                    analyzer.plot_combined(data, str(charts_output_dir))
                    
                    # 保存数据
                    csv_file = charts_output_dir / 'publications_citations_data.csv'
                    data.to_csv(csv_file, index=False)
                    
                    # 记录生成的文件
                    chart_files = [
                        charts_output_dir / "各年发文量.png",
                        charts_output_dir / "各年引用量.png",
                        charts_output_dir / "各年发文量及引用量.png"
                    ]
                    for chart_file in chart_files:
                        if chart_file.exists():
                            generated_charts.append(str(chart_file))
                            self.log(f"   ✅ 已生成: {chart_file.name}")
                    
                except Exception as e:
                    self.log(f"   ⚠️ 年度分析图表生成失败: {e}")
                    self.log(traceback.format_exc())
            
            # 2. 文档类型分析 - 生成三个并排的甜甜圈图
            if 'types' in modules:
                try:
                    self.log("")
                    self.log("📊 生成文档类型分布图表（三数据库对比）...")
                    
                    # 创建输出目录
                    types_output_dir = output_dir / "Figures and Tables" / "01 文档类型"
                    types_output_dir.mkdir(parents=True, exist_ok=True)
                    
                    analyzer = modules['types']()
                    
                    # 🔍 查找三个数据文件
                    # 1. WoS 原始文件 - 在输出文件夹和输入文件夹中都查找
                    input_dir = Path(params.get('data_dir', output_dir))
                    wos_file = None
                    # 先在输出文件夹找
                    for filename in ['wos.txt', 'wos_year_filtered.txt']:
                        candidate = output_dir / filename
                        if candidate.exists():
                            wos_file = candidate
                            break
                    # 如果输出文件夹没有，去输入文件夹找
                    if not wos_file or not wos_file.exists():
                        for filename in ['wos.txt', 'wos_year_filtered.txt']:
                            candidate = input_dir / filename
                            if candidate.exists():
                                wos_file = candidate
                                break
                    # 如果还是没有，设置一个默认值
                    if not wos_file:
                        wos_file = output_dir / 'wos.txt'
                    
                    # 2. Scopus 转换后的文件（优先使用enriched版本）
                    scopus_file = output_dir / 'scopus_enriched.txt'
                    if not scopus_file.exists():
                        scopus_file = output_dir / 'scopus_converted_to_wos.txt'
                    
                    # 3. Final Dataset（当前处理的文件）
                    final_file = input_file
                    
                    # 检查文件是否存在
                    missing_files = []
                    if not wos_file.exists():
                        missing_files.append("WoS")
                        self.log(f"   ⚠️ 未找到 WoS 文件: {wos_file}")
                    if not scopus_file.exists():
                        missing_files.append("Scopus")
                        self.log(f"   ⚠️ 未找到 Scopus 文件: {scopus_file}")
                    if not final_file.exists():
                        missing_files.append("Final")
                        self.log(f"   ⚠️ 未找到最终文件: {final_file}")
                    
                    if missing_files:
                        self.log(f"   ⚠️ 缺少文件: {', '.join(missing_files)}")
                        self.log("   ℹ️  改为生成单一数据集图表...")
                        # 回退到单图模式
                        counts = analyzer.parse_wos_file(str(final_file))
                        analyzer.plot_single_dataset(counts, str(types_output_dir))
                        
                        # 保存简化数据
                        import pandas as pd
                        data = pd.DataFrame({
                            'Article_Type': ['Article', 'Review'],
                            'Count': [counts['Article'], counts['Review']],
                            'Percentage': [
                                counts['Article'] / (counts['Article'] + counts['Review']) * 100 if (counts['Article'] + counts['Review']) > 0 else 0,
                                counts['Review'] / (counts['Article'] + counts['Review']) * 100 if (counts['Article'] + counts['Review']) > 0 else 0
                            ]
                        })
                        csv_file = types_output_dir / 'document_types_data.csv'
                        data.to_csv(csv_file, index=False)
                    else:
                        # ✅ 三个文件都存在，生成对比图
                        self.log(f"   ✓ WoS 文件: {wos_file.name}")
                        self.log(f"   ✓ Scopus 文件: {scopus_file.name}")
                        self.log(f"   ✓ Final 文件: {final_file.name}")
                        
                        import pandas as pd
                        
                        # 解析三个文件
                        wos_counts = analyzer.parse_wos_file(str(wos_file))
                        scopus_counts = analyzer.parse_wos_file(str(scopus_file))
                        final_counts = analyzer.parse_wos_file(str(final_file))
                        
                        # 创建 DataFrame
                        data = pd.DataFrame({
                            'Article_Type': ['Article', 'Review'],
                            'WoS_Count': [wos_counts['Article'], wos_counts['Review']],
                            'Scopus_Count': [scopus_counts['Article'], scopus_counts['Review']],
                            'Final_Count': [final_counts['Article'], final_counts['Review']]
                        })
                        
                        # 生成三个并排的甜甜圈图
                        analyzer.plot_distribution(data, str(types_output_dir))
                        
                        self.log(f"   ✅ 生成三数据库对比图")
                        
                        # 保存完整数据
                        csv_file = types_output_dir / 'document_types_data.csv'
                        data.to_csv(csv_file, index=False)
                    
                    # 记录生成的文件
                    chart_file = types_output_dir / "document_types.png"
                    if chart_file.exists():
                        generated_charts.append(str(chart_file))
                        self.log(f"   ✅ 已生成: {chart_file.name}")
                    
                except Exception as e:
                    self.log(f"   ⚠️ 文档类型图表生成失败: {e}")
                    self.log(traceback.format_exc())
            
            # 总结
            self.log("")
            if generated_charts:
                self.log(f"✅ 可视化完成! 共生成 {len(generated_charts)} 个图表")
                self.log("")
                self.log("📁 生成的图表:")
                for chart in generated_charts:
                    self.log(f"   - {Path(chart).name}")
                return True, ", ".join(generated_charts)
            else:
                self.log("⚠️ 未能生成任何图表")
                return True, ""
            
        except Exception as e:
            self.log(f"❌ 可视化失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)

    def reformatrepair_wos(self, params: Dict) -> Tuple[bool, str]:
        """最终步骤: WoS 格式规范修复
        
        对工作流最终输出文件执行 reformatrepair_wos 逻辑：
          - 补全缺失 AU 字段（从 AF / C1 提取）
          - 将 C1、C3、RP 多行合并为单行
          - 确保每条记录以 ER 结尾、记录间有空行
          - 循环处理直到格式完全正确（最多20轮）
          - 输出 <原文件名>_reformatted.txt
        """
        import re as _re

        try:
            self.log("✨ 最终步骤: 格式规范修复 (reformatrepair)")
            self.log("=" * 80)

            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = self._get_latest_file(output_dir)
            if not input_file:
                self.log("⚠️ 未找到可处理的数据文件，跳过")
                return True, ""

            self.log(f"📥 输入文件: {input_file.name}")
            output_file = output_dir / (input_file.stem + "_reformatted.txt")
            self.log(f"📤 输出文件: {output_file.name}")

            # ── 以下完整还原 reformatrepair_wos.py 的逻辑 ──────────────────

            def extract_au_from_af(af_line):
                if not af_line:
                    return ""
                authors = af_line[3:].strip()
                author_list = [a.strip() for a in authors.split(";")]
                au_lines = []
                for author in author_list:
                    if ',' in author:
                        parts = author.split(", ")
                        surname = parts[0].strip()
                        given_name = parts[1].strip() if len(parts) > 1 else ""
                        if given_name:
                            initials = "".join([w[0].upper() for w in given_name.split()])
                            au_lines.append(f"{surname}, {initials}")
                        else:
                            au_lines.append(f"{surname},")
                    else:
                        au_lines.append(author)
                return "\n   ".join(au_lines)

            def extract_au_from_c1(c1_line):
                if not c1_line:
                    return ""
                content = c1_line[3:].strip()
                matches = _re.findall(r'\[(.*?)\]', content)
                au_names = []
                for match in matches:
                    for author in [a.strip() for a in match.split(";")]:
                        if ',' in author:
                            parts = author.split(", ")
                            surname = parts[0].strip()
                            given_name = parts[1].strip() if len(parts) > 1 else ""
                            if given_name:
                                initials = "".join([w[0].upper() for w in given_name.split()])
                                au_names.append(f"{surname}, {initials}")
                            else:
                                au_names.append(f"{surname},")
                        else:
                            au_names.append(author)
                return "\n   ".join(au_names) if au_names else ""

            def format_c1_line(c1_content):
                if not c1_content:
                    return ""
                content = _re.sub(r'\s+', ' ', c1_content[3:].strip())
                return f"C1 {content}"

            def format_c3_line(c3_content):
                if not c3_content:
                    return ""
                content = _re.sub(r'\s+', ' ', c3_content[3:].strip())
                return f"C3 {content}"

            def format_rp_line(rp_content):
                if not rp_content:
                    return ""
                content = _re.sub(r'\s+', ' ', rp_content[3:].strip())
                return f"RP {content}"

            def process_record(record_content):
                if not record_content.strip():
                    return None
                lines = record_content.strip().split('\n')
                # 剥离每行首尾的多余双引号（如 "AU Hida, RM" → AU Hida, RM）
                lines = [
                    l[1:-1] if len(l) >= 2 and l.startswith('"') and l.endswith('"') else l
                    for l in lines
                ]
                has_au = any(l.startswith('AU ') for l in lines)
                af_line = next((l for l in lines if l.startswith('AF ')), None)
                c1_line = next((l for l in lines if l.startswith('C1 ')), None)

                if not has_au:
                    au_content = extract_au_from_af(af_line) if af_line else ""
                    if not au_content and c1_line:
                        au_content = extract_au_from_c1(c1_line)
                    if au_content:
                        # 将多作者字符串拆成单行插入，不加引号
                        au_single_lines = au_content.split('\n   ')
                        formatted_au_lines = []
                        for idx, author in enumerate(au_single_lines):
                            author = author.strip()
                            if idx == 0:
                                formatted_au_lines.append(f'AU {author}')
                            else:
                                formatted_au_lines.append(f'   {author}')

                        new_lines, inserted = [], False
                        for line in lines:
                            new_lines.append(line)
                            if not inserted and line.startswith('PT '):
                                new_lines.extend(formatted_au_lines)
                                inserted = True
                        if not inserted:
                            new_lines = formatted_au_lines + new_lines
                        lines = new_lines

                new_lines, i = [], 0
                while i < len(lines):
                    line = lines[i]
                    if line.startswith('C1 '):
                        c1_content = line
                        i += 1
                        while i < len(lines) and (lines[i].startswith('   ') or lines[i].startswith(' ')):
                            c1_content += " " + lines[i].strip()
                            i += 1
                        new_lines.append(format_c1_line(c1_content))
                        continue
                    elif line.startswith('C3 '):
                        c3_content = line
                        i += 1
                        while i < len(lines) and (lines[i].startswith('   ') or lines[i].startswith(' ')):
                            c3_content += " " + lines[i].strip()
                            i += 1
                        new_lines.append(format_c3_line(c3_content))
                        continue
                    elif line.startswith('RP '):
                        rp_content = line
                        i += 1
                        while i < len(lines) and (lines[i].startswith('   ') or lines[i].startswith(' ')):
                            rp_content += " " + lines[i].strip()
                            i += 1
                        new_lines.append(format_rp_line(rp_content))
                        continue
                    else:
                        new_lines.append(line)
                        i += 1
                lines = new_lines

                if not lines[-1].startswith('ER'):
                    lines.append('ER')
                return '\n'.join(lines)

            def validate_format(content):
                pt_j_count = len(_re.findall(r'^PT J', content, _re.MULTILINE))
                er_count   = len(_re.findall(r'^ER$',  content, _re.MULTILINE))
                lines = content.split('\n')
                pt_j_positions = [i for i, l in enumerate(lines) if l.startswith('PT J')]
                empty_before = sum(
                    1 for idx, pos in enumerate(pt_j_positions)
                    if pos > 0 and lines[pos - 1].strip() == ''
                )
                is_valid = (pt_j_count == er_count and
                            empty_before == len(pt_j_positions) - 1)
                return is_valid, pt_j_count, er_count, empty_before, len(pt_j_positions)

            # ── 读取文件并循环修复 ───────────────────────────────────────────
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()

            for iteration in range(1, 21):
                is_valid, pt_j_count, er_count, empty_before, total_pt_j = validate_format(content)
                self.log(f"   第{iteration}轮 — PT J: {pt_j_count}, ER: {er_count}, "
                         f"空行: {empty_before}/{max(total_pt_j-1,0)}, "
                         f"格式{'✓' if is_valid else '✗'}")
                if is_valid:
                    break

                parts = _re.split(r'(?=^PT J)', content, flags=_re.MULTILINE)
                fixed_records, missing_au_count = [], 0
                for part in parts:
                    if not part.strip() or not part.strip().startswith('PT J'):
                        continue
                    if 'AU ' not in part:
                        missing_au_count += 1
                    processed = process_record(part)
                    if processed:
                        fixed_records.append(processed)

                new_content = '\n\n'.join(fixed_records)

                # 内容无变化时强制在 PT J 前补空行
                if new_content == content and not is_valid:
                    lines = new_content.split('\n')
                    result = []
                    for line in lines:
                        if line.startswith('PT J') and result and result[-1].strip():
                            result.append('')
                        result.append(line)
                    new_content = '\n'.join(result)

                content = new_content

                is_valid_after, *_ = validate_format(content)
                if is_valid_after:
                    self.log(f"   ✅ 第{iteration}轮修复后格式正确")
                    break

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            is_valid_final, pt_j_f, er_f, *_ = validate_format(content)
            self.log(f"✅ 格式规范修复完成")
            self.log(f"   PT J: {pt_j_f} | ER: {er_f} | "
                     f"格式{'正确 ✓' if is_valid_final else '仍有问题 ⚠️'}")
            self.log(f"   输出: {output_file.name}")
            return True, str(output_file)

        except Exception as e:
            self.log(f"❌ 格式规范修复失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)

    def _get_latest_file(self, directory: Path, prefixes: List[str] = None) -> Optional[Path]:
        """获取最新的处理文件"""
        if prefixes is None:
            prefixes = ["merged", "scopus_converted", "wos"]
        
        files = []
        for prefix in prefixes:
            files.extend(directory.glob(f"{prefix}*.txt"))
        
        # 🔧 FIX: Exclude report files, cleaning reports, and temporary files
        data_files = [
            f for f in files 
            if not any(exclude in f.name for exclude in [
                '_report.txt',
                '_cleaning_report.txt',
                '_analysis_report.txt',
                '_statistics.txt',
                '_reformatted.txt',
                '.tmp'
            ])
        ]
        
        if not data_files:
            return None
        
        # 按修改时间排序，返回最新的
        return max(data_files, key=lambda f: f.stat().st_mtime)
    
    def run_full_workflow(self, params: Dict) -> bool:
        """运行完整工作流"""
        self.stop_requested = False
        
        steps = [
            ("格式转换",       self.format_conversion),
            ("合并去重",       self.merge_and_deduplicate),
            ("字段修复",       self.field_repair) if params.get('enable_repair') else None,
            ("撤稿筛选",       self.retraction_filter) if params.get('enable_retraction_filter') else None,
            ("高级检索",       self.advanced_search),
            ("语言筛选",       self.language_filter),
            ("年份筛选",       self.year_filter),
            ("机构清洗",       self.institution_cleaning),
            ("WoS格式恢复",    self.restore_wos_standard_format),  # 去除多余引号版本
            ("WoS原始格式转换", self.convert_to_wos_format),        # 还原为完整WoS原始格式
            ("统计分析",       self.statistical_analysis),
            ("可视化",         self.visualization),
            ("格式规范修复",    self.reformatrepair_wos),            # 最终 AU/C1/C3/RP 格式修复
        ]
        
        # 过滤掉None（被禁用的步骤）
        # Fix: Filter None items first before unpacking

        steps = [item for item in steps if item is not None]

        steps = [(name, func) for name, func in steps if func is not None]
        
        self.log(f"📋 将执行 {len(steps)} 个步骤")
        self.log("=" * 80)
        
        for i, (step_name, step_func) in enumerate(steps, 1):
            if self.stop_requested:
                self.log("⏸️ 用户终止处理")
                return False
            
            self.log(f"\n▶️ 步骤 {i}/{len(steps)}: {step_name}")
            success, message = step_func(params)
            
            if not success:
                self.log(f"❌ {step_name}失败: {message}")
                return False
        
        self.log("\n" + "=" * 80)
        self.log("🎉 所有步骤完成！")
        return True


# ============================================================================
# 主GUI类
# ============================================================================

class BibliometricGUI:
    """文献计量学数据整合工具GUI"""
    
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Bibliometric Data Consolidation Tool v7.0")
        self.root.geometry("1200x800")
        
        # 变量初始化
        self.data_dir = ctk.StringVar(value="")
        self.output_dir = ctk.StringVar(value="")
        self.year_range = ctk.StringVar(value="2015-2024")
        self.language = ctk.StringVar(value="English")
        self.dedup_method = ctk.StringVar(value="ultimate")
        
        # 高级功能开关
        self.enable_repair = ctk.BooleanVar(value=True)
        self.enable_ai_repair = ctk.BooleanVar(value=False)
        self.enable_both_versions = ctk.BooleanVar(value=False)
        self.enable_wos_format_convert = ctk.BooleanVar(value=False)
        self.enable_retraction_filter = ctk.BooleanVar(value=True)
        self.enable_online_verification = ctk.BooleanVar(value=False)
        self.enable_advanced_search = ctk.BooleanVar(value=False)
        self.search_query = ctk.StringVar(value="")
        self.enable_institution_cleaning = ctk.BooleanVar(value=False)
        
        # 日志队列
        self.log_queue = queue.Queue()
        self.processing = False
        self.worker_thread = None
        
        # 创建UI
        self._create_ui()
        
        # 启动日志更新
        self._update_log_display()
    
    def _create_ui(self):
        """创建UI界面"""
        # 主容器
        main_container = ctk.CTkFrame(self.root, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 创建标题栏
        self._create_header(main_container)
        
        # 创建内容区域
        content_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, pady=(10, 0))
        
        # 左侧配置面板
        left_panel = ctk.CTkFrame(content_frame, width=500, fg_color="transparent")
        left_panel.pack(side="left", fill="both", expand=False, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # 创建滚动区域
        scroll_container = ctk.CTkScrollableFrame(
            left_panel,
            fg_color=("gray95", "gray15")
        )
        scroll_container.pack(fill="both", expand=True)
        
        self._create_file_selection(scroll_container)
        self._create_basic_params(scroll_container)
        self._create_advanced_features(scroll_container)
        
        # 右侧日志面板
        right_panel = ctk.CTkFrame(content_frame, fg_color="transparent")
        right_panel.pack(side="right", fill="both", expand=True)
        
        self._create_log_panel(right_panel)
        
        # 底部控制栏
        self._create_control_bar(main_container)
    
    def _create_header(self, parent):
        """创建标题栏"""
        header = ctk.CTkFrame(parent, fg_color=("gray90", "gray20"), height=60)
        header.pack(fill="x", pady=(0, 10))
        header.pack_propagate(False)
        
        # 左侧标题
        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(side="left", padx=20, pady=10)
        
        ctk.CTkLabel(
            title_frame,
            text="📊 Bibliometric Data Consolidation Tool",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            title_frame,
            text="v7.0.0",
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray50")
        ).pack(anchor="w")
        
        # 右侧状态
        self.status_badge = StatusBadge(header)
        self.status_badge.pack(side="right", padx=20)
        self.status_badge.set_status('idle')
    
    def _create_file_selection(self, parent):
        """创建文件选择卡片"""
        card = ModernCard(parent, "📁 文件选择")
        card.pack(fill="x", padx=10, pady=5)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=20, pady=(0, 12))
        
        # 数据目录
        dir_row = ctk.CTkFrame(content, fg_color="transparent")
        dir_row.pack(fill="x", pady=5)
        
        ctk.CTkLabel(
            dir_row,
            text="数据目录:",
            font=ctk.CTkFont(size=12),
            width=80,
            anchor="w"
        ).pack(side="left")
        
        ctk.CTkEntry(
            dir_row,
            textvariable=self.data_dir,
            font=ctk.CTkFont(size=11)
        ).pack(side="left", fill="x", expand=True, padx=(5, 5))
        
        ctk.CTkButton(
            dir_row,
            text="浏览",
            width=70,
            command=self._browse_data_directory
        ).pack(side="left")
        
        # 输出目录
        output_row = ctk.CTkFrame(content, fg_color="transparent")
        output_row.pack(fill="x", pady=5)
        
        ctk.CTkLabel(
            output_row,
            text="输出目录:",
            font=ctk.CTkFont(size=12),
            width=80,
            anchor="w"
        ).pack(side="left")
        
        ctk.CTkEntry(
            output_row,
            textvariable=self.output_dir,
            font=ctk.CTkFont(size=11),
            placeholder_text="可选，留空则使用数据目录"
        ).pack(side="left", fill="x", expand=True, padx=(5, 5))
        
        ctk.CTkButton(
            output_row,
            text="浏览",
            width=70,
            command=self._browse_output_directory
        ).pack(side="left")
    
    def _create_basic_params(self, parent):
        """创建基础参数卡片"""
        card = ModernCard(parent, "⚙️ 基础参数")
        card.pack(fill="x", padx=10, pady=5)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=20, pady=(0, 12))
        
        # 年份范围
        year_row = ctk.CTkFrame(content, fg_color="transparent")
        year_row.pack(fill="x", pady=5)
        
        ctk.CTkLabel(
            year_row,
            text="年份范围:",
            font=ctk.CTkFont(size=12),
            width=100,
            anchor="w"
        ).pack(side="left")
        
        ctk.CTkEntry(
            year_row,
            textvariable=self.year_range,
            width=150,
            font=ctk.CTkFont(size=11)
        ).pack(side="left", padx=5)
        
        # 语言
        lang_row = ctk.CTkFrame(content, fg_color="transparent")
        lang_row.pack(fill="x", pady=5)
        
        ctk.CTkLabel(
            lang_row,
            text="语言:",
            font=ctk.CTkFont(size=12),
            width=100,
            anchor="w"
        ).pack(side="left")
        
        ctk.CTkOptionMenu(
            lang_row,
            variable=self.language,
            values=["All", "English", "Chinese"],
            width=150
        ).pack(side="left", padx=5)
        
        # 去重方法
        dedup_row = ctk.CTkFrame(content, fg_color="transparent")
        dedup_row.pack(fill="x", pady=5)
        
        ctk.CTkLabel(
            dedup_row,
            text="机构清洗:",
            font=ctk.CTkFont(size=12),
            width=100,
            anchor="w"
        ).pack(side="left")
        
        ctk.CTkOptionMenu(
            dedup_row,
            variable=self.dedup_method,
            values=["basic", "standard", "ultimate"],
            width=150
        ).pack(side="left", padx=5)
    
    def _create_advanced_features(self, parent):
        """创建高级功能卡片"""
        card = ModernCard(parent, "🚀 高级功能")
        card.pack(fill="x", padx=10, pady=5)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=20, pady=(0, 12))
        
        # 字段修复
        repair_section = ctk.CTkFrame(content, fg_color=("gray85", "gray20"), corner_radius=8)
        repair_section.pack(fill="x", pady=5)
        
        self.repair_cb = ctk.CTkCheckBox(
            repair_section,
            text="启用字段修复 (基于源数据补全缺失字段)",
            variable=self.enable_repair,
            command=self._on_repair_toggle
        )
        self.repair_cb.pack(anchor="w", padx=20, pady=(8, 2))
        
        self.ai_repair_cb = ctk.CTkCheckBox(
            repair_section,
            text="— 启用AI智能补全 (使用AI检索缺失信息)",
            variable=self.enable_ai_repair,
            state="normal" if self.enable_repair.get() else "disabled"
        )
        self.ai_repair_cb.pack(anchor="w", padx=40, pady=2)
        
        self.both_versions_cb = ctk.CTkCheckBox(
            repair_section,
            text="— 输出修复后两个版本 (便于对比)",
            variable=self.enable_both_versions,
            state="normal" if self.enable_repair.get() else "disabled"
        )
        self.both_versions_cb.pack(anchor="w", padx=40, pady=(2, 4))

        self.wos_convert_cb = ctk.CTkCheckBox(
            repair_section,
            text="— 转换为 WoS 原始导出格式 (每作者独行/引号/折行)",
            variable=self.enable_wos_format_convert,
            state="normal" if self.enable_repair.get() else "disabled"
        )
        self.wos_convert_cb.pack(anchor="w", padx=40, pady=(2, 8))
        
        # 撤稿筛选
        retraction_section = ctk.CTkFrame(content, fg_color=("gray85", "gray20"), corner_radius=8)
        retraction_section.pack(fill="x", pady=5)
        
        self.retraction_cb = ctk.CTkCheckBox(
            retraction_section,
            text="筛选撤稿文献 (检测并移除已撤稿文献)",
            variable=self.enable_retraction_filter,
            command=self._on_retraction_toggle
        )
        self.retraction_cb.pack(anchor="w", padx=20, pady=(8, 2))
        
        self.online_cb = ctk.CTkCheckBox(
            retraction_section,
            text="— 启用在线数据库查询 (更准但较慢)",
            variable=self.enable_online_verification,
            state="normal" if self.enable_retraction_filter.get() else "disabled"
        )
        self.online_cb.pack(anchor="w", padx=40, pady=(2, 8))
        
        # 高级检索
        search_section = ctk.CTkFrame(content, fg_color=("gray85", "gray20"), corner_radius=8)
        search_section.pack(fill="x", pady=5)
        
        self.search_cb = ctk.CTkCheckBox(
            search_section,
            text="启用高级检索 (使用WoS检索式语法)",
            variable=self.enable_advanced_search,
            command=self._on_search_toggle
        )
        self.search_cb.pack(anchor="w", padx=20, pady=2)
        
        self.search_entry = ctk.CTkEntry(
            search_section,
            textvariable=self.search_query,
            placeholder_text="例: TI=(cancer OR tumor) AND AB=treatment",
            state="disabled"
        )
        self.search_entry.pack(fill="x", padx=40, pady=(2, 8))
        
        # 其他功能
        other_section = ctk.CTkFrame(content, fg_color=("gray85", "gray20"), corner_radius=8)
        other_section.pack(fill="x", pady=5)
        
        ctk.CTkCheckBox(
            other_section,
            text="机构名称清洗 (标准化机构名称)",
            variable=self.enable_institution_cleaning
        ).pack(anchor="w", padx=20, pady=8)
    
    def _create_log_panel(self, parent):
        """创建日志面板"""
        card = ModernCard(parent, "📝 处理日志")
        card.pack(fill="both", expand=True)
        
        # 日志文本框
        self.log_text = ctk.CTkTextbox(
            card,
            font=ctk.CTkFont(family="Monaco", size=11),
            wrap="word"
        )
        self.log_text.pack(fill="both", expand=True, padx=20, pady=(0, 12))
    
    def _create_control_bar(self, parent):
        """创建控制栏"""
        control_bar = ctk.CTkFrame(parent, fg_color="transparent", height=50)
        control_bar.pack(fill="x", pady=(10, 0))
        control_bar.pack_propagate(False)
        
        # 按钮行
        button_row = ctk.CTkFrame(control_bar, fg_color="transparent")
        button_row.pack(expand=True)
        
        # 开始按钮
        self.start_button = ctk.CTkButton(
            button_row,
            text="🚀 开始处理",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            command=self._start_processing
        )
        self.start_button.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # 退出按钮
        exit_btn = ctk.CTkButton(
            button_row,
            text="❌ 退出",
            font=ctk.CTkFont(size=14),
            height=40,
            width=100,
            fg_color=("gray70", "gray30"),
            hover_color=("gray60", "gray25"),
            command=self.root.quit
        )
        exit_btn.pack(side="left")
    
    def _on_repair_toggle(self):
        """字段修复开关切换"""
        if self.enable_repair.get():
            self.ai_repair_cb.configure(state="normal")
            self.both_versions_cb.configure(state="normal")
            self.wos_convert_cb.configure(state="normal")
        else:
            self.ai_repair_cb.configure(state="disabled")
            self.both_versions_cb.configure(state="disabled")
            self.wos_convert_cb.configure(state="disabled")
    
    def _on_retraction_toggle(self):
        """撤稿筛选开关切换"""
        if self.enable_retraction_filter.get():
            self.online_cb.configure(state="normal")
        else:
            self.online_cb.configure(state="disabled")
    
    def _on_search_toggle(self):
        """高级检索开关切换"""
        if self.enable_advanced_search.get():
            self.search_entry.configure(state="normal")
        else:
            self.search_entry.configure(state="disabled")
    
    def _browse_data_directory(self):
        """浏览数据目录"""
        directory = filedialog.askdirectory(title="选择数据目录")
        if directory:
            self.data_dir.set(directory)
    
    def _browse_output_directory(self):
        """浏览输出目录"""
        directory = filedialog.askdirectory(title="选择输出目录")
        if directory:
            self.output_dir.set(directory)
    
    def _start_processing(self):
        """开始处理"""
        if self.processing:
            messagebox.showwarning("警告", "已有任务正在运行")
            return
        
        # 验证输入
        if not self.data_dir.get():
            messagebox.showerror("错误", "请选择数据目录")
            return
        
        # 准备参数
        params = {
            'data_dir': self.data_dir.get(),
            'output_dir': self.output_dir.get() or self.data_dir.get(),
            'year_range': self.year_range.get(),
            'language': self.language.get(),
            'dedup_method': self.dedup_method.get(),
            'enable_repair': self.enable_repair.get(),
            'enable_ai_repair': self.enable_ai_repair.get(),
            'enable_both_versions': self.enable_both_versions.get(),
            'enable_wos_format_convert': self.enable_wos_format_convert.get(),
            'enable_retraction_filter': self.enable_retraction_filter.get(),
            'enable_online_verification': self.enable_online_verification.get(),
            'enable_advanced_search': self.enable_advanced_search.get(),
            'search_query': self.search_query.get(),
            'enable_institution_cleaning': self.enable_institution_cleaning.get()
        }
        
        # 清空日志
        self.log_text.delete("1.0", "end")
        
        # 更新状态
        self.processing = True
        self.status_badge.set_status('running')
        self.start_button.configure(state="disabled")
        
        # 启动工作线程
        self.worker_thread = threading.Thread(
            target=self._run_workflow,
            args=(params,),
            daemon=True
        )
        self.worker_thread.start()
    
    def _run_workflow(self, params: Dict):
        """在后台线程运行工作流"""
        try:
            engine = WorkflowEngine(self._log)
            success = engine.run_full_workflow(params)
            
            if success:
                self.log_queue.put(("STATUS", "success"))
            else:
                self.log_queue.put(("STATUS", "error"))
                
        except Exception as e:
            self._log(f"❌ 致命错误: {e}")
            self._log(traceback.format_exc())
            self.log_queue.put(("STATUS", "error"))
        finally:
            self.log_queue.put(("DONE", None))
    
    def _log(self, message: str):
        """添加日志消息"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_queue.put(("LOG", f"[{timestamp}] {message}"))
    
    def _update_log_display(self):
        """更新日志显示"""
        try:
            while True:
                msg_type, content = self.log_queue.get_nowait()
                
                if msg_type == "LOG":
                    self.log_text.insert("end", content + "\n")
                    self.log_text.see("end")
                elif msg_type == "STATUS":
                    self.status_badge.set_status(content)
                elif msg_type == "DONE":
                    self.processing = False
                    self.start_button.configure(state="normal")
                    
        except queue.Empty:
            pass
        
        # 继续更新
        self.root.after(100, self._update_log_display)
    
    def run(self):
        """运行应用"""
        self.root.mainloop()


# ============================================================================
# 主函数
# ============================================================================

def main():
    """主函数"""
    try:
        app = BibliometricGUI()
        app.run()
    except Exception as e:
        logger.error(f"启动失败: {e}")
        logger.error(traceback.format_exc())
        messagebox.showerror("启动失败", f"{e}\n\n{traceback.format_exc()}")


if __name__ == "__main__":
    main()
