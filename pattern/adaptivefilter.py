#coding:utf-8
import cv2
from pattern.sharp import corner_noise
import logging

logger = logging.getLogger(__name__)


def adaptive_filter_by_median(img, blur_range=(11, 27), noise=30, step=4):
    u"""
    :param img:图片
    :param blur_range:滤波参数范围
    :param noise:噪声范围
    :param step:参数步长
    :return:自适应滤波后的图片
    自适应滤波容易影响精度，而且速度慢，需要谨慎使用。
    """
    blur, max_blur = blur_range
    logger.info("range:{},blur:{}".format(blur_range, blur))
    for i in range(10):
        output = cv2.medianBlur(img, blur)
        n = corner_noise(output)
        logger.error("adaptive by noise:{},blur:{}".format(n, blur))

        if n > noise and blur < 27:
            blur = blur + step
            blur = int(blur)
        else:
            return output
