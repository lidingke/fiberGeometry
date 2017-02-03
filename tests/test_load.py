from setting.orderset import SETTING
SETTING().keyUpdates("Default")
import cv2
from util.loadimg import sliceImg
from pattern.getimg import GetImage



def test_sliceImg():
    img = GetImage().get("IMG\\midoctagon\\mid1.BMP")
    if img.shape == (1944, 2592):
        print 'slice shape', img.shape
        corey, corex = SETTING()["corepoint"]
        minRange, maxRange = SETTING()["coreRange"]
        img = sliceImg(img, (corex, corey), maxRange)
        print 'slice shape', img.shape
        assert img.shape == (160, 160)

    img = GetImage().get("IMG\\midoctagon\\mid1.BMP","color")
    if img.shape == (1944, 2592, 3):
        print 'slice shape', img.shape
        corey, corex = SETTING()["corepoint"]
        minRange, maxRange = SETTING()["coreRange"]
        img = sliceImg(img, (corex, corey), maxRange)
        print 'slice shape', img.shape
        assert img.shape == (124, 124, 3)
