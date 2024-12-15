from Model.Data.TypeData import TypeData
from Resource.String.DataString import DataString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    Video 数据结构
    @author chen
"""

class VideoData(TypeData):
    TYPE = DataString.TYPE_VIDEO

    """
        @param unixTimestamp 系统时间戳
        @param values 视频数据
    """
    def __init__(self, unixTimestamp: int, values: list) -> None:
        super().__init__(VideoData.TYPE, unixTimestamp)
        self.values = values

VideoData.DATA_PROCER = ListenProcer(VideoData)