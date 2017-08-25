
from setting.orderset import SETTING
from tests.test_pattern import assert_result

SETTING().keyUpdates('G652','test')
import pdb
import numpy as np
import cv2
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
from pattern.classify import G652Classify
from pattern.sharp import IsSharp
from SDK.mdpy import GetRawImg

def test_class_G652():
    SETTING().keyUpdates('G652', 'test')
    print 'set', SETTING()
    big = G652Classify()
    img = GetImage().get("IMG\\G652\\mid\\g652mid.BMP", colour = 'colour')
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    print img.shape
    result = big.find(img)
    assert_result(result)









