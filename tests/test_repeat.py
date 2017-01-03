from __future__ import division
from setting.orderset import SETTING
SETTING("test", "octagon", "centerImg")
from pattern.octagon import ClassOctagon
from pattern.edge import ExtractEdge
import cv2
from util.loadimg import edge2img, yieldImg
from pattern.getimg import GetImage, randomImg
import numpy as np
from SDK.mdpy import GetRawImgTest
from pattern.edge import EdgeFuncs
import pdb
import time
from random import choice


def test_repeat_octagon():
    sets = SETTING()
    resultget = []
    for img in yieldImg("IMG\\octagon\\500s\\"):
        img = ExtractEdge().run(img)
        img = cv2.medianBlur(img, 11)
        result = ClassOctagon().run(img)
        _1, _2 = result['corePoint'][0].tolist()
        radius = result['longAxisLen'] + result['shortAxisLen'] / 2
        print  _1, _2, radius
        resultget.append([_1, _2, radius])

    resultarray = np.array(resultget)
    # print resultarray
    std  = np.std(resultarray, axis= 0 )
    x, y, z = std * 0.088
    print 'std', x, y, z
    assert z < 0.5


def test_GetRawImgTest():
    # print std * 0.088
    getraw = GetRawImgTest()
    dget = getraw.get()
    isinstance(dget, np.ndarray)
        # print dget.shape, type(dget), dget.sum()


if __name__ == '__main__':
    test_repeat_octagon()