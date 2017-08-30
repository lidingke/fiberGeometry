import sys

import os
from PyQt4.QtGui import QApplication

from onefile.convert import to_html, to_pdf

if __name__ == '__main__':
    os.system('del test_pdf\\test.pdf')
    app = QApplication(sys.argv)
    dir_ = "test_pdf\\test.pdf"
    # myhtml = to_html()
    with open("test_pdf\\test.html", 'r') as f:
        myhtml = "".join(f.readlines())
    to_pdf(dir_, myhtml)
    sys.exit(app.exec_())