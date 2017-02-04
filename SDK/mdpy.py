
import pdb
import numpy as np
import time
import cv2
from pattern.getimg import GetImage, randomImg

# try:
#     import SDK.MindPy.MindPyCEx.MindPy as mdp
# except WindowsError:
#     try:
#         import MindPy.MindPyCEx.MindPy as mdp
#     except WindowsError:
#         import MindPy as mdp
from setting.orderset import SETTING
import SDK.MindPy as mdp

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


class GetRawImgTest(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, ):
        # super(GetRawImgTest, self).__init__()
        print ('test img init')

    def get(self):
        # img = GetImage().get("IMG\\GIOF1\\sig")
        # shape = (1944, 2592)
        # img = np.fromfile("tests\\data\\imgred.bin", dtype="uint8")
        # img.shape = shape
        # time.sleep(0.1)
        img = randomImg("IMG\\20400corec\\750\\")
        print 'change rgb'
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img

    # def bayer2RGB(self, img):
    #     if not isinstance(img, np.ndarray):
    #         raise ValueError("bayer2RGB input para error")
    #     img = cv2.cvtColor(img, cv2.COLOR_BAYER_GB2RGB)
    #     return img

    def unInitCamera(self):
        pass


class GetRawImgTest20400(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, ):
        # super(GetRawImgTest, self).__init__()
        print ('test img init')

    def get(self):
        time.sleep(0.1)
        img = randomImg("IMG\\20400coreb\\750\\")
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img

    def unInitCamera(self):
        pass

class GetRawImgTestg652(GetRawImg):
    """docstring for getRawImg"""
    def __init__(self, ):
        # super(GetRawImgTest, self).__init__()
        print ('test img init')

    def get(self):
        time.sleep(0.1)
        img = randomImg("IMG\\g652\\")
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img

    def unInitCamera(self):
        pass