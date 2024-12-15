from Model.Data.TypeData import TypeData
from Resource.String.DataString import DataString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    MagneticFieldU 未校准 数据结构
    @author chen
"""

class MagneticFieldUData(TypeData):
    TYPE = DataString.TYPE_MAGNETIC_FIELD_UNCALIBRATED
    VALUE_LEN = 6

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(MagneticFieldUData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.magneticFieldX_uncalib = values[0]
        self.magneticFieldY_uncalib = values[1]
        self.magneticFieldZ_uncalib = values[2]
        self.magneticFieldX_bias = values[3]
        self.magneticFieldY_bias = values[4]
        self.magneticFieldZ_bias = values[5]

MagneticFieldUData.DATA_PROCER = ListenProcer(MagneticFieldUData)