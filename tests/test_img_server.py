# -*- coding: utf-8 -*-
from tornado import ioloop
# import tornado
from imgserver.tcp_server import MyServer, init_logging
from imgserver.tcp_client import ImgClient
from SDK.mdpy import DynamicGetRawImgTest
import cv2
import numpy as np
import multiprocessing
import time
from pattern.getimg import randomImg
import json
import logging
from threading import Thread
from tornado.testing import AsyncTestCase,gen_test

# server = MyServer()
PORT = 5115

def Server():

    # ioloop.IOLoop.instance().start()
    server = MyServer()
    server.listen(PORT)

    print 'start get img client'

def ttest_getImgOnceMore():
    init_logging()
    Thread(target = Server).start()
    # multiprocessing.Process(target=Server).start()
    DyIMG = DynamicGetRawImgTest(PORT)
    DyIMG.getImgOnce()
    DyIMG.getImgOnce()
    DyIMG.io_loop.start()

def ttest_getImgOncethread():
    init_logging()
    Thread(target=Server).start()
    # multiprocessing.Process(target=Server).start()
    # time.sleep(1)
    # DyIMG = DynamicGetRawImgTest(PORT)
    # DyIMG.getImgOnce()
    # DyIMG.io_loop.start()
    # time.sleep(1)
    para = {'function': 'getImage', 'para': 'IMG/midoc.bmp'}
    # DyIMG.changeImgFunction(para)
    tchange = Thread(target=DynamicGetRawImgTest(PORT).changeImgFunction, args=(para))
    timg = Thread(target=DynamicGetRawImgTest(PORT).getImgOnce)
    time.sleep(1)
    # DyIMG.io_loop.start()
    DyIMG.getImgOnce()
    # time.sleep(1)
    # DyIMG.getImgOnce()
    DyIMG.io_loop.start()
    # DyIMG.close()




class ATestCase(AsyncTestCase):

    def Sever(self):
        server = MyServer(io_loop=self.io_loop)
        server.listen(PORT)

    # @gen_test
    def test_imgOnce(self):
        init_logging()
        Thread(target = Server).start()
        client = ImgClient('localhost', PORT, self.io_loop)
        client.get_img()
        ioloop.IOLoop.instance().start()
        self.wait()

