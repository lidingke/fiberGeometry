from setting.orderset import SETTING
SETTING('test','octagon')
from pattern.octagon import ClassOctagon, ClassCore
from pattern.pickoctagon import PickOctagon
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
    result = ClassOctagon().run(img)
    # print 'get octagon', ['shortAxisLen'],result['longAxisLen']
    assert isinstance(result['plot'], np.ndarray)
    assert result['longAxisLen'] > result['shortAxisLen']
    ratio = result['shortAxisLen']/result['longAxisLen']
    assert ratio > 0.9
    print dir_, result['shortAxisLen'], result['longAxisLen'], ratio
    assert isinstance(result['corePoint'], np.ndarray)

# @pytest.mark.parametrize(
#     'dir_',(
#         'IMG\\IMG00001.BMP',
#         'IMG\\IMG00003.BMP',
#     ))
# def test_ClassCore(dir_):
#
#     img = GetImage().get(dir_)
#     img = ExtractEdge().run(img)
#     cv2.imshow('img', img[::4,::4])
#     cv2.waitKey()
    # core, img = PickOctagon().pick(img)
    # result = ClassCore().run(core)
    # assert isinstance(result['plot'], np.ndarray)
    # assert result['longAxisLen'] > result['shortAxisLen']
    # ratio = result['shortAxisLen'] / result['longAxisLen']
    # print 'len', result['shortAxisLen'] , result['longAxisLen']
    # assert ratio > 0.9
    # print result['shortAxisLen'], result['longAxisLen'], ratio
    # assert isinstance(result['corePoint'], np.ndarray)

def oldmain():
    sets = SETTING({"ampFactor": "20X", "cameraID": "MindVision500"})
    print sets
    # img = GetImage().get('IMG\\IMG00001.BMP')
    # img = GetImage().get('IMG\\octagon\\5001.BMP')
    # img = ExtractEdge().run(img)
    # print 'dtype', img.dtype
    # cv2.imshow("edge", img[::2, ::2])
    # cv2.waitKey(0)

    # img = edge2img("IMG\\octagon\\500s\\")
    # cv2.imshow("bitwise_not", img[::4, ::4])
    # cv2.waitKey(0)
    # cv2.imwrite("bitwise_not.bmp", img)
    # core, img = PickOctagon().pick(img)
    resultget = []
    for img in yieldImg("IMG\\octagon\\500s\\"):
        img = ExtractEdge().run(img)
        # img = EdgeFuncs().open(img, 10)
        # img = cv2.medianBlur(img, 11)
        result = ClassOctagon().run(img)
        _1, _2 = result['corePoint'][0].tolist()
        resultget.append([_1, _2, result['longAxisLen'],result['shortAxisLen']])
        # pdb.set_trace()

        # cv2.imshow("plot", result['plot'][::3, ::3])
        # cv2.waitKey(0)
        # print result
    resultarray = np.array(resultget)
    print resultarray
    std  = np.std(resultarray, axis= 0 )
    print std * 0.088
    # for res in resultget:
    #     print 'result get', res


    # core, img = PickOctagon().pick(img)
    # cv2.imshow("picked", img[::2, ::2])
    # cv2.waitKey(0)
    # # img = GetImage().get('IMG\\thr.png')
    # result = ClassOctagon().run(img)
    # core = ClassCore().run(core)
    # cv2.imshow("result", result['plot'][::2,::2])
    # cv2.waitKey(0)


"""GetImage().get()->ExtractEdge().run()
PickOctagon().pick()=>core/outer
=>ClassCore().run()/ClassOctagon().run()"""

if __name__ == '__main__':
    img = GetImage().get('IMG\\octagon\\500oc.BMP')
    img = ExtractEdge().run(img)
    cv2.imshow("img", img[::2,::2])
    cv2.waitKey(0)
    img = cv2.medianBlur(img, 11)
    cv2.imshow("img", img[::2,::2])
    cv2.waitKey(0)
    result = ClassOctagon().run(img)
    cv2.imshow("result", result['plot'][::2, ::2])
    print result
    cv2.waitKey(0)
