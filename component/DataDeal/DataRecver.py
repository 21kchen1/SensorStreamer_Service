from genericpath import isdir
import json
import logging
import os
import shutil
import threading
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.PictureData import PictureData
from Model.Data.RotationVectorData import RotationVectorData
from Model.Data.TypeData import TypeData
from Model.Data.VideoData import VideoData
from Model.SQLModel.RecordItem import RecordItem, RecordItemEnable
from component.DataDeal.DataProcer.PictureProcer import PictureProcer
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

        # 由于音频和视频的数据存储特别，先使用此类处理，后续收集到数据后再做处理
        self.videoProcer = SensorProcer(VideoData)
        self.audioProcer = SensorProcer(AudioData)
        # 图片需要专门的处理
        self.pictureProcer = PictureProcer(self.typeDataCount)
        # 传感器数据处理
        self.accelerometerProcer = SensorProcer(AccelerometerData)
        self.gyroscopeProcer = SensorProcer(GyroscopeData)
        self.magneticFieldProcer = SensorProcer(MagneticFieldData)
        self.rotationVectorProcer = SensorProcer(RotationVectorData)

        # 根据数据类型选择数据处理
        self.typeProcerDict = {
            VideoData.TYPE: self.videoProcer,
            PictureData.TYPE: self.pictureProcer,
            AudioData.TYPE: self.audioProcer,
            AccelerometerData.TYPE: self.accelerometerProcer,
            GyroscopeData.TYPE: self.gyroscopeProcer,
            MagneticFieldData.TYPE: self.magneticFieldProcer,
            RotationVectorData.TYPE: self.rotationVectorProcer
        }

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
            procer = self.typeProcerDict.get(t_type)
            if procer == None:
                continue
            procer.create(self.storagePath, dataCode)
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
        获取路径并存储到数据库
        @param recordItem 数据模型
        @return 保存是否成功
    """
    def saveData(self, recordItem: RecordItemEnable) -> bool:
        try:
            recordItem.setPathInfo(
                picturePath = self.pictureProcer.getPath(),
                videoPath = self.videoProcer.getPath(),
                audioPath = self.audioProcer.getPath(),
                accelerometerPath = self.accelerometerProcer.getPath(),
                gyroscopePath = self.gyroscopeProcer.getPath(),
                rotationVectorPath = self.rotationVectorProcer.getPath(),
                magneticFieldPath = self.magneticFieldProcer.getPath(),
            )
            RecordItemEnable.save(vars(recordItem))
            # recordItem = RecordItem.create(**vars(baseInfo))
            # recordItem.save()
        except Exception as e:
            logging.error(f"saveData: {e}")
            return False

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
        取消保存数据，删除生成的数据
        @return 是否删除成功
    """
    def cancelSaveData(self) -> bool:
        # 关闭
        for procer in self.typeProcerDict.values():
            procer.getPath()
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

            # 获取数据处理
            dataType = initDataDict.pop(TypeData.ATTR_TYPE, None)
            procer = self.typeProcerDict.get(dataType)
            # 检查是否为有效类型
            if procer == None:
                return

            # 检查数据是否存在时间戳
            if initDataDict.get(TypeData.ATTR_UNIX_TIMESTANP, None) == None:
                return
            initDataDict[TypeData.ATTR_UNIX_TIMESTANP] -= self.timestamp

            # 数据类型计数
            self.typeDataCount(dataType)
            # 添加数据
            procer.addData(initDataDict)
        except Exception as e:
            logging.error(f"__acceptData: {e}")
