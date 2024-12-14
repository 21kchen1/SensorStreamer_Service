from Model.Data.TypeData import TypeData
from Resource.String.DataString import DataString

"""
    Gyroscope 数据结构
    @author chen
"""

class GyroscopeData(TypeData):
    TYPE = DataString.TYPE_GYROSCOPE
    VALUE_LEN = 3

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(GyroscopeData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.angularSpeedX = values[0]
        self.angularSpeedY = values[1]
        self.angularSpeedZ = values[2]
