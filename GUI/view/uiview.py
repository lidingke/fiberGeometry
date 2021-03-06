# coding=utf-8
from GUI.UI.modbusUI import Ui_Form as modbusUI
from GUI.UI.cvUI import Ui_MainWindow as cvUI
from GUI.UI.opcvUI import Ui_MainWindow as opcvUI
from GUI.UI.capUI import Ui_Form as capUI
import sys
from PyQt4 import QtGui


class ManualCVForm(QtGui.QMainWindow, cvUI):
    def __init__(self, ):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


class CapCVForm(QtGui.QMainWindow, cvUI):
    def __init__(self, ):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        cap_ui = capUI()
        cap_ui.setupUi(self.extendwidget)
        self.__dict__.update(cap_ui.__dict__)
        # print self.extendwidget.__dict__,cap_ui.__dict__


class AutomaticCVForm(QtGui.QMainWindow, cvUI):
    def __init__(self, ):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.modbus_ui = modbusUI()  # 初始化串口发送面板
        self.modbus_ui.setupUi(self.extendwidget)  # 将串口发送面板添加到cvUI面板中
        self.__dict__.update(self.modbus_ui.__dict__)


class OPCVForm(QtGui.QMainWindow, opcvUI):
    def __init__(self, ):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.modbus_ui = modbusUI()  # 初始化串口发送面板
        self.modbus_ui.setupUi(self.extendwidget)  # 将串口发送面板添加到cvUI面板中
        self.__dict__.update(self.modbus_ui.__dict__)
        # self.hide_moves_button()

    def hide_moves_button(self):
        collections = ("move_down", "move_up",
                       "move_right", "move_left", "reset")
        moves = {getattr(self.modbus_ui, c) for c in collections}
        for move in moves:
            if move:
                move.hide()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AutomaticCVForm()
    myapp.show()
    sys.exit(app.exec_())
