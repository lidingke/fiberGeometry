#coding:utf-8
# int
# float
# "abc"
#
#
# [1,2,3,4]
#
#
# dict_a = {"k":1,"k2":2} #key:value
#
# tuple([1,2,3])
#
# # set(["k"])
#
#
# def fun(x):
#     if True:
#         pass
#     else:
#         pass
#     while True:
#         pass
#     print("helo world",x)
#     return 1
import pdb

class Op(object):
    u"""类：包含属性和方法"""

    def __init__(self):
        self.a = 1
        self.b = 2

    def _print(self):
        print(self.a,self.b)


class chirld(Op):

    pass


op = Op()
op._print()
c = chirld()
c._print()
# pdb.set_trace()