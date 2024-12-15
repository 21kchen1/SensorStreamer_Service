import socket
import threading
import logging
from Service.Link.Link import Link

"""
    UDPLink 用于传输数据,。
    建议一个设备单独分配一个 UDPLink, 防止缓冲区不足
    @author chen
"""
class UDPLink(Link):
    LOG_TAG = "TCPLink"

    """
        @param port 端口
        @param address 地址，数据接收校准，数据发送目标
    """
    def __init__(self, port: int, address: str) -> None:
        super().__init__(port, address)

        # 设置接收 socket
        self.receSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receSocket.bind((super().listenAddress, self.port))
        # 线程锁
        self.receLock = threading.Lock()

        # 设置发送 socket
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendLock = threading.Lock()

    """
        @param data 数据
        @param encode 编码方式
        @return 发送成功
    """
    def send(self, data: str, encode: str) -> bool:
        try:
            with self.sendLock:
                self.sendSocket.sendto(data.encode(encode), (self.address, self.port))
            return True
        except Exception as e:
            logging.warning(str(e))
            return False

    """
        @param bufSize 设置缓冲大小
        @return 返回数据与客户端地址
    """
    def rece(self, bufSize = 1024) -> tuple:
        try:
            with self.receLock:
                data, address = self.receSocket.recvfrom(bufSize)
            return data, address
        except Exception as e:
            logging.warning(str(e))
            return None
