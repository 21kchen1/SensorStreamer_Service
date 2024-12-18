from Model.Control.TypeControl import TypeControl
from Resource.String.ModelString import DataString

"""
    Video 控制数据结构
    @author chen
"""

class VideoControl(TypeControl):
    TYPE = DataString.TYPE_VIDEO

    """
        @param sampling 采样率
    """
    def __init__(self, sampling: int) -> None:
        super().__init__(VideoControl.TYPE, sampling)