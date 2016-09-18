# from setting.load import WriteReadJson
from setting.set import SETTING
import pdb


class A(object):
    """docstring for A"""
    def __init__(self, ):
        super(A, self).__init__()
        # self.arg = arg
        self.SET = SETTING().getSetting()
        self.SET['ampPixSize'] = 0.088
        SETTING().saveSetting()


class B(object):
    """docstring for B"""
    def __init__(self, ):
        super(B, self).__init__()
        # self.arg = arg
        self.SET = SETTING().getSetting()
        print 'set', self.SET['ampPixSize']
        self.SET['dip'] = '500W'
        SETTING().saveSetting()


class C(object):
    """docstring for B"""
    def __init__(self, ):
        super(C, self).__init__()
        print 'set', SETTING()['ampPixSize'], SETTING()['dip']


if __name__ == '__main__':
    SETTING({'ampFactor':'20X','cameraID':'MindVision'})
    A()
    B()
    C()
