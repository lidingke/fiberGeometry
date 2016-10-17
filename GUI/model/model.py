from threading import Thread
from PyQt4.QtCore import QObject, pyqtSignal
from SDK.mdpy import GetRawImg
import cv2
import numpy as np
from method.edgedetect import ErodeDilate
from method.contour import findContours
from method.contour import FitEllipse

from pattern.edge import ExtractEdge
from pattern.classify import G652Classify
from pattern.sharp import IsSharp

from method.toolkit import Cv2ImShow, Cv2ImSave
import time
import pdb
import collections


class Model(Thread,QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object)
    # returnFiberResult = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(Model, self).__init__()
        self.setDaemon(True)
        self.IS_RUN = True
        self.isSharp = IsSharp()
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen = 5)
        self.fiberResult = {}


    def run(self):
        while self.IS_RUN:
            img = self._getImg()
            sharp = "%0.2f"%self.isSharp.isSharpDiff(list(self.imgQueue))
            self.returnImg.emit(img, sharp)

    def _getImg(self):
        img = self.getRawImg.get()
        self.imgQueue.append(img)
        # self.sharpQueue.append(img)
        return img[::4,::4]


    def mainCalculate(self):
        Thread(target = self._calcImg).start()

    def multiTest(self):
        Thread(target=self._multiCalc).start()

    def _multiCalc(self):
        resultlist = []
        for x in range(20):
            img = self._getDifferImg()
            result = self._toClassify(img)
            print 'result,', result
            if result:
                resultlist.append(str(result)[1:-1]+'\n')
            time.sleep(3)


        with open('IMG\\result.csv', 'wb+') as f:
            f.writelines(resultlist)

    # def _calcImg2(self):
    #     imgs = list(self.imgQueue)
    #     isImgAdded = True
    #     for img in imgs:
    #         img = ErodeDilate().run(img)
    #         if isImgAdded:
    #             imgadd = img
    #             isImgAdded = False
    #         else:
    #             imgadd = imgadd + img
    #     img = imgadd/3
    #     img = cv2.medianBlur(img, 9)
    #     img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)
    #     self.show.show('edge', img[::4,::4])
    #     FitEllipse().ellipseForIfCondition(img)

    def _calcImg(self):
        img = self._getDifferImg()
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)
        self._toClassify(img)

    def _getDifferImg(self):
        imgs = list(self.imgQueue)
        imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
        for img in imgs:
            img = ExtractEdge().run(img)

            imgAllor = cv2.bitwise_or(imgAllor, img)
        # self.show.show('img', img[::4, ::4])
        img = cv2.medianBlur(imgAllor, 7)

        return img

    def _toClassify(self, img):

        # self.show.show('edge', img[::4,::4])
        classify = G652Classify()
        classify.find(img)
        result = classify.getResult()
        return result


    def exit(self,):
        print "unInit"
        self.IS_RUN = False
        time.sleep(0.5)
        self.getRawImg.unInitCamera()
