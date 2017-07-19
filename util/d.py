
from functools import wraps
import time


class ActorBase():


    def _get_get_get(self):
        pass

f = lambda x:x+x

f(1)

def decorator(fun):
    @wraps(fun)
    def inner(*args,**kwargs):
        begin = time.time()
        fun(*args,**kwargs)
        end = time.time()
        print end - begin
    return inner



@decorator
def fun1(a):
    A = 1
    time.sleep(1)

class A():

    def __init__(self):
        a = 1

    def __exit__(self):
        del a


if __name__ == '__main__':
    fun1(1)

    # newfun = decorator(fun1)
    # newfun()


