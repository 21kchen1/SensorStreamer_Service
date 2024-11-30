import sys
sys.path.append("../")

from View.MainView import Ui_MainWidget
from View.ViewActive import ViewActive



va = ViewActive(Ui_MainWidget())
va.run()