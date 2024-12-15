from genericpath import isdir
import json
import logging
import os
import shutil
import threading
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AccelerometerUData import AccelerometerUData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.GyroscopeUData import GyroscopeUData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.MagneticFieldUData import MagneticFieldUData
from Model.Data.PictureData import PictureData
from Model.Data.RotationVectorData import RotationVectorData
from Model.Data.TypeData import TypeData
from Model.Data.VideoData import VideoData
from Model.SQLModel.RecordItem import RecordItem, RecordItemEnable
from Service.DataProcer.PictureProcer import PictureProcer
from Service.DataProcer.ListenProcer import ListenProcer
from Service.Link.UDPLink import UDPLink

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
    def __init__(self, udpLinks: list, bufSize: int, charset: str, stringTypeDataDict: dict) -> None:
        self.udpLinks = udpLinks
        self.charset = charset
        # 是否处理数据
        self.running = False

        self.stringTypeDataDict = stringTypeDataDict

        # 根据数据类型记录数量 自适应
        self.typeNumDict = {}

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
        @param timestamp 统一时间戳
    """
    def startAccept(self, typeSetting: list, storagePath: str, dataCode: str, timestamp: int) -> None:
        if not self.checkDataCode(dataCode):
            logging.warning(f"startAccept: DataCode duplicate")
            return
        self.timestamp = timestamp
        self.storagePath = f"{storagePath}/{dataCode}"
        # 重置选择的数据处理类
        for t_type in typeSetting:
            typeData = self.stringTypeDataDict.get(t_type)
            if typeData == None:
                continue
            typeData.DATA_PROCER.create(self.storagePath, dataCode, self.typeDataCount)
        # 重置字典
        self.typeNumDict = {}
        # 开始处理数据
        self.running = True

    """
        停止处理数据
    """
    def stopAccept(self) -> None:
        self.running = False

    """
        统计数据
        @param dataType 数据类型
    """
    def typeDataCount(self, dataType: str) -> None:
        # 添加数量
        if self.typeNumDict.get(dataType) == None:
            self.typeNumDict[dataType] = 0
        self.typeNumDict[dataType] += 1

    """
        获取路径并存储到数据库
        @param recordItem 数据模型
        @return 保存是否成功
    """
    def saveData(self, recordItem: RecordItemEnable) -> bool:
        try:
            # 关闭
            for typeData in self.stringTypeDataDict.values():
                typeData.DATA_PROCER.getPath()
            # 保存
            recordItem.setPathInfo(path= self.storagePath)
            RecordItemEnable.save(vars(recordItem))

            # 生成 note json
            with open(f"{ self.storagePath }/note.json", "w") as file:
                json.dump(vars(recordItem), file, indent= 4)
        except Exception as e:
            logging.error(f"saveData: {e}")
            return False

    """
        取消保存数据，删除生成的数据
        @return 是否删除成功
    """
    def cancelSaveData(self) -> bool:
        # 关闭
        for typeData in self.stringTypeDataDict.values():
            typeData.DATA_PROCER.getPath()
        try:
            if os.path.exists(self.storagePath):
                shutil.rmtree(self.storagePath)
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
            self.__acceptData(initData)

    """
        对 recvDataLoop 接收到的数据进行处理，并利用字典进行类型转换和时间戳化简
        @param initData 原始数据
    """
    def __acceptData(self, initData: bytes) -> None:
        try:
            initDataDict = json.loads(initData.decode(self.charset))
            """
                TypeData 是类
                typeData 是从字典里拿到的类
            """
            # 获取数据处理
            dataType = initDataDict.pop(TypeData.ATTR_TYPE, None)
            typeData = self.stringTypeDataDict.get(dataType)
            # 检查是否为有效类型
            if typeData == None:
                return

            # 检查数据是否存在时间戳
            if initDataDict.get(TypeData.ATTR_UNIX_TIMESTANP, None) == None:
                return
            initDataDict[TypeData.ATTR_UNIX_TIMESTANP] -= self.timestamp

            # 数据类型计数
            # self.typeDataCount(dataType)
            # 添加数据
            typeData.DATA_PROCER.addData(initDataDict)
        except Exception as e:
            logging.error(f"__acceptData: {e}")
