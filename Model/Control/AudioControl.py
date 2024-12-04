from Model.Control.TypeControl import TypeControl

"""
    Audio 控制数据结构
    @author chen
"""

class AudioControl(TypeControl):
    TYPE = "AudioControl"

    """
        @param sampling 采样率
    """
    def __init__(self, sampling: int) -> None:
        super().__init__(AudioControl.TYPE, sampling)