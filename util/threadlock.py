import threading
from threading import Lock
from time import sleep
from functools import wraps
def mutex(fun):
    alock = Lock()
    @wraps(fun)
    def inner(*args, **kwargs):
        # nonlocal alock
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


if __name__ == '__main__':
    passs()
    passs()
    passs()
    times()
    passs()
    passs()
    passs()