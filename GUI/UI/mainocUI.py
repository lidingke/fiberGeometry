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
        MainWindow.resize(1622, 1097)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.canvas = QtGui.QWidget(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 1296, 972))
        self.canvas.setMinimumSize(QtCore.QSize(400, 400))
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.axis = QtGui.QWidget(self.centralwidget)
        self.axis.setGeometry(QtCore.QRect(1870, 150, 400, 400))
        self.axis.setMinimumSize(QtCore.QSize(400, 400))
        self.axis.setObjectName(_fromUtf8("axis"))
        self.resultShowAT = QtGui.QTextBrowser(self.axis)
        self.resultShowAT.setGeometry(QtCore.QRect(90, 220, 256, 91))
        self.resultShowAT.setMinimumSize(QtCore.QSize(10, 10))
        self.resultShowAT.setObjectName(_fromUtf8("resultShowAT"))
        self.layoutWidget_2 = QtGui.QWidget(self.axis)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 290, 171, 203))
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
        self.parameterCV = QtGui.QPushButton(self.axis)
        self.parameterCV.setEnabled(False)
        self.parameterCV.setGeometry(QtCore.QRect(50, 140, 169, 23))
        self.parameterCV.setObjectName(_fromUtf8("parameterCV"))
        self.coreMedian = QtGui.QLabel(self.axis)
        self.coreMedian.setGeometry(QtCore.QRect(90, 120, 72, 16))
        self.coreMedian.setObjectName(_fromUtf8("coreMedian"))
        self.coreMedianIndex = QtGui.QSpinBox(self.axis)
        self.coreMedianIndex.setGeometry(QtCore.QRect(110, 70, 36, 20))
        self.coreMedianIndex.setReadOnly(False)
        self.coreMedianIndex.setMinimum(3)
        self.coreMedianIndex.setMaximum(15)
        self.coreMedianIndex.setSingleStep(2)
        self.coreMedianIndex.setProperty("value", 11)
        self.coreMedianIndex.setObjectName(_fromUtf8("coreMedianIndex"))
        self.cladMedian = QtGui.QLabel(self.axis)
        self.cladMedian.setGeometry(QtCore.QRect(150, 80, 72, 16))
        self.cladMedian.setObjectName(_fromUtf8("cladMedian"))
        self.cladMedianIndex = QtGui.QSpinBox(self.axis)
        self.cladMedianIndex.setGeometry(QtCore.QRect(240, 50, 36, 20))
        self.cladMedianIndex.setReadOnly(False)
        self.cladMedianIndex.setMinimum(3)
        self.cladMedianIndex.setMaximum(17)
        self.cladMedianIndex.setSingleStep(2)
        self.cladMedianIndex.setProperty("value", 11)
        self.cladMedianIndex.setObjectName(_fromUtf8("cladMedianIndex"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1320, 20, 281, 711))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.operaLayout = QtGui.QGridLayout()
        self.operaLayout.setObjectName(_fromUtf8("operaLayout"))
        self.reporterCV = QtGui.QPushButton(self.widget)
        self.reporterCV.setEnabled(True)
        self.reporterCV.setObjectName(_fromUtf8("reporterCV"))
        self.operaLayout.addWidget(self.reporterCV, 3, 1, 1, 1)
        self.beginTestCV = QtGui.QPushButton(self.widget)
        self.beginTestCV.setMinimumSize(QtCore.QSize(50, 0))
        self.beginTestCV.setObjectName(_fromUtf8("beginTestCV"))
        self.operaLayout.addWidget(self.beginTestCV, 2, 1, 1, 1)
        self.labelCV = QtGui.QLabel(self.widget)
        self.labelCV.setObjectName(_fromUtf8("labelCV"))
        self.operaLayout.addWidget(self.labelCV, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.operaLayout)
        self.resultShowCV = QtGui.QTextBrowser(self.widget)
        self.resultShowCV.setMinimumSize(QtCore.QSize(50, 90))
        self.resultShowCV.setObjectName(_fromUtf8("resultShowCV"))
        self.verticalLayout.addWidget(self.resultShowCV)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.dynamicSharp = QtGui.QLabel(self.widget)
        self.dynamicSharp.setObjectName(_fromUtf8("dynamicSharp"))
        self.gridLayout.addWidget(self.dynamicSharp, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.coreLight = QtGui.QLabel(self.widget)
        self.coreLight.setObjectName(_fromUtf8("coreLight"))
        self.gridLayout.addWidget(self.coreLight, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.cladLight = QtGui.QLabel(self.widget)
        self.cladLight.setObjectName(_fromUtf8("cladLight"))
        self.gridLayout.addWidget(self.cladLight, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.inputLayout = QtGui.QGridLayout()
        self.inputLayout.setObjectName(_fromUtf8("inputLayout"))
        self.labelFiberType = QtGui.QLabel(self.widget)
        self.labelFiberType.setObjectName(_fromUtf8("labelFiberType"))
        self.inputLayout.addWidget(self.labelFiberType, 0, 0, 1, 1)
        self.labelLength = QtGui.QLabel(self.widget)
        self.labelLength.setObjectName(_fromUtf8("labelLength"))
        self.inputLayout.addWidget(self.labelLength, 1, 0, 1, 1)
        self.labelFactory = QtGui.QLabel(self.widget)
        self.labelFactory.setObjectName(_fromUtf8("labelFactory"))
        self.inputLayout.addWidget(self.labelFactory, 2, 0, 1, 1)
        self.labelWorker = QtGui.QLabel(self.widget)
        self.labelWorker.setObjectName(_fromUtf8("labelWorker"))
        self.inputLayout.addWidget(self.labelWorker, 4, 0, 1, 1)
        self.labelFiberNumber = QtGui.QLabel(self.widget)
        self.labelFiberNumber.setObjectName(_fromUtf8("labelFiberNumber"))
        self.inputLayout.addWidget(self.labelFiberNumber, 3, 0, 1, 1)
        self.fiberLength = QtGui.QLineEdit(self.widget)
        self.fiberLength.setObjectName(_fromUtf8("fiberLength"))
        self.inputLayout.addWidget(self.fiberLength, 1, 1, 1, 1)
        self.Worker = QtGui.QLineEdit(self.widget)
        self.Worker.setObjectName(_fromUtf8("Worker"))
        self.inputLayout.addWidget(self.Worker, 4, 1, 1, 1)
        self.factory = QtGui.QLineEdit(self.widget)
        self.factory.setObjectName(_fromUtf8("factory"))
        self.inputLayout.addWidget(self.factory, 2, 1, 1, 1)
        self.fiberNumber = QtGui.QLineEdit(self.widget)
        self.fiberNumber.setObjectName(_fromUtf8("fiberNumber"))
        self.inputLayout.addWidget(self.fiberNumber, 3, 1, 1, 1)
        self.fiberTypeBox = QtGui.QComboBox(self.widget)
        self.fiberTypeBox.setObjectName(_fromUtf8("fiberTypeBox"))
        self.inputLayout.addWidget(self.fiberTypeBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.inputLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1622, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "有源光纤几何测试平台", None))
        self.resultShowAT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">波长范围：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">最大值：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">最小值：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">平均值：</span></p></body></html>", None))
        self.parameterAT.setText(_translate("MainWindow", "参数配置", None))
        self.reporterAT.setText(_translate("MainWindow", "输出报告", None))
        self.beginTestAT.setText(_translate("MainWindow", "开始测试", None))
        self.labelAT.setText(_translate("MainWindow", "衰减：", None))
        self.parameterCV.setText(_translate("MainWindow", "参数配置", None))
        self.coreMedian.setText(_translate("MainWindow", "纤芯滤波值：", None))
        self.cladMedian.setText(_translate("MainWindow", "包层滤波值：", None))
        self.reporterCV.setText(_translate("MainWindow", "输出报告", None))
        self.beginTestCV.setText(_translate("MainWindow", "开始测试", None))
        self.labelCV.setText(_translate("MainWindow", "几何：", None))
        self.resultShowCV.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">清晰度指数：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">纤芯直径(um)：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">包层直径(um)：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">纤芯不圆度：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">包层不圆度：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">芯包同心度(um)：</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "清晰度：", None))
        self.dynamicSharp.setText(_translate("MainWindow", "0.0", None))
        self.label.setText(_translate("MainWindow", "纤芯饱和度：", None))
        self.coreLight.setText(_translate("MainWindow", "0.0", None))
        self.label_3.setText(_translate("MainWindow", "包层饱和度：", None))
        self.cladLight.setText(_translate("MainWindow", "0.0", None))
        self.labelFiberType.setText(_translate("MainWindow", "光纤规格：", None))
        self.labelLength.setText(_translate("MainWindow", "光纤长度(m)：", None))
        self.labelFactory.setText(_translate("MainWindow", "生产厂家：", None))
        self.labelWorker.setText(_translate("MainWindow", "操作人员：", None))
        self.labelFiberNumber.setText(_translate("MainWindow", "光纤编号：", None))
        self.fiberLength.setText(_translate("MainWindow", "24", None))
        self.Worker.setText(_translate("MainWindow", "12345", None))
        self.factory.setText(_translate("MainWindow", "yofc", None))
        self.fiberNumber.setText(_translate("MainWindow", "123456", None))

