# coding:utf-8
"""project names: cvoffline,cvonline,cvopoffline,cvoponline"""
import pdb
import sys
import os
import logging

from setting import config
from setting.configs.tool import update_config_by_name, SAFE_ARGVS

if len(sys.argv) > 1:
    project_name = sys.argv[1]
else:
    raise ValueError("input argv must be " + " ".join(SAFE_ARGVS))
config_info = update_config_by_name(project_name)
log_level = getattr(logging, config.LOG_LEVEL, logging.ERROR)
log_dir = getattr(config,"LOG_DIR",False)
if log_dir == "print":
    logging.basicConfig(format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
        level=log_level)
else:
    logging.basicConfig(filename="setting\\testlog.log",
        filemode="a", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
        level=log_level)
logger = logging.getLogger(__name__)
logger.error(config_info)


from PyQt4.QtGui import QPalette, QColor, QApplication
from GUI.view.view import get_view
from GUI.controller import get_controller
from util.load import loadStyleSheet

if __name__ == '__main__':
    # sys.stdout = open('setting\\abc.txt', 'w')
    label = config.VIEW_LABEL  # label为AutomaticCV
    logger.error(" main info: {} {} \n{}".format(label, project_name, sys.argv[0]))
    app = QApplication(sys.argv)
    app.setStyleSheet(loadStyleSheet('main'))
    # pt = QPalette()
    # pt.setColor(QPalette.Background, QColor(4, 159, 241))
    # app.setPalette(pt)
    controller = get_controller(label)
    view = get_view(label)
    # print view.__dict__, type(view)
    c = controller(view())
    c.show()
    # sys.stdout = sys.__stdout__

    sys.exit(app.exec_())
