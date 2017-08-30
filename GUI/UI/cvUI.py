# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cv.ui'
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
        MainWindow.resize(1809, 1129)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(600, 400))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.graphicsView.setMidLineWidth(0)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.graphicsView.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.cvOperatorLayout = QtGui.QVBoxLayout()
        self.cvOperatorLayout.setObjectName(_fromUtf8("cvOperatorLayout"))
        self.operaLayout = QtGui.QGridLayout()
        self.operaLayout.setObjectName(_fromUtf8("operaLayout"))
        self.reporterCV = QtGui.QPushButton(self.centralwidget)
        self.reporterCV.setEnabled(True)
        self.reporterCV.setObjectName(_fromUtf8("reporterCV"))
        self.operaLayout.addWidget(self.reporterCV, 3, 1, 1, 1)
        self.beginTestCV = QtGui.QPushButton(self.centralwidget)
        self.beginTestCV.setMinimumSize(QtCore.QSize(50, 0))
        self.beginTestCV.setObjectName(_fromUtf8("beginTestCV"))
        self.operaLayout.addWidget(self.beginTestCV, 2, 1, 1, 1)
        self.labelCV = QtGui.QLabel(self.centralwidget)
        self.labelCV.setObjectName(_fromUtf8("labelCV"))
        self.operaLayout.addWidget(self.labelCV, 0, 1, 1, 1)
        self.cvOperatorLayout.addLayout(self.operaLayout)
        self.resultShowCV = QtGui.QTextBrowser(self.centralwidget)
        self.resultShowCV.setMinimumSize(QtCore.QSize(200, 200))
        self.resultShowCV.setObjectName(_fromUtf8("resultShowCV"))
        self.cvOperatorLayout.addWidget(self.resultShowCV)
        self.RIShow = QtGui.QWidget(self.centralwidget)
        self.RIShow.setMinimumSize(QtCore.QSize(0, 200))
        self.RIShow.setObjectName(_fromUtf8("RIShow"))
        self.cvOperatorLayout.addWidget(self.RIShow)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.light = QtGui.QLabel(self.centralwidget)
        self.light.setObjectName(_fromUtf8("light"))
        self.gridLayout.addWidget(self.light, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.dynamicSharp = QtGui.QLabel(self.centralwidget)
        self.dynamicSharp.setObjectName(_fromUtf8("dynamicSharp"))
        self.gridLayout.addWidget(self.dynamicSharp, 0, 1, 1, 1)
        self.cvOperatorLayout.addLayout(self.gridLayout)
        self.inputLayout = QtGui.QGridLayout()
        self.inputLayout.setObjectName(_fromUtf8("inputLayout"))
        self.fiberNumber = QtGui.QLineEdit(self.centralwidget)
        self.fiberNumber.setObjectName(_fromUtf8("fiberNumber"))
        self.inputLayout.addWidget(self.fiberNumber, 3, 1, 1, 1)
        self.Worker = QtGui.QLineEdit(self.centralwidget)
        self.Worker.setObjectName(_fromUtf8("Worker"))
        self.inputLayout.addWidget(self.Worker, 4, 1, 1, 1)
        self.labelFiberNumber = QtGui.QLabel(self.centralwidget)
        self.labelFiberNumber.setObjectName(_fromUtf8("labelFiberNumber"))
        self.inputLayout.addWidget(self.labelFiberNumber, 3, 0, 1, 1)
        self.factory = QtGui.QLineEdit(self.centralwidget)
        self.factory.setObjectName(_fromUtf8("factory"))
        self.inputLayout.addWidget(self.factory, 2, 1, 1, 1)
        self.labelWorker = QtGui.QLabel(self.centralwidget)
        self.labelWorker.setObjectName(_fromUtf8("labelWorker"))
        self.inputLayout.addWidget(self.labelWorker, 4, 0, 1, 1)
        self.labelLength = QtGui.QLabel(self.centralwidget)
        self.labelLength.setObjectName(_fromUtf8("labelLength"))
        self.inputLayout.addWidget(self.labelLength, 1, 0, 1, 1)
        self.labelFactory = QtGui.QLabel(self.centralwidget)
        self.labelFactory.setObjectName(_fromUtf8("labelFactory"))
        self.inputLayout.addWidget(self.labelFactory, 2, 0, 1, 1)
        self.labelFiberType = QtGui.QLabel(self.centralwidget)
        self.labelFiberType.setObjectName(_fromUtf8("labelFiberType"))
        self.inputLayout.addWidget(self.labelFiberType, 0, 0, 1, 1)
        self.fiberTypeBox = QtGui.QComboBox(self.centralwidget)
        self.fiberTypeBox.setObjectName(_fromUtf8("fiberTypeBox"))
        self.inputLayout.addWidget(self.fiberTypeBox, 0, 1, 1, 1)
        self.fiberLength = QtGui.QLineEdit(self.centralwidget)
        self.fiberLength.setObjectName(_fromUtf8("fiberLength"))
        self.inputLayout.addWidget(self.fiberLength, 1, 1, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.inputLayout.addWidget(self.widget, 5, 0, 1, 1)
        self.cvOperatorLayout.addLayout(self.inputLayout)
        self.extendwidget = QtGui.QWidget(self.centralwidget)
        self.extendwidget.setMinimumSize(QtCore.QSize(0, 100))
        self.extendwidget.setObjectName(_fromUtf8("extendwidget"))
        self.cvOperatorLayout.addWidget(self.extendwidget)
        self.horizontalLayout.addLayout(self.cvOperatorLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1809, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "光纤几何测试平台", None))
        self.reporterCV.setText(_translate("MainWindow", "输出报告", None))
        self.beginTestCV.setText(_translate("MainWindow", "开始测试", None))
        self.labelCV.setText(_translate("MainWindow", "几何：", None))
        self.resultShowCV.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">清晰度指数：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">纤芯直径(um)：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">包层直径(um)：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">纤芯不圆度：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">包层不圆度：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">芯包同心度(um)：</p></body></html>", None))
        self.light.setText(_translate("MainWindow", "0.0", None))
        self.label.setText(_translate("MainWindow", "光强：", None))
        self.label_2.setText(_translate("MainWindow", "清晰度：", None))
        self.dynamicSharp.setText(_translate("MainWindow", "0.0", None))
        self.fiberNumber.setText(_translate("MainWindow", "123456", None))
        self.Worker.setText(_translate("MainWindow", "12345", None))
        self.labelFiberNumber.setText(_translate("MainWindow", "光纤编号：", None))
        self.factory.setText(_translate("MainWindow", "yofc", None))
        self.labelWorker.setText(_translate("MainWindow", "操作人员：", None))
        self.labelLength.setText(_translate("MainWindow", "光纤长度(m)：", None))
        self.labelFactory.setText(_translate("MainWindow", "生产厂家：", None))
        self.labelFiberType.setText(_translate("MainWindow", "光纤规格：", None))
        self.fiberLength.setText(_translate("MainWindow", "24", None))

