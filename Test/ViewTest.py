import sys
sys.path.append("../")

"""
    控制器测试
    @deprecated 过时的控制器
"""

from View.MainView import Ui_MainWidget
from Controller.Controller import Controller

va = Controller(Ui_MainWidget())
va.run()