from peewee import Model

from Dao import MySql

"""
    基本模型
    @author chen
"""

class BaseModel(Model):
    # 指定数据库连接
    class Meta:
        database = MySql.DB