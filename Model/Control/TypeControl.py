
"""
    通用控制数据结构
    @author chen
"""

class TypeControl:

    """
        @param t_type 传感器类型
        @param sampling 采样率
    """
    def __init__(self, t_type: str, sampling: int) -> None:
        self.type = t_type
        self.sampling = sampling
