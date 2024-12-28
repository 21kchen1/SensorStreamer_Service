from View.View import View
from Service.DataDeal.DataShower import DataShower

"""
    DataShow 控制器, 用于处理 UI 与 DataDeal 之间的数据显示任务
    @author chen
"""

class DataShowController:

    def __init__(self, view: View, dataShower: DataShower) -> None:
        # 视图
        self.view = view
        # 数据展示器
        self.dataShower = dataShower
        self.setSlotFunc()

    """
        槽函数
    """

    # 开始
    def startStream(self) -> None:
        self.running = True
        # 设置结束信息
        self.dataShower.setEndInfo(self.view.DATA_STATUS_INFO_STOP)
        # 发送开始信号
        self.dataShower.start()

    # 结束
    def stopStream(self) -> None:
        self.running = False
        # 发送停止信号
        self.dataShower.quit()
        # 等待停止
        self.dataShower.wait()

    # 设置槽
    def setSlotFunc(self) -> None:
        # 反向设置槽函数
        self.dataShower.runSign.connect(self.view.setDataStatusInfo)
        # 设置按钮事件
        self.view.setStartClicked(self.startStream)
        self.view.setStopClicked(self.stopStream)
