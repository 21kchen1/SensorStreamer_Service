from Model.Data.TypeData import TypeData
from Resource.String.ModelString import DataString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    AccelerometerU 未校准 数据结构
    @author chen
"""

class AccelerometerUData(TypeData):
    TYPE = DataString.TYPE_ACCELEROMETER_UNCALIBRATED
    VALUE_LEN = 6

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(AccelerometerUData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.Gx_uncalib = values[0]
        self.Gy_uncalib = values[1]
        self.Gz_uncalib = values[2]
        self.Gx_bias = values[3]
        self.Gy_bias = values[4]
        self.Gz_bias = values[5]

AccelerometerUData.DATA_PROCER = ListenProcer(AccelerometerUData)