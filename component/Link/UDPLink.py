import socket
import threading
from component.Link.Link import Link

class UDPLink(Link):
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

    def send(self, data: str, encode: str) -> bool:

        try:
            with self.sendLock:
                self.sendSocket.sendto(data.encode(encode), (self.address, self.port))
        except Exception as e:
            print("UDPLink.send:", e)
            return False
        return True

    def rece(self, bufSize: int) -> tuple[str]:
        with self.receLock:
            data, address = self.receSocket.recvfrom(bufSize)
        return data, address
