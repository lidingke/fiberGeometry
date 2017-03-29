import serial
from .cmd import cmdscrc as  cmds



class ModBusMode(object):

    def __init__(self, port = 'com1', baudrate = 19200, ):
        self.IsWriting = True
        self.ser = serial.Serial(port,baudrate,timeout=0.05, parity= 'E')
        self.axies = ('x', 'y', 'z')
        self.forwards = ('0','1')
        self.clickstatus = ('clicked','release')
        self.data = ""

    def run(self, No = 'x', click = 'clicked',forward = '0'):

        if self.IsWriting:
            self.IsWriting = False
            if No not in self.axies:
                raise ValueError('axis No. error', No, type(No))
            if click not in self.clickstatus:
                raise ValueError('click status error', click, type(click))
            if forward not in self.forwards:
                raise ValueError('forward error', forward, type(forward))

            cmd = No + click + forward
            if cmd not in cmds.keys():
                raise ValueError('cmd error',cmd,type(cmd))
            # try:
            send = cmds[cmd]
            # print 'send cmd'," ".join("{:02x}".format(ord(c)) for c in send)
            self.ser.write(send)
            try:
                self.data = self.ser.read(8)
                # print 'getcmd'," ".join("{:02x}".format(ord(c)) for c in self.data)
            except serial.SerialException as e:
                print e
            self.IsWriting = True


    # def close(self):
    #     print 'get modbus close'
    #     self.IsWriting = False










