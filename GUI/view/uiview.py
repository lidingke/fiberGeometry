#coding=utf-8
from GUI.UI.modbusUI import Ui_Form as modbusUI
from GUI.UI.cvUI import Ui_MainWindow as cvUI

import sys
from PyQt4 import QtGui


class ManualCVForm(QtGui.QMainWindow, cvUI):
    def __init__(self, ):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


class AutomaticCVForm(QtGui.QMainWindow, cvUI):
    def __init__(self, ):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        modbu_ui = modbusUI()#初始化串口发送面板
        modbu_ui.setupUi(self.extendwidget)#将串口发送面板添加到cvUI面板中
        self.__dict__.update(modbu_ui.__dict__)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AutomaticCVForm()
    myapp.show()
    sys.exit(app.exec_())
