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

    def fitEllipses(self, contours, hierarchys):
        ampRatio = self.ampRatio
        coreList = []
        for x, contour in enumerate(contours):
            if contour.shape[0] > 5:
                area, circleIndex = self.CircleIndex.contourIn(contour)
                # print area, circleIndex
                ellipseResult = cv2.fitEllipse(contour)
                if area > 100 and circleIndex >0.7 and area < 1000000:
                    coreList.append((area, circleIndex, ellipseResult))
        # coreList.sort()
        coreList.sort(key= itemgetter(1))
        # if len(coreList)>10:
        #     perhapsCore = coreList[-10:]
        # else:
        #     perhapsCore = coreList
        # for _ in coreList:
        #     print _
        img = np.ones(self.img.shape, dtype='uint8') * 255
        # for core in coreList[-3:-1]:
        # img = self.img
        cv2.ellipse(img,coreList[-1][2],(0,0,0),3)
        core = coreList[-1][2]
        minRange = (core[1][1]+core[1][0])/2 + 50.0
        maxRange = (core[1][1]+core[1][0])/2 + 300.0
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
        img = self.fitEllipses(contours, hierarchys)
        return img
