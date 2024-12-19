import threading

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

        self.typeNum = 0
        self.running = False

    """
        创建存储结构
        @param storagePath 存储父路径
        @param dataCode 数据编号
        @param callback 回调函数
        @return 是否创建成功
    """
    def create(self, storagePath: str, dataCode: str) -> bool:
        if self.running:
            return False
        self.storagePath = storagePath
        self.dataCode = dataCode
        self.typeNum = 0
        return True

    """
        加工结构化数据
        @param typeData 结构化数据
    """
    def _procData(self, typeData) -> bool:
        if not isinstance(typeData, self.TypeData):
            return False
        return True

    """
        记录类型数据数量
    """
    def _addTypeNum(self) -> None:
        if not self.running:
            return
        self.typeNum = self.typeNum + 1

    """
        获取类型数据数量
    """
    def getTypeNum(self) -> int:
        if not self.running:
            return -1
        return self.typeNum

    """
        向存储结构添加数据，注意线程安全
        @param data 原始数据
    """
    def addData(self, data: dict) -> bool:
        if not self.running:
            return False
        return True

    """
        返回存储结构路径，并结束存储
    """
    def getPath(self) -> str:
        if not self.running:
            return None

        self.running = False
        self.typeNum = 0
        return ""