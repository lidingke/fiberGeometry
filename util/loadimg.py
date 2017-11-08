from pattern.edge import ExtractEdge
from pattern.getimg import getImage
import cv2
import numpy as np
import os
from pattern.edge import EdgeFuncs


# def edge2img(dirs):
#     dirlist = os.listdir(dirs)
#     dirlist = [dirs + x for x in dirlist]
#     imgs = []
#     for dir_ in dirlist:
#         img = GetImage().get(dir_)
#         imgs.append(img)
#     imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
#     for img in imgs:
#         img = ExtractEdge().run(img)
#         imgAllor = cv2.bitwise_or(imgAllor, img)
#     img = imgAllor
#     img = EdgeFuncs().open(img, 10)
#     img = cv2.medianBlur(img, 3)
#     return img


def yieldImg(dirs):
    dirlist = os.listdir(dirs)
    dirlist = [dirs + x for x in dirlist]
    for dir_ in dirlist:
        img = GetImage().get(dir_, 'colour')
        yield  img


def sliceImg(img, core, slice, split = 1):
    corex, corey = core
    maxRange = slice
    begin = (corex - maxRange, corey - maxRange)
    end = (corex + maxRange, corey + maxRange)
    if len(img.shape) == 2:
        return img[begin[0]:end[0]:split, begin[1]:end[1]:split]
    else:
        return img[begin[0]:end[0]:split, begin[1]:end[1]:split]
