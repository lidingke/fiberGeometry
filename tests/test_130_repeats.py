#coding:utf-8
import logging
import os

import pytest

from pattern.classify import classifyObject
from util.getimg import random_img, get_img


@pytest.mark.parametrize(
    "dir_",
    ("IMG\\130-test\\img1\\",)
)
def test_class_poly20125(dir_):
    u"""输出130文件夹下图片保存的光纤的重复性"""
    logging.basicConfig(level=logging.ERROR)
    # img = getImage("IMG\\midoctagon\\mid1.BMP")
    dirs = os.listdir(dir_)
    for d in dirs[::-1]:
        img = get_img(os.path.join(dir_,d))
        octs = classifyObject("G652")
        result = octs.find(img)
        print result["showResult"]