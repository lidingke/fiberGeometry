import time
from threading import Thread

from PyQt4.QtCore import QObject, pyqtSignal

from setting.orderset import SETTING

Set = SETTING()
setGet = Set.get('ifcamera', False)
from SDK.oceanoptics import OceanOpticsTest
from util.toolkit import Cv2ImShow, Cv2ImSave

class ModelOp(Thread, QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object, object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(ModelOp, self).__init__()
        self.setDaemon(True)
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.oceanoptics = OceanOpticsTest()

    def run(self):
        while True:
            wave, powers = self.oceanoptics.getData(25)
            time.sleep(0.5)
            self.returnImg.emit(wave, powers)

    def getAttenuation(self,length):
            # print 'emit'
        wave, powers = self.oceanoptics.getData(25)
        return wave, powers

