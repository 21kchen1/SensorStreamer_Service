"""
    Link 抽象类
    @author chen
"""
class Link:
    listenAddress = "0.0.0.0"

    """
        @param port 端口
        @param address 地址
    """
    def __init__(self, port: int, address: str) -> None:
        self.port = port
        self.address = address

    """
        @param data 数据
        @param encode 编码方式
        @return send 结果
    """
    def send(self, data: str, encode: str) -> bool:
        return False

    """
        @return rece 数据，地址
    """
    def rece(self, bufSize = 1024) -> tuple:
        return ()