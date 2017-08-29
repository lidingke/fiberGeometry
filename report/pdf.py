#coding=utf-8
from PyQt4.QtCore import QString

from setting.config import PDF_PARAMETER
from .origin import *
from setting.orderset import SETTING
import sys
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication
from jinja2 import Environment, PackageLoader, select_autoescape

def writePdf(dir_):
    newbody = originHTML.format(**htmlpara)

    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_+'.pdf')
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(newbody.decode('utf-8'))#将utf-8编码的字符串解码为unicode
    text.print_(printer)
    # sys.exit(app.exec_())
    # sys.exit(0)

# def writePdfabs(dir_):
#     updates = PDF_PARAMETER
#     htmlpara.update(updates)
#     newbody = originHTML.format(**htmlpara)
#     # with open('t.html', 'wb') as f:
#     #     f.write(newbody)
#     #     f.close()
#     printer = QPrinter()
#     printer.setOutputFormat(QPrinter.PdfFormat)
#     printer.setOutputFileName(dir_)
#     printer.setPageSize(QPrinter.A4)
#     text = QTextDocument()
#     text.setHtml(newbody.decode('utf-8'))
#     text.print_(printer)


def writePdfabs(dir_):
    env = Environment(
        loader=PackageLoader('report', 'template'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('tabel.html')

    myhtml = template.render(
        title=unicode(PDF_PARAMETER['title'],"utf-8"),
        worker=PDF_PARAMETER['worker'],
        fibertype=PDF_PARAMETER['fibertype'],
        producer=PDF_PARAMETER['producer'],
        fiberNo=PDF_PARAMETER['fiberNo'],
        corediameter=PDF_PARAMETER['corediameter'],
        claddiameter=PDF_PARAMETER['claddiameter'],
        coreroundness=PDF_PARAMETER['coreroundness'],
        cladroundness=PDF_PARAMETER['cladroundness'],
        concentricity=PDF_PARAMETER['concentricity'],
        sharpindex=PDF_PARAMETER['sharpindex'],
        # lightindex=PDF_PARAMETER['lightindex'],
        date=PDF_PARAMETER['date'],
        fiberLength=unicode(PDF_PARAMETER['fiberLength'],"utf-8"),
        # src="img\img.jpg"
    )
    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_)
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(myhtml)
    text.print_(printer)
