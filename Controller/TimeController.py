import logging
from Component.Time.TimeLine import TimeLine
from View.View import View

"""
    Time 控制器, 用于处理 UI 与 Time 之间的时间戳管理任务
    @author chen
"""

class TimeController:

    def __init__(self, view: View) -> None:
        # 视图
        self.view = view

    """
        设置基准时间
    """
    def setBaseTime(self) -> None:
        baseTime = TimeLine.setBaseTime()
        logging.info(f"setBaseTime: { baseTime }")

    """
        重置基准时间
    """
    def resetBaseTime(self):
        TimeLine.resetBaseTime()
        logging.info(f"resetBaseTime: { TimeLine.getBaseTime() }")

    """
        设置槽函数
    """
    def setStartSlot(self):
        self.view.setStartClicked(self.setBaseTime)

    def setStopSlot(self):
        self.view.setStopClicked(self.resetBaseTime)