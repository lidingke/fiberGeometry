import cv2
from pattern.meta import CV2MethodSet


class ExtractEdge(CV2MethodSet):
    """docstring for ExtractEdge"""
    def __init__(self, ):
        super(ExtractEdge, self).__init__()

    # @timing
    def run(self, img):
        """medianBlur consume 0.23s"""

        if len(img.shape) > 2:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        kernelSize = self.SET["adaptiveTreshold"].get("kernelSize",7)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelSize, kernelSize))
        erode = cv2.erode(img, kernel)
        dilate = cv2.dilate(img, kernel)
        img = cv2.absdiff(dilate, erode)
        img = cv2.bitwise_not(img)
        blockSize = self.SET["adaptiveTreshold"]["blockSize"]
        Constant = self.SET["adaptiveTreshold"]["Constant"]
        img = cv2.adaptiveThreshold(img, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, Constant)
        return img

class EdgeFuncs(object):
    """docstring for CloseOpen"""
    def __init__(self, ):
        super(EdgeFuncs, self).__init__()
        # self.arg = arg

    def open(self, img, time_ = 4, kernelLen = 3, ):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernelLen, kernelLen))
        for x in range(1,time_):
            img = cv2.erode(img,kernel)
            img = cv2.dilate(img,kernel)
        return img

    def close(self, img, time_ = 4, kernelLen = 3):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernelLen, kernelLen))
        for x in range(1,time_):
            img = cv2.dilate(img,kernel)
            img = cv2.erode(img,kernel)
        return img

    def topHat(self,img, kernelLen = 3):
        img = cv2.absdiff(img,self.open(img, kernelLen))
        img = cv2.bitwise_not(img)
        return img

    def blackHat(self,img, kernelLen = 3):
        img = cv2.absdiff(self.close(img, kernelLen ), img)
        img = cv2.bitwise_not(img)
        return img

    def multiDilate(self, img, time_ = 4, kernelLen = 3):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernelLen, kernelLen))
        for x in range(1,time_):
            img = cv2.dilate(img,kernel)
        return img

    def multiErode(self, img, time_ = 4, kernelLen = 3):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernelLen, kernelLen))
        for x in range(1,time_):
            img = cv2.erode(img,kernel)
        return img


