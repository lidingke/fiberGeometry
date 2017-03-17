import sys
import os
import pdb
from setting.orderset import SETTING
Set = SETTING("test", "octagon", "centerImg")#, "nostdout")
Set['ifcamera'] = False
from PyQt4.QtGui import QPalette, QColor,QApplication
from PyQt4.QtCore import QCoreApplication, QFile
from GUI.view.view import View
from GUI.controller import Controller
from util.load import loadStyleSheet



if __name__ == '__main__':
    # sys.stdout = open('setting\\abc.txt', 'w')
    print ('len set', len(Set))
    app = QApplication(sys.argv)
    app.setStyleSheet(loadStyleSheet('main'))
    pt = QPalette()
    pt.setColor(QPalette.Background , QColor(4,159,241))
    app.setPalette(pt)
    c = Controller(View())
    c.show()
    # sys.stdout = sys.__stdout__

    sys.exit(app.exec_())