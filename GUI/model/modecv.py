#coding:utf-8
from threading import Thread
from PyQt4.QtCore import QObject, pyqtSignal
import time
import pdb
import collections
import cv2
import numpy as np

from setting.orderset import SETTING
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
setGet = Set.get('fiberType',"G652")
print 'fibertype',setGet
if setGet == "octagon":
    from pattern.classify import OctagonClassify as Classify
else:
    from pattern.classify import G652Classify as Classify
from pattern.sharp import IsSharp
from pattern.draw import DecorateImg, drawCoreCircle
from SDK.oceanoptics import OceanOpticsTest
from method.toolkit import Cv2ImShow, Cv2ImSave
import logging


class ModelCV(Thread, QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object)
    returnATImg = pyqtSignal(object, object)
    resultShowCV = pyqtSignal(object)
    resultShowAT = pyqtSignal(object)
    # returnFiberResult = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(ModelCV, self).__init__()
        self.setDaemon(True)
        logging.basicConfig(filename="setting\\modelog.txt", filemode='a', level=logging.ERROR,
                            format="%(asctiem)s-%(levelname)s-%(funcName):%(message)s")
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
            self.sharp = "%0.2f"%self.isSharp.isSharpDiff(list(self.imgQueue))
            # plotResults = (self.ellipses, self.result)

            colorImg = self.getRawImg.bayer2BGR(img)
            colorImg = self._decorateImg(colorImg)
            self.returnImg.emit(colorImg[::4,::4].copy(), self.sharp)

    def _getImg(self):
        img = self.getRawImg.get()
        self.imgQueue.append(img)
        # print 'imgqueue', len(self.imgQueue)
        # self.sharpQueue.append(img)
        return img

    def mainCalculate(self):
        Thread(target = self._calcImg).start()

    def _calcImg(self):
        try:
            img = self._getDifferImg()
            self._toClassify(img)
            self._emitCVShowResult()
        except Exception as e:
            logging.exception(e)

    def _getDifferImg(self):
        #todo: quanju medianblur
        imgs = list(self.imgQueue)
        imgAllor = np.zeros(imgs[0].shape[:2], dtype=imgs[0].dtype)
        for img in imgs:
            img = ExtractEdge().run(img)
            imgAllor = cv2.bitwise_or(imgAllor, img)
        img = cv2.medianBlur(imgAllor, 7)
        return img

    def _toClassify(self, img):
        classify = Classify()
        self.ellipses = classify.find(img)
        self.result = classify.getResult()
        return self.result

    def _decorateImg(self,img):
        """"mark the circle and size parameter"""
        img = drawCoreCircle(img)
        ellipses = self.ellipses
        result = self.result
        # print 'decorate in ', ellipses or result, result
        if not (ellipses or result):
            return img
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img = DecorateImg(img,ellipses,result)

        return img


    def exit(self):
        print "unInit"
        self.IS_RUN = False
        time.sleep(0.5)
        self.getRawImg.unInitCamera()

    def attenuationTest(self, length):
        wave, powers = self.Oceanoptics.getData(length)
        self._emitATShowResult(wave, powers)
        self.returnATImg.emit(wave, powers)

    def _emitATShowResult(self, wave, powers):
        waveLimit = wave[-1] - wave[0]
        waveMax = np.max(powers)
        waveMin = np.min(powers)
        waveAvg = np.average(powers)
        print waveLimit, waveMax, waveMin, waveAvg
        text = [
            u'''波长范围：    {}\n'''.format('%0.2f' % waveLimit),
            u'''最大值：      {}\n'''.format('%0.2f' % waveMax),
            u'''最小值：      {}\n'''.format('%0.2f' % waveMin),
            u'''平均值：      {}\n'''.format('%0.2f' % waveAvg)
        ]
        text = u''.join(text)
        self.resultShowAT.emit(text)


    def _emitCVShowResult(self):
        result = self.result
        sharp = self.sharp
        if isinstance(result, tuple):
            # print 'get result', result
            text = [
                u'''清晰度指数：  {}\n'''.format(sharp),
                u'''纤芯直径：    {}\n'''.format('%0.2f'%result[1]),
                u'''包层直径：    {}\n'''.format('%0.2f'%result[2]),
                u'''纤芯不圆度：  {}\n'''.format('%0.2f'%result[3]),
                u'''包层不圆度：  {}\n'''.format('%0.2f'%result[4]),
                u'''芯包同心度：  {}'''.format('%0.2f'%result[0])
                ]
            text = u''.join(text)
            self.resultShowCV.emit(text)

