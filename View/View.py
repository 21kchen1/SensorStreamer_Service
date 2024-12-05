from View.MainView import Ui_MainWidget
from PyQt5 import QtWidgets, QtCore
import sys

"""
    视图, 用于设置 UI
    @author chen
"""

class View:
    VIDEO_CHECK = "videoCheck"
    AUDIO_CHECK = "audioCheck"
    HEART_RATE_CHECK = "heartRateCheck"
    ACCELEROMETER_CHECK = "accelerometerCheck"
    GYROSCOPE_CHECK = "gyroscopeCheck"
    ROTATION_VECTOR_CHECK = "rotationVectorCheck"
    MAGNETIC_FIELD_CHECK = "magneticFieldCheck"

    CHECK_LIST = [
        VIDEO_CHECK,
        AUDIO_CHECK,
        HEART_RATE_CHECK,
        ACCELEROMETER_CHECK,
        GYROSCOPE_CHECK,
        ROTATION_VECTOR_CHECK,
        MAGNETIC_FIELD_CHECK,
    ]

    """
        初始化 ui，并实现信息获取
        @param ui qt 产生的 ui 类
    """
    def __init__(self, ui: Ui_MainWidget) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWidget = QtWidgets.QWidget()
        self.ui = ui
        # 初始化
        self.ui.setupUi(self.mainWidget)
        self.mainWidget.resize(1500, 1000)
        self.mainWidget.setMinimumSize(QtCore.QSize(500, 500))

        self.dataCodeList = [
            self.getCodeGender,
            self.getCodeExp,
            self.getCodeAction,
            self.getCodeName,
            self.getCodeTime,
            self.getCodeOther
        ]

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
        return self.ui.codeOtherLineEdit()

    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())