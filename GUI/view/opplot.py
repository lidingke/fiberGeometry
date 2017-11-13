#!/usr/bin/env python
# coding:utf-8
# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.


from __future__ import unicode_literals
import sys
import os
import random
from matplotlib.backends import qt_compat
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class OpticalPlot(FigureCanvas):
    def __init__(self, parent=None, width=6.48, height=4.84, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='none')
        self.axes = fig.add_subplot(111)

        self.initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def initial_figure(self):
        self.axes.plot([], [], 'r')
        self.axes.set_facecolor('none')
        self.axes.set_title(u"待测光纤光谱", fontproperties='SimHei')
        self.axes.set_xlabel(u"波长(nm)", fontproperties='SimHei')
        self.axes.set_ylabel(u"强度(counts)", fontproperties='SimHei')
        self.axes.set_xlim(900,1700)
        self.axes.set_ylim(0,65000)

    def update_figure(self, x, y1):
        self.axes.cla()
        self.axes.plot(x, y1, 'r')
        self.axes.set_title(u"待测光纤光谱", fontproperties='SimHei')
        self.axes.set_xlabel(u"波长(nm)", fontproperties='SimHei')
        self.axes.set_ylabel(u"强度(counts)", fontproperties='SimHei')
        self.axes.set_xlim(900,1700)
        self.axes.set_ylim(0,65000)
        self.draw()
