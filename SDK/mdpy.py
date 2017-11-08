import numpy as np
import cv2
from util.getimg import GetImage, randomImg

import SDK.MindPy as mdp

class GetRawImg(object):
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        try:
            self.hand = mdp.init_camera()
        except Exception as e:
            raise e

    # @timing
    def get(self):
        try:
            md = mdp.get_raw_img()
        except Exception as e:
            raise e
        return self.bayer2BGR(md)

    def bayer2BGR(self, img):
        if not isinstance(img, np.ndarray):
            raise ValueError("bayer2RGB input para error")
        return cv2.cvtColor(img, cv2.COLOR_BAYER_GR2BGR)

    def release_camera(self):
        mdp.uninit_camera()

    def get_camera_serial(self):
        return mdp.get_camera_serial()


def release_camera():
    mdp.uninit_camera()


def get_camera_serial():
    mdp.get_camera_serial()


class GetRawImgTest(GetRawImg):
    def __init__(self, ):
        print ('dynamic get img test')

    def get(self):
        img = randomImg("IMG\\G652\\0912R\\")
        return img

    def release_camera(self):
        pass
