# encoding:utf-8
import cv2

from setting.orderset import SETTING

core_point = SETTING()['corepoint']


def inner_fill(img, core=core_point, radius=0, value=0):
    if not radius: return img
    sharp = img.shape
    print sharp, core
    ymax = sharp[0]
    xmax = sharp[1]
    y0, x0 = core
    yranges = xrange(y0 - radius, y0 + radius)
    # xranges = []
    for y in yranges:
        x00, x01 = -(radius ** 2 - (y - y0) ** 2) ** 0.5 + x0, (radius ** 2 - (y - y0) ** 2) ** 0.5 + x0
        x00, x01 = int(x00), int(x01)
        # xranges.append((x00, x01))
        # print 'fill',y , x00, x01
        if x00 < x01:
            img[x00:x01, y].fill(value)

    # (x-x0)^2 +(y-y0)^2 = R^2
    # ±(R - (y-y0)^2)**0.5 +x0

    return img


def outer_fill(img, core=core_point, radius=0, value=0):
    if not radius:
        return img
    sharp = img.shape
    print sharp, core
    ymax = sharp[0]
    xmax = sharp[1]
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


def cover_core_by_circle(core, img, radius, value):
    core = map(int, core)
    cv2.circle(img, tuple(core), radius, value, -1)
    return img
