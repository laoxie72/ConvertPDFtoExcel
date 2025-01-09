import pdfplumber
import pandas as pd


def read_table_from_pdf(file_path):
    # 打开 PDF 文件
    with pdfplumber.open(file_path) as pdf:
        # 提取第一页的内容（假设表格在第一页）
        page = pdf.pages[0]

        # 使用 extract_table 提取表格内容
        table = page.extract_table()

        # 检查是否成功提取表格
        if table:
            # 将表格转换为 DataFrame
            df = pd.DataFrame(table[1:], columns=table[0])  # 使用第一行为列名

            # 在控制台以表格形式输出
            print("提取到的表格内容：")
            print(df.to_string(index=False))
        else:
            print("没有检测到表格内容！")


# 示例调用
pdf_file_path = "四川1.pdf"  # 替换为你的 PDF 文件路径
read_table_from_pdf(pdf_file_path)
