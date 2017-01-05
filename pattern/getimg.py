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

    def get(self, dir_='', colour = 'black'):
        if dir_.find('.') > 0:
            self.singleFileFind(dir_,colour)
        else :
            self.fileFind(dir_,colour)
        if not isinstance(self.img, np.ndarray):
            raise ValueError('img not ndarray')
        return self.img

    def fileFind(self, dir_,colour):
        for file in os.listdir(dir_):
            # pdb.set_trace()
            self.img = cv2.imread(dir_ + "\\" + file)
            self.origin = self.img.copy()
            if len(self.img.shape) == 3 and colour == 'black':
                self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)


    def singleFileFind(self, dir_,colour):
        self.img = cv2.imread(dir_)
        self.origin = self.img.copy()
        if len(self.img.shape) == 3 and colour == 'black':
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)

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
