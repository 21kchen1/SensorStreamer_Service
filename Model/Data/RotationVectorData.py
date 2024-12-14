from Model.Data.TypeData import TypeData
from Resource.String.DataString import DataString

"""
    RotationVector 数据结构
    @author chen
"""

class RotationVectorData(TypeData):
    # TYPE = "ROTATION_VECTOR"
    TYPE = DataString.TYPE_ROTATION_VECTOR
    VALUE_LEN = 5

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(RotationVectorData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.vectorX = values[0]
        self.vectorY = values[1]
        self.vectorZ = values[2]
        self.cosDelta = values[3]
        self.headingAccuracy = values[4]
