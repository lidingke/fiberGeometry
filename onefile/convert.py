import sys
from PyQt4.QtGui import QPrinter, QTextDocument, QApplication
from jinja2 import Environment, PackageLoader, select_autoescape
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def to_html():
    # print 'Base', BASE_DIR

    env = Environment(
        loader=PackageLoader('onefile', 'template'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('tabel.html')
    # d = {"title":unicode("ssx", "utf-8")}
    myhtml = template.render(
        title=unicode("ssx", "utf-8"),
        worker="a",
        fibertype="b",
        producer="c",
        fiberNo="d",
        corediameter="e",
        claddiameter="f",
        coreroundness="g",
        cladroundness="h",
        concentricity="i",
        sharpindex="j",
        # lightindex=PDF_PARAMETER['lightindex'],
        date="k",
        fiberLength=unicode("l", "utf-8"),
    )
    return myhtml

def to_pdf(dir_,myhtml):
    # try:
    # app = QApplication(sys.argv)
    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_)
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(myhtml)
    text.print_(printer)
    # sys.exit(app.exec_())


