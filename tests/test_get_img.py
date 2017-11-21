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