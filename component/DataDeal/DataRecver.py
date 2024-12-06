import json
import logging
import os
import threading
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.RotationVectorData import RotationVectorData
from Model.SQLModel.RecordItem import RecordItem, RecordItemBaseInfo
from component.DataDeal.DataProcer.SensorProcer import SensorProcer
from component.Link.UDPLink import UDPLink

"""
    利用 UDPLink 接收数据，并将数据处理与存储任务分配给 DataProcer
    @author chen
"""

class DataRecver:
    """
        @param udpLink
        @param bufSize 缓冲大小
        @param charset 编码
    """
    def __init__(self, udpLinks: list, bufSize: int, charset: str) -> None:
        self.udpLinks = udpLinks
        self.charset = charset
        # 是否处理数据
        self.running = False

        self.audioProcer = SensorProcer(AudioData)
        self.accelerometerProcer = SensorProcer(AccelerometerData)
        self.gyroscopeProcer = SensorProcer(GyroscopeData)
        self.magneticFieldProcer = SensorProcer(MagneticFieldData)
        self.rotationVectorProcer = SensorProcer(RotationVectorData)

        # 类型处理类字典
        self.typeProcerDict = {
            AudioData.TYPE: self.audioProcer,
            AccelerometerData.TYPE: self.accelerometerProcer,
            GyroscopeData.TYPE: self.gyroscopeProcer,
            MagneticFieldData.TYPE: self.magneticFieldProcer,
            RotationVectorData.TYPE: self.rotationVectorProcer
        }

        # 开启循环接收线程
        for udpLink in self.udpLinks:
            threading.Thread(target= self.__recvDataLoop, args= (udpLink, bufSize)).start()

    """
        从数据库中检查数据编号是否重复
        @param dataCode 数据编号
    """
    def checkDataCode(self, dataCode: str) -> bool:
        res = RecordItem.get_or_none(RecordItem.recordName == dataCode)
        if not res == None:
            return False
        return True

    """
        开始处理数据
        @param typeSetting 设置列表
        @param storagePath 存储路径
        @param dataCode 数据编号
    """
    def startAccept(self, typeSetting: list, storagePath: str, dataCode: str) -> None:
        if not self.checkDataCode(dataCode):
            logging.warning(f"startAccept: DataCode duplicate")
            return

        # 重置选择的数据处理类
        for t_type in typeSetting:
            procer = self.typeProcerDict.get(t_type)
            if procer == None:
                continue
            procer.create(storagePath, dataCode)

        # 开始处理数据
        self.running = True

    """
        停止处理数据
    """
    def stopAccept(self) -> None:
        self.running = False

    """
        获取路径并存储到数据库
        @param baseInfo
        @return 保存是否成功
    """
    def saveData(self, baseInfo: RecordItemBaseInfo) -> bool:
        try:
            recordItem = RecordItem.create(
                recordName = baseInfo.recordName,
                gender = baseInfo.gender,
                exp = baseInfo.exp,
                action = baseInfo.action,
                time = baseInfo.time,
                other = baseInfo.other,
                picturePath = None,
                videoPath = None,
                audioPath = self.audioProcer.getPath(),
                accelerometerPath = self.accelerometerProcer.getPath(),
                gyroscopePath = self.gyroscopeProcer.getPath(),
                rotationVectorPath = self.rotationVectorProcer.getPath(),
                magneticFieldPath = self.magneticFieldProcer.getPath(),
            )
            recordItem.save()
        except Exception as e:
            logging.error(f"saveData: {e}")
            return False

    """
        取消保存数据，删除生成的数据
        @return 是否删除成功
    """
    def cancelSaveData(self) -> bool:
        try:
            for procer in self.typeProcerDict.values():
                dataPath = procer.getPath()
                if dataPath == None:
                    continue
                # 检测是否存在文件
                if os.path.exists(dataPath):
                    os.remove(dataPath)
            return True
        except Exception as e:
            logging.error(f"cancelSaveData: {e}")
            return False

    """
        init 后开启的持续性接收线程, 只考虑接收数据
        @param updLink
        @param bufSize 缓冲大小
    """
    def __recvDataLoop(self, udpLink: UDPLink, bufSize: int) -> None:
        while True:
            initData, _ = udpLink.rece(bufSize)
            if not self.running:
                continue
            print(initData)
            self.__acceptData(initData)

    """
        对 recvDataLoop 接收到的数据进行处理，并利用字典进行类型转换和时间戳化简
        @param initData 原始数据
    """
    def __acceptData(self, initData: bytes) -> None:
        try:
            initDataDict = json.loads(initData.decode(self.charset))
            procer = self.typeProcerDict.get(initDataDict.pop("type", None))
            # 检查是否为有效类型
            if procer == None:
                return
            # 添加数据
            procer.addData(initDataDict)
        except Exception as e:
            logging.error(f"__acceptData: {e}")


