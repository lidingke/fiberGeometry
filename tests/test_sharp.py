from setting.parameter import SETTING
SETTING().update_by_key('test', 'octagon')
from pattern.sharp import IsSharp, is_sharp_laplacian
from pattern.edge import ExtractEdge, EdgeFuncs
import numpy as np
# from util.getimg import
from util.getimg import getImage, randomImg, yieldImg, list_img_by_file
import cv2
import os
import sys
import pdb
import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt

import pytest

def _getFilterImg(core, origin, minRange, maxRange):
    img = np.ones(origin.shape, dtype='uint8') * 255
    core = [core, 1]
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), -1)
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), -1)
    img = cv2.bitwise_or(img, origin)
    return img


def n_test_new_sharp():
    imgs = randomImg("IMG\\midoctagon\\sharp\\")
    for img in imgs:
        if len(img.shape) > 2:
            img = img[:,:,2]
        kernelSize = 15
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelSize, kernelSize))
        erode = cv2.erode(img, kernel)
        dilate = cv2.dilate(img, kernel)
        img = cv2.absdiff(dilate, erode)
        img = cv2.bitwise_not(img)

        blockSize = 15
        Constant = 7
        img = cv2.adaptiveThreshold(img, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, Constant)
        corecore = SETTING()["corepoint"]
        minRange, maxRange = SETTING()["cladRange"]
        img = _getFilterImg(corecore, img, minRange, maxRange)
        # sharp = IsSharp().isSharpDiff([img,img,img])
        # img = EdgeFuncs().topHat(img, 3)
        # sumGrad2 = img.sum()
        # sharp = sumGrad2**2//img.size//100
        # cv2.imshow('img', img[::4,::4])
        # cv2.waitKey()
        img = img[::4,::4].copy()
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        areaSum = 0
        for x in contours:
            area = cv2.contourArea(x)
            areaSum = areaSum + area
        sharp = areaSum//len(contours)
        print 'get sharp', sharp


def n_test_sharp_canny():
    imgs = yieldImg("IMG\\midoctagon\\sharp\\")
    for img in imgs:
        # pdb.set_trace()
        if len(img.shape) > 2:
            img = img[:,:,2]

        # img = cv2.Canny(img, 120, 150)
        img = cv2.Sobel(img, -1, 1, 1)
        img = cv2.bitwise_not(img)
        corecore = SETTING()["corepoint"]
        minRange, maxRange = SETTING()["cladRange"]
        img = _getFilterImg(corecore, img, minRange, maxRange)
        sumGrad2 = (img**2).sum()
        normalizationSharp = sumGrad2*10000//img.size
        cv2.imshow('img', img[::4,::4])
        cv2.waitKey()
        print 'get sharp', normalizationSharp


def n_test_sharp_Laplacian():
    imgs = yieldImg("IMG\\midoctagon\\sharp\\")
    sharpobject = IsSharp()
    for img in imgs:
        if len(img.shape) > 2:
            img = img[:,:,2]

        img = sharpobject._doSharpRange(img)
        sharp = cv2.Laplacian(img, cv2.CV_64F).var()

        print 'get sharp', sharp

def test_sharp_Laplacian():
    imgs = randomImg("IMG\\emptytuple\\sharp\\")

    sharpobject = IsSharp()
    for img in imgs:
        sharp = sharpobject.issharpla(img)
        print 'get sharp', sharp



@pytest.mark.parametrize(
    "dir_",(
            ("IMG\\sharp\\02\\"),
            ("IMG\\sharp\\03\\"),

    ))
def ttest_sharp_laplacian_list(dir_):
    print dir_
    dirs = sorted(os.listdir(dir_))
    dosharp = IsSharp().issharpla
    imgs = (getImage(dir_+d) for d in dirs)
    sharps = [dosharp(img[::,::,0]) for img in imgs]
    # plt.figure(len(dir_))
    # plt.plot(range(len(sharps)),sharps)
    # plt.title(dir_)
    # plt.show()

@pytest.mark.parametrize(
    "dir_",(
            ("IMG\\sharp\\02\\"),
            ("IMG\\sharp\\03\\"),

    ))
def test_sharp_laplacian_all_list(dir_):
    print dir_
    dirs = sorted(os.listdir(dir_))
    dosharp = IsSharp().issharplaall
    imgs = (getImage(dir_+d) for d in dirs)
    sharps = [dosharp(img[::,::,0]) for img in imgs]
    origin = [sharp[0] for sharp in sharps]
    roundsharp = [sharp[1] for sharp in sharps]
    # fig = plt.figure(len(dir_))
    # ax1 = fig.add_subplot(111)
    # ax1.plot(range(len(sharps)),roundsharp)
    # ax2 = ax1.twinx()
    # ax2.plot(range(len(sharps)),origin,color='red')
    # # ax2.title(dir_)
    # plt.show()

@pytest.mark.parametrize(
    "dir_", (
            ("IMG\\sharp\\gammamid\\"),
    ))
def ttest_sharp_fft_list(dir_):
    print dir_
    dirs = sorted(os.listdir(dir_))
    def fft(img):
        get = np.fft.fft2(img)
        return np.abs(np.sum(get))

    imgs = (getImage(dir_+d) for d in dirs)
    for img in imgs:
        sharps = fft(img)
        print sharps



if __name__ == "__main__":
    dirs = "IMG\\sharp\\nonnoise2"

    for i in list_img_by_file(dirs):
        tiny = i[::4,::4].copy()
        tiny = cv2.medianBlur(tiny,5)
        print(is_sharp_laplacian(tiny))

    sums = [sharp[0] for sharp in sharps]
    sharps = [sharp[1] for sharp in sharps]
    # sums = [dosharp(img[::,::,0])[1] for img in imgs]
    # print sharps
    # fig = plt.figure(len(dir_))
    # ax1 = fig.add_subplot(111)
    # ax1.plot(range(len(sharps)),sharps)
    # ax2 = ax1.twinx()
    # ax2.plot(range(len(sharps)),sums)
    # ax2.title(dir_)
    # plt.show()