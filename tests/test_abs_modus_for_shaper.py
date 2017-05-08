import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import threading
import random
import serial
import crcmod
import struct
from util.function import hex2str
from util.observer import MySignal
from  threading import Thread
import time
from SDK.modbusabs import AbsModeBusMode
from pattern.sharper import AbsFocuser
import sys


class Slave(threading.Thread):

    sharp_return = MySignal()
    def __init__(self, ):
        super(Slave, self).__init__()
        self.ser = serial.Serial('com14', 19200, timeout=0.05, parity='E')
        self.RUNNING = True
        self.data_buffer = ""
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')
        self.direction = 30000
        self.get_direction = 0
        self.midpoint = 25000#random.randint(30, 80)
        logger.warning("dist = " + str(self.midpoint))


    def run(self):
        Thread(target=self._to_dist).start()
        Thread(target=self.emit_sharp).start()
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
                    warning = "get direct {} {}".format( self.direction, self.get_direction)
                    logger.warning(warning)
        self.ser.close()

    # def _goto_direction(self, dist):
    def _to_dist(self):
        while self.RUNNING:
            time.sleep(0.001)
            if self.direction > self.get_direction:
                next_ = -1
            elif self.direction == self.get_direction:
                next_ = 0
            else:
                next_ = 1
            # warning = "get nex_ {} {} {}".format(next_,self.direction,self.get_direction)
            # logger.warning(warning)
            self.direction = self.direction + next_
        #

    def emit_sharp(self):
        while self.RUNNING:
            time.sleep(1)
            self.sharp_return.emit(self.get_sharp_direction())


    def close(self):
        print 'get slave close'
        self.RUNNING = False
        # self.ser.close()


    def get_sharp_direction(self):
        x = self.direction
        if x < 0 :
            x = 0
        elif x > 50000:
            x = 50000
        return (x - self.midpoint) ** 2

class TestOnline():
    def test_abs_mode(self):
        logger.setLevel(logging.DEBUG)
        print 'goto direction'
        a = AbsModeBusMode('x', 'com4')
        direction = 35000

        a.goto(direction)
        readed = a.location()
        while abs(readed - direction) > 3:
            time.sleep(0.01)
            readed = a.location()
            logger.info('get readed ' + str(readed))

    def ttest_abs_sharper(self):
        a = AbsFocuser('x','com4')
        # slave.sharp_return.connect(a.get_sharp)
        a.run()
        # slave.close()

class TTestOffline():

    def test_abs_mode(self):
        slave = Slave()
        slave.start()
        logger.setLevel(logging.WARN)
        a = AbsModeBusMode('x', 'com13')
        direction = 35000
        a.goto(direction)
        readed = a.location()
        while abs(readed - direction) > 100:
            time.sleep(0.01)
            readed = a.location()
            logger.info('get readed ' + str(readed))
        slave.ser.close()
        a.ser.close()
        slave.close()


    def Ttest_abs_sharper(self):

        slave = Slave()
        slave.start()
        a = AbsFocuser('x','com13')
        slave.sharp_return.connect(a.get_sharp)
        a.run()
        a.mode.ser.close()
        slave.close()
