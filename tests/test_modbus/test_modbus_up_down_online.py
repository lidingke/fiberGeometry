from SDK.modbus.directions import MOTOR_STATE
from SDK.modbus.modbusmerge import AbsModeBusModeByAxis


def test_modebusmerge():
    mode = AbsModeBusModeByAxis(port='com13')
    mode.plat_motor_goto("PLAT1", 'x1', 'xstart', 35000)