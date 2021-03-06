import inspect
import pdb
import sys
import threading

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import  QHBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt4.QtGui import QWidget

from SDK.tests.test_gui.testcases import knife_into_demo


class View(QWidget):
    def __init__(self):
        super(View, self).__init__()
        hlayout = QHBoxLayout()
        self.input_line = QLineEdit("123")
        self.enter_button = QPushButton('-1s')
        self.enter_button.clicked.connect(self.show_enter)
        self.output_line = QLabel("1234567")
        hlayout.addWidget(self.input_line)
        hlayout.addWidget(self.enter_button)
        hlayout.addWidget(self.output_line)
        self.setLayout(hlayout)

    def show_enter(self):
        inputs = int(self.input_line.text()) - 1
        self.output_line.setText(str(inputs))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    threading.Thread(target=knife_into_demo, args=(view,)).start()#unittest thread insert
    view.show()
    sys.exit(app.exec_())
