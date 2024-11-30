import threading
from View.MainView import Ui_MainWidget
from View.ViewActive import ViewActive
from component.Control.WatchControl import WatchControl
from component.Link.TCPMLinkListen import TCPMLinkListen
from component.Link.UDPLink import UDPLink
import socket
import logging

watchTCPPort = 5006
watchUDPPort = 5005

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)
# 视图活动
viewActive = ViewActive(Ui_MainWidget())

dataDgram = UDPLink(watchUDPPort, "0.0.0.0")
# 处理数据接收
def dealData(conn: socket):
    while True:
        if getattr(conn, '_closed'):
            break
        data, address = dataDgram.rece(10240)
        print(f"Received message: {data} from {address}")

# 手表监听器回调函数
def watchListenCallback(conn: socket, addr):
    threading.Thread(target=dealData, args= {conn}).start()
    # 添加回调函数
    watchControl = WatchControl(conn, viewActive.cancelWatchControl, "utf-8")
    viewActive.setWatchControl(watchControl)



if __name__ == "__main__":
    # 开始监听
    watchListen = TCPMLinkListen(watchTCPPort, "0.0.0.0", watchListenCallback)
    watchListen.startListen()
    # 开启视图
    viewActive.run()

