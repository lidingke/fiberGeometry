#coding:utf-8
import time


def timing(fun):
    u"""计时器装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        runtime = time.time() - start
        print fun.func_name, 'consume: ', runtime, 's'
        return result
    return wrapper
