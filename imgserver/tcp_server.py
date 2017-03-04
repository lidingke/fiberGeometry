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

    def _on_message(self, data):
        # print data
        data = native_str(data.decode('latin1'))
        logging.info("Received: %s", data)
        if data.strip() == 'getimg' :
            self._writeimg()
        elif data.strip() == 'close':
            logging.info("close img sever")
            self.close()
            # self.io_loop.add_timeout(self.io_loop.time() + timeout, self._on_timeout)

    def _writeimg(self):
        # for i in range(1,5):
        img = randomImg('IMG\\20400\\750\\')
        shape = img.shape
        print 'get img size', shape, img.dtype
        img = img.tostring()

        slicesize = shape[0]
        times = len(img)//slicesize
        emit = {'imgshape':shape,
                'imglen':len(img),
                'imgtimes':times,
                'slicesize':slicesize
        }
        jsonemit = json.dumps(emit)
        print jsonemit
        self.write("%04d"%len(jsonemit))
        self.write(jsonemit)
        # temp = []
        for i in range(0,times):
            cmd = img[i*slicesize:(i + 1)*slicesize]
            # temp.append(cmd)
            self.write(cmd)
        print 'write img len ', len(cmd)
        # temp = ''.join(temp)
        # temp = np.fromstring(temp,dtype='uint8')
        # temp.shape = (1944, 2592, 3)
        # cv2.imshow('temp',temp[::4,::4])
        # cv2.waitKey()
            # time.sleep(0.1)
        # self.write(b'getend'+self.EOF)

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