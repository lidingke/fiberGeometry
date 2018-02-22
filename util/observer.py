# coding:utf-8
"""观察者模式=信号槽机制，用Python实现的信号槽，可以替代Qt自带的信号槽。"""
from PyQt4.QtCore import pyqtSignal, QObject
from collections import deque
from threading import Lock


class QTypeSignal(QObject):
    u"""信号槽的使用方式：
    继承QObject，
    在类变量中定义一个qt信号槽，
    单独初始化一次QObject，
    执行emit"""
    sendmsg = pyqtSignal(object)  # 定义一个信号槽，传入一个参数位参数

    def __init__(self):
        QObject.__init__(self)  # 用super初始化会出错

    def run(self):
        self.sendmsg.emit('send')  # 发信号


class QTypeSlot(object):
    def get(self, msg):  # 槽对象里的槽函数
        print 'Qslot get msg', msg


class PyTypeSignal(object):
    u"""下面几行代码既可以实现Qt风格的信号槽。
    在connect方法中将需要执行的方法添加进队列，
    在emit中取出函数并执行，这是一个基本的信号槽执行方式。
    为了线程安全，定义一个Lock锁住线程。"""
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
