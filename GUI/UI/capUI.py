# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap.ui'
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
        Form.resize(350, 350)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_cap_fibre = QtGui.QLabel(Form)
        self.label_cap_fibre.setObjectName(_fromUtf8("label_cap_fibre"))
        self.gridLayout.addWidget(self.label_cap_fibre, 0, 0, 1, 1)
        self.cap_fibre = QtGui.QLineEdit(Form)
        self.cap_fibre.setObjectName(_fromUtf8("cap_fibre"))
        self.gridLayout.addWidget(self.cap_fibre, 0, 1, 1, 1)
        self.label_cap_mc = QtGui.QLabel(Form)
        self.label_cap_mc.setObjectName(_fromUtf8("label_cap_mc"))
        self.gridLayout.addWidget(self.label_cap_mc, 1, 0, 1, 1)
        self.cap_mc = QtGui.QComboBox(Form)
        self.cap_mc.setModelColumn(0)
        self.cap_mc.setObjectName(_fromUtf8("cap_mc"))
        self.cap_mc.addItem(_fromUtf8(""))
        self.cap_mc.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cap_mc, 1, 1, 1, 1)
        self.label_cap_bt = QtGui.QLabel(Form)
        self.label_cap_bt.setObjectName(_fromUtf8("label_cap_bt"))
        self.gridLayout.addWidget(self.label_cap_bt, 2, 0, 1, 1)
        self.cap_bt = QtGui.QComboBox(Form)
        self.cap_bt.setObjectName(_fromUtf8("cap_bt"))
        self.cap_bt.addItem(_fromUtf8(""))
        self.cap_bt.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cap_bt, 2, 1, 1, 1)
        self.label_cap_operator = QtGui.QLabel(Form)
        self.label_cap_operator.setObjectName(_fromUtf8("label_cap_operator"))
        self.gridLayout.addWidget(self.label_cap_operator, 3, 0, 1, 1)
        self.cap_operator = QtGui.QLineEdit(Form)
        self.cap_operator.setObjectName(_fromUtf8("cap_operator"))
        self.gridLayout.addWidget(self.cap_operator, 3, 1, 1, 1)
        self.label_cap_machine = QtGui.QLabel(Form)
        self.label_cap_machine.setObjectName(_fromUtf8("label_cap_machine"))
        self.gridLayout.addWidget(self.label_cap_machine, 4, 0, 1, 1)
        self.cap_machine = QtGui.QLineEdit(Form)
        self.cap_machine.setObjectName(_fromUtf8("cap_machine"))
        self.gridLayout.addWidget(self.cap_machine, 4, 1, 1, 1)
        self.cap_diffrange = QtGui.QSpinBox(Form)
        self.cap_diffrange.setMinimum(10)
        self.cap_diffrange.setMaximum(972)
        self.cap_diffrange.setSingleStep(10)
        self.cap_diffrange.setProperty("value", 500)
        self.cap_diffrange.setObjectName(_fromUtf8("cap_diffrange"))
        self.gridLayout.addWidget(self.cap_diffrange, 5, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.cap_mc.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_cap_fibre.setText(_translate("Form", "Fibre：", None))
        self.cap_fibre.setText(_translate("Form", "1234567", None))
        self.label_cap_mc.setText(_translate("Form", "M(easure)/C(opy):", None))
        self.cap_mc.setItemText(0, _translate("Form", "M", None))
        self.cap_mc.setItemText(1, _translate("Form", "C", None))
        self.label_cap_bt.setText(_translate("Form", "B(ottom)/T(op)  :", None))
        self.cap_bt.setItemText(0, _translate("Form", "B", None))
        self.cap_bt.setItemText(1, _translate("Form", "T", None))
        self.label_cap_operator.setText(_translate("Form", "Operator:", None))
        self.cap_operator.setText(_translate("Form", "037", None))
        self.label_cap_machine.setText(_translate("Form", "Machine:", None))
        self.cap_machine.setText(_translate("Form", "001", None))
        self.label.setText(_translate("Form", "diff radius (pix)", None))

