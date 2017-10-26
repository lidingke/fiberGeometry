# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modbus.ui'
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
        Form.resize(574, 144)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stateText = QtGui.QLabel(Form)
        self.stateText.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.stateText.setObjectName(_fromUtf8("stateText"))
        self.horizontalLayout.addWidget(self.stateText)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.move_up = QtGui.QPushButton(Form)
        self.move_up.setObjectName(_fromUtf8("move_up"))
        self.gridLayout_4.addWidget(self.move_up, 1, 1, 1, 1)
        self.move_left = QtGui.QPushButton(Form)
        self.move_left.setObjectName(_fromUtf8("move_left"))
        self.gridLayout_4.addWidget(self.move_left, 2, 0, 1, 1)
        self.move_down = QtGui.QPushButton(Form)
        self.move_down.setObjectName(_fromUtf8("move_down"))
        self.gridLayout_4.addWidget(self.move_down, 2, 1, 1, 1)
        self.move_right = QtGui.QPushButton(Form)
        self.move_right.setObjectName(_fromUtf8("move_right"))
        self.gridLayout_4.addWidget(self.move_right, 2, 2, 1, 1)
        self.reset = QtGui.QPushButton(Form)
        self.reset.setObjectName(_fromUtf8("reset"))
        self.gridLayout_4.addWidget(self.reset, 1, 2, 1, 1)
        self.next_state = QtGui.QPushButton(Form)
        self.next_state.setObjectName(_fromUtf8("next_state"))
        self.gridLayout_4.addWidget(self.next_state, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.stateText.setText(_translate("Form", "state", None))
        self.move_up.setText(_translate("Form", "up", None))
        self.move_left.setText(_translate("Form", "left", None))
        self.move_down.setText(_translate("Form", "down", None))
        self.move_right.setText(_translate("Form", "right", None))
        self.reset.setText(_translate("Form", "reset", None))
        self.next_state.setText(_translate("Form", "next", None))

