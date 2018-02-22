#coding:utf-8
import threading
from collections import deque
from threading import Lock
from time import sleep
from functools import wraps


def mutex(fun):
    alock = Lock()

    @wraps(fun)
    def inner(*args, **kwargs):
        alock.acquire()
        result = fun(*args, **kwargs)
        alock.release()
        return result

    return inner


@mutex
def passs():
    print "passs"


@mutex
def times():
    print "sleep in"
    sleep(3)
    print "sleep out"


class WorkerQueue(threading.Thread):
    u"""队列执行，保证不线程冲突。"""
    def __init__(self, maxlen=3):
        super(WorkerQueue, self).__init__()
        self.RUNNING = True
        self.queue = deque(maxlen=maxlen)

    def run(self):
        while self.RUNNING:
            sleep(0.1)
            if len(self.queue):
                fun, args, kwargs = self.queue.popleft()
                fun(*args, **kwargs)

    def append(self, fun, *args, **kwargs):
        if not self.RUNNING:
            raise StopIteration("QUEUE finished")
        self.queue.append((fun, args, kwargs))

    def close(self):
        self.RUNNING = False


if __name__ == '__main__':
    def fun(*args, **kwargs):
        print(args, kwargs)


    w = WorkerQueue()
    w.start()
    sleep(1)
    w.append(fun)
    w.append(fun)
    w.append(fun, 1, 2, 3, a=1)
    w.close()
    w.append(fun)
