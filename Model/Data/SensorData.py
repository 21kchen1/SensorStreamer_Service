from Model.Data.TypeData import TypeData
from Resource.String.ModelString import DataString
from Service.DataProcer.ListenProcer import ListenProcer

"""
    Sensor 数据结构
    @author chen
"""

class SensorData(TypeData):
    TYPE = DataString.TYPE_SENSOR

    """
        @param unixTimestamp 系统时间戳
        @param sensorTimestamp 传感器时间戳
        @param sensorType 传感器类型
        @param values 传感器数据
    """
    def __init__(self, unixTimestamp: int, sensorTimestamp: int, sensorType: str, values: list) -> None:
        super().__init__(SensorData.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.sensorType = sensorType
        self.values = values

SensorData.DATA_PROCER = ListenProcer(SensorData)