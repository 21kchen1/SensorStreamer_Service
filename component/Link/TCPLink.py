import socket
import threading
from component.Link.Link import Link

class TCPLink(Link):
    def __init__(self, port: int, address: str, receCallback: function) -> None:
        super().__init__(port, address)
        self.receCallback = receCallback

        # 设置 socket
        self.serviceSocket = None
        self.clientSocket = None
        # 线程锁
        self.serviceLock = threading.Lock()
        self.clientLock = threading.Lock()
        # 连接标志
        self.linking = False

    def rece(self, bufSize = 1024) -> tuple[str]:
        if not self.linking or not self.clientSocket:
            return None

        try:
            data = self.clientSocket.recv(bufSize)
            return data
        except Exception as e:
            print("TCPLink.rece:", e)
            return None

    def send(self, data: str, encode: str) -> bool:
        if not self.linking or not self.clientSocket:
            return False

        try:
            self.clientSocket.sendall(data.encode(encode))
            return True
        except Exception as e:
            print("TCPLink.send:", e)
            return False

    # 开启连接线程
    def startListen(self) -> None:
        self.linking = True
        with self.serviceLock:
            if self.serviceSocket:
                self.serviceSocket.close()
            # 创建一个新 socket 并开始监听
            self.serviceSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serviceSocket.bind((self.address, self.port))
            self.serviceSocket.listen()
        linkingThread = threading.Thread(target= self._linking, args= (self))
        linkingThread.start()

    # 连接并持续调用 rece
    def _linking(self) -> None:
        while self.linking:
            try:
                # 连接阻塞
                self.clientSocket, self.address = self.serviceSocket.accept()
                print(f"TCPLink._linking: Connection from { self.address }")
                while self.linking:
                    data = self.rece()
                    if data == None:
                        break
                    # 使用回调函数处理数据
                    self.receCallback(data)
            except Exception as e:
                print("TCPLink._linking:", e)
                self.clientSocket.close()
                if self.linking:
                    continue
                break

    # 关闭连接
    def stopListen(self) -> None:
        self.linking = False
        if not self.serviceSocket:
            return
        self.serviceSocket.close()



