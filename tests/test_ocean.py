#coding:utf-8

from SDK.oceanoptics import OceanOpticsTest
import unittest

class OceanTest(unittest.TestCase):

    def setUp(self):
        self.op = OceanOpticsTest()

    def test_GetData(self):
        print self.op.getData(25)


if __name__ == "__main__":
    unittest.main()