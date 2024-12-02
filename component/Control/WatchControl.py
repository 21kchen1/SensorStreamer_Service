import logging
import socket
from Model.Control.AudioControl import AudioControl
from Model.Control.SensorControl import SensorControl
from Model.PDU.RLink_PDU import RLink_PDU
from Model.PDU.Remote_PDU import Remote_PDU
from component.Control.Control import Control
from component.Link.TCPMLinkListen import TCPMLinkListen

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
    def setSensor(self, sampling: int, sensors: list) -> None:
        checkSensors = []
        # 检查是否为有效传感器
        for sensor in sensors:
            if not sensor in SensorControl.TEST_LIST:
                continue
            self.checkSensors.append(sensor)

        self.sensorControl = SensorControl(sampling, checkSensors).__dict__

    """
        设置手表的音频
        @param sampling 采样率
    """
    def setAudio(self, sampling: int) -> None:
        self.audioControl = AudioControl(sampling).__dict__

    """
        @Override 重写，根据 set 设置控制信息
    """
    def startStream(self, timeStamp: int) -> None:
        try:
            # Switch 使用的 PDU
            remotePDU = Remote_PDU(Remote_PDU.TYPE_CONTROL, timeStamp, Remote_PDU.CONTROL_SWITCHON, [str(self.sensorControl), str(self.audioControl)]).__dict__
            # 发送启动命令
            rLinkPDU = RLink_PDU(Remote_PDU.REUSE_NAME, str(remotePDU)).__dict__
            assert TCPMLinkListen.send(self.conn, str(rLinkPDU) + "\n", self.charsets)

        except Exception as e:
            logging.error(f"startStream: {e}")
            self.offLink()