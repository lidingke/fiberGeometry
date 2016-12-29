import cv2
import numpy as np
from .classify import MetaClassify
from operator import itemgetter
import pdb
import pytest


class PickOctagon(MetaClassify):

    def __init__(self):
        super(PickOctagon, self).__init__()

        self.result = {}
        self.ampRatio = 0.0835#0.08653

    def _filter(self, contours, hierarchys):
        ampRatio = self.ampRatio
        coreList = []
        for x, contour in enumerate(contours):
            if contour.shape[0] > 5:
                area, circleIndex = self.CircleIndex.contourIn(contour)

                ellipseResult = cv2.fitEllipse(contour)
                # print area, circleIndex, ellipseResult
                if area > 100 and circleIndex >0.5:
                    # and area < 1000000:
                    coreList.append((area, circleIndex, ellipseResult))

        coreList.sort(key= itemgetter(1))
        # pdb.set_trace()
        # cv2.ellipse(img,coreList[-1][2],(0,0,0),3)
        core = coreList[-1][2]
        octagonImg = self._getOctagon(core, contours)
        coreImg = self._getCore(core, contours)

        return (coreImg, octagonImg)

    def _getOctagon(self, core, contours):
        img = np.ones(self.img.shape, dtype='uint8') * 255
        minRange = (core[1][1]+core[1][0])/2 + 50.0
        maxRange = (core[1][1]+core[1][0])/2 + 300.0
        # corePoint = {'core'}
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), -1)
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), -1)
        contourImg = np.ones(self.img.shape, dtype='uint8') * 255
        cv2.drawContours(contourImg, contours, -1, (0,0,0))
        img = cv2.bitwise_or(img,contourImg)
        return img

    def _getCore(self, core, contours):
        img = np.ones(self.img.shape, dtype='uint8') * 255
        minRange = (core[1][1]+core[1][0])/2*0.5
        maxRange = (core[1][1]+core[1][0])/2*1.2
        # corePoint = {'core'}
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), -1)
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), -1)
        contourImg = np.ones(self.img.shape, dtype='uint8') * 255
        cv2.drawContours(contourImg, contours, -1, (0,0,0))
        img = cv2.bitwise_or(img,contourImg)
        return img


    def pick(self, img):
        self.img = img
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        core, octagon = self._filter(contours, hierarchys)
        return (core, octagon)

    def _findCore(self, img):
        img = cv2.medianBlur(img, 15)
        # cv2.imshow("md", img[::4,::4])
        # cv2.waitKey()
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        ellipses = []
        for contour in contours:
            area, circleIndex = self.CircleIndex.contourIn(contour)
            if len(contour) < 5 or area <50 or circleIndex < 0.5 or area > 2000000:
                continue
            ellipse= cv2.fitEllipse(contour)
            if ellipse[2] == 0.0:
                continue
            ellipses.append((area, circleIndex, ellipse))
        ellipses.sort(key=itemgetter(1))
        for e in ellipses:
            print e
        if len(ellipses) == 0:
            raise CanNotFindCore()
        core = ellipses[-1][1]
        return core


class CanNotFindCore(Exception):
    
    def __init__(self):
        super(CanNotFindCore, self).__init__()
