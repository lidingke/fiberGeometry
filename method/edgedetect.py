import cv2
import numpy as np
import pdb
from method.toolkit import Cv2ImShow
from setting.set import SETTING

class Edge(object):
    """docstring for Edge"""
    def __init__(self, ):
        super(Edge, self).__init__()
        self.show = Cv2ImShow()

    def run(self, img):
        pass

class Canny(Edge):
    """docstring for Canny"""
    def __init__(self, ):
        super(Canny, self).__init__()
        # self.arg = arg

    def run(self,img):
        # img = cv2.GaussianBlur(img,(3, 3 ),0)
        img = cv2.Canny(img, 40, 200)
        img = cv2.bitwise_not(img)
        return img

class Threshold(Edge):
    """docstring for Threshold"""
    def __init__(self, ):
        super(Threshold, self).__init__()

    def run(self, img):

        img = cv2.GaussianBlur(img,(3, 3 ),0)
        # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        # pdb.set_trace()
        # self._calcHist(img)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)
        cv2.imshow("hist",img[::2,::2])
        cv2.waitKey(0)
        img = cv2.Canny(img, 10, 200)
        img = cv2.bitwise_not(img)
        return img

class ErodeDilate(Edge):
    """docstring for ErodeDilate"""
    def __init__(self, ):
        super(ErodeDilate, self).__init__()
        # self.arg = arg
        self.SET = SETTING()

    def run(self, img):
        medianBlur = self.SET["medianBlur"]["ErodeDilateKsize"]
        img = cv2.medianBlur(img, 9)

        # img  = cv2.pyrMeanShiftFiltering(img, 30, 30, 5)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        erode = cv2.erode(img, kernel)
        dilate = cv2.dilate(img, kernel)
        # img = np.array(arrimg)
        img = cv2.absdiff(dilate, erode)
        # img = cv2.absdiff(img,erode)
        img = cv2.bitwise_not(img)
        blockSize = self.SET["adaptiveTreshold"]["blockSize"]
        Constant = self.SET["adaptiveTreshold"]["Constant"]
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)
        # img = cv2.erode(img,kernel)
        # img = cv2.equalizeHist(img)
        # img = cv2.dilate(img,kernel)
        # img = cv2.medianBlur(img,3)
        # cts,hy = cv2.findContours(img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE, offset=(0, 0))
        return img

class CloseOpen(Edge):
    """docstring for CloseOpen"""
    def __init__(self, ):
        super(CloseOpen, self).__init__()
        # self.arg = arg

    def run(self, img):
        pass


    def _open(self, img, time_ = 4, kernelLen = 3, ):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernelLen, kernelLen))
        for x in range(1,time_):
            img = cv2.erode(img,kernel)
            img = cv2.dilate(img,kernel)
        return img

    def _close(self, img, time_ = 4, kernelLen = 3):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernelLen, kernelLen))
        for x in range(1,time_):
            img = cv2.dilate(img,kernel)
            img = cv2.erode(img,kernel)
        return img

    def topHat(self,img):
        img = cv2.absdiff(img,self._open(img))
        img = cv2.bitwise_not(img)
        return img

    def blackHat(self,img):
        img = cv2.absdiff(self._close(img), img)
        img = cv2.bitwise_not(img)
        return img



