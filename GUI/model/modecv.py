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
    elif fiberType == "G652":
        from SDK.mdpy import GetRawImgTestg652 as GetRawImg
    else:
        from SDK.mdpy import GetRawImgTest as GetRawImg
    print 'script don\'t open camera'

from pattern.edge import ExtractEdge

from pattern.classfiyInterface import classifyObject

from pattern.sharp import IsSharp
from pattern.draw import DecorateImg, drawCoreCircle, decorateMethod
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
        self.eresults = False
        self.result = False
        self.decorateMethod = decorateMethod("G652")
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen = 1)
        self.fiberResult = {}
        self.Oceanoptics = OceanOpticsTest()
        self.classify = classifyObject('G652')


    def run(self):
        while self.IS_RUN:
            img = self._getImg()

            # self.sharp = "%0.2f"%self.isSharp.isSharpDiff(list(self.imgQueue))
            self.sharp = "%0.2f" % self.isSharp.issharpla(self.img)
            # plotResults = (self.ellipses, self.result)
            self._greenLight(img[::, ::, 1])
            colorImg = self._decorateImg(img)
            self.returnImg.emit(colorImg[::2,::2].copy(), self.sharp)


    def _getImg(self):
        img = self.getRawImg.get()
        # img = self.getRawImg.bayer2BGR(img)
        self.img = img.copy()
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
        print 'get img type', img.shape, img.dtype
        self.eresults = self.classify.find(img)

        self.result = self.eresults["showResult"]
        print 'get ellipses', self.result
        # if self.result:
        #     SETTING()['tempLight'].append([int(self.green), float(self.result[1])])

        return self.result

    def updateClassifyObject(self, obj = 'G652'):
        self.classify = classifyObject(obj)
        self.eresults = False
        self.decorateMethod = decorateMethod(obj)

    def _decorateImg(self,img):
        """"mark the circle and size parameter"""
        img = drawCoreCircle(img)

        # print 'decorate in ',not (ellipses  or self.decorateMethod), ellipses , result , self.decorateMethod
        if not self.eresults:
            return img
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img = self.decorateMethod(img, self.eresults)
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
            print 'emit result', text

    def _greenLight(self, green):
        if isinstance(green, np.ndarray):
            corey, corex = SETTING()["corepoint"]
            minRange, maxRange = SETTING()["coreRange"]
            green = sliceImg(green, (corex, corey), maxRange)
            self.green = green.sum()/2550
            self.returnGreen.emit("%0.2f"%self.green)

    def fiberTypeMethod(self, key):
        SETTING().keyUpdates(key)




