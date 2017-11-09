# coding:utf-8
import threading
from functools import partial
from PyQt4.QtCore import QObject
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget

from GUI.model.models import session_add_by_account
from GUI.view.opplot import OpticalPlot
from GUI.view.uiview import ManualCVForm, AutomaticCVForm, OPCVForm
from GUI.view.mplqt4 import MyMplCanvas
from setting.config import VIEW_LABEL, PDF_PARAMETER, DB_PARAMETER

from util.observer import PyTypeSignal
from .reporter import Reporter
from PyQt4.QtCore import Qt, QRectF
from PyQt4.QtGui import QPixmap, QImage, QGraphicsScene
import numpy as np
from util.load import WriteReadJson, WRpickle, load_pickle_nor_json
from datetime import datetime
import logging
logger = logging.getLogger(__name__)


class CVViewModel(object):
    """docstring for View"""

    def __init__(self, ):
        self.scence = QGraphicsScene()
        self.graphicsView.setScene(self.scence)
        self.beginTestCV.clicked.connect(
            partial(self.beginTestCV.setEnabled,False))
        self.reporterCV.clicked.connect(self.writeReporterCV)
        self.insert_widgets()
        self.emit_fibertype_in_items = PyTypeSignal()
        self.last_save = {}
        self._last_data_init()
        self.emit_close_event = PyTypeSignal()

    def insert_widgets(self):
        self.relative_index_canvas = MyMplCanvas(QWidget(self.extendwidget), width=5, height=2, dpi=100)
        self.cvOperatorLayout.insertWidget(2,self.relative_index_canvas)



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

    def updatePixmap(self, arr, sharp, light):
        height, width, bytesPerComponent = arr.shape
        bytesPerLine = bytesPerComponent * width
        img = QImage(arr.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pximapimg = QPixmap.fromImage(img)

        self.scence.clear()
        self.scence.addPixmap(pximapimg)

        self.dynamicSharp.setText(sharp)
        self.light.setText(light)

    def enable_move_button(self, is_move=True):
        collections = ("move_down", "move_up", "next_state",
                       "move_right", "move_left", "reset")
        moves = {getattr(self, c) for c in collections}
        for move in moves:
            move.setEnabled(is_move)

    def closeEvent(self, *args, **kwargs):
        # if 'olddata' in SETTING().keys():
        #     self.olddata.save(SETTING()['olddata'])
        logger.info('get last save\n'+str(self.last_save))
        # print(self.last_save)
        self.olddata.save(self.last_save)
        self.emit_close_event.emit()

    def updateCVShow(self, str_,):
        if str_:

            self.resultShowCV.setText(str_)
            # self.resultShowCV.setStyleSheet("QTextBrowser{font-family: \"Microsoft YaHei\";}")
        self.beginTestCV.setEnabled(True)



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

    def relative_index_show(self, plots):
        self.relative_index_canvas.update_figure(*plots)


class OPCVViewModel(CVViewModel):

    def __init__(self):
        super(OPCVViewModel, self).__init__()
        # self.mainLayout.addWidget(self.opplot)

    def insert_widgets(self):
        self.opplot = OpticalPlot(QWidget(self.extendwidget), width=5, height=2, dpi=100)
        self.opLayout.insertWidget(0,self.opplot)
        self.relative_index_canvas = MyMplCanvas(QWidget(self.extendwidget), width=5, height=2, dpi=100)
        self.graphicsLayout.addWidget(self.relative_index_canvas)


class AutomaticCV(object):
    fathers = (AutomaticCVForm, CVViewModel,)

    @staticmethod
    def init(self):
        AutomaticCVForm.__init__(self)
        CVViewModel.__init__(self)

class OPCV(object):
    fathers = (OPCVForm, OPCVViewModel,)

    @staticmethod
    def init(self):
        OPCVForm.__init__(self)
        OPCVViewModel.__init__(self)


class ManualCV(object):
    fathers = (ManualCVForm, CVViewModel,)

    @staticmethod
    def init(self):
        ManualCVForm.__init__(self)
        CVViewModel.__init__(self)


def get_view(label):
    if label == "AutomaticCV":
        view = type("View", AutomaticCV.fathers, {"__init__": AutomaticCV.init})
    elif label == "ManualCV":
        view = type("View", ManualCV.fathers, {"__init__": ManualCV.init})
    elif label == "OPCV":
        view = type("View", OPCV.fathers, {"__init__": OPCV.init})
    else:
        raise TypeError("no view label correct")
    return view


View = get_view(VIEW_LABEL)
