import struct
from collections import deque, OrderedDict
from threading import Thread
from time import sleep

import serial
import crcmod

from SDK.modbus.directions import HEAD_DIR, MOTOR_GROUP, START_STOP,\
    UP_DOWN, MOTOR_STATE, STATION_DIR
import logging

from util.hexs import hex2str
from util.observer import PyTypeSignal
from util.threadlock import mutex
from setting.config import MODBUS_PORT
logger = logging.getLogger(__name__+":"+str(MODBUS_PORT))


class SendTranslater(object):
    def __init__(self):
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, station, head_dir, move):
        station = STATION_DIR[station]
        if head_dir not in HEAD_DIR.keys():
            raise ValueError("head direction error")
        head_dir = HEAD_DIR[head_dir]

        if isinstance(move, str):
            if move in ('start', 'stop'):
                result = self._dimension_motor_by_str(station, head_dir, move)
            elif move in '12345':
                result = self._up_down_motor(station, head_dir, move)
            elif move == 'rest':
                result = self._rest_motor(station, head_dir, move)
            else:
                raise ValueError("error move command")
        elif isinstance(move, int):
            result = self._dimension_motor_by_int(station, head_dir, move)
        else:
            raise ValueError('error command type')

        result += struct.pack('<H', self.crc16(result))
        return result

    # def _get_station(self, station):
    #     if station in MOTOR_GROUP[0]:
    #         return '\x01'
    #     elif station in MOTOR_GROUP[1]:
    #         return '\x02'
    #     else:
    #         raise ValueError("station code error")

    def _dimension_motor_by_str(self, station, head_dir, move):
        if move == 'start':
            move = START_STOP[0]
        else:
            move = START_STOP[1]
        cmd = station + '\x10' + head_dir + '\x00\x01\x02' + move
        return cmd

    def _dimension_motor_by_int(self, station, head_dir, move):
        for_invert = struct.pack('>I', move)
        move = for_invert[2:]
        cmd = station + '\x10' + head_dir + '\x00\x02\x04' + START_STOP[0] + move
        return cmd

    def _up_down_motor(self, station, head_dir, move):
        move = struct.pack('>H', int(move))
        cmd = station + '\x10' + '\x00\xdc' + '\x00\x01\x02' + move
        return cmd

    def _rest_motor(self, station, head_dir, move):
        cmd = station + '\x10' + HEAD_DIR['rest'] + '\x00\x01\x02' + '\x00\x02'
        return cmd


class ReadTranslater(object):
    def __init__(self):
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, head_dir, size=1):
        assert head_dir in HEAD_DIR.keys()
        size = struct.pack('>H', size)
        cmdline = '\x01\x03' + HEAD_DIR[head_dir] + size
        crc = struct.pack('<H', self.crc16(cmdline))
        cmdline = cmdline + crc
        return cmdline

class ReturnParse(object):

    def __init__(self):
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, method ,cmd):
        if method == "up_down_state":
            return self._up_down_state(cmd)

    def _up_down_state(self, cmd):
        cmd = struct.unpack('>H',cmd[3:5])[0]
        return cmd

MODENABLE_SIGNAL = PyTypeSignal()

def enable_move(fun):

    def inner(*args,**kwargs):
        MODENABLE_SIGNAL.emit(False)
        result = fun(*args,**kwargs)
        MODENABLE_SIGNAL.emit(True)
        return result
    return inner

