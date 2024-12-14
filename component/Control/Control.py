import logging
import socket
import threading
import json

from Model.PDU.RLink_PDU import RLink_PDU
from Model.PDU.Remote_PDU import Remote_PDU
from Component.Link.TCPMLinkListen import TCPMLinkListen

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
        @param charsets 编码
    """
    def __init__(self, conn: socket, offCallback, charsets: str) -> None:
        self.conn = conn
        self.offCallback = offCallback
        self.charsets = charsets

        self.running = True
        # 启动心跳线程
        self.heartBeatThread = threading.Thread(target= self.heartBeat, name= "HeartBeatThread")
        self.heartBeatThread.start()

    """
        处理客户端心跳信号
    """
    def heartBeat(self) -> None:
        while self.running:
            try:
                data, _ = TCPMLinkListen.rece(self.conn)
                assert isinstance(data, bytes)
                data_dict = json.loads(data)
                # 需要是心跳信息
                if not data_dict[RLink_PDU.REUSE_NAME] == Control.REUSE_HEARTBEAT:
                    continue
                logging.info(f"Rece: {data}")
                # 返回心跳
                reData = vars(RLink_PDU(Control.REUSE_HEARTBEAT, Control.HEARTBEAT))
                assert TCPMLinkListen.send(self.conn, str(reData) + "\n", self.charsets)
                logging.info(f"Send: {reData}")
            except Exception as e:
                logging.error(f"heartBeat: {e}")
                self.offLink()
                break

    """
        启动流式传输
        @param controlData 启动设备需要的控制信息
        @param timeStamp 服务器时间戳
    """
    def startStream(self, controlData: list, timeStamp: int) -> None:
        try:
            # Switch 使用的 PDU
            remotePDU = vars(Remote_PDU(Remote_PDU.TYPE_CONTROL, timeStamp, Remote_PDU.CONTROL_SWITCH_ON, controlData))
            # 发送启动命令
            rLinkPDU = vars(RLink_PDU(Remote_PDU.REUSE_NAME, str(remotePDU)))
            assert TCPMLinkListen.send(self.conn, str(rLinkPDU) + "\n", self.charsets)
        except Exception as e:
            logging.error(f"startStream: {e}")
            self.offLink()

    """
        关闭流式传输
        @param timeStamp 服务器时间戳
    """
    def stopStream(self, timeStamp: int) -> None:
        try:
            # Switch 使用的 PDU
            remotePDU = vars(Remote_PDU(Remote_PDU.TYPE_CONTROL, timeStamp, Remote_PDU.CONTROL_SWITCH_OFF, []))
            # 发送关闭命令
            rLinkPDU = vars(RLink_PDU(Remote_PDU.REUSE_NAME, str(remotePDU)))
            assert TCPMLinkListen.send(self.conn, str(rLinkPDU) + "\n", self.charsets)
        except Exception as e:
            logging.error(f"stopStream: {e}")
            self.offLink()

    """
        关闭连接
    """
    def offLink(self) -> None:
        self.running = False
        self.conn.close()
        # 激活回调函数
        if not self.offCallback == None:
            self.offCallback()


