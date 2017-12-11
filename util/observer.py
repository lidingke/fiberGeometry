# coding:utf-8
from PyQt4.QtCore import pyqtSignal, QObject
from collections import deque
from threading import Lock


class QTypeSignal(QObject):
    sendmsg = pyqtSignal(object)  # 定义一个信号槽，传入一个参数位参数

    def __init__(self):
        QObject.__init__(self)  # 用super初始化会出错

    def run(self):
        self.sendmsg.emit('send')  # 发信号

class QTypeSlot(object):
    def get(self, msg):  # 槽对象里的槽函数
        print 'Qslot get msg', msg


class PyTypeSignal(object):
    def __init__(self):
        self.collection = deque()
        self.lock = Lock()

    def connect(self, fun):
        if fun not in self.collection:
            self.collection.append(fun)

    def emit(self, *args, **kwargs):
        self.lock.acquire()
        for fun in set(self.collection):
            fun(*args, **kwargs)
        self.lock.release()


class MyTypeSignal(object):
    sendmsg = PyTypeSignal()

    def run(self):
        self.sendmsg.emit('send')


class MyTypeSlot(object):
    def get(self, msg):
        print 'My slot get msg', msg


if __name__ == "__main__":
    send = MyTypeSignal()
    slot = MyTypeSlot()
    send.sendmsg.connect(slot.get)  # 链接信号槽
    send.run()

    # >>get msg send


    send = QTypeSignal()
    slot = QTypeSlot()
    send.sendmsg.connect(slot.get)  # 链接信号槽
    send.run()
