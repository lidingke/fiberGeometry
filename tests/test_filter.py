from pattern.coverimg import inner_fill_auto_value, outer_fill, sliceImg
from util.getimg import randomImg, GetImage
from setting.parameter import SETTING
from util.load import WriteReadJson
from util.filter import MedianFilter, MedianLimitFilter, AvgResult
import numpy as np

from pattern.coverimg import sliceImg


def test_sliceImg():
    SETTING().update_by_key("Default")
    img = GetImage().get("IMG\\midoctagon\\mid1.BMP", "gray")
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
        assert img.shape == (160, 160, 3)


def test_MedianFilter():
    jsobject = WriteReadJson("tests\\data\\light.json").load()
    medianget = MedianFilter(maxlen=5)
    result = []
    for x, y  in jsobject:
        medianget.append(x)
        print x,y,medianget.get()
        result.append((x,y,medianget.get()))
    npresult = np.array(result)
    assert npresult[::,0].std() > npresult[::,2].std()

def test_MedianLimitFilter():
    jsobject = WriteReadJson("tests\\data\\light.json").load()
    medianget = MedianLimitFilter(maxlen=5)
    result = []
    for x, y  in jsobject:
        # medianget.append(x)
        get = medianget.run(x)
        print x,y,get
        result.append((x,y,get))
    npresult = np.array(result)
    assert npresult[::,0].std() > npresult[::,2].std()


def test_avgresult():
    get = [[1,2,3],[2,3,4],[4,3,5],[7,6,2],[3,6,1]]
    result = AvgResult(get)
    print result
    assert [3.0,4.0,3.0] == result

def test_fill_mid():
    # SETTING().update_by_key("capillary")
    img = randomImg("IMG\\emptytuple\\eptlight0\\")
    coreimg = img[::, ::, 0].copy()
    coreimg = inner_fill_auto_value(coreimg, radius=100)

    cladimg = img[::, ::, 1].copy()
    cladimg = outer_fill(cladimg, radius=100)
    # cv2.imshow("filled",img[::4,::4])
