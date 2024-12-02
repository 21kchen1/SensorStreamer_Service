
"""
    通用数据处理
    @author: chen
"""

class DataProcer:
    """
        @param storagePath 数据存储路径
        @param dataCode 数据编码，用于生成存储文件
    """
    def __init__(self, storagePath: str) -> None:
        self.storagePath = storagePath


    """
        初始化中间变量，并设置锁，保证中间变量线程安全
    """
    def initProc(self) -> None:
        pass

    """
        利用存储路径和数据编码
    """
    def saveData(self, dataCode: str) -> None:
        pass