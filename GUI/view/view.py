#coding:utf-8
from setting.orderset import SETTING
import cv2
from GUI.UI.mainUI import Ui_MainWindow
fibertype = SETTING().get("fiberType", "G652")
if fibertype == "octagon":
    from GUI.UI.mainocUI import Ui_MainWindow as new_MainWindow
elif fibertype in ("20400","G652"):
    from GUI.UI.mainocUI import Ui_MainWindow as new_MainWindow
else:
    from GUI.UI.mainUI import Ui_MainWindow as new_MainWindow
from util.load import WriteReadJson
from GUI.view.opplot import OpticalPlot
from .reporter import Reporter
from pattern.sharp import MaxSharp
from PyQt4.QtCore import QRect, Qt
from PyQt4.QtGui import QWidget, QMainWindow, QPainter, QFont,\
    QPixmap, QImage, QColor, QFileDialog, QMessageBox, QPalette
import numpy as np
from util.load import WriteReadJson
from datetime import datetime as dt

class View(QMainWindow, new_MainWindow):
    """docstring for View"""

    def __init__(self,):
        super(View, self).__init__()
        self.setupUi(self)
        self.painterWidget = CVPainterWidget(self.canvas)
        self.axisWidget = OpticalPlot(parent=self.axis)
        self.IS_INIT_PAINTER = False
        self.__initUI__()
        # self.reporterCV.clicked.connect(self.writeReporterCV)
        self._tempMedianIndex()
        self.isMaxSharp = MaxSharp()

    def __initUI__(self):
        # items = ['G652']
        # self.fiberType.addItems(items)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.width(),self.height())
        self.beginTestCV.clicked.connect(self._disableCVButton)
        self._initItems()
        self.reporterCV.clicked.connect(self.writeReporterCV)

    def _initItems(self):
        wrJson = WriteReadJson("setting\\userdata.json")
        types = wrJson.load().get("fiberTypes")
        self.fiberTypeBox.addItems(types)

    def updatePixmap(self, arr, sharp):
        #todo : set Text box
        if not self.IS_INIT_PAINTER:
            self.painterWidget.initPixmap(arr)
            self.IS_INIT_PAINTER = True
        self.painterWidget.getPixmap(arr)
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
        self.model.exit()

    def updateOpticalview(self, wave, powers):
        self.axisWidget.XYaxit(wave, powers)

    # def attenuationTest(self):
    #     length = self.fiberLength.getText()
    #     threading.Thread
    #
    # def attenuationGetThread(self, length):

    def updateCVShow(self,str_):
        self.resultShowCV.setText(str_)
        self._disableCVButton(True)

    def _disableCVButton(self, bool = False):
        self.beginTestCV.setEnabled(bool)

    def updateATShow(self,str_):
        self.resultShowAT.setText(str_)

    def writeReporterCV(self):
        para = {}
        para['fiberLength'] = self.fiberLength.text()
        para['worker'] = self.Worker.text()
        para['producer'] = self.factory.text()
        para['fiberNo'] = self.fiberNumber.text()
        para['fibertype'] = self.fiberTypeBox.currentIndex()
        para['date'] = dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')
        para['title'] = '测试报告'
        SETTING()['pdfpara'].update(para)
        Reporter(self)


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

    def getCoreLight(self, green):
        self.coreLight.setText(green)


class CVPainterWidget(QWidget):
    """docstring for PainterWidget"""
    def __init__(self, parent):
        super(CVPainterWidget, self).__init__(parent)
        self.pixmap = False
        self.painter = QPainter(self)
        self.ellipses, self.result = False, False

    def initPixmap(self, mapArray):
        try:
            width, height, size = mapArray.shape
        except Exception, e:
            width, height = mapArray.shape
        self.width = width
        self.height = height
        self.rect = QRect(0, 0,height, width )
        self.setGeometry(self.rect)

    def paintEvent(self, event):

        if self.pixmap:
            # print 'rect', self.rect
            self.painter.begin(self)
            self.painter.drawPixmap(self.rect, self.pixmap)
            # self._decorateImg(self.painter)
            self.painter.end()

    # def _decorateImg(self, painter):
    #     if self.ellipses or self.result:
    #         pass

    def getPixmap(self, mapArray):
        #todo: image format error
        # self.ellipses, self.result = plotResults
        if not isinstance(mapArray, np.ndarray):
            raise ValueError('get Pixmap ERROR input')
        if len(mapArray.shape) >= 3:
            height, width, bytesPerComponent = mapArray.shape
            bytesPerLine = bytesPerComponent * width
            img = QImage(mapArray.data, width, height, bytesPerLine, QImage.Format_RGB888)
        else:
            img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        # img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        self.pixmap = QPixmap.fromImage(img)
        self.update()
