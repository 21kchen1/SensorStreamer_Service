import socket
import threading
from Service.Link.Link import Link
import logging

"""
    TCPLink 仅处理一个 TCP 连接。
    一个 TCPLink 对应一个 client socket
    @author chen
"""
class TCPLink(Link):
    """
        @param port 端口
        @param address 一般为 0.0.0.0, 其余无效
    """
    def __init__(self, port: int, address: str) -> None:
        super().__init__(port, address)

        # 设置 socket
        self.serviceSocket = None
        self.clientSocket = None
        # 线程锁
        self.serviceLock = threading.Lock()
        self.clientLock = threading.Lock()
        # 当已经连接时，进入阻塞
        self.linkingBlock = threading.Condition()

        # 连接标志
        self.__linking = False

    """
        @param data 数据
        @param encode 编码方式
        @return 发送成功
    """
    def send(self, data: str, encode: str) -> bool:
        if not self.clientSocket or getattr(self.clientSocket, '_closed'):
            return False

        try:
            self.clientSocket.sendall(data.encode(encode))
            return True
        except Exception as e:
            logging.warning(str(e))
            with self.linkingBlock:
                self.linkingBlock.notify()
            return False

    """
        @param bufSize 设置缓冲大小
        @return 返回数据与客户端地址
    """
    def rece(self, bufSize = 1024) -> tuple:
        if not self.clientSocket or getattr(self.clientSocket, '_closed'):
            return None, None

        try:
            data, address = self.clientSocket.recvfrom(bufSize)
            if not data:
                raise socket.error("The remote host aborted an established connection")
            return data, address
        except Exception as e:
            logging.warning(str(e))
            with self.linkingBlock:
                self.linkingBlock.notify()
            return None, None

    """
        设置 __linking 为真
        启动 service socket, 启动监听线程
    """
    def startListen(self) -> None:
        self.__linking = True
        with self.serviceLock:
            if self.serviceSocket:
                self.serviceSocket.close()
            # 创建一个新 socket 并开始监听
            self.serviceSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serviceSocket.bind((self.address, self.port))
            self.serviceSocket.listen()
        logging.info(f"Listening on { self.port }")
        linkingThread = threading.Thread(target= self.__tryLink)
        linkingThread.start()

    """
        监听状态下持续尝试 client socket
        当 __linking 为真时, 连接失效会继续尝试
    """
    def __tryLink(self) -> None:
        if self.clientSocket:
            self.clientSocket.close()

        while self.__linking:
            try:
                # 未连接阻塞
                self.clientSocket, self.address = self.serviceSocket.accept()
                logging.info(f"Connection from { self.address }")
                # 连接阻塞
                with self.linkingBlock:
                    self.linkingBlock.wait()

                self.clientSocket.close()
            except Exception as e:
                logging.error(str(e))
                self.clientSocket.close()
                if self.__linking:
                    continue
                break

    """
        设置 __linking 为 False
        关闭监听模式
    """
    def stopListen(self) -> None:
        self.__linking = False
        with self.linkingBlock:
            self.linkingBlock.notify()
        if not self.serviceSocket:
            return
        self.serviceSocket.close()