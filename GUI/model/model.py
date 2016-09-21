from threading import Thread
from PyQt4.QtCore import QObject, pyqtSignal
from SDK.mindpy import GetRawImg
import cv2
from method.edgedetect import ErodeDilate
from method.contour import findContours
from method.contour import FitEllipse

from method.toolkit import Cv2ImShow, Cv2ImSave
import time
import pdb
import collections


class Model(Thread,QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(Model, self).__init__()
        self.setDaemon(True)
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen = 3)


    def run(self):
        while True:
            # time.sleep(1)
            img = self._getImg()

            # print 'emit ', img.shape
            self.returnImg.emit(img)

    def _getImg(self):
        img = self.getRawImg.get()
        # print 'img shape', img.shape
        self.imgQueue.append(img)
        # q = list(self.imgQueue)
        # # print 'qlen ', len(q)
        # if len(q) == 3:
        #     pass
        #     print 'imgqueue id ', id(q[0]), id(q[1]), id(q[2])
        return img[::4,::4]


    def mainCalculate(self):
        Thread(target = self._calcImg).start()


    def _calcImg(self):
        imgs = list(self.imgQueue)
        isImgAdded = True
        for img in imgs:
            img = ErodeDilate().run(img)
            if isImgAdded:
                imgadd = img
                isImgAdded = False
            else:
                imgadd = imgadd + img
        img = imgadd/3
        img = cv2.medianBlur(img, 9)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)

        self.show.show('edge', img[::4,::4])
        # self.save.save('filter.jpg', img[::4,::4])
        # imgs = list(self.imgQueue)
        # self.save.save('origin', imgs[0][::4,::4])
        # img, result, contours, treeList = findContours().runNoThrowChirldMethod(img)
        # self.show.show('find contours result', result[::4,::4])
        # origin = imgs[2].copy()
        # origin = FitEllipse().ellipseTreeforCircleIndexSort(origin, result, contours, treeList)
        # self.show.show('ellipse result', origin[::4,::4])

        FitEllipse().ellipseForIfCondition(img)

