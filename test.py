# from setting.load import WriteReadJson
from setting.set import SETTING
import pdb
import numpy as np
from pattern.getimg import GetImage
from pattern.edge import ExtractEdge
from pattern.classify import G652Classify

import unittest

class CVTest(unittest.TestCase):


    def setUp(self):
        SETTING({})

    def test_functionall(self):
        img = GetImage().get("IMG\\GIOF1\\sig")
        self.assertIsInstance(img, np.ndarray)
        img = ExtractEdge().run(img)
        self.assertIsInstance(img, np.ndarray)
        classify = G652Classify()
        result = classify.find(img)
        self.assertIsInstance(result, dict)
        print 'result', classify.getResult()
        # print 'result ', result


if __name__ == '__main__':
    unittest.main()
    # mc = MergeCircle()
    # mc.flow()
    # SETTING({})
    # img = GetImage().get("IMG\\GIOF1\\sig")
    # img = ExtractEdge().run(img)
    # img = G652Classify().find(img)


