import cv2

from pattern.adaptivefilter import adaptive_filter_by_median
from pattern.classify import PolyClassify, classifyObject
from util.getimg import get_img
from pattern.sharp import corner_noise
import logging
#
from setting import config


def ttest_adaptive_filter():
    config.SAVE_TEMP_IMG = True

    logging.basicConfig(level=logging.INFO)
    img = get_img("IMG\\10125\\dirty\\1.BMP")
    # print "origin noise", corner_noise(img)
    # cv2.imshow("img",img[::4,::4,0])
    # cv2.waitKey()
    img = adaptive_filter_by_median(img)
    # print "after noise", corner_noise(img)
    cv2.imshow("img",img[::4,::4,0])
    cv2.waitKey()

def test_adaptive_filter_on_classify():
    img = get_img("IMG\\10125\\dirty\\1.BMP")
    logger = logging.getLogger(__name__)

    r = classifyObject("10/130(oc)").find(img)