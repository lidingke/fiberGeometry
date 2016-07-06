import cv2
import numpy as np
import pdb
import time
import matplotlib.pyplot as plt

class Plus(object):
    """docstring for Plus"""
    def __init__(self, file):
        super(Plus, self).__init__()
        self.file = file
        print 'file:',file
        self.img = cv2.imread(file)
        midsize = self._midSize(sizecoup = self.img.shape)
        self.img = self.img[midsize[0]:midsize[1]:2,midsize[2]:midsize[3]:2,:]
        self.origin = self.img.copy()

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
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # pdb.set_trace()
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        erode = cv2.erode(img,kernel)
        dilate = cv2.dilate(img,kernel)
        img = cv2.absdiff(dilate,erode)
        # img = cv2.Canny(img, 20, 100)
        img = cv2.bitwise_not(img)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        result = np.hstack((self.origin,img))
        return result

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

    def _midSize(self,sizecoup = (100,100), rato = 0):
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
    n = 0
    for file in os.listdir(filename)[3:-3]:
        # find = IsSharp(filename+"\\"+file).isSharp()
        jpg = Plus(filename+"\\"+file).method()
        dir_ = 'result\\'+str(n)+'.jpg'
        n = n+1
        print('dir_',dir_)
        cv2.imwrite(dir_,jpg)
        find = Plus(filename+"\\"+file).isSharpCanny()
        print(file,'::', find)
        xlist.append(find)
    plt.plot(range(len(xlist)),xlist)
    plt.show()
