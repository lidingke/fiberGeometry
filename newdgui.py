
from setting.orderset import SETTING
SETTING('MindVision500', 'Online')
import sys
import os
import pdb

from PyQt4.QtGui import QPalette, QColor,QApplication
from GUI.view.view import DynamicView
from GUI.controller import Controller



def loadStyleSheet(sheetName):
    with open('GUI/UI/qss/{}.qss'.format(sheetName), 'rb') as f:
        styleSheet = f.readlines()
        styleSheet = b''.join(styleSheet)
        styleSheet = styleSheet.decode('utf-8')

    return styleSheet


if __name__ == '__main__':
    SETTING('MindVision500', 'Online')
    app = QApplication(sys.argv)
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background , QColor(4,159,241))
    app.setPalette(pt)
    c = Controller(DynamicView())
    c.show()
    sys.exit(app.exec_())