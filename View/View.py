from Resource.String.ViewString import ViewString
from View.MainView import Ui_MainWidget
from PyQt5 import QtWidgets, QtCore
import sys

"""
    视图, 用于设置 UI
    @author chen
"""

class View:
    VIDEO_CHECK = ViewString.VIDEO_CHECK
    PICTURE_CHECK = ViewString.PICTURE_CHECK
    AUDIO_CHECK = ViewString.AUDIO_CHECK
    HEART_RATE_CHECK = ViewString.HEART_RATE_CHECK
    ACCELEROMETER_CHECK = ViewString.ACCELEROMETER_CHECK
    GYROSCOPE_CHECK = ViewString.GYROSCOPE_CHECK
    ROTATION_VECTOR_CHECK = ViewString.ROTATION_VECTOR_CHECK
    MAGNETIC_FIELD_CHECK = ViewString.MAGNETIC_FIELD_CHECK


    CHECK_LIST = [
        VIDEO_CHECK,
        PICTURE_CHECK,
        AUDIO_CHECK,
        HEART_RATE_CHECK,
        ACCELEROMETER_CHECK,
        GYROSCOPE_CHECK,
        ROTATION_VECTOR_CHECK,
        MAGNETIC_FIELD_CHECK,
    ]

    """
        常用的视图信息字符串
    """
    # 设备状态
    STATUS_ON = "ON"
    STATUS_OFF = "OFF"
    # 数据状态信息
    DATA_STATUS_INFO_STOP = "Streaming has not started..."

    """
        初始化 ui，并实现信息获取
        @param width 窗口宽度
        @param height 窗口高度
    """
    def __init__(self, width= 1500, height= 1000) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWidget = QtWidgets.QWidget()
        # 主界面
        self.ui = Ui_MainWidget()
        self.width = width
        self.height = height
        # 初始化
        self.uiInit()

        self.dataCodeList = [
            self.getCodeGender,
            self.getCodeExp,
            self.getCodeAction,
            self.getCodeName,
            self.getCodeTime,
            self.getCodeOther
        ]

    """
        重写关闭事件
    """
    def closeEvent(self, event) -> None:
        # 如果还在运行
        if self.ui.stopStream.isEnabled():
            self.ui.stopStream.click()
        self.app.quit()
        event.accept()

    def uiInit(self) -> None:
        # 大小设置
        self.ui.setupUi(self.mainWidget)
        self.mainWidget.resize(self.width, self.height)
        self.mainWidget.setMinimumSize(QtCore.QSize(self.width, self.height))
        # 设置关闭事件
        self.mainWidget.closeEvent = self.closeEvent

        # 设置按钮禁用
        self.ui.startStream.setEnabled(False)
        self.ui.stopStream.setEnabled(False)

    """
        数据存储路径警告
    """
    def showDataCodeWarning(self):
        return QtWidgets.QMessageBox.warning(
            self.mainWidget,
            "Data Code Warning",
            "Duplicate Data Code."
        )

    """
        数据存储校验警告
    """
    def showDataPathWarning(self):
        return QtWidgets.QMessageBox.warning(
            self.mainWidget,
            "Data Path Warning",
            "Exception Data Path."
        )

    """
        数据存储确认
    """
    def showSaveData(self, dataName: str):
        return QtWidgets.QMessageBox.question(
            self.mainWidget,
            f"Confirm Save",
            f"Confirm save {dataName}",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

    """
        组件设置
    """
    # 设置开始事件
    def setStartClicked(self, slot):
        self.ui.startStream.clicked.connect(slot)

    # 设置结束事件
    def setStopClicked(self, slot):
        self.ui.stopStream.clicked.connect(slot)

    # 设置检测事件
    def setDataSetCheckClicked(self, slot):
        self.ui.dataSetCheckButton.clicked.connect(slot)

    # 设置手表状态
    def setWatchStatus(self, status: str) -> None:
        self.ui.watchStatus.setText(status)

    # 设置手机
    def setPhoneStatus(self, status: str) -> None:
        self.ui.phoneStatus.setText(status)

    # 设置数据状态信息
    def setDataStatusInfo(self, info: str) -> None:
        self.ui.dataInfoText.setText(info)

    # 设置默认存储路径
    def setDefaultStoragePath(self, path: str) -> None:
        self.ui.dataPathLineEdit.setText(path)

    def getCodeGender(self) -> str:
        return self.ui.codeGenderComboBox.currentText()

    def getCodeExp(self) -> str:
        return self.ui.codeExpComboBox.currentText()

    def getCodeAction(self) -> str:
        return self.ui.codeActionComboBox.currentText()

    def getCodeName(self) -> str:
        return self.ui.codeNameEdit.text()

    def getCodeTime(self) -> str:
        return self.ui.codeTimeSpinBox.text()

    def getCodeOther(self) -> str:
        return self.ui.codeOtherLineEdit.text()

    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())