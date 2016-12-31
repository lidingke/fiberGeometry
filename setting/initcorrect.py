
from setting.orderset import SETTING
SETTING("test")
from SDK.mdpy import GetRawImg
import uuid
from setting.dset import  MetaDict, WriteReadJson
from PyQt4.QtGui import QPalette, QColor,QApplication, QMessageBox, QWidget
import sys
class InitCorrect(object):

    def __init__(self):
        super(InitCorrect, self).__init__()

    def run(self):
        try:
            self.rightMac()
            self.rightCamera()

        except ValueError as e:
            return e
        return

    def rightCamera(self):
        try:
            GetRawImg()
        except ValueError as e:
            print 'get e is ',e
            raise e

    def rightMac(self):
        macid = uuid.UUID(int=uuid.getnode()).hex[-12:]
        wrJson = WriteReadJson("setting\\userdata.json")
        jsonLoad = wrJson.load()
        print jsonLoad
        if macid not in jsonLoad["mac"]:
            raise ValueError("device information error")
        return

# class ErrorWindow(QWidget):
#
#     def __init__(self):
#         super(ErrorWindow, self).__init__()
#
#     def message(self, msg):
#         msg = InitCorrect().run()
#         print 'gettype', type(str(msg))
#         QMessageBox.information(QWidget(), "error", str(msg), QMessageBox.Ok,QMessageBox.NoButton)

def loadStyleSheet(sheetName):
#D:\MyProjects\WorkProject\opencv4fiber\cv\GUI\UI\qss\main.qss
    with open('GUI/UI/qss/{}.qss'.format(sheetName), 'rb') as f:
        styleSheet = f.readlines()
        # print(read)
        styleSheet = b''.join(styleSheet)
        styleSheet = styleSheet.decode('utf-8')

    return styleSheet

if __name__ == "__main__":
    # SETTING('MindVision500', 'Online')
    app = QApplication(sys.argv)
    msgs = InitCorrect().run()
    QMessageBox.warning(QWidget(), "error", str(msgs),QMessageBox.NoButton,QMessageBox.NoButton)
    sys.exit(app.exec_())
    # pass
