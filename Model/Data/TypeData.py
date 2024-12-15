
"""
    通用数据结构
    @author chen
"""

from Service.DataProcer.DataProcer import DataProcer

class TypeData:
    ATTR_UNIX_TIMESTANP = "unixTimestamp"
    ATTR_TYPE = "type"

    """
        与模型相绑定的服务
    """
    DATA_PROCER = None

    """
        @param t_type 数据类型
        @param unixTimestamp 时间戳
    """
    def __init__(self, t_type: str, unixTimestamp: int) -> None:
        self.type = t_type
        self.unixTimestamp = unixTimestamp

TypeData.DATA_PROCER = DataProcer(TypeData)