from __future__ import division
from setting.orderset import SETTING
SETTING().keyUpdates("test", "octagon", "centerImg")
from pattern.pickmethod import PickOctagon
from pattern.edge import ExtractEdge
import cv2
from util.loadimg import edge2img, yieldImg
from pattern.getimg import GetImage, randomImg
import numpy as np
from SDK.mdpy import GetRawImgTest
from pattern.classify import G652Classify
from pattern.edge import EdgeFuncs
import pdb
import time
from random import choice

def test_repeat_G652():
    sets = SETTING()
    sets.updates('G652','test')
    print 'sets', sets
    resultgetcore = []
    resultgetclad = []
    for img in yieldImg("IMG\\G652\\"):
        result = G652Classify().find(img)
        core, clad = result['coreResult'], result['cladResult']
        print core['ellipese'], clad['ellipese']
        assert core['longAxisLen'] > 0.5
        assert core['shortAxisLen'] > 0.5
        assert core['longAxisLen'] > core['shortAxisLen']
        ratio = core['shortAxisLen'] / core['longAxisLen']
        assert ratio > 0.9
        _1, _2 = core['corePoint'][0].tolist()
        radius = core['longAxisLen'] + core['shortAxisLen'] / 2
        print  _1, _2, radius
        resultgetcore.append([_1, _2, radius])

        print clad['ellipese'], clad['ellipese']
        assert clad['longAxisLen'] > 0.5
        assert clad['shortAxisLen'] > 0.5
        assert clad['longAxisLen'] > clad['shortAxisLen']
        ratio = clad['shortAxisLen'] / clad['longAxisLen']
        assert ratio > 0.9
        _1, _2 = clad['corePoint'][0].tolist()
        radius = clad['longAxisLen'] + clad['shortAxisLen'] / 2
        print  _1, _2, radius
        resultgetclad.append([_1, _2, radius])

    resultarray = np.array(resultgetcore)
    # print resultarray
    std  = np.std(resultarray, axis= 0 )
    x, y, z = std
    print 'std', x, y, z
    assert z < 0.5

    resultarray = np.array(resultgetclad)
    # print resultarray
    std  = np.std(resultarray, axis= 0 )
    x, y, z = std
    print 'std', x, y, z
    assert z < 1.5

def test_repeat_octagon():
    sets = SETTING()
    resultget = []
    for img in yieldImg("IMG\\octagon\\500s\\"):
        img = ExtractEdge().run(img)
        img = cv2.medianBlur(img, 11)
        result = PickOctagon().run(img)
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