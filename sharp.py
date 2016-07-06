#!/usr/bin/python
from __future__ import division
import cv2
import numpy as np
import pdb
import time
import matplotlib.pyplot as plt


class IsSharp(object):
    """docstring for IsSharp"""
    def __init__(self,file):
        super(IsSharp, self).__init__()
        # self.arg = arg
        self.img = cv2.imread(file)


    def isSharp(self):
        time0 = time.time()
        img = self.img
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # pdb.set_trace()
        midsize = self._midSize(sizecoup = img.shape)
        img = img[midsize[0]:midsize[1],midsize[2]:midsize[3]]
        # img = cv2.GaussianBlur(img,(5, 5 ),0)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        erode = cv2.erode(img,kernel)
        dilate = cv2.dilate(img,kernel)
        img = cv2.absdiff(dilate,erode)
        # img = cv2.bitwise_not(img)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
        # img = img[:-1,:-1] - img[1:,1:]
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        # img = cv2.erode(img,kernel)
        sumGrad2 = (img**2).sum()
        normalizationSharp = sumGrad2*1000//img.size
        timeEnd = time.time()-time0
        print('work time ',timeEnd)
        print('result:',sumGrad2,'norm:',normalizationSharp//10.0)
        # cv2.imshow("adaptiveThreshold",img)
        # cv2.waitKey(0)
        return round(normalizationSharp/1000.0,2)

    def isSharpCanny(self):
        time0 = time.time()
        img = self.img
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # pdb.set_trace()
        midsize = self._midSize(sizecoup = img.shape)
        # pdb.set_trace()
        img = img[midsize[0]:midsize[1]:2,midsize[2]:midsize[3]:2]
        # img = cv2.GaussianBlur(img,(5, 5 ),0)

        img = cv2.Canny(img, 50, 150)
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        # erode = cv2.erode(img,kernel)
        # dilate = cv2.dilate(img,kernel)
        # img = cv2.absdiff(dilate,erode)


        # img = cv2.bitwise_not(img)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
        # img = img[:-1,:-1] - img[1:,1:]
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        # img = cv2.erode(img,kernel)
        sumGrad2 = (img**2).sum()
        normalizationSharp = sumGrad2*1000//img.size
        timeEnd = time.time()-time0
        print('work time ',timeEnd)
        print('result:',sumGrad2,'norm:',normalizationSharp//10.0)
        # cv2.imshow("adaptiveThreshold",img)
        # cv2.waitKey(0)
        return round(normalizationSharp/1000.0,2)


    def _midSize(self,sizecoup = (100,100), rato = 0.4):
        # size0 = sizecoup[]
        x00 = int(sizecoup[0]*rato)
        x01 = int(sizecoup[0]*(1-rato))
        x10 = int(sizecoup[1]*(rato))
        x11 = int(sizecoup[1]*(1-rato))
        # pdb.set_trace()
        return (x00, x01, x10 ,x11)


import sys
import os
if __name__ == '__main__':
    filename ="word"
    xlist = []
    for file in os.listdir(filename):
        # find = IsSharp(filename+"\\"+file).isSharp()
        find = IsSharp(filename+"\\"+file).isSharpCanny()
        print(file,'::', find)
        xlist.append(find)
    plt.plot(range(len(xlist)),xlist)
    plt.show()
        # find
