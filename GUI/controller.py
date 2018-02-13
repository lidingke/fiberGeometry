# coding:utf-8
from functools import partial
from time import sleep
from GUI.view.monkey import MonkeyServer
from pattern.classify import classifyObject
from pattern.draw import draw_core_cross
from setting import config
from GUI.model.stateconf import state_number
from SDK.modbus.modbusmerge import AbsModeBusModeByAxis, MODENABLE_SIGNAL
from GUI.model.modelcv import ModelCV
from GUI.model.modelop import ModelOP
import logging
from util.observer import PyTypeSignal
from util.threadlock import WorkerQueue

logger = logging.getLogger(__name__)


class StateMixin(object):
    u"""状态转换管理，管理衰减测试流程中的电机、按钮、界面显示状态"""

    def _start_state(self):
        self.state_number = state_number()
        self._worker = WorkerQueue()
        self.fiber_length_value = None
        self.state_connect()
        self._view.modbus_ui.stateText.setText("    start reboot motos")
        self._view.modbus_ui.next_state.setText("start")

    def state_connect(self):
        u"""先用同步的方式校对状态是否正常"""
        def state_change():
            sequence_number = next(self.state_number)
            # self.state_all(sequence_number)
            logger.warning("next state" + str(sequence_number))
        if hasattr(self._view, "next_state"):
            self._view.next_state.clicked.connect(state_change)
            print "next_state connect"

    def context_transform_1(self):
        self._view.modbus_ui.stateText.setText(u"state 1:获取暗电流，显示夹1图像")
        self._modelop.get_zero()
        # self._view.modbus_ui.stateText.setText("state 1:geted dark current")
        self._view.modbus_ui.next_state.setText("next")
        self._modbus.motor_up_down('1')
        # motor 1down 2up 3up

    def context_transform_2(self):
        """"switch to PLAT2"""
        self._view.modbus_ui.stateText.setText(u"显示夹2图像")
        self._modbus.platform_state = "PLAT2"
        self._modbus.motor_up_down('2')

        # self._view.modbus_ui.stateText.setText("state 2")
        # motor 123

    def context_transform_3(self):
        self._modbus.platform_state = "PLAT1"
        self._view.modbus_ui.stateText.setText(u"卤灯通过夹1耦合进光纤")
        self._modbus.motor_up_down('3')


    def context_transform_4(self):
        """"switch to PLAT1"""
        # self._view.modbus_ui.stateText.setText("state 4:input init current")
        self._modelop.get_before()
        self._view.modbus_ui.stateText.setText(u"state 4:测得第一次光谱")
        self._modbus.platform_state = "PLAT1"
        self._modbus.motor_up_down('4')


    def context_transform_5(self):
        # self._modelop.get_after()
        # self._modelop.calculate_power(25)
        self._view.modbus_ui.stateText.setText(u"state 5:取2m光纤，显示夹2端面，进行几何测试")
        self._modbus.motor_up_down('5')


    def context_transform_6(self):
        self._modelop.get_after()
        if self.fiber_length_value:
            fiber_length = self.fiber_length_value
        else:
            fiber_length = 25
            logging.warning("no fiber length getted")
        self._modelop.calculate_power(fiber_length)
        self._view.modbus_ui.stateText.setText(u"state 6: 获取光谱结果")
        # self._view.modbus_ui.stateText.setText("start reboot motos")
        self._view.modbus_ui.next_state.setText("start")
        self._modbus.motor_up_down('5')


    def state_all(self, number):

        # self.modbus_up_down(self.squence_number)
        # self.modbus.motor_up_down(str(self.sequence_number + 1))
        function_for_transform = getattr(self, "context_transform_" + str(number + 1))
        function_for_transform()
        sleep(1)
        # print("state all", number)
        if number == 5:
            return
        print("state all", number)
        # push_operate_to_worker_queue = self._worker.append
        # push_operate_to_worker_queue(self._modbus.motor_up_down, str(number + 1))


