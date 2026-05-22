import re

def extract_au_from_af(af_line):
    """
    从 AF 行提取作者姓名并格式化为 AU 字段格式
    AF 格式: "Shi, Yan; Li, Wei; Wang, Xiaoming"
    AU 格式: "Shi, Y\n   Li, W\n   Wang, X"
    """
    if not af_line:
        return ""
    
    # 移除前缀 "AF "
    authors = af_line[3:].strip()
    
    # 按分号分隔作者
    author_list = [a.strip() for a in authors.split(";")]
    
    au_lines = []
    for author in author_list:
        # 格式：姓, 名
        if ',' in author:
            parts = author.split(", ")
            surname = parts[0].strip()
            given_name = parts[1].strip() if len(parts) > 1 else ""
            
            # 获取名字首字母
            if given_name:
                initials = "".join([word[0].upper() for word in given_name.split()])
                au_lines.append(f"{surname}, {initials}")
            else:
                au_lines.append(f"{surname},")
        else:
            au_lines.append(author)
    
    # 返回带换行的 AU 字段内容
    return "\n   ".join(au_lines)

def extract_au_from_c1(c1_line):
    """
    从 C1 行提取作者姓名并格式化为 AU 字段格式
    C1 格式: "[Zhou, Quansheng; Cao, Zhifei] Soochow Univ..."
    返回 AU 格式: "Zhou, Q\n   Cao, Z"
    """
    if not c1_line:
        return ""
    
    # 移除前缀 "C1 "
    content = c1_line[3:].strip()
    
    # 匹配 [作者] 部分
    pattern = r'\[(.*?)\]'
    matches = re.findall(pattern, content)
    
    au_names = []
    for match in matches:
        # 作者用分号分隔
        authors = [a.strip() for a in match.split(";")]
        for author in authors:
            if ',' in author:
                parts = author.split(", ")
                surname = parts[0].strip()
                given_name = parts[1].strip() if len(parts) > 1 else ""
                if given_name:
                    initials = "".join([word[0].upper() for word in given_name.split()])
                    au_names.append(f"{surname}, {initials}")
                else:
                    au_names.append(f"{surname},")
            else:
                au_names.append(author)
    
    if au_names:
        return "\n   ".join(au_names)
    return ""

def format_c1_line(c1_content):
    """
    格式化 C1 为单行格式
    作者在方括号内，多个作者用分号分隔，多个机构用句点分隔
    """
    if not c1_content:
        return ""
    
    # 移除前缀 "C1 "
    content = c1_content[3:].strip()
    
    # 将换行和多个空格替换为空格
    content = re.sub(r'\s+', ' ', content)
    
    return f"C1 {content}"

def format_c3_line(c3_content):
    """
    格式化 C3 为单行格式
    C3 格式：机构名称，用分号分隔
    例如: C3 Urmia University of Medical Sciences; Urmia University of Medical Sciences
    """
    if not c3_content:
        return ""
    
    # 移除前缀 "C3 "
    content = c3_content[3:].strip()
    
    # 将换行和多个空格替换为空格
    content = re.sub(r'\s+', ' ', content)
    
    # 确保机构之间用分号分隔
    # 如果包含逗号，可能需要处理，但保持原样
    
    return f"C3 {content}"

def format_rp_line(rp_content):
    """
    格式化 RP 为单行格式
    RP 格式：作者姓名用分号分隔，然后是机构
    例如: RP Zhou, QS; Cao, ZF (通讯作者)，Soochow Univ...
    """
    if not rp_content:
        return ""
    
    # 移除前缀 "RP "
    content = rp_content[3:].strip()
    
    # 将换行和多个空格替换为空格
    content = re.sub(r'\s+', ' ', content)
    
    return f"RP {content}"

