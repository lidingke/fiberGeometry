from collections import OrderedDict
import json
# import pdb
import traceback
import sys, os
from util.loadfile import MetaDict, WriteReadJson, WRpickle

import os
import logging

logger = logging.getLogger(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DIR = "sqlite:///setting/relation_result.db"


def singleton(class_):
    instance = {}

    def getinstance(*args, **kwargs):
        # if "printline" in args:
        #     try:
        #         raise ValueError('singleton line')
        #     except Exception:
        #         print 'trace', sys._getframe(1).f_code

        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
            # print 'singleton id', id(instance[class_]), len(instance)

        return instance[class_]

    return getinstance


@singleton
class SETTING(MetaDict):
    """docstring for PickContext"""

    def __init__(self, *args, **kwargs):
        MetaDict.__init__(self)

        self.store = OrderedDict()
        self.json_load = self._read_pickle_first()
        self.store.update(self.json_load["Default"])

    def update_by_key(self, *key):
        for k in key:
            if isinstance(k, str):
                self.store.update(self.json_load.get(k, {}))
            else:
                raise ValueError("error input key", type(key))
        logger.error('key update =======\n' + str(self))

    def _read_pickle_first(self):
        wrp = WRpickle("setting\\oset.pickle")
        try:
            load = wrp.loadPick()
        except IOError:
            wrJson = WriteReadJson("setting\\oset.json")
            load = wrJson.load()
        if not isinstance(load, dict):
            raise ValueError('SETTING\'s oset error format')
        return load

    def __str__(self):
        strs = []
        for k, v in self.store.items():
            s = "\n=>{}:{}".format(k, v)
            strs.append(s)
        return "".join(strs)

    def __del__(self):
        self.store.clear()


class ClassifyParameter(MetaDict):
    def __init__(self, *args, **kwargs):
        MetaDict.__init__(self)
        self.store = {}
        self.json_load = self._read_pickle_first()
        self.store.update(self.json_load["Default"])

    def _read_pickle_first(self):
        wrp = WRpickle("setting\\parameters.pickle")
        try:
            load = wrp.loadPick()
        except IOError:
            wrJson = WriteReadJson("setting\\parameters.json")
            load = wrJson.load()
        if not isinstance(load, dict):
            raise ValueError('SETTING\'s oset error format')
        return load

    def update_by_key(self, key):
        if key in self.json_load.keys():
            self.store.update(self.json_load.get(key))
            self.store['fiberType'] = key
        else:
            raise ValueError("{} is not in json".format(key))
        logger.error('key update :' + str(self))

    def __str__(self):
        strs = []
        for k, v in self.store.items():
            s = "=>{}:{}".format(k, v)
            strs.append(s)
        return "\n    " + "\n    ".join(strs)

    def __del__(self):
        self.store.clear()
