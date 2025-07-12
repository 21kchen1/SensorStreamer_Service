#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

r"""
@DATE    :   2025-07-12 18:50:04
@Author  :   Chen
@File    :   Util\Net.py
@Software:   VSCode
@Description:
    网络相关的工具函数
"""

import ipaddress
import socket
from typing import Union
import netifaces as ni

class WLANInfo:
    """
    局域网信息
    """
    def __init__(self, ip: str, netmask: Union[str, None]= None, broadcastAddr: Union[str, None]= None) -> None:
        """
        初始化

        Args:
            ip (str): 地址
            netmask (Union[str, None]): 子网掩码
            broadcastAddr (Union[str, None]): 子网广播地址
        """
        self.ip = ip
        self.netmask = netmask
        self.broadcastAddr = broadcastAddr

def getWLANInfo() -> WLANInfo:
    """
    获取局域网信息

    Returns:
        WLANInfo: 局域网信息
    """

    # 使用 udp 获取当前局域网 ip
    tempSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 无效地址即可
    tempSocket.connect(("10.255.255.255", 1))
    # 获取地址
    localIP = tempSocket.getsockname()[0]
    tempSocket.close()

    # 获取子网掩码
    netmask = ""
    # 遍历网络接口
    for interface in ni.interfaces():
        addrs = ni.ifaddresses(interface)
        # 是否包含 ipv4 地址
        if not socket.AF_INET in addrs:
            continue
        # 遍历查看是否包含本地 ip
        for addr in addrs[ni.AF_INET]:
            if not addr["addr"] == localIP:
                continue
            netmask = addr["netmask"]
            break

    # 如果没找到掩码
    if netmask == "":
        return WLANInfo(localIP)

    # 生成广播地址
    network = ipaddress.ip_network(f"{ localIP }/{ netmask }", strict= False)
    return WLANInfo(localIP, netmask, str(network.broadcast_address))

if __name__ == "__main__":
    print(getWLANInfo().__dict__)