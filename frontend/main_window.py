import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
)
from backend.pdf_to_csv import read_table_from_pdf_and_save_to_csv
from backend.csv_to_excel import convert_csv_to_excel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF 表格处理工具")
        self.setGeometry(100, 100, 600, 300)

        # 文件路径输入框
        self.file_path_label = QLabel("PDF 文件路径:", self)
        self.file_path_label.setGeometry(20, 30, 100, 30)
        self.file_path_input = QLineEdit(self)
        self.file_path_input.setGeometry(120, 30, 350, 30)
        self.file_path_input.setReadOnly(True)
        self.select_file_button = QPushButton("选择文件", self)
        self.select_file_button.setGeometry(480, 30, 80, 30)
        self.select_file_button.clicked.connect(self.select_pdf_file)

        # 开始转换按钮
        self.convert_button = QPushButton("开始转换", self)
        self.convert_button.setGeometry(240, 80, 100, 40)
        self.convert_button.clicked.connect(self.start_conversion)

        # 转换结果显示框
        self.result_label = QLabel("处理结果:", self)
        self.result_label.setGeometry(20, 150, 80, 30)
        self.result_text = QLineEdit(self)
        self.result_text.setGeometry(110, 150, 350, 30)
        self.result_text.setReadOnly(True)

    def select_pdf_file(self):
        """选择 PDF 文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "选择 PDF 文件", "", "PDF 文件 (*.pdf)")
        if file_path:
            self.file_path_input.setText(file_path)

    def start_conversion(self):
        """开始处理文件"""
        file_path = self.file_path_input.text()
        if not file_path:
            QMessageBox.warning(self, "警告", "请先选择 PDF 文件！")
            return

        try:
            # PDF -> CSV -> Excel
            output_csv_path = "output/output.csv"
            output_excel_path = "output/output.xlsx"

            read_table_from_pdf_and_save_to_csv(file_path, output_csv_path)
            convert_csv_to_excel(output_csv_path, output_excel_path)

            self.result_text.setText(f"转换成功！文件已保存为 {output_excel_path}")
        except Exception as e:
            self.result_text.setText("转换失败！")
            QMessageBox.critical(self, "错误", f"处理过程中发生错误：\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
