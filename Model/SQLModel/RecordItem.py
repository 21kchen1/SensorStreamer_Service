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
    picturePath = CharField()
    # 视频路径
    videoPath = CharField()
    # 音频路径
    audioPath = CharField()
    # 传感器路径
    accelerometerPath = CharField()
    gyroscopePath = CharField()
    rotationVectorPath = CharField()
    magneticFieldPath = CharField()