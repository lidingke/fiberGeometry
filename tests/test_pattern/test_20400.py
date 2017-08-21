from  setting.orderset import SETTING
SETTING("test").keyUpdates('20400')
from util.loadimg import yieldImg, GetImage
from pattern.classify import Big20400Classify
import cv2
import numpy as np

def test_class_rough():
    SETTING("test").keyUpdates('20400')
    big = Big20400Classify()
    # for img in yieldImg("IMG\\20400\\"):
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    img = GetImage().get("IMG\\20400\\size1.bmp")
    print img.shape
    result = big.find(img)
    core, clad = result['coreResult'], result['cladResult']
    print core['ellipese'], clad['ellipese'], result['cladResult'].keys()
    assert core['longAxisLen'] > 0.5
    assert core['shortAxisLen'] > 0.5
    assert core['longAxisLen'] > core['shortAxisLen']
    ratio = core['shortAxisLen'] / core['longAxisLen']
    assert ratio > 0.9


if __name__ == "__main__":
    test_class_rough()