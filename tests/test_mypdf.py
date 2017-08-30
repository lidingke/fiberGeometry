import os
import sys

from PyQt4.QtGui import QApplication
from onefile.convert import to_html, to_pdf


def test_writePdfabs():
    os.system('del ..\\test.pdf')
    app = QApplication(sys.argv)
    dir_ = "..\\test.pdf"
    myhtml = to_html()
    # with open("test.html", 'rb') as f:
    #     myhtml = f.read()
    # with open("test_pdf\\test.html","wb") as f:
    #     f.write(myhtml.encode('utf-8'))
    to_pdf(dir_, myhtml)
    # listdir = os.listdir("test_pdf")
    # assert 'test.pdf' in listdir
    # sys.exit(app.exec_())

