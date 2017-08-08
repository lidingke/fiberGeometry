import threading

import crcmod
import serial

import logging

from util.function import hex2str

logger = logging.getLogger(__name__)


class SlaveByDelay(threading.Thread):
    def __init__(self, port='com14'):
        super(SlaveByDelay, self).__init__()
        self.ser = serial.Serial(port, 19200, timeout=0.05, parity='E')
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


class Slave(threading.Thread):
    def __init__(self, port='com14'):
        super(Slave, self).__init__()
        self.ser = serial.Serial(port, 19200, timeout=0.05, parity='E')
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

