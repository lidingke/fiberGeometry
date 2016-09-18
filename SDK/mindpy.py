from ctypes import *
import pdb
import numpy as np
import time
import cv2
from method.tookit import timing
try:
    mydll = CDLL('MindPy/ConsoleMindPy/ConsoleMindPy/MindPy.dll')
except WindowsError:
    mydll = CDLL('SDK/MindPy/ConsoleMindPy/ConsoleMindPy/MindPy.dll')


print mydll




class GetImg(object):
    """docstring for GetImg"""
    def __init__(self, ):
        super(GetImg, self).__init__()
        # self.arg = arg

    def getImg(self):
        limit = 2592*2048*3
        ctypeArray = c_byte * limit
        arget = ctypeArray()
        hand = mydll.InitCameraPlay()
        md = mydll.GetOneImg(arget, limit, hand)
        npArray = np.array(arget, dtype=np.uint8)
        npArray = npArray.reshape(2048, 2592, 3)

        return npArray

class GetRawImg(object):
    """docstring for getRawImg"""
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        self.limit = 2592*1944
        ctypeArray = c_byte * self.limit
        self.arget = ctypeArray()
        self.hand = mydll.InitCameraPlay()
        # print 'init end', self.limit, self.arget, self.hand

    @timing
    def get(self):

        md = mydll.GetRawImg(self.arget, self.limit, self.hand)

        npArray = np.array(self.arget, dtype=np.uint8)
        npArray = npArray.reshape(1944, 2592)
        return npArray
