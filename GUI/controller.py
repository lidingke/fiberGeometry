# coding:utf-8
# from view import View
import traceback
from functools import partial

import sys

from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPushButton

from GUI.view.monkey import MonkeyServer
from setting.config import MODBUS_PORT
from GUI.model.stateconf import state_number, CONTEXT
from SDK.modbus.modbusmerge import AbsModeBusModeByAxis, MODENABLE_SIGNAL
from setting.parameter import SETTING
from GUI.model.modelcv import ModelCV
from GUI.model.modelop import ModelOP
from PyQt4.QtCore import QObject, pyqtSignal

import logging

from util.observer import PyTypeSignal
from util.threadlock import WorkerQueue

logger = logging.getLogger(__name__)

# QSpinBox

class StateMixin(object):

    def _start_state(self):
        self.state_number = state_number()
        self._worker = WorkerQueue()
        self.state_connect()
        # QLabel.setText()
        self._view.modbus_ui.stateText.setText("start")
        self._view.modbus_ui.next_state.setText("start")


    def state_connect(self):
        def state_change():
            sequence_number = next(self.state_number)
            self.state_all(sequence_number)
            logger.warning("next state" + str(sequence_number))

        if hasattr(self._view, "next_state"):
            self._view.next_state.clicked.connect(state_change)
            print "next_state connect"
        # move up button connection


    def context_transform_1(self):
        # QPushButton.setText()
        self._view.modbus_ui.stateText.setText("state 1")
        self._view.modbus_ui.next_state.setText("next")


    def context_transform_2(self):
        """"switch to PLAT2"""
        self._view.modbus_ui.stateText.setText("state 2:input dark current")
        self._modbus.platform_state = "PLAT2"
        # self._modelop.spect.new()
        self._modelop.get_zero()
        self._view.modbus_ui.stateText.setText("state 2:get dark current")
        # self.platform_number = "2"


    def context_transform_3(self):
        self._view.modbus_ui.stateText.setText("state 3:input init current")
        self._modelop.get_before()
        self._view.modbus_ui.stateText.setText("state 3:get init current")


    def context_transform_4(self):
        """"switch to PLAT1"""
        self._modbus.platform_state = "PLAT1"
        self._view.modbus_ui.stateText.setText("state 4")
        self._view.modbus_ui.next_state.setText("end")


        # self.platform_number = "1"

    def context_transform_5(self):
        self._modelop.get_after()
        self._modelop.calculate_power(25)
        self._view.modbus_ui.stateText.setText("start")
        self._view.modbus_ui.next_state.setText("start")




    def state_all(self, number):
        # self.modbus_up_down(self.squence_number)
        # self.modbus.motor_up_down(str(self.sequence_number + 1))
        push_operate_to_worker_queue = self._worker.append
        push_operate_to_worker_queue(self._modbus.motor_up_down, str(number + 1))
        function_for_transform = getattr(self, "context_transform_" + str(number + 1))
        function_for_transform()



class ModbusControllerMixin(object):
    def _start_modbus(self):
        self._modbus = AbsModeBusModeByAxis(port=MODBUS_PORT)
        self._modbus_connect()

    def _modbus_connect(self):
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "xstart", 50000))
        self._view.move_up.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "xstart", "stop"))
        self._view.move_up.released.connect(_)
        # move down button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1" , "xstart", 0))
        self._view.move_down.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "xstart", "stop"))
        self._view.move_down.released.connect(_)
        # move right button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "ystart", 50000))
        self._view.move_right.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "ystart", "stop"))
        self._view.move_right.released.connect(_)
        # move left button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "ystart", 0))
        self._view.move_left.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "ystart", "stop"))
        self._view.move_left.released.connect(_)
        # rest button connection
        self._view.reset.clicked.connect(self._modbus.plat_motor_reset)
        MODENABLE_SIGNAL.connect(self._view.enable_move_button)


