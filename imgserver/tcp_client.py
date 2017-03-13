#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from tornado import ioloop, httpclient, gen
from tornado.gen import Task
import pdb, time, logging
import tornado.ioloop
import tornado.iostream
import socket
import numpy as np
from PyQt4.QtCore import QObject, pyqtSignal
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

class ImgClient(QObject):
    returnImg = pyqtSignal(object)

    def __init__(self, host, port, io_loop=None):
        QObject.__init__(self)
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

    def get_img(self):
        self.get_stream()
        self.stream.connect((self.host, self.port), self.send_message)

    def send_message(self):
        logging.info("Send message 1....")
        self.stream.write("getimgonce" + self.EOF)
        self.stream.read_until(self.EOF, self.on_receive)

        logging.info("After send 1....")

    def on_receive(self, data):
        assert isinstance(data, str)
        if data[-2:] == self.EOF:
            data = data[:-2]
        img = np.frombuffer(data, dtype=np.uint8)
        print 'getimg size', img.shape
        if img.shape[0] == 15116544:
            img.shape = (1944, 2592, 3)
        self.returnImg.emit(img)

        # cv2.imshow('img', img)
        # cv2.waitKey()
            # self.imgs.append(img)

    def set_shutdown(self):
        self.shutdown = True


def main():
    init_logging()
    io_loop = tornado.ioloop.IOLoop.instance()
    c2 = ImgClient("127.0.0.1", 8011, io_loop)
    # c2.connect()
    c2.get_img()
    # c2.set_shutdown()
    logging.info("**********************start ioloop******************")
    io_loop.start()
    c2.get_img()
    # c2.set_shutdown()
    logging.info("**********************start ioloop******************")
    io_loop.start()



if __name__ == "__main__":
    main()