# coding:utf-8
import pdb
import threading
from functools import partial

import sys
from PyQt4.QtCore import QObject
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QWidget

from GUI.model.models import session_add_by_account
from GUI.view.spectcanvas import SpectrumCanvas
from GUI.view.uiview import ManualCVForm, AutomaticCVForm, OPCVForm, CapCVForm
from GUI.view.refractcanvas import RefractCanvas
from report.pdf import write_txt
from setting.config import PDF_PARAMETER, DB_PARAMETER

from util.observer import PyTypeSignal
from GUI.view.reporter import ReporterPdfs
from PyQt4.QtCore import Qt, QRectF
from PyQt4.QtGui import QPixmap, QImage, QGraphicsScene
import numpy as np
from util.loadfile import WriteReadJson, WRpickle, load_pickle_nor_json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class CVViewModel(object):
    """docstring for View"""

    def __init__(self, ):
        super(CVViewModel, self).__init__()
        self.scence = QGraphicsScene()
        self.graphicsView.setScene(self.scence)
        self.beginTestCV.clicked.connect(
            partial(self.beginTestCV.setEnabled, False))
        self.reporterCV.clicked.connect(self.writeReporterCV)
        self.insert_widgets()
        self.emit_fibertype_in_items = PyTypeSignal()
        self.last_save = {}
        self._last_data_init()
        self.emit_close_event = PyTypeSignal()
        self.to_report = ReporterPdfs

    def insert_widgets(self):
        self.relative_index_canvas = RefractCanvas(QWidget(self.extendwidget), width=5, height=2, dpi=100)
        self.cvOperatorLayout.insertWidget(2, self.relative_index_canvas)

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
        logger.info('get last save\n' + str(self.last_save))
        # print(self.last_save)
        self.olddata.save(self.last_save)
        self.emit_close_event.emit()

    def updateCVShow(self, str_, ):
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
        self.to_report(self)
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


class CapCVViewModel(CVViewModel):
    def __init__(self):
        super(CapCVViewModel, self).__init__()
        if hasattr(self, "lightControl"):
            self.lightControl.hide()
            self.labelFiberType.hide()
            self.labelFactory.hide()
            self.labelFiberNumber.hide()
            self.labelLength.hide()
            self.labelWorker.hide()
            self.Worker.hide()
            self.factory.hide()
            self.fiberLength.hide()
            self.fiberNumber.hide()
            self.fiberTypeBox.hide()
        self.to_report = write_txt

        # self..hide()
        # print dir(self.inputLayout)
        # pdb.set_trace()

    def insert_widgets(self):
        pass

    def relative_index_show(self, plots):
        pass

    def writeReporterCV(self):
        para = {}
        para['cap_fibre'] = unicode(self.cap_fibre.text())
        para["cap_mc"] = unicode(self.cap_mc.currentText())
        para["cap_bt"] = unicode(self.cap_bt.currentText())
        para["cap_operator"] = unicode(self.cap_operator.text())
        para["cap_machine"] = unicode(self.cap_machine.text())
        para["cap_date"] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        PDF_PARAMETER.update(para)
        self.to_report(".", PDF_PARAMETER)


class OPCVViewModel(CVViewModel):
    def __init__(self):
        super(OPCVViewModel, self).__init__()
        # pdb.set_trace()
        # self.mainLayout.addWidget(self.opplot)

    def insert_widgets(self):
        self.opplot = SpectrumCanvas(QWidget(self.extendwidget), width=5, height=2, dpi=100)
        self.opLayout.insertWidget(0, self.opplot)
        self.relative_index_canvas = RefractCanvas(QWidget(self.extendwidget), width=5, height=2, dpi=100)
        self.graphicsLayout.addWidget(self.relative_index_canvas)


# class AutomaticCV(object):
#     fathers = (CVViewModel, AutomaticCVForm)
#
#     @staticmethod
#     def init(self):
#         AutomaticCVForm.__init__(self)
#         CVViewModel.__init__(self)
#
# class OPCV(object):
#     fathers = (OPCVViewModel, OPCVForm, )
#
#     @staticmethod
#     def init(self):
#         OPCVForm.__init__(self)
#         OPCVViewModel.__init__(self)
#
#
# class ManualCV(object):
#     fathers = (CVViewModel,ManualCVForm)
#
#     @staticmethod
#     def init(self):
#         ManualCVForm.__init__(self)
#         CVViewModel.__init__(self)

#
# class CapCV(object):
#     fathers = (CapCVForm, CapCVViewModel,)
# 
#     @staticmethod
#     def init(self):
#         CapCVForm.__init__(self)
#         CapCVViewModel.__init__(self)
# 
# class CapCV(CapCVViewModel,CapCVForm):
# 
#     def __init__(self):
#         super(CapCV, self).__init__()


# class MetaFormViewModel(object):
#     def __new__(cls, *args, **kwargs):
#         mro = cls.mro()
#         print "mro",mro
#         return type(cls)
# 
# class CapCVT(CapCVViewModel, CapCVForm, ):
# 
#     def __init__(self):
#         super(CapCVT, self).__init__()
#         # print "mro",self.mro()


def get_view(label):
    if label == "AutomaticCV":
        return type("View", (CVViewModel, AutomaticCVForm), {})
    elif label == "ManualCV":
        return type("View", (CVViewModel, ManualCVForm), {})
    elif label == "OPCV":
        return type("View", (OPCVViewModel, OPCVForm,), {})
    elif label == "CapCV":
        return type("View", (CapCVViewModel, CapCVForm), {})
    else:
        raise TypeError("no view label correct")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    CapCVT()
    # sys.exit(app.exec_())
