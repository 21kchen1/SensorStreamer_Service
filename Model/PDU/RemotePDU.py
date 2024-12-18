from Resource.String.ModelString import PDUString

"""
    控制数据单元
    @author chen
"""

class RemotePDU:
    REUSE_NAME = PDUString.REUSE_NAME_REMOTE_SWITCH

    TYPE_CONTROL = PDUString.SWITCH_TYPE_CONTROL
    TYPE_SYN = PDUString.SWITCH_TYPE_SYN
    TYPE_MSG = PDUString.SWITCH_TYPE_MSG

    CONTROL_SWITCH_ON = PDUString.SWITCH_CONTROL_SWITCH_ON
    CONTROL_SWITCH_OFF = PDUString.SWITCH_CONTROL_SWITCH_OFF

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
        return f"RemotePDU(type= {self.type}, time= {self.time}, control= {self.control}, data= {self.data})"