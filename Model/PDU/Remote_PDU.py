
"""
    协议数据单元
"""

class Remote_PDU:
    REUSE_NAME = "RemoteSwitch"

    TYPE_CONTROL = "type_control"
    TYPE_SYN = "type_syn"
    TYPE_MSG = "type_msg"

    CONTROL_SWITCHON = "control_switchOn"
    CONTROL_SWITCHOFF = "control_switchOff"

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