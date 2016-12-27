from collections import OrderedDict
import json
import pdb
from setting.dset import singleton, MetaDict, WriteReadJson

@singleton
class SETTING(MetaDict):
    """docstring for PickContext"""
    def __init__(self, *args, **kwargs):
        MetaDict.__init__(self)
        # if not ParaDict:
        #     print("set SETTING to default", ParaDict)
        # self.GET_SETTING_ID = json.dumps(ParaDict)
        # self.wrJson = WriteReadJson("setting\\set.json")
        # self.jsonLoad = self.wrJson.load()
        # self.store = self.jsonLoad.get(self.GET_SETTING_ID, {})
        # self.IS_GETED_SETTING = False
        # self.store = OrderedDict()
        # pdb.set_trace()
        # print args, type(args)
        if isinstance(args[0], dict):
            args = args[0].values()
        self.store = self._mergeDict(args)



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
        if not args:
            odict.update(jsonLoad["Default"])
            return odict
        for k in args:
            print 'get k', k
            v = jsonLoad.get(k,{})
            print 'update',k, v
            odict.update(v)
        return odict




    def getSetting(self):
        return self.store

    # def saveSetting(self):
    #     self.jsonLoad.update({self.GET_SETTING_ID:self.store})
    #     self.wrJson.save(self.jsonLoad)


