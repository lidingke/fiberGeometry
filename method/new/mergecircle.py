import cv2
import numpy as np

from method.toolkit import Cv2ImShow, Cv2ImSave
from method.toolkit import IsCircle, cv2CircleIndex, XlsWrite, Cv2ImShow


from method.edgedetect import ErodeDilate
from setting.set import SETTING
import pdb



class MergeCircle(object):
    """docstring for MergeCircle"""
    def __init__(self, ):
        super(MergeCircle, self).__init__()
        # self.arg = arg
        self.img = cv2.imread("method\\new\\dcircle.png")
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        # self.img = cv2.imread(self.file)
        self.origin = self.img.copy()
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.circleIndex = cv2CircleIndex()
        st = SETTING({})
        # pdb.set_trace()

    def flow(self):
        img = self.img

        img = ErodeDilate().run(img)
        self.show.show('img', img)
        self.ellipseForIfCondition(img)
        # print 'contours', contours
        # pdb.set_trace()


    def runNoThrowChirldMethod(self, img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        result = np.ones(img.shape) * 255
        print 'before contour', hierarchys
        fatherDot = set()
        for i,x in enumerate(contours):
            xhierar = hierarchys[0][i]
            area , circleIndex = self.circleIndex.contourIn(x)
            fatherDot.add(xhierar[3])
        print 'fatherdot', fatherDot
        for x in fatherDot:
            cv2.drawContours(result, contours[x], -1, (0,0,255))
        return img, result, contours, xrange(0, len(hierarchys[0]))


    def ellipseForIfCondition(self, img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        ellipses, eContours = [], []
        for x, contour in enumerate(contours):
            if contour.shape[0] > 5:
                area, circleIndex = self.circleIndex.contourIn(contour)
                if area > 50:
                    ellipseResult = cv2.fitEllipse(contour)
                    ellipses.append(ellipseResult)
                    eContours.append(contour)
                    print area, circleIndex, ellipseResult
        # for x in ellipses:
        result = np.zeros(img.shape)
        cv2.drawContours(result, eContours, -1, (255))
        # self.show.show('img',result)
        self.mergeCircle(eContours[2], eContours[1])
        # self.mergeContour(eContours[2], eContours[1])
        # pdb.set_trace()

    # def mergeContour(self, contourIn, contourOut):
    #     # try:
    #     allContour = []
    #     # pdb.set_trace()
    #     shapeIn = contourIn.shape
    #     shapeOut = contourOut.shape

    #     # pdb.set_trace()
    #     # contourIn.flatten()+
    #     for x in contourIn:
    #         # for y in x:
    #         allContour.append((x[0],x[1]))

    #     contourOut = contourOut.reshape(:,2)
    #     for x in contourOut:
    #         allContour.append((x[0],x[1]))
    #     # pdb.set_trace()
    #     allContour = np.array(allContour)
    #     # allContour = np.intersect1d(contourIn, contourOut)
    #     ellipseResult = cv2.fitEllipse(allContour)
    #     print 'ellipseResult', ellipseResult

    #     # except Exception, e:
        #     pdb.set_trace()


    def mergeCircle(self, contourIn, contourOut):
        resultIn = np.zeros(self.img.shape, dtype=self.img.dtype)
        cv2.drawContours(resultIn, contourIn, -1, (255), -1)
        cv2.fillConvexPoly(resultIn, contourIn, (255))
        # pdb.set_trace()
        resultOut = np.zeros(self.img.shape, dtype=self.img.dtype)
        cv2.drawContours(resultOut, contourOut, -1, (255), -1)
        cv2.fillConvexPoly(resultOut, contourOut, (255))
        # self.show.show('in', resultIn)
        # self.show.show('out', resultOut)
        self.show.show('two', resultOut - resultIn)
        resultTwo = resultOut - resultIn
        last = []
        while True:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            resultTwo = cv2.erode(resultTwo, kernel)
            contours, hierarchys = cv2.findContours(resultTwo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            # print 'len(hierarchys)', hierarchys.shape
            # if len(hierarchys[0]) == 2:
            #     print hierarchys
            #     for x in contours:
            #         ellipseResult = cv2.fitEllipse(x)
            #         print 'ellipseResult', ellipseResult
            # if (hierarchys == None) or (len(hierarchys[0]) == 1):
            #     break
            if len(hierarchys[0]) > 2:
                break
            last = [contours, hierarchys]
        # allContour = ()
        # for con in last[0]:
        #     for point in con:
        #         allContour = point
        # pdb.set_trace()
        allContour = np.concatenate(contours)
        ellipseResult = cv2.fitEllipse(allContour)
        print 'ellipseResult', ellipseResult
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        # resultTwo = cv2.erode(resultTwo, kernel)
        # self.show.show('little two', resultTwo)
        # pdb.set_trace()

        # contours, hierarchys = cv2.findContours(resultTwo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # imgContour = np.zeros(self.img.shape, dtype=self.img.dtype)
        # cv2.drawContours(imgContour, contours, -1, (255), -1)

        # print 'hierarchys', hierarchys
        # self.show.show('imgContour', imgContour)
        # # pdb.set_trace()
