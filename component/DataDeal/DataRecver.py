import json
import logging
import threading
from Model.Data.AccelerometerData import AccelerometerData
from component.DataDeal.DataProcer.AccelerometerProcer import AccelerometerProcer
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
            AccelerometerData.TYPE: AccelerometerProcer()
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
        @param dataCode 数据编号
        @param timeStamp 时间戳
    """
    def startAccept(self, dataCode: str, timeStamp: int) -> None:
        if not self.checkDataCode(dataCode):
            logging.warning(f"startAccept: DataCode duplicate")
            return
        self.dataCode = dataCode
        self.timeStamp = timeStamp
        # 重置数据处理类
        for procer in self.typeProcerDict.values():
            procer.resetDataSet()

        # 开始处理数据
        self.running = True

    """
        停止处理数据
    """
    def stopAccept(self) -> None:
        self.running = False

    """
        获取并存储各组数据
        @param storagePath 数据存储路径
        @return 保存是否成功
        @develop
    """
    def saveData(self, storagePath: str) -> bool:
        # 一个dao，用于在数据库存储路径
        try:
            # 数据字典 type dataframe
            for (dataType, procer) in self.typeProcerDict.items():
                dataframe = procer.getDataSet()
                print(dataframe)
                dataframe.to_csv(f"{storagePath}/{dataType}/{self.dataCode}_{dataType}.csv", index= False)
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
            threading.Thread(target= self.__acceptData, args= (initData, )).start()

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


