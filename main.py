import cv2
import numpy as np
import pdb
import sys
import os

from method.toolkit import Cv2ImShow

from method.edgedetect import Canny
from method.edgedetect import Threshold
from method.edgedetect import ErodeDilate

from method.contour import findContours
from method.contour import HoughCircles



class Flow(object):
    """docstring for Flow"""
    def __init__(self, file):
        super(Flow, self).__init__()
        # self.arg = arg
        self.file = file
        self.img = cv2.imread(self.file)
        self.origin = self.img.copy()
        self.show = Cv2ImShow()

    def flow(self,):
        img = self.img
        self.show.show('origin', img[::2,::2])
        img = ErodeDilate().run(img)
        # img = Canny().run(img)

        self.show.show('edge', img[::2,::2])
        # img, result , contours , tree = findContours().run(img)
        # self.show.show('contour', result[::2,::2])
        img = HoughCircles().run(img)
        self.show.show('contour', img[::2,::2])


class TraverseFolder(object):
    """docstring for TraverseFolder"""
    def __init__(self, folder):
        super(TraverseFolder, self).__init__()
        self.folder = folder

    def traverse(self):
        for file in os.listdir(self.folder):
            flow = Flow(self.folder + "\\" + file)
            flow.flow()

if __name__ == '__main__':
    tr = TraverseFolder(folder = 'VT')
    tr.traverse()
