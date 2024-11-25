from component.Link.TCPLink import TCPLink
from component.Link.TCPMLink import TCPMLink
import time
import socket
import logging

tcpPort = 5006
udpPort = 5005
HEARTBEAT = "heartbeat"

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.DEBUG)


# a = TCPLink(tcpPort, "0.0.0.0")

# a.startListen()

# while True:
#     # print(a.send("123", "utf-8"))
#     print(a.rece())
#     time.sleep(1)

def callback(conn: socket, addr):
    while True:
        try:
            data, addr = TCPMLink.rece(conn)
            assert isinstance(data, bytes)
            print("recv data: " + data.decode())

            if data == HEARTBEAT:
                assert TCPMLink.send(conn, HEARTBEAT, "utf-8")
            print("send data: " + HEARTBEAT)

            time.sleep(1)
        except Exception as e:
            break

b = TCPMLink(tcpPort, "0.0.0.0", callback)
b.startListen()