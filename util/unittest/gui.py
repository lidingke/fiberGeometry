import inspect
import pdb
import sys
import threading

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow, QHBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QObject, SLOT, SIGNAL
from sphinx.builders import changes

from util.observer import PyTypeSignal
from util.unittest.demo import knife_into


class View(QWidget):
    def __init__(self):
        super(View, self).__init__()
        hlayout = QHBoxLayout()
        self.input_line = QLineEdit("123")
        self.enter_button = QPushButton('enter')

        self.enter_button.clicked.connect(self.show_enter)
        # clicked = self.enter_button.clicked
        self.output_line = QLabel("1234567")
        hlayout.addWidget(self.input_line)
        hlayout.addWidget(self.enter_button)
        hlayout.addWidget(self.output_line)
        # print dir()
        self.setLayout(hlayout)

    def show_enter(self):
        inputs = int(self.input_line.text()) + 1
        self.output_line.setText(str(inputs))
        # def show(self):
        #     self.show()


if __name__ == '__main__':
    # start_server()
    app = QApplication(sys.argv)
    view = View()
    # code =  view.__init__.__code__
    # # pdb.set_trace()
    # codes = inspect.getsource(view.__init__)
    # print codes
    # # connecter = Connecter()
    # # print dir(view)
    threading.Thread(target=knife_into, args=(view,)).start()

    view.show()
    # Client().get_change()

    sys.exit(app.exec_())
