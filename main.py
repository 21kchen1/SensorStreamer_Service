from Controller.DataSaveController import DataSaveController
from Controller.DataShowController import DataShowController
from Model.Data.AccelerometerData import AccelerometerData
from Model.Data.AccelerometerUData import AccelerometerUData
from Model.Data.AudioData import AudioData
from Model.Data.GyroscopeData import GyroscopeData
from Model.Data.GyroscopeUData import GyroscopeUData
from Model.Data.MagneticFieldData import MagneticFieldData
from Model.Data.MagneticFieldUData import MagneticFieldUData
from Model.Data.PictureData import PictureData
from Model.Data.RotationVectorData import RotationVectorData
from Model.Data.VideoData import VideoData
from Service.DataDeal.DataShower import DataShower
from View.View import View
from Controller.ControlController import ControlController
from Model.SQLModel.RecordItem import RecordItem
from Service.DataDeal.DataRecver import DataRecver
from Service.Link.TCPMLinkListen import TCPMLinkListen
from Service.Link.UDPLink import UDPLink
from Dao import MySql
import logging
import os
import ctypes

"""
    main
    @version 2.0
    @author chen
"""

# 测试模式
TEST = True
# 清理数据库
CLEAN = False

# 窗口宽高
VIEW_WIDTH = 1500
VIEW_HEIGHT = 1000
# 默认存储路径
VIEW_DEFAULT_STORAGE_PATH = "G:/Badminton/DataBase"

# 地址
ADDRESS = "0.0.0.0"
# 端口
WATCH_TCP_PORT = 5006
WATCH_UDP_PORT = 5005
PHONE_TCP_PORT = 5008
PHONE_UDP_PORT = 5007
# 编码
CHARSET = "utf-8"
# 日志设置
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)

"""
    统一字符串与数据模型的映射
"""
STRING_TYPEDATA_DICT = {
    VideoData.TYPE: VideoData,
    PictureData.TYPE: PictureData,
    AudioData.TYPE: AudioData,
    AccelerometerData.TYPE: AccelerometerData,
    AccelerometerUData.TYPE: AccelerometerUData,
    GyroscopeData.TYPE: GyroscopeData,
    GyroscopeUData.TYPE: GyroscopeUData,
    MagneticFieldData.TYPE: MagneticFieldData,
    MagneticFieldUData.TYPE: MagneticFieldUData,
    RotationVectorData.TYPE: RotationVectorData
}

"""
    关闭控制台的快速编辑模式
"""
def disableQEMode() -> None:
    if not os.name == 'nt':
        return

    # 获取标准输入的句柄
    stdinHandle = ctypes.windll.kernel32.GetStdHandle(-10)
    # 获取控制台模式
    mode = ctypes.c_ulong()
    ctypes.windll.kernel32.GetConsoleMode(stdinHandle, ctypes.byref(mode))
    # 禁用快速编辑模式
    mode.value &= ~0x0040
    # 设置控制台模式
    ctypes.windll.kernel32.SetConsoleMode(stdinHandle, mode)

if __name__ == "__main__":
    if not TEST:
        disableQEMode()

    if CLEAN:
        MySql.DB.drop_tables([RecordItem])
        exit(0)

    # 创建表
    MySql.DB.create_tables([RecordItem], safe= True)

    # 视图
    view = View(VIEW_WIDTH, VIEW_HEIGHT)
    # 设置默认存储路径
    view.setDefaultStoragePath(VIEW_DEFAULT_STORAGE_PATH)

    # 控制控制器
    controlController = ControlController(view, CHARSET)
    # 开始监听，并生成控制
    watchListen = TCPMLinkListen(WATCH_TCP_PORT, ADDRESS, controlController.setWatchControl)
    watchListen.startListen()
    phoneListen = TCPMLinkListen(PHONE_TCP_PORT, ADDRESS, controlController.setPhoneControl)
    phoneListen.startListen()

    # 启动 UDP
    watchUDPLink = UDPLink(WATCH_UDP_PORT, ADDRESS)
    phoneUDPLink = UDPLink(PHONE_UDP_PORT, ADDRESS)
    # 数据接收器
    dataRecver = DataRecver([watchUDPLink, phoneUDPLink], 65536, CHARSET, STRING_TYPEDATA_DICT)
    # 数据展示器
    dataShower = DataShower(dataRecver)

    # 数据处理控制器
    dataDealController = DataSaveController(view, dataRecver)
    # 数据展示控制器
    dataShowController = DataShowController(view, dataShower)

    # 开启视图
    view.run()