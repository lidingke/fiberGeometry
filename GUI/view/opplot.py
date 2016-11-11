#!/usr/bin/env python

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
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import threading
progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=6.48, height=4.84, dpi=100):
        #todo: need resize
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor = 'white')
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class OpticalPlot(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        super(OpticalPlot, self).__init__(*args, **kwargs)

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        self.axes.plot(self.xlist, self.y1list, 'r')
        self.draw()
        # self.setStyleSheet("QWidget{border-radius: 50px}")

    def XYaxit(self ,x ,y1):
        self.xlist = x
        self.y1list = y1
        print 'get plot ', len(x), len(y1), self.xlist[-1], self.y1list[-1]
        self.update_figure()

    def savePlotFig(self):
        def savefigThread(self):
            self.fig.savefig("data\\plot.svg", format='svg')  # data\
        threading.Thread(target=savefigThread, daemon=True).start()
