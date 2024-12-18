
"""
    通信数据单元
    @author chen
"""

class RLinkPDU:
    ATTR_REUSE_NAME = "reuseName"
    DATA = "data"
    """
        @param reuseName 复用名称
        @param data 数据
    """
    def __init__(self, reuseName: str, data: str) -> None:
        self.reuseName = reuseName
        self.data = data

    def __repr__(self) -> str:
        return f"RLinkPDU(reuseName= {self.reuseName}, data= {self.data})"