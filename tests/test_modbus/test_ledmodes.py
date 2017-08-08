import threading
import logging
from time import sleep

from util.serialslaves import SlaveByDelay

logger = logging.getLogger(__name__)
import crcmod
import serial

from SDK.modbus.ledmodes import set_current_cmd, LEDMode
from util.function import hex2str


def test_set_online():
    logging.basicConfig(level=logging.INFO)
    mode = LEDMode('com4')
    # for i in range(10):
    mode.set_current(c1st=800, c2st=500, c3st=100, savemode=True)
        # sleep(3)
        # mode.set_current(c1st=300, c2st=100, c3st=100)
        # sleep(3)


def test_set_current_cmd():
    cmd = set_current_cmd(0, 0, 0)
    assert hex2str(cmd).upper() == "01 10 00 01 00 04 08 00 00 00 00 00 00 00 00 4B B9"


def test_LEDMode_offline():
    logging.basicConfig(level=logging.INFO)
    slave = SlaveByDelay()
    slave.start()
    mode = LEDMode('com13')
    mode.set_current(c1st=1, c2st=2, c3st=3)
    sleep(0.1)
    assert hex2str(slave.data_buffer[7:13]) == '00 01 00 02 00 03'
    mode.set_current(c1st=3)
    sleep(0.1)
    assert hex2str(slave.data_buffer[7:13]) == '00 03 00 02 00 03'
    mode.set_current(c3st=4, savemode=True)
    sleep(0.1)
    assert hex2str(slave.data_buffer[7:15]).upper() == '00 03 00 02 00 04 FF FF'
    print(hex2str(slave.data_buffer[7:15]))
    sleep(0.1)
    slave.close()
