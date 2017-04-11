#coding:utf-8
from SDK.modbussdk import Translater, DyModeBusMode
from threading import Thread
import serial
import time

class Slave(Thread):
    def __init__(self):
        super(Slave, self).__init__()
        self.ser = serial.Serial('com14', 19200, timeout=0.05, parity= 'E')
        self.RUNNING = True
        self.data = ""
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
                print 'get write'," ".join("{:02x}".format(ord(c)) for c in readed)
                self.ser.write(readed)
                self.data = readed

    def close(self):
        print 'get slave close'
        self.RUNNING = False

def test_modbus():
    d = Translater()
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


def test_move_mode():
    slave = Slave()
    slave.start()
    mod = DyModeBusMode('x', port='com13')
    mod.start(True)
    time.sleep(0.1)
    assert slave.data == mod.data
    cmdline = " ".join("{:02x}".format(ord(c)) for c in slave.data)
    assert cmdline.upper() == '01 10 00 C8 00 06 0C 00 01 00 00 03 E8 00 00 00 C8 00 00 F0 58'
    slave.close()


def ttest_live_move():
    d = DyModeBusMode('x', port='com13')
    d.start(True)
    time.sleep(10)
    d.reversed()
    time.sleep(10)
    d.start(False)

