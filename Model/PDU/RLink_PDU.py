
"""
    通信数据单元
    @author chen
"""
class RLink_PDU:
    REUSE_NAME = "reuseName"
    DATA = "data"
    """
        @param reuseName 复用名称
        @param data 数据
    """
    def __init__(self, reuseName: str, data: str) -> None:
        self.reuseName = reuseName
        self.data = data

    def __repr__(self) -> str:
        return f"RLink_PDU(reuseName= {self.reuseName}, data= {self.data})"