# 导入需要的模块
import codecs
import os

# 定义一个函数，接受一个字符串参数
def add_suffix_files(dir):
    # 遍历当前目录及其子目录下的所有文件
    for root, dirs, files in os.walk(dir):
        # 遍历所有文件名
        for file in files:
            # 获取完整的文件路径
            old_name = os.path.join(root, file)
            # 判断是否是 .md 文件，并且文件名长度小于 20
            name, ext = os.path.splitext(old_name)
            absName, ext = os.path.splitext(file)
            if ext == ".md" and len(absName) < 20:
                # 用 codecs 模块打开文件，指定编码为 utf-8
                input_md = codecs.open(old_name, mode="r", encoding="utf-8")
                # 读取文件内容，存储为字符串
                md_str = input_md.read()
                # 关闭文件
                input_md.close()
                # 将字符串按换行符分割为列表
                md_list = md_str.split("\n")
                # 遍历列表，找到第一个以 Question: 开头的元素
                for line in md_list:
                    if line.startswith('The following is a search input in a search engine, giving useful content or solutions and as much information as you can related to it, use markdown syntax to make your answer more readable, such as code blocks, bold, list:') or \
                        line.startswith('Reply in Chinese (Simplified).Analyze the following content and express your opinion,or give your answer:') or \
                        line.startswith('The following is the text content of a web page,analyze the core content and summarize:') or \
                        line.startswith('Reply in Chinese (Simplified).Summarize the following as concisely as possible:') or \
                        line.startswith('Reply in Chinese (Simplified).'):
                        # 获取 Question: 后面的一行文字，去掉两端的空格
                        question = md_list[md_list.index(line) + 1].strip()
                        # 打印问题
                        print(question)
                        print(len(question))
                        if len(question) > 40:
                            break
                        # 在文件名末尾添加字符串
                        new_name = name + question + ext
                        # 重命名文件
                        os.rename(old_name, new_name)
                        # 打印提示信息
                        print(old_name, "has been renamed to", new_name)
                        break

# 调用函数，传入当前目录作为参数
add_suffix_files(".")
