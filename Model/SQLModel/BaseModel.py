from peewee import Model

from Dao import MySql

"""
    基本模型
    @author chen
"""

class BaseModel(Model):
    class Meta:
        database = MySql.sqlInit()