#coding:utf-8
from GUI.model.report.pdf import writePdf, writePdfabs
import os
import sys
import time
from PyQt4.QtGui import  QApplication

def test_write_pdf():
    """unit test for pdf writer"""
    os.system('del tests\\data\\report2.pdf')
    app = QApplication(sys.argv)
    writePdf("tests\\data\\report")
    writePdfabs("tests\\data\\report2.pdf")
    listdir = os.listdir("tests\\data")
    assert 'report.pdf' in listdir
    assert 'report2.pdf' in listdir
    os.system('del tests\\data\\report.pdf')
    # os.system('del tests\\data\\report2.pdf')
