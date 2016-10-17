# from setting.load import WriteReadJson
from setting.set import SETTING
import pdb
import numpy as np
import cv2
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
from pattern.classify import G652Classify
from pattern.sharp import IsSharp

from SDK.mdpy import GetRawImg


import unittest

class CVTest(unittest.TestCase):

    def setUp(self):
        SETTING({})
        img = GetImage().get("IMG\\GIOF1\\sig")
        self.assertIsInstance(img, np.ndarray)
        self.img = img

    def test_functionall(self):
        img = self.img
        img = ExtractEdge().run(img)
        self.assertIsInstance(img, np.ndarray)
        classify = G652Classify()
        result = classify.find(img)
        self.assertIsInstance(result, dict)
        print 'result', classify.getResult()
        # print 'result ', result

    def test_sharp(self):
        img = self.img
        issharp = IsSharp()
        result = issharp.isSharp(img)
        self.assertIsInstance(result, float)
        print 'sharp: ', result

    def test_sharpDiff(self):
        img = self.img
        issharp = IsSharp()
        result = issharp.isSharpDiff([img,img,img,img,img])
        self.assertIsInstance(result, float)
        print 'sharp: ', result

    def test_mindpySDK(self):

        grt = GetRawImg()
        img = grt.get()
        grt.unInitCamera()
        self.assertIsInstance(img, np.ndarray)
        cv2.imshow('img', img[::8,::8])
        cv2.waitKey(0)


if __name__ == '__main__':
    unittest.main()
    # mc = MergeCircle()
    # mc.flow()
    # SETTING({})
    # img = GetImage().get("IMG\\GIOF1\\sig")
    # img = ExtractEdge().run(img)
    # img = G652Classify().find(img)


