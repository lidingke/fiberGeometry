#coding:utf-8
import numpy as np
import pytest

from util.getimg import get_img_by_dir, random_img_by_file, list_img_by_file, yield_img_by_file


@pytest.mark.parametrize(
    "path",
    (
            "IMG\\midoc.BMP",
            "IMG/midoc.BMP",
            "IMG/204001.bmp"
    )
)
def test_get_img_by_dir_bmp(path):
    u"""unit test case for get_img_by_dir
    读取bmp图片的函数的单元测试"""
    img = get_img_by_dir(path)
    assert isinstance(img, np.ndarray)
    assert img.shape == (1944, 2592, 3)

    img = get_img_by_dir(path, 'gray')
    assert isinstance(img, np.ndarray)
    assert img.shape == (1944, 2592)


@pytest.mark.parametrize(
    "path",
    (
            "IMG\\thr.png",
    )
)
def test_get_img_by_dir_png(path):
    u"""unit test case for get_img_by_dir
    读取png图片的函数的单元测试"""
    img = get_img_by_dir(path)
    assert isinstance(img, np.ndarray)
    assert img.shape == (1080, 1920, 3)

@pytest.mark.parametrize(
    "path",
    (
            "IMG\\G652\\pk",
            "IMG/G652/pk",
            "IMG\\G652\\pk\\",
            "IMG/G652/pk/",
    )
)
def test_get_img_by_file_methods(path):
    u"""按文件夹读取函数的单元测试，
    这几个函数按文件夹读取，分别为随机返回一个函数，返回一个图片list，惰性返回单个图片"""
    img = random_img_by_file(path)
    assert isinstance(img, np.ndarray)
    assert img.shape == (1944, 2592, 3)
    imgs = list_img_by_file(path)
    for img in imgs[::4]:
        assert isinstance(img, np.ndarray)
        assert img.shape == (1944, 2592, 3)
    imgs = yield_img_by_file(path)

    for img in imgs:
        assert isinstance(img, np.ndarray)
        assert img.shape == (1944, 2592, 3)