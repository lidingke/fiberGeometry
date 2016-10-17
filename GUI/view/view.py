from GUI.UI.mainUI import Ui_MainWindow

from PyQt4.QtCore import QRect
from PyQt4.QtGui import QWidget, QMainWindow, QPainter,QFont,\
QPixmap, QImage, QColor
from method.toolkit import timing
import time
import numpy as np
import cv2

import pdb


class View(QMainWindow,Ui_MainWindow):
    """docstring for View"""

    def __init__(self,):
        super(View, self).__init__()

        self.setupUi(self)
        self.painterWidget = PainterWidget(self.widget)
        # self.painterWidget.getPixmap(self.readImg())
        # self.addWidget(pw)
        self.IS_INIT_PAINTER = False
        font = QFont("Microsoft YaHei", 20, 75)
        self.sharpLabel.setFont(font)

    def readImg(self):
        img = cv2.imread("IMG\\7core2.bmp")
        return img

    # @timing
    def updatePixmap(self,arr, sharp):
        if not self.IS_INIT_PAINTER:
            self.painterWidget.initPixmap(arr)
            self.IS_INIT_PAINTER = True
        self.painterWidget.getPixmap(arr)
        self.sharpLabel.setText(sharp)

    def getModel(self, model):
        self.model = model

    def closeEvent(self, *args, **kwargs):
        self.model.exit()


class PainterWidget(QWidget):
    """docstring for PainterWidget"""
    def __init__(self, parent):
        super(PainterWidget, self).__init__(parent)
        # self.arg = arg
        self.pixmap = False
        self.painter = QPainter(self)

    def initPixmap(self, mapArray):
        """Init pixmap after get image,
        so this map can't init in __init__"""
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
            self.painter.end()


    def getPixmap(self, mapArray):

        img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)

        self.pixmap = QPixmap.fromImage(img)
        self.update()
