import pdb
import numpy as np
import time
import cv2
from pattern.getimg import GetImage, randomImg
import json
# try:
#     import SDK.MindPy.MindPyCEx.MindPy as mdp
# except WindowsError:
#     try:
#         import MindPy.MindPyCEx.MindPy as mdp
#     except WindowsError:
#         import MindPy as mdp
from setting.orderset import SETTING
from PyQt4.QtCore import QObject
import SDK.MindPy as mdp
import socket
import tornado
# from imgserver.tcp_client import ImgClient

class GetRawImg(object):
    """docstring for getRawImg"""
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        self.SET = SETTING()
        self.limit = 2592*1944
        # if self.SET.get("ifcamera", False):
        try :
            self.hand = mdp.initCamera()
        except Exception as e:
            raise e


    # @timing
    def get(self):
        try:
            # md = mdp.getRawImg(self.limit)
            md = mdp.getRawImg()
            # ValueError: get raw image error: -12

        except Exception, e:
            raise e

        npArray = md.reshape(1944, 2592)
        npArray = self.bayer2BGR(npArray)
        return npArray

    def bayer2BGR(self, img):
        if not isinstance(img, np.ndarray):
            raise ValueError("bayer2RGB input para error")
        # if len(img.shape) == 3:
        #     return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return cv2.cvtColor(img, cv2.COLOR_BAYER_GR2BGR)

    def unInitCamera(self):
        mdp.uninitCamera()

    def getSerialNumber(self):
        return  mdp.getCameraSerial()

def releaseCamera():
    mdp.uninitCamera()

def getSerialNumber():
    mdp.getCameraSerial()


# class DynamicGetRawImgTest(GetRawImg):
#     """docstring for getRawImg"""
#     def __init__(self, port = 5110):
#         # super(GetRawImgTest, self).__init__()
#         print ('test img init')
#         import socket
#         self.EOF = '\n\r'
#         self.port = port
#         self.host = 'localhost'
#         self.io_loop = tornado.ioloop.IOLoop.current()
#         # self.io_loop = tornado.ioloop.IOLoop.current()
#
#         self.img = None
#
#
#     # def getBigImg(self):
#     #     self.ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #     self.ser.connect((self.host, self.port))
#     #     self.ser.sendall("getbigimg\n\r")
#     #     img = self.ser.recv(15116544)
#     #     print len(img)
#     #
#     # def get(self):
#     #     self.ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #     self.ser.connect((self.host, self.port))
#     #     self.ser.sendall("getimg\n\r")
#     #     length = self.ser.recv(8).strip()
#     #     if length[:4] != 'img:':
#     #         raise ValueError('error',length)
#     #     jsonget = self.ser.recv(int(length[4:]))
#     #     jsonget = json.loads(jsonget)
#     #     times = jsonget['imgtimes']
#     #     slicesize = jsonget['slicesize']
#     #     imgs = []
#     #     print time.time()
#     #     for i in range(0,times):
#     #         recved = self.ser.recv(slicesize)
#     #         # assert slicesize == len(recved)
#     #         print 'recv', len(recved)
#     #         imgs.append(recved)
#     #     imgs = b''.join(imgs)
#     #     img = np.frombuffer(imgs,dtype='uint8')
#     #     if img.shape[0] == 15116544:
#     #         img.shape = (1944, 2592, 3)
#     #     print img.shape
#     #     return img
#
#     def getImgOnce(self):
#         imgclient = ImgClient(self.host, self.port, self.io_loop)
#         imgclient.get_img()
#         # io_loop.start()
#
#
#     def changeImgFunction(self,kwargs):
#         imgclient = ImgClient(self.host, self.port, self.io_loop)
#         # self.ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # self.ser.connect((self.host, self.port))
#         cmd = 'change:'
#         # para = {'function' : 'randomImg', 'para' : """\'IMG/G652/pk/\'"""}
#         cmd = cmd+json.dumps(kwargs) +self.EOF
#         # self.ser.sendall(cmd)
#         print 'write cmd ', cmd
#         imgclient.change_method(cmd)
#
#     def unInitCamera(self):
#         pass
#
#     # def close(self):
#     #     self.imgclient.close_server()
#     #     self.imgclient.on_close()
#     #     self.io_loop.stop()
#     #     self.io_loop.close()
#         # self.ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # self.ser.connect((self.host, self.port))
#         # self.ser.sendall("close\n\r")



class GetRawImgTest(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, ):
        # super(GetRawImgTest, self).__init__()
        print ('dynamic get img test')

    def get(self):
        img = randomImg("IMG\\G652\\pk\\")
        # img = randomImg("IMG\\105125\\OC\\")
        # img = randomImg("IMG\\10130\\nonecore\\")
        return img

    def unInitCamera(self):
        pass