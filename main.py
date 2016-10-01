
#MindVision pixel size = 4.8 um,
#MindVision pixel new size = 2.2 um,/20 0.11um
#a pix = 4.8um/40 = 0.12um

import cv2
import numpy as np
import pdb
import sys
import os
import matplotlib.pyplot as plt

from method.toolkit import Cv2ImShow, Cv2ImSave

from method.edgedetect import Canny
from method.edgedetect import Threshold
from method.edgedetect import ErodeDilate
from method.edgedetect import CloseOpen
from method.toolkit import CalcHist
from method.sharp import IsSharp

from method.contour import findContours
from method.contour import HoughCircles
from method.contour import FitEllipse

from setting.set import SETTING


class Flow(object):
    """docstring for Flow"""
    def __init__(self, file):
        super(Flow, self).__init__()
        # self.arg = arg
        self.file = file
        self.img = cv2.imread(self.file)
        self.origin = self.img.copy()
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()

    def flow(self,):
        img = self.img
        self.show.show('origin', img[::2,::2])
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = ErodeDilate().run(img)
        self.show.show('edge', img[::2,::2])
        # img, result , contours , tree, treeList = findContours().run(img)
        img, result, contours, tree, treeList = findContours().run(img)
        # result = findContours().runNewTreeMethod(img)
        self.show.show('result', result[::2,::2])
        origin = FitEllipse().run(self.origin, result, contours, treeList)
        self.show.show('ellipse', origin[::2,::2])


    def flowTree(self,):
        img = self.img
        # self.show.show('origin', img[::2,::2])
        # self.save.save('save\\0.jpg', img)
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = ErodeDilate().run(img)
        self.show.show('edge', img[::2,::2])
        # self.save.save('save\\1.jpg', img)
        # img, result , contours , tree, treeList = findContours().run(img)
        # img, result, contours, tree, treeList = findContours().run(img)
        img, result, contours, treeList = findContours().runNewTreeMethod(img)
        self.show.show('find contours result', result[::2,::2])
        # self.save.save('save\\2.jpg', result)
        origin = FitEllipse().run(self.origin, result, contours, treeList)
        # self.show.show('ellipse', origin[::2,::2])
        # self.save.save('save\\3.jpg', origin)

    def flowRepetitive(self,):
        img = self.img
        # pdb.set_trace()
        img = ErodeDilate().run(img)
        # img = Canny().run(img)
        self.show.show('edge', img[::4,::4])
        img, result, contours, treeList = findContours().runNewTreeMethod(img)
        self.show.show('find contours result', result[::4,::4])
        origin = FitEllipse().ellipseTreeforCircleIndexSort(self.origin, result, contours, treeList)
        self.show.show('ellipse result', origin[::4,::4])

    def flowTest(self):
        img = self.img
        img = ErodeDilate().run(img)
        img = cv2.medianBlur(img, 9)
        self.show.show('edge', img[::4,::4])
        FitEllipse().ellipseForIfCondition(img)
        # self.show.show('ellipse result', origin[::4,::4])

    def flowCannyEllipse(self,):
        img = self.img
        # img = ErodeDilate().run(img)
        img = Canny().run(img)
        self.show.show('edge', img[::4,::4])
        img, result, contours, treeList = findContours().runNewTreeMethod(img)
        self.show.show('find contours result', result[::4,::4])
        origin = FitEllipse().ellipseTreeforCircleIndexSort(self.origin, result, contours, treeList)


    def flowHist(self):
        img = self.img
        self.show.show('origin', img[::2,::2])
        CalcHist().run(img)
        # calcHist(img)


class TraverseFolder(object):
    """docstring for TraverseFolder"""
    def __init__(self, folder):
        super(TraverseFolder, self).__init__()
        self.folder = folder

    def flow(self):
        for file in os.listdir(self.folder):
            flow = Flow(self.folder + "\\" + file)
            # flow.flow()
            # flow.flowCannyEllipse()
            # flow.flowRepetitive()
            flow.flowTest()

    def flowTree(self):
        for file in os.listdir(self.folder):
            flow = Flow(self.folder + "\\" + file)
            # flow.flow()
            flow.flowTree()
            # flow.flowHist()
            # flow.flowTest()

    def flowHist(self):
        for file in os.listdir(self.folder):
            flow = Flow(self.folder + "\\" + file)
            # flow.flow()
            # flow.flowTree()
            flow.flowHist()

    def sharpDetector(self):
        filename = self.folder
        xlist = []
        for file in os.listdir(filename):
            find = IsSharp(filename+"\\"+file).isSharp()
            # find = IsSharp(filename+"\\"+file).isSharpCanny()
            findsplit = file.split('-')
            print( 'find ', len(findsplit), findsplit[-2])
            timekitNum = findsplit[-2]

            # print(file,'::', find)
            xlist.append((timekitNum, find))
        xlist.sort()
        # pdb.set_trace()
        xlist = np.array(xlist)
        plt.plot(xlist[:,0],xlist[:,1])
        plt.show()

from SDK.mindpy import GetImg

class RealTimeFlow(object):
    """docstring for RealTimeFlow
    real-time method get picture"""
    def __init__(self, ):
        super(RealTimeFlow, self).__init__()
        # self.arg = arg
        self.show = Cv2ImShow()
        self.getImg = GetImg()
        self.save = Cv2ImSave()

    def img(self):
        return self.getImg.getImg()

    def flow(self):
        img = self.img()
        self.origin = img.copy()
        img = ErodeDilate().run(img)
        # img = Canny().run(img)
        self.show.show('edge', img[::4,::4])
        self.save.save('1.jpg',img[::4,::4])
        img, result, contours, treeList = findContours().runNewTreeMethod(img)
        self.show.show('find contours result', result[::4,::4])
        # self.save.save('2', img[::4,::4])
        origin = FitEllipse().ellipseTreeforCircleIndexSort(self.origin, result, contours, treeList)
        self.show.show('ellipse result', origin[::4,::4])

if __name__ == '__main__':
    # tr = TraverseFolder(folder = 'VT')
    # tr.flowTree()
    SETTING({'ampFactor':'20X','cameraID':'MindVision'})
    tr = TraverseFolder(folder='IMG\\GIOF1\\sig')
    tr.flow()
    # rtf = RealTimeFlow()
    # rtf.flow()




    # calc hist
    # tr = TraverseFolder(folder = 'VT')
    # tr.flowHist()
    #sharp detecter
    # tr = TraverseFolder(folder = 'sharp')
    # tr.sharpDetector()
