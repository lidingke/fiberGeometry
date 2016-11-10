from GUI.UI.mainUI import Ui_MainWindow
from GUI.UI.newgui import Ui_MainWindow as new_MainWindow

from PyQt4.QtCore import QRect
from PyQt4.QtGui import QWidget, QMainWindow, QPainter,QFont,\
QPixmap, QImage, QColor



class View(QMainWindow,Ui_MainWindow):
    """docstring for View"""

    def __init__(self,):
        super(View, self).__init__()
        self.setupUi(self)
        self.painterWidget = PainterWidget(self.widget)
        self.IS_INIT_PAINTER = False
        font = QFont("Microsoft YaHei", 20, 75)
        self.sharpLabel.setFont(font)

    def updatePixmap(self,arr, sharp):
        if not self.IS_INIT_PAINTER:
            self.painterWidget.initPixmap(arr)
            self.IS_INIT_PAINTER = True
        self.painterWidget.getPixmap(arr)
        self.sharpLabel.setText(sharp)

    def getModel(self, model):
        self.model = model

    def closeEvent(self, *args, **kwargs):
        self.model.exit()


class PainterWidget(QWidget):
    """docstring for PainterWidget"""
    def __init__(self, parent):
        super(PainterWidget, self).__init__(parent)
        self.pixmap = False
        self.painter = QPainter(self)
        self.ellipses, self.result = False, False

    def initPixmap(self, mapArray):
        try:
            width, height, size = mapArray.shape
        except Exception, e:
            width, height = mapArray.shape
        self.width = width
        self.height = height
        self.rect = QRect(0, 0,height, width )
        self.setGeometry(self.rect)

    def paintEvent(self, event):

        if self.pixmap:
            # print 'rect', self.rect
            self.painter.begin(self)
            self.painter.drawPixmap(self.rect, self.pixmap)
            # self._decorateImg(self.painter)
            self.painter.end()

    # def _decorateImg(self, painter):
    #     if self.ellipses or self.result:
    #         pass

    def getPixmap(self, mapArray):
        #todo: image format error
        # self.ellipses, self.result = plotResults
        if len(mapArray.shape) >= 3:
            img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_RGB16)
        else:
            img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        # img = QImage(mapArray.flatten(), self.height, self.width, QImage.Format_Indexed8)
        self.pixmap = QPixmap.fromImage(img)
        self.update()




class DynamicView(QMainWindow, new_MainWindow):
    """docstring for View"""

    def __init__(self,):
        super(DynamicView, self).__init__()
        self.setupUi(self)
        self.painterWidget = PainterWidget(self.canvas)
        self.IS_INIT_PAINTER = False
        # font = QFont("Microsoft YaHei", 20, 75)
        # self.sharpLabel.setFont(font)
        self.__initUI__()

    def __initUI__(self):
        items = ['G652']
        self.fiberType.addItems(items)

    def updatePixmap(self, arr, sharp):
        #todo : set Text box
        if not self.IS_INIT_PAINTER:
            self.painterWidget.initPixmap(arr)
            self.IS_INIT_PAINTER = True
        self.painterWidget.getPixmap(arr)
        # self.sharpLabel.setText(sharp)

    def getModel(self, model):
        self.model = model

    def closeEvent(self, *args, **kwargs):
        self.model.exit()

# class StaticView(QMainWindow,new_MainWindow):
#
#     def __init__(self):
#         super(StaticView, self).__init__()
#         self.setupUi(self)
#         self.__initUI__()
#
#     def __initUI__(self):
#         items = ['G652']
#         self.fiberType.addItems(items)
#
