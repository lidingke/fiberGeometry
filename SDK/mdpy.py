
import pdb
import numpy as np
import time
import cv2
from pattern.getimg import GetImage, yieldImg
from method.toolkit import timing
# try:
#     import SDK.MindPy.MindPyCEx.MindPy as mdp
# except WindowsError:
#     try:
#         import MindPy.MindPyCEx.MindPy as mdp
#     except WindowsError:
#         import MindPy as mdp
from setting.orderset import SETTING
from pattern.getimg import randomImg
import SDK.MindPy as mdp

class GetRawImg(object):
    """docstring for getRawImg"""
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        self.SET = SETTING({})
        self.limit = 2592*1944
        # if self.SET.get("ifcamera", False):
        self.hand = mdp.initCamera()


    # @timing
    def get(self):
        """ get 0.0990002155304 s
            get raw dll 0.0910000801086 s
            create np.array 0.00600004196167 s
            reshape 0s
        """
        try:
            # md = mdp.getRawImg(self.limit)
            md = mdp.getRawImg()
            # ValueError: get raw image error: -12

        except Exception, e:
            raise e

        npArray = md.reshape(1944, 2592)
        return npArray

    def bayer2BGR(self, img):
        if not isinstance(img, np.ndarray):
            raise ValueError("bayer2RGB input para error")
        if len(img.shape) == 3:
            return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return cv2.cvtColor(img, cv2.COLOR_BAYER_GR2BGR)

    def unInitCamera(self):
        mdp.uninitCamera()


class GetRawImgTest(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, ):
        # super(GetRawImgTest, self).__init__()
        print ('test img init')

    def get(self):
        # img = GetImage().get("IMG\\GIOF1\\sig")
        # img = np.fromfile("tests\\data\\dynamicimg1.bin", dtype="uint8")
        # img.shape = (1944, 2592)
        # print 'get image', img.shape
        # time.sleep(0.1)
        return self.dynamicGet()

    def dynamicGet(self):
        return randomImg("IMG\\octagon\\D500\\")
        # return yieldImg("IMG\\octagon\\D500")


    # def bayer2RGB(self, img):
    #     if not isinstance(img, np.ndarray):
    #         raise ValueError("bayer2RGB input para error")
    #     img = cv2.cvtColor(img, cv2.COLOR_BAYER_GB2RGB)
    #     return img

    def unInitCamera(self):
        pass




