import cv2
from pattern.meta import CV2MethodSet
from pattern.edge import ExtractEdge
from method.toolkit import timing
import numpy as np
import pdb

class IsSharp(CV2MethodSet):
    """docstring for IsSharp"""
    def __init__(self):
        super(IsSharp, self).__init__()


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

        imgAllor = np.zeros(imgs[0][::5,::5].shape, dtype=imgs[0].dtype)
        for img in imgs[-3:]:
            img = ExtractEdge().run(img[::5,::5])
            imgAllor = cv2.bitwise_or(imgAllor, img)
        imgAllor = cv2.bitwise_not(imgAllor)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        imgAllor = cv2.erode(imgAllor, kernel)
        # self.Show.show('sharp', imgAllor)
        # imgAllor = cv2.medianBlur(imgAllor, 7)
        sumGrad2 = imgAllor.sum()

        normalizationSharp = sumGrad2**2//imgAllor.size//1000.0

        return normalizationSharp


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