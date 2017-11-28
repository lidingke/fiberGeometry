from collections import Iterable
import pytest
import cv2
from pattern.classify import classifyObject
from util.getimg import random_img
import logging


def assert_result(result, coreto=20, cladto=125, ranges=(2, 2, 5, 2, 2)):
    for i in ('corecore', 'plots', 'showResult'):
        assert i in result
    assert isinstance(result['plots'], Iterable)
    for p in result['plots']:
        a, b, c = p
        assert a in dir(cv2)
        assert isinstance(a, str)
        assert isinstance(b, tuple)
        assert isinstance(c, dict)
    co, core, clad, cor, clr = result["showResult"]
    rco, rcore, rclad, rcor, rclr = ranges
    assert co < rco
    assert coreto - rcore < core < coreto + rcore
    assert cladto - rclad < clad < cladto + rclad
    assert cor < rcor
    assert clr < rclr


def test_classify_capillary():
    img = random_img("IMG\\emptytuple\\eptlight0\\")
    classify = classifyObject("capillary")
    result = classify.find(img)
    print result
    assert_result(result, 0.5, 1)


@pytest.mark.parametrize(
    "dir_",
    ("IMG\\20125\\201709051\\",
     "IMG\\20125\\zl0906\\",)
)
def test_class_poly20125(dir_):
    logging.basicConfig(level=logging.INFO)
    # img = getImage("IMG\\midoctagon\\mid1.BMP")
    img = random_img(dir_)
    octs = classifyObject("20/130(oc)")
    result = octs.find(img)
    print result

    assert_result(result, 20, 125, ranges=(2, 2, 5, 3, 2))


# @pytest.mark.parametrize(
#     "dir_",
#     ("IMG\\10125\\dirtycore0907\\",
#      "IMG\\10125\\dirty\\",
#      "IMG\\10125\\diffraction\\")
# )
# def test_class_poly10125(dir_):
#     logging.basicConfig(level=logging.INFO)
#     img = random_img(dir_)
#     octs = classifyObject("10/130(oc)")
#     result = octs.find(img)
#     print result
#
#     assert_result(result, 10, 125, ranges=(3, 3, 10, 2, 2))


def test_class_thin():
    img = random_img("IMG\\200210\\nomid\\")
    big = classifyObject("200/220")
    result = big.find(img)
    print result
    assert_result(result, 200, 220)

def test_class_doublecircle():
    big = classifyObject("G652")
    img = random_img("IMG\\G652\\mid\\")
    result = big.find(img,amp_ratio=0.0792393)
    assert_result(result, 10, 125)
#
# @pytest.mark.testpy
# def test_mark():
#     print "get in test mark"


if __name__ == '__main__':
    d = "IMG\\20400\\0913\\"
    logging.basicConfig(level=logging.INFO)
    img = random_img(d)
    octs = classifyObject("20/400")
    result = octs.find(img)
    print result["showResult"]

    # test_class_poly10125("IMG\\10125\\dirty\\")
    # assert_result(result, 10, 125, ranges=(3, 3, 10, 2, 2))
