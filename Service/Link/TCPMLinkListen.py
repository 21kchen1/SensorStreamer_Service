import socket
import logging
import threading
from Service.Link.Link import Link

"""
    TCPMLinkListen 处理多个 TCP 连接。
    开启监听模式后, 如果接收到客户端连接, 则启动回调函数线程并传递对应 client socket
    @author chen
"""
class TCPMLinkListen(Link):
    """
        @param port 端口
        @param address 一般为 0.0.0.0, 其余无效
        @param callback 回调函数
    """
    def __init__(self, port: int, address: str, callback) -> None:
        super().__init__(port, address)
        # 设置回调函数
        self.callback = callback

        # 设置 socket
        self.serviceSocket = None
        # 线程锁
        self.serviceLock = threading.Lock()

        # 连接标志
        self.__linking = False

    """
        @param conn 连接的 socket
        @param data 数据
        @param encode 编码方式
        @return 发送成功
    """
    @staticmethod
    def send(conn: socket, data: str, encode: str) -> bool:
        if not conn or getattr(conn, '_closed'):
            return False

        try:
            conn.sendall(data.encode(encode))
            return True
        except Exception as e:
            logging.warning(f"send: {e}")
            return False

    """
        @param conn 连接的 socket
        @param bufSize 设置缓冲大小
        @return 返回数据与客户端地址
    """
    @staticmethod
    def rece(conn: socket, bufSize = 1024) -> tuple:
        if not conn or getattr(conn, '_closed'):
            return None, None

        try:
            data, address = conn.recvfrom(bufSize)
            if not data:
                raise socket.error("The remote host aborted an established connection")
            return data, address
        except Exception as e:
            logging.warning(f"rece: {e}")
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
        threading.Thread(target= self.__tryLink).start()

    """
        监听状态下持续尝试 client socket, 获取所有客户端的连接
    """
    def __tryLink(self) -> None:
        while self.__linking:
            try:
                # 未连接阻塞
                conn, self.address = self.serviceSocket.accept()
                logging.info(f"Connection from { self.address }")
                threading.Thread(target= self.callback, args=(conn, self.address)).start()
            except Exception as e:
                logging.error(f"__tryLink: {e}")
                if self.__linking:
                    continue
                break

    """
        设置 __linking 为 False
        关闭监听模式
    """
    def stopListen(self) -> None:
        self.__linking = False
        if not self.serviceSocket:
            return
        self.serviceSocket.close()