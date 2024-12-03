"""
    通用数据处理
    @author: chen
"""

import threading
from typing import Any

class DataProcer:

    """
        初始化数据集合与锁
    """
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.dataSet = None

    """
        重置数据集
    """
    def resetDataSet(self) -> None:
        pass

    """
        向数据集合添加数据，注意线程安全
        @param data 原始数据
    """
    def addData(self, data: dict) -> None:
        pass

    """
        返回数据集合
    """
    def getDataSet(self) -> Any:
        pass