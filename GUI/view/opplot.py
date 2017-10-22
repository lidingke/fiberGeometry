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
# use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE

from PyQt4 import QtGui, QtCore
import matplotlib.mlab as mlab
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class OpticalPlot(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=6.48, height=4.84, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor = 'none')
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
        self.axes.plot([], [], 'r')
        self.axes.set_facecolor('none')

    def update_figure(self):
        # self.axes.clf()
        self.axes.plot(self.xlist, self.y1list, 'r')
        self.draw()
        # self.setStyleSheet("QWidget{border-radius: 50px}")

    def XYaxit(self ,x ,y1):
        self.xlist = x
        self.y1list = y1
        print 'get plot ', len(x), len(y1), self.xlist[-1], self.y1list[-1]
        self.axes.set_facecolor('none')

        self.update_figure()
    #
    # def savePlotFig(self):
    #     def savefigThread(self):
    #         self.fig.savefig("data\\plot.svg", format='svg')  # data\
    #     # threading.Thread(target=savefigThread, daemon=True).start()
