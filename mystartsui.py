#coding=utf-8
from PyQt4 import  QtGui

# from simulator.myview import  Controllers
from simulator.myview import Controllers

if __name__ == '__main__':#tcp/ip更换预读取的图像文件

    import sys

    app = QtGui.QApplication(sys.argv)
    c = Controllers()
    c.show()

    sys.exit(app.exec_())

