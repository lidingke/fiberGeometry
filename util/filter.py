from __future__ import  division
import  collections


class MedianFilter(object):

    def __init__(self,maxlen=5):
        super(MedianFilter, self).__init__()
        self.store = collections.deque(maxlen=maxlen)
        self.dequelen = maxlen

    def append(self,data):
        self.store.append(data)

    def get(self, digits = 2):
        getlist = list(self.store)
        getlist.sort()
        get = getlist[1:-1]
        lenget = len(get)
        if lenget < self.dequelen-2:
            # print 'get len', lenget
            return self.store[-1]
        # print 'get len', lenget
        sumResult = sum(get)/lenget
        if round:
            return round(sumResult, digits)
        else:
            return int(round(sumResult))

class MedianLimitFilter(object):

    def __init__(self,maxlen=5):
        super(MedianLimitFilter, self).__init__()
        self.oldforrepet = 0
        self.oldbeforcounter = 0.0001
        self.counter = 0
        self.queue = collections.deque(maxlen=maxlen)

    def _removeRepet(self, data):
        if data != self.oldforrepet:
            self.oldforrepet = data
            return data

    def _medianMean(self, datas):
        if isinstance(datas,collections.deque):
            datas = list(datas)

        if len(datas) < 5:
            return datas[-1]
        datas.sort()
        datas = datas[1:-1]
        # pdb.set_trace()
        result = sum(datas)/len(datas)
        return result

    def run(self, data):
        data = self._removeRepet(data)
        if not data:
            return self.oldbeforcounter
        self.queue.append(data)
        get_ = self._medianMean(self.queue)
        if abs(get_ - self.oldbeforcounter)/self.oldbeforcounter > 0.01:
            self.oldbeforcounter = get_
        else:
            self.counter = self.counter + 1
        if self.counter > 3:
            self.counter = 0
            self.oldbeforcounter = get_

        return self.oldbeforcounter
