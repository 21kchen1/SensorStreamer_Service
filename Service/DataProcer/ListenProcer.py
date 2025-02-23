import csv
import logging
import os
from Model.Data.TypeData import TypeData
from Service.DataProcer.DataProcer import DataProcer
import pandas as pd

"""
    Sensor 数据处理
    @author: chen
"""

class ListenProcer(DataProcer):
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
        if not super().create(storagePath, dataCode):
            return False

        try:
            # 生成存储路径
            self.pathDirName = f"{self.storagePath}/{self.TypeData.TYPE}"
            fileName = f"{self.dataCode}_{self.TypeData.TYPE}.csv"
            self.pathFileName = f"{self.pathDirName}/{fileName}"
            # 检查是否已经存在文件
            self.fileExists = os.path.isfile(self.pathFileName)
            if self.fileExists:
                raise Exception("File already exists!")
            # 创建文件路径
            if not os.path.exists(self.pathDirName):
                os.makedirs(self.pathDirName)
            # 开启文件
            self.file = open(self.pathFileName, "w", newline= "")
            self.writer = csv.writer(self.file)
            # 记录缓存区的数据行数
            self.writerIndex = 0
        except Exception as e:
            logging.error(f"create: {e}")
            return False

        self.running = True
        return True

    """
        处理数据并向 csv 文件添加数据
    """
    def addData(self, data: dict) -> bool:
        if not super().addData(data):
            return False

        try:
            # 结构化数据
            typeData = self.TypeData(**data)
            self._procData(typeData)
            # 解包生成类字典转化为 df
            dataFrame = pd.DataFrame.from_dict([vars(typeData)])
            with self.lock:
                # 第一次添加，额外写入头部
                if not self.fileExists:
                    self.writer.writerow(dataFrame.columns.to_list())
                    self.fileExists = True
                self.writer.writerow(dataFrame.values.tolist()[0])
            self.writerIndex += 1
            # 记录数据
            self._addTypeNum()
            # 当缓存满，直接写入文件
            if self.writerIndex >= self.bufRowSize:
                self.file.flush()
                self.writerIndex = 0
            return True
        except Exception as e:
            logging.warning(f"addData: {e}")
            self.getPath()
            return False

    """
        关闭存储并返回 csv 文件路径
    """
    def getPath(self) -> str:
        if super().getPath() == None:
            return None
        # 关闭存储
        self.writer = None
        self.file.close()

        return self.pathFileName