from View.MainView import Ui_MainWidget
from PyQt5 import QtWidgets
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
        # 控制器
        self.watchControl = None
        self.phoneControl = None
        self.setConnect()

    """
        控制器函数
    """
    # 设置控制器
    def setWatchControl(self, watchControl: WatchControl):
        self.watchControl = watchControl
        self.ui.watchStatus.setText("On")

    def setPhoneControl(self, phoneControl: PhoneControl):
        self.phoneControl = phoneControl
        self.ui.phoneStatus.setText("On")

    # 取消控制器
    def cancelWatchControl(self):
        self.watchControl = None
        self.ui.watchStatus.setText("Off")

    def cancelPhoneControl(self):
        self.watchControl = None
        self.ui.phoneStatus.setText("Off")

    """
        槽函数
    """
    # 开始流式传输
    def startStream(self):
        if self.watchControl != None:
            self.watchControl.startStream()

        if self.phoneControl != None:
            self.phoneControl.startStream()

    # 停止流式传输
    def stopStream(self):
        if self.watchControl != None:
            self.watchControl.stopStream()

        if self.phoneControl != None:
            self.phoneControl.stopStream()

    # 设置槽
    def setConnect(self):
        # 设置开始和结束按钮的事件
        self.ui.startStream.clicked.connect(self.startStream)
        self.ui.stopStream.clicked.connect(self.stopStream)

    def run(self):
        self.mainWidget.show()
        sys.exit(self.app.exec_())
