from setting import config
config.VIEW_LABEL = "ManualCV"  # ManualCV AutomaticCV
config.DYNAMIC_CAMERA = True
from setting.orderset import SETTING
SETTING('MindVision500', 'Online', "G652", "centerImg")
import logging
logging.basicConfig(level=logging.INFO)
import sys
import os
import pdb

from PyQt4.QtGui import QPalette, QColor,QApplication, QMessageBox, QWidget
from GUI.view.view import View, get_view
from GUI.controller import get_controller
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
    label = config.VIEW_LABEL
    controller = get_controller(label)
    view = get_view(label)
    print view.__dict__, type(view)
    c = controller(view())
    c.show()
    sys.exit(app.exec_())