
from setting.parameter import SETTING
# SETTING("test")
from SDK.mdpy import GetRawImg, release_camera, get_camera_serial
import uuid
from util.loadfile import  MetaDict, WriteReadJson, WRpickle
from PyQt4.QtGui import QPalette, QColor,QApplication, QMessageBox, QWidget
import sys
import time
class InitCorrect(object):

    def __init__(self):
        super(InitCorrect, self).__init__()

    def run(self):
        try:
            self.readJson()
            self.rightMac()
            self.rightCamera()
            print "finish init msg"
        except ValueError as e:
            return e
        # return

    def readJson(self):
        # wrJson = WriteReadJson("setting\\userdata.json")
        wrp = WRpickle("setting\\userdata.pickle")
        try:
            load = wrp.loadPick()
        except IOError:
            wrJson = WriteReadJson("setting\\userdata.json")
            load = wrJson.load()
        self.json = load
        # print jsonLoad

    def rightCamera(self):
        try:
            get = GetRawImg()
            serialnumber = get.get_camera_serial()
        except ValueError as e:
            print 'get e is ',e
            # releaseCamera()
            # time.sleep(0.1)
            raise e
        finally:
            release_camera()
        if serialnumber not in self.json["camera"]:
            raise ValueError("Camera serial number error")

    def rightMac(self):
        macid = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
        # macid = macid
        print macid , self.json["mac"]
        if macid not in self.json["mac"]:
            raise ValueError("device information error")
        # return

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
