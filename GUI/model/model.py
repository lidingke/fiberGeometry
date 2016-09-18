from threading import Thread
from PyQt4.QtCore import QObject, pyqtSignal
from SDK.mindpy import GetRawImg
import time


class Model(Thread,QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(Model, self).__init__()
        self.setDaemon(True)
        self.getRawImg = GetRawImg()


    def run(self):
        while True:
            time.sleep(1)
            img = self._getImg()

            print 'emit ', img.shape
            self.returnImg.emit(img)

    def _getImg(self):
        img = self.getRawImg.get()
        return img[::4,::4]

