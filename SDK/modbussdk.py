#encoding:utf-8
import serial
from .cmd import cmdscrc as  cmds
from .cmd import direction
import crcmod
import struct
from collections import OrderedDict
from util.load import MetaDict
from functools import wraps


def unwrite(func):
    IS_RUNNING = [True,]
    @wraps(func)
    def inner(*args, **kwargs):
        # print 'get R',IS_RUNNING[0], id(IS_RUNNING)
        if IS_RUNNING[0]:
            IS_RUNNING[0] = False
            try:
                func(*args, **kwargs)
            except Exception as e:
                IS_RUNNING[0] = True
                raise e
            IS_RUNNING[0] = True
    return inner



class ModBusMode(object):

    def __init__(self, port = 'com1', baudrate = 19200, ):
        self.IsWriting = True
        self.ser = serial.Serial(port, baudrate, timeout=0.05, parity= 'E')
        self.axies = ('x', 'y', 'z')
        self.forwards = ('0','1')
        self.clickstatus = ('clicked','release')
        self.data = ""


    @unwrite
    def run(self, No = 'x', click = 'clicked',forward = '0'):

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

    # def close(self):
    #     print 'get modbus close'
    #     self.IsWriting = False


# class DyModeBusMode(object):
class Translater(object):
    def __init__(self):
        self.axies = ('x', 'y', 'z')
        self.move = OrderedDict([('start',''),
                ('forward',''),
                ('pulse',''),
                ('frequency','')])
        self.move_len = OrderedDict([('start',1),
                ('forward',1),
                ('pulse',2),
                ('frequency',2)])
        self.binary_dict = {"True":'\x00\x01',"False":'\x00\x00'}
        self.crc16 = crcmod.predefined.mkCrcFun('modbus')

    def __call__(self, *args, **kwargs):
        if not hasattr(kwargs,'axis'):
            KeyError('need axis parameter',)
        movekeys = set(kwargs.keys()) and set(direction.keys())
        if not movekeys:
            KeyError('need move parameter')
        move_items = OrderedDict()
        for x in self.move.keys():
            _ = kwargs.get(x,'')
            if _:
                move_items[x] = _

        value, num, byte = self._order_pack_cmd(move_items)
        dir0 = self._cmd_len_right(kwargs.get('axis'), move_items)
        cmdline = ''.join(['\x01\x10', dir0, num, byte, value])
        crc = struct.pack('>H',self.crc16(cmdline))
        cmdline = cmdline + crc[1:] + crc[:1]
        print '\n'+" ".join("{:02x}".format(ord(c)) for c in cmdline)
        return cmdline

    def _cmd_len_right(self, axis, move_items):
        startkey = axis + move_items.keys()[0]
        endkey = axis + move_items.keys()[-1]
        dir0 = direction[startkey]
        dir1 = direction[endkey]
        total = struct.unpack('>H', dir1)[0] \
                - struct.unpack('>H', dir0)[0] \
                + self.move_len[endkey[1:]]
        total_len = sum([self.move_len[x] for x in move_items.keys()])
        if total is not total_len:
            raise AssertionError("cmd len error {} {}".format(total,total_len))
        return dir0


    def _order_pack_cmd(self, move_items):
        value = []
        num = 0
        if 'start' in move_items.keys():
            value.append(self.binary_dict[move_items['start']])
            num = num + 1
        if 'forward' in move_items.keys():
            value.append(self.binary_dict[move_items['forward']])
            num = num + 1
        if 'pulse' in move_items.keys():
            for_invert = struct.pack('>I', move_items['pulse'])
            value = value + [for_invert[2:], for_invert[:2]]
            num = num + 2
        if 'frequency' in move_items.keys():
            for_invert = struct.pack('>I', move_items['frequency'])
            value = value + [for_invert[2:], for_invert[:2]]
            num = num + 2
        byte = struct.pack('>I', num * 2)[-1:]
        num = struct.pack('>I', num)[-2:]
        if not num:
            raise ValueError('unenough move cmd')
        value = "".join(value)
        return value, num, byte


class DyModeBusMode(MetaDict):

    def __init__(self, axis, port = None, baudrate = 19200, store = None):
        super(DyModeBusMode, self).__init__()
        self.IsWriting = True
        self.ser = serial.Serial(port, baudrate, timeout=0.05, parity='E')
        self.data = None
        self.forward = True
        self.axis = axis
        self.translater = Translater()
        self.store = {'start': "True",
                 'forward': "False",
                 'pulse': 1000,
                 'frequency': 200}
        if store:
            self.store.update(store)


    def start(self, bool_):
        if bool_:
            self.store['start'] = "True"
        else:
            self.store['start'] = "False"
        print self.store
        self._write()

    def reversed(self):
        self.forward = not self.forward
        if self.forward:
            self.store['start'] = "True"
        else:
            self.store['start'] = "False"
        self._write()

    @unwrite
    def _write(self):
        send = self.translater(axis = self.axis, **self.store)
        self.ser.write(send)
        len_ = len(send)
        print 'len', len_
        try:
            self.data = self.ser.read(len_)
            # print 'getcmd'," ".join("{:02x}".format(ord(c)) for c in self.data)
        except serial.SerialException as e:
            raise e

        # return self.data
