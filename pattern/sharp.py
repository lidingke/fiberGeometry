import collections

import cv2
import numpy as np

from pattern.edge import ExtractEdge
from pattern.meta import CV2MethodSet
from setting.orderset import SETTING


class IsSharp(CV2MethodSet):
    """docstring for IsSharp"""
    def __init__(self):
        super(IsSharp, self).__init__()
        self.SET = SETTING()


    def isSharp(self, img):
        #better than isSharpCanny
        # midsize = self._midSize(sizecoup = img.shape)
        # img = img[midsize[0]:midsize[1],midsize[2]:midsize[3]]
        # img = cv2.GaussianBlur(img,(5, 5 ),0)
        img = self.erodeDilate(img)
        # self.Show.show("sharp", img[::4,::4])
        sumGrad2 = (img**2).sum()
        normalizationSharp = sumGrad2*1000//img.size
        return normalizationSharp/1000.0

    def _imgs2gray(self,imgs):
        result = []
        for img in imgs:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            result.append(img)
        return result

    # @timing
    def isSharpDiff(self, imgs):
        if len(imgs[0].shape) == 3:
            imgs = self._imgs2gray(imgs)
        # for i,img in enumerate(imgs):
        #     img.tofile("tests\\data\\imgforsharp{}.bin".format(i))
        imgs = [self._doSharpRange(img) for img in imgs]
        # self._doSharpRange(img)
        imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
        for img in imgs[-3:]:
            img = ExtractEdge().run(img)
            imgAllor = cv2.bitwise_or(imgAllor, img)
        imgAllor = cv2.bitwise_not(imgAllor)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        imgAllor = cv2.erode(imgAllor, kernel)
        # self.Show.show('sharp', imgAllor)
        # imgAllor = cv2.medianBlur(imgAllor, 7)
        sumGrad2 = imgAllor.sum()
        normalizationSharp = sumGrad2**2//imgAllor.size//100

        return normalizationSharp

    def _doSharpRange(self, img):
        # if hasattr(self.SET, "corepoint") and hasattr(self.SET, "cladRange"):
        if "cladRange" in self.SET:
            corex, corey = self.SET["corepoint"]
            minRange, maxRange = self.SET["cladRange"]
            begin = (corex - maxRange, corey - maxRange)
            end = (corex + maxRange, corey + maxRange)
            return img[begin[0]:end[0]:2, begin[1]:end[1]:2]
        else:
            return img[::5,::5]



    def erodeDilate(self,img):
        # img = cv2.medianBlur(img, 9)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 7))
        erode = cv2.erode(img,kernel)
        dilate = cv2.dilate(img,kernel)
        img = cv2.absdiff(dilate,erode)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)

        return img

    def _midSize(self,sizecoup = (100,100), rato = 0.1):
        x00 = int(sizecoup[0]*rato)
        x01 = int(sizecoup[0]*(1-rato))
        x10 = int(sizecoup[1]*(rato))
        x11 = int(sizecoup[1]*(1-rato))
        return (x00, x01, x10 ,x11)


class MaxSharp(object):

    def __init__(self):
        super(MaxSharp, self).__init__()
        self.deque = collections.deque(maxlen = 20)

    def isRight(self, sharp):
        sharp = float(sharp)
        self.deque.append(sharp)

        if len(self.deque) < 5:
            return False
        sortque = sorted(list(self.deque))
        if sharp > sortque[-1] * 0.6:
            return True
        else:
            return False