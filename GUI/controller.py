# from    view        import View

from GUI.model.model import Model
from PyQt4.QtCore import QObject, pyqtSignal
# from SDK.mindpy import IsInitCamera

class Controller(QObject):
    """docstring for Controller"""
    def __init__(self,view):
        super(Controller, self).__init__()
        self._view = view
        self._startModel()

    def show(self):
        self._model.start()
        self._view.show()


    def _startModel(self):
        self._model = Model()
        self._view.getModel(self._model)
        self._model.returnImg.connect(self._view.updatePixmap)
        self._view.pushButton.clicked.connect(self._model.mainCalculate)
        self._view.multiTest.clicked.connect(self._model.multiTest)
