from Model.Data.TypeData import TypeData
from Resource.String.ModelString import DataString
from Service.DataProcer.VideoProcer import VideoProcer

"""
    Video 数据结构
    @author chen
"""

class VideoData(TypeData):
    TYPE = DataString.TYPE_VIDEO

    """
        @param unixTimestamp 系统时间戳
        @param width 视频宽度
        @param height 视频高度
        @param values 视频数据
    """
    def __init__(self, unixTimestamp: int, width: int, height: int, values: list) -> None:
        super().__init__(VideoData.TYPE, unixTimestamp)
        self.width = width
        self.height = height
        self.values = values

VideoData.DATA_PROCER = VideoProcer(VideoData)