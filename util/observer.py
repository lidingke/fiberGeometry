#coding:utf-8
from PyQt4.QtCore import pyqtSignal, QObject

class QTypeSignal(QObject):
    sendmsg = pyqtSignal(object)#定义一个信号槽，传入一个参数位参数

    def __init__(self):
        QObject.__init__(self)#用super初始化会出错

    def run(self):
        self.sendmsg.emit('send')#发信号


class QTypeSlot(object):

    def get(self, msg):#槽对象里的槽函数
        print 'Qslot get msg', msg



class MySignal(object):

    def __init__(self):
        self.collection = []#定义一个列表保存槽函数

    def connect(self, fun):
        self.collection.append(fun)#添加槽函数

    def emit(self, *args, **kwargs):
        for fun in self.collection:
            fun(*args, **kwargs)#遍历执行槽函数

class MyTypeSignal(object):
    sendmsg = MySignal()#实例化

    def run(self):
        self.sendmsg.emit('send')#发送

class MyTypeSlot(object):

    def get(self, msg):#槽对象里的槽函数
        print 'My slot get msg', msg

if __name__ == "__main__":

    send = MyTypeSignal()
    slot = MyTypeSlot()
    send.sendmsg.connect(slot.get)#链接信号槽
    send.run()

#>>get msg send


    send = QTypeSignal()
    slot = QTypeSlot()
    send.sendmsg.connect(slot.get)  # 链接信号槽
    send.run()