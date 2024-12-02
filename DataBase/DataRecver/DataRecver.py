
"""
    TCPLink 仅处理一个 TCP 连接。
    一个 TCPLink 对应一个 client socket
    @author chen
"""

from tkinter import N
from component.Link.UDPLink import UDPLink


class DataRecver:

    def __init__(self, udpLink: UDPLink) -> None:
        """_summary_

        Args:
            udpLink (UDPLink): _description_
        """
        self.udpLink = udpLink
        # 是否处理数据
        self.running = False

    """
        开始处理数据
    """
    def starAccept(self) -> None:
        self.running = True

    """
        停止处理数据
    """
    def stopAccept(self) -> None:
        self.running = False

    """
        init 后开启的持续性接收线程, 只考虑接收数据
    """
    def __recvDataLoop(self) -> None:
        pass

    """
        对 recvDataLoop 接收到的数据进行处理
    """
    def __acceptData(self) -> None:
        if not self.running:
            return

