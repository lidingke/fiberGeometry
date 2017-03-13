#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from tornado import ioloop, httpclient, gen
from tornado.gen import Task
from tornado.tcpserver import TCPServer
import pdb, time, logging
from tornado import stack_context
from tornado.escape import native_str
from pattern.getimg import randomImg,getImage
import json
import numpy as np
import cv2
import copy
from . import methods
#Init logging
def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))

class MyServer(TCPServer):
    def __init__(self, io_loop=None, **kwargs):
        TCPServer.__init__(self, io_loop=io_loop, **kwargs)
    def handle_stream(self, stream, address):
        self.con = TCPConnection(stream, address, io_loop=self.io_loop)

    def close(self):
        self.con.close()


class TCPConnection(object):

    METHOD_PARA = {'function': 'randomImg', 'para': """\'IMG/G652/pk/\'"""}

    def __init__(self, stream, address, io_loop):
        self.io_loop = io_loop
        self.stream = stream
        self.address = address
        self.address_family = stream.socket.family
        self.EOF = '\n\r'
        self._clear_request_state()
        self._message_callback = stack_context.wrap(self._on_message)
        self.stream.set_close_callback(self._on_connection_close)
        self.stream.read_until(self.EOF, self._message_callback)

    def _on_timeout(self):
        logging.info("Send message..")
        self.write("Hello client! time out" + self.EOF)

    def _getImgMethod(self, function = 'randomImg', para = """\'IMG\\G652\\pk\\\''"""):
        if function not in dir(methods):
            return 'function not found'
        cmd = function+"({})".format(para)
        # logging.info('cmd:',str(cmd))
        print 'cmd:', cmd
        return eval(cmd)

    def _on_message(self, data):
        print data
        data = native_str(data.decode('latin1'))
        logging.info("Received: %s", data)
        data = data.strip()
        if data == 'getimg' :
            self._getImg()
        elif data == 'getbigimg':
            self._getBigImg()
        elif data == 'getimgonce':
            self._getImgOnce()
        elif data[:7] == 'change:':
            self.METHOD_PARA = json.loads(data[7:])
            print 'get change', self.METHOD_PARA
        elif data == 'close':
            logging.info("close img sever")
            self.close()
            # self.io_loop.add_timeout(self.io_loop.time() + timeout, self._on_timeout)

    def _getImgOnce(self):
        img = randomImg("IMG\\G652\\pk\\")
        img = img.tobytes() + b'\n\r'
        print 'write img'
        self.write(img)

    def _getBigImg(self):
        img = randomImg("IMG\\G652\\pk\\")
        img = img.tobytes()
        self.write(img)

    def _getImg(self):
        img = self._getImgMethod(**self.METHOD_PARA)
        print 'getImg', self.METHOD_PARA
        if isinstance(img, str):
            cmd = 'funnotfd'
            self.write(cmd)
        elif isinstance(img, np.ndarray):
            self._writeimg(img)
        else:
            raise ValueError(len(img),type(img))

    def _writeimg(self,img):
        shape = img.shape
        img = img.tobytes()
        slicesize = shape[0]
        times = len(img)//slicesize
        emit = {'imgshape':shape,
                'imglen':len(img),
                'imgtimes':times,
                'slicesize':slicesize
        }
        jsonemit = json.dumps(emit)
        print jsonemit
        self.write("img:%04d"%len(jsonemit))
        self.write(jsonemit)
        for i in range(0,times):
            cmd = img[i*slicesize:(i + 1)*slicesize]
            self.write(cmd)


    def _clear_request_state(self):
        """Clears the per-request state.
        """
        self._write_callback = None
        self._close_callback = None

    def set_close_callback(self, callback):
        """Sets a callback that will be run when the connection is closed.
        """
        self._close_callback = stack_context.wrap(callback)

    def _on_connection_close(self):
        if self._close_callback is not None:
            callback = self._close_callback
            self._close_callback = None
            callback()
        self._clear_request_state()

    def close(self):
        self.stream.close()
        # Remove this reference to self, which would otherwise cause a
        self._clear_request_state()

    def write(self, chunk, callback=None):
        """Writes a chunk of output to the stream."""
        if not self.stream.closed():
            self._write_callback = stack_context.wrap(callback)
            self.stream.write(chunk, self._on_write_complete)

    def _on_write_complete(self):
        if self._write_callback is not None:
            callback = self._write_callback
            self._write_callback = None
            callback()

def main():
    init_logging()
    server = MyServer()
    server.listen(5110)
    ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    try:
        main()
    except Exception, ex:
        print "Ocurred Exception: %s" % str(ex)
        quit()