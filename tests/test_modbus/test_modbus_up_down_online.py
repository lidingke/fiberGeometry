from time import sleep
import threading

import crcmod
import serial

from GUI.model.stateconf import state_number
from SDK.modbus.directions import MOTOR_STATE
from SDK.modbus.modbusmerge import AbsModeBusModeByAxis
from util.function import hex2str
import logging

logger = logging.getLogger(__name__)


class Slave(threading.Thread):
    def __init__(self, port='com14'):
        super(Slave, self).__init__()
        self.ser = serial.Serial(port, 19200, timeout=0.5, parity='E')
        self.RUNNING = True
        self.data_buffer = ""
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def run(self):
        while self.RUNNING:
            readed = self.ser.read(50)
            # print('readed'+readed)
            if readed:
                self.data_buffer = readed
                logger.info('slave get buffer ' + hex2str(readed))

    def close(self):
        self.RUNNING = False
        self.ser.close()


def ttest_modebusmerge_x1_runs():
    logging.basicConfig(level=logging.INFO)
    mode = AbsModeBusModeByAxis(port='com4')
    mode.plat_motor_goto("PLAT2", 'zstart', 50000)
    sleep(3)
    mode.plat_motor_goto("PLAT2", 'zstart', 'stop')
    sleep(0.1)
    mode.plat_motor_goto("PLAT2", 'zstart', 0)
    sleep(3)
    mode.plat_motor_goto("PLAT2", 'zstart', 'stop')

def test_modebusmerge_up_down_state_trans():
    logging.basicConfig(level=logging.INFO)
    mode = AbsModeBusModeByAxis(port='com4')
    state = state_number()
    for i in xrange(3):
        s = str(next(state)+1)
        logger.info("state get "+s)
        mode.motor_up_down(str(s))


def Ttest_modebusmerge_x1_runs_on_slave():
    logging.basicConfig(level=logging.INFO)
    slave = Slave()
    slave.start()
    mode = AbsModeBusModeByAxis(port='com13')
    mode.plat_motor_goto("PLAT1", 'xstart', 50000)
    sleep(1)
    print('databuffer' + hex2str(slave.data_buffer))
    mode.plat_motor_goto("PLAT1", 'xstart', 'stop')
    mode.plat_motor_goto("PLAT1", 'xstart', 0)
    sleep(1)
    mode.plat_motor_goto("PLAT1", 'xstart', 'stop')
    mode.close()
    slave.close()
