
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
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE

from PyQt4 import QtGui, QtCore
import matplotlib.mlab as mlab
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=4, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor = 'none')
        self.axes = fig.add_subplot(211)
        self.axes_twinx = self.axes.twinx()
        # self.hist = fig.add_subplot(212)

        fig.set_tight_layout(True)
        # fig.tight_layout(pad=1)
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
        # self.axes
        # self.hist.hist([0, 1, 2, 3])

    def update_figure(self, x, h,y,v):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        # l = [random.randint(0, 10) for i in range(4)]
        # lastprices, yellowlines = LastPrice[::20].copy(), YellowLine[::20]
        # print 'plot len', len(numbers), len(lastprices), len(yellowlines)
        self.axes.cla()
        self.axes.plot(x,h,'y')#yellow line
        self.axes_twinx.plot(y,v,'r')#red line
        self.axes.set_facecolor('none')
        self.draw()





