# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainoc.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1542, 1029)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.canvas = QtGui.QWidget(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 1296, 972))
        self.canvas.setMinimumSize(QtCore.QSize(400, 400))
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1320, 20, 171, 111))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.operaLayout = QtGui.QGridLayout(self.layoutWidget)
        self.operaLayout.setObjectName(_fromUtf8("operaLayout"))
        self.parameterCV = QtGui.QPushButton(self.layoutWidget)
        self.parameterCV.setEnabled(False)
        self.parameterCV.setObjectName(_fromUtf8("parameterCV"))
        self.operaLayout.addWidget(self.parameterCV, 4, 1, 1, 1)
        self.beginTestCV = QtGui.QPushButton(self.layoutWidget)
        self.beginTestCV.setMinimumSize(QtCore.QSize(50, 0))
        self.beginTestCV.setObjectName(_fromUtf8("beginTestCV"))
        self.operaLayout.addWidget(self.beginTestCV, 2, 1, 1, 1)
        self.reporterCV = QtGui.QPushButton(self.layoutWidget)
        self.reporterCV.setEnabled(False)
        self.reporterCV.setObjectName(_fromUtf8("reporterCV"))
        self.operaLayout.addWidget(self.reporterCV, 3, 1, 1, 1)
        self.labelCV = QtGui.QLabel(self.layoutWidget)
        self.labelCV.setObjectName(_fromUtf8("labelCV"))
        self.operaLayout.addWidget(self.labelCV, 0, 1, 1, 1)
        self.axis = QtGui.QWidget(self.centralwidget)
        self.axis.setGeometry(QtCore.QRect(1590, 190, 400, 400))
        self.axis.setMinimumSize(QtCore.QSize(400, 400))
        self.axis.setObjectName(_fromUtf8("axis"))
        self.resultShowAT = QtGui.QTextBrowser(self.axis)
        self.resultShowAT.setGeometry(QtCore.QRect(90, 220, 256, 91))
        self.resultShowAT.setMinimumSize(QtCore.QSize(10, 10))
        self.resultShowAT.setObjectName(_fromUtf8("resultShowAT"))
        self.layoutWidget1 = QtGui.QWidget(self.axis)
        self.layoutWidget1.setGeometry(QtCore.QRect(110, 100, 201, 222))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.inputLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.inputLayout.setObjectName(_fromUtf8("inputLayout"))
        self.labelFiberType = QtGui.QLabel(self.layoutWidget1)
        self.labelFiberType.setObjectName(_fromUtf8("labelFiberType"))
        self.inputLayout.addWidget(self.labelFiberType, 0, 0, 1, 1)
        self.labelLength = QtGui.QLabel(self.layoutWidget1)
        self.labelLength.setObjectName(_fromUtf8("labelLength"))
        self.inputLayout.addWidget(self.labelLength, 1, 0, 1, 1)
        self.labelFactory = QtGui.QLabel(self.layoutWidget1)
        self.labelFactory.setObjectName(_fromUtf8("labelFactory"))
        self.inputLayout.addWidget(self.labelFactory, 2, 0, 1, 1)
        self.labelWorker = QtGui.QLabel(self.layoutWidget1)
        self.labelWorker.setObjectName(_fromUtf8("labelWorker"))
        self.inputLayout.addWidget(self.labelWorker, 4, 0, 1, 1)
        self.labelFiberNumber = QtGui.QLabel(self.layoutWidget1)
        self.labelFiberNumber.setObjectName(_fromUtf8("labelFiberNumber"))
        self.inputLayout.addWidget(self.labelFiberNumber, 3, 0, 1, 1)
        self.fiberLength = QtGui.QLineEdit(self.layoutWidget1)
        self.fiberLength.setObjectName(_fromUtf8("fiberLength"))
        self.inputLayout.addWidget(self.fiberLength, 1, 1, 1, 1)
        self.fiberType = QtGui.QComboBox(self.layoutWidget1)
        self.fiberType.setObjectName(_fromUtf8("fiberType"))
        self.inputLayout.addWidget(self.fiberType, 0, 1, 1, 1)
        self.Worker = QtGui.QLineEdit(self.layoutWidget1)
        self.Worker.setObjectName(_fromUtf8("Worker"))
        self.inputLayout.addWidget(self.Worker, 4, 1, 1, 1)
        self.factory = QtGui.QLineEdit(self.layoutWidget1)
        self.factory.setObjectName(_fromUtf8("factory"))
        self.inputLayout.addWidget(self.factory, 2, 1, 1, 1)
        self.fiberNumber = QtGui.QLineEdit(self.layoutWidget1)
        self.fiberNumber.setObjectName(_fromUtf8("fiberNumber"))
        self.inputLayout.addWidget(self.fiberNumber, 3, 1, 1, 1)
        self.layoutWidget_2 = QtGui.QWidget(self.axis)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 290, 171, 111))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.attenuationLayout = QtGui.QGridLayout(self.layoutWidget_2)
        self.attenuationLayout.setObjectName(_fromUtf8("attenuationLayout"))
        self.parameterAT = QtGui.QPushButton(self.layoutWidget_2)
        self.parameterAT.setObjectName(_fromUtf8("parameterAT"))
        self.attenuationLayout.addWidget(self.parameterAT, 4, 1, 1, 1)
        self.reporterAT = QtGui.QPushButton(self.layoutWidget_2)
        self.reporterAT.setObjectName(_fromUtf8("reporterAT"))
        self.attenuationLayout.addWidget(self.reporterAT, 3, 1, 1, 1)
        self.beginTestAT = QtGui.QPushButton(self.layoutWidget_2)
        self.beginTestAT.setMinimumSize(QtCore.QSize(50, 0))
        self.beginTestAT.setObjectName(_fromUtf8("beginTestAT"))
        self.attenuationLayout.addWidget(self.beginTestAT, 2, 1, 1, 1)
        self.labelAT = QtGui.QLabel(self.layoutWidget_2)
        self.labelAT.setObjectName(_fromUtf8("labelAT"))
        self.attenuationLayout.addWidget(self.labelAT, 1, 1, 1, 1)
        self.resultShowCV = QtGui.QTextBrowser(self.centralwidget)
        self.resultShowCV.setGeometry(QtCore.QRect(1320, 150, 191, 111))
        self.resultShowCV.setMinimumSize(QtCore.QSize(50, 90))
        self.resultShowCV.setObjectName(_fromUtf8("resultShowCV"))
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(1320, 280, 181, 84))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.dynamicSharp = QtGui.QLabel(self.layoutWidget2)
        self.dynamicSharp.setObjectName(_fromUtf8("dynamicSharp"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.dynamicSharp)
        self.coreMedian = QtGui.QLabel(self.layoutWidget2)
        self.coreMedian.setObjectName(_fromUtf8("coreMedian"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.coreMedian)
        self.coreMedianIndex = QtGui.QSpinBox(self.layoutWidget2)
        self.coreMedianIndex.setReadOnly(False)
        self.coreMedianIndex.setMinimum(3)
        self.coreMedianIndex.setMaximum(15)
        self.coreMedianIndex.setSingleStep(2)
        self.coreMedianIndex.setProperty("value", 11)
        self.coreMedianIndex.setObjectName(_fromUtf8("coreMedianIndex"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.coreMedianIndex)
        self.cladMedian = QtGui.QLabel(self.layoutWidget2)
        self.cladMedian.setObjectName(_fromUtf8("cladMedian"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.cladMedian)
        self.cladMedianIndex = QtGui.QSpinBox(self.layoutWidget2)
        self.cladMedianIndex.setReadOnly(False)
        self.cladMedianIndex.setMinimum(3)
        self.cladMedianIndex.setMaximum(17)
        self.cladMedianIndex.setSingleStep(2)
        self.cladMedianIndex.setProperty("value", 11)
        self.cladMedianIndex.setObjectName(_fromUtf8("cladMedianIndex"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cladMedianIndex)
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.coreLight = QtGui.QLabel(self.layoutWidget2)
        self.coreLight.setObjectName(_fromUtf8("coreLight"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.coreLight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1542, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "八边形几何测试平台", None))
        self.parameterCV.setText(_translate("MainWindow", "参数配置", None))
        self.beginTestCV.setText(_translate("MainWindow", "开始测试", None))
        self.reporterCV.setText(_translate("MainWindow", "输出报告", None))
        self.labelCV.setText(_translate("MainWindow", "几何：", None))
        self.resultShowAT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">波长范围：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">最大值：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">最小值：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">平均值：</p></body></html>", None))
        self.labelFiberType.setText(_translate("MainWindow", "光纤规格：", None))
        self.labelLength.setText(_translate("MainWindow", "光纤长度(km)：", None))
        self.labelFactory.setText(_translate("MainWindow", "生产厂家：", None))
        self.labelWorker.setText(_translate("MainWindow", "操作人员：", None))
        self.labelFiberNumber.setText(_translate("MainWindow", "光纤编号：", None))
        self.fiberLength.setText(_translate("MainWindow", "24", None))
        self.Worker.setText(_translate("MainWindow", "12345", None))
        self.factory.setText(_translate("MainWindow", "yofc", None))
        self.fiberNumber.setText(_translate("MainWindow", "123456", None))
        self.parameterAT.setText(_translate("MainWindow", "参数配置", None))
        self.reporterAT.setText(_translate("MainWindow", "输出报告", None))
        self.beginTestAT.setText(_translate("MainWindow", "开始测试", None))
        self.labelAT.setText(_translate("MainWindow", "衰减：", None))
        self.resultShowCV.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">清晰度指数：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">纤芯直径：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">包层直径：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">纤芯不圆度：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">包层不圆度：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">芯包同心度：</p></body></html>", None))
        self.dynamicSharp.setText(_translate("MainWindow", "0.0", None))
        self.coreMedian.setText(_translate("MainWindow", "纤芯滤波值：", None))
        self.cladMedian.setText(_translate("MainWindow", "包层滤波值：", None))
        self.label.setText(_translate("MainWindow", "纤芯亮度：", None))
        self.coreLight.setText(_translate("MainWindow", "0.0", None))

