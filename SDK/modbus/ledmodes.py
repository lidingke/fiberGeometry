import struct
from functools import partial
from collections import OrderedDict,defaultdict
import crcmod
import serial
import logging

from util.function import hex2str

logger = logging.getLogger(__name__)

SAVE_MODES = {True: '\xFF\xFF',
              False: '\x00\x00'}
crc16 = crcmod.predefined.mkCrcFun('modbus')
# Currents = namedtuple('Currents', 'fst sec thd save')


def set_current_cmd(c1st=1, c2st=1, c3st=1, savemode=False):
    """ex:01 10 00 01 00 04 08 00 00 4B B9
     01 10 <2bytes 1st led> <2bytes 2st led> <2bytes 3st led> <save mode FF FF == save><crc>"""
    hpack = partial(struct.pack, '>H')
    values = "".join([hpack(i) for i in (c1st, c2st, c3st)])
    cmd = '\x01\x10\x00\x01\x00\x04\x08' + values + SAVE_MODES[savemode]
    cmd += struct.pack('<H', crc16(cmd))
    return cmd


class LEDMode(object):
    def __init__(self, port):
        super(LEDMode, self).__init__()
        self.ser = serial.Serial(port, baudrate=19200, timeout=0.05, parity='E')
        self.currents = OrderedDict(c1st=1, c2st=1, c3st=1, savemode=False)


    def set_current(self,**kwargs):
        """c1st: first current(INT), c2st:second current(INT), c3st:third current(INT), savemode:BOOL"""
        #c1st=False, c2st=False, c3st=False,savemode=False
        # defaults = defaultdict(False)
        paras_key = ('c1st','c2st','c3st','savemode')
        # paras = {k: False for k in paras_key}
        # paras.update(**kwargs)
        # self.currents.update(**paras)
        for k,v in kwargs.items():
            if k not in paras_key:
                raise  ValueError("error input:"+str(k))
            self.currents[k] = v
        cmd = set_current_cmd(**self.currents)
        logger.info('set current '+hex2str(cmd))
        self.ser.write(cmd)
