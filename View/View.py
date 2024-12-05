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

    """
        初始化 ui
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

    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())