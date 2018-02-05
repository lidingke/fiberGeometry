import time


def timing(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        runtime = time.time() - start
        print fun.func_name, 'consume: ', runtime, 's'
        return result
    return wrapper
