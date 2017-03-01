#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from tornado import ioloop, httpclient, gen
from tornado.gen import Task
import pdb, time, logging
import tornado.ioloop
import tornado.iostream
import socket
import numpy as np
import cv2
#Init logging
def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))

class TCPClient(object):
    def __init__(self, host, port, io_loop=None):
        self.host = host
        self.port = port
        self.io_loop = io_loop
        self.shutdown = False
        self.stream = None
        self.sock_fd = None
        self.EOF = b'\n\r'
        self.imgs = []

    def get_stream(self):
        self.sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.stream = tornado.iostream.IOStream(self.sock_fd)
        self.stream.set_close_callback(self.on_close)



    def on_close(self):
        if self.shutdown:
            self.io_loop.stop()


    def connect(self):
        self.get_stream()
        self.stream.connect((self.host, self.port), self.send_message)

    def send_message(self):
        logging.info("Send message 1....")
        self.stream.write(b"cmd:getimg" + self.EOF)
        self.stream.read_until(self.EOF, self.on_receive)
        logging.info("After send 1....")

    def on_receive(self, data):
        assert isinstance(data, str)
        if len(data) <100:
            if data.strip() == 'getend':
                print 'get ended', len(self.imgs)
                self.showimgs()
                self.on_close()
                return
        if data[-2:] == self.EOF:
            data = data[:-2]
        img = np.fromstring(data, dtype=np.uint8)
        # pdb.set_trace()
        print 'getimg size', img.shape
        if img.shape[0] == 15116544:
            img.shape = (1944, 2592, 3)
            self.imgs.append(img)
        self.stream.read_until(self.EOF, self.on_receive)
        # self.on_close()

    def set_shutdown(self):
        self.shutdown = True

    def showimgs(self):
        if self.imgs:
            for img in self.imgs:
                cv2.imshow('img', img[::4,::4])
                cv2.waitKey()

def main():
    init_logging()
    io_loop = tornado.ioloop.IOLoop.instance()
    c2 = TCPClient("127.0.0.1", 8001, io_loop)
    c2.connect()
    c2.set_shutdown()
    logging.info("**********************start ioloop******************")
    io_loop.start()
    
if __name__ == "__main__":
    try:
        main()
    except Exception, ex:
        print "Ocurred Exception: %s" % str(ex)
        quit()