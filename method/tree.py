#!/usr/bin/python
import pdb

from collections import MutableMapping

class MetaDict(MutableMapping):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys
        self.maxLenTrees = []
        self.maxLenLevel = 0

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return str(self.store)

class NodeDict(MetaDict):
    """"""
    def __init__(self,):
        super(NodeDict, self).__init__()
        # self.index = index
        # self.father = parent
        # self.child = [child]
        # # self.data = '-1'

    def __setitem__(self, key, value):
        key = str(key)
        value = str(value)
        # pdb.set_trace()
        if key in self.store.keys():
            if not value in self.store[key]:
                self.store[key].append(value)
        else:
            self.store[key] = [value]

    def treeFilter(self):

        for k,v in self.store.iteritems():
            for value in v:
                if not value in self.store.keys():
                    v.remove(value)

        for x in self.store.keys():
            if not self.store[x]:
                self.store.pop(x)

        for k,v in self.store.iteritems():
            for value in v:
                if not value in self.store.keys():
                    v.remove(value)

    def maxLenTree(self,k = '-1'):
        if k == '-1':
            self.maxLenTrees = []
            self.maxLenLevel = 0

        v = self.store[k]

        for value in v:
            if value in self.store.keys():
                self.maxLenTrees.append(k)
                self.maxLenTree(value)
        self.maxLenLevel += 1
        if self.maxLenLevel == len(self.store.keys()):
            # self.maxLenTrees.append(k)
            return self.maxLenTrees


        # self.maxLenTrees.append(v)
        # return self.maxLenTrees

        # for x in self.store.keys():
        #     if not self.store[x]:
        #         self.store.pop(x)

        # for k,v in self.store.iteritems():
        #     if len(k) >1:
        #         for value in v:
        #             if not value in self.store.keys():
        #                 v.remove(value)

#Tree hierarchys[array] = contour[h]




