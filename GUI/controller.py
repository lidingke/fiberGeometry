# from view import View
from GUI.model.modecv import ModelCV
from GUI.model.modelop import ModelOp
from PyQt4.QtCore import QObject, pyqtSignal
# from SDK.mindpy import IsInitCamera

class Controller(QObject):
    """docstring for Controller"""
    def __init__(self,view):
        super(Controller, self).__init__()
        self._view = view
        self._startModel()

    def show(self):
        self._modelcv.start()
        self._modelop.start()
        self._view.show()

    def _startModel(self):
        self._modelcv = ModelCV()
        self._modelop = ModelOp()
        self._view.getModel(self._modelcv)
        self._modelcv.returnImg.connect(self._view.updatePixmap)
        self._view.beginTest.clicked.connect(self._modelcv.mainCalculate)
        self._modelop.returnImg.connect(self._view.upadateOpticalview)
        # self._view.multiTest.clicked.connect(self._model.multiTest)


