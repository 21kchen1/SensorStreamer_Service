import logging
import socket
from Model.Control.AudioControl import AudioControl
from Model.Control.SensorControl import SensorControl
from Model.PDU.RLinkPDU import RLinkPDU
from Model.PDU.RemotePDU import RemotePDU
from Service.Control.Control import Control
from Service.Link.TCPMLinkListen import TCPMLinkListen

"""
    WatchControl 手表控制器
    @author chen
"""
class WatchControl(Control):

    def __init__(self, conn: socket, offCallback, charsets: str) -> None:
        super().__init__(conn, offCallback, charsets)
        # 传感器控制信息
        self.sensorControl = None
        # 音频控制信息
        self.audioControl = None

    """
        设置手表的传感器
        @param sampling 采样率
        @param sensors 列表
    """
    def setSensor(self, sensors: list, sampling = 0) -> None:
        checkSensors = []
        # 检查是否为有效传感器
        for sensor in sensors:
            if not sensor in SensorControl.TEST_LIST:
                continue
            checkSensors.append(sensor)

        self.sensorControl = vars(SensorControl(sampling, checkSensors))

    """
        设置手表的音频
        @param sampling 采样率
    """
    def setAudio(self, sampling = 16000) -> None:
        self.audioControl = vars(AudioControl(sampling))

    """
        @Override 重写，根据 set 设置控制信息
    """
    def startStream(self, timeStamp: int) -> None:
        try:
            # Switch 使用的 PDU
            remotePDU = vars(RemotePDU(RemotePDU.TYPE_CONTROL, timeStamp, RemotePDU.CONTROL_SWITCH_ON, [str(self.sensorControl), str(self.audioControl)]))
            # 发送启动命令
            rLinkPDU = vars(RLinkPDU(RemotePDU.REUSE_NAME, str(remotePDU)))
            TCPMLinkListen.send(self.conn, str(rLinkPDU) + "\n", self.charsets)
        except Exception as e:
            logging.error(f"startStream: {e}")
            self.offLink()