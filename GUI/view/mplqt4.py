#coding:utf-8
# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon#               2006 Darren Dale
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


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=4, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor = 'none')
        self.axes = self.fig.add_subplot(111)
        # self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=1)
        # fig.tight_layout(True)


        self.axes_twinx = self.axes.twinx()
        self.initial_figure()
        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def initial_figure(self):
        self.axes.plot([], [], 'r')
        self.axes.set_facecolor('none')
        self.axes.set_title(u"折射率剖面模拟器", fontproperties='SimHei')

    def update_figure(self, x, h,y,v):
        self.axes.cla()
        self.axes.plot(x,h,'y')
        self.axes_twinx.plot(y,v,'r')
        self.axes.set_facecolor('none')
        self.axes.set_title(u"折射率剖面模拟器", fontproperties='SimHei')
        self.draw()





