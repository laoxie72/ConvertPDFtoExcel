import pandas as pd

def convert_csv_to_excel(csv_file_path, excel_file_path):
    """将 CSV 文件转换为 Excel 文件"""
    df = pd.read_csv(csv_file_path)
    df.to_excel(excel_file_path, index=False, engine='openpyxl')
