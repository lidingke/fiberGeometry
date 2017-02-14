from report.pdf import writePdf
import os
import sys
from PyQt4.QtGui import  QApplication

def test_write_pdf():
    app = QApplication(sys.argv)
    writePdf("tests\\report")
    listdir = os.listdir("tests")
    # print listdir
    assert 'report.pdf' in listdir