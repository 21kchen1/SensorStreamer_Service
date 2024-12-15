import sys
sys.path.append("../../")

from Model.SQLModel.BaseModel import BaseModel
from Model.SQLModel.RecordItem import RecordItem
from View.MainView import Ui_MainWidget
from Controller.Controller import Controller
from Service.Control.WatchControl import WatchControl
from Service.DataDeal.DataRecver import DataRecver
from Service.Link.TCPMLinkListen import TCPMLinkListen
from Service.Link.UDPLink import UDPLink
from Dao import MySql
import socket
import logging

"""
    Old version of main
    @author chen
"""

WATCH_TCP_PORT = 5006
WATCH_UDP_PORT = 5005
PHONE_TCP_PORT = 5008
PHONE_UDP_PORT = 5007
CHARSET = "utf-8"

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)

# 手表监听器回调函数
def watchListenCallback(conn: socket, addr) -> None:
    # 添加回调函数
    watchControl = WatchControl(conn, controller.cancelWatchControl, CHARSET)
    controller.setWatchControl(watchControl)

if __name__ == "__main__":
    # 创建表
    MySql.DB.create_tables([RecordItem], safe= True)

    # 启动 UDP
    watchUDPLink = UDPLink(WATCH_UDP_PORT, "0.0.0.0")
    phoneUDPLink = UDPLink(PHONE_UDP_PORT, "0.0.0.0")

    # 控制器
    controller = Controller(
        ui= Ui_MainWidget(),
        dataRecver= DataRecver([watchUDPLink, phoneUDPLink], 10240, CHARSET)
    )

    # 开始监听
    watchListen = TCPMLinkListen(WATCH_TCP_PORT, "0.0.0.0", watchListenCallback)
    watchListen.startListen()
    # 开启视图
    controller.run()

