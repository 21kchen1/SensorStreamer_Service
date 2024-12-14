from Model.Control.TypeControl import TypeControl

"""
    Sensor 控制数据结构
    @author chen
"""

class SensorControl(TypeControl):
    TYPE = "SENSOR"

    SENSOR_ACCELEROMETER = 1
    SENSOR_GYROSCOPE = 4
    SENSOR_ROTATION_VECTOR = 11
    SENSOR_MAGNETIC_FIELD = 2

    TEST_LIST = [
        SENSOR_ACCELEROMETER,
        SENSOR_GYROSCOPE,
        SENSOR_ROTATION_VECTOR,
        SENSOR_MAGNETIC_FIELD
    ]

    """
        @param sampling 采样率
        @param sensors sensor 列表
    """
    def __init__(self, sampling: int, sensors: list) -> None:
        super().__init__(SensorControl.TYPE, sampling)
        self.sensors = sensors