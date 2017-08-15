# coding:utf-8
# branch dev
import threading
from functools import partial

from PyQt4.QtCore import QObject
from PyQt4.QtCore import pyqtSignal
from GUI.UI.mainUI import Ui_MainWindow as new_MainWindow
from GUI.view.opplot import OpticalPlot
import cv2

from GUI.model.models import session_add_by_account
from GUI.view.uiview import ManualCVForm, AutomaticCVForm
from setting.config import VIEW_LABEL, PDF_PARAMETER, DB_PARAMETER
from setting.orderset import SETTING

# from GUI.UI.mainUI import Ui_MainWindow
import logging

from util.observer import MySignal
from .reporter import Reporter
from pattern.sharp import MaxSharp
from PyQt4.QtCore import QRect, Qt, QRectF
from PyQt4.QtGui import QPixmap, QImage, QGraphicsScene
import numpy as np
from util.load import WriteReadJson, WRpickle, load_pickle_nor_json
from datetime import datetime

logger = logging.getLogger(__name__)


class CVViewModel(object):
    """docstring for View"""

    def __init__(self, ):
        # super(CVViewModel, self).__init__()
        # self.setupUi(self)
        print "init cv view"
        self.scence = QGraphicsScene()
        self.graphicsView.setScene(self.scence)
        # self.isMaxSharp = MaxSharp()
        self.beginTestCV.clicked.connect(self._disableCVButton)
        self.reporterCV.clicked.connect(self.writeReporterCV)
        self.emit_fibertype_in_items = MySignal()
        self.last_save = {}
        self._last_data_init()
        self.emit_close_event = MySignal()

    def _last_data_init(self):
        load = load_pickle_nor_json("setting\\userdata")
        types = load.get("fiberTypes")
        self.fiberTypeBox.addItems(types)
        # now = self.fiberTypeBox.currentText()
        self.emit_fibertype_in_items.emit()

        try:
            self.olddata = WriteReadJson('setting\\old.json')
            self.last_save = self.olddata.load()
        except ValueError:
            return
        if self.last_save:
            self.fiberLength.setText(self.last_save['fiberLength'])
            self.Worker.setText(self.last_save['worker'])
            self.factory.setText(self.last_save['producer'])
            self.fiberNumber.setText(self.last_save['fiberNo'])

    def updatePixmap(self, arr, sharp):
        if not isinstance(arr, np.ndarray):
            raise ValueError('get Pixmap ERROR input')
        height, width, bytesPerComponent = arr.shape
        bytesPerLine = bytesPerComponent * width
        img = QImage(arr.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        pximapimg = QPixmap.fromImage(img)
        # = self._getPixmap(arr)
        self.scence.clear()
        self.scence.addPixmap(pximapimg)

        # if hasattr(self, 'dynamicSharp'):
        self.dynamicSharp.setText(sharp)

    def enable_move_button(self, is_move=True):
        print "set move", is_move
        collections = ("move_down", "move_up", "next_state",
                       "move_right", "move_left", "reset")
        moves = {getattr(self, c) for c in collections}
        for move in moves:
            move.setEnabled(is_move)

    def closeEvent(self, *args, **kwargs):
        # if 'olddata' in SETTING().keys():
        #     self.olddata.save(SETTING()['olddata'])
        print('get last save')
        print(self.last_save)
        self.olddata.save(self.last_save)
        self.emit_close_event.emit()

    def updateCVShow(self, str_):
        if str_:
            self.resultShowCV.setText(str_)
        self._disableCVButton(True)

    def _disableCVButton(self, bool=False):
        self.beginTestCV.setEnabled(bool)

        # def updateATShow(self,str_):
        #     self.resultShowAT.setText(str_)

        # def initGUI(self):

        # print para['fibertypeindex'], int(para['fibertypeindex'])
        # self.fiberTypeBox.setCurrentIndex(int(para['fibertypeindex']))

    def writeReporterCV(self):
        para = {}
        para['fiberLength'] = str(self.fiberLength.text())
        para['worker'] = str(self.Worker.text())
        para['producer'] = str(self.factory.text())
        para['fiberNo'] = str(self.fiberNumber.text())
        para['fibertype'] = str(self.fiberTypeBox.currentText())
        para['fibertypeindex'] = str(self.fiberTypeBox.currentIndex())
        para['date'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        para['title'] = para['fibertype'] + '光纤端面几何测试报告'
        PDF_PARAMETER.update(para)
        self.last_save.update(para)
        Reporter(self)
        # print 'get in session'
        DB_PARAMETER.update(para)
        # dbpara = SETTING()['dbpara']
        session_add_by_account(DB_PARAMETER)


        # def getCoreLight(self, coreLight, cladLight):
        #     if hasattr(self, "coreLight"):
        #         self.coreLight.setText(coreLight)
        #     if hasattr(self, "cladLight"):
        #         self.cladLight.setText(cladLight)


class MyQGraphicsScene(QGraphicsScene):
    def __init__(self):
        QGraphicsScene.__init__(self)
        # super(MyQGraphicsScene, self).__init__()
        self.rect_pos = [False, False]
        # self.setBspTreeDepth(1)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rect_pos[0] = event.scenePos()

    def mouseMoveEvent(self, event):
        self.rect_pos[1] = event.scenePos()
        self._paint_event()

    def _paint_event(self):
        if self.rect_pos[1]:
            top_left, bottom_right = self.rect_pos
            rect = QRectF(top_left, bottom_right)
            self.addRect(rect)


# class View(AutomaticCVForm,CVViewModel):
#     def __init__(self):
#         AutomaticCVForm.__init__(self)
#         CVViewModel.__init__(self)
#         self.print_mro()
#
#     @classmethod
#     def print_mro(cls):
#         print cls.__mro__

class AutomaticCV(object):
    fathers = (AutomaticCVForm, CVViewModel,)

    @staticmethod
    def init(self):
        AutomaticCVForm.__init__(self)
        CVViewModel.__init__(self)


class ManualCV(object):
    fathers = (ManualCVForm, CVViewModel,)

    @staticmethod
    def init(self):
        ManualCVForm.__init__(self)
        CVViewModel.__init__(self)


def get_view(label):
    print label
    if label == "AutomaticCV":
        view = type("View", AutomaticCV.fathers, {"__init__": AutomaticCV.init})
    elif label == "ManualCV":
        view = type("View", ManualCV.fathers, {"__init__": ManualCV.init})
    else:
        raise TypeError("no view label correct")
    return view


View = get_view(VIEW_LABEL)
