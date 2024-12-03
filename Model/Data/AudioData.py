from Model.Data.TypeData import TypeData


"""
    Audio 数据结构
    @author chen
"""

class AudioData(TypeData):
    TYPE = "AUDIO"

    """
        @param unixTimestamp 系统时间戳
        @param values 音频数据
    """
    def __init__(self, unixTimestamp: int, values: list) -> None:
        super().__init__(AudioData.TYPE, unixTimestamp)
        self.values = values