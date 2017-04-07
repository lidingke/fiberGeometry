#encoding:utf-8
from SDK.modbussdk import ModBusMode
from threading import Thread
import serial
import time
from SDK.cmd import cmds, cmdscrc
from pattern.sharper import Focuser
try:
    import crcmod
except ImportError as e:
    print e
    Iscrcmod = False
else:
    Iscrcmod = True


class Slave(Thread):
    def __init__(self):
        super(Slave, self).__init__()
        self.ser = serial.Serial('com14', 19200, timeout=0.05, parity= 'E')
        self.RUNNING = True
        self.data = ""
        print self.ser.parity

    def run(self):
        while self.RUNNING:
            readed = self.ser.read(8)
            if readed:
                print 'get write'," ".join("{:02x}".format(ord(c)) for c in readed)
                self.ser.write(readed)
                self.data = readed

    def close(self):
        print 'get slave close'
        self.RUNNING = False


"""test port com15 connect cm16"""
def test_mode():
    slave = Slave()
    slave.start()
    mod = ModBusMode('com13')
    mod.run()
    time.sleep(0.05)
    assert slave.data != ""
    assert mod.data != ""
    assert mod.data == slave.data
    mod.run('x', 'clicked', '1')
    time.sleep(0.05)
    assert slave.data != ""
    assert mod.data != ""
    assert mod.data == cmdscrc['xclicked1']
    assert mod.data == slave.data
    slave.close()
    # mod.close()


def test_print():
    for k,cmd in cmds.items():
        print " ".join("{:02x}".format(ord(c)) for c in cmd)


def test_get_crc():
    if Iscrcmod:
        crc16 = crcmod.predefined.mkCrcFun('modbus')
        for k,v in cmds.items():
            crccode = hex(crc16(v))
            if len(crccode) <6:
                crccode = crccode[:2]+'0'+crccode[2:]
            print '\\x{}\\x{}'.format(crccode[-4:-2], crccode[-2:])

            print " ".join("{:02x}".format(ord(c)) for c in v), crccode
            assert "".join("{:02x}".format(ord(c)) for c in cmdscrc[k][-2:]) == crccode[-2:]+crccode[-4:-2]


def ttest_move():
    md = ModBusMode('com4')
    print 'send'
    md.run('x', 'clicked', '0')
    time.sleep(30)
    md.run('x', 'release', '0')
    time.sleep(1)
    md.run('x', 'clicked', '1')
    time.sleep(30)
    md.run('x', 'release', '1')


def ttest_focuser():
    focus = Focuser()
    focus.run()

