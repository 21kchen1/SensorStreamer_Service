import sys
sys.path.append("../")

from Controller.DataSaveController import DataSaveController
from View.View import View
from Controller.ControlController import ControlController
from Model.SQLModel.RecordItem import RecordItem
from component.DataDeal.DataRecver import DataRecver
from component.Link.TCPMLinkListen import TCPMLinkListen
from component.Link.UDPLink import UDPLink
from Dao import MySql
import logging

"""
    mainTest
    @author chen
"""

WATCH_TCP_PORT = 5006
WATCH_UDP_PORT = 5005
PHONE_TCP_PORT = 5008
PHONE_UDP_PORT = 5007
CHARSET = "utf-8"

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)

if __name__ == "__main__":
    # 创建表
    MySql.DB.create_tables([RecordItem], safe= True)
    # MySql.DB.drop_tables([RecordItem])

    # 视图
    view = View()

    # 启动 UDP
    watchUDPLink = UDPLink(WATCH_UDP_PORT, "0.0.0.0")
    phoneUDPLink = UDPLink(PHONE_UDP_PORT, "0.0.0.0")
    # 数据控制器
    dataDealController = DataSaveController(view, DataRecver([watchUDPLink, phoneUDPLink], 10240, CHARSET))

    # 控制控制器
    controlController = ControlController(view, CHARSET)
    # 开始监听，并生成控制
    watchListen = TCPMLinkListen(WATCH_TCP_PORT, "0.0.0.0", controlController.setWatchControl)
    watchListen.startListen()
    phoneListen = TCPMLinkListen(PHONE_TCP_PORT, "0.0.0.0", controlController.setPhoneControl)
    phoneListen.startListen()

    # 开启视图
    view.run()


