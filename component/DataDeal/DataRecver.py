import logging
import threading
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
        @param storagePath 数据存储路径
    """
    def __init__(self, udpLink: UDPLink, bufSize: int, storagePath: str) -> None:
        self.udpLink = udpLink
        self.storagePath = storagePath
        # 是否处理数据
        self.running = False
        # 数据处理类
        self.sensorProcer = None

        # 开启循环接收线程
        self.__receDataLoopThread = threading.Thread(target= self.__recvDataLoop, args= (bufSize))
        self.__receDataLoopThread.start()

    """
        检查数据编号是否重复
        @param dataCode 数据编号
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
        self.sensorProcer = SensorProcer()
        # 开始处理数据
        self.running = True

    """
        停止处理数据
    """
    def stopAccept(self) -> None:
        self.running = False

    """
        获取并存储各组数据
    """
    def saveData() -> None:
        pass

    """
        init 后开启的持续性接收线程, 只考虑接收数据
        @param bufSize 缓冲大小
    """
    def __recvDataLoop(self, bufSize: int) -> None:
        while True:
            initData, _ = self.udpLink.rece(bufSize)
            if not self.running:
                continue
            threading.Thread(target= self.__acceptData, args= (initData)).start()

    """
        对 recvDataLoop 接收到的数据进行处理，并利用字典进行类型转换和时间戳化简
        @param initData 原始数据
    """
    def __acceptData(self, initData: bytes) -> None:
        pass

