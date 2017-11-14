# encoding:utf-8
import cv2
import numpy as np
from setting.parameter import SETTING
import logging

logger = logging.getLogger(__name__)
core_point = SETTING()['corepoint']


def inner_fill_by_value(img, core=core_point, radius=0, value=0):
    """ (x-x0)^2 +(y-y0)^2 = R^2, ±(R - (y-y0)^2)**0.5 +x0"""
    if not radius: return img
    sharp = img.shape
    logger.info("sharp:{},corecore:{}".format(sharp, core))
    ymax = sharp[0]
    xmax = sharp[1]
    y0, x0 = core
    yranges = xrange(y0 - radius, y0 + radius)
    for y in yranges:
        x00, x01 = -(radius ** 2 - (y - y0) ** 2) ** 0.5 + x0, (radius ** 2 - (y - y0) ** 2) ** 0.5 + x0
        x00, x01 = int(x00), int(x01)
        if x00 < x01:
            img[x00:x01, y].fill(value)
    return img

def inner_fill_auto_value(img, core=core_point, radius=0, value=0):
    """ (x-x0)^2 +(y-y0)^2 = R^2 ±(R - (y-y0)^2)**0.5 +x0"""
    if not radius: return img
    sharp = img.shape
    logger.info("sharp:{},corecore:{}".format(sharp, core))

    ymax = sharp[0]
    xmax = sharp[1]
    y0, x0 = core
    yranges = xrange(y0 - radius, y0 + radius)
    for y in yranges:
        x00, x01 = -(radius ** 2 - (y - y0) ** 2) ** 0.5 + x0, (radius ** 2 - (y - y0) ** 2) ** 0.5 + x0
        x00, x01 = int(x00), int(x01)
        if x00 < x01:
            img[x00:x01, y].fill(value)
    return img


def outer_fill(img, core=core_point, radius=0, value=0):
    if not radius:
        return img
    sharp = img.shape
    logger.info("sharp:{},corecore:{}".format(sharp, core))
    ymax = sharp[1]
    xmax = sharp[0]
    y0, x0 = core
    yranges = xrange(y0 - radius, y0 + radius)

    for y in yranges:
        x00, x01 = -(radius ** 2 - (y - y0) ** 2) ** 0.5 + x0, (radius ** 2 - (y - y0) ** 2) ** 0.5 + x0
        x00, x01 = int(x00), int(x01)
        if x00 < x01:
            img[0:x00, y].fill(value)
            img[x01:xmax, y].fill(value)
        else:
            img[:, y].fill(value)
            pass
    if ymax == radius * 2:
        return img
    img[:, :(y0 - radius)].fill(value)
    img[:, (y0 + radius):].fill(value)

    # (x-x0)^2 +(y-y0)^2 = R^2
    # ±(R - (y-y0)^2)**0.5 +x0

    return img

def out_fill_by_white_circle(img,core,radius):
    img = img.copy()
    shape = img.shape
    merge_img = np.ones(shape,dtype="uint8")*255
    cv2.circle(merge_img,tuple(core),radius,0,-1)
    # cv2.imshow("m",merge_img[::4,::4])
    # cv2.waitKey()
    img = cv2.bitwise_or(img,merge_img)
    # cv2.imshow("c",img[::4,::4])
    # cv2.waitKey()
    return img




def cover_core_by_circle(core, img, radius, value):
    core = map(int, core)
    cv2.circle(img, tuple(core), radius, value, -1)
    return img


def cover_core_by_circle_auto_value(core, img, radius, value=False):
    core = map(int, core)
    y, x = core
    radius2 = radius * 1.414 // 2
    radius2 = int(radius2)
    if not value:
        points = [(x - radius, y), (x + radius, y),
                  (x, y - radius), (x, y + radius),
                  (x - radius2, y - radius2), (x + radius2, y + radius2),
                  (x + radius2, y - radius), (x - radius2, y + radius2)]
        values = [img[point[0], point[1]] for point in points]
        values.sort()
        value = sum(values[1:-1]) // 6
    cv2.circle(img, tuple(core), radius, value, -1)
    return img


def sliceImg(img, core, slice, split = 1):
    corex, corey = core
    maxRange = slice
    begin = (corex - maxRange, corey - maxRange)
    end = (corex + maxRange, corey + maxRange)
    if len(img.shape) == 2:
        return img[begin[0]:end[0]:split, begin[1]:end[1]:split]
    else:
        return img[begin[0]:end[0]:split, begin[1]:end[1]:split]