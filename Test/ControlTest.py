import sys
sys.path.append("../")

import threading
from component.Control.WatchControl import WatchControl
from component.Link.TCPMLinkListen import TCPMLinkListen
from component.Link.UDPLink import UDPLink
import time
import socket
import logging

# 有服务器发送记录信息，再让客户端发送回来的时候带上自己的标识信息和服务端发送的记录信息
# 直接用端口来区分设备，先把单组做完再说

watchTCPPort = 5006
watchUDPPort = 5005

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)

dataDgram = UDPLink(watchUDPPort, "0.0.0.0")
# 处理数据接收
def dealData(conn: socket):
    while True:
        if getattr(conn, '_closed'):
            break
        data, address = dataDgram.rece(10240)
        print(f"Received message: {data} from {address}")

def dealControl(control: WatchControl):
    while control.running:
        try:
            ch = input("o or f")
            if ch == 'o':
                control.startStream()
            elif ch == 'f':
                control.stopStream()
        except Exception as e:
            control.offLink()
            break


def callback(conn: socket, addr):
    threading.Thread(target=dealData, args= {conn}).start()
    watchControl = WatchControl(conn, None, "utf-8")
    dealControl(watchControl)


b = TCPMLinkListen(watchTCPPort, "0.0.0.0", callback)
b.startListen()