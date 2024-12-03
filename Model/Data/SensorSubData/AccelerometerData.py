from Model.Data.TypeData import TypeData

"""
    Accelerometer 数据结构
    @author chen
"""

class AccelerometerData(TypeData):
    TYPE = "ACCELEROMETER"
    VALUE_LEN = 3

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(AccelerometerData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.Gx = values[0]
        self.Gy = values[1]
        self.Gz = values[2]