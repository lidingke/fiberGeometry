# coding:utf-8
import collections
import inspect
import pdb
import time
import traceback
from threading import Thread
import copy
import numpy as np
import sys
from PyQt4.QtCore import QObject, pyqtSignal

from SDK.modbus.autolight import LightController
from setting.config import PDF_PARAMETER, DB_PARAMETER, DYNAMIC_CAMERA, FRAME_CORE, RAISE_EXCEPTION, IMG_ZOOM

if DYNAMIC_CAMERA:
    from SDK.mdpy import GetRawImg
else:
    # from SDK.mdpytest import DynamicGetRawImgTest as GetRawImg
    from SDK.mdpytest import DynamicGetRawImgTest as GetRawImg

from pattern.classify import classifyObject
from pattern.sharp import IsSharp
from pattern.draw import drawCoreCircle, decorateMethod, output_axies_plot_to_matplot, duck_type_decorate, core_flag
from util.filter import AvgResult
from pattern.coverimg import sliceImg

import logging

logger = logging.getLogger(__name__)


class ModelCV(Thread, QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object, object)
    # returnATImg = pyqtSignal(object, object)
    resultShowCV = pyqtSignal(object)
    # resultShowAT = pyqtSignal(object)
    returnCoreLight = pyqtSignal(object, object)
    emit_relative_index = pyqtSignal(object)

    def __init__(self, ):
        super(ModelCV, self).__init__()
        QObject.__init__(self)
        # self.setDaemon(True)
        self.IS_RUNNING = True
        self.isSharp = IsSharp()
        # self.img_core_tag = (FRAME_CORE,20,80)
        self.get_raw_img = GetRawImg()
        self.imgQueue = collections.deque(maxlen=5)
        self.classify = classifyObject("G652")
        # self.decorateMethod = decorateMethod("G652")
        self.pdfparameter = PDF_PARAMETER  # SETTING()['pdfpara']
        self.dbparameter = DB_PARAMETER  # SETTING()['dbpara']
        self.plots = core_flag()
        self.init_light_controller()

    def init_light_controller(self):
        self.light = ""
        self.light_controller = LightController()
        self.light_controller_handle = False
        self.light_controller.emit_dynamic_light.connect(self.get_light)

    def run(self):
        while self.IS_RUNNING:
            img = self.get_raw_img.get()
            if not isinstance(img, np.ndarray):
                break
            self.img = img.copy()
            self.imgQueue.append(self.img)
            if self.light_controller_handle:
                try:
                    self.light_controller_handle.send(img.copy())
                except StopIteration:
                    self.light_controller_handle = False

            self.sharp = "%0.2f" % self.isSharp.issharpla(self.img[::, ::, 0])
            # self._greenLight(img)

            # self.light = "%0.2f" % self.red

            img = self._decorateImg(img)
            zoom_img = img[::IMG_ZOOM, ::IMG_ZOOM].copy()
            self.returnImg.emit(zoom_img, self.sharp, self.light)

    def mainCalculate(self):
        def _calcImg(self):
            try:
                # img.tofile("tests\\data\\tests\\midimg{}.bin".format(str(int(time.time()))[-3:]))
                self.imgQueue.clear()
                results = []
                while len(self.imgQueue) != 5:
                    time.sleep(0.01)
                for img in list(self.imgQueue):
                    classify_result = self.classify.find(img)
                    result = classify_result["showResult"]
                    logger.info('get result' + str(result))
                    results.append(result)
                    core = classify_result["corecore"]
                    last_result = (core, img)
                plots = classify_result.get('plots', {})
                self.plots.extend(plots)
                self._emitCVShowResult(AvgResult(results))
                self._relaxtive_index_to_matplot(*last_result)
            except ValueError as e:
                msg = e.message
                logger.error("calc error {}".format(msg))
                logger.error("thread state - {}".format(self.IS_RUNNING))
                self.resultShowCV.emit(msg)
                # except Exception as e:
                #     raise e

        Thread(target=_calcImg, args=(self,)).start()

    def light_controller_handle_start(self):
        self.light_controller_handle = self.light_controller.start_coroutine()

    def _decorateImg(self, img):
        """" mark the circle and size parameter """
        # img = drawCoreCircle(img,*self.img_core_tag)
        if self.plots:
            img = duck_type_decorate(img, self.plots)
        # elif self.result2Show:
        #     img = self.decorateMethod(img, self.result2Show)
        return img

    def close(self):
        self.IS_RUNNING = False
        self.light_controller.close()
        # time.sleep(0.1)
        self.get_raw_img.release_camera()

    def _emitCVShowResult(self, result):
        sharp = self.sharp
        # self.result2Show = copy.deepcopy(self.eresults)
        # self.result2Show["showResult"] = result
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

        self.dbparameter.update(raw_db_data_from_result)
        text = (u'''纤芯直径：    {:0.2f}\n'''
                u'''包层直径：    {:0.2f}\n'''
                u'''纤芯不圆度：  {:0.2f}\n'''
                u'''包层不圆度：  {:0.2f}\n'''
                u'''芯包同心度：  {:0.2f}''')
        text = text.format(*result)
        logger.error(text)
        self.resultShowCV.emit(text)

    def get_light(self, light):
        self.light = light

    def updateClassifyObject(self, obj='G652'):
        self.classify = classifyObject(obj)
        # self.eresults = False
        # self.result2Show = False
        # self.decorateMethod = decorateMethod(obj)
        # self.decorateMethod = decorateMethod(obj)

    def _relaxtive_index_to_matplot(self, core, img):
        plots = output_axies_plot_to_matplot(core, img)
        self.emit_relative_index.emit(plots)
