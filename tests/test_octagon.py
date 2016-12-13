from pattern.octagon import ClassOctagon
from pattern.pickoctagon import PickOctagon
from pattern.edge import ExtractEdge
import pytest
import cv2
from pattern.getimg import GetImage
import numpy as np
import pdb


def test_ClassOctagon():
    co = ClassOctagon()
    imgObject = GetImage()
    img = imgObject.get('IMG\\thr.png')
    result = co.run(img)
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > result['shortAxisLen']
    ratio = result['shortAxisLen']/result['longAxisLen']
    assert ratio >0.9
    print result['shortAxisLen'], result['longAxisLen'], ratio
    assert isinstance(result['corePoint'], np.ndarray)



if __name__ == '__main__':

    img = GetImage().get('IMG\\IMG00001.BMP')
    img = ExtractEdge().run(img)
    print 'dtype', img.dtype
    cv2.imshow("edge", img[::2, ::2])
    cv2.waitKey(0)
    img = PickOctagon().pick(img)
    cv2.imshow("picked", img[::2, ::2])
    cv2.waitKey(0)
    # img = GetImage().get('IMG\\thr.png')
    result = ClassOctagon().run(img)

    cv2.imshow("result", result['plot'][::2,::2])
    cv2.waitKey(0)

