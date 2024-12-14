import socket
from Component.Control.Control import Control

"""
    PhoneControl 手机控制器
    @author chen
"""

class PhoneControl(Control):
    def __init__(self, conn: socket, offCallback, charsets: str) -> None:
        super().__init__(conn, offCallback, charsets)