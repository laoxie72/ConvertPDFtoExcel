import pdfplumber
import pandas as pd


def read_table_from_pdf_by_title(file_path, output_csv_path, target_title):
    """
    从多页 PDF 中根据标题搜索并提取表格保存为 CSV 文件。

    :param file_path: PDF 文件路径
    :param output_csv_path: 输出 CSV 文件路径
    :param target_title: 搜索的标题关键词
    """
    with pdfplumber.open(file_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            # 提取页面文本
            text = page.extract_text()
            if target_title in text:  # 判断标题是否出现在该页
                print(f"找到标题 '{target_title}'，位于第 {page_number} 页。")

                # 提取表格
                table = page.extract_table()
                if table:
                    # 将表格转换为 DataFrame
                    df = pd.DataFrame(table[1:], columns=table[0])  # 使用第一行为列名

                    # 保存到 CSV 文件
                    df.to_csv(output_csv_path, index=False, encoding='utf-8')
                    print(f"表格内容已保存到文件：{output_csv_path}")
                    return

                else:
                    print(f"标题 '{target_title}' 所在页没有检测到表格内容！")
                    return

        print(f"未找到包含标题 '{target_title}' 的页面！")
