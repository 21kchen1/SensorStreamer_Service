from Model.Data.TypeData import TypeData
from Model.Data.SensorSubData.AccelerometerData import AccelerometerData
from Model.Data.SensorSubData.GyroscopeData import GyroscopeData
from Model.Data.SensorSubData.MagneticFieldData import MagneticFieldData
from Model.Data.SensorSubData.RotationVectorData import RotationVectorData

"""
    Sensor 数据结构
    @author chen
"""

class SensorData(TypeData):
    TYPE = "SensorData"

    TYPE_CLASS_DICT = {
        AccelerometerData.TYPE: AccelerometerData,
        GyroscopeData.TYPE: GyroscopeData,
        MagneticFieldData.TYPE: MagneticFieldData,
        RotationVectorData.TYPE: RotationVectorData,
    }

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