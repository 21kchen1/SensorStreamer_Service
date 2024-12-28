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
    # 名字
    name = CharField()
    # 实验次数
    time = IntegerField()
    # 其他
    other = CharField()
    # 持续时间
    duration = IntegerField()
    # 路径
    path = CharField()

"""
    实际使用的模型
    @author chen
"""
class RecordItemEnable:
    # 设置基本信息
    def __init__(
        self,
        recordName: str,
        gender: str,
        exp: str,
        action: str,
        name: str,
        time: int,
        other: str,
        duration: int
    ) -> None:
        # 记录名称，即 dataCode
        self.recordName = recordName
        # 性别
        self.gender = gender
        # 经验
        self.exp = exp
        # 动作
        self.action = action
        # 名字
        self.name = name
        # 实验次数
        self.time = time
        # 其他
        self.other = other
        # 持续时间
        self.duration = duration

    def setPathInfo(
        self,
        path: str
    ) -> None:
        self.path = path

    """
        存储信息
    """
    @staticmethod
    def save(dataDict: dict) -> None:
        try:
            recordItem = RecordItem.create(**dataDict)
            recordItem.save()
        except Exception as e:
            raise e