# coding:utf-8
import threading
from time import sleep

import multiprocessing
import xlrd
import numpy as np
import pdb

from PyQt4.QtCore import QThread, pyqtSignal, QObject

from SDK import pynir

import logging

from setting import config
from util.observer import PyTypeSignal

logger = logging.getLogger(__name__)


class WorkThread(QThread):
    # trigger = pyqtSignal(object)
    trigger = PyTypeSignal()


    def __int__(self, ):
        super(WorkThread, self).__init__()

    def run(self):
        self.args = None
        print("run work thread")
        while True:
            sleep(0.1)
            if self.args:
                print(self.args)
                data = pynir.get_spectrum(*self.args)
                w, d = data.tolist()
                # w,d = self.test_get(*self.args)
                self.trigger.emit((w, d))
                self.args = None

    def get_result(self, arg):
        print("get arg",arg)
        self.args = arg

    def test_get(self,*args):
        print("test get",args)
        return 1,2


class Spectrograph(QObject):
    # trigger = pyqtSignal(object)
    trigger = PyTypeSignal()

    def __init__(self):
        # super(Spectrograph, self).__init__()
        QObject.__init__(self)
        self.worker = WorkThread()
        self.trigger.connect(self.worker.get_result)
        self.worker.trigger.connect(self.get_result)
        self.worker.start()

    def get_spectrographq(self, *args):
        sleep(1)
        self.result = None
        self.trigger.emit(args)
        print("run get spect")
        while True:
            if self.result:
                return self.result
            sleep(0.1)



    def get_result(self, result):
        print("get arg",result)
        self.result = result

    def get_spectrograph(self,*args):
        logging.error("spect args:{}".format(args))
        threading.Thread(target=self.get_spect_by_thread,args=(args)).start()
        while True:
            sleep(0.5)
            if self.result:
                return self.result

    def get_spectrograph_by_length(self,length,*args):
        args_0 = self.get_spect_continue(length)
        args_1 = args[1:]
        args_new = (args_0,)+args_1
        # pdb.set_trace()
        print(args_new)
        self.get_spectrograph(*args_new)
    # def get_spectrograph(self,*args):
    #
    #     multiprocessing.Process(target=self.get_spect_by_thread,args=(self,args)).start()
    #     while True:
    #         sleep(0.5)
    #         if self.result:
    #             return self.result



    def get_spect_by_thread(self, *args):
        self.result = None
        # pdb.set_trace()
        # logging.error("")
        print(args)
        data = pynir.get_spectrum(*args)
        w, d = data.tolist()
        self.result = (w, d)

    def get_spect_continue(self,length):
        for limit, value in config.SPECT_CONTINUE:
            if length > limit:
                return value
        raise ValueError("spect continue error")



class TestDataSheets(object):

    def __init__(self):
        self.datas = self._getData()

    def _getData(self):
        # print 'get data'
        data = xlrd.open_workbook('SDK\\OceanOpticsScript\\20160920.xlsx')
        # table = data.sheet_by_name(u'25公里 200um狭缝')
        table = data.sheets()[0]
        self.wave = table.col_values(0)
        self.before = table.col_values(3)
        self.after = table.col_values(5)
        # return [(w,b,a) for w,b,a in zip(wave,before,after)]

    def get_wave(self):
        return self.wave

    def get_zero(self):
        return [0] * len(self.wave)

    def get_before(self):
        return self.before

    def get_after(self):
        return self.after


def get_next():
    while True:
        for i in range(3):
            yield i


class SpectrographLikeTest(object):

    def __init__(self):
        self.number = get_next()
        # next(self.number)
        self.datasheets = TestDataSheets()
        self.gets = [self.datasheets.get_zero,
                     self.datasheets.get_before,
                     self.datasheets.get_after]
        # self.gets =

    def new(self):
        self.number = get_next()
        # next(self.number)

    def get_spectrograph(self):
        w = self.datasheets.get_wave()
        d = self.gets[next(self.number)]()
        # r = [(w,l) for w,l in zip(w,d)]
        return (w, d)



