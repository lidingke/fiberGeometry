import cv2
import numpy as np
import pdb
from operator import itemgetter
from pattern.getimg import GetImage
from pattern.getimg import getImage
from pattern.edge import ExtractEdge
from .classify import MetaClassify


class OctagonClassify(object):
    """find: return a plot for plot show
    getResult: return a final result for result show"""
    def __init__(self,):
        super(OctagonClassify, self).__init__()


    def find(self, img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        resultForm = self._formClassify(contours)
        self._classOctagon(resultForm['octagonClad'])

    def getResult(self):
        pass


    def _formClassify(self, contours):
        resultForm = {'core':False, 'octagonClad':False}
        return resultForm

    def _classOctagon(self, img):
        co = ClassOctagon()
        tempPlots = co.run(img)
        return tempPlots


class ClassOctagon(object):

    def __init__(self):
        super(ClassOctagon, self).__init__()

    def angleRatio(self, A, B, C):
        """"baike baidu yuxiandingli
        A-c-B-a-C-b JIAO A"""
        c = np.sqrt(((A[0][0] - B[0][0]) ** 2 + (A[0][1] - B[0][1]) ** 2))
        a = np.sqrt(((C[0][0] - B[0][0]) ** 2 + (C[0][1] - B[0][1]) ** 2))
        b = np.sqrt(((A[0][0] - C[0][0]) ** 2 + (A[0][1] - C[0][1]) ** 2))
        dif = (b ** 2 + c ** 2 - a ** 2)
        diff = (2 * b * c)
        alpha =  dif//diff
        return alpha

    def horizonalRatio(self, A, B):
        C = [[B[0][0], A[0][1]]]
        return self.angleRatio(A, B, C)

    def _getLongAxit(self, points):
        lenPoints = points.shape[0]
        print 'lens is ', lenPoints
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

    def _getResult(self, longAxis, midPoint, getVerticalPoint):

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
        point2 = np.array(getVerticalPoint[2])
        result['contour'] = np.array([longAxis[1], longAxis[2], vPoint, point1, point2])
        # pdb.set_trace()
        return result


    def run(self, img):
        """
        :findContours->convexHull->sortMaxPointsDistance
        ->calculateVerticalPoint->result: Long & short axis
        :param img:
        :return:
        """
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        tempPlots = np.ones(img.shape) * 255
        # tempPlots = img
        for contour in contours:
            cv2.drawContours(tempPlots, contour, -1, (0, 0, 255))
        mergedpoints = np.concatenate(contours[1:])
        points = cv2.convexHull(points=mergedpoints)
        longAxis = self._getLongAxit(points)
        x, y = tuple(longAxis[1][0].tolist()),tuple(longAxis[2][0].tolist())
        cv2.line(tempPlots, x, y, (0, 255, 0), 2)
        midPoint = longAxis[1][0] + longAxis[2][0]
        midPoint = midPoint / 2
        getVerticalPoint = points.tolist()
        getVerticalPoint.sort(key=lambda x: abs(self.angleRatio([midPoint], longAxis[1], x)))
        x, y = tuple(getVerticalPoint[0][0]), tuple(midPoint.tolist())
        print 'get x y ', x, y, midPoint, longAxis
        cv2.line(tempPlots, x, y, (0, 25, 25), 2)

        # forEllipese = (tuple(getVerticalPoint[0][0]), tuple(longAxis[1][0].tolist()), tuple(longAxis[2][0].tolist()))
        # forEllipese = np.array(forEllipese)
        # ellipese = cv2.fitEllipse(forEllipese)
        # cv2.ellipse(result, ellipese)

        result = self._getResult(longAxis, midPoint, getVerticalPoint)
        # pdb.set_trace()
        ellipese = cv2.fitEllipse(result['contour'])
        cv2.ellipse(tempPlots, ellipese, (0, 25, 25), 2)
        result['plot'] = tempPlots
        return  result
