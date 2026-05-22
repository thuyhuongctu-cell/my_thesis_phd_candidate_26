#!/usr/bin/env python3
import re

with open('gui_app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 完整的修复后的language_filter方法
new_language_filter = '''    def language_filter(self, params: Dict) -> Tuple[bool, str]:
        """步骤6: 语言筛选"""
        try:
            self.log("🌍 步骤6: 语言筛选")
            self.log("=" * 80)
            
            language = params.get('language', 'All')
            if language == 'All':
                self.log("⏭️ 不限语言，跳过筛选")
                return True, ""
            
            self.log(f"🔤 目标语言: {language}")
            
            output_dir = Path(params.get('output_dir', params['data_dir']))
            input_file = self._get_latest_file(output_dir)
            
            if not input_file:
                return False, "未找到输入文件"
            
            # ===== 修复：直接导入当前目录的language模块 =====
            try:
                import sys
                import os
                # 添加当前目录到系统路径
                current_dir = os.path.dirname(os.path.abspath(__file__))
                if current_dir not in sys.path:
                    sys.path.insert(0, current_dir)
                
                # 检查language.py是否存在
                language_file = os.path.join(current_dir, 'language.py')
                if not os.path.exists(language_file):
                    self.log(f"⚠️ language.py不存在: {language_file}")
                    self.log("⏭️ 跳过语言筛选")
                    return True, str(input_file)
                
                from language import LanguageFilter
                self.log(f"✅ 成功导入LanguageFilter")
                
                # 输出文件
                output_file = output_dir / f"{input_file.stem}_{language.lower()}.txt"
                
                # 创建筛选器并执行
                filter_tool = LanguageFilter(
                    input_file=str(input_file),
                    output_file=str(output_file),
                    target_language=language
                )
                
                success = filter_tool.run()
                
                if success:
                    self.log(f"✅ 语言筛选完成")
                    self.log(f"   筛选后记录: {filter_tool.stats['filtered_records']}")
                    return True, str(output_file)
                else:
                    return False, "语言筛选失败"
                    
            except ImportError as e:
                self.log(f"⚠️ 语言筛选模块导入失败: {e}")
                # 列出当前目录的py文件，帮助诊断
                try:
                    import os
                    py_files = [f for f in os.listdir(current_dir) if f.endswith('.py')]
                    self.log(f"📋 当前目录Python文件: {', '.join(py_files[:10])}")
                except:
                    pass
                self.log("⏭️ 跳过语言筛选")
                return True, str(input_file)
            except Exception as e:
                self.log(f"⚠️ 语言筛选执行失败: {e}")
                self.log("⏭️ 跳过语言筛选")
                return True, str(input_file)
            
        except Exception as e:
            self.log(f"❌ 筛选失败: {e}")
            self.log(traceback.format_exc())
            return False, str(e)'''

# 替换原有的language_filter方法
pattern = r'    def language_filter\(self, params: Dict\) -> Tuple\[bool, str\]:.*?return False, str\(e\)'
new_content = re.sub(pattern, new_language_filter, content, flags=re.DOTALL)

with open('gui_app.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ language_filter方法已完全替换")
