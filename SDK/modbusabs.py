from .modbussdk import mutex_lock, ReadTranslater
from .cmd import direction, read_direction, abs_direction
import crcmod
import time
import serial
import struct
import logging
from collections import deque
from util.function import hex2str
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class SendTranslater(object):
    def __init__(self):
        self.axies = ('x', 'y', 'z')
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, axies, cmd):
        logger.info("send translater called")
        if axies not in self.axies:
            raise KeyError('axis input error')
        first = abs_direction[axies]

        if not cmd:
            cmdline = '\x01\x10' \
                      + first \
                      + '\x00\x01\x02' \
                      + '\x00\x00'
            crc = struct.pack('>H', self.crc16(cmdline))
            cmdline = cmdline + crc[1:] + crc[:1]
            return cmdline
        elif isinstance(cmd, int):
            for_invert = struct.pack('>H', cmd)
            value = for_invert[2:] + for_invert[:2]

            cmdline = '\x01\x10'\
                + first\
                + '\x00\x02\x04\x00\x01'\
                + value
            crc = struct.pack('>H',self.crc16(cmdline))
            cmdline = cmdline + crc[1:] + crc[:1]
            return cmdline
        else:
            raise ValueError('input parameter error')




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
        self.direction = self.location() or 3000
        self.queue = deque(maxlen=15)

    @mutex_lock
    def goto(self, direction):
        self.direction = direction
        send = self.send_translater(self.axis, self.direction)
        logger.info('mode send cmd'+" ".join("{:02x}".format(ord(c)) for c in send))
        self.ser.write(send)
        self.data_buffer = self._read_untill_data_in('\x10')

        # readed = self.location()
        # while abs(readed-direction) > 100:
        #     time.sleep(0.1)
        #     readed = self.location()
        #     logger.info('get readed ' + str(readed))

    # @mutex_lock
    # def _write_direction(self, send):
    #     send = self.send_translater(self.axis, self.direction)
    #     logger.info('mode send cmd'+" ".join("{:02x}".format(ord(c)) for c in send))
    #     self.ser.write(send)
    #     self.data_buffer = self._read_untill_data_in('\x10')

    def scram(self):
        send = self.send_translater(self.axis, False)
        logger.info('send stop cmd'+" ".join("{:02x}".format(ord(c)) for c in send))
        self.ser.write(send)
        self.data_buffer = self._read_untill_data_in('\x10')

    @mutex_lock
    def location(self):
        read = self.read_translater(self.axis)
        info = 'mode send cmd '+" ".join("{:02x}".format(ord(c)) for c in read)
        logger.info(info)
        self.ser.write(read)

        self.data_buffer = self._read_untill_data_in('\x03')
        info = 'mode get cmd '+" ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        logger.info(info)
        if len(self.data_buffer) < 6:
            debug = "error " + " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
            logger.debug(debug)
            raise ModbusConnectionException("data buffer length error")
        print 'master get cmd ', " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        reversed = self.data_buffer[3:-2]
        if reversed:
            _ = struct.unpack('>I', reversed[2:] + reversed[:2])[0]
            return _
        # return None

    # def _read_by_length(self):
    #     head = self.ser.read(3)
    #     if not head:
    #         return None
    #     length = struct.unpack('>b', head[2:3])[0]
    #     readed = self.ser.read(length*2 + 2)
    #     result = head + readed
    #     logger.info('read by length'+hex2str(result))
    #     return result

    def _read_untill_data_in(self, mode = '\x03'):
        IS = True
        while IS:
            _0 = self.ser.read(1)
            if _0 != '\x01':
                continue
            _1 = self.ser.read(1)
            if _1 == '\x03':
                _2 = self.ser.read(1)
                length = struct.unpack('>b', _2)[0]
                readed = self.ser.read(length * 2 + 2)
                return '\x01\x03' + _2 + readed
            elif _1 == '\x10':
                return '\x01\x03'+self.ser.read(6)
            else:
                raise ValueError('bad input data')



class ModbusConnectionException(ValueError):
    def __init__(self,*args,**kwargs):
        super(ModbusConnectionException, self).__init__()