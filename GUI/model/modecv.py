#coding:utf-8
import collections
import time
from threading import Thread

import cv2
import numpy as np
from PyQt4.QtCore import QObject, pyqtSignal

from setting.orderset import SETTING

Set = SETTING('octagon')
setGet = Set.get('ifcamera', False)
fiberType = Set.get('fiberType',"G652")
print 'fibertype',fiberType,'setget', setGet
if setGet:
    from SDK.mdpy import GetRawImg
else:
    if fiberType == "20400":
        from SDK.mdpy import GetRawImgTest20400 as GetRawImg
    else:
        from SDK.mdpy import GetRawImgTest as GetRawImg
    print 'script don\'t open camera'

from pattern.edge import ExtractEdge

if fiberType == "octagon":
    from pattern.classify import OctagonClassify as Classify
elif fiberType == "20400":
    from pattern.classify import Big20400Classify as Classify
else:
    from pattern.classify import G652Classify as Classify
from pattern.sharp import IsSharp
from pattern.draw import DecorateImg, drawCoreCircle
from SDK.oceanoptics import OceanOpticsTest
from util.toolkit import Cv2ImShow, Cv2ImSave
import logging
from util.timing import timing
from util.loadimg import sliceImg


class ModelCV(Thread, QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object)
    returnATImg = pyqtSignal(object, object)
    resultShowCV = pyqtSignal(object)
    resultShowAT = pyqtSignal(object)
    returnGreen = pyqtSignal(object)
    # returnFiberResult = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(ModelCV, self).__init__()
        self.setDaemon(True)
        logging.basicConfig(filename="setting\\modelog.txt", filemode='a', level=logging.ERROR,
                            format="%(asctime)s-%(levelname)s-%(funcName)s:%(message)s")
        self.IS_RUN = True
        self.isSharp = IsSharp()
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.ellipses = False
        self.result = False
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen = 1)
        self.fiberResult = {}
        self.Oceanoptics = OceanOpticsTest()
        self.classify = Classify()


    def run(self):
        while self.IS_RUN:
            img = self._getImg()
            img = self.getRawImg.bayer2BGR(img)
            # self.sharp = "%0.2f"%self.isSharp.isSharpDiff(list(self.imgQueue))
            self.sharp = "%0.2f" % self.isSharp.issharpla(self.img)
            # plotResults = (self.ellipses, self.result)
            self._greenLight(img[::, ::, 1])
            colorImg = self._decorateImg(img)
            self.returnImg.emit(colorImg[::2,::2].copy(), self.sharp)


    def _getImg(self):
        img = self.getRawImg.get()

        self.img = img
        # self.imgQueue.append(img)
        # print 'imgqueue', len(self.imgQueue)
        # self.sharpQueue.append(img)
        return img

    def mainCalculate(self):
        def _calcImg():
            try:
                # img.tofile("tests\\data\\tests\\midimg{}.bin".format(str(int(time.time()))[-3:]))
                self._toClassify(self.img)
                self._emitCVShowResult()
            except Exception as e:
                logging.exception(e)
        Thread(target = _calcImg).start()



    # @timing
    # def _getDifferImg(self):
    #     imgs = list(self.imgQueue)
    #     imgAllor = np.zeros(imgs[0].shape[:2], dtype=imgs[0].dtype)
    #     for img in imgs:
    #         img = ExtractEdge().run(img)
    #         imgAllor = cv2.bitwise_or(imgAllor, img)
    #     img = imgs[-1]
    #     print 'img.shape', img.shape
    #     return img

    @timing
    def _toClassify(self, img):
        self.ellipses = self.classify.find(img)
        self.result = self.classify.getResult()
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

    def _greenLight(self, green):
        if isinstance(green, np.ndarray):
            corey, corex = SETTING()["corepoint"]
            minRange, maxRange = SETTING()["coreRange"]
            green = sliceImg(green, (corex, corey), maxRange)
            result = green.sum()/2550
            self.returnGreen.emit("%0.2f"%result)



