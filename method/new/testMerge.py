import pdb
import cv2

import numpy as np
from method.toolkit import DynamicPick
from method.toolkit import IsCircle, cv2CircleIndex, XlsWrite, Cv2ImShow

def mer():
    circleIndexGet = cv2CircleIndex()
    dpk = DynamicPick()
    contours = dpk.load("IMG\\pick\\2con.pickle")
    ampRatio = 0.08895
    cladingList, coreList = [], []
    for x, contour in enumerate(contours):
        if contour.shape[0] > 5:
            area, circleIndex = circleIndexGet.contourIn(contour)
            ellipseResult = cv2.fitEllipse(contour)
            if area > 50 :
                print 'ellipseCounter Result ', area, circleIndex, ellipseResult[1][0] * ampRatio, ellipseResult[1][1]*ampRatio
                radiusTemp = (ellipseResult[1][0] + ellipseResult[1][1]) * ampRatio / 2
                if radiusTemp > 3 and radiusTemp < 7 and circleIndex > 0.3:
                    print 'core: ', ellipseResult[1][0]*ampRatio, ellipseResult[1][1]*ampRatio, circleIndex
                    coreList.append((area, circleIndex, ellipseResult, contour))
                elif radiusTemp > 58 and radiusTemp < 65:
                    print 'clad: ', area,ellipseResult[1][0], ellipseResult[1][1]
                    cladingList.append((area, circleIndex, ellipseResult, contour))
    pdb.set_trace()
    if len(coreList) == 2:
        allContour = np.concatenate((coreList[0][3], coreList[1][3]))
        ellipseResult = cv2.fitEllipse(allContour)
        print 'ellipseResult', ellipseResult
        print '2 merged core: ', ellipseResult[1][0]*ampRatio, ellipseResult[1][1]*ampRatio
