import sys
import logging
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
)

from backend.csv_to_excel import convert_csv_to_excel
from backend.pdf_to_csv import read_table_from_pdf_by_title


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF 表格处理工具")
        self.setGeometry(100, 100, 600, 300)
        self.init_ui()

    def init_ui(self):
        # 文件路径输入框
        self.file_path_label = QLabel("PDF 文件路径:", self)
        self.file_path_label.setGeometry(20, 30, 100, 30)
        self.file_path_input = QLineEdit(self)
        self.file_path_input.setGeometry(120, 30, 350, 30)
        self.file_path_input.setReadOnly(True)
        self.select_file_button = QPushButton("选择文件", self)
        self.select_file_button.setGeometry(480, 30, 80, 30)
        self.select_file_button.clicked.connect(self.select_pdf_file)

        # 标题输入框
        self.title_label = QLabel("输入目标标题关键词：", self)
        self.title_label.setGeometry(20, 80, 150, 30)
        self.title_input = QLineEdit(self)
        self.title_input.setGeometry(180, 80, 380, 30)
        self.title_input.setPlaceholderText("如：财务报表")

        # 开始转换按钮
        self.convert_button = QPushButton("开始转换", self)
        self.convert_button.setGeometry(240, 130, 100, 40)
        self.convert_button.clicked.connect(self.handle_conversion)

        # 转换结果显示框
        self.result_label = QLabel("处理结果:", self)
        self.result_label.setGeometry(20, 200, 80, 30)
        self.result_text = QLineEdit(self)
        self.result_text.setGeometry(110, 200, 450, 30)
        self.result_text.setReadOnly(True)

        # 状态反馈框
        # self.status_label = QLabel("", self)
        # self.status_label.setGeometry(20, 250, 400, 30)

    def select_pdf_file(self):
        """选择 PDF 文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "选择 PDF 文件", "", "PDF 文件 (*.pdf)")
        if file_path:
            self.file_path_input.setText(file_path)

    def validate_inputs(self):
        """验证用户输入"""
        file_path = self.file_path_input.text().strip()
        title = self.title_input.text().strip()

        if not file_path:
            QMessageBox.warning(self, "警告", "请先选择 PDF 文件！")
            return False

        if not title:
            QMessageBox.warning(self, "警告", "请输入目标标题关键词！")
            return False

        return True

    def handle_conversion(self):
        """处理转换逻辑"""
        if not self.validate_inputs():
            return

        file_path = self.file_path_input.text()
        title = self.title_input.text().strip()
        # output_csv_path = "output.csv"  # 输出文件路径

        try:
            # 调用后端函数 PDF->CSV->Excel
            output_csv_path = "output/output.csv"
            output_excel_path = "output/output.xlsx"

            read_table_from_pdf_by_title(file_path, output_csv_path, title)
            convert_csv_to_excel(output_csv_path, output_excel_path)

            QMessageBox.information(self, "成功", f"表格已成功提取并保存到 {output_excel_path}！")
            self.result_text.setText(f"表格已保存到 {output_excel_path}")
            # self.status_label.setText("转换成功！")
        except Exception as e:
            logging.error(f"转换失败：{e}")
            QMessageBox.critical(self, "错误", f"转换失败：{e}")
            self.status_label.setText("转换失败，请检查日志！")


if __name__ == "__main__":
    # 初始化日志
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
