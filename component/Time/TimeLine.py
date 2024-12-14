import threading
from Component.Time.Time import Time

"""
    统一时间轴静态类
    @version 1.0
    @author chen
"""

class TimeLine(Time):
    __BASE_TIME = 0
    # 线程锁
    __BASE_TIME_LOCK = threading.Lock()

    """
        设置基准时间
    """
    @staticmethod
    def __setBaseTime():
        TimeLine.BASE_TIME = TimeLine.getSystemTime()

    """
        获取基准时间
        如果没有设置基准时间，则将当前时间设置为基准时间并返回
    """
    @staticmethod
    def getBaseTime() -> int:
        if not TimeLine.__BASE_TIME == 0:
            return TimeLine.__BASE_TIME

        with TimeLine.__BASE_TIME_LOCK:
            # 防止多个线程同时进入，需要做额外检查
            if not TimeLine.__BASE_TIME == 0:
                return TimeLine.__BASE_TIME
            TimeLine.__BASE_TIME = TimeLine.getSystemTime()
            return TimeLine.__BASE_TIME

    """
        从基准时间开始计时到现在的时间
    """
    @staticmethod
    def getBaseToNow() -> int:
        if TimeLine.__BASE_TIME == 0:
            return 0
        return TimeLine.getSystemTime() - TimeLine.__BASE_TIME

    """
        重置基准时间
    """
    @staticmethod
    def resetBaseTime():
        TimeLine.__BASE_TIME = 0