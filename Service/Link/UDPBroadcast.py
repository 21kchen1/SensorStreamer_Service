#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

r"""
@DATE    :   2025-07-12 11:42:47
@Author  :   Chen
@File    :   Service\Link\UDPBroadcast.py
@Software:   VSCode
@Description:
    UDP 广播
"""

import socket
import threading
import time
from Model.PDU.BroadcastSocketPDU import BroadcastSocketPDU
from Service.Link.TCPMLinkListen import TCPMLinkListen

class UDPBroadcast:
    """
    UDP 广播类，自带地址广播器
    """
    def __init__(self, port: int) -> None:
        """
        初始化

        Args:
            port (int): 广播端口
        """
        self.host = "255.255.255.255"
        self.port = port
        # 广播 socket
        self.socket = None
        # 用于终止线程的标志变量
        self._broadcasting = False

    def _running(self, message: str) -> None:
        """
        循环广播
        """
        try:
            while self._broadcasting and not self.socket is None:
                # 广播 utf-8 编码
                self.socket.sendto(message.encode(), (self.host, self.port))
                # 间隔 3 秒
                # print(message)
                time.sleep(3)
        finally:
            # 出现异常 直接停止
            self.stop()

    def start(self, message: str) -> None:
        """
        开始广播

        Args:
            message (str): 广播信息
        """
        # 如果已经广播
        if self._broadcasting == True:
            return

        # 获取广播 socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # 开始广播
        self._broadcasting = True
        # 开启循环线程
        threading.Thread(target= self._running, args= (message,)).start()

    def stop(self) -> None:
        """
        停止广播
        """
        # 停止循环
        self._broadcasting = False
        # 关闭 socket
        if self.socket:
            self.socket.close()

    def broadcastSocket(self, tcpPort: int, udpPort: int) -> None:
        """
        默认广播嵌套字

        Args:
            tcpPort (int): tcp 端口
            udpPort (int): udp 端口
        """
        # 获取本机 ip
        localIP = TCPMLinkListen.getWLANIP()
        message = str(BroadcastSocketPDU(localIP, tcpPort, udpPort).__dict__)
        # 开始广播
        self.start(message)