from setting.orderset import SETTING
SETTING('test','octagon')
from pattern.sharp import IsSharp
import numpy as np
import pytest


def test_doSharpRange():
    imgs = []
    for i in range(0,3):
        dir_ = "tests\\data\\imgforsharp{}.bin".format(i)
        img = np.fromfile(dir_,dtype= "uint8")
        img.shape = (1944,2592)
        imgs.append(img)
    sharp = IsSharp()
    for img in imgs:
        img = sharp._doSharpRange(img)
        assert isinstance(img, np.ndarray)
        assert len(img.shape) == 2

    result = sharp.isSharpDiff(imgs)
    assert isinstance(result, int) or isinstance(result, np.int64)


if __name__ == "__main__":
    test_doSharpRange()

