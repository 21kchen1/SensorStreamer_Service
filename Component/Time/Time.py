import time

"""
    时间处理静态类
    @version 1.0
    @author chen
"""

class Time:

    """
        获得系统时间
    """
    @staticmethod
    def getSystemTime() -> int:
        return int(time.time() * 1000)