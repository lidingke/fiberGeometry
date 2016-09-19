from ctypes import *
import pdb
import numpy as np
import time
import cv2
from method.toolkit import timing
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
        limit = 2592*1944*3
        ctypeArray = c_byte * limit
        arget = ctypeArray()
        hand = mydll.InitCameraPlay()
        md = mydll.GetOneImg(arget, limit, hand)
        npArray = np.array(arget, dtype=np.uint8)
        npArray = npArray.reshape(1944, 2592, 3)
        return npArray

class GetRawImg(object):
    """docstring for getRawImg"""
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        self.limit = 2592*1944
        ctypeArray = c_byte * self.limit
        self.arget = ctypeArray()
        self.hand = mydll.InitCameraPlay()
        print 'init end', self.limit, self.arget, self.hand

    # @timing
    def get(self):
        """ get 0.0990002155304 s
            get raw dll 0.0910000801086 s
            create np.array 0.00600004196167 s
            reshape 0s
        """
        try:
            md = mydll.GetRawImg(self.arget, self.limit, self.hand)
        except Exception, e:
            raise e

        npArray = np.array(self.arget, dtype=np.uint8)
        npArray = npArray.reshape(1944, 2592)
        # print 'nparray ', npArray.shape
        return npArray


class IsInitCamera(object):
    """docstring for InitCamera"""
    def __init__(self, ):
        super(IsInitCamera, self).__init__()
        # self.arg = arg


    def isInit(self):
        hand = mydll.InitCameraPlay()
        mydll.UninitCamera(hand)
        if hand:
            return True
        else:
            return False



