from collections import OrderedDict
import json
import pdb
import traceback
import sys
from util.load import  MetaDict, WriteReadJson, WRpickle


def singleton(class_):
    instance = {}
    def getinstance(*args,**kwargs):
        if "printline" in args:
            try:
                raise ValueError('singleton line')
            except Exception:
                print 'trace', sys._getframe(1).f_code
        if class_ not in instance:
            instance[class_] = class_(*args,**kwargs)
            print 'singleton id', id(instance[class_]), len(instance)

        return instance[class_]
    return getinstance

@singleton
class SETTING(MetaDict):
    """docstring for PickContext"""
    def __init__(self, *args, **kwargs):
        MetaDict.__init__(self)

        # if isinstance(args[0], dict):
        #     args = args[0].values()
        # self.store = self._mergeDict(args)
        # print self.store.keys()
        self.store = OrderedDict()
        self.jsonLoad = self._readJson()
        self.store.update(self.jsonLoad["Default"])
        for data in args:
            self.updates(data)
        for data in kwargs:
            self.updates(data)

    def _mergeDict(self, args):
        odict = OrderedDict()
        jsonLoad = self._readJson()
        print 'jsonLoad', jsonLoad
        odict.update(jsonLoad["Default"])
        for k in args:
            v = jsonLoad.get(k,{})
            odict.update(v)
        return odict


    def updates(self, *args, **kwargs):
        if kwargs:
            print 'get kwargs', kwargs
            self.store.update(kwargs)
        if args:
            print 'get args', args
            for data in args:
                if isinstance(data,str):
                    self._storeUpdateJsonStr(data)
                elif isinstance(data, dict):
                    self.store.update(data)
                else:
                    raise ValueError("updateSets input data error", type(data))

    def keyUpdates(self, *key):
        for k in key:
            if isinstance(k, str):
                self.store.update(self.jsonLoad.get(k, {}))
            else:
                raise ValueError("error input key", type(key))
        print 'key update', self.store


    def _storeUpdateJsonStr(self, data):
        if not isinstance(data, str):
            raise ValueError('update method input must be str')
        js = self._readJson()
        if data in js.keys():
            read = js.get(data)
            self.store.update(read)
        else:
            print 'WARNNING: no str keys:', data

    def _readJson(self):
        wrp = WRpickle("setting\\oset.pickle")
        try:
            load = wrp.loadPick()
        except IOError:
            wrJson = WriteReadJson("setting\\oset.json")
            load = wrJson.load()
        if not isinstance(load, dict):
            raise ValueError('SETTING\'s oset error format')
        return load

    def getSetting(self):
        return self.store

    def getInitLoad(self):
        return self.jsonLoad

    def __str__(self):
        return str(self.store)

    def __del__(self):
        self.store.clear()

    # def saveSetting(self):
    #     self.jsonLoad.update({self.GET_SETTING_ID:self.store})
    #     self.wrJson.save(self.jsonLoad)


