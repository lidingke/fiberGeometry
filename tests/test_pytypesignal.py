#coding:utf-8
"""pytype signal slot"""
from concurrent.futures import ThreadPoolExecutor

from util.observer import PyTypeSignal

class MyTypeSignal(object):
    sendmsg = PyTypeSignal()

    def run(self,data):
        self.sendmsg.emit(data)

class MyTypeSlot(object):

    def get(self, msg):
        # for i in range(1000):
        self.emit_get = msg

    def get_list(self,msg):
        self.list_get = list(range(1000))
        for i in range(100):
            self.list_get[i] = msg[i]
            # print self.list_get

def single_signal(data):
    send = MyTypeSignal()
    slot = MyTypeSlot()
    send.sendmsg.connect(slot.get)

    send.run(data=data)
    assert data == slot.emit_get
    return slot.emit_get

def single_signal_list(data):
    send = MyTypeSignal()
    slot = MyTypeSlot()
    send.sendmsg.connect(slot.get_list)

    send.run(data=data)
    assert data[:100] == slot.list_get[:100]
    return slot.list_get

from PyQt4.QtCore import pyqtSignal, QObject

class QTypeSignal(QObject):
    sendmsg = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)

    def run(self):
        self.sendmsg.emit('send')

class QTypeSlot(object):
    def get(self, msg):
        print 'Qslot get msg', msg

    def get_list(self,msg):
        for i in range(100):
            self.list_get[i] = msg[i]


def qt_signal(self, data):
    send = QTypeSignal()
    slot = QTypeSlot()
    send.sendmsg.connect(slot.get_list)

    send.run(data=data)

    assert data == slot.list_get

def tstart(data):
    return data

class TestMySignal():


    def test_signal(self):
        send = MyTypeSignal()
        slot = MyTypeSlot()
        send.sendmsg.connect(slot.get)
        for i in range(10):
            send.run(data=i)
            assert i == slot.emit_get

    def test_pool(self):
        with ThreadPoolExecutor(100) as pool:
            pools = [pool.submit(single_signal, (i,) ) for i in range(1000)]
        print len([len(p.result()) for p in pools])

    def test_list_pool(self):
        with ThreadPoolExecutor(100) as pool:
            pools = [pool.submit(single_signal_list, (list(range(i, i + 1000)))) for i in range(1000)]
        print len([len(p.result()) for p in pools])

