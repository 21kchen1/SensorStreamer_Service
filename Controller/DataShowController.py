from time import sleep
from View.View import View
from component.DataDeal.DataRecver import DataRecver
from component.DataDeal.DataShower import DataShower

"""
    DataShow 控制器, 用于处理 UI 与 DataDeal 之间的数据显示任务
    @author chen
"""

class DataShowController:

    def __init__(self, view: View, dataRecver: DataRecver) -> None:
        # 视图
        self.view = view
        # 数据展示器
        self.dataShower = DataShower(dataRecver, self.view.DATA_STATUS_INFO_STOP)
        self.setSlotFunc()

    """
        槽函数
    """

    # 开始
    def startStream(self) -> None:
        self.running = True
        self.dataShower.start()

    # 结束
    def stopStream(self) -> None:
        self.running = False
        # 发送停止信号
        self.dataShower.quit()
        # 等待停止
        self.dataShower.wait()
        # self.view.setDataStatusInfo(View.DATA_STATUS_INFO_STOP)

    # 设置槽
    def setSlotFunc(self) -> None:
        # 反向设置槽函数
        self.dataShower.runSign.connect(self.view.setDataStatusInfo)

        self.view.ui.startStream.clicked.connect(self.startStream)
        self.view.ui.stopStream.clicked.connect(self.stopStream)
