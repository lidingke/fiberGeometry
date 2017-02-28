from .sharp import IsSharp
from .getimg import GetImage
import os, sys

class Focuser(object):

    def __init__(self):
        super(Focuser, self).__init__()
        self.issharp = IsSharp().issharpla

    def run(self):
        pass



class Motor(object):

    def __init__(self):
        super(Motor, self).__init__()

    def move(self, step):
        raise NotImplementedError

class TestMotor(Motor):

    def __init__(self):
        super(TestMotor, self).__init__()

    def move(self, step):
        print  'move', step

class TestImgGet(object):

    def __init__(self):
        super(TestImgGet, self).__init__()
        self.getimg = GetImage().get
        self.dir_ = "IMG\\sharp\\oc1"
        self.getimgs()


    def getimgs(self):
        os.sys

    def get(self):
