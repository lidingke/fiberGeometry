# from    view        import View

from GUI.model.model import Model
from PyQt4.QtCore import QObject, pyqtSignal
from SDK.mindpy import IsInitCamera

class Controller(QObject):
    """docstring for Controller"""
    def __init__(self,view):
        super(Controller, self).__init__()
        self._view = view

        self._startModel()



    def show(self):
        self._view.show()


    def _initedStartModel(self):
        self.isInitCamera = IsInitCamera().isInit()
        if self.isInitCamera:
            # pass
            self._model = Model()
            self._model.returnImg.connect(self._view.updatePixmap)
            self._model.start()
        else:
            print 'camera not init'

    def _startModel(self):
        self._model = Model()
        self._model.returnImg.connect(self._view.updatePixmap)
        self._model.start()
