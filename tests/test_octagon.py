from pattern.octagon import ClassOctagon
from pattern.octagon import ClassCore
from pattern.pickoctagon import PickOctagon
from pattern.edge import ExtractEdge
import pytest
import cv2
from pattern.getimg import GetImage
import numpy as np
import pdb

def test_ClassOctagon():
    img = GetImage().get('IMG\\thr.png')
    result = ClassOctagon().run(img)
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > result['shortAxisLen']
    ratio = result['shortAxisLen']/result['longAxisLen']
    assert ratio > 0.9
    # print result['shortAxisLen'], result['longAxisLen'], ratio
    assert isinstance(result['corePoint'], np.ndarray)

@pytest.mark.parametrize(
    'dir_',(
        'IMG\\IMG00001.BMP',
        'IMG\\IMG00003.BMP',
    )
)
def test_ClassCore(dir_):
    img = GetImage().get(dir_)
    img = ExtractEdge().run(img)
    core, img = PickOctagon().pick(img)
    result = ClassCore().run(core)
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > result['shortAxisLen']
    ratio = result['shortAxisLen'] / result['longAxisLen']
    assert ratio > 0.9
    # print result['shortAxisLen'], result['longAxisLen'], ratio
    assert isinstance(result['corePoint'], np.ndarray)


if __name__ == '__main__':
    img = GetImage().get('IMG\\IMG00001.BMP')
    img = ExtractEdge().run(img)
    print 'dtype', img.dtype
    cv2.imshow("edge", img[::2, ::2])
    cv2.waitKey(0)
    core, img = PickOctagon().pick(img)
    cv2.imshow("picked", img[::2, ::2])
    cv2.waitKey(0)
    # img = GetImage().get('IMG\\thr.png')
    result = ClassOctagon().run(img)
    core = ClassCore().run(core)

    cv2.imshow("result", result['plot'][::2,::2])
    cv2.waitKey(0)

