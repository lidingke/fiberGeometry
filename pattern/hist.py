from collections import  MutableMapping, deque, MutableSequence
import pdb
import matplotlib.pyplot as plt

class CounterDict(MutableMapping):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, dequeMaxlen, *args, **kwargs):
        # self.store = dict()
        # print 'before init'
        self.store = deque(maxlen=dequeMaxlen)
        for x in range(0, dequeMaxlen):
            self.store.append(0)
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = self.store[key] + 1

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return  list(self.store).__str__()

    def append(self, key):
        if isinstance(key , int):
            self.__setitem__(key, key)
        elif isinstance(key, list):
            for k in key:
                self.__setitem__(k, k)
        else:
            raise ValueError("error input key")

    def data(self):
        return list(self.store)



def getHist(container):
    if not isinstance(container, list):
        raise ValueError("fun getHist input para error", type(container))
    md = CounterDict(max(container) + 1)
    md.append(container)
    x = range(0,max(container)+1)
    y = md.data()
    return (x,y)


if __name__ == '__main__':
    mdlist = [1,2,2,3,4,3,3,4,5]
    # pdb.set_trace()
    imhf = getHist(mdlist)
    # print imhf
    plt.plot(imhf)
    plt.show()

