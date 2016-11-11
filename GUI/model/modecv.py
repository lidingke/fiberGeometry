from threading import Thread
from PyQt4.QtCore import QObject, pyqtSignal
import time
import pdb
import collections
import cv2
import numpy as np

from setting.set import SETTING
Set = SETTING()
setGet = Set.get('ifcamera', False)
print 'setget', setGet
if setGet:
    from SDK.mdpy import GetRawImg
else:
    from SDK.mdpy import GetRawImgTest as GetRawImg
    print 'script don\'t open camera'

from method.edgedetect import ErodeDilate
from method.contour import findContours
from method.contour import FitEllipse

from pattern.edge import ExtractEdge
from pattern.classify import G652Classify
from pattern.sharp import IsSharp
from pattern.draw import DecorateImg
from SDK.oceanoptics import OceanOpticsTest
from method.toolkit import Cv2ImShow, Cv2ImSave



class ModelCV(Thread, QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object)
    returnATImg = pyqtSignal(object, object)
    # returnFiberResult = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(ModelCV, self).__init__()
        self.setDaemon(True)
        self.IS_RUN = True
        self.isSharp = IsSharp()
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.ellipses = False
        self.result = False
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen = 5)
        self.fiberResult = {}
        self.Oceanoptics = OceanOpticsTest()


    def run(self):
        while self.IS_RUN:
            img = self._getImg()
            sharp = "%0.2f"%self.isSharp.isSharpDiff(list(self.imgQueue))
            # plotResults = (self.ellipses, self.result)
            img = self._decorateImg(img)
            self.returnImg.emit(img[::4,::4], sharp)

    def _getImg(self):
        img = self.getRawImg.get()
        self.imgQueue.append(img)
        # print 'imgqueue', len(self.imgQueue)
        # self.sharpQueue.append(img)
        return img

    def mainCalculate(self):
        Thread(target = self._calcImg).start()

    def _calcImg(self):
        img = self._getDifferImg()
        self._toClassify(img)

    def _getDifferImg(self):
        imgs = list(self.imgQueue)
        imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
        for img in imgs:
            img = ExtractEdge().run(img)
            imgAllor = cv2.bitwise_or(imgAllor, img)
        img = cv2.medianBlur(imgAllor, 7)
        return img

    def _toClassify(self, img):
        classify = G652Classify()
        self.ellipses = classify.find(img)
        self.result = classify.getResult()
        return self.result

    def _decorateImg(self,img):
        #todo: grb2gray need delete after rgb image show bug fixed
        """"mark the circle and size parameter"""
        ellipses = self.ellipses
        result = self.result
        # print 'decorate in ', ellipses or result, result
        if not (ellipses or result):
            return img
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img = DecorateImg(img,ellipses,result)
        # origin = np.ones_like(origin) * 255
        # cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 1, lineType=200)  # (162,183,0)(green, blue, red)
        # cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 1, lineType=200)  # 255,102,0#FF6600
        # print 'after decorate', img.shape
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img


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

    def exit(self):
        print "unInit"
        self.IS_RUN = False
        time.sleep(0.5)
        self.getRawImg.unInitCamera()

    def attenuationTest(self, length):
        wave, powers = self.Oceanoptics.getData(length)

        self.returnATImg.emit(wave, powers)
