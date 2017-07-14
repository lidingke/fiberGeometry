#coding:utf-8
# from view import View
from functools import partial

from GUI.model.stateconf import state_number, CONTEXT
from SDK.modbus.modbusmerge import AbsModeBusModeByAxis
from setting.orderset import SETTING
from GUI.model.modecv import ModelCV
from GUI.model.modelop import ModelOp
from PyQt4.QtCore import QObject, pyqtSignal

import logging
logger = logging.getLogger(__name__)

class StateMixin(object):

    def state_1(self):
        pass

    def state_2(self):
        pass


    def state_3(self):
        pass


    def state_4(self):
        pass


    def state_5(self):
        pass

    def state_all(self):
        # self.modbus_up_down(self.squence_number)
        self.modbus.motor_up_down(str(self.sequence_number+1))


class Controller(QObject, StateMixin):
    """docstring for Controller"""
    #todo: state manager 放在这一层
    def __init__(self,view):
        super(Controller, self).__init__()
        QObject.__init__(self)
        self._view = view
        self._startModel()
        self._start_modbus()
        self.state_number = state_number()
        self.sequence_number = None


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
        # self._view.beginTestAT.clicked.connect(self._getAttenuation)
        self._modelcv.resultShowCV.connect(self._view.updateCVShow)
        self._modelcv.resultShowAT.connect(self._view.updateATShow)
        self._modelcv.returnCoreLight.connect(self._view.getCoreLight)
        if hasattr(self._view, "focuser"):
            self._view.focuser.clicked.connect(self._modelcv.focus)
        self._view.fiberTypeBox.currentIndexChanged.connect(self._changeFiberType)
        # self.state_connect()
        # self._tempMedianIndex()
        # self._view.multiTest.clicked.connect(self._model.multiTest)

    def _start_modbus(self):
        self.modbus = AbsModeBusModeByAxis(port='com14')
        self.state_connect()

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

    def state_connect(self):
        def state_change(self):
            print(self)
            self.sequence_number = next(self.state_number)
            self.state_all()
            logger.warning("next state"+str(self.sequence_number))
        if hasattr(self._view, "next_state"):
            self._view.next_state.clicked.connect(partial(state_change,self))






