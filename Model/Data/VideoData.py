from Model.Data.TypeData import TypeData
from Resource.String.DataString import DataString

"""
    Video 数据结构
    @author chen
"""

class VideoData(TypeData):
    # TYPE = "VIDEO"
    TYPE = DataString.TYPE_VIDEO

    """
        @param unixTimestamp 系统时间戳
        @param values 视频数据
    """
    def __init__(self, unixTimestamp: int, values: list) -> None:
        super().__init__(VideoData.TYPE, unixTimestamp)
        self.values = values