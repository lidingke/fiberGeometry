import cv2
import numpy as np
from pattern.meta import CV2MethodSet
from method.toolkit import timing

class MetaClassify(CV2MethodSet):
    """docstring for MetaClassify"""
    def __init__(self, ):
        super(MetaClassify, self).__init__()
        # self.arg = arg
        self.result = {}

    # @timing
    def find(self, img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # pdb.set_trace()
        self._filter(contours, hierarchys)
        return self.result

    def _filter(self, contours, hierarchys):
        pass


class G652Classify(MetaClassify):
    """docstring for G652Classify"""
    def __init__(self, ):
        super(G652Classify, self).__init__()
        self.result = {}
        self.ampRatio = 0.0835#0.08653

    def _filter(self, contours, hierarchys):
        ampRatio = self.ampRatio
        cladingList, coreList = [], []
        for x, contour in enumerate(contours):
            if contour.shape[0] > 5:
                area, circleIndex = self.CircleIndex.contourIn(contour)
                ellipseResult = cv2.fitEllipse(contour)
                if area > 50 :
                    # print 'ellipseCounter Result ', area, circleIndex, ellipseResult[1][0] * ampRatio, ellipseResult[1][1]*ampRatio
                    radiusTemp = (ellipseResult[1][0] + ellipseResult[1][1]) * ampRatio / 2
                    if radiusTemp > 3 and radiusTemp < 7 and circleIndex > 0.3:
                        # print 'core: ', ellipseResult[1][0]*ampRatio, ellipseResult[1][1]*ampRatio, circleIndex
                        coreList.append((area, circleIndex, ellipseResult, contour))
                    elif radiusTemp > 55 and radiusTemp < 70:
                        # print 'clad: ', area,ellipseResult[1][0], ellipseResult[1][1]
                        cladingList.append((area, circleIndex, ellipseResult, contour))
        # pdb.set_trace()
        self._mergedEllipese(coreList, 'core')
        self._mergedEllipese(cladingList, 'clad')
        # self.getResult()

    def _mergedEllipese(self, lst, id_):
        ampRatio = self.ampRatio
        if len(lst) == 2:
            allContour = np.concatenate((lst[0][3], lst[1][3]))
            ellipseResult = cv2.fitEllipse(allContour)
            # print 'ellipseResult', ellipseResult
            print '2 ', id_, ellipseResult[1][0]*ampRatio, ellipseResult[1][1]*ampRatio
        elif len(lst) == 1:
            ellipseResult = lst[0][2]
            print '1 ', id_, ellipseResult[1][0]*ampRatio, ellipseResult[1][1]*ampRatio
        elif len(lst) == 0:
            ellipseResult = False
        else:
            lst.sort()
            allContour = np.concatenate((lst[0][3], lst[1][3]))
            ellipseResult = cv2.fitEllipse(allContour)
            print '2+ ', id_, ellipseResult[1][0]*ampRatio, ellipseResult[1][1]*ampRatio
        self.result[id_] = ellipseResult

    def getResult(self):
        coreResult = self.result.get('core', False)
        cladResult = self.result.get('clad', False)
        if coreResult and cladResult:
            coreCore, coreRadius, angle = coreResult
            cladCore, cladRadius, angle = cladResult
            concentricity = ((coreCore[0] - cladCore[0])**2
                             + (coreCore[1] - cladCore[1])**2 )**0.5
            concentricity = concentricity * self.ampRatio
            coreMidRadius = self.ampRatio * (coreRadius[0] + coreRadius[1])
            cladMidRadius = self.ampRatio * (cladRadius[0] + cladRadius[1])
            # cladMidRadius = (cladRadius[0] + cladRadius[1])
            coreRness = self.ampRatio * abs(coreRadius[0] - coreRadius[1])
            cladRness = self.ampRatio * abs(cladRadius[0] - cladRadius[1])
            # print "result ,%0.4f,%0.4f,%0.4f,%0.4f,%0.4f,"%(concentricity,
            #                                         coreMidRadius,
            #                                         cladMidRadius,
            #                                         coreRness,
            #                                         cladRness)
            return (concentricity,coreMidRadius,cladMidRadius,coreRness,cladRness)
        else:
            print 'error find core or clad'
            return ()