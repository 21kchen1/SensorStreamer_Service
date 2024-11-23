from component.Control.Control import Control

class WatchControl(Control):
    # 用于控制和接收数据的端口
    def __init__(self, tcpPort: int, udpPort: int) -> None:
        super().__init__(tcpPort, udpPort)

    def run(self):
        print(self.tcpPort)

