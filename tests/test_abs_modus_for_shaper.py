
import threading
import random
import serial
import crcmod
import struct
from util.function import hex2str
from  threading import Thread
import time
from SDK.modbusabs import AbsModeBusMode
from pattern.sharper import AbsFocuser
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# h1 = logging.StreamHandler(sys.stdout)
# h1.setLevel(logging.DEBUG)
# h2 = logging.StreamHandler()
# h2.setLevel(logging.DEBUG)
#
# logger.addHandler(h1)
# logger.addHandler(h2)

class Slave(threading.Thread):


    def __init__(self):
        super(Slave, self).__init__()
        self.ser = serial.Serial('com14', 19200, timeout=0.05, parity='E')
        self.RUNNING = True
        self.data_buffer = ""
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')
        self.direction = 30000
        self.get_direction = 0
        self.midpoint = random.randint(30, 80)


    def run(self):
        Thread(target=self._to_dist).start()
        while self.RUNNING:
            try:
                readed = self.ser.read(21)

            except Exception as e:
                raise e
            if readed:
                self.data_buffer = readed
                info = 'slave get buffer ' + " ".join("{:02x}".format(ord(c)) for c in readed)
                logging.info(info)
                if readed[1:2] == '\x10':
                    cmdline = readed[:8]
                    crc = struct.pack('>H', self.crc16(cmdline))
                    cmdline = cmdline + crc[1:] + crc[:1]
                    # print 'get write'," ".join("{:02x}".format(ord(c)) for c in result)
                    self.ser.write(cmdline)
                    value = readed[9:11]
                    # print  " ".join("{:02x}".format(ord(c)) for c in value)
                    # value = value[1:] + value[:1]
                    # print " ".join("{:02x}".format(ord(c)) for c in value)
                    value = struct.unpack('>H', value)[0]
                    # self._goto_direction(value)
                    self.get_direction = value

                elif readed[1:2] == '\x03':
                    for_invert = struct.pack('>I', self.direction)
                    value = for_invert[2:] + for_invert[:2]
                    readed = '\x01\x03\x04' + value
                    crc = struct.pack('>H', self.crc16(readed))
                    readed = readed + crc[1:] + crc[:1]
                    logger.info('slave write' + hex2str(readed))
                    self.ser.write(readed)

    # def _goto_direction(self, dist):
    def _to_dist(self):
        while self.RUNNING:
            time.sleep(0.01)
            if self.direction > self.get_direction:
                next_ = -1
            elif self.direction == self.get_direction:
                next_ = 0
            else:
                next_ = 1
            self.direction = self.direction + next_
        #

    def close(self):
        print 'get slave close'
        self.RUNNING = False
        self.ser.close()


    def get_sharp_direction(self):
        x = self.direction
        if x < 0 :
            x = 0
        elif x > 50000:
            x = 50000
        return (x - self.midpoint) ** 2


def ttest_abs_mode():
    slave = Slave()
    slave.start()
    logger.setLevel(logging.WARN)
    a = AbsModeBusMode('x', 'com13')
    direction = 30500
    a.goto(direction)
    readed = a.location()
    while abs(readed - direction) > 100:
        time.sleep(0.01)
        readed = a.location()
        logger.info('get readed ' + str(readed))
    slave.close()


def test_abs_sharper():

    slave = Slave()
    slave.start()

    a = AbsFocuser('x','com13')
    a.run()
