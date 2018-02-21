#coding:utf-8
import gc

from util.observer import PyTypeSignal
from util.zombie import ZombieSingleton, CallableItem
from _functools import partial


def test_zombiesigleton():
    """ZombieSigleton 是一个动态的生成属性的类，这部分是针对这一类的单元测试"""
    # ZombieSigleton.
    a, b, c = ZombieSingleton('demo'), ZombieSingleton('test'), ZombieSingleton('demo'),
    # print dir(a)
    print a.__name__, id(a), a
    print b.__name__, id(b), b
    print c.__name__, id(c), c
    assert a.__name__[:15] == "ZombieSigleton_"
    assert a.__name__ != b.__name__
    assert a.__name__ == c.__name__
    assert id(a) != id(b)
    assert id(a) == id(c)

    assert a['a'] == "ab"
    assert isinstance(a.a, CallableItem)
    signal = PyTypeSignal()

    signal.connect(partial(a.a,'test'))
    # signal.connect(partial(a.update, {'a': 'test'}))
    signal.emit()
    assert a['a'] == "test"

    a['a'] = "ab"
    # ZombieSigleton._instance.clear()
    #
    # del a
    # print ZombieSigleton._instance
    # del b
    # print ZombieSigleton._instance
    # del c
    # print ZombieSigleton._instance
    #
    # gc.collect()


def test_zombiesigleton_save():
    t = ZombieSingleton('test')
    tn = t['n']
    t['n'] = tn+1
    print t['n'],ZombieSingleton._instance
    # ZombieSigleton._instance.clear()

    ZombieSingleton._instance.pop(t.__name__.split('_')[-1])
    del t
    # del t
