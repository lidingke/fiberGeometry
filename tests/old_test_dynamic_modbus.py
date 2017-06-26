#coding:utf-8
from SDK.modbussdk import SendTranslater, DyModeBusMode, ReadTranslater

from threading import Thread
import multiprocessing
import serial
import struct
import time
from random import randint
import crcmod
from util.function import hex2str
from SDK.modbusabs import SendTranslater as AbsSendTranslater
from SDK.modbusabs import AbsModeBusMode
import logging
logger = logging.getLogger(__name__)

class Slave(Thread):
    def __init__(self):
        super(Slave, self).__init__()
        self.ser = serial.Serial('com14', 19200, timeout=0.05, parity= 'E')
        self.RUNNING = True
        self.data_buffer = ""
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')
        print self.ser.parity

    def run(self):
        while self.RUNNING:
            try:
                readed = self.ser.read(21)
            # except serial.SerialTimeoutException:
            #     pass
            except Exception as e:
                raise e
            if readed:
                self.data_buffer = readed
                print 'buffer', " ".join("{:02x}".format(ord(c)) for c in readed)
                if readed[1:2] == '\x10':
                    cmdline = readed[:8]
                    crc = struct.pack('>H', self.crc16(cmdline))
                    cmdline = cmdline + crc[1:] + crc[:1]
                    # print 'get write'," ".join("{:02x}".format(ord(c)) for c in result)
                    self.ser.write(cmdline)

                elif readed[1:2] == '\x03':

                    for_invert = struct.pack('>I', randint(10,1000))
                    value =  for_invert[2:] + for_invert[:2]

                    cmdline = '\x01\x03\04' + value
                    crc = struct.pack('>H', self.crc16(cmdline))
                    cmdline = cmdline + crc[1:] + crc[:1]
                    print 'get write', " ".join("{:02x}".format(ord(c)) for c in cmdline)
                    self.ser.write(cmdline)

    def close(self):
        print 'get slave close'
        self.RUNNING = False

class tTestUnit():

    def test_send_translater(self):
        d = SendTranslater()
        keys = {'axis':'x',
                'start':"True",
                'forward':"False",
                'pulse':1000,
                'frequency':200}
        cmdline = d(**keys)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == '01 10 00 C8 00 06 0C 00 01 00 00 03 E8 00 00 00 C8 00 00 F0 58'

        keys = {'axis':'x',
                'forward':"False"}
        cmdline = d(**keys)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == '01 10 00 C9 00 01 02 00 00 B7 C9'

        keys = {'axis':'x',
                'pulse':1000}
        cmdline = d(**keys)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == '01 10 00 CA 00 02 04 03 E8 00 00 FF F0'

        keys = {'axis':'x',
                'frequency':200}
        cmdline = d(**keys)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == '01 10 00 CC 00 02 04 00 C8 00 00 7E 54'

        keys = {'axis': 'x',
                'start': 'True'}
        cmdline = d(**keys)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == '01 10 00 C8 00 01 02 00 01 77 D8'


    def test_read_translater(self):
        d = ReadTranslater()
        cmdline = d('x')
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == '01 03 40 AA 00 02 F1 EB'

    def test_move_mode(self):
        slave = Slave()
        slave.start()
        mod = DyModeBusMode('x', port='com13')
        mod.start(True)
        time.sleep(0.1)
        assert slave.data_buffer[:8] == mod.data_buffer[:8]
        # cmdline = " ".join("{:02x}".format(ord(c)) for c in slave.data_buffer)
        cmdline = hex2str(slave.data_buffer)
        assert cmdline.upper() == '01 10 00 C8 00 06 0C 00 01 00 00 03 E8 00 00 00 C8 00 00 F0 58'
        assert slave.data_buffer[9:11] == '\x00\x00'
        mod.reversed()
        assert slave.data_buffer[9:11] == '\x00\x01'
        mod.start(False)
        time.sleep(0.1)
        assert slave.data_buffer[7:9] == '\x00\x00'
        for x in range(10):
            time.sleep(0.1)
            gets = mod.read_pulse()
            if gets:

                print 'read get no.',x,  gets
                assert gets < 1000
                assert gets > 10


        slave.close()
        slave.ser.close()
        mod.ser.close()

class tTestUnitDynamic():

    def read_sleep(self,d,times = 30):
        for x in range(30):
            time.sleep(1)
            get = d.location()
            print 'sleep time', x, get

    def test_live_move(self,):
        d = DyModeBusMode('x', port='com4')
        keys = {'start':"True",
                'forward':"True",
                'pulse':10000,
                'frequency':200}
        d.update(keys)
        d.start(True)
        print 'start'
        # time.sleep(10)
        self.read_sleep(d,10)
        print '10s'
        d.start(False)
        # time.sleep(1)
        keys = {'start':"True",
                'forward':"False",
                'pulse':10000,
                'frequency':200}
        d.update(keys)
        print 'rev'
        d.start(True)

        d.reversed()
        self.read_sleep(d, 10)
        # time.sleep(10)
        print 'stop'
        d.start(False)

class AbsSlave(Thread):
    def __init__(self):
        super(AbsSlave, self).__init__()
        self.ser = serial.Serial('com14', 19200, timeout=0.05, parity= 'E')
        self.RUNNING = True
        self.data_buffer = ""
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')
        print self.ser.parity
        self.direction = 3000

    def run(self):
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
                    value = struct.unpack('>H',value)[0]
                    self._goto_direction(value)

                elif readed[1:2] == '\x03':
                    for_invert = struct.pack('>I', self.direction)
                    value =  for_invert[2:] + for_invert[:2]
                    readed = '\x01\x03\x04' + value
                    crc = struct.pack('>H', self.crc16(readed))
                    readed = readed + crc[1:] + crc[:1]
                    logger.info('slave write'+hex2str(readed))
                    self.ser.write(readed)

    def _goto_direction(self, dist):
        def _to_dist(self):
            start = self.direction
            print "start thread", start,dist,xrange(start, dist,1 if start < dist else -1)
            for x in xrange(start, dist, 1 if start < dist else -1):
                time.sleep(0.01)
                self.direction = x
        Thread(target=_to_dist, args=(self,)).start()

    def close(self):
        print 'get slave close'
        self.RUNNING = False



class TestAbs():


    def test_translate(self):

        s = AbsSendTranslater()
        cmdline = s('x',35000)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == "01 10 00 C8 00 02 04 00 01 88 B8 C9 EB"
        cmdline = s('x',False)
        cmdline = " ".join("{:02x}".format(ord(c)) for c in cmdline)
        assert cmdline.upper() == "01 10 00 C8 00 01 02 00 00 B6 18"

    def test_live_mode(self):
        logger.setLevel(logging.ERROR)
        slave = AbsSlave()
        slave.start()
        a = AbsModeBusMode('x', 'com13')
        print 'init direction', a.direction
        direction = 2500
        a.goto(direction)
        readed = a.location()
        while abs(readed-direction) > 100:
            time.sleep(0.01)
            readed = a.location()
            logger.info('get readed ' + str(readed))
        slave.close()
