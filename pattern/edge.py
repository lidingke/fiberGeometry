import cv2
import numpy as np
from pattern.meta import CV2MethodSet
from method.toolkit import timing

class ExtractEdge(CV2MethodSet):
    """docstring for ExtractEdge"""
    def __init__(self, ):
        super(ExtractEdge, self).__init__()
        # self.arg = arg

    # @timing
    def run(self, img):
        """medianBlur consume 0.23s"""
        medianBlur = self.SET["medianBlur"]["ErodeDilateKsize"]
        img = cv2.medianBlur(img, medianBlur)
        # img  = cv2.pyrMeanShiftFiltering(img, 30, 30, 5)
        if len(img.shape) > 2:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        erode = cv2.erode(img, kernel)
        dilate = cv2.dilate(img, kernel)
        img = cv2.absdiff(dilate, erode)

        img = cv2.bitwise_not(img)
        blockSize = self.SET["adaptiveTreshold"]["blockSize"]
        Constant = self.SET["adaptiveTreshold"]["Constant"]
        img = cv2.adaptiveThreshold(img, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, Constant)
        return img

