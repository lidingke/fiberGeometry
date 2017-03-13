# -*- coding: utf-8 -*-
from tornado import ioloop
from imgserver.tcp_server import MyServer, init_logging
from imgserver.tcp_client import ImgClient
from SDK.mdpy import DynamicGetRawImgTest
import cv2
import numpy as np
import multiprocessing
import time
from pattern.getimg import randomImg
import json
from threading import Thread

server = MyServer()

def Server():
    init_logging()
    # server = MyServer()
    server.listen(5110)
    ioloop.IOLoop.instance().start()
    print 'start get img client'



def ntest_img_get():
    # multiprocessing.Process(target=server).start()
    Thread(target = Server).start()
    time.sleep(1)
    DyIMG = DynamicGetRawImgTest(5110)
    print time.time()
    img = DyIMG.get()
    print time.time()
    assert img.shape == (1944, 2592, 3)
    assert img.dtype == 'uint8'
    kwargs = {'function' : 'getImage', 'para' : """\'IMG/midoc.BMP\'"""}
    # DyIMG.changeImgFunction(kwargs)
    # print time.time()
    # img = DyIMG.get()
    # print time.time()
    # DyIMG.getBigImg()
    # cv2.imshow('img', img[::4,::4])
    # cv2.waitKey()
    DyIMG.closeSever()
    # server.close()
    ioloop.IOLoop.instance().stop()
    ioloop.IOLoop.instance().close()
    #
    # cv2.imshow('img', img[::4,::4])
    # cv2.waitKey()

def test_getImgOnce():
    Thread(target = Server).start()
    # time.sleep(1)
    DyIMG = DynamicGetRawImgTest(5110)
    def getImg(img):
        print 'getImg def',img.shape
    DyIMG.imgclient.returnImg.connect(getImg)
    DyIMG.getImgOnce()


    DyIMG.closeSever()
    # server.close()
    ioloop.IOLoop.instance().stop()
    ioloop.IOLoop.instance().close()