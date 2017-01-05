from setting.orderset import SETTING
SETTING("MindVision500","20X","octagon","centerImg")
from pattern.octagon import ClassOctagon
from pattern.octagon import ClassCore
from pattern.pickoctagon import PickOctagon
from pattern.edge import ExtractEdge
from pattern.classify import OctagonClassify as Classify
import pytest
import cv2
from util.loadimg import edge2img, yieldImg
from pattern.getimg import GetImage, randomBin
import numpy as np
from pattern.edge import EdgeFuncs
import pdb

# @pytest.mark.parametrize(
#     'dir_',(
#         'IMG\\IMG00001.BMP',
#     ))
# def test_proccess1(dir_):
#     img = GetImage().get(dir_)
#     img = ExtractEdge().run(img)
#     # cv2.imshow('img',img[::4,::4])
#     # cv2.waitKey()
#     core, clad = PickOctagon().pick(img)
#     result = ClassOctagon().run(clad)
#     corecore, long, short = result['corePoint'], result['longAxisLen'], result['shortAxisLen']
#     print corecore, long, short
#     assert long > short
#     assert long > 600 and long < 800
#     assert short > 600 and short < 800
#
#     result = ClassCore().run(core)
#     coreclad, long, short = result['corePoint'], result['longAxisLen'], result['shortAxisLen']
#     print coreclad, long, short
#     assert long > short
#     assert long > 55 and long < 90
#     assert short > 55 and short < 90

def test_big_noise():
    img = randomBin("tests\\data\\bignoise\\")
    # img = cv2.medianBlur(img, 9)
    cv2.imshow('img',img[::4,::4])
    cv2.waitKey()
    classify = Classify()
    coreimg, cladimg = classify._difcore(img)
    core = ClassCore().run(coreimg)
    clad = ClassOctagon().run(cladimg)
    # cv2.imshow('clad', core['plot'][::4,::4])
    # cv2.waitKey()
    cv2.imshow('clad', clad['plot'][::4,::4])
    cv2.waitKey()
    # cv2.imshow('coreimg',coreimg[::4,::4])
    # cv2.waitKey()
    # cv2.imshow('cladimg',cladimg[::4,::4])
    # cv2.waitKey()
    # result = classify.getResult()



def test_dynamic_img():
    img = np.fromfile("tests\\data\\dynamicimg1.bin", dtype= "uint8")
    # pdb.set_trace()
    img.shape = (1944, 2592)
    # cv2.imshow('img',img[::4,::4])
    # cv2.waitKey()
    # get = PickOctagon()._findCore(img)
    core, clad = PickOctagon().pick(img)
    # cv2.imshow('core',core[::4,::4])
    # cv2.waitKey()
    # cv2.imshow('clad',clad[::4,::4])
    # cv2.waitKey()
    result = ClassOctagon().run(clad)
    corecore, long, short = result['corePoint'], result['longAxisLen'], result['shortAxisLen']
    print corecore, long, short
    result = ClassCore().run(core)
    coreclad, long, short = result['corePoint'], result['longAxisLen'], result['shortAxisLen']
    print coreclad, long, short

def test_main():
    dir_ = "IMG\\octagon\\new500\\mid.BMP"
    img = GetImage().get(dir_)
    img = ExtractEdge().run(img)
    # cv2.imshow('img',img[::4,::4])
    # cv2.waitKey()
    core, clad = PickOctagon().pick(img)
    # cv2.imshow('core',core[::4,::4])
    # cv2.waitKey()
    # cv2.imshow('clad',clad[::4,::4])
    # cv2.waitKey()
    result = ClassOctagon().run(clad)
    # cv2.imshow('ocplot',result['plot'][::4,::4])
    # cv2.waitKey()
    corecore, long, short = result['corePoint'], result['longAxisLen'], result['shortAxisLen']
    print corecore, long, short
    # cv2.imshow('coplot',result['plot'][::4,::4])
    # cv2.waitKey()
    result = ClassCore().run(core)
    coreclad, long, short = result['corePoint'], result['longAxisLen'], result['shortAxisLen']
    print coreclad, long, short
    # cv2.imshow('result', result['plot'][::4, ::4])
    # cv2.waitKey()

if __name__ == "__main__":
    test_big_noise()
    # test_main()