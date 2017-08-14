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
        Form.resize(591, 390)
        self.textline = QtGui.QLabel(Form)
        self.textline.setGeometry(QtCore.QRect(40, 30, 96, 16))
        self.textline.setObjectName(_fromUtf8("textline"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(31, 126, 481, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputLine = QtGui.QLineEdit(self.widget)
        self.inputLine.setObjectName(_fromUtf8("inputLine"))
        self.gridLayout.addWidget(self.inputLine, 0, 1, 1, 1)
        self.loadButton = QtGui.QPushButton(self.widget)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.gridLayout.addWidget(self.loadButton, 0, 2, 1, 1)
        self.okButton = QtGui.QPushButton(self.widget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.gridLayout.addWidget(self.okButton, 1, 2, 1, 1)
        self.choose_light = QtGui.QLabel(self.widget)
        self.choose_light.setObjectName(_fromUtf8("choose_light"))
        self.gridLayout.addWidget(self.choose_light, 2, 0, 1, 1)
        self.port = QtGui.QComboBox(self.widget)
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
        self.gridLayout.addWidget(self.port, 2, 1, 1, 1)
        self.change_red = QtGui.QLabel(self.widget)
        self.change_red.setObjectName(_fromUtf8("change_red"))
        self.gridLayout.addWidget(self.change_red, 3, 0, 1, 1)
        self.red_Slider = QtGui.QSlider(self.widget)
        self.red_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_Slider.setObjectName(_fromUtf8("red_Slider"))
        self.gridLayout.addWidget(self.red_Slider, 3, 1, 1, 1)
        self.red_light = QtGui.QLabel(self.widget)
        self.red_light.setObjectName(_fromUtf8("red_light"))
        self.gridLayout.addWidget(self.red_light, 3, 2, 1, 1)
        self.change_green = QtGui.QLabel(self.widget)
        self.change_green.setObjectName(_fromUtf8("change_green"))
        self.gridLayout.addWidget(self.change_green, 4, 0, 1, 1)
        self.green_Slider = QtGui.QSlider(self.widget)
        self.green_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_Slider.setObjectName(_fromUtf8("green_Slider"))
        self.gridLayout.addWidget(self.green_Slider, 4, 1, 1, 1)
        self.green_light = QtGui.QLabel(self.widget)
        self.green_light.setObjectName(_fromUtf8("green_light"))
        self.gridLayout.addWidget(self.green_light, 4, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textline.setText(_translate("Form", "请发送串口信息：", None))
        self.label.setText(_translate("Form", "请选择文件夹：", None))
        self.loadButton.setText(_translate("Form", "选择", None))
        self.okButton.setText(_translate("Form", "确认", None))
        self.choose_light.setText(_translate("Form", "请选择光串口：", None))
        self.port.setItemText(0, _translate("Form", "com1", None))
        self.port.setItemText(1, _translate("Form", "com2", None))
        self.port.setItemText(2, _translate("Form", "com3", None))
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

