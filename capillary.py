from setting.orderset import SETTING
SETTING('MindVision500', 'Online', "capillary", "centerImg")
import sys
import os
import pdb
import logging
logging.basicConfig(level=logging.INFO)
from PyQt4.QtGui import QPalette, QColor,QApplication, QMessageBox, QWidget
from GUI.view.view import CVViewModel
from GUI.controller import Controller
from setting.initcorrect import InitCorrect
from util.load import loadStyleSheet


if __name__ == '__main__':
    # SETTING('MindVision500', 'Online')
    SETTING()['tempLight'] = []
    app = QApplication(sys.argv)
    # msg = InitCorrect().run()
    # if msg:
    #     print 'get error msg', msg
    #     QMessageBox.information(QWidget(), "error", str(msg),
    #                             QMessageBox.NoButton, QMessageBox.NoButton)
    #     sys.exit(app.exec_())
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background , QColor(4,159,241))
    app.setPalette(pt)
    c = Controller(CVViewModel())
    c.show()
    sys.exit(app.exec_())