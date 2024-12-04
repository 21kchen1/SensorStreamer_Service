import threading
from typing import Any

"""
    通用数据处理
    @author: chen
"""

class DataProcer:

    """
        初始化文件与锁
        @TypeData 对应数据类型的构造函数
    """
    def __init__(self, TypeData) -> None:
        self.lock = threading.Lock()
        self.TypeData = TypeData
        self.running = False

    """
        创建存储结构
        @param storagePath 存储父路径
        @param dataCode 数据编号
        @return 是否创建成功
    """
    def create(self, storagePath: str, dataCode: str) -> bool:
        pass


    """
        向存储结构添加数据，注意线程安全
        @param data 原始数据
    """
    def addData(self, data: dict) -> None:
        pass

    """
        返回存储结构路径，并结束存储
    """
    def getPath(self) -> str:
        pass