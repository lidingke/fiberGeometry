import time
from threading import Thread
import numpy as np
from PyQt4.QtCore import QObject, pyqtSignal

from setting.parameter import SETTING
from util.observer import PyTypeSignal

# Set = SETTING()
# setGet = Set.get('ifcamera', False)
from setting.config import SPEC_ONLINE

if SPEC_ONLINE:
    from SDK.oceanoptics import Spectrograph
else:
    from SDK.oceanopticstest import SpectrographLikeTest as Spectrograph
from util.toolkit import Cv2ImShow, Cv2ImSave


class ModelOP():
    def __init__(self):
        self.spect = Spectrograph()
        self.emit_spect = PyTypeSignal()
        self.spect_args = (500000, 1, 0)

    def get_zero(self):
        wave, zero = self.spect.get_spectrograph(*self.spect_args)
        self.wave, self.zeros = wave, zero
        return (wave, zero)

    def get_data(self):
        wave, data = self.spect.get_spectrograph(*self.spect_args)
        if len(wave) == len(self.wave):
            diff_zero = [z1 - z0 for z1, z0 in zip(data, self.zeros)]
            self.wave, self.before = wave, diff_zero
            return (wave, diff_zero)
        else:
            raise ValueError("wavelength unmatched")

    def get_before(self):
        wave, diff_zero = self.get_data()
        self.emit_spect.emit(wave, diff_zero)

    def get_after(self):
        self.get_data()

    # def get_power(self):
    def calculate_power(self, length):
        wave, before, after, zeros = \
            self.wave, self.before, self.after, self.zeros
        powers = []
        for x, y, z in zip(before, after, zeros):
            if y < 0:
                power = 0.0
            else:
                if y == 0.0:
                    y = 0.0000000001
                power = 10 * np.log10(x / y) / length
            powers.append(power)

        self.emit_spect.emit(wave, powers)
        return (wave, powers)

    def set_spect_args(self, integral_times_ms, integral_steps,smoothness):
        integral_times_us = integral_times_ms*1000
        self.spect_args = (integral_times_us, integral_steps,smoothness)
