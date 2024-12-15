from Model.Data.TypeData import TypeData
from Resource.String.DataString import DataString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    Accelerometer 数据结构
    @author chen
"""

class AccelerometerData(TypeData):
    TYPE = DataString.TYPE_ACCELEROMETER
    VALUE_LEN = 3

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(AccelerometerData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.Gx = values[0]
        self.Gy = values[1]
        self.Gz = values[2]

AccelerometerData.DATA_PROCER = ListenProcer(AccelerometerData)