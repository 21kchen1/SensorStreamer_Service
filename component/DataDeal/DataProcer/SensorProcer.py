import csv
import logging
import os
from component.DataDeal.DataProcer.DataProcer import DataProcer
import pandas as pd

"""
    Sensor 数据处理
    @author: chen
"""

class SensorProcer(DataProcer):
    """
        @TypeData: 数据构造函数
        @bufRowSize: 缓冲区行数
    """
    def __init__(self, TypeData, bufRowSize= 500) -> None:
        super().__init__(TypeData)
        self.bufRowSize = bufRowSize
        # 存储的文件指针
        self.file = None
        self.writer = None

    """
        创建 csv 文件夹，并做对应的校验
    """
    def create(self, storagePath: str, dataCode: str) -> bool:
        if self.running:
            return False

        # 生成存储路径
        path = f"{storagePath}/{self.TypeData.TYPE}"
        fileName = f"{dataCode}_{self.TypeData.TYPE}.csv"
        self.pathFileName = f"{path}/{fileName}"
        # 检查是否已经存在文件
        self.fileExists = os.path.isfile(self.pathFileName)
        if self.fileExists:
            return False
        # 创建文件路径
        if not os.path.exists(path):
            os.makedirs(path)
        # 开启文件
        self.file = open(self.pathFileName, "w", newline= "")
        self.writer = csv.writer(self.file)
        # 记录缓存区的数据行数
        self.writerIndex = 0
        self.running = True

    """
        处理数据并向 csv 文件添加数据
    """
    def addData(self, data: dict) -> None:
        if not self.running:
            return
        try:
            # 解包生成类字典
            dataDict = [vars(self.TypeData(**data))]
            dataFrame = pd.DataFrame.from_dict(dataDict)
            with self.lock:
                # 第一次添加，额外写入头部
                if not self.fileExists:
                    self.writer.writerow(dataFrame.columns.to_list())
                    self.fileExists = True
                self.writer.writerow(dataFrame.values.tolist()[0])
            self.writerIndex += 1
            # 当缓存满，直接写入文件
            if self.writerIndex >= self.bufRowSize:
                self.file.flush()
                self.writerIndex = 0
        except Exception as e:
            logging.warning(f"addData: {e}")

    """
        关闭存储并返回 csv 文件路径
    """
    def getPath(self) -> str:
        if not self.running:
            return None
        # 关闭存储
        self.running = False
        self.writer = None
        self.file.close()

        return self.pathFileName