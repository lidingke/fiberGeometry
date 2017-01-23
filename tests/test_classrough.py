from  setting.orderset import SETTING
SETTING("test")
from util.loadimg import yieldImg
from pattern.classify import Big20400Classify
import cv2
import numpy as np

def test_class_rough():
    big = Big20400Classify()
    for img in yieldImg("IMG\\sizeCore\\"):
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        print img.shape
        core, clad = big.find(img)
        print core['ellipese'], clad['ellipese']
        cv2.imshow("core", core['plot'])
        cv2.imshow("clad", clad['plot'][::4,::4])
        cv2.waitKey()



if __name__ == "__main__":
    test_class_rough()