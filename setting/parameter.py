from collections import OrderedDict
import json
# import pdb
import traceback
import sys, os
from util.load import MetaDict, WriteReadJson, WRpickle

import os
import logging

logger = logging.getLogger(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DIR = "sqlite:///setting/cv_result.db"


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

        # def getSetting(self):
        #     return self.store
        #
        # def getInitLoad(self):
        #     return self.jsonLoad

        # def saveSetting(self):
        #     self.jsonLoad.update({self.GET_SETTING_ID:self.store})
        #     self.wrJson.save(self.jsonLoad)

        # for data in args:
        #     self.updates(data)
        # for data in kwargs:
        #     self.updates(data)

        # def _mergeDict(self, args):
        #     odict = OrderedDict()
        #     jsonLoad = self._readJson()
        #     print 'jsonLoad', jsonLoad
        #     odict.update(jsonLoad["Default"])
        #     for k in args:
        #         v = jsonLoad.get(k,{})
        #         odict.update(v)
        #     return odict


        # def updates(self, *args, **kwargs):
        #     if kwargs:
        #         print 'get kwargs', kwargs
        #         self.store.update(kwargs)
        #     if args:
        #         print 'get args', args
        #         for data in args:
        #             if isinstance(data,str):
        #                 self._storeUpdateJsonStr(data)
        #             elif isinstance(data, dict):
        #                 self.store.update(data)
        #             else:
        #                 raise ValueError("updateSets input data error", type(data))

        # def _storeUpdateJsonStr(self, data):
        #     if not isinstance(data, str):
        #         raise ValueError('update method input must be str')
        #     js = self._readJson()
        #     if data in js.keys():
        #         read = js.get(data)
        #         self.store.update(read)
        #     else:
        #         print 'WARNNING: no str keys:', data
