from .sharp import IsSharp
from .getimg import GetImage
import os, sys
import cv2
from collections import deque
import logging
import time
import serial
logger = logging.getLogger(__name__)
from SDK.modbussdk import ModBusMode
from SDK.mdpy import GetRawImg

def Midfilter(que):
    assert isinstance(que, list)
    que.sort()
    que = que[1:-1]
    # print que
    return sum(que) / len(que)

class Focuser(object):

    def __init__(self):
        super(Focuser, self).__init__()
        self.issharp = IsSharp().issharpla
        self.step = 0
        self.sharps = deque(maxlen=15)
        self.motor = SerialMotor(port='com4')
        self.getImg = GetRawImg().get
        self.RUNNING = True


    def getSharp(self):
        img = self.getImg()
        # cv2.imwrite("IMG\\emptytuple\\sharpa\\"+st+".BMP",img)
        sharp = self.issharp(img)
        # time.sleep(3)
        print 'get sharp',sharp
        return sharp

    def run(self):
        self.motor.start()
        RUNNING = True
        time.sleep(1)
        while RUNNING:
            sharp = self.getSharp()
            self.sharps.append(sharp)
            logging.info(sharp)
            if len(self.sharps) >= 15:
                sharps = list(self.sharps)
                print sharps
                begin = Midfilter(sharps[:5])
                end = Midfilter(sharps[-5:])
                if begin <= end :
                    self.motor.moveback()
                RUNNING = False
        while self.RUNNING:

            sharp = self.getSharp()
            self.sharps.append(sharp)
            sharps = list(self.sharps)
            print
            begin = Midfilter(sharps[:5])
            mid = Midfilter(sharps[5:-5])
            end = Midfilter(sharps[-5:])
            if (begin > mid) and (end > mid):
                self.RUNNING=False
        self.motor.moveback()
        time.sleep(0.1)
        print 'end', self.getSharp()
        self.motor.close()

    # def get(self):
    #     self.motor.start()
    #     print self.motor, self.getSharp
    #     sharp = self.getSharp()
    #     print 'getsharp',sharp
        # return sharp
        # self.motor.close()
            # self.motor.move(self.get(img))

class LiveFocuser(object):

    def __init__(self,):
        super(LiveFocuser, self).__init__()
        self.sharps = deque(maxlen=15)
        self.motor = SerialMotor(port='com4')
        self.IS_START = False

    def get_sharps(self,sharp):
        if self.IS_START:
            if isinstance(sharp, str):
                sharp = float(sharp)
            else:
            # if not isinstance(sharps, list):
                raise ValueError('sharp not str number')

            print 'get sharp', sharp
            self.sharps.append(sharp)
            if len(self.sharps) != 15:
                return
            sharps = list(self.sharps)
            begin = Midfilter(sharps[:5])
            mid = Midfilter(sharps[5:-5])
            end = Midfilter(sharps[-5:])
            # end = Midfilter(sharps[-5:])
            if begin <= end:
                self.motor.moveback()
            elif (begin > mid) and (end > mid):
                self.IS_START = False
                self.motor.moveback()
                time.sleep(1)
                self.motor.close()
                self.sharps.clear()

    def start(self):
        self.motor.start()
        time.sleep(0.1)
        self.IS_START = True



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


class SerialMotor(Motor):

    def __init__(self, port = "com13", baudrate = 19200):
        super(SerialMotor, self).__init__()
        self.mod = ModBusMode(port=port, baudrate=baudrate, )
        self.direct = 'x'
        self.status = 'clicked'
        self.forward = '0'

    def move(self):
        pass

    def start(self):
        self.mod.run(self.direct, 'clicked', self.forward)

    def moveback(self):
        self.mod.run(self.direct, 'release', self.forward)
        if self.forward == '0':
            self.forward = '1'
        else:
            self.forward = '0'
        self.mod.run(self.direct, 'clicked', self.forward)

    def close(self):
        self.mod.run(self.direct, 'release', self.forward)





