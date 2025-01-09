import PyPDF2
import pandas as pd


def read_pdf_and_save_to_table(file_path, output_file, file_format='csv'):
    # 打开 PDF 文件
    with open(file_path, 'rb') as pdf_file:
        # 创建 PDF 阅读器对象
        reader = PyPDF2.PdfReader(pdf_file)

        # 检查 PDF 是否有内容
        if len(reader.pages) > 0:
            # 获取第一页内容
            first_page = reader.pages[0]
            text = first_page.extract_text()

            # 将提取的内容保存到表格文件
            data = {'Page': [1], 'Content': [text]}  # 构建数据字典
            df = pd.DataFrame(data)  # 转换为 DataFrame

            if file_format == 'csv':
                df.to_csv(output_file, index=False, encoding='utf-8')
            elif file_format == 'excel':
                df.to_excel(output_file, index=False, encoding='utf-8', engine='openpyxl')
            else:
                print("不支持的文件格式！")

            print(f"内容已保存到 {output_file}")
        else:
            print("PDF 文件没有任何页面！")


# 示例调用
pdf_file_path = "四川1.pdf"  # PDF 文件路径
output_csv_path = "output.csv"  # 输出 CSV 文件路径
# output_excel_path = "output.xlsx"  # 输出 Excel 文件路径

# 保存为 CSV
read_pdf_and_save_to_table(pdf_file_path, output_csv_path, file_format='csv')

# 保存为 Excel
# read_pdf_and_save_to_table(pdf_file_path, output_excel_path, file_format='excel')
