# coding:utf-8
# from view import View
from functools import partial
from setting.config import MODBUS_PORT
from GUI.model.stateconf import state_number, CONTEXT
from SDK.modbus.modbusmerge import AbsModeBusModeByAxis, MODENABLE_SIGNAL
from setting.orderset import SETTING
from GUI.model.modecv import ModelCV
from GUI.model.modelop import ModelOp
from PyQt4.QtCore import QObject, pyqtSignal

import logging

from util.threadlock import WorkerQueue

logger = logging.getLogger(__name__)


class StateMixin(object):
    def context_transform_1(self):
        pass

    def context_transform_2(self):
        """"switch to PLAT2"""
        self._modbus.platform_state = "PLAT2"
        self.platform_number = "2"

    def context_transform_3(self):
        pass

    def context_transform_4(self):
        """"switch to PLAT1"""
        self._modbus.platform_state = "PLAT1"
        self.platform_number = "1"

    def context_transform_5(self):
        pass

    def state_all(self, number):
        # self.modbus_up_down(self.squence_number)
        # self.modbus.motor_up_down(str(self.sequence_number + 1))
        self._worker.append(self._modbus.motor_up_down, str(number + 1))
        fun = getattr(self, "context_transform_" + str(number + 1))
        fun()


class Controller(QObject, StateMixin):
    """docstring for Controller"""

    def __init__(self, view):
        super(Controller, self).__init__()
        QObject.__init__(self)
        self._view = view
        self.platform_number = "1"
        self._startModel()
        self._start_modbus()
        self.state_number = state_number()
        self.sequence_number = None
        self._worker = WorkerQueue()

    def show(self):
        self._worker.start()
        self._modelcv.start()
        # self._modelop.start()
        self._view.show()

    def _startModel(self):
        self._modelcv = ModelCV()
        # self._modelop = ModelOp()
        # self._view.getModel(self._modelcv)
        self._view.emit_close_event.connect(self.close)
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
        self._modbus = AbsModeBusModeByAxis(port=MODBUS_PORT)
        self.state_connect()

    def _getAttenuation(self, ):
        length = self._view.fiberLength.text()
        length = float(length)
        self._modelcv.attenuationTest(length)

    def _changeFiberType(self):
        key = str(self._view.fiberTypeBox.currentText())
        SETTING().keyUpdates(key)
        newKey = SETTING().get('fiberType', 'error type')
        # self._view.fiberTypeLabel.setText(newKey)
        self._modelcv.updateClassifyObject(newKey)

    def state_connect(self):
        def state_change():
            self.sequence_number = next(self.state_number)
            self.state_all(self.sequence_number)

            logger.warning("next state" + str(self.sequence_number))

        if hasattr(self._view, "next_state"):
            self._view.next_state.clicked.connect(state_change)
        # move up button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "xstart", 50000))
        self._view.move_up.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "xstart", "stop"))
        self._view.move_up.released.connect(_)
        # move down button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "xstart", 0))
        self._view.move_down.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "xstart", "stop"))
        self._view.move_down.released.connect(_)
        # move right button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "ystart", 50000))
        self._view.move_right.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "ystart", "stop"))
        self._view.move_right.released.connect(_)
        # move left button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "ystart", 0))
        self._view.move_left.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT" + self.platform_number, "ystart", "stop"))
        self._view.move_left.released.connect(_)
        # rest button connection
        self._view.reset.clicked.connect(self._modbus.plat_motor_reset)
        MODENABLE_SIGNAL.connect(self._view.enable_move_button)

    def close(self):
        print("close")
        self._modelcv.exit()
        self._worker.close()
        self._modbus.close()
