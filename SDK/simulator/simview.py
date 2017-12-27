#coding=utf-8
import logging
import os
from PyQt4 import QtGui, QtCore

from PyQt4.QtCore import QRect, Qt, QRectF, pyqtSignal, QObject
from PyQt4.QtGui import QWidget, QMainWindow, QPainter, QFont,\
    QPixmap, QImage, QColor, QFileDialog, QMessageBox, QPalette,\
    QGraphicsWidget, QGraphicsScene

from SDK.simulator.model import Model, Slave
from SDK.simulator.simUI import Ui_Form


class Frame(QMainWindow, Ui_Form,QObject):
    emit_dir = pyqtSignal(object)#信号槽

    emit_close=pyqtSignal()
    emit_Led=pyqtSignal(object,object,object)
    # emit_Led = pyqtSignal( object, object)
    emit_red=pyqtSignal(object)

    def __init__(self, ):
        super(Frame, self).__init__()
        self.setupUi(self)#初始化ui文件
        self.__initUI__()

    def __initUI__(self):
        self.red_Slider.setMinimum(0)
        self.red_Slider.setMaximum(1900)
        self.red_Slider.setPageStep(50)#鼠标点击步长

        self.green_Slider.setMinimum(0)
        self.green_Slider.setMaximum(3000)
        self.green_Slider.setPageStep(50)

        self.connect(self.red_Slider, QtCore.SIGNAL('valueChanged(int)'),
                     self.getLight)#将滑块的valueChanged()信号与自定义的getlight()方法向连接

        self.connect(self.green_Slider, QtCore.SIGNAL('valueChanged(int)'),
                     self.getLight)  # 将滑块的valueChanged()信号与自定义的getlight()方法向连接
        self.connect(self.port, QtCore.SIGNAL('currentIndexChanged(int)'), self.getLight)
        self.loadButton.clicked.connect(self.loadContact)
        self.okButton.clicked.connect(self.okContact)



    def getInfo(self,mystr):
        self.textline.setText(mystr)

    def getLight(self):
        red_light=self.red_Slider.value()#light为int型，要转化为字符串型显示
        green_light = self.green_Slider.value()
        port=self.port.currentText()

        self.red_light.setText(str(red_light))
        self.green_light.setText(str(green_light))
        self.emit_Led.emit(str(port),red_light,green_light)
        self.emit_red.emit(red_light)

    def loadContact(self):
        self.fileName=QtGui.QFileDialog.getExistingDirectory(self,"Open IMG ",'',)

        for f in os.listdir(self.fileName):
           if f.endswith('.BMP'):
               self.inputLine.setText(self.fileName)
           else:
               QtGui.QMessageBox.information(self, u"文件读取失败，不是BMP图像文件夹",
                                             u" \"%s\"不是BMP图像文件夹" % self.fileName)
               self.inputLine.setText("")
               return

    def okContact(self):
        self.emit_dir.emit(self.fileName)#发送文件名


    def closeEvent(self, *args, **kwargs):
        self.emit_close.emit()

    def closeEvent(self, *args, **kwargs):
        self.emit_close.emit()


class Controllers(object):

    def __init__(self):

        self.view = Frame()#初始化窗口
        self.mode = Model()#初始化Model
        self.view.emit_dir.connect(self.mode.okContact)#将信号槽内容发送到mode里的确认操作
        self.mode.emitinfodao_dir.connect(self.view.getInfo)# 将信号槽内容发送到窗口的text当中
        self.view.emit_Led.connect(self.mode.led_test)
        self.view.emit_close.connect(self.close)
        self.view.emit_red.connect(self.mode.getIMGlight)
        self.view.red_Slider.valueChanged.connect(self.mode.getIMGlight)
        self.view.light_collect.clicked.connect(self.mode.plotlight)
        self.view.reset.clicked.connect(self.mode.reset)


    def show(self):
        # self.mode.start()
        self.view.show()#窗口显示

    def close(self):
        self.mode.close()