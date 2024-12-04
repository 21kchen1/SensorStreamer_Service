import logging
from peewee import MySQLDatabase

"""
    数据库配置
    @author chen
"""

DB = None

"""
    数据库初始化及连接
    @return 成功
"""
def sqlInit() -> bool:
    try:
        config = {
            "database": "badminton",
            "user": "root",
            "password": "mysqlpassword",
            "host": "localhost",
            "port": 3306
        }

        global DB
        DB = MySQLDatabase(**config)
        DB.connect()
        return True
    except Exception as e:
        logging.error(f"sqlInit: {e}")
        return False

def sqlClose() -> None:
    if DB == None:
        return
    DB.close()