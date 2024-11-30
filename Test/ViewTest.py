import sys
sys.path.append("../")

from View.MainView import Ui_MainWidget
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QWidget()

server_gui = Ui_MainWidget()
server_gui.setupUi(mainWindow)

mainWindow.show()
sys.exit(app.exec_())