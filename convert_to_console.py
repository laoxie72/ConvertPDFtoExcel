import PyPDF2


def read_pdf(file_path):
    # 打开 PDF 文件
    with open(file_path, 'rb') as pdf_file:
        # 创建 PDF 阅读器对象
        reader = PyPDF2.PdfReader(pdf_file)

        # 确保 PDF 至少有一页
        if len(reader.pages) > 0:
            # 获取第一页内容
            first_page = reader.pages[0]
            text = first_page.extract_text()

            # 输出内容
            print("PDF内容：")
            print(text)
        else:
            print("PDF 文件没有任何页面！")


# 示例调用
pdf_file_path = "四川1.pdf"  # 替换为你的 PDF 文件路径
read_pdf(pdf_file_path)
