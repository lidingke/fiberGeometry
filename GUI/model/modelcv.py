# coding:utf-8
import collections
import pdb
import time
from threading import Thread
import copy
import numpy as np
from PyQt4.QtCore import QObject, pyqtSignal

from setting.config import PDF_PARAMETER, DB_PARAMETER, DYNAMIC_CAMERA
from setting.orderset import SETTING
from pattern.exception import ClassCoreError, ClassOctagonError

Set = SETTING('octagon')
# setGet = Set.get('ifcamera', False)
# fiberType = Set.get('fiberType', "G652")
# print 'fibertype', fiberType, 'setget', setGet
if DYNAMIC_CAMERA:
    from SDK.mdpy import GetRawImg
else:
    from SDK.mdpytest import DynamicGetRawImgTest as GetRawImg

    # from  SDK.mdpy import GetRawImgTest as GetRawImg
    # print 'script don\'t open camera'
from pattern.classify import classifyObject
from pattern.sharp import IsSharp
from pattern.draw import DecorateImg, drawCoreCircle, decorateMethod
from util.filter import AvgResult
from util.loadimg import sliceImg

import logging

logger = logging.getLogger(__name__)


class ModelCV(Thread, QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object)
    # returnATImg = pyqtSignal(object, object)
    resultShowCV = pyqtSignal(object)
    # resultShowAT = pyqtSignal(object)
    returnCoreLight = pyqtSignal(object, object)

    def __init__(self, ):
        super(ModelCV, self).__init__()
        QObject.__init__(self)
        self.setDaemon(True)
        self.IS_RUNNING = True
        self.isSharp = IsSharp()
        self.eresults = False
        self.result2Show = {}
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen=5)
        self.classify = classifyObject("G652")
        self.decorateMethod = decorateMethod("G652")
        self.pdfparameter = PDF_PARAMETER # SETTING()['pdfpara']
        self.dbparameter = DB_PARAMETER #SETTING()['dbpara']

    def run(self):
        while self.IS_RUNNING:
            img = self.getRawImg.get()
            if not isinstance(img, np.ndarray):
                break
            self.img = img.copy()
            self.imgQueue.append(self.img)
            # self.sharp = "%0.2f" % self.isSharp.issharpla(img[::, ::, 0])
            self._greenLight(img)
            self.sharp = "%0.2f" % self.green
            colorImg = self._decorateImg(img)
            self.returnImg.emit(colorImg[::2, ::2].copy(), self.sharp)

    def mainCalculate(self):
        def _calcImg():
            try:
                # img.tofile("tests\\data\\tests\\midimg{}.bin".format(str(int(time.time()))[-3:]))
                self.imgQueue.clear()
                results = []
                while len(self.imgQueue) != 5:
                    time.sleep(0.1)
                for img in list(self.imgQueue):
                    self.eresults = self.classify.find(img)
                    result = self.eresults["showResult"]
                    logger.info('get result' + str(result))
                    results.append(result)
                self._emitCVShowResult(AvgResult(results))
            except ClassCoreError as e:
                logger.error('class core error')
                self.resultShowCV.emit('error')
                return
            except ValueError as e:
                logger.error(str(e))
                self.resultShowCV.emit('error')
                return
            except Exception as e:
                logger.exception(e)

        Thread(target=_calcImg).start()


    def _decorateImg(self, img):
        """"mark the circle and size parameter"""
        img = drawCoreCircle(img)
        if self.result2Show:
            img = self.decorateMethod(img, self.result2Show)
        return img

    def close(self):
        self.IS_RUNNING = False
        time.sleep(0.3)
        self.getRawImg.unInitCamera()

    def _emitCVShowResult(self, result):
        sharp = self.sharp
        self.result2Show = copy.deepcopy(self.eresults)
        self.result2Show["showResult"] = result
        if not hasattr(result, '__getitem__'):
            self.resultShowCV.emit('error')
            return
        result = result[1:] + result[:1]
        keys = ('corediameter', 'claddiameter', 'coreroundness',
                'cladroundness', 'concentricity')
        str_pdf_para_from_result = {k: '%0.2f' % r for k, r in zip(keys, result)}
        str_pdf_para_from_result.update({'sharpindex': sharp})
        self.pdfparameter.update(str_pdf_para_from_result)

        raw_db_data_from_result = {k: r for k, r in zip(keys, result)}
        raw_db_data_from_result.update({'sharpindex': sharp})
        # if None in result:
        #     for i,v in enumerate(result):
        #         if not v:
        #             result[i] = '-1'
        self.dbparameter.update(raw_db_data_from_result)
        text = (u'''纤芯直径：    {:0.2f}\n'''
                u'''包层直径：    {:0.2f}\n'''
                u'''纤芯不圆度：  {:0.2f}\n'''
                u'''包层不圆度：  {:0.2f}\n'''
                u'''芯包同心度：  {:0.2f}''')
        text = text.format(*result)
        logger.exception(text)
        self.resultShowCV.emit(text)

    def _greenLight(self, img):
        if isinstance(img, np.ndarray):
            #TODO:SETTING
            corey, corex = SETTING()["corepoint"]
            minRange, maxRange = SETTING()["coreRange"]
            green = sliceImg(img[::, ::, 1], (corex, corey), maxRange)
            blue = sliceImg(img[::, ::, 2], (corex, corey), maxRange)
            self.allblue = img[::, ::, 2].sum() / 255

            self.green = green.sum() / 255
            self.blue = blue.sum() / 255
            self.allgreen = img[::, ::, 1].sum() / 255 - self.green
            self.pdfparameter['corelight'] = "%0.2f" % self.blue
            self.pdfparameter['cladlight'] = "%0.2f" % self.allgreen
            self.returnCoreLight.emit("%0.2f" % (self.blue), "%0.2f" % (self.allgreen))
            # self.returnCladLight.emit()


    def updateClassifyObject(self, obj='G652'):
        self.classify = classifyObject(obj)
        self.eresults = False
        self.result2Show = False
        # self.decorateMethod = decorateMethod(obj)
        self.decorateMethod = decorateMethod(obj)



import pdb
class first():
    def __init__(self):
        print('first')

class next():
    def __init__(self):
        print('next')

class END(first,next):
    def __init__(self):
        mro = type(self).mro()
        for m in mro:
            m.__name__.endswith('first')
            m.__init(self)
        # pdb.set_trace()

# END()
