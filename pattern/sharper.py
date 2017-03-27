from .sharp import IsSharp
from .getimg import GetImage
import os, sys
from collections import deque
import logging
logger = logging.getLogger(__name__)

def Midfilter(que):
    assert isinstance(que, list)
    que.sort()
    que = que[1:-1]
    print que
    return sum(que) / len(que)

class Focuser(object):

    def __init__(self):
        super(Focuser, self).__init__()
        self.issharp = IsSharp().issharpla
        self.step = 0
        self.sharps = deque(maxlen=15)
        self.motor = Motor()
        self.getImg = GetImage().get
        self.RUNNING = True


    def getSharp(self):
        img = self.getImg()
        sharp = self.issharp(img)

        return sharp

    def run(self):
        self.motor.start()
        RUNNING = True
        while RUNNING:
            sharp = self.getSharp()
            self.sharps.append(sharp)
            logging.info(sharp)
            if len(self.sharps) >= 15:
                sharps = list(self.sharps)
                begin = Midfilter(sharps[:5])
                end = Midfilter(sharps[-5:])
                if begin < end :
                    self.motor.moveback()
                RUNNING = False
        while self.RUNNING:
            sharp = self.getSharp()
            self.sharps.append(sharp)
            sharps = list(self.sharps)
            begin = Midfilter(sharps[:5])
            mid = Midfilter(sharps[5:-5])
            end = Midfilter(sharps[-5:])
            if (begin > mid) and (end > mid):
                self.RUNNING=False
        self.motor.close()

    def get(self):
        self.motor.start()
        print self.motor, self.getSharp
        sharp = self.getSharp()
        print 'getsharp',sharp
        # self.motor.close()
            # self.motor.move(self.get(img))


class Motor(object):

    def __init__(self):
        super(Motor, self).__init__()

    def move(self, step):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def moveback(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


