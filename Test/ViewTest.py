import sys
sys.path.append("../")

from View.MainView import Ui_MainWidget
from Controller.Controller import Controller

va = Controller(Ui_MainWidget())
va.run()