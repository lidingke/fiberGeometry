import cv2
import numpy as np
import pdb
import sys
import os

from method.toolkit import Cv2ImShow

from method.edgedetect import Canny
from method.edgedetect import Threshold
from method.edgedetect import ErodeDilate
from method.edgedetect import CloseOpen

from method.contour import findContours
from method.contour import HoughCircles
from method.contour import FitEllipse


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
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = ErodeDilate().run(img)
        self.show.show('edge', img[::2,::2])
        # img, result , contours , tree, treeList = findContours().run(img)
        img, result, contours, tree, treeList = findContours().run(img)
        self.show.show('result', result[::2,::2])
        origin = FitEllipse().run(self.origin, result, contours, treeList)
        self.show.show('ellipse', origin[::2,::2])

    # def flowTest(self,):
    #     img = self.img
    #     self.show.show('origin', img[::2,::2])
    #     gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #     # pdb.set_trace()
    #     gray32 = np.int32(gray)
    #     self.show.show('origin', gray[::2,::2])
    #     cv2.watershed(img,gray32)
    #     self.show.show('origin', gray32[::2,::2])



class TraverseFolder(object):
    """docstring for TraverseFolder"""
    def __init__(self, folder):
        super(TraverseFolder, self).__init__()
        self.folder = folder

    def traverse(self):
        for file in os.listdir(self.folder):
            flow = Flow(self.folder + "\\" + file)
            flow.flow()
            # flow.flowTest()

if __name__ == '__main__':
    tr = TraverseFolder(folder = 'VT')
    tr.traverse()
