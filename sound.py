from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class ServerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.start_button = QPushButton("Start Client")
        self.stop_button = QPushButton("Stop Client")
        self.status_label = QLabel("Status: Offline")
        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)
        self.start_button.clicked.connect(self.start_client)
        self.stop_button.clicked.connect(self.stop_client)

    def start_client(self):
        # 发送启动客户端的命令
        pass

    def stop_client(self):
        # 发送关闭客户端的命令
        pass

    def update_status(self, status):
        self.status_label.setText(f"Status: {status}")

app = QApplication([])
server_gui = ServerGUI()
server_gui.show()
app.exec_()