#coding:utf-8
from origin import *

def writePdf():
    with open("report.html", 'wb') as f:
        originHTML.format(**htmlpara)
        print originHTML
        f.write(originHTML)
        f.close()