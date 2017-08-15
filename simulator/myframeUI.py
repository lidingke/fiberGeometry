# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myframe.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(591, 392)
        self.textline = QtGui.QLabel(Form)
        self.textline.setGeometry(QtCore.QRect(40, 30, 96, 16))
        self.textline.setObjectName(_fromUtf8("textline"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 541, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.loadButton = QtGui.QPushButton(self.groupBox)
        self.loadButton.setGeometry(QtCore.QRect(340, 30, 75, 23))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.okButton = QtGui.QPushButton(self.groupBox)
        self.okButton.setGeometry(QtCore.QRect(340, 60, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 84, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputLine = QtGui.QLineEdit(self.groupBox)
        self.inputLine.setGeometry(QtCore.QRect(100, 30, 221, 20))
        self.inputLine.setObjectName(_fromUtf8("inputLine"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 220, 541, 171))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.choose_light = QtGui.QLabel(self.groupBox_4)
        self.choose_light.setGeometry(QtCore.QRect(10, 30, 84, 16))
        self.choose_light.setObjectName(_fromUtf8("choose_light"))
        self.port = QtGui.QComboBox(self.groupBox_4)
        self.port.setGeometry(QtCore.QRect(100, 30, 201, 20))
        self.port.setObjectName(_fromUtf8("port"))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.port.addItem(_fromUtf8(""))
        self.change_red = QtGui.QLabel(self.groupBox_4)
        self.change_red.setGeometry(QtCore.QRect(10, 70, 84, 16))
        self.change_red.setObjectName(_fromUtf8("change_red"))
        self.red_Slider = QtGui.QSlider(self.groupBox_4)
        self.red_Slider.setGeometry(QtCore.QRect(100, 70, 281, 22))
        self.red_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_Slider.setObjectName(_fromUtf8("red_Slider"))
        self.red_light = QtGui.QLabel(self.groupBox_4)
        self.red_light.setGeometry(QtCore.QRect(400, 70, 18, 16))
        self.red_light.setObjectName(_fromUtf8("red_light"))
        self.change_green = QtGui.QLabel(self.groupBox_4)
        self.change_green.setGeometry(QtCore.QRect(10, 100, 84, 16))
        self.change_green.setObjectName(_fromUtf8("change_green"))
        self.green_Slider = QtGui.QSlider(self.groupBox_4)
        self.green_Slider.setGeometry(QtCore.QRect(100, 100, 281, 22))
        self.green_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_Slider.setObjectName(_fromUtf8("green_Slider"))
        self.green_light = QtGui.QLabel(self.groupBox_4)
        self.green_light.setGeometry(QtCore.QRect(400, 100, 18, 16))
        self.green_light.setObjectName(_fromUtf8("green_light"))
        self.light_collect = QtGui.QPushButton(self.groupBox_4)
        self.light_collect.setGeometry(QtCore.QRect(330, 30, 101, 23))
        self.light_collect.setObjectName(_fromUtf8("light_collect"))
        self.reset = QtGui.QPushButton(self.groupBox_4)
        self.reset.setGeometry(QtCore.QRect(450, 30, 75, 23))
        self.reset.setObjectName(_fromUtf8("reset"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textline.setText(_translate("Form", "请发送串口信息：", None))
        self.groupBox.setTitle(_translate("Form", "静态显示：改变获取的图像文件夹", None))
        self.loadButton.setText(_translate("Form", "选择", None))
        self.okButton.setText(_translate("Form", "确认", None))
        self.label.setText(_translate("Form", "请选择文件夹：", None))
        self.groupBox_4.setTitle(_translate("Form", "动态显示：调整背景光亮度", None))
        self.choose_light.setText(_translate("Form", "请选择光串口：", None))
        self.port.setItemText(0, _translate("Form", "com3", None))
        self.port.setItemText(1, _translate("Form", "com1", None))
        self.port.setItemText(2, _translate("Form", "com2", None))
        self.port.setItemText(3, _translate("Form", "com4", None))
        self.port.setItemText(4, _translate("Form", "com5", None))
        self.port.setItemText(5, _translate("Form", "com6", None))
        self.port.setItemText(6, _translate("Form", "com7", None))
        self.port.setItemText(7, _translate("Form", "com8", None))
        self.port.setItemText(8, _translate("Form", "com9", None))
        self.port.setItemText(9, _translate("Form", "com10", None))
        self.port.setItemText(10, _translate("Form", "com11", None))
        self.port.setItemText(11, _translate("Form", "com12", None))
        self.port.setItemText(12, _translate("Form", "com13", None))
        self.port.setItemText(13, _translate("Form", "com14", None))
        self.port.setItemText(14, _translate("Form", "com15", None))
        self.port.setItemText(15, _translate("Form", "com16", None))
        self.change_red.setText(_translate("Form", "红光光强调节：", None))
        self.red_light.setText(_translate("Form", "0.0", None))
        self.change_green.setText(_translate("Form", "绿光光强调节：", None))
        self.green_light.setText(_translate("Form", "0.0", None))
        self.light_collect.setText(_translate("Form", "背景光数据统计", None))
        self.reset.setText(_translate("Form", "重测", None))

