import logging
logging.basicConfig(#filename="setting\\testlog.log",
                    filemode="a", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                    level=logging.ERROR)

from setting import config
config.VIEW_LABEL = "ManualCV"  # ManualCV AutomaticCV
config.DYNAMIC_CAMERA = True
config.SAVE_TEMP_IMG = True
# from setting.parameter import SETTING
# SETTING()

import sys
import os
import pdb

from PyQt4.QtGui import QPalette, QColor,QApplication
from GUI.view.view import get_view
from GUI.controller import get_controller
from setting.initcorrect import InitCorrect
from util.load import loadStyleSheet


if __name__ == '__main__':
    # SETTING()['tempLight'] = []
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
    # print view.__dict__, type(view)
    c = controller(view())
    c.show()
    sys.exit(app.exec_())