from __future__ import  division
import cv2
import numpy as np
import pdb
from operator import itemgetter
from pattern.getimg import GetImage
from pattern.getimg import getImage
from pattern.edge import ExtractEdge, EdgeFuncs
from pattern.exception import ClassCoreError, ClassOctagonError
from setting.orderset import SETTING
from util.timing import timing


class PickCircle(object):
    def __init__(self):
        super(PickCircle, self).__init__()

    # @timing
    def run(self,img):
        blurindex = SETTING()["medianBlur"].get("corefilter", 3)

        img = cv2.medianBlur(img, blurindex)
        # cv2.imshow("img", img[::4, ::4])
        # cv2.waitKey()
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        tempPlots = np.ones(img.shape) * 255
        print 'get contours len', len(contours)
        if len(contours) == 0:
            raise ClassCoreError
        elif len(contours) == 1:
            mergedpoints =contours[0]
        else:
            mergedpoints = np.concatenate(contours[1:])
        ellipse = cv2.fitEllipse(mergedpoints)
        result = self._getResult(ellipse)
        result['ellipese'] = ellipse
        cv2.ellipse(tempPlots, ellipse, (0,255,255))
        result['plot'] = tempPlots
        result['contour'] = mergedpoints
        return result

    def _getResult(self, ellipse):
        result = {}
        result['longAxisLen'] = ellipse[1][1]
        result['shortAxisLen'] = ellipse[1][0]
        result['corePoint'] = np.array([ellipse[0]])
        return result




class PickOctagon(object):

    def __init__(self):
        super(PickOctagon, self).__init__()

    def angleRatio(self, A, B, C):
        """"baike baidu yuxiandingli
        A-c-B-a-C-b JIAO A"""
        c = np.sqrt(((A[0][0] - B[0][0]) ** 2 + (A[0][1] - B[0][1]) ** 2))
        a = np.sqrt(((C[0][0] - B[0][0]) ** 2 + (C[0][1] - B[0][1]) ** 2))
        b = np.sqrt(((A[0][0] - C[0][0]) ** 2 + (A[0][1] - C[0][1]) ** 2))
        dif = (b * b + c * c - a * a)
        diff = (2 * b * c)
        if diff == 0:
            return 1
        alpha =  dif/diff
        return alpha

    def horizonalRatio(self, A, B):
        C = [[B[0][0], A[0][1]]]
        return self.angleRatio(A, B, C)


    def _getLongAxit(self, points):
        lenPoints = points.shape[0]
        # print 'lens is ', lenPoints
        pointsContain = []
        for i in range(0, lenPoints):
            points2top = []
            for j in range(0, lenPoints):
                _ = np.linalg.norm(points[i] - points[j])
                horiAngl = self.horizonalRatio(points[i], points[j])
                alist = (_, points[i], points[j], horiAngl)
                points2top.append(alist)
            points2top.sort(key=itemgetter(0))
            pointsContain.append(points2top[-1])
            # print i, 'st len:', len(pointsContain), pointsContain[-1][3]
        pointsContain.sort(key=itemgetter(0))
        return pointsContain[-1]

    def _getResult(self, longAxis, midPoint, getVerticalPoint,tempCounters):
        result = {}
        vPoint = getVerticalPoint[0]
        result['longAxisLen'] = longAxis[0]
        vPoint = np.array(vPoint)
        midPoint = np.array([midPoint])
        result['shortAxisLen'] = np.linalg.norm(vPoint - midPoint)*2
        result['corePoint'] = midPoint
        if len(getVerticalPoint) < 3:
            raise ValueError('not enough points')
        point1 = np.array(getVerticalPoint[1])
        point2 = np.array(getVerticalPoint[-1])
        # pdb.set_trace()
        # result['contour'] = np.array([longAxis[1], longAxis[2], vPoint, point1, point2])
        result['contour'] = np.array([tempCounters[0], tempCounters[-1], point1, point2, longAxis[1], longAxis[2], vPoint ])
        # pdb.set_trace()
        return result

    def _getHalfList(self, list_):
        len_ = len(list_)
        if len_ > 3:
            end = int(len_/2)
            return list_[end:]
        else:
            return list_

    @timing
    def run(self, img):
        """
        :findContours->convexHull->sortMaxPointsDistance
        ->calculateVerticalPoint->result: Long & short axis
        :param img:
        :return:
        """

        blurindex = SETTING()["medianBlur"].get("cladfilter", 3)
        img = cv2.medianBlur(img, blurindex)
        # img = cv2.adaptiveBilateralFilter
        img = cv2.bilateralFilter(img, 5, 80, 75)
        # img = EdgeFuncs().close(img,kernelLen=3)
        # print 'get blur index ', blurindex
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        tempPlots = np.ones(img.shape) * 255

        for contour in contours:
            cv2.drawContours(tempPlots, contour, -1, (0, 0, 255))
        for contour in contours:
            cv2.drawContours(tempPlots, contour, -1, (0, 0, 255))
        if len(contours) == 0:
            raise ClassCoreError
        elif len(contours) == 1:
            mergedpoints = contours[0]
        else:
            mergedpoints = np.concatenate(contours[1:])
        points = cv2.convexHull(points=mergedpoints)
        longAxis = self._getLongAxit(points)
        result = {}
        x, y = tuple(longAxis[1][0].tolist()),tuple(longAxis[2][0].tolist())
        result['longPlot'] = (x, y)
        cv2.line(tempPlots, x, y, (0, 255, 0), 8)
        midPoint = longAxis[1][0] + longAxis[2][0]
        midPointf = midPoint /2
        midPoint = midPoint // 2

        getVerticalPoint = mergedpoints.tolist()
        getVerticalPoint.sort(key = lambda x: np.linalg.norm(x-midPoint))
        # getVerticalPoint = getVerticalPoint[:-2]
        tempCounters = (getVerticalPoint[0], getVerticalPoint[-1])
        getVerticalPoint = self._getHalfList(getVerticalPoint)
        getVerticalPoint.sort(key = lambda x: abs(self.angleRatio([midPoint], longAxis[1], x)))
        # getVerticalPoint.sort(key=lambda x: abs(self.horizonalRatio45([midPoint], longAxis[1], x)))

        # print 'get x y ', x, y, midPoint, longAxis
        # pdb.set_trace()
        x,y = tuple(midPoint.tolist()), tuple(getVerticalPoint[0][0])

        cv2.line(tempPlots, x, y, (0, 255, 0), 8)
        result['shortPlot'] = (x,y)
        result.update(self._getResult(longAxis, midPoint, getVerticalPoint,tempCounters))

        # print 'result[\'contour\']', result['contour']
        ellipse = cv2.fitEllipse(result['contour'])
        # cv2.ellipse(tempPlots, ellipse, (0, 25, 25), 4)
        result['plot'] = tempPlots
        result['ellipese'] = ellipse

        for circleCore in result['contour']:
            circleCore = tuple(circleCore[0].tolist())
            cv2.circle(tempPlots, circleCore, 40, (0,255,0), lineType=4)
        return  result
