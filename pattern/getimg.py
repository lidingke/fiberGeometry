import cv2
import os
import pdb
import numpy as np
from pattern.meta import CV2MethodSet

class GetImage(CV2MethodSet):
    """docstring for GetImage"""
    def __init__(self, ):
        super(GetImage, self).__init__()
        # self.arg = arg
        self.img = False

    def get(self, dir_=''):
        if dir_.find('.') > 0:
            self.singleFileFind(dir_)
        else :
            self.fileFind(dir_)
        return self.img

    def fileFind(self, dir_):
        for file in os.listdir(dir_):
            # pdb.set_trace()
            self.img = cv2.imread(dir_ + "\\" + file)
            self.origin = self.img.copy()
            if len(self.img.shape) == 3:
                self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)



    def singleFileFind(self, dir_):
        self.img = cv2.imread(dir_)
        self.origin = self.img.copy()
        if len(self.img.shape) == 3:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)

