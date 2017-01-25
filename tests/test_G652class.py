
from setting.orderset import SETTING
SETTING('G652','test')
import pdb
import numpy as np
import cv2
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
from pattern.classify import G652Classify
from pattern.sharp import IsSharp
from SDK.mdpy import GetRawImg

def test_class_G652():
    print 'set', SETTING()
    big = G652Classify()
    img = GetImage().get("IMG\\G652\\g652mid.BMP", colour = 'colour')
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    print img.shape
    result = big.find(img)
    core, clad = result['coreResult'], result['cladResult']
    print core['ellipese'], clad['ellipese'], result['cladResult'].keys()
    assert core['longAxisLen'] > 0.5
    assert core['shortAxisLen'] > 0.5
    assert core['longAxisLen'] > core['shortAxisLen']
    ratio = core['shortAxisLen'] / core['longAxisLen']
    assert ratio > 0.9

    # cv2.imshow("clad", clad['plot'][::4,::4])
    # cv2.waitKey()
    assert clad['longAxisLen'] > 0.5
    assert clad['shortAxisLen'] > 0.5
    assert clad['longAxisLen'] > clad['shortAxisLen']
    ratio = clad['shortAxisLen'] / clad['longAxisLen']
    assert ratio > 0.9









