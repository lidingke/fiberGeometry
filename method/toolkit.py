import cv2
import numpy as np
import pdb

class CalcHist(object):
    """docstring for CalcHist"""
    def __init__(self, ):
        super(CalcHist, self).__init__()

    def run(self,img):

        hist = cv2.calcHist([img], [0], None, [256], [0.0,255.0])
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
        histImg = np.zeros([256,256,1],np.uint8)
        hpt = int(0.9*256)
        for h in range(256):
            intensity = int(hist[h]*hpt/maxVal)
            cv2.line(histImg,(h,256),(h,256-intensity), [255,0,0])
        cv2.imshow("hist",histImg)
        cv2.waitKey(0)


class IsCircle(object):
    """docstring for IsCircle"""
    def __init__(self, ):
        super(IsCircle, self).__init__()
        # self.arg = arg

    # def run(self):
    def run(self, area, center, contours):
        # pdb.set_trace()
        forMaxNumber = []
        for x in contours:
            absLen = ((center[0]-x[0][0])**2 + (center[1]-x[0][1])**2)**0.5
            forMaxNumber.append(absLen)
        forMaxNumber.sort()
        maxLen = forMaxNumber[-1]
        if maxLen == 0:
            return 0
        return area/(maxLen**2*3.14)


class Cv2ImShow(object):
    """docstring for Cv2ImShow"""
    def __init__(self, ):
        super(Cv2ImShow, self).__init__()
        # self.arg = arg

    def show(self, title ,img):
        cv2.imshow(title, img)
        cv2.waitKey(0)



