#coding:utf-8
import  xlrd
import numpy as np
import pdb
from SDK import pynir

class Spectrograph(object):

    def __init__(self):
        pass

    def get_spectrograph(self,*args):
        data = pynir.get_spectrum(*args)
        # len_data = len(data)
        # data = data.reshape((2, len_data // 2))
        w, d = data.tolist()
        return (w,d)

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
        # r = [(w,l) for w,l in zip(self.wave,)]
        return [0]*len(self.wave)

    def get_before(self):
        # r = [(w,l) for w,l in zip(self.wave,self.before)]
        return self.before

    def get_after(self):
        # r = [(w,l) for w,l in zip(self.wave,self.after)]
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
        return (w,d)

