import pdfplumber
import pandas as pd


def read_table_from_pdf_and_save_to_csv(file_path, output_csv_path):
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

            # 保存到 CSV 文件
            df.to_csv(output_csv_path, index=False, encoding='utf-8')
            print(f"表格内容已保存到文件：{output_csv_path}")
        else:
            print("没有检测到表格内容！")


def convert_csv_to_excel(csv_file_path, excel_file_path):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file_path)

    # 保存为 Excel 文件
    df.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f"CSV 文件已成功转换为 Excel 文件：{excel_file_path}")



# 调用
pdf_file_path = ""  # PDF 文件路径
output_csv_path = "output.csv"  # 输出 CSV 文件路径
# read_table_from_pdf_and_save_to_csv(pdf_file_path, output_csv_path)

csv_file_path = "output.csv"  # 输入的 CSV 文件路径
excel_file_path = "output.xlsx"  # 输出的 Excel 文件路径
convert_csv_to_excel(csv_file_path, excel_file_path)