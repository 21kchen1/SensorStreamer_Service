from pymysql import Time
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.PictureData import PictureData
from Model.Data.RotationVectorData import RotationVectorData
from Model.Data.VideoData import VideoData
from Model.SQLModel.RecordItem import RecordItemBaseInfo
from View.View import View
from component.DataDeal.DataRecver import DataRecver
from PyQt5 import QtWidgets

from component.Time.TimeLine import TimeLine

"""
    DataDeal 控制器, 用于处理UI 与 DataDeal 之间的数据存储任务
    @author chen
"""

class DataSaveController:

    # 选择框与 data 的映射，键可能为不存在的变量，需要检查
    CHECK_DATA_DICT = {
        View.VIDEO_CHECK: VideoData.TYPE,
        View.PICTURE_CHECK: PictureData.TYPE,
        View.AUDIO_CHECK: AudioData.TYPE,
        View.ACCELEROMETER_CHECK: AccelerometerData.TYPE,
        View.GYROSCOPE_CHECK: GyroscopeData.TYPE,
        View.ROTATION_VECTOR_CHECK: RotationVectorData.TYPE,
        View.MAGNETIC_FIELD_CHECK: MagneticFieldData.TYPE
    }

    """
        @param view 视图
        @param dataRecver 数据处理器
    """
    def __init__(self, view: View, dataRecver: DataRecver) -> None:
        # 视图
        self.view = view
        # 接收器
        self.dataRecver = dataRecver
        # 数据编号
        self.dataCode = None
        # 数据基本信息
        self.dataBaseInfo = None
        # 设置槽函数
        self.setSlotFunc()

    """
        获取数据标签
    """
    def getDataCode(self) -> str:
        dataCode = ""
        for func in self.view.dataCodeList:
            dataCode += func() + "_"
        return dataCode[0 : -1]

    """
        获取存储路径
    """
    def getDataPath(self) -> str:
        return self.view.ui.dataPathLineEdit.text()

    """
        获取传感器设置
    """
    def getTypeSetting(self) -> list:
        # 获取选中
        typeList = []
        for (checkName, sensorType) in DataSaveController.CHECK_DATA_DICT.items():
            # 尝试获取按钮
            checkBox = getattr(self.view.ui, checkName, None)
            # 按钮不存在或没有选中
            if checkBox == None or not checkBox.isChecked():
                continue
            typeList.append(sensorType)
        return typeList

    """
        获取 dataCode 基本信息
    """
    def getBaseInfo(self) -> RecordItemBaseInfo:
        return RecordItemBaseInfo(
            recordName= self.getDataCode(),
            gender= self.view.getCodeGender(),
            exp= self.view.getCodeExp(),
            action= self.view.getCodeAction(),
            name= self.view.getCodeName(),
            time= int(self.view.getCodeTime()),
            other= self.view.getCodeOther()
        )

    """
        槽函数
    """

    # 检验当前的数据标签是否重复
    def checkDataCode(self) -> None:
        # 如果验证正确，则允许开始执行
        self.dataCode = self.getDataCode()
        if self.dataRecver.checkDataCode(self.dataCode):
            self.dataBaseInfo = self.getBaseInfo()
            self.view.ui.startStream.setEnabled(True)
            self.view.ui.stopStream.setEnabled(False)
            return
        # 如果验证错误，则弹出提示框
        self.dataCode = None
        self.dataBaseInfo = None
        self.view.ui.startStream.setEnabled(False)
        self.view.ui.stopStream.setEnabled(False)
        self.view.showDataCodeWarning()

    # 开始流式传输
    def startStream(self) -> None:
        self.dataRecver.startAccept(
            self.getTypeSetting(),
            self.getDataPath(),
            self.dataCode,
            TimeLine.getBaseTime()
        )
        # 停止校验功能
        self.view.ui.dataSetCheckButton.setEnabled(False)
        # 可以停止
        self.view.ui.startStream.setEnabled(False)
        self.view.ui.stopStream.setEnabled(True)

    # 停止流式传输
    def stopStream(self) -> None:
        self.dataRecver.stopAccept()
        # 询问是否保存
        result = self.view.showSaveData(self.dataCode)
        if result == QtWidgets.QMessageBox.Yes:
            self.dataRecver.saveData(self.dataBaseInfo)
        # 如果不保存则删除文件
        else:
            self.dataRecver.cancelSaveData()
        # 重置校验
        self.view.ui.startStream.setEnabled(False)
        self.view.ui.stopStream.setEnabled(False)
        self.view.ui.dataSetCheckButton.setEnabled(True)
        TimeLine.resetBaseTime()

    # 设置槽
    def setSlotFunc(self) -> None:
        # 设置开始和结束按钮的事件
        self.view.ui.startStream.clicked.connect(self.startStream)
        self.view.ui.stopStream.clicked.connect(self.stopStream)
        # 设置校验按钮事件
        self.view.ui.dataSetCheckButton.clicked.connect(self.checkDataCode)