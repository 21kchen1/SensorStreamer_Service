import logging
import socket
import threading
import json

from Model.PDU.RLink_PDU import RLink_PDU
from component.Link.TCPMLinkListen import TCPMLinkListen

"""
    Control 通用控制类
    @author chen
"""
class Control:
    listenAddress = "0.0.0.0"
    REUSE_HEARTBEAT = "HeartBeat"
    HEARTBEAT = "heartbeat"

    """
        @param conn client socket
        @param off 回调函数
    """
    def __init__(self, conn: socket, offCallback) -> None:
        self.conn = conn
        self.offCallback = offCallback

        self.__running = True
        # 启动心跳线程
        self.heartBeatThread = threading.Thread(target= self.heartBeat, name= "HeartBeatThread")

    """
        处理客户端心跳信号
    """
    def heartBeat(self) -> None:
        while self.__running:
            try:
                data, _ = TCPMLinkListen.rece(self.conn)
                assert isinstance(data, bytes)
                data_dict = json.loads(data)
                # 需要是心跳信息
                if not data_dict[RLink_PDU.REUSE_NAME] == Control.REUSE_HEARTBEAT:
                    continue
                logging.info(f"Rece: {data}")
                reData = RLink_PDU(Control.REUSE_HEARTBEAT, Control.HEARTBEAT)
                assert TCPMLinkListen.send(self.conn, str(reData) + "\n", "utf-8")
                logging.info(f"Send: {reData}")
            except Exception as e:
                self.offLink()
                break

    """
        启动流式传输
        @param controlData 启动设备需要的控制信息
    """
    def startStream(self, controlData) -> None:
        pass

    """
        关闭流式传输
    """
    def stopStream(self) -> None:
        pass

    """
        关闭连接
    """
    def offLink(self) -> None:
        self.__running = False
        self.conn.close()
        # 激活回调函数
        self.offCallback()
        # 等待线程结束
        self.heartBeatThread.join()


