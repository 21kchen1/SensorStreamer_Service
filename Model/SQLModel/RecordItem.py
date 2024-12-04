from enum import unique
from Model.SQLModel.BaseModel import BaseModel
from peewee import CharField, BooleanField

"""
    实验记录项模型
    @author chen
"""

class RecordItem(BaseModel):
    # 记录名称，即 dataCode
    recordName = CharField(unique= True)
    # 1 man 0 women
    gender = BooleanField()