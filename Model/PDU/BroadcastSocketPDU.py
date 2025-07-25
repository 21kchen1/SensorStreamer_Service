#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

r"""
@DATE    :   2025-07-12 12:15:31
@Author  :   Chen
@File    :   Model\PDU\BroadcastSocketPDU.py
@Software:   VSCode
@Description:
    嵌套字广播协议数据单元
"""

class BroadcastSocketPDU:
    """
    嵌套字广播协议数据单元
    """

    ATTR_IP = "IPAddress"
    ATTR_TCP_PORT = "tcpPort"
    ATTR_UDP_PORT = "udpPort"

    def __init__(self, IPAddress: str, tcpPort: int, udpPort: int) -> None:
        """
        初始化

        Args:
            IPAddress (str): 主机地址
            tcpPort (int): tcp 端口
            udpPort (int): udp 端口
        """
        self.IPAddress = IPAddress
        self.tcpPort = tcpPort
        self.udpPort = udpPort