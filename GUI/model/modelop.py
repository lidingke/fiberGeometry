import time
from threading import Thread
import numpy as np
from PyQt4.QtCore import QObject, pyqtSignal

from setting.parameter import SETTING
from util.observer import PyTypeSignal

Set = SETTING()
setGet = Set.get('ifcamera', False)
from setting.config import SPEC_ONLINE

if SPEC_ONLINE:
    from SDK.oceanoptics import Spectrograph
else:
    from SDK.oceanopticstest import SpectrographLikeTest as Spectrograph
from util.toolkit import Cv2ImShow, Cv2ImSave


# class ModelOp(Thread, QObject):
#     """docstring for Model"""
#     returnImg = pyqtSignal(object, object)
#
#     def __init__(self, ):
#         Thread.__init__(self)
#         QObject.__init__(self)
#         super(ModelOp, self).__init__()
#         self.setDaemon(True)
#         self.show = Cv2ImShow()
#         self.save = Cv2ImSave()
#         self.oceanoptics = TestDataSheets()
#
#     def run(self):
#         while True:
#             wave, powers = self.oceanoptics._getData(25)
#             time.sleep(0.5)
#             self.returnImg.emit(wave, powers)
#
#     def getAttenuation(self,length):
#             # print 'emit'
#         wave, powers = self.oceanoptics._getData(25)
#         return wave, powers


class ModelOP():
    def __init__(self):
        self.spect = Spectrograph()
        self.emit_spect = PyTypeSignal()

    def get_zero(self):
        wave, zero = self.spect.get_spectrograph()
        self.wave, self.zeros = wave, zero
        return (wave, zero)

    def get_before(self):
        wave, zero = self.spect.get_spectrograph()
        if len(wave) == len(self.wave):
            self.wave, self.before = wave, zero
            self.emit_spect.emit(wave, zero)
            return (wave, zero)
        else:
            raise ValueError("wavelength unmatched")

    def get_after(self):
        wave, zero = self.spect.get_spectrograph()
        if len(wave) == len(self.wave):
            self.wave, self.after = wave, zero
            return (wave, zero)
        else:
            raise ValueError("wavelength unmatched")

    # def get_power(self):
    def calculate_power(self, length):
        wave, before, after, zeros = \
            self.wave, self.before, self.after, self.zeros
        powers = []
        for x, y, z in zip(before, after, zeros):
            if y < 0:
                power = 0.0
            else:
                x  = x -z
                y = y -z
                if y ==0.0:
                    y = 0.0000000001
                power = 10 * np.log10((x - z) / (y - z)) / length
            # print 'power',x ,y ,power
            powers.append(power)

        self.emit_spect.emit(wave, powers)
        return (wave, powers)
