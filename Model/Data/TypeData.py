
"""
    通用数据结构
    @author chen
"""

class TypeData:
    """
        @param t_type 数据类型
        @param unixTimestamp 时间戳
    """
    def __init__(self, t_type: str, unixTimestamp: int) -> None:
        self.type = t_type
        self.unixTimestamp = unixTimestamp