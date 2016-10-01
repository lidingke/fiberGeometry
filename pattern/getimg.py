import cv2
import os

import numpy as np
from pattern.meta import CV2MethodSet

class GetImage(CV2MethodSet):
    """docstring for GetImage"""
    def __init__(self, ):
        super(GetImage, self).__init__()
        # self.arg = arg

    def get(self, dir_=''):
        if dir_.find('.') > 0:
            self.singleFileFind(dir_)
        else :
            self.fileFind(dir_)

    def singleFileFind(self, dir_):
        for file in os.listdir(dir_):
            self.img = cv2.imread(file)
            self.origin = self.img.copy()

    def fileFind(self, dir_):
        self.img = cv2.imread(dir_)
