from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal
from Component.DataDeal.DataRecver import DataRecver
from Component.Time.TimeLine import TimeLine

"""
    基于 DataRecver 的线程类，专门用于生成展示数据
    @author chen
"""

class DataShower(QThread):
    # 此信号用于传输到主线程
    runSign = pyqtSignal(str)

    """
        @param dataRecver 获取字典
        @param endInfo 结束信息
    """
    def __init__(self, dataRecver: DataRecver, endInfo: str):
        super().__init__()
        self.dataRecver = dataRecver
        self.endInfo = endInfo
        self.running = False

    def start(self):
        self.running = True
        return super().start()

    def quit(self):
        self.running = False
        return super().quit()

    def run(self):
        # 未发送停止信号时持续运行
        while self.running:
            # 每一秒处理一次
            sleep(1)
            showStr = ""
            # 显示时间
            timestamp = f"System Timestamp: { float(TimeLine.getBaseToNow()) / 1000 } s\n\n"
            showStr += timestamp

            # 数据统计
            dataNumDict = self.dataRecver.typeNumDict
            if len(dataNumDict) == 0:
                self.runSign.emit(showStr)
                continue
            maxLen = max(max(len(str(key)), len(str(value))) for key, value in dataNumDict.items())
            maxLen = max(maxLen, 10)
            # 表头
            dataHead = f"Data Recv Table\n{'-' * (maxLen * 2) }\n{'DataType': <{ maxLen }}\t{'Count': <{ maxLen }}\n"
            # 数据
            dataValues = ""
            for dataType, count in dataNumDict.items():
                dataValues += f"{dataType: <{ maxLen }}\t{count: <{ maxLen }}\n"

            showStr += dataHead + dataValues
            # 发送信号
            if self.running:
                self.runSign.emit(showStr)
        self.runSign.emit(self.endInfo)