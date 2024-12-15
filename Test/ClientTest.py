import sys
sys.path.append("../")

from Resource.String.NetString import NetString
from Resource.String.SwitchString import SwitchString
import json
import socket
import time
from threading import Thread

"""
    客户端测试，测试客户端数据传输与控制效果
    有效测试程序
    @version 1.0
    @author chen
"""

def udp_server_recv(host, port):
    # 创建一个UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定socket到指定的主机和端口
    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
        # 接收数据和客户端地址
        data, address = server_socket.recvfrom(10240)  # 缓冲区大小设置为10240字节
        print(f"Received message: {data} from {address}")


def udp_server_send(host, port, data):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    jsonData = json.dumps(data)

    print(f"UDP server sending on {host}:{port}")

    try:
        while True:
            server_socket.sendto(jsonData.encode("utf-8"), (host, port))
            time.sleep(1)
    except socket.error as e:
        print(e)


# 发送 tcp 信息时，记得结尾要使用 \n
def tcp_server(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))

        RTCP_PDU["reuseName"] = NetString.REUSE_NAME_HEART_BEAT
        RTCP_PDU["data"] = HEARTBEAT
        jsonData = RTCP_PDU + "\n"

        while True:
            print(f"Server is listening on { host } : { port }")
            s.listen()

            conn, addr = s.accept()
            index = 1
            with conn:
                print(f"Connected by { addr }")
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(jsonData.encode("utf-8"))
                        print(f"Received data: {data.decode('utf-8')} ({ index })")
                        print(f"Message sent: {jsonData} ({ index })")
                        index += 1
                    except Exception as e:
                        print(e)
                        break


"""
    @param host 0.0.0.0 用于监听某个客户端发来的连接请求
    @param port 监听的端口，由服务端和客户端共同约定
"""
def tcp_control_test(host, port):
    control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_socket.bind((host, port))

    """
        @func 用于定时向客户端发送控制信息
    """
    def control(conn):
        index = 0
        while True:
            index = (index + 1) % 2
            if index == 1:
                data = {
                    "type": TYPE_CONTROL,
                    "time": int(time.time() * 1000),
                    "control": CONTROL_SWITCHON,
                    "data": [
                        str(SensorControl),
                        str(AudioControl)
                    ],
                }
            else:
                data = {
                    "type": TYPE_CONTROL,
                    "time": int(time.time() * 1000),
                    "control": CONTROL_SWITCHOFF,
                    "data": [
                    ],
                }
            try:
                RTCP_PDU["reuseName"] = "RemoteSwitch"
                RTCP_PDU["data"] = str(data)
                jsonData = json.dumps(RTCP_PDU) + "\n"
                conn.sendall(jsonData.encode("utf-8"))
                print(f"Messae sent: { jsonData }")
                time.sleep(3)
            except Exception as e:
                print(e)
                break

    """
        @func 用于接收并处理心跳信号
    """
    def heartbeat(conn):
        RTCP_PDU["reuseName"] = NetString.REUSE_NAME_HEART_BEAT
        RTCP_PDU["data"] = NetString.VALUE_HEART_BEAT
        recedata = str(RTCP_PDU) + "\n"
        index = 1
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received data: {data.decode('utf-8')} ({ index })")
                # time.sleep(3)
                conn.sendall(recedata.encode("utf-8"))
                print(f"Message sent: { recedata } ({ index })")
                index += 1
            except Exception as e:
                print(e)
                break

    while True:
        print(f"TCP server is listening on { host } : { port }")
        control_socket.listen()
        conn, addr = control_socket.accept()
        print(f"Connected by { addr }")

        controlThread = Thread(target= control, args= {conn})
        # controlThread = Thread(target= heartbeat, args= {conn})
        controlThread.start()
        heartbeat(conn)
        # control(conn)
        conn = None



# 设置服务器的主机地址和端口
recvHost = "0.0.0.0"  # 监听所有可用的接口+
udpPort = 5005  # UDP 端口
tcpPort = 5006  # TCP 端口

sendHost = "192.168.1.102"

TYPE_CONTROL = SwitchString.TYPE_CONTROL
TYPE_SYN = SwitchString.TYPE_SYN
CONTROL_SWITCHON = SwitchString.CONTROL_SWITCH_ON
CONTROL_SWITCHOFF = SwitchString.CONTROL_SWITCH_OFF
HEARTBEAT = NetString.VALUE_HEART_BEAT

data = {"type": TYPE_CONTROL, "time": 114514, "control": CONTROL_SWITCHON, "data": []}

TYPE_ACCELEROMETER = 1
TYPE_GYROSCOPE = 4
TYPE_ROTATION_VECTOR = 11
TYPE_MAGNETIC_FIELD = 2

RTCP_PDU = {
    "reuseName": None,
    "data": None
}

SensorControl = {
    "type": "SENSOR",
    "sampling": 0,
    "sensors": [
        TYPE_GYROSCOPE,
        TYPE_MAGNETIC_FIELD,
        TYPE_ROTATION_VECTOR,
        TYPE_MAGNETIC_FIELD
    ]
}

AudioControl = {
    "type": "AUDIO",
    "sampling": 16000
}

if __name__ == "__main__":
    # UDP接收数据
    a = Thread(target=udp_server_recv, args=(recvHost, udpPort))
    a.start()
    # UDP发送数据
    b = Thread(target=udp_server_send, args=(sendHost, udpPort, data))
    # b.start()
    # TCP接收数据
    c = Thread(target=tcp_server, args=(recvHost, tcpPort, data))
    # c.start()
    # TCP接发数据
    d = Thread(target=tcp_control_test, args=(recvHost, tcpPort))
    d.start()
