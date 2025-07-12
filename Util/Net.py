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
from typing import Union
import netifaces as ni

class WLANInfo:
    """
    局域网信息
    """
    def __init__(self, addr: str, netmask: str, network: str, broadcastAddr: str) -> None:
        """
        初始化

        Args:
            addr (str): 地址
            netmask (str): 子网掩码
            network (str): 网络号
            broadcastAddr (str): 子网广播地址
        """
        self.addr = addr
        self.netmask = netmask
        self.network  = network
        self.broadcastAddr = broadcastAddr

def getWLANInfo() -> Union[WLANInfo, None]:
    """
    获取局域网信息

    Returns:
        Union[WLANInfo, None]: 局域网信息
    """
    # 遍历网络接口
    for interface in ni.interfaces():
        # 判断是否为局域网
        print(ni.ifaddresses(interface))
        if not "wlan" in interface.lower() and not "wi-fi" in interface.lower():
            continue
        # 地址
        addrs = ni.ifaddresses(interface)
        # 是否包含 ipv4
        if not ni.AF_INET in addrs:
            continue
        addrInfo = addrs[ni.AF_INET][0]
        ip = addrInfo["addr"]
        netmask = addrInfo["netmask"]
        network = ipaddress.ip_network(f"{ip}/{netmask}", strict= False)
        return WLANInfo(ip, netmask, str(network), str(network.broadcast_address))
    return None
