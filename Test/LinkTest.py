import sys
sys.path.append("../")

from Resource.String.ModelString import PDUString
from Resource.String.ModelString import PDUString

import threading
from Service.Link.TCPMLinkListen import TCPMLinkListen
from Service.Link.UDPLink import UDPLink
import time
import socket
import logging

# 有服务器发送记录信息，再让客户端发送回来的时候带上自己的标识信息和服务端发送的记录信息
# 直接用端口来区分设备，先把单组做完再说

"""
    连接测试，测试底层连接协议，同时检查设备数据传输是否正常
    有效测试程序
    @version 1.0
    @author chen
"""

tcpPort = 5006
udpPort = 5005
HEARTBEAT = PDUString.VALUE_HEART_BEAT
# 远程开关
TYPE_CONTROL = PDUString.SWITCH_TYPE_CONTROL
CONTROL_SWITCHON = PDUString.SWITCH_CONTROL_SWITCH_ON
CONTROL_SWITCHOFF = PDUString.SWITCH_CONTROL_SWITCH_OFF
# 传感器
TYPE_ACCELEROMETER = 1
TYPE_GYROSCOPE = 4
TYPE_ROTATION_VECTOR = 11
TYPE_MAGNETIC_FIELD = 2

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)

RTCP_PDU = {
    "reuseName": None,
    "data": None
}

# 处理心跳
def dealHeartBeat(conn: socket):
    index = 1
    noneTime = 0
    while True:
        try:
            data, addr = TCPMLinkListen.rece(conn)
            if not data:
                print(1)
                # noneTime += 1
                # if noneTime > 100:
                #     break
                continue
            assert isinstance(data, bytes)
            print(f"recv data: {data.decode()} {index}")

            RTCP_PDU["reuseName"] = PDUString.REUSE_NAME_HEART_BEAT
            RTCP_PDU["data"] = HEARTBEAT
            assert TCPMLinkListen.send(conn, str(RTCP_PDU) + "\n", "utf-8")
            print(f"send data: {RTCP_PDU} {index}")
            index += 1
        except Exception as e:
            print(f"{e}")
            conn.close()
            break

dataDgram = UDPLink(udpPort, "0.0.0.0")
# 处理数据接收
def dealData(conn: socket):
    while True:
        if getattr(conn, '_closed'):
            print("ddadadadada")
            break
        data, address = dataDgram.rece(10240)
        print(f"Received message: {data} from {address}")

# 处理控制
def dealControl(conn: socket):
    controlOn = {
        "type": TYPE_CONTROL,
        "time": int(time.time() * 1000),
        "control": CONTROL_SWITCHON,
        "data": []
    }

    controlOff = {
        "type": TYPE_CONTROL,
        "time": int(time.time() * 1000),
        "control": CONTROL_SWITCHOFF,
        "data": []
    }

    while True:
        try:
            ch = input("On or Off")
            RTCP_PDU["reuseName"] = PDUString.REUSE_NAME_REMOTE_SWITCH
            if ch == 'On':
                RTCP_PDU["data"] = str(controlOn)
            elif ch == 'Off':
                RTCP_PDU["data"] = str(controlOff)

            assert TCPMLinkListen.send(conn, str(RTCP_PDU) + "\n", "utf-8")
            print(f"send data: {RTCP_PDU}")
        except Exception as e:
            conn.close()
            break


def callback(conn: socket, addr):
    threading.Thread(target=dealHeartBeat, args= {conn}).start()
    threading.Thread(target=dealData, args= {conn}).start()
    dealControl(conn)


b = TCPMLinkListen(tcpPort, "0.0.0.0", callback)
b.startListen()