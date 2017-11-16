from __future__ import division
import cv2
# from util.loadimg import  yieldImg
from util.getimg import GetImage, randomImg, yieldImg
import numpy as np
from SDK.mdpy import GetRawImgTest
from pattern.classify import classifyObject
import logging
logging.basicConfig(level=logging.ERROR)




def test_repeat_G652():
    resultget = []
    for img in yieldImg("IMG\\G652\\mid\\"):
        g = classifyObject('G652')
        result = g.find(img)
        show = result['showResult']
        print show
        resultget.append(show)
    resultarray = np.array(resultget)
    std  = np.std(resultarray, axis= 0 )
    print 'std', std
    for i,z in enumerate(std):
        print i,z
        assert z < 1


def test_repeat_octagon():
    resultget = []
    for img in yieldImg("IMG\\20125\\20170904\\"):
        octc = classifyObject('20/130(oc)')
        result = octc.find(img)
        show = result['showResult']
        print show
        resultget.append(show)

    resultarray = np.array(resultget)
    std  = np.std(resultarray, axis= 0 )
    print 'std', std
    for i,z in enumerate(std):
        print i,z
        assert z < 1




def test_GetRawImgTest():
    # print std * 0.088
    getraw = GetRawImgTest()
    dget = getraw.get()
    isinstance(dget, np.ndarray)
        # print dget.shape, type(dget), dget.sum()


if __name__ == '__main__':
    test_repeat_octagon()