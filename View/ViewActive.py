import time
from View.MainView import Ui_MainWidget
from PyQt5 import QtWidgets, QtCore
import sys

from component.Control.PhoneControl import PhoneControl
from component.Control.WatchControl import WatchControl

"""
    界面活动, 用于处理UI产生的各种事件
"""

class ViewActive:
    def __init__(self, ui: Ui_MainWidget) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWidget = QtWidgets.QWidget()
        self.ui = ui
        # 初始化
        self.ui.setupUi(self.mainWidget)
        self.mainWidget.resize(1000, 1000)
        self.mainWidget.setMinimumSize(QtCore.QSize(1000, 1000))
        # 控制器
        self.watchControl = None
        self.phoneControl = None
        self.setConnect()

    """
        控制器函数
    """
    # 设置控制器
    def setWatchControl(self, watchControl: WatchControl) -> None:
        self.watchControl = watchControl
        self.ui.watchStatus.setText("On")

    def setPhoneControl(self, phoneControl: PhoneControl) -> None:
        self.phoneControl = phoneControl
        self.ui.phoneStatus.setText("On")

    # 取消控制器
    def cancelWatchControl(self) -> None:
        self.watchControl = None
        self.ui.watchStatus.setText("Off")

    def cancelPhoneControl(self) -> None:
        self.watchControl = None
        self.ui.phoneStatus.setText("Off")

    """
        获取数据标签
    """
    def getDataCode(self) -> str:
        # 性别
        codeGender = self.ui.codeGenderBox.currentText()
        # 命名
        codeName = self.ui.codeNameEdit.text()
        # 次数
        codeNum = self.ui.codeNumSpinBox.text()
        return codeGender + "_" + codeName + "_" + codeNum

    """
        槽函数
    """
    # 开始流式传输
    def startStream(self) -> None:
        self.ServiceTimeStamp = int(time.time() * 1000)

        if self.watchControl != None:
            self.watchControl.startStream(self.ServiceTimeStamp)

        if self.phoneControl != None:
            self.phoneControl.startStream(None, self.ServiceTimeStamp)

    # 停止流式传输
    def stopStream(self) -> None:
        if self.watchControl != None:
            self.watchControl.stopStream(0)

        if self.phoneControl != None:
            self.phoneControl.stopStream(0)

    # 设置槽
    def setConnect(self) -> None:
        # 设置开始和结束按钮的事件
        self.ui.startStream.clicked.connect(self.startStream)
        self.ui.stopStream.clicked.connect(self.stopStream)

    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())
