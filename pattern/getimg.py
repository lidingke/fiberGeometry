import cv2
import os
from random import choice
import pdb
import numpy as np
from pattern.meta import CV2MethodSet

class GetImage(CV2MethodSet):
    """docstring for GetImage"""
    def __init__(self, ):
        super(GetImage, self).__init__()
        # self.arg = arg
        self.img = False
        self.colour = None
        self.suffix = ''
        self.GRAY = ('gray', 'black')
        self.COLOR = ('colour', 'color')

    def get(self, dir_='', colour = 'colour'):
        if dir_.find('.') > 0:
            self.suffix = dir_.split('.')[-1]
            self.singleFileFind(dir_,colour)
        else :
            self.fileFind(dir_,colour)
        if not isinstance(self.img, np.ndarray):
            raise ValueError('img not ndarray')
        if self.img.dtype != "uint8":
            self.img = cv2.convertScaleAbs(self.img)
            # self.img = np.array(self.img,dtype="uint8")
        return self.img

    def fileFind(self, dir_,colour):
        for file in os.listdir(dir_):
            # pdb.set_trace()
            self.suffix = dir_.split('.')[-1]
            self.img = cv2.imread(dir_ + "\\" + file)
            self._getColorImg(colour = colour)


    def singleFileFind(self, dir_,colour):
        self.img = cv2.imread(dir_)
        self._getColorImg(colour = colour)

    def _getColorImg(self,colour = 'colour'):
        if not self.colour:
            self.colour = colour
            print '_get img colour', self.colour, self.suffix
        if self.colour in self.GRAY:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        elif (self.colour in self.COLOR) and self.suffix.upper() == 'BMP':
            print 'get bgr 2 rbg'
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        else:
            pass

def yieldImg(dirs):
    if dirs[-4:].find('.') > 0:
        raise ValueError('input para is not a folder, a file')
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    for dir_ in dirlist:
        img = GetImage().get(dir_)
        yield  img

def randomImg(dirs):
    if dirs[-4:].find('.') > 0:
        raise ValueError('input para is not a folder, a file')

    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    img = GetImage().get(choice(dirlist),colour='color')
    return img

def randomBin(dirs):
    if dirs[-4:].find('.') > 0:
        raise ValueError('input para is not a folder, a file')
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    # dir_ = "tests\\data\\imgforsharp{}.bin".format(i)
    img = np.fromfile(choice(dirlist), dtype="uint8")
    img.shape = (1944, 2592)
    return img


"""" interface """
def getImage(dir_):
    return GetImage().get(dir_)
