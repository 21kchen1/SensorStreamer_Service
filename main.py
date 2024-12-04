from View.MainView import Ui_MainWidget
from View.ViewActive import ViewActive
from component.Control.WatchControl import WatchControl
from component.DataDeal.DataRecver import DataRecver
from component.Link.TCPMLinkListen import TCPMLinkListen
from component.Link.UDPLink import UDPLink
import socket
import logging

WATCH_TCP_PORT = 5006
WATCH_UDP_PORT = 5005
PHONE_TCP_PORT = 5008
PHONE_UDP_PORT = 5007
CHARSET = "utf-8"

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)
# 视图活动
viewActive = ViewActive(Ui_MainWidget())
# 启动 UDP
watchUDPLink = UDPLink(WATCH_UDP_PORT, "0.0.0.0")
phoneUDPLink = UDPLink(PHONE_UDP_PORT, "0.0.0.0")
viewActive.setDataRecver(DataRecver([watchUDPLink, phoneUDPLink], 10240, CHARSET))

# 处理数据接收
def dealData(conn: socket) -> None:
    while True:
        if getattr(conn, '_closed'):
            break
        data, address = watchUDPLink.rece(10240)
        print(f"Received message: {data} from {address}")

# 手表监听器回调函数
def watchListenCallback(conn: socket, addr) -> None:
    # threading.Thread(target= dealData, args= {conn}).start()
    # 添加回调函数
    watchControl = WatchControl(conn, viewActive.cancelWatchControl, CHARSET)
    viewActive.setWatchControl(watchControl)

if __name__ == "__main__":
    # 开始监听
    watchListen = TCPMLinkListen(WATCH_TCP_PORT, "0.0.0.0", watchListenCallback)
    watchListen.startListen()
    # 开启视图
    viewActive.run()

