from socket import socket
from Model.Control.SensorControl import SensorControl
from Component.Sound.Sound import Sound
from View.View import View
from Service.Control.PhoneControl import PhoneControl
from Service.Control.WatchControl import WatchControl
from Component.Time.TimeLine import TimeLine

"""
    Control 控制器, 用于处理 UI 和 Control 之间的任务
    @author chen
"""

class ControlController:
    # 选择框与 control 的映射，键可能为不存在的变量，需要检查
    CHECK_CONROL_DICT = {
        View.ACCELEROMETER_CHECK: SensorControl.SENSOR_ACCELEROMETER,
        View.GYROSCOPE_CHECK: SensorControl.SENSOR_GYROSCOPE,
        View.ROTATION_VECTOR_CHECK: SensorControl.SENSOR_ROTATION_VECTOR,
        View.MAGNETIC_FIELD_CHECK: SensorControl.SENSOR_MAGNETIC_FIELD
    }

    """
        @param view 视图
        @param charset 编码集
    """
    def __init__(self, view: View, charset: str) -> None:
        # 视图
        self.view = view
        # 编码
        self.charset = charset
        # 控制器
        self.watchControl = None
        self.phoneControl = None
        # 设置槽函数
        self.setSlotFunc()

    """
        控制器函数
    """
    # 设置控制器
    def setWatchControl(self, conn: socket, address) -> None:
        self.watchControl = WatchControl(conn, self.cancelWatchControl, self.charset)
        self.view.setWatchStatus(f"{ View.STATUS_ON } | { address }")

    def setPhoneControl(self, conn: socket, address) -> None:
        self.phoneControl = PhoneControl(conn, self.cancelPhoneControl, self.charset)
        self.view.setPhoneStatus(f"{ View.STATUS_ON } | { address }")

    # 取消控制器
    def cancelWatchControl(self) -> None:
        # 提示退出
        Sound.MessageBeep()
        self.watchControl = None
        self.view.setWatchStatus(View.STATUS_OFF)

    def cancelPhoneControl(self) -> None:
        # 提示退出
        Sound.MessageBeep()
        self.PhoneControl = None
        self.view.setPhoneStatus(View.STATUS_OFF)

    """
        获取传感器设置
    """
    def getSensorSetting(self) -> list:
        # 获取选中
        sensorList = []
        for (checkName, sensorType) in ControlController.CHECK_CONROL_DICT.items():
            # 尝试获取按钮
            checkBox = getattr(self.view.ui, checkName, None)
            # 按钮不存在或没有选中
            if checkBox == None or not checkBox.isChecked():
                continue
            sensorList.append(sensorType)
        return sensorList

    """
        获取音频设置
    """
    def getAudioSetting(self) -> int:
        if not self.view.ui.audioCheck.isChecked():
            return 0
        return self.view.ui.audioSpinBox.value()

    """
        获取视频设置
    """
    def getVideoSetting(self) -> int:
        if not self.view.ui.videoCheck.isChecked():
            return 0
        return 1

    """
        槽函数
    """
    # 开始流式传输
    def startStream(self) -> None:
        serviceTimeStamp = TimeLine.getBaseTime()

        if self.watchControl != None:
            # 设置音频采样率
            self.watchControl.setAudio(self.getAudioSetting())
            # 设置 Sensor 启动
            self.watchControl.setSensor(self.getSensorSetting())
            self.watchControl.startStream(serviceTimeStamp)

        if self.phoneControl != None:
            self.phoneControl.setVideo(self.getVideoSetting())
            self.phoneControl.startStream(serviceTimeStamp)

    # 停止流式传输
    def stopStream(self) -> None:
        serviceTimeStamp = TimeLine.getSystemTime()

        if self.watchControl != None:
            self.watchControl.stopStream(serviceTimeStamp)

        if self.phoneControl != None:
            self.phoneControl.stopStream(serviceTimeStamp)

    # 设置槽函数
    def setSlotFunc(self) -> None:
        # 设置开始和结束按钮的事件
        self.view.setStartClicked(self.startStream)
        self.view.setStopClicked(self.stopStream)