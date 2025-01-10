import pdfplumber
import pandas as pd

def read_table_from_pdf_and_save_to_csv(file_path, output_csv_path):
    """从 PDF 提取表格并保存为 CSV 文件"""
    with pdfplumber.open(file_path) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])  # 使用第一行为列名
            df.to_csv(output_csv_path, index=False, encoding='utf-8')
        else:
            raise ValueError("未检测到表格内容")
