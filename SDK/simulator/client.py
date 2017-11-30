from __future__ import print_function

import socket

from setting import config
from setting.config import SIMULATOR_IMG_SERVER_COFIG
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.tcpclient import TCPClient
from tornado.options import options, define
import numpy as np
import json
import cv2
import time
from threading import Thread
from functools import partial
import logging
logger = logging.getLogger(__name__)


define("host", default="localhost", help="TCP server host")
define("portc", default=9888, help="TCP port to connect to")
define("message", default="getimgonce", help="Message to send")
port = 9880

class Client(object):

    def __init__(self, host = False, port = False):
        shost, sport, smethod, spath = config.SIMULATOR_IMG_SERVER_COFIG

        if not host :
            host = shost
        if not port:
            port = sport
        self.host = host
        self.port = port

    @gen.coroutine
    def get_img_once(self):
        # print (self.host,self.port)
        stream = yield TCPClient().connect(self.host,self.port)
        logging.info('img connect on port:{}'.format(self.port))
        yield stream.write(("getimgonce" + "\n\r").encode())
        logging.info('img send')
        data = yield stream.read_until(b"\n\r\n\r")
        stream.close()
        # rawdata = np.frombuffer(data.strip(), dtype=np.uint8)
        raise gen.Return(data[:-4])

    @gen.coroutine
    def get_change(self,para):
        stream = yield TCPClient().connect(self.host,self.port)
        cmd = 'change:' + json.dumps(para) + '\n\r'
        yield stream.write((cmd).encode())
        stream.close()

    @gen.coroutine
    def close_server(self):
        stream = yield TCPClient().connect(self.host,self.port)
        yield stream.write(("close" + "\n\r").encode())
        stream.close()



class SharpClient(object):
    def __init__(self, host='localhost', port=9880):
        self.host = host
        self.port = port

    @gen.coroutine
    def get_sharp(self):
        stream = yield TCPClient().connect(self.host, self.port)
        logging.info('img connect')
        yield stream.write(("getsharp:" + "\n\r").encode())
        logging.info('img send')
        data = yield stream.read_until("\n\r\n\r")
        stream.close()
        # rawdata = np.frombuffer(data.strip(), dtype=np.uint8)
        raise gen.Return(data)


    @gen.coroutine
    def start_motor(self):
        stream = yield TCPClient().connect(self.host,self.port)
        yield stream.write(("start:" + "\n\r").encode())
        stream.close()

    @gen.coroutine
    def turn_back(self):
        stream = yield TCPClient().connect(self.host,self.port)
        yield stream.write(("back:" + "\n\r").encode())
        stream.close()

    @gen.coroutine
    def send_close(self):
        stream = yield TCPClient().connect(self.host,self.port)
        yield stream.write(("close" + "\n\r").encode())
        stream.close()





