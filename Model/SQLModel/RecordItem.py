from enum import unique
from Model.SQLModel.BaseModel import BaseModel
from peewee import CharField, BooleanField, IntegerField

"""
    实验记录项模型
    @author chen
"""

class RecordItem(BaseModel):
    # 记录名称，即 dataCode
    recordName = CharField(unique= True)
    # 性别
    gender = CharField()
    # 经验
    exp = CharField()
    # 动作
    action = CharField()
    # 实验次数
    time = IntegerField()
    # 其他
    other = CharField()

    # 图片路径
    picturePath = CharField(null= True)
    # 视频路径
    videoPath = CharField(null= True)
    # 音频路径
    audioPath = CharField(null= True)
    # 传感器路径
    accelerometerPath = CharField(null= True)
    gyroscopePath = CharField(null= True)
    rotationVectorPath = CharField(null= True)
    magneticFieldPath = CharField(null= True)

"""
    用于记录基础信息
"""
class RecordItemBaseInfo:
    def __init__(self, recordName: str, gender: str, exp: str, action: str, time: int, other: str) -> None:
        # 记录名称，即 dataCode
        self.recordName = recordName
        # 性别
        self.gender = gender
        # 经验
        self.exp = exp
        # 动作
        self.action = action
        # 实验次数
        self.time = time
        # 其他
        self.other = other