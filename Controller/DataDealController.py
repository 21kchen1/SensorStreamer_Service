from Model.Control.SensorControl import SensorControl
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.RotationVectorData import RotationVectorData
from Model.SQLModel.RecordItem import RecordItemBaseInfo
from View.View import View
from component.DataDeal.DataRecver import DataRecver

"""
    DataDeal 控制器, 用于处理UI 与 DataDeal 之间的任务
    @author chen
"""

class DataDealController:

    # 选择框与 data 的映射，键可能为不存在的变量，需要检查
    CHECK_DATA_DICT = {
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
        for (checkName, sensorType) in DataDealController.CHECK_DATA_DICT.items():
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
    def  getBaseInfo(self) -> RecordItemBaseInfo:
        return RecordItemBaseInfo(
            recordName= self.getDataCode()
            self.
        )

    """
        槽函数
    """
    # 开始流式传输
    def startStream(self) -> None:
        self.dataRecver.startAccept(self.getTypeSetting(), self.getDataPath(), self.getDataCode())

    # 停止流式传输
    def stopStream(self) -> None:
        self.dataRecver.stopAccept()

    # 保存数据
    def saveData(self) -> None:
        self.dataRecver.saveData()


    # 设置槽
    def setSlotFunc(self) -> None:
        # 设置开始和结束按钮的事件
        self.view.ui.startStream.clicked.connect(self.startStream)
        self.view.ui.stopStream.clicked.connect(self.stopStream)
