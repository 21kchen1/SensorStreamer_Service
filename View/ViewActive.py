import time
from Model.Control.SensorControl import SensorControl
from View.MainView import Ui_MainWidget
from PyQt5 import QtWidgets, QtCore
import sys

from component.Control.PhoneControl import PhoneControl
from component.Control.WatchControl import WatchControl

"""
    界面活动, 用于处理UI产生的各种事件
"""

class ViewActive:
    ACCELEROMETER_CHECK = "accelerometerCheck"
    GYROSCOPE_CHECK = "gyroscopeCheck"
    ROTATION_VECTOR_CHECK = "rotationVectorCheck"
    MAGNETIC_FIELD_CHECK = "accelerometerCheck"

    # 选择框与 sensor 的映射，键可能为不存在的变量，需要检查
    CHECK_CONROL_DICT = {
        ACCELEROMETER_CHECK: SensorControl.SENSOR_ACCELEROMETER,
        GYROSCOPE_CHECK: SensorControl.SENSOR_GYROSCOPE,
        ROTATION_VECTOR_CHECK: SensorControl.SENSOR_ROTATION_VECTOR,
        MAGNETIC_FIELD_CHECK: SensorControl.SENSOR_MAGNETIC_FIELD
    }

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
        获取传感器设置
    """
    def getSensorSetting(self) -> list:
        sensorList = []
        for (checkName, sensorType) in ViewActive.CHECK_CONROL_DICT.items():
            # 尝试获取按钮
            checkBox = getattr(self.ui, checkName, None)
            # 按钮不存在或没有选中
            if checkBox == None or not checkBox.isChecked():
                continue
            sensorList.append(sensorType)
        return sensorList

    """
        获取音频设置
    """
    def getAudioSetting(self) -> int:
        if not self.ui.audioCheck.isChecked():
            return 0
        return self.ui.audioSpinBox.value()

    """
        槽函数
    """
    # 开始流式传输
    def startStream(self) -> None:
        self.ServiceTimeStamp = int(time.time() * 1000)

        if self.watchControl != None:
            # 设置音频采样率
            self.watchControl.setAudio(self.getAudioSetting())
            # 设置 Sensor 启动
            self.watchControl.setSensor(self.getSensorSetting())
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
