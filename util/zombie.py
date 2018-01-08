import json
import os
import pdb

from util.loadfile import MetaDict

# def singleton(class_):
#     class class_w(class_):
#         _instance = None
#         def __new__(class_, *args, **kwargs):
#             if class_w._instance is None:
#                 class_w._instance = super(class_w,
#                                     class_).__new__(class_,
#                                                     *args,
#                                                     **kwargs)
#                 class_w._instance._sealed = False
#             return class_w._instance
#         def __init__(self, *args, **kwargs):
#             if self._sealed:
#                 return
#             super(class_w, self).__init__(*args, **kwargs)
#             self._sealed = True
#     class_w.__name__ = class_.__name__
#     return class_w

JSON_CONFIG_PATH = 'setting/zombie/'


# @singleton
class ZombieSingleton(MetaDict):
    _instance = {}

    def __new__(cls, file_name, *args, **kwargs):
        # print 'cls',id(cls)
        if file_name in cls._instance:
            return cls._instance[file_name]
        else:
            # cls['name'] = file_name
            obj = super(ZombieSingleton, cls).__new__(cls, *args, **kwargs)
            # obj = object.__new__()
            obj.__name__ = 'ZombieSigleton_' + file_name
            cls._instance[file_name] = obj
            # print 'obj',id(obj)
            return obj

    # def __init__(self,file_name):
    #     print "self",id(self),self._instance

    def __init__(self, file_name):
        super(ZombieSingleton, self).__init__()
        self.path = os.path.join(JSON_CONFIG_PATH, file_name) + '.json'
        with open(self.path, 'rb') as f:
            # pdb.set_trace()
            data = json.load(f)
            assert isinstance(data, dict)
            self.store.update(data)
            for k, v in data.items():
                value_fun = CallableItem(self.store, k)
                setattr(self, k, value_fun)

    def save(self):
        with open(self.path, 'wb') as f:
            data = json.dumps(self.store)
            f.write(data)

    def __del__(self):
        self.save()
        # print 'self.__name__ ', self.__name__
        # self._del(self.__name__)
        # self._instance.pop(self.__name__.split('_')[-1])
        # super(ZombieSigleton, self).__del__()
        # super(ZombieSigleton, self).__exit__(self, exc_type, exc_val, exc_tb)

    @classmethod
    def _del(cls, name):
        print 'pop', cls, name
        cls._instance.pop(name)
        print 'pop cls instance', cls._instance


class CallableItem(object):
    def __init__(self, qoute, key):
        self.qoute = qoute
        self.key = key

    def __call__(self, value):
        # print value
        self.qoute[self.key] = value


# def fun(value):
#     print fun.__name__


def test_zombiesigleton():
    # ZombieSigleton.
    a, b, c = ZombieSingleton('a'), ZombieSingleton('b'), ZombieSingleton('a'),
    print dir(a)
    print a.__name__, id(a), a
    print b.__name__, id(b), b
    print c.__name__, id(c), c
    assert id(a) != id(b)
    assert id(a) == id(c)

    # print z.__dict__

    # z =


if __name__ == '__main__':
    d = ZombieSingleton("demo")
    print d
