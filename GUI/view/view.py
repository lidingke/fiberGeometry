#coding:utf-8
#branch dev
from PyQt4.QtCore import pyqtSignal

from GUI.model.models import session_add_by_account
from GUI.model.stateconf import state_number
from setting.orderset import SETTING
import cv2
# from GUI.UI.mainUI import Ui_MainWindow
import logging
from GUI.UI.mainUI import Ui_MainWindow as new_MainWindow

from GUI.view.opplot import OpticalPlot
from .reporter import Reporter
from pattern.sharp import MaxSharp
from PyQt4.QtCore import QRect, Qt, QRectF
from PyQt4.QtGui import QWidget, QMainWindow, QPainter, QFont,\
    QPixmap, QImage, QColor, QFileDialog, QMessageBox, QPalette,\
    QGraphicsWidget, QGraphicsScene
import numpy as np
from util.load import WriteReadJson, WRpickle
from datetime import datetime

class View(QMainWindow, new_MainWindow):
    """docstring for View"""
    # __slot__ = ("scence","pximapimg")
    emit_close_event = pyqtSignal()

    def __init__(self,):
        super(View, self).__init__()
        self.setupUi(self)
        # self.painterWidget = CVPainterWidget(self.canvas)
        # self.scence = MyQGraphicsScene()
        self.scence = QGraphicsScene()
        # print dir(self.scence)
        self.graphicsView.setScene(self.scence)
        # self.graphicsView.setCacheMode()
        # self.axisWidget = OpticalPlot(parent=self.axis)
        self.IS_INIT_PAINTER = False
        self.__initUI__()
        # self.reporterCV.clicked.connect(self.writeReporterCV)
        self._tempMedianIndex()
        self.isMaxSharp = MaxSharp()
        # logging.basicConfig(filename="setting\\modelog.txt", filemode='a', level=logging.ERROR,
        #                     format="%(asctime)s-%(levelname)s-%(funcName)s:%(message)s")
        self.state_4_next = state_number()

    def __initUI__(self):
        # items = ['G652']
        # self.fiberType.addItems(items)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setFixedSize(self.width(),self.height())
        self.beginTestCV.clicked.connect(self._disableCVButton)
        self._initItems()
        self.reporterCV.clicked.connect(self.writeReporterCV)
        self.initGUI()


    def _initItems(self):
        # wrJson = WriteReadJson("setting\\userdata.json")
        wrp = WRpickle("setting\\userdata.pickle")
        try:
            load = wrp.loadPick()
        except IOError:
            wrJson = WriteReadJson("setting\\userdata.json")
            load = wrJson.load()
        types = load.get("fiberTypes")
        self.fiberTypeBox.addItems(types)

    def updatePixmap(self, arr, sharp):
        if not self.IS_INIT_PAINTER:
            self.IS_INIT_PAINTER = True
        self.pximapimg = self._getPixmap(arr)

        self.scence.clear()
        self.scence.addPixmap(self.pximapimg)
        # self.painterWidget.getPixmap(arr)
        if hasattr(self, 'dynamicSharp'):
            self.dynamicSharp.setText(sharp)
            if self.isMaxSharp.isRight(sharp):
                self.dynamicSharp.setStyleSheet("color:red")
            else:
                self.dynamicSharp.setStyleSheet("color:white")


    def getModel(self, model):
        self.model = model

    def closeEvent(self, *args, **kwargs):
        # result = SETTING()['tempLight']
        # print 'get light result', result
        # WriteReadJson('tests/data/light.json').save(result)
        if 'olddata' in SETTING().keys():
            self.olddata.save(SETTING()['olddata'])
        self.emit_close_event.emit()
        # self.model.exit()

    def updateOpticalview(self, wave, powers):
        self.axisWidget.XYaxit(wave, powers)

    # def attenuationTest(self):
    #     length = self.fiberLength.getText()
    #     threading.Thread
    # def attenuationGetThread(self, length):

    def updateCVShow(self,str_):
        if str_:
            self.resultShowCV.setText(str_)
        self._disableCVButton(True)

    def _disableCVButton(self, bool = False):
        self.beginTestCV.setEnabled(bool)

    def updateATShow(self,str_):
        self.resultShowAT.setText(str_)

    def initGUI(self):
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
        para['title'] = para['fibertype']+'光纤端面几何测试报告'
        SETTING()['pdfpara'].update(para)
        SETTING()['olddata'] = para
        Reporter(self)
        # print 'get in session'
        SETTING()['dbpara'].update(para)
        dbpara = SETTING()['dbpara']
        session_add_by_account(dbpara)

    def _tempMedianIndex(self):
        def changeCoreIndex():
            index = self.coreMedianIndex.value()
            SETTING()["medianBlur"]["corefilter"] = index
        def changeCladIndex():
            index = self.cladMedianIndex.value()
            SETTING()["medianBlur"]["cladfilter"] = index
        if hasattr(self, "cladMedianIndex"):
            self.cladMedianIndex.valueChanged.connect(changeCladIndex)
        if hasattr(self, "coreMedianIndex"):
            self.coreMedianIndex.valueChanged.connect(changeCoreIndex)

    def getCoreLight(self, coreLight, cladLight):
        if hasattr(self, "coreLight"):
            self.coreLight.setText(coreLight)
        if hasattr(self, "cladLight"):
            self.cladLight.setText(cladLight)


    def _getPixmap(self, mapArray):
        # self.ellipses, self.result = plotResults
        if not isinstance(mapArray, np.ndarray):
            raise ValueError('get Pixmap ERROR input')
        height, width, bytesPerComponent = mapArray.shape
        bytesPerLine = bytesPerComponent * width
        img = QImage(mapArray.data, width, height, bytesPerLine, QImage.Format_RGB888)# img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        return QPixmap.fromImage(img)
        # self.update()



class MyQGraphicsScene(QGraphicsScene):

    def __init__(self):
        QGraphicsScene.__init__(self)
        # super(MyQGraphicsScene, self).__init__()
        self.rect_pos = [False,False]
        # self.setBspTreeDepth(1)

    def mousePressEvent(self,event):
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


