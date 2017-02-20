#coding:utf-8
from util.reporter.reportcontext import PickContext
import re
from datetime import datetime as dt
from PyQt4.QtGui import QWidget, QFileDialog, QMessageBox
from report.pdf import writePdfabs

def Reporter(father):
    if not isinstance(father, QWidget):
        raise Exception('father widget is wrong', father)
    fileName = QFileDialog.getSaveFileName(father, "Save Report",
                                           '',
                                           " (*.pdf);;(*.html);;All Files (*)")
    print 'file', fileName
    fileName = str(fileName)
    if fileName.find('.') > 0:
        fileform = fileName.split('.')[-1]
    else:
        fileform = False
    print('fileform', fileform)
    if not (fileName and fileform):
        return
    try:
        out_file = open(fileName, 'wb')
    except IOError:
        QMessageBox.information(father, u"无法打开文件",
                                u"在打开文件 \"%s\" 时出错，新文件未生成" % fileName)
        return

    out_file.close()
    if fileform:
        try:
            fileform = re.findall('\(*\.(.*?)\)', fileform)[-1]
        except IndexError:
            fileform = str(fileform)
        print('fileform,', fileform)
        if fileform == 'pdf':
            # self.savePdf(fileName)
            writePdfabs(fileName)
            # self.saveFile(fileName)
    # print(fileName)


def GetParameter(self):
    para = {}
    # _ = datetime.datetime.now()
    dtstr = dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')
    # nowDate = u"{}年{}月{}日{}时{}分".format(_[0],_[1],_[2],_[3],_[4])
