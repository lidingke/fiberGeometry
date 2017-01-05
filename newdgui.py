
from setting.orderset import SETTING
SETTING('MindVision500', 'Online', "octagon", "centerImg")
import sys
import os
import pdb

from PyQt4.QtGui import QPalette, QColor,QApplication, QMessageBox, QWidget
from GUI.view.view import View
from GUI.controller import Controller
from setting.initcorrect import InitCorrect
from setting.load import loadStyleSheet

# def loadStyleSheet(sheetName):
#     with open('GUI/UI/qss/{}.qss'.format(sheetName), 'rb') as f:
#         styleSheet = f.readlines()
#         styleSheet = b''.join(styleSheet)
#         styleSheet = styleSheet.decode('utf-8')
#
#     return styleSheet


if __name__ == '__main__':
    SETTING('MindVision500', 'Online')
    app = QApplication(sys.argv)
    msg = InitCorrect().run()
    if msg:
        print 'get error msg', msg
        QMessageBox.information(QWidget(), "error", str(msg),
                                QMessageBox.NoButton, QMessageBox.NoButton)
        sys.exit(app.exec_())
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background , QColor(4,159,241))
    app.setPalette(pt)
    c = Controller(View())
    c.show()
    sys.exit(app.exec_())