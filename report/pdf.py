#coding:utf-8
from report.captemplate import cap_template
from setting.config import PDF_PARAMETER
from .origin import *
from setting.parameter import SETTING
import sys
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication

def writePdf(dir_):
    newbody = originHTML.format(**htmlpara)

    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_+'.pdf')
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(newbody.decode('utf-8'))
    text.print_(printer)
    # sys.exit(app.exec_())
    # sys.exit(0)

def writePdfabs(dir_):
    updates = PDF_PARAMETER
    htmlpara.update(updates)
    newbody = originHTML.format(**htmlpara)
    # with open('t.html', 'wb') as f:
    #     f.write(newbody)
    #     f.close()
    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_)
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(newbody.decode('utf-8'))
    text.print_(printer)

def write_txt(dir_,paras):
    capstrings = cap_template.format(**paras)
    with open("result.txt", "wb") as f:
        f.write(capstrings)