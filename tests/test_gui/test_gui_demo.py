import sys
import threading

from PyQt4.QtGui import QApplication
import logging
logging.basicConfig(format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                    level=logging.ERROR)
from tests.test_gui.testcases import knife_into_demo
from util.unittest.demogui import View


def test_gui_demo():
    try:
        app = QApplication(sys.argv)
        view = View()
        threading.Thread(target=knife_into_demo, args=(view,app)).start()#unittest thread insert
        view.show()
        sys.exit(app.exec_())
    except SystemExit:
        pass
