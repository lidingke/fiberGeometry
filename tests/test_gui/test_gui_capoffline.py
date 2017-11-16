# coding:utf-8
"""project names: cvoffline,cvonline,cvopoffline,cvoponline"""
import sys
import os
import logging
import threading

from setting import config
from setting.configs.tool import update_config_by_name
from tests.test_gui.testcases import knife_into_demo, knife_into_cv, knife_into_cap
from util.unittest.demogui import View

project_name = "capoffline"
update_config_by_name(project_name)
log_level = getattr(logging, config.LOG_LEVEL, logging.ERROR)
logging.basicConfig(  filename="setting\\testlog.log",
    filemode="a", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    level=logging.ERROR)
logger = logging.getLogger(__name__)


from PyQt4.QtGui import QPalette, QColor, QApplication
from GUI.view.view import get_view
from GUI.controller import get_controller
from util.load import loadStyleSheet
def test_gui_cap():
    # project_name = "capoffline"
    # update_config_by_name(project_name)
    try:
        label = config.VIEW_LABEL  # label为AutomaticCV
        assert label == "CapCV"
        logger.error(" main info: {} {} \n{}".format(label, project_name, sys.argv[0]))
        app = QApplication(sys.argv)
        app.setStyleSheet(loadStyleSheet('main'))
        pt = QPalette()
        pt.setColor(QPalette.Background, QColor(4, 159, 241))
        app.setPalette(pt)
        controller = get_controller(label)
        view = get_view(label)
        # print view.__dict__, type(view)
        c = controller(view())
        threading.Thread(target=knife_into_cap, args=(c, app)).start()#unittest thread insert

        c.show()
        # sys.stdout = sys.__stdout__

        sys.exit(app.exec_())

    except SystemExit as e:
        pass