class ModbusControllerMixin(object):
    def _start_modbus(self):
        self._modbus = AbsModeBusModeByAxis(port=config.MODBUS_PORT)
        self._modbus_connect()

    def _modbus_connect(self):
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "xstart", 50000))
        self._view.move_up.pressed.connect(_)
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "xstart", "stop"))
        self._view.move_up.clicked.connect(_)
        # move down button connection
        _ = partial(self._modbus.plat_motor_goto, *("PLAT1", "xstart", 0))
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
        self._view.raw_spect.clicked.connect(self._modelop.get_raw_spectograph_data)
        self._view.fiberLength.textChanged.connect(self._change_fiber_length)
        self.fiber_length_value = float(self._view.fiberLength.text())
        if config.MAMUAL_SPECT_ARGS_FLAG:
            self._spect_args_connect_manual()
        else:
            self._spect_args_connect_auto()

    def _spect_args_connect_auto(self):
        self._view.fiberLength.textChanged.connect.connect(self._modelop.set_spect_args_auto)

    def _spect_args_connect_manual(self):
        self._emit_spect = PyTypeSignal()
        self._emit_spect.connect(self._modelop.set_spect_args_manual)

        def get_spect_args(self):
            spect_args = (self._view.spin_integral_times.value(),
                          self._view.spin_integral_steps.value(),
                          self._view.spin_smoothness.value(),)
            self._emit_spect.emit(*spect_args)

        get_spect_args(self)
        self._view.spin_integral_times.valueChanged.connect(partial(get_spect_args, self))
        self._view.spin_integral_steps.valueChanged.connect(partial(get_spect_args, self))
        self._view.spin_smoothness.valueChanged.connect(partial(get_spect_args, self))

    def _change_fiber_length(self, length):
        try:
            length = float(length)
        except Exception as e:
            self._view.resultShowCV.setText(u"长度输入错误：\n"+unicode(e))
        else:
            self._view.resultShowCV.setText(u"输入长度："+unicode(length)+"m")
        self.fiber_length_value = length
        # print("value change",self.fiber_length_value)

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
        self._modelcv.light_controller.emit_light_ready.connect(partial(self._view.lightControl.setEnabled, True))

        # self._modelcv.returnCoreLight.connect(self._view.getCoreLight)

    def _changeFiberType(self):
        key = str(self._view.fiberTypeBox.currentText())
        self._modelcv.light_controller.update_fibertype(key)
        self._modelcv.updateClassifyObject(key)

    def _start_light_control(self):
        self._view.lightControl.setEnabled(False)
        self._modelcv.light_controller_handle_start()


class OPCVController(ModelCVControllerMixin,
                     ModbusControllerMixin,
                     ModelOPControllerMixin, StateMixin):
    def __init__(self, view):
        super(OPCVController, self).__init__()
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
        self._view.show()

    def close(self):
        logger.error("close controller")
        self._modelcv.close()
        self._worker.close()
        self._modbus.close()
        self._monkey.close()


class AutomaticCVController(ModelCVControllerMixin,
                            ModbusControllerMixin,
                            ModelOPControllerMixin, StateMixin):

    def __init__(self, view):
        super(AutomaticCVController, self).__init__()
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


class CapCVController(ManualCVController):

    def __init__(self, *args, **kwargs):
        super(CapCVController, self).__init__(*args, **kwargs)
        self._modelcv.classify = classifyObject("capillary")
        self._view.cap_diffrange.valueChanged.connect(
            self._modelcv.classify.change_diff_radius
        )

        def model_plot_change(self, value):
            # print self,value
            core = self.classify.frame_core
            plots = draw_core_cross(core, value)
            self.plots.update({"diff_range": plots})

        setattr(self._modelcv, "model_plot_change", partial(model_plot_change, self._modelcv))
        self._view.cap_diffrange.valueChanged.connect(
            self._modelcv.model_plot_change
        )


def get_controller(label):
    if label == "AutomaticCV":
        return AutomaticCVController
    elif label == "ManualCV":
        return ManualCVController
    if label == "OPCV":
        return OPCVController
    if label == "CapCV":
        return CapCVController
    else:
        raise TypeError("no view label correct")
