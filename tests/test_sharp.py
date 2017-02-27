from setting.orderset import SETTING
SETTING().keyUpdates('test', 'octagon')
from pattern.sharp import IsSharp
from pattern.edge import ExtractEdge, EdgeFuncs
import numpy as np
from util.loadimg import yieldImg
import cv2
import pdb
import pytest

def _getFilterImg(core, origin, minRange, maxRange):
    img = np.ones(origin.shape, dtype='uint8') * 255
    core = [core, 1]
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), -1)
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), -1)
    # origin = cv2.bitwise_not(origin)
    img = cv2.bitwise_or(img, origin)
    return img


def n_test_new_sharp():
    imgs = yieldImg("IMG\\midoctagon\\sharp\\")
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
        # cv2.imshow('img', img[::4,::4])
        # cv2.waitKey()


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
        # pdb.set_trace()
        if len(img.shape) > 2:
            img = img[:,:,2]
        # cv2.imshow('img', img[::4,::4])
        # cv2.waitKey()
        # img = cv2.Canny(img, 120, 150)
        img = sharpobject._doSharpRange(img)
        sharp = cv2.Laplacian(img, cv2.CV_64F).var()

        print 'get sharp', sharp


if __name__ == "__main__":
    n_test_sharp_canny()
    pass

