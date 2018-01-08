import pickle
import sys
# import pdb
import json


# from view.user import User

class WRpickle(object):
    """docstring for WRpickle
    input a pick name
    """

    def __init__(self, arg):
        super(WRpickle, self).__init__()
        self.pickname = arg
        self.pick = {}

    def loadPick(self):
        with open(self.pickname, 'rb') as f:
            # print('f',f)
            try:
                self.pick = pickle.load(f)
            except Exception as e:
                raise e
                # pass
            # print('load',self.pick)
        return self.pick

    def savePick(self, pick):
        with open(self.pickname, 'wb') as f:
            # print('savePick',pick)
            pickle.dump(pick, f)

    def insertItem(self, key, item):
        if type(key) is not str:
            raise TypeError('key must be a str')
        self.pick[key] = item


class DynamicPick(object):
    """docstring for DynamicPick"""

    def __init__(self, ):
        super(DynamicPick, self).__init__()
        self.pick = {}

    def load(self, name):
        with open(name, 'rb') as f:
            self.pick = pickle.load(f)
        return self.pick

    def save(self, name):
        with open(name, 'wb') as f:
            pickle.dump(self.pick, f)


class WriteReadJson(object):
    """docstring for WriteReadJson"""

    def __init__(self, dir_):
        super(WriteReadJson, self).__init__()
        self.dir_ = dir_
        self.store = {}

    def load(self):
        with open(self.dir_, 'rb') as f:
            try:
                bitFileRead2Str = f.read().decode('utf-8')
                self.store = json.loads(bitFileRead2Str)
            except Exception as e:
                raise e
        return self.store

    def save(self, store):
        with open(self.dir_, 'wb') as f:
            jsonBitBuffer = json.dumps(store).encode('utf-8')
            # print('json', jsonBitBuffer)
            f.write(jsonBitBuffer)


class WriteReadJsonNoB(object):
    """docstring for WriteReadJson"""

    def __init__(self, dir_):
        super(WriteReadJsonNoB, self).__init__()
        self.dir_ = dir_
        self.store = {}

    def load(self):
        with open(self.dir_, 'r') as f:
            try:
                bitFileRead2Str = f.read()
                self.store = json.loads(bitFileRead2Str)
            except Exception as e:
                raise e
        return self.store

    def save(self, store):
        with open(self.dir_, 'w') as f:
            jsonBitBuffer = json.dumps(store)
            # print('json', jsonBitBuffer)
            f.write(jsonBitBuffer)


def loadStyleSheet(sheetName):
    # D:\MyProjects\WorkProject\opencv4fiber\cv\GUI\UI\qss\main.qss
    with open('GUI/UI/qss/{}.qss'.format(sheetName), 'rb') as f:
        styleSheet = f.readlines()
        # print(read)
        styleSheet = b''.join(styleSheet)
        styleSheet = styleSheet.decode('utf-8')
    return styleSheet


from collections import MutableMapping


class MetaDict(MutableMapping):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

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


def load_pickle_nor_json(file_name):
    """if pickle exist load pickle, nor json"""
    wrp = WRpickle(file_name + ".pickle")
    try:
        load = wrp.loadPick()
    except IOError:
        wrJson = WriteReadJson(file_name + ".json")
        load = wrJson.load()
    return load


if __name__ == '__main__':
    wrj = WriteReadJson("test.json")
    wrjdict = {'1': 2, '2': '34'}
    wrj.load()
    wrj.save(wrjdict)
