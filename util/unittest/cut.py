
import pdb

from util.observer import PyTypeSignal

import inspect
def demo():
    print "demo"
codes = inspect.getsource(demo())
print codes

#
# class demo():
#
#
#     def __init__(self):
#         self.a = PyTypeSignal()
#         self.a.connect(self.b)
#         self.b()
#
#     def b(self):
#         self.c = PyTypeSignal()
#         self.c.connect(self.d)
#
#     def d(self):
#         print "d"
#
# diss = {
#     "a":"1",
#     "b":"2"
# }
#
#
# class Cut(object):
#
#     def __new__(cls, *args, **kwargs):
#         print "in cut new"
#         for k,v in diss.items():
#             setattr(cls,k,v)
#         # pdb.set_trace()
#         # cls.update(diss)
#         return object.__new__(cls)


if __name__ == '__main__':
    c = Cut()
    print c
