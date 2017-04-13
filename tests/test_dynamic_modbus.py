#coding:utf-8
from SDK.modbussdk import SendTranslater, DyModeBusMode, ReadTranslater
from threading import Thread
import serial
import struct
import time
from random import randint
import crcmod
from util.function import hex2str

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

class TestUnit():

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
            forrevers = mod.read()
            forrevers = forrevers[2:] + forrevers[:2]
            gets = struct.unpack('>I',forrevers)[0]
            print 'read get no.',x, hex2str(forrevers), gets
            assert gets < 1000
            assert gets > 10


        slave.close()


def Ttest_live_move():
    d = DyModeBusMode('x', port='com4')
    keys = {'start':"True",
            'forward':"True",
            'pulse':10000,
            'frequency':200}
    d.update(keys)
    d.start(True)
    print 'start'
    time.sleep(30)
    print '10s'
    # d.start(False)
    # time.sleep(1)
    keys = {'start':"True",
            'forward':"False",
            'pulse':10000,
            'frequency':200}
    d.update(keys)
    print 'rev'
    # d.start(True)
    time.sleep(30)
    # d.reversed()
    # time.sleep(10)
    print 'stop'
    d.start(False)

