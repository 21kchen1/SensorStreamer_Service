import logging
import socket
from Model.Control.VideoControl import VideoControl
from Model.PDU.RLinkPDU import RLinkPDU
from Model.PDU.RemotePDU import RemotePDU
from Service.Control.Control import Control
from Service.Link.TCPMLinkListen import TCPMLinkListen

"""
    PhoneControl 手机控制器
    @author chen
"""

class PhoneControl(Control):
    def __init__(self, conn: socket, offCallback, charsets: str) -> None:
        super().__init__(conn, offCallback, charsets)
        # 视频控制信息
        self.videoControl = None

    """
        设置手机的视频
    """
    def setVideo(self, sampling = 0) -> None:
        self.videoControl = vars(VideoControl(sampling))

    """
        @Override 重写，根据 set 设置控制信息
    """
    def startStream(self, timeStamp: int) -> None:
        try:
            # Switch 使用的 PDU
            remotePDU = vars(RemotePDU(RemotePDU.TYPE_CONTROL, timeStamp, RemotePDU.CONTROL_SWITCH_ON, [str(self.videoControl)]))
            # 发送启动命令
            rLinkPDU = vars(RLinkPDU(RemotePDU.REUSE_NAME, str(remotePDU)))
            TCPMLinkListen.send(self.conn, str(rLinkPDU) + "\n", self.charsets)
        except Exception as e:
            logging.error(f"startStream: {e}")
            self.offLink()