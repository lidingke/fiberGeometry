
import pdb
import numpy as np
import time
import cv2
from pattern.getimg import GetImage
from method.toolkit import timing
# try:
#     import SDK.MindPy.MindPyCEx.MindPy as mdp
# except WindowsError:
#     try:
#         import MindPy.MindPyCEx.MindPy as mdp
#     except WindowsError:
#         import MindPy as mdp
from setting.set import SETTING
import SDK.MindPy as mdp

class GetRawImg(object):
    """docstring for getRawImg"""
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        self.SET = SETTING()
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

    def bayer2RGB(self, img):
        if not isinstance(img, np.ndarray):
            raise ValueError("bayer2RGB input para error")
        return cv2.cvtColor(img, cv2.COLOR_BAYER_GR2RGB)

    def unInitCamera(self):
        mdp.uninitCamera()


class GetRawImgTest(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, ):
        # super(GetRawImgTest, self).__init__()
        print ('test img init')

    def get(self):
        # img = GetImage().get("IMG\\GIOF1\\sig")
        shape = (1944, 2592)
        img = np.fromfile("tests\\data\\imgred.bin", dtype="uint8")
        img.shape = shape
        # print 'get image', img.shape
        time.sleep(0.1)
        return img

    # def bayer2RGB(self, img):
    #     if not isinstance(img, np.ndarray):
    #         raise ValueError("bayer2RGB input para error")
    #     img = cv2.cvtColor(img, cv2.COLOR_BAYER_GB2RGB)
    #     return img

    def unInitCamera(self):
        pass