class ModelOPControllerMixin(object):

    def _start_modelop(self):
        self._modelop = ModelOP()
        self._modelop.emit_spect.connect(self._view.opplot.update_figure)
        self._spect_args_connect()

    def _spect_args_connect(self):
        self._emit_spect = PyTypeSignal()
        self._emit_spect.connect(self._modelop.set_spect_args)

        def get_spect_args(self):
            spect_args = (self._view.spin_integral_times.value(),
                          self._view.spin_integral_steps.value(),
                          self._view.spin_smoothness.value(),)
            self._emit_spect.emit(*spect_args)
        get_spect_args(self)
        self._view.spin_integral_times.valueChanged.connect(partial(get_spect_args,self))
        self._view.spin_integral_steps.valueChanged.connect(partial(get_spect_args,self))
        self._view.spin_smoothness.valueChanged.connect(partial(get_spect_args,self))




class ModelCVControllerMixin(object):
    def _start_modelcv(self):
        self._modelcv = ModelCV()

        self._view.emit_close_event.connect(self.close)
        self._view.beginTestCV.clicked.connect(self._modelcv.mainCalculate)
        self._view.fiberTypeBox.currentIndexChanged.connect(self._changeFiberType)

        self._view.emit_fibertype_in_items.connect(self._changeFiberType)
        self._view.lightControl.clicked.connect(self._start_light_control)

        self._modelcv.returnImg.connect(self._view.updatePixmap)
        self._modelcv.resultShowCV.connect(self._view.updateCVShow)
        self._modelcv.emit_relative_index.connect(self._view.relative_index_show)
        self._modelcv.light_controller.emit_light_ready.connect(partial(self._view.lightControl.setEnabled,True))

        # self._modelcv.returnCoreLight.connect(self._view.getCoreLight)

    def _changeFiberType(self):
        key = str(self._view.fiberTypeBox.currentText())

        # newKey = SETTING().get('fiberType', 'error type')
        # self._view.fiberTypeLabel.setText(newKey)
        self._modelcv.light_controller.update_fibertype(key)

        self._modelcv.updateClassifyObject(key)

    def _start_light_control(self):
        self._view.lightControl.setEnabled(False)
        self._modelcv.light_controller_handle_start()


class OPCVController(ModelCVControllerMixin,
                            ModbusControllerMixin,
                            ModelOPControllerMixin,StateMixin):
    """docstring for Controller"""

    def __init__(self, view):
        super(OPCVController, self).__init__()
        # QObject.__init__(self)
        self._view = view
        self._start_modelcv()
        self._start_modelop()
        self._start_modbus()
        self._start_state()
        self._monkey = MonkeyServer(self)

    def show(self):
        self._worker.start()
        self._modelcv.start()
        self._monkey.start()
        # self._modelop.start()
        self._view.show()

    def close(self):
        logger.error("close controller")
        self._modelcv.close()
        self._worker.close()
        self._modbus.close()
        self._monkey.close()


class AutomaticCVController(ModelCVControllerMixin,
                            ModbusControllerMixin,
                            ModelOPControllerMixin,StateMixin):
    """docstring for Controller"""

    def __init__(self, view):
        super(AutomaticCVController, self).__init__()
        # QObject.__init__(self)
        self._view = view
        self._start_modelcv()
        self._start_modelop()
        self._start_modbus()
        self._start_state()
        self._monkey = MonkeyServer(self)

    def show(self):
        self._worker.start()
        self._modelcv.start()
        self._monkey.start()
        # self._modelop.start()
        self._view.show()

    def close(self):
        logger.error("close controller")
        self._modelcv.close()
        self._worker.close()
        self._modbus.close()
        self._monkey.close()

class ManualCVController(ModelCVControllerMixin,
                    ModelOPControllerMixin):
    """docstring for Controller"""

    def __init__(self, view):
        super(ManualCVController, self).__init__()
        # QObject.__init__(self)
        self._view = view
        # self.platform_number = "1"
        self._start_modelcv()

    def show(self):
        self._modelcv.start()
        self._view.show()

    def close(self):
        logger.error("close controller")
        self._modelcv.close()
        # logger.error(traceback.format_exception(*sys.exc_info()))



def get_controller(label):
    if label == "AutomaticCV":
        return AutomaticCVController
    elif label == "ManualCV":
        return ManualCVController
    if label == "OPCV":
        return OPCVController
    else:
        raise TypeError("no view label correct")
