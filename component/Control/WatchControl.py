import socket
from component.Control.Control import Control

"""
    WatchControl 手表控制器
    @author chen
    @deprecated
"""
class WatchControl(Control):
    def __init__(self, conn: socket, clientIP: str) -> None:
        super().__init__(conn, clientIP)

    def run(self):
        print(self.tcpPort)

