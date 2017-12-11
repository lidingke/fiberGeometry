from __future__ import division
import cv2
import numpy as np
import time

from pattern.adaptivefilter import adaptive_filter_by_median
from pattern.coverimg import out_fill_by_white_circle
from pattern.exception import  NoneContoursError, PolyPointsError
import logging

from util.timing import timing

logger = logging.getLogger(__name__)


class MetaPick(object):
    def __init__(self):
        super(MetaPick, self).__init__()
        self._adaptive_filter_by_median = adaptive_filter_by_median

    # @timing
    def run(self, img, blurindex=False):
        # blurindex = SETTING()["medianBlur"].get("corefilter", 3)
        # raise ValueError("abc")
        if blurindex:
            img = cv2.medianBlur(img, blurindex)
        # cv2.imshow("img", img[::4, ::4])
        # cv2.waitKey()
        contours, hierarchys = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # tempPlots = np.ones(img.shape) * 255
        logger.info('get contours len %s' % len(contours))
        if len(contours) == 0:
            raise NoneContoursError("contours = 0")
        elif len(contours) == 1:
            mergedpoints = contours[0]
        else:
            mergedpoints = np.concatenate(contours[1:])
        ellipse = cv2.fitEllipse(mergedpoints)
        result = self._getResult(ellipse)
        result['ellipese'] = ellipse
        # cv2.ellipse(tempPlots, ellipse, (0,255,255))
        # result['plot'] = tempPlots

        result['contour'] = mergedpoints
        return result

    def _getResult(self, ellipse):
        result = {}
        result['longAxisLen'] = ellipse[1][1]
        result['shortAxisLen'] = ellipse[1][0]
        result['corePoint'] = np.array([ellipse[0]])
        plots = ("ellipse", (ellipse, (0, 102, 255), 5), {'lineType': 5})
        result['plots'] = [plots]
        return result


class PickCircle(MetaPick):
    def __init__(self):
        super(PickCircle, self).__init__()


class PickHullCircle(MetaPick):
    def __init__(self):
        super(PickHullCircle, self).__init__()

    # @timing
    def run(self, img, blurindex=False):
        # if blurindex:
        #     img = cv2.medianBlur(img, blurindex)
        # else:
        #     img = self._adaptive_filter_by_median(img)
        img = cv2.medianBlur(img, 11)
        # img = out_fill_by_white_circle(img, [1296, 972], 1200)

        # cv2.imshow("img", img[::4, ::4])
        # cv2.waitKey()
        contours, hierarchys = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        logger.info('get contours len %s' % len(contours))
        if len(contours) == 0:
            raise NoneContoursError()
        elif len(contours) == 1:
            mergedpoints = contours[0]
        else:
            mergedpoints = np.concatenate(contours[1:])
        hull = cv2.convexHull(mergedpoints)
        if len(hull) <= 5:
            raise ValueError("not enough hull point")
        ellipse = cv2.fitEllipse(hull)
        result = self._getResult(ellipse)
        result['ellipese'] = ellipse
        result['contour'] = mergedpoints
        return result


class PickPoly(MetaPick):
    def __init__(self, poly):
        super(PickPoly, self).__init__()
        self.poly_number = poly

    def run(self, img, blurindex=False):

        # if blurindex:
        #     img = cv2.medianBlur(img, blurindex)
        # else:
        #     img = self._adaptive_filter_by_median(img)
        img = cv2.medianBlur(img, 11)

        # blurindex = 37
        # cv2.imshow("{}".format(blurindex), img[::4, ::4])
        # cv2.waitKey()
        contours, hierarchys = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        logger.info('get contours len %s' % len(contours))
        if len(contours) == 0:
            raise NoneContoursError("contours = 0")
        elif len(contours) == 1:
            mergedpoints = contours[0]
        else:
            mergedpoints = np.concatenate(contours[1:])
        hull = cv2.convexHull(mergedpoints)

        ellipse, plots = self._get_poly_8(hull)

        result = self._getResult(ellipse)
        result['ellipese'] = ellipse
        result['plots'] = plots

        return result

    def _get_poly_8(self, contour):
        """ellipse format: ((x,y),(s,l),0)"""
        plots = []
        epsilon = 100
        # img = img.copy()
        def dynamic_approx_poly(epsilon):
            for i in range(20):
                poly_points = cv2.approxPolyDP(contour, epsilon=epsilon, closed=True)
                if len(poly_points) == self.poly_number:
                    return poly_points
                elif len(poly_points) > self.poly_number:
                    epsilon += 50
                else:
                    epsilon -= 50
                return poly_points

        poly_points = dynamic_approx_poly(epsilon)

        if len(poly_points) < 5:
            raise PolyPointsError("poly point not enough")
        ellipse = cv2.fitEllipse(poly_points)
        for n, i in enumerate(poly_points):
            x, y = i[0]
            plot_arg = ((x, y), 20, (255, 255, 255))
            plot_kwarg = {"lineType": 10}
            plot = ("circle", plot_arg, plot_kwarg)
            plots.append(plot)
            plot_arg = ((x, y), 5, (255, 255, 255),-1)
            plot_kwarg = {"lineType": 10}
            plot = ("circle", plot_arg, plot_kwarg)
            plots.append(plot)
        return ellipse, plots