def process_record(record_content, verbose=False):
    """处理单条记录，返回处理后的内容"""
    if not record_content.strip():
        return None
    
    lines = record_content.strip().split('\n')
    
    # 检查是否有 AU 字段
    has_au = any(line.startswith('AU ') for line in lines)
    
    # 查找 AF 或 C1 字段
    af_line = next((line for line in lines if line.startswith('AF ')), None)
    c1_line = next((line for line in lines if line.startswith('C1 ')), None)
    
    # 如果缺少 AU 字段
    if not has_au:
        au_content = None
        
        # 优先从 AF 提取
        if af_line:
            au_content = extract_au_from_af(af_line)
            if verbose and au_content:
                print(f"  从 AF 提取到 {au_content.count(chr(10))+1} 个作者")
        # 如果 AF 没有或提取为空，从 C1 提取
        if not au_content and c1_line:
            au_content = extract_au_from_c1(c1_line)
            if verbose and au_content:
                print(f"  从 C1 提取到 {au_content.count(chr(10))+1} 个作者")
        
        # 如果成功提取到 AU 内容，则插入
        if au_content:
            new_lines = []
            inserted = False
            for line in lines:
                new_lines.append(line)
                # 在 PT 行之后插入 AU
                if not inserted and line.startswith('PT '):
                    new_lines.append(f'AU {au_content}')
                    inserted = True
            if not inserted:
                new_lines.insert(0, f'AU {au_content}')
            lines = new_lines
    
    # 格式化 C1、C3、RP 为单行格式
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 处理 C1 字段
        if line.startswith('C1 '):
            c1_content = line
            i += 1
            while i < len(lines) and (lines[i].startswith('   ') or lines[i].startswith(' ')):
                c1_content += " " + lines[i].strip()
                i += 1
            new_lines.append(format_c1_line(c1_content))
            continue
        
        # 处理 C3 字段
        elif line.startswith('C3 '):
            c3_content = line
            i += 1
            while i < len(lines) and (lines[i].startswith('   ') or lines[i].startswith(' ')):
                c3_content += " " + lines[i].strip()
                i += 1
            new_lines.append(format_c3_line(c3_content))
            continue
        
        # 处理 RP 字段
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
    
    # 检查最后一行是否是 ER
    if not lines[-1].startswith('ER'):
        lines.append('ER')
    
    return '\n'.join(lines)

def validate_format(content):
    """
    验证文件格式是否符合标准
    """
    pt_j_count = len(re.findall(r'^PT J', content, re.MULTILINE))
    er_count = len(re.findall(r'^ER$', content, re.MULTILINE))
    
    lines = content.split('\n')
    pt_j_positions = [i for i, line in enumerate(lines) if line.startswith('PT J')]
    empty_before = 0
    issues = []
    
    for idx, pos in enumerate(pt_j_positions):
        if pos == 0:
            continue
        elif pos > 0 and lines[pos-1].strip() == '':
            empty_before += 1
        else:
            issues.append(f"第 {idx+1} 个 PT J (行 {pos+1}) 前面没有空行")
    
    is_valid = (pt_j_count == er_count and empty_before == len(pt_j_positions) - 1)
    
    return is_valid, pt_j_count, er_count, empty_before, len(pt_j_positions), issues

