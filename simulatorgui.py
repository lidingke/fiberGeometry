# coding=utf-8
from PyQt4 import QtGui
from setting import config

config.DYNAMIC_CAMERA = False
print 'set dynamic camera', config.DYNAMIC_CAMERA, id(config.DYNAMIC_CAMERA)
from simulator.simview import Controllers

# from simulator.myview import  Controllers


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    c = Controllers()
    c.show()

    sys.exit(app.exec_())