# class PickOctagon(object):
#     def __init__(self):
#         super(PickOctagon, self).__init__()
#
#     def angleRatio(self, A, B, C):
#         """"baike baidu yuxiandingli
#         A-c-B-a-C-b JIAO A"""
#         c = np.sqrt(((A[0][0] - B[0][0]) ** 2 + (A[0][1] - B[0][1]) ** 2))
#         a = np.sqrt(((C[0][0] - B[0][0]) ** 2 + (C[0][1] - B[0][1]) ** 2))
#         b = np.sqrt(((A[0][0] - C[0][0]) ** 2 + (A[0][1] - C[0][1]) ** 2))
#         dif = (b * b + c * c - a * a)
#         diff = (2 * b * c)
#         if diff == 0:
#             return 1
#         alpha = dif / diff
#         return alpha
#
#     def horizonalRatio(self, A, B):
#         C = [[B[0][0], A[0][1]]]
#         return self.angleRatio(A, B, C)
#
#     def _getLongAxit(self, points):
#         lenPoints = points.shape[0]
#         # print 'lens is ', lenPoints
#         pointsContain = []
#         for i in range(0, lenPoints):
#             points2top = []
#             for j in range(0, lenPoints):
#                 _ = np.linalg.norm(points[i] - points[j])
#                 horiAngl = self.horizonalRatio(points[i], points[j])
#                 alist = (_, points[i], points[j], horiAngl)
#                 points2top.append(alist)
#             points2top.sort(key=itemgetter(0))
#             pointsContain.append(points2top[-1])
#             # print i, 'st len:', len(pointsContain), pointsContain[-1][3]
#         pointsContain.sort(key=itemgetter(0))
#         return pointsContain[-1]
#
#     def _getResult(self, longAxis, midPoint, getVerticalPoint, tempCounters):
#         result = {}
#         vPoint = getVerticalPoint[0]
#         result['longAxisLen'] = longAxis[0]
#         vPoint = np.array(vPoint)
#         midPoint = np.array([midPoint])
#         result['shortAxisLen'] = np.linalg.norm(vPoint - midPoint) * 2
#         result['corePoint'] = midPoint
#         if len(getVerticalPoint) < 3:
#             raise ValueError('not enough points')
#         point1 = np.array(getVerticalPoint[1])
#         point2 = np.array(getVerticalPoint[-1])
#         # pdb.set_trace()
#         # result['contour'] = np.array([longAxis[1], longAxis[2], vPoint, point1, point2])
#         result['contour'] = np.array(
#             [tempCounters[0], tempCounters[-1], point1, point2, longAxis[1], longAxis[2], vPoint])
#         # pdb.set_trace()
#         return result
#
#     def _getHalfList(self, list_):
#         len_ = len(list_)
#         if len_ > 3:
#             end = int(len_ / 2)
#             return list_[end:]
#         else:
#             return list_
#
#     # @timing
#     def run(self, img, blurindex=False):
#         """
#         :findContours->convexHull->sortMaxPointsDistance
#         ->calculateVerticalPoint->result: Long & short axis
#         :param img:
#         :return:
#         """
#         if blurindex:
#             # img = cv2.medianBlur(img, blurindex)
#             img = adaptive_filter_by_median(img)
#         contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#
#         logger.info('get contours len %s' % len(contours))
#
#         if len(contours) == 0:
#             raise ClassCoreError("contours = 0")
#         elif len(contours) == 1:
#             mergedpoints = contours[0]
#         else:
#             mergedpoints = np.concatenate(contours[1:])
#         points = cv2.convexHull(points=mergedpoints)
#         longAxis = self._getLongAxit(points)
#
#         result = {}
#         result['plots'] = []
#         # result['angle'] = longAxis[3]
#         x, y = tuple(longAxis[1][0].tolist()), tuple(longAxis[2][0].tolist())
#         result['longPlot'] = (x, y)
#         plot = (x, y, (25, 255, 0), 8)
#         result['plots'].append(('line', plot, {}))
#         midPoint = longAxis[1][0] + longAxis[2][0]
#         midPointf = midPoint / 2
#         midPoint = midPoint // 2
#
#         getVerticalPoint = mergedpoints.tolist()
#         getVerticalPoint.sort(key=lambda x: np.linalg.norm(x - midPoint))
#         tempCounters = (getVerticalPoint[0], getVerticalPoint[-1])
#         getVerticalPoint = self._getHalfList(getVerticalPoint)
#         getVerticalPoint.sort(key=lambda x: abs(self.angleRatio([midPoint], longAxis[1], x)))
#         result['angle'] = self.angleRatio([midPoint], longAxis[1], getVerticalPoint[-1])
#         x, y = tuple(midPoint.tolist()), tuple(getVerticalPoint[0][0])
#
#         result['shortPlot'] = (x, y)
#         plot = (x, y, (25, 255, 0), 8)
#         result['plots'].append(('line', plot, {}))
#
#         result.update(self._getResult(longAxis, midPoint, getVerticalPoint, tempCounters))
#
#         ellipse = cv2.fitEllipse(result['contour'])
#         result['ellipese'] = ellipse
#
#         # return result
