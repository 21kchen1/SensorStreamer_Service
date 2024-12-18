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
        self.running = False

    """
        创建存储结构
        @param storagePath 存储父路径
        @param dataCode 数据编号
        @param callback 回调函数
        @return 是否创建成功
    """
    def create(self, storagePath: str, dataCode: str, callback) -> bool:
        if self.running:
            return False
        self.running = True

    """
        加工结构化数据
        @param typeData 结构化数据
    """
    def _procData(self, typeData) -> bool:
        if not isinstance(typeData, self.TypeData):
            return False
        return True

    """
        向存储结构添加数据，注意线程安全
        @param data 原始数据
    """
    def addData(self, data: dict) -> None:
        if not self.running:
            return
        typeData = self.TypeData(**data)
        self._procData(typeData)
        pass

    """
        返回存储结构路径，并结束存储
    """
    def getPath(self) -> str:
        if not self.running:
            return None
        return ""