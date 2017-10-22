# coding:utf-8
from setting import config
from setting.configs.update import update_config_by_name

update_config_by_name("dynamicopcv")
import logging

log_level = getattr(logging, config.LOG_LEVEL)
logging.basicConfig(format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                    level=log_level)

logger = logging.getLogger(__name__)
logger.error("log level:{} {}".format(config.LOG_LEVEL, log_level))

import sys
import os
import pdb
from setting.parameter import SETTING

# Set = SETTING()
# Set['ifcamera'] = False
from PyQt4.QtGui import QPalette, QColor, QApplication
from PyQt4.QtCore import QCoreApplication, QFile
from GUI.view.view import get_view
from GUI.controller import get_controller
from util.load import loadStyleSheet

if __name__ == '__main__':
    # sys.stdout = open('setting\\abc.txt', 'w')

    # print ('len set', len(Set))
    app = QApplication(sys.argv)
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background, QColor(4, 159, 241))
    app.setPalette(pt)
    label = config.VIEW_LABEL  # label为AutomaticCV
    # print label
    controller = get_controller(label)
    view = get_view(label)
    # print view.__dict__, type(view)
    c = controller(view())
    c.show()
    # sys.stdout = sys.__stdout__

    sys.exit(app.exec_())
