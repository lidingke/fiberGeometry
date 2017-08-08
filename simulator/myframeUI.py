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
        Form.resize(748, 274)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(19, 20, 501, 207))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textline = QtGui.QLabel(self.widget)
        self.textline.setObjectName(_fromUtf8("textline"))
        self.verticalLayout.addWidget(self.textline)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
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
        self.gridLayout.addWidget(self.okButton, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textline.setText(_translate("Form", "请发送串口信息：", None))
        self.closeButton.setText(_translate("Form", "关闭串口通信", None))
        self.label.setText(_translate("Form", "请选择：", None))
        self.loadButton.setText(_translate("Form", "选择", None))
        self.okButton.setText(_translate("Form", "确认", None))

