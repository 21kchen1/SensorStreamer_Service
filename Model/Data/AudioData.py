from Model.Data.TypeData import TypeData
from Resource.String.ModelString import DataString
from Service.DataProcer.ListenProcer import ListenProcer


"""
    Audio 数据结构
    @author chen
"""

class AudioData(TypeData):
    TYPE = DataString.TYPE_AUDIO

    """
        @param unixTimestamp 系统时间戳
        @param samplingRate 采样率
        @param values 音频数据
    """
    def __init__(self, unixTimestamp: int, samplingRate: int, values: list) -> None:
        super().__init__(AudioData.TYPE, unixTimestamp)
        self.samplingRate = samplingRate
        self.values = values

AudioData.DATA_PROCER = ListenProcer(AudioData)