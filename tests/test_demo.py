import unittest
from functools import partial

#
# """demo 0"""
# class Demo0(object):
#
#
#     def is_test(self):
#         if __name__.find('test') > -1:
#             raise EnvironmentError('in test')
#
# def replace():
#     if __name__.find('test') > -1:
#         print(__name__, type(__name__), __name__.find('test'))
#         return True
#
#
# class TestDemo0(unittest.TestCase):
#
#     def test_demo0(self):
#         d = Demo0()
#         self.assertRaises(EnvironmentError,d.is_test)
#
#     def test_replace(self):
#         d = Demo0()
#         d.is_test = replace
#         assert d.is_test()
#
#
#
# """demo 1"""
# class Demo1(Demo0):
#
#     def __init__(self):
#         super(Demo1, self).__init__()
#         self.is_test()
#
#
# class TestDemo1(unittest.TestCase):
#
#     def test_demo1(self):
#         self.assertRaises(EnvironmentError, Demo1)
#
#     def test_replace(self):
#         def init(self):
#             pass
#         Demo1.__init__ = init
#         d = Demo1()
#         self.assertRaises(EnvironmentError, d.is_test)
#         d.is_test = replace
#         assert d.is_test()
#     #
# def test_closure():
#     port = 110
#     def init(self):
#         print('get',port)
#     Demo1.__init__ = init
#     Demo1()

import demo

def test_demo():
    try:
        demo.Demo()
    except Exception as e:
        assert isinstance(e, EnvironmentError)

def replace(fun):
    _ = demo.fail
    demo.fail = demo.success
    def inner():
        fun()
        demo.fail = _
    return inner()

@replace
def test_replace_demo():
    demo.Demo()





