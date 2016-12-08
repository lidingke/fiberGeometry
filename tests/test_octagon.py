from pattern.octagon import ClassOctagon
import pytest
from pattern.getimg import GetImage
import numpy as np


def test_ClassOctagon():
    co = ClassOctagon()
    imgObject = GetImage()
    img = imgObject.get('IMG\\thr.png')
    result = co.run(img)
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > result['shortAxisLen']
    assert isinstance(result['corePoint'], np.ndarray)


