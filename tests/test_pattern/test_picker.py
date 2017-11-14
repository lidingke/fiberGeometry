from collections import Iterable

from setting.parameter import SETTING

from pattern.picker import  PickCircle, PickHullCircle, PickPoly
from pattern.edge import ExtractEdge
import pytest
import cv2
# from util.loadimg import yieldImg
from util.getimg import GetImage, yieldImg
import numpy as np


def assert_result(result):
    need_keys = ("ellipese", 'longAxisLen', 'shortAxisLen', 'plots')
    for k in need_keys:
        assert k in result.keys()
    assert isinstance(result['plots'], Iterable)
    for p in result['plots']:
        a, b, c = p
        assert a in dir(cv2)
        assert isinstance(a, str)
        assert isinstance(b, tuple)
        assert isinstance(c, dict)
    core, axis, angle = result['ellipese']
    x, y = core
    short, long = axis
    assert short < long
    for i in (x, y, short, long):
        assert i > 0
    assert (long - short) * 100 / long < 2


def test_circle():
    img = np.load("tests\\data\\pickers\\circlepicker.npy")
    result = PickCircle().run(img, 11)
    assert_result(result)
    # pass


def test_hullcircle():
    img = np.load("tests\\data\\pickers\\hullcirclepicker.npy")
    result = PickHullCircle().run(img, 11)
    assert_result(result)


def test_polycircle():
    img = np.load("tests\\data\\pickers\\hullcirclepicker.npy")
    result = PickPoly(8).run(img, 11)
    assert_result(result)


# @pytest.mark.parametrize(
#     'dir_', (
#             'IMG\\midoctagon\\mid1.bmp',
#     ))



"""GetImage().get()->ExtractEdge().run()
PickOctagon().pick()=>core/outer
=>ClassCore().run()/ClassOctagon().run()"""

if __name__ == '__main__':
    img = GetImage().get('IMG\\204001.BMP', colour="colour")
    print img.shape, 'get', type(img), img.dtype
    img = img[::, ::, 2].copy()
    # img = np.array(img,dtype='uint8')
    print img.shape, 'get', type(img), img.dtype
    cv2.circle(img, (1296, 972), 100, 0, -1)
    # cv2.circle(img,(972, 1296),80,0)
    img = ExtractEdge().directThr(img)
    # cv2.imshow("img", img[::4,::4])
    # cv2.waitKey(0)
    img.tofile("tests\\data\\midcladafteredge.bin")

    # img = cv2.medianBlur(img, 11)
    # cv2.imshow("img", img[::2,::2])
    # cv2.waitKey(0)
    # result = PickOctagon().run(img)
    # cv2.imshow("result", result['plot'][::2, ::2])
    # print result
    # cv2.waitKey(0)
    # dir_="tests\\data\\midcoreafteredge.bin"
    # test_pickcircle(dir_)
