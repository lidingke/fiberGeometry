from setting.orderset import SETTING
SETTING('test','octagon')
from pattern.pickmethod import PickOctagon, PickCircle
from pattern.edge import ExtractEdge
import pytest
import cv2
from util.loadimg import edge2img, yieldImg
from pattern.getimg import GetImage
import numpy as np
from pattern.edge import EdgeFuncs
import pdb

@pytest.mark.parametrize(
    'dir_',(
        'IMG\\thr.png',
        'IMG\\500edge.bmp',
    ))
def test_ClassOctagon(dir_):
    img = GetImage().get(dir_)
    result = PickOctagon().run(img)
    # print 'get octagon', ['shortAxisLen'],result['longAxisLen']
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > result['shortAxisLen']
    ratio = result['shortAxisLen']/result['longAxisLen']
    assert ratio > 0.9
    print dir_, result['shortAxisLen'], result['longAxisLen'], ratio
    assert isinstance(result['corePoint'], np.ndarray)


@pytest.mark.parametrize(
    'dir_',(
        'tests\\data\\midcoreafteredge.bin',
        'tests\\data\\midcladafteredge.bin'
    ))
def test_pickcircle(dir_):
    img = np.fromfile(dir_, dtype="uint8")
    img.shape = (1944,2592)
    # img = ExtractEdge().run(img)
    # img.tofile("tests\\data\\midcoreafteredge.bin")
    # cv2.imshow("img", img[::4, ::4])
    # cv2.waitKey()
    result = PickCircle().run(img)
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > 0.5
    assert result['shortAxisLen'] > 0.5
    assert result['longAxisLen'] > result['shortAxisLen']
    ratio = result['shortAxisLen']/result['longAxisLen']
    print dir_, result['shortAxisLen'], result['longAxisLen'], ratio
    assert ratio > 0.9

    assert isinstance(result['corePoint'], np.ndarray)




"""GetImage().get()->ExtractEdge().run()
PickOctagon().pick()=>core/outer
=>ClassCore().run()/ClassOctagon().run()"""

if __name__ == '__main__':
    img = GetImage().get('IMG\\204001.BMP',colour="colour")
    print img.shape, 'get', type(img), img.dtype
    img = img[::,::,2].copy()
    # img = np.array(img,dtype='uint8')
    print img.shape ,'get', type(img), img.dtype
    cv2.circle(img, (1296,972), 100, 0, -1)
    # cv2.circle(img,(972, 1296),80,0)
    img = ExtractEdge().run(img)
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