class AbsModeBusModeByAxis(object):
    def __init__(self, port=None, baudrate=19200, store=None):
        super(AbsModeBusModeByAxis, self).__init__()
        # print port,type(port)
        # if isinstance(port,unicode):
        #     port = port.encode("utf-8")
        logger.error("motor com:{} {}".format(port,baudrate))
        self.ser = serial.Serial(port, baudrate, timeout=0.05, parity='E')
        # self.forward = False
        self.send_translater = SendTranslater()
        self.read_translater = ReadTranslater()
        self.return_parse = ReturnParse()
        self._platform_state = None
        self.RUNNING = True
        self.timeout_times = 0

    # @enable_move
    def plat_motor_goto(self, station, head_dir, move):
        if self._platform_state:
            station = self._platform_state
        # state = self._platform_state
        # station = STATION_DIR[state]
        # assert station in MOTOR_STATE[state]
        print station, head_dir, move
        cmd = self.send_translater(station, head_dir, move)
        logger.info('mode send cmd' + hex2str(cmd))
        self.ser.write(cmd)

    # @enable_move
    def plat_motor_reset(self):
        cmd = self.send_translater('PLAT1', 'xstart', 'rest')
        logger.info('mode send cmd' + hex2str(cmd))
        self.ser.write(cmd)

    # @mutex
    @enable_move
    def motor_up_down(self, move='1'):
        assert isinstance(move, str)
        cmd = self.send_translater('UP_DOWN', 'xstart', move)
        logger.error('mode send cmd' + hex2str(cmd))
        self.ser.write(cmd)
        self.timeout_times = 0
        while self.RUNNING:
            sleep(0.1)
            self.ser.write(self.read_translater('up1'))
            sleep(0.1)
            readed = self.ser.read(7)
            self.timeout_times +=1
            if self.timeout_times == 20:
                logger.debug("modbus recieved time out")
                self.timeout_times = 0
                break
            if readed:
                if len(readed) == 7:
                    result = self.return_parse('up_down_state', readed)
                    if result == 1:
                        logger.error("finished motor")
                        self.timeout_times = 0
                        break
                else:
                    self.ser.flushInput()


    def close(self):
        self.RUNNING = False
        sleep(0.5)
        self.ser.close()

    @property
    def platform_state(self):
        return self._platform_state

    @platform_state.setter
    def platform_state(self,value):
        assert value in MOTOR_STATE.keys()
        print "plat", value, MOTOR_STATE.keys()
        self._platform_state = value

        # def goto(self, direction, axis='x'):
        #     self.direction = direction
        #     send = self.send_translater(axis, self.direction)
        #     logger.info('mode send cmd' + " ".join("{:02x}".format(ord(c)) for c in send))
        #     self.ser.write(send)
        #     self.data_buffer = self._read_untill_data_in('\x10')
        #
        # def scram(self, axis):
        #     send = self.send_translater(axis, False)
        #     logger.info('send stop cmd' + " ".join("{:02x}".format(ord(c)) for c in send))
        #     self.ser.write(send)
        #     self.data_buffer = self._read_untill_data_in('\x10')
        #
        # # @mutex_lock
        # def location(self, axis):
        #     logger.debug("lod ing location")
        #     read = self.read_translater(axis)
        #     info = 'mode send cmd ' + " ".join("{:02x}".format(ord(c)) for c in read)
        #     logger.debug(info)
        #     self.ser.write(read)
        #
        #     self.data_buffer = self._read_untill_data_in('\x03')
        #     # info = 'mode get cmd '+" ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        #     logger.debug(info)
        #     if len(self.data_buffer) < 6:
        #         debug = "error " + " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        #         logger.debug(debug)
        #         raise ModbusConnectionException("data buffer length error")
        #     # print 'master get cmd ', " ".join("{:02x}".format(ord(c)) for c in self.data_buffer)
        #     reversed = self.data_buffer[3:-2]
        #     if reversed:
        #         _ = struct.unpack('>I', reversed[2:] + reversed[:2])[0]
        #         # print 'get _', _
        #         return _
        #         # return None
        #
        # def _read_untill_data_in(self, mode='\x03'):
        #     IS = True
        #     while IS:
        #         _0 = self.ser.read(1)
        #         if _0 != '\x01':
        #             continue
        #         _1 = self.ser.read(1)
        #         if _1 == '\x03':
        #             _2 = self.ser.read(1)
        #             length = struct.unpack('>b', _2)[0]
        #             readed = self.ser.read(length * 2 + 2)
        #             return '\x01\x03' + _2 + readed
        #         elif _1 == '\x10':
        #             return '\x01\x03' + self.ser.read(6)
        #         else:
        #             raise ValueError('bad input data')

# class ModbusWorker(Thread):
#
#     mode = False
#
#     def __init__(self,port):
#         super(ModbusWorker, self).__init__()
#         self.mode = AbsModeBusModeByAxis(port)
#         self.RUNNING = True
#         self.gens = self.gen()
#         next(self.gens)
#
#     def run(self):
#
#         self.gen()
#
#     def gen(self):
#         while self.RUNNING:
#             fun = yield
#             fun()
#
#     def plat_motor_goto(self,*args,**kwargs):
        # pass

