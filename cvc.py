#!/usr/bin/python
import cv2
import numpy as np
import pdb

class findCircles(object):
    """docstring for findCircles"""
    def __init__(self, file):
        super(findCircles, self).__init__()
        self.file = file
        print 'file:',file
        self.img = cv2.imread(file)
        # cv2.imshow('img',self.img)
        # cv2.waitKey(0)
        self.origin = self.img.copy()
        # self.method()

    def run(self):
        try:
            img = self.method()
            # img = self.noGradMethod(self.img)
            cv2.imshow(str(self.file),img)
            cv2.waitKey(0)
        except Exception as e:
            print(e)


    def method(self):
        img = self.img
        img = self._edgeDetectDiff(img)
        # img = self._edgeDetectCanny(img)
        # cv2.imshow("adaptiveThreshold",img)
        # cv2.waitKey(0)
        # img = self._circleFind(img)
        img = self._circleFindContours(img)

        return img


    def _edgeDetectCanny(self,img):
        # img = cv2.GaussianBlur(img,(3, 3 ),0)
        img = cv2.Canny(img, 10, 200)
        return img

    def _edgeDetectDiff(self,img):
        # img = cv2.medianBlur(img,3)
        img  = cv2.pyrMeanShiftFiltering(img,5,5,1)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # img = cv2.GaussianBlur(img,(3, 3 ),0)
        # kernel = np.ones((10,10),np.uint8)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        # pdb.set_trace()
        # erosion = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
        # cv2.imshow('show',erosion)
        # cv2.waitKey(0)
        # img = erosion
        # arrimg = cv2.cv.fromarray(img)
        erode = cv2.erode(img,kernel)
        # dilate = cv2.dilate(img,kernel)
        # img = np.array(arrimg)
        # img = cv2.absdiff(dilate,erode)
        img = cv2.absdiff(img,erode)
        img = cv2.bitwise_not(img)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)

        # img = cv2.equalizeHist(img)
        # cv2.imshow("equalizeHist",img)
        # cv2.waitKey(0)
        # img = cv2.dilate(img,kernel)
        # img = cv2.medianBlur(img,3)
        # cts,hy = cv2.findContours(img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE, offset=(0, 0))
        # pdb.set_trace()
        # print('ctshy',cts,hy)
        # cv2.imshow(,contours)
        return img

    def _circleFindContours(self,img):
        contours, hierarchys = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        result = np.ones(img.shape)*255
        # for x in contours:
        for x in contours:
            pdb.set_trace()
            area = cv2.contourArea(x)
            cvMom = cv2.moments(x)
            if cvMom['m00'] != 0.0:
                cvMomXY = (cvMom['m10']/cvMom['m00'],cvMom['m01']/cvMom['m00'])
                circleIndex = self._isCircle(area, cvMomXY, x)

                if circleIndex > 0.8:
                    print "area" , area , "circleIndex:", circleIndex,"mom:", cvMomXY
                    cv2.drawContours(result, x, -1, (0,0,255),maxLevel = 2)
        cv2.imshow("img", result)
        cv2.waitKey(0)

    def _circleFind(self,img):
        para = 150
        circleMap = cv2.HoughCircles(image = img,
            method = cv2.cv.CV_HOUGH_GRADIENT,
            dp = 1,
            minDist = len(img)/8,#len(img)/8,
            param1 = 20,
            param2 = 10,
            minRadius = 0,
            maxRadius = 100)
        c0map = []
        if circleMap is None:
            raise Exception('circle not find')
        for c0 in circleMap[0]:
            c01sum = []
            for c1 in circleMap[0]:
                diff = abs(c0[1]-c1[1])+abs(c0[0]-c1[0])
                c01sum.append(diff)
            c0map.append((sum(c01sum)/len(c01sum), c0[0], c0[1], c0[2]))
            # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            cv2.circle(img,(c0[0],c0[1]), c0[2], (255 ,0,0), 2)
        # pdb.set_trace()
        # if len(c0map) >10:
        #     c0map = c0map[4:-4]
        c0map.sort()
        circle = c0map[0]
        cv2.circle(img,(circle[1],circle[2]), circle[3], (0,255,0), 10)
        cv2.circle(self.origin,(circle[1],circle[2]), circle[3], (0,0,255), 4)
        cv2.imwrite('result.jpg',self.origin)
        return img


    def noGradMethod(self,img):
        # img = cv2.medianBlur(img,3)
        # img  = cv2.pyrMeanShiftFiltering(img,5,5,1)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # img = cv2.GaussianBlur(img,(3, 3 ),0)
        # kernel = np.ones((10,10),np.uint8)
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        # pdb.set_trace()
        # erosion = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
        # cv2.imshow('show',erosion)
        # cv2.waitKey(0)
        # img = erosion
        # arrimg = cv2.cv.fromarray(img)
        # erode = cv2.erode(img,kernel)
        # dilate = cv2.dilate(img,kernel)
        # img = np.array(arrimg)
        # img = cv2.absdiff(dilate,erode)
        # img = cv2.bitwise_not(img)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
        cv2.imshow("adaptiveThreshold",img)
        cv2.imwrite('threshold.jpg',img)
        cv2.waitKey(0)
        # img = cv2.equalizeHist(img)
        # cv2.imshow("equalizeHist",img)
        # cv2.waitKey(0)
        # img = cv2.dilate(img,kernel)
        # img = cv2.medianBlur(img,3)
        # cts,hy = cv2.findContours(img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE, offset=(0, 0))
        # pdb.set_trace()
        # print('ctshy',cts,hy)
        # cv2.imshow(,contours)
        para = 150
        circleMap = cv2.HoughCircles(image = img,
            method = cv2.cv.CV_HOUGH_GRADIENT,
            dp = 1,
            minDist = len(img)/8,#len(img)/8,
            param1 = 20,
            param2 = 10,
            minRadius = 0,
            maxRadius = 100)
        c0map = []
        if circleMap is None:
            raise Exception('circle not find')
        for c0 in circleMap[0]:
            c01sum = []
            for c1 in circleMap[0]:
                diff = abs(c0[1]-c1[1])+abs(c0[0]-c1[0])
                c01sum.append(diff)
            c0map.append((sum(c01sum)/len(c01sum), c0[0], c0[1], c0[2]))
            # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            cv2.circle(img,(c0[0],c0[1]), c0[2], (255 ,0,0), 2)
        # pdb.set_trace()
        # if len(c0map) >10:
        #     c0map = c0map[4:-4]
        c0map.sort()
        circle = c0map[0]
        cv2.circle(img,(circle[1],circle[2]), circle[3], (0,255,0), 10)
        cv2.circle(self.origin,(circle[1],circle[2]), circle[3], (0,0,255), 4)
        cv2.imwrite('result.jpg',self.origin)
        return img


    def _isCircle(self, area, center, contours):
        # pdb.set_trace()
        forMaxNumber = []
        for x in contours:
            absLen = ((center[0]-x[0][0])**2 + (center[1]-x[0][1])**2)**0.5
            forMaxNumber.append(absLen)
        forMaxNumber.sort()
        maxLen = forMaxNumber[-1]
        if maxLen == 0:
            return 0
        return area/(maxLen**2*3.14)

import sys
import os
if __name__ == '__main__':
    for file in os.listdir('img'):
        find = findCircles("img\\"+file)
        find.run()

