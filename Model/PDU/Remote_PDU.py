
"""
    协议数据单元
    @author chen
"""

from Resource.String.NetString import NetString
from Resource.String.SwitchString import SwitchString


class Remote_PDU:
    REUSE_NAME = NetString.REUSE_NAME_REMOTE_SWITCH

    TYPE_CONTROL = SwitchString.TYPE_CONTROL
    TYPE_SYN = SwitchString.TYPE_SYN
    TYPE_MSG = SwitchString.TYPE_MSG

    CONTROL_SWITCH_ON = SwitchString.CONTROL_SWITCH_ON
    CONTROL_SWITCH_OFF = SwitchString.CONTROL_SWITCH_OFF

    """
        @param t_type 数据类型
        @param time 时间戳
        @param control 控制信息
        @param data 数据
    """
    def __init__(self, t_type: str, time: int, control: str, data: list) -> None:
        self.type = t_type
        self.time = time
        self.control = control
        self.data = data

    def __repr__(self) -> str:
        return f"Remote_PDU(type= {self.type}, time= {self.time}, control= {self.control}, data= {self.data})"