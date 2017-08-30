#coding=utf-8
import os
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
    PDF_PARAMETER['title']=PDF_PARAMETER['title'].decode("utf-8")
    PDF_PARAMETER['src']="E:\Python\\fiberwmx\\fiberGeometry\onefile\img.jpg"
    myhtml = template.render(**PDF_PARAMETER)

    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_)
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(myhtml)
    text.print_(printer)
