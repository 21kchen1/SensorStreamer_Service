from PyQt5 import QtWidgets

from View.ViewUtil import ViewUtil

class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMain()
        self.initTopLeft()
        self.initTopRight()
        self.initButtom()

    def initMain(self):
        self.setFixedSize(1500, 900)
        self.mainWidget, self.mainLayout = ViewUtil.createWidget("mainWidget", QtWidgets.QGridLayout())
        self.topLeftWidget, self.topLeftLayout = ViewUtil.createWidget("topLeftWidget", QtWidgets.QGridLayout())
        self.topRightWidget, self.topRightLayout = ViewUtil.createWidget("topRightWidget", QtWidgets.QGridLayout())
        self.bottomWidget, self.bottomLayout = ViewUtil.createWidget("bottomWidget", QtWidgets.QGridLayout())
        # 5 * 9
        self.mainLayout.addWidget(self.topLeftWidget, 0, 0, 4, 3)
        self.mainLayout.addWidget(self.topRightWidget, 0, 3, 4, 6)
        self.mainLayout.addWidget(self.bottomWidget, 4, 0, 1, 9)
        self.setCentralWidget(self.mainWidget)

        self.buttonAdaptive = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    def initButtom(self):
        startStreamButton = ViewUtil.createButton("startStreamButton", "Start")
        stopStreamButton = ViewUtil.createButton("stopStreamButton", "Stop")
        startStreamButton.setSizePolicy(self.buttonAdaptive)
        stopStreamButton.setSizePolicy(self.buttonAdaptive)
        # 绑定
        startStreamButton.clicked.connect(self.startStream)
        stopStreamButton.clicked.connect(self.stopStream)

        self.bottomLayout.addWidget(startStreamButton, 0, 0, 1, 1)
        self.bottomLayout.addWidget(stopStreamButton, 0, 1, 1, 1)

    def initTopLeft(self):
        Button = ViewUtil.createButton("Button", "Start")
        Button.setSizePolicy(self.buttonAdaptive)
        self.topLeftLayout.addWidget(Button, 0, 0, 1, 1)

    def initTopRight(self):
        Button = ViewUtil.createButton("Button", "Start")
        Button.setSizePolicy(self.buttonAdaptive)
        self.topRightLayout.addWidget(Button, 0, 0, 1, 1)



    def startStream(self):
        # 发送启动客户端的命令
        pass

    def stopStream(self):
        # 发送关闭客户端的命令
        pass

    def update_status(self, status):
        self.status_label.setText(f"Status: {status}")