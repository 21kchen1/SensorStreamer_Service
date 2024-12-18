from Model.Data.TypeData import TypeData
from Resource.String.ModelString import DataString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    GyroscopeU 未校准 数据结构
    @author chen
"""

class GyroscopeUData(TypeData):
    TYPE = DataString.TYPE_GYROSCOPE_UNCALIBRATED
    VALUE_LEN = 6

    def __init__(self, unixTimestamp: int, sensorTimestamp: int, values: list) -> None:
        super().__init__(GyroscopeUData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.angularSpeedX_no_drift = values[0]
        self.angularSpeedY_no_drift = values[1]
        self.angularSpeedZ_no_drift = values[2]
        self.angularSpeedX_drift = values[3]
        self.angularSpeedY_drift = values[4]
        self.angularSpeedZ_drift = values[5]

GyroscopeUData.DATA_PROCER = ListenProcer(GyroscopeUData)