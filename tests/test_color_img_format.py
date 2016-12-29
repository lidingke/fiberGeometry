import pdb
import numpy as np
import cv2
from SDK.mdpy import GetRawImgTest as GetRawImg


def test_origin_imgColor():
    bayer2RGB = GetRawImg().bayer2RGB
    img = np.fromfile("tests\\data\\imgblue.bin", dtype="uint8")
    img.shape = (1944, 2592)
    img = bayer2RGB(img)
    r, g, b = img[:, :, 0].sum(), img[:, :, 1].sum(), img[:, :, 2].sum()
    assert b > g and b > r
    img = np.fromfile("tests\\data\\imggreen.bin", dtype="uint8")
    img.shape = (1944, 2592)
    img = bayer2RGB(img)
    r, g, b = img[:, :, 0].sum(), img[:, :, 1].sum(), img[:, :, 2].sum()
    assert g > r and g > b
    img = np.fromfile("tests\\data\\imgred.bin", dtype="uint8")
    img.shape = (1944, 2592)
    img = bayer2RGB(img)
    r, g, b = img[:, :, 0].sum(), img[:, :, 1].sum(), img[:, :, 2].sum()
    assert r > g and r > b


