#coding:utf-8
import time
from threading import Thread
import numpy as np
from PyQt4.QtCore import QObject, pyqtSignal

from setting import config
from setting.parameter import SETTING
from util.observer import PyTypeSignal

# Set = SETTING()
# setGet = Set.get('ifcamera', False)
from setting.config import SPEC_ONLINE
import pickle

if SPEC_ONLINE:
    from SDK.oceanoptics import Spectrograph
else:
    from SDK.oceanopticstest import SpectrographLikeTest as Spectrograph
from util.patterntoolkit import Cv2ImShow, Cv2ImSave


class ModelOP():
    def __init__(self):
        self.spect = Spectrograph()
        self.emit_spect = PyTypeSignal()
        self.spect_args = (500000, 1, 0)
        self.pdfparameter = config.PDF_PARAMETER  # SETTING()['pdfpara']
        self.dbparameter = config.DB_PARAMETER  # SETTING()['dbpara']

    def get_zero(self):
        print("get zero")
        wave, zero = self.spect.get_spectrograph(*self.spect_args)
        self.wave, self.zeros = wave, zero
        self.emit_spect.emit(self.wave, self.zeros)
        return (wave, zero)

    def get_data(self):
        u"""获得减去暗电流的数据"""
        wave, data = self.spect.get_spectrograph(*self.spect_args)
        if len(wave) == len(self.wave):
            powers = [z1 - z0 for z1, z0 in zip(data, self.zeros)]
            self.pickle_data(wave, powers)
            return (wave, powers)
        else:
            raise ValueError("wavelength unmatched")

    def get_diff_zero_spectograph_data(self):
        print("get diff zero data")
        wave, data = self.get_data()
        self.emit_spect.emit(wave, data)

    def get_raw_spectograph_data(self):
        u"""获得原始的未减去暗电流的数据"""
        wave, data = self.spect.get_spectrograph(*self.spect_args)
        self.emit_spect.emit(wave, data)

    def get_before(self):
        self.wave, self.before = self.get_data()
        self.emit_spect.emit(self.wave, self.before)


    def get_after(self):
        self.wave, self.after = self.get_data()
        self.emit_spect.emit(self.wave, self.after)


    def calculate_power(self, length):
        u"""计算power = 10 * log10(x / y) / length
        x:第一次测试。
        y:第二次测试。
        length：光纤长度。
        """
        # print("get length",length)
        wave, before, after, zeros = \
            self.wave, self.before, self.after, self.zeros
        powers = []
        waves = []
        for x, y, z,w in zip(before, after, zeros, wave):
            if y <= 0 or x <= 0 or x / y <= 0:
                continue
            power = 10 * np.log10(y / x) / length
            powers.append(power)
            waves.append(w)
        self.emit_spect.emit(waves, powers)
        return (waves, powers)

    def pickle_data(self, waves, powers):

        self.dbparameter['attwaves'] = pickle.dumps(waves)
        self.dbparameter['attpowers'] = pickle.dumps(powers)

    def set_spect_args_manual(self, integral_times_ms, integral_steps, smoothness):
        integral_times_us = integral_times_ms * 1000
        self.spect_args = (integral_times_us, integral_steps, smoothness)

    def set_spect_args_auto(self, length):
        args = list(self.spect_args)
        args_0 = self.auto_get_spect_continue(length)
        args[0] = args_0
        self.spect_args = tuple(args)
        # print(args_new)

    def auto_get_spect_continue(self, length):
        for limit, value in config.SPECT_CONTINUE:
            if length > limit:
                return value
        raise ValueError("spect continue error")