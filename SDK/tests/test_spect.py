import logging
import sys
from time import sleep, time

from PyQt4 import QtCore

from SDK.oceanoptics import Spectrograph






def test_get():
    # app = QtCore.QCoreApplication(sys.argv)
    logging.basicConfig(level=logging.INFO)
    print("start")
    sleep(1)
    t = time()
    s = Spectrograph()
    t0 = time()
    print(t-t0)
    wd = s.get_spectrograph(10000,1,0)
    t1 = time()
    print(wd)
    print(t1-t0)
    wd = s.get_spectrograph(100000,1,0)
    t2 = time()
    print(wd)
    print(t2-t1)

def test_get_spectrograph_by_length():
    s = Spectrograph()
    wd = s.get_spectrograph_by_length(21, 10000, 1, 0)
    print(wd)


def test_getq():
    # app = QtCore.QCoreApplication(sys.argv)
    logging.basicConfig(level=logging.INFO)
    print("start")
    sleep(1)
    s = Spectrograph()
    wd = s.get_spectrographq(100000,1,0)
    print(wd)