
"""
    通用数据结构
    @author chen
"""

class TypeData:
    ATTR_UNIX_TIMESTANP = "unixTimestamp"
    ATTR_TYPE = "type"

    """
        @param t_type 数据类型
        @param unixTimestamp 时间戳
    """
    def __init__(self, t_type: str, unixTimestamp: int) -> None:
        self.type = t_type
        self.unixTimestamp = unixTimestamp