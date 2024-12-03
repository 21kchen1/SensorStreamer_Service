from Model.Data.TypeData import TypeData

"""
    MagneticField 数据结构
    @author chen
"""

class MagneticFieldData(TypeData):
    TYPE = "MAGNETIC_FIELD"
    VALUE_LEN = 3

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(MagneticFieldData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.magneticFieldX = values[0]
        self.magneticFieldY = values[1]
        self.magneticFieldZ = values[2]
