from .modbussdk import mutex_lock, ReadTranslater
from .cmd import direction, read_direction
import crcmod
import serial
import struct


class SendTranslater(object):
    def __init__(self):
        self.axies = ('x', 'y', 'z')
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, axies, abs_direction):

        if axies not in self.axies:
            raise KeyError('axis input error')
        if not isinstance(abs_direction, int):
            raise ValueError('directions type error', type(abs_direction))
        for_invert = struct.pack('>I', abs_direction)
        value = for_invert[2:] + for_invert[:2]
        first = direction[axies]
        cmdline = '\x01\x03'\
            + first\
            + '\x00\x01\x02'\
            + value\
            + '\x00\x02'
        crc = struct.pack('>H',self.crc16(cmdline))
        cmdline = cmdline + crc[1:] + crc[:1]
        return cmdline



class AbsModeBusMode(object):

    def __init__(self, axis, port = None, baudrate = 19200, store = None):
        super(AbsModeBusMode, self).__init__()
        self.IsWriting = True
        self.ser = serial.Serial(port, baudrate, timeout=0.05, parity='E')
        self.data_buffer = None
        # self.forward = False
        self.axis = axis
        self.send_translater = SendTranslater()
        self.read_translater = ReadTranslater()
        self.direction = self.read_pulse or 3000

    def goto(self, direction):
        self.direction = direction
        self._write(self.direction)


    @mutex_lock
    def _write(self,send):
        send = self.send_translater(self.axis, self.direction)
        print 'mode send cmd', " ".join("{:02x}".format(ord(c)) for c in send)
        self.ser.write(send)
        len_ = len(send)
        try:
            self.data_buffer = self.ser.read(len_)
            # print 'getcmd'," ".join("{:02x}".format(ord(c)) for c in self.data)
        except serial.SerialException as e:
            #01 10 00 c8 00 06 c1 f5 right
            #01 90 .. error
            raise e

        # return self.data

    @mutex_lock
    def read_pulse(self):
        read = self.read_translater(self.axis)
        print 'mode read cmd', " ".join("{:02x}".format(ord(c)) for c in read)
        self.ser.write(read)
        len_ = len(read)
        try:
            self.data_buffer = self.ser.read(len_+2)
        except Exception as e:
            raise e
        if self.data_buffer:
            if len(self.data_buffer) < 6:
                raise ModbusConnectionException("data buffer length error")
            print 'master get cmd', " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
            reversed = self.data_buffer[3:-2]
            if reversed:
                _ = struct.unpack('>I', reversed[2:] + reversed[:2])[0]
                return _
        return None


class ModbusConnectionException(ValueError):
    def __init__(self):
        super(ModbusConnectionException, self).__init__()