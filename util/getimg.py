import cv2
import os
from random import choice
# import pdb
import numpy as np
# from pattern.meta import CV2MethodSet
import sys

import os


# old
class GetImage(object):
    """docstring for GetImage"""

    def __init__(self, ):
        super(GetImage, self).__init__()
        self.img = False
        self.colour = None
        self.suffix = ''
        self.GRAY = ('gray', 'black')
        self.COLOR = ('colour', 'color')

    def get(self, dir_='', colour='colour'):
        assert os.path.isfile(dir_)
        self.suffix = dir_.split('.')[-1]
        self.singleFileFind(dir_, colour)
        assert isinstance(self.img, np.ndarray)
        # if not isinstance(self.img, np.ndarray):
        #     raise ValueError('img not ndarray')
        if self.img.dtype != "uint8":
            self.img = cv2.convertScaleAbs(self.img)
            # self.img = np.array(self.img,dtype="uint8")
        return self.img

    def fileFind(self, dir_, colour):
        for file in os.listdir(dir_):
            self.suffix = dir_.split('.')[-1]
            self.img = cv2.imread(dir_ + "\\" + file)
            self._getColorImg(colour=colour)

    def singleFileFind(self, dir_, colour):
        self.img = cv2.imread(dir_)
        self._getColorImg(colour=colour)

    def _getColorImg(self, colour='colour'):
        if not self.colour:
            self.colour = colour
        if self.colour in self.GRAY:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        elif (self.colour in self.COLOR) and self.suffix.upper() == 'BMP':
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        else:
            pass


def randomImg(dirs):
    if dirs[-1] != '/':
        dirs = dirs + '/'
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    img = GetImage().get(choice(dirlist), colour='color')
    return img


def randomBin(dirs):
    if dirs[-4:].find('.') > 0:
        raise ValueError('input para is not a folder, a file')
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    img = np.fromfile(choice(dirlist), dtype="uint8")
    img.shape = (1944, 2592)
    return img


def yieldImg(dirs):
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    for dir_ in dirlist:
        img = GetImage().get(dir_, 'colour')
        yield img


def get_img_by_dir(dir_, colour='colour'):
    assert os.path.isfile(dir_)
    array = cv2.imread(dir_)
    assert isinstance(array, np.ndarray)
    if colour not in ('colour', 'color'):
        array = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)
        return array
    if dir_[-3:].upper() == "BMP":
        array = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
        return array
    return array


def random_img_by_file(dirs):
    assert os.path.isdir(dirs)
    dirlist = os.listdir(dirs)
    dirlist = [os.path.join(dirs, x) for x in dirlist]
    img = get_img_by_dir(choice(dirlist), colour='colour')
    return img


def list_img_by_file(dirs):
    assert os.path.isdir(dirs)
    files = os.listdir(dirs)
    dirlist = [os.path.join(dirs, x) for x in files]
    imgs = [get_img_by_dir(path, colour='colour') for path in dirlist]
    return imgs


def yield_img_by_file(dirs):
    assert os.path.isdir(dirs)
    files = os.listdir(dirs)
    dirlist = [os.path.join(dirs, x) for x in files]
    for path in dirlist:
        img = get_img_by_dir(path, colour='colour')
        yield img


"""" interface """

# def getImage(dir_):
#     return GetImage().get(dir_)


getImage = get_img_by_dir
randomImg = random_img_by_file
random_img = randomImg
get_img = getImage