def process_wos_file(input_file, output_file, max_iterations=20, verbose=True):
    """处理 WOS 文件，循环直到所有记录格式正确"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        print(f"\n{'='*50}")
        print(f"第 {iteration} 轮处理")
        print(f"{'='*50}")
        
        is_valid, pt_j_count, er_count, empty_before, total_pt_j, issues = validate_format(content)
        
        print(f"当前状态:")
        print(f"  PT J 数量: {pt_j_count}")
        print(f"  ER 数量: {er_count}")
        print(f"  PT J 前有空行: {empty_before}/{total_pt_j - 1}")
        
        if is_valid:
            print(f"\n✓ 格式完全正确！")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return content
        
        print(f"\n格式不符合标准，开始处理...")
        
        parts = re.split(r'(?=^PT J)', content, flags=re.MULTILINE)
        
        fixed_records = []
        missing_au_count = 0
        
        for part in parts:
            if not part.strip():
                continue
            if not part.strip().startswith('PT J'):
                continue
            
            if 'AU ' not in part:
                missing_au_count += 1
            
            processed = process_record(part, verbose)
            if processed:
                fixed_records.append(processed)
        
        print(f"处理结果:")
        print(f"  记录总数: {len(fixed_records)}")
        print(f"  缺失 AU 的记录: {missing_au_count}")
        
        new_content = '\n\n'.join(fixed_records)
        
        is_valid_after, pt_j_after, er_after, empty_before_after, total_after, issues_after = validate_format(new_content)
        
        print(f"处理后状态:")
        print(f"  PT J 数量: {pt_j_after}")
        print(f"  ER 数量: {er_after}")
        print(f"  PT J 前有空行: {empty_before_after}/{total_after - 1}")
        
        if new_content == content and not is_valid_after:
            print(f"\n内容无变化，强制添加空行...")
            lines = new_content.split('\n')
            new_lines = []
            for line in lines:
                if line.startswith('PT J'):
                    if new_lines and new_lines[-1].strip() != '':
                        new_lines.append('')
                    new_lines.append(line)
                else:
                    new_lines.append(line)
            new_content = '\n'.join(new_lines)
        
        content = new_content
        
        if is_valid_after:
            print(f"\n✓ 处理完成！格式正确！")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return content
    
    print(f"\n⚠ 达到最大迭代次数 ({max_iterations})，强制写入当前结果")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    return content

def main():
    input_file = 'reformatted.txt'
    output_file = 'reformatted_fixed.txt'
    
    try:
        result = process_wos_file(input_file, output_file, max_iterations=20, verbose=True)
        
        # 最终验证
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            print("\n" + "="*50)
            print("最终验证")
            print("="*50)
            
            pt_j_count = len(re.findall(r'^PT J', content, re.MULTILINE))
            er_count = len(re.findall(r'^ER$', content, re.MULTILINE))
            print(f"PT J 数量: {pt_j_count}")
            print(f"ER 数量: {er_count}")
            
            if pt_j_count == er_count:
                print("✓ 每条记录都以 ER 结尾")
            else:
                print(f"⚠ PT J ({pt_j_count}) 与 ER ({er_count}) 数量不匹配")
            
            lines = content.split('\n')
            pt_j_lines = [i for i, line in enumerate(lines) if line.startswith('PT J')]
            empty_before = 0
            for line_num in pt_j_lines:
                if line_num > 0 and lines[line_num-1].strip() == '':
                    empty_before += 1
            
            print(f"PT J 前有空行的数量: {empty_before}/{len(pt_j_lines)}")
            
            if empty_before == len(pt_j_lines) - 1:
                print("✓ 所有 PT J 前面都有空行")
            
            # 显示 C1 和 C3 格式示例
            print("\n=== 字段格式示例 ===")
            
            # 查找 C1 字段
            c1_line = None
            for line in lines:
                if line.startswith('C1 '):
                    c1_line = line
                    break
            if c1_line:
                print(f"C1: {c1_line[:200]}...")
                # 检查 C1 中的作者格式
                if ';' in c1_line:
                    print("   ✓ C1 中作者用分号分隔")
                if ',' in c1_line:
                    print("   ✓ C1 中作者姓名用逗号分隔")
            
            # 查找 C3 字段
            c3_line = None
            for line in lines:
                if line.startswith('C3 '):
                    c3_line = line
                    break
            if c3_line:
                print(f"C3: {c3_line}")
                # C3 应该是机构名称，用分号分隔
                if ';' in c3_line:
                    print("   ✓ C3 中机构用分号分隔")
            
            # 查找 AU 字段示例
            au_lines = [line for line in lines if line.startswith('AU ')][:1]
            if au_lines:
                print(f"AU: {au_lines[0][:50]}")
                # AU 格式: "AU 姓, 名"
                if ',' in au_lines[0]:
                    print("   ✓ AU 中作者姓名用逗号分隔")
                
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}")
    except Exception as e:
        print(f"处理出错：{e}")

if __name__ == '__main__':
    main()
