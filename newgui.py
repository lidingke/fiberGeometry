

import sys
import os
import pdb

from PyQt4.QtGui import QPalette, QColor,QApplication
from PyQt4.QtCore import QCoreApplication, QFile
from GUI.view.view import StaticView
from GUI.controller import Controller

from setting.set import SETTING


def loadStyleSheet(sheetName):
#D:\MyProjects\WorkProject\opencv4fiber\cv\GUI\UI\qss\main.qss
    with open('GUI/UI/qss/{}.qss'.format(sheetName), 'rb') as f:
        styleSheet = f.readlines()
        # print(read)
        styleSheet = b''.join(styleSheet)
        styleSheet = styleSheet.decode('utf-8')

    return styleSheet


if __name__ == '__main__':
    SETTING({'ampFactor':'20X','cameraID':'MindVision'})
    app = QApplication(sys.argv)
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background , QColor(4,159,241))
    app.setPalette(pt)
    c = StaticView()
    c.show()

    sys.exit(app.exec_())