# coding:utf-8
# branch dev

from GUI.model.models import session_add_by_account
from GUI.view.uiview import ManualCVForm, AutomaticCVForm
from setting.config import VIEW_LABEL
from setting.orderset import SETTING
import cv2
# from GUI.UI.mainUI import Ui_MainWindow
import logging

from util.observer import MySignal
from .reporter import Reporter
from pattern.sharp import MaxSharp
from PyQt4.QtCore import QRect, Qt, QRectF
from PyQt4.QtGui import QPixmap, QImage, QGraphicsScene
import numpy as np
from util.load import WriteReadJson, WRpickle
from datetime import datetime

logger = logging.getLogger(__name__)


def init_form_first(fun):
    def init(self):
        mro = type(self).mro()
        for m in mro:
            if m.__name__.endswith('Form'):
                print 'class name:',m.__name__
                m.__init__(self)
        fun(self)
    return init

class CVViewModel(object):
    """docstring for View"""

    @init_form_first
    def __init__(self, ):
        super(CVViewModel, self).__init__()
        # self.setupUi(self)
        print "init cv view"
        self.scence = QGraphicsScene()
        self.graphicsView.setScene(self.scence)
        self.isMaxSharp = MaxSharp()
        self.beginTestCV.clicked.connect(self._disableCVButton)
        self.reporterCV.clicked.connect(self.writeReporterCV)
        self._last_data_init()
        self.emit_close_event = MySignal()

    def _last_data_init(self):
        wrp = WRpickle("setting\\userdata.pickle")
        try:
            load = wrp.loadPick()
        except IOError:
            wrJson = WriteReadJson("setting\\userdata.json")
            load = wrJson.load()
        types = load.get("fiberTypes")
        self.fiberTypeBox.addItems(types)

        try:
            self.olddata = WriteReadJson('setting\\old.json')
            para = self.olddata.load()
        except ValueError:
            return
        if para:
            self.fiberLength.setText(para['fiberLength'])
            self.Worker.setText(para['worker'])
            self.factory.setText(para['producer'])
            self.fiberNumber.setText(para['fiberNo'])

    def updatePixmap(self, arr, sharp):

        self.pximapimg = self._getPixmap(arr)
        self.scence.clear()
        self.scence.addPixmap(self.pximapimg)

        if hasattr(self, 'dynamicSharp'):
            self.dynamicSharp.setText(sharp)
            if self.isMaxSharp.isRight(sharp):
                self.dynamicSharp.setStyleSheet("color:red")
            else:
                self.dynamicSharp.setStyleSheet("color:white")

    def enable_move_button(self, is_move=True):
        print "set move", is_move
        collections = ("move_down", "move_up", "next_state",
                       "move_right", "move_left", "reset")
        moves = {getattr(self, c) for c in collections}
        for move in moves:
            move.setEnabled(is_move)

    def closeEvent(self, *args, **kwargs):
        if 'olddata' in SETTING().keys():
            self.olddata.save(SETTING()['olddata'])
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
        SETTING()['pdfpara'].update(para)
        SETTING()['olddata'] = para
        Reporter(self)
        # print 'get in session'
        SETTING()['dbpara'].update(para)
        dbpara = SETTING()['dbpara']
        session_add_by_account(dbpara)

    def getCoreLight(self, coreLight, cladLight):
        if hasattr(self, "coreLight"):
            self.coreLight.setText(coreLight)
        if hasattr(self, "cladLight"):
            self.cladLight.setText(cladLight)

    def _getPixmap(self, mapArray):
        if not isinstance(mapArray, np.ndarray):
            raise ValueError('get Pixmap ERROR input')
        height, width, bytesPerComponent = mapArray.shape
        bytesPerLine = bytesPerComponent * width
        img = QImage(mapArray.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        return QPixmap.fromImage(img)
        # self.update()


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

automatic_fathers = (AutomaticCVForm, CVViewModel,)

manual_fathers = (ManualCVForm, CVViewModel,)



def get_view(label):
    print("get view label "+label)
    if label == "AutomaticCV":
        view = type("View", automatic_fathers,{})
    elif label == "ManualCV":
        view = type("View", manual_fathers,{})
    else:
        raise TypeError("no view label correct")
    return view


View = get_view(VIEW_LABEL)
