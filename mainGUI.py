

import sys
import os
import pdb

from PyQt4 import QtCore, QtGui, uic
from GUI.view.view import View
from GUI.controller import Controller


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Controller(View())
    c.show()

    sys.exit(app.exec_())
