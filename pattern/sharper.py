from .sharp import IsSharp
from .getimg import GetImage
import os, sys

class Focuser(object):

    def __init__(self):
        super(Focuser, self).__init__()
        self.issharp = IsSharp().issharpla
        self.step = 0
        self.oldsharp = 0
        self.motor = Motor()
        self.RUNNING = True

    def get(self, img):
        sharp = self.issharp(img)
        if self.oldsharp < sharp:
            return -1
        elif self.oldsharp > sharp:
            return 1
        elif self.oldsharp == sharp:
            return 0

    def getImg(self):
        return None

    def run(self):
        while self.RUNNING:
            img = self.get()
            self.motor.move(self.get(img))



class Motor(object):

    def __init__(self):
        super(Motor, self).__init__()

    def move(self, step):
        raise NotImplementedError

