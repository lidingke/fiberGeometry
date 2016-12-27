

import sys
import os
import pdb
from setting.orderset import SETTING
Set = SETTING({'ampFactor': '20X', 'cameraID': 'MindVision'})
Set['ifcamera'] = False
# print 'if camera', len(Set)

from PyQt4.QtGui import QPalette, QColor,QApplication
from PyQt4.QtCore import QCoreApplication, QFile
from GUI.view.view import DynamicView
from GUI.controller import Controller

def loadStyleSheet(sheetName):
#D:\MyProjects\WorkProject\opencv4fiber\cv\GUI\UI\qss\main.qss
    with open('GUI/UI/qss/{}.qss'.format(sheetName), 'rb') as f:
        styleSheet = f.readlines()
        # print(read)
        styleSheet = b''.join(styleSheet)
        styleSheet = styleSheet.decode('utf-8')

    return styleSheet


if __name__ == '__main__':

    print ('len set', len(Set))
    app = QApplication(sys.argv)
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background , QColor(4,159,241))
    app.setPalette(pt)
    c = Controller(DynamicView())
    c.show()

    sys.exit(app.exec_())