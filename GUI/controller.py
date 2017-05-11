# from view import View
from setting.orderset import SETTING
from GUI.model.modecv import ModelCV
from GUI.model.modelop import ModelOp
from PyQt4.QtCore import QObject, pyqtSignal

class Controller(QObject):
    """docstring for Controller"""
    def __init__(self,view):
        super(Controller, self).__init__()
        self._view = view
        self._startModel()

    def show(self):
        self._modelcv.start()
        # self._modelop.start()
        self._view.show()

    def _startModel(self):
        self._modelcv = ModelCV()
        # self._modelop = ModelOp()
        self._view.getModel(self._modelcv)
        self._modelcv.returnImg.connect(self._view.updatePixmap)
        self._modelcv.returnATImg.connect(self._view.updateOpticalview)
        self._view.beginTestCV.clicked.connect(self._modelcv.mainCalculate)
        self._view.beginTestAT.clicked.connect(self._getAttenuation)
        self._modelcv.resultShowCV.connect(self._view.updateCVShow)
        self._modelcv.resultShowAT.connect(self._view.updateATShow)
        self._modelcv.returnCoreLight.connect(self._view.getCoreLight)
        self._view.focuser.clicked.connect(self._modelcv.focus)
        self._view.fiberTypeBox.currentIndexChanged.connect(self._changeFiberType)

        # self._tempMedianIndex()

        # self._view.multiTest.clicked.connect(self._model.multiTest)

    def _getAttenuation(self,):
        length = self._view.fiberLength.text()
        length = float(length)
        self._modelcv.attenuationTest(length)

    def _changeFiberType(self):
        key = str(self._view.fiberTypeBox.currentText())
        SETTING().keyUpdates(key)
        newKey = SETTING().get('fiberType','error type')
        # self._view.fiberTypeLabel.setText(newKey)
        self._modelcv.updateClassifyObject(newKey)


