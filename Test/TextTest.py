from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

app = QApplication([])

# 创建QTextEdit控件
text_edit = QTextEdit()
text_edit.resize(600, 400)

# 设置等宽字体
font = QFont("Consolas", 10)  # Consolas 是一种常见的等宽字体
text_edit.setFont(font)

# 设置文本对齐方式为左对齐
text_edit.setAlignment(Qt.AlignLeft)

# 设置文本颜色为控制台常用的白色或亮色
text_edit.setStyleSheet("color: white;")

# 设置背景色为黑色，模拟控制台的背景
text_edit.setStyleSheet(text_edit.styleSheet() + "background-color: black;")

# 插入文本
text_edit.append("Streaming has not started...")

# 显示QTextEdit控件
text_edit.show()

# 启动应用程序
app.exec_()