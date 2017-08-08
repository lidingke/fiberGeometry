#coding=utf-8
import os
from PyQt4 import  QtGui

from PyQt4.QtCore import QRect, Qt, QRectF, pyqtSignal, QObject
from PyQt4.QtGui import QWidget, QMainWindow, QPainter, QFont,\
    QPixmap, QImage, QColor, QFileDialog, QMessageBox, QPalette,\
    QGraphicsWidget, QGraphicsScene

from simulator.model import Model, Slave
from simulator.myframeUI import Ui_Form as new_MainWindow


class Frame(QMainWindow, new_MainWindow,QObject):
    emit_dir = pyqtSignal(object)#信号槽
    emit_close=pyqtSignal()
    def __init__(self, ):
        super(Frame, self).__init__()
        self.setupUi(self)#初始化ui文件
        self.__initUI__()

    def __initUI__(self):
        self.loadButton.clicked.connect(self.loadContact)
        self.okButton.clicked.connect(self.okContact)

    def getInfo(self,mystr):
        self.textline.setText(mystr)


    def loadContact(self):
        self.fileName=QtGui.QFileDialog.getExistingDirectory(self,"Open IMG ",'',)

        for f in os.listdir(self.fileName):

           if f.endswith('.BMP'):
               self.inputLine.setText(self.fileName)
           else:
               QtGui.QMessageBox.information(self, u"文件读取失败，不是BMP图像文件夹",
                                             u" \"%s\"不是BMP图像文件夹" % self.fileName)
               return

    def okContact(self):
        self.emit_dir.emit(self.fileName)#发送文件名

    def closeEvent(self, *args, **kwargs):
        self.emit_close.emit()



class Controllers(object):

    def __init__(self):

        self.view = Frame()#初始化窗口
        self.mode = Model()#初始化Model
        self.view.emit_dir.connect(self.mode.okContact)#将信号槽内容发送到mode里的确认操作
        self.mode.emitinfodao_dir.connect(self.view.getInfo)# 将信号槽内容发送到窗口的text当中
        self.view.emit_close.connect(self.close)


    def show(self):
        # self.mode.start()
        self.view.show()#窗口显示

    def close(self):
        self.mode.close()