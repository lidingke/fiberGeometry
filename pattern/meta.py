# identify algorithm flow:
# get image
# extract edge
# extract contours
# fit ellipese
# aimed optimizing
from setting.orderset import SETTING
from util.toolkit import cv2CircleIndex, Cv2ImShow, Cv2ImSave, DynamicPick


class CV2MethodSet(object):
    """docstring for CV2MethodSet"""
    def __init__(self,):
        """ init """
        super(CV2MethodSet, self).__init__()
        self.Show = Cv2ImShow()
        self.Save = Cv2ImSave()
        self.DPick = DynamicPick()
        self.CircleIndex = cv2CircleIndex()
        self.SET = SETTING()









