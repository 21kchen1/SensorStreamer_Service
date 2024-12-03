import logging
import threading

from Model.Data.SensorData import SensorData
from Model.Data.TypeData import TypeData
from component.DataDeal.DataProcer.DataProcer import DataProcer
import pandas as pd

"""
    Sensor 数据处理
    @author: chen
"""

class SensorProcer(DataProcer):

    def __init__(self) -> None:
        # 类型数据字典
        self.typeDataframeDict = {}
        # 数据锁
        self.typeLockDict = {}

    """
        将 sensor 类转换为更具体的类
        @return 返回处理后的数据
        @Override
    """
    def addData(self, initDataDict: dict) -> TypeData:
        try:
            # 解包生成类
            data = SensorData(**initDataDict)
            # 将 sensor 转换为具体类 unixTimestamp, sensorTimestamp, values
            classData = SensorData.TYPE_CLASS_DICT[data.sensorType](data.unixTimestamp, data.sensorTimestamp, data.values)
            dataDict = vars(classData)

            # 先检查是否存在锁
            if self.typeLockDict.get(classData.type) == None:
                self.typeLockDict[classData.type] = threading.Lock()

            # 获取锁之后才能对对应数据操作
            with self.typeLockDict[classData.type]:
                # 检查是否已经存在 dataframe
                if self.typeDataframeDict.get(classData.type) == None:
                    self.typeDataframeDict[classData.type] = pd.DataFrame([dataDict], index= False)
                else:
                    self.typeDataframeDict[classData.type] = self.typeDataframeDict[classData.type].append(dataDict, ignore_index= True)
            return classData
        except Exception as e:
            logging.warning(f"addData: {e}")

    """
        @Override
    """
    def getData(self) -> dict:
        return self.typeDataframeDict