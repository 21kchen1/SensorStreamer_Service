from PyQt5 import QtWidgets

"""
    视图工具函数
"""
class ViewUtil:
    @staticmethod
    def createWidget(name: str, layout: QtWidgets.QLayout):
        widget = QtWidgets.QWidget()
        widget.setObjectName(name)
        widget.setLayout(layout)
        return widget, layout

    @staticmethod
    def createLabel(name: str, layout: QtWidgets.QLayout):
        label = QtWidgets.QLabel()
        label.setObjectName(name)
        label.setLayout(layout)
        return label ,layout

    @staticmethod
    def createButton(name: str, content: str):
        but = QtWidgets.QPushButton(content)
        but.setObjectName(name)
        return but