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
        Form.resize(475, 200)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 409, 89))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textline = QtGui.QLabel(self.verticalLayoutWidget)
        self.textline.setObjectName(_fromUtf8("textline"))
        self.verticalLayout.addWidget(self.textline)
        self.closeButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)
        self.loadButton = QtGui.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(330, 120, 71, 23))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.okButton = QtGui.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(110, 160, 81, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 120, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputLine = QtGui.QLineEdit(Form)
        self.inputLine.setGeometry(QtCore.QRect(80, 120, 231, 20))
        self.inputLine.setObjectName(_fromUtf8("inputLine"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textline.setText(_translate("Form", "请发送串口信息：", None))
        self.closeButton.setText(_translate("Form", "关闭串口通信", None))
        self.loadButton.setText(_translate("Form", "选择", None))
        self.okButton.setText(_translate("Form", "确认", None))
        self.label.setText(_translate("Form", "请选择：", None))

