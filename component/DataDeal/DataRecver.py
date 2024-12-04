import json
import logging
import threading
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.RotationVectorData import RotationVectorData
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

        # 类型处理类字典
        self.typeProcerDict = {
            AccelerometerData.TYPE: SensorProcer(AccelerometerData),
            GyroscopeData.TYPE: SensorProcer(GyroscopeData),
            MagneticFieldData.TYPE: SensorProcer(MagneticFieldData),
            RotationVectorData.TYPE: SensorProcer(RotationVectorData),
            AudioData.TYPE: SensorProcer(AudioData)
        }

        # 开启循环接收线程
        for udpLink in self.udpLinks:
            threading.Thread(target= self.__recvDataLoop, args= (udpLink, bufSize)).start()

    """
        从数据库中检查数据编号是否重复
        @param dataCode 数据编号
        @develop
    """
    def checkDataCode(self, dataCode: str) -> bool:
        return True

    """
        开始处理数据
        @param storagePath 存储路径
        @param dataCode 数据编号
        @param timeStamp 时间戳
    """
    def startAccept(self, storagePath: str, dataCode: str, timeStamp: int) -> None:
        if not self.checkDataCode(dataCode):
            logging.warning(f"startAccept: DataCode duplicate")
            return
        self.timeStamp = timeStamp
        # 重置数据处理类
        for procer in self.typeProcerDict.values():
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
        @return 保存是否成功
        @develop
    """
    def saveData(self) -> bool:
        # 一个dao，用于在数据库存储路径
        try:
            # 数据字典 type dataframe
            for (dataType, procer) in self.typeProcerDict.items():
                path = procer.getPath()
                print(path)
            return True
        except Exception as e:
            logging.error(f"saveData: {e}")
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
            initDataDict["unixTimestamp"] = initDataDict["unixTimestamp"] - self.timeStamp
            # 添加数据
            procer.addData(initDataDict)
        except Exception as e:
            logging.error(f"__acceptData: {e}")


