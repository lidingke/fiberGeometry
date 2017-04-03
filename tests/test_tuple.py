from pattern.getimg import getImage, randomImg
from pattern.sizefilter import inner_fill, outer_fill
import numpy as np
import cv2
from pattern.classify import Capillary
from setting.orderset import SETTING


def test_fill_mid():
    SETTING().keyUpdates("capillary", "test")
    img = randomImg("IMG\\emptytuple\\eptlight0\\")
    coreimg = img[::, ::, 0].copy()
    coreimg = inner_fill(coreimg, radius=100)

    cladimg = img[::, ::, 1].copy()
    cladimg = outer_fill(cladimg, radius=100)
    # cv2.imshow("filled",img[::4,::4])
    # cv2.waitKey()

def test_classify_tuple():
    SETTING().keyUpdates("capillary", "test")
    img = randomImg("IMG\\emptytuple\\eptlight0\\")
    # cv2.imshow("filled",img[::4,::4])
    # cv2.waitKey()
    classify = Capillary()
    result = classify.find(img)
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
