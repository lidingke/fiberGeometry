# from    view        import View

from GUI.model.model import Model
from PyQt4.QtCore import QObject, pyqtSignal


class Controller(QObject):
    """docstring for Controller"""
    def __init__(self,view):
        super(Controller, self).__init__()
        self._view = view
        self._model = Model()

        self._model.returnImg.connect(self._view.updatePixmap)
        self._model.start()
        # self._model.start()

    def show(self):
        self._view.show()
