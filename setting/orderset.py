from collections import OrderedDict
import json
import pdb
from setting.dset import  MetaDict, WriteReadJson


def singleton(class_):
    instance = {}
    def getinstance(*args,**kwargs):
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

        if isinstance(args[0], dict):
            args = args[0].values()
        self.store = self._mergeDict(args)
        print self.store.keys()



    def _mergeDict(self, args):
        # for x in args:
        #     print 'x', x
        # print 'args', args, type(args)
        odict = OrderedDict()
        wrJson = WriteReadJson("setting\\oset.json")
        jsonLoad = wrJson.load()
        if not isinstance(jsonLoad, dict):
            raise ValueError('SETTING\'s oset.json error format')
        # pdb.set_trace()
        print 'jsonLoad', jsonLoad
        odict.update(jsonLoad["Default"])
        for k in args:
            # print 'get k', k
            v = jsonLoad.get(k,{})
            # print 'update',k, v
            odict.update(v)
        return odict





    def getSetting(self):
        return self.store

    # def saveSetting(self):
    #     self.jsonLoad.update({self.GET_SETTING_ID:self.store})
    #     self.wrJson.save(self.jsonLoad)


