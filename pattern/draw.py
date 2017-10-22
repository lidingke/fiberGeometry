from __future__ import division

from functools import wraps
from time import sleep
import time

import cv2

import matplotlib;

matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import numpy as np

from setting.config import SAVE_TEMP_IMG, OCTAGON_FIBERS
from setting.parameter import SETTING


def decorateOctagon(origin, ellipses, result=False):
    if len(origin.shape) < 3:
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    if not (ellipses or result):
        return origin
    result = ellipses['showResult']
    x, y = ellipses['cladResult']['longPlot']
    cv2.line(origin, x, y, (25, 255, 0), 8)
    x, y = ellipses['cladResult']['shortPlot']
    cv2.line(origin, x, y, (25, 200, 0), 8)
    # cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 5, lineType=2)  # (162,183,0)(green, blue, red)
    cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 5, lineType=2)  # 255,102,0#FF6600
    corex, corey = ellipses['core'][0]
    # radius = ellipses['core'][1]
    radius = ellipses['coreResult']['shortAxisLen']
    core = (int(corex + radius * 0.7), int(corey - radius * 0.7))
    coreR = "%4.2f" % result[1]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    corex, corey = ellipses['clad'][0]
    radius = ellipses['cladResult']['shortAxisLen']
    core = (int(corex + radius * 0.5), int(corey - radius * 0.5))
    coreR = "%4.2f" % result[2]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    return origin


def decorateDoubleCircle(origin, ellipses, result=False):
    # print ellipses.keys()
    if len(origin.shape) < 3:
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    result = ellipses['showResult']
    cv2.ellipse(origin, ellipses['clad'], (0, 102, 255), 5, lineType=2)
    # cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 5, lineType=2)  # (162,183,0)(green, blue, red)
    cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 5, lineType=2)  # 255,102,0#FF6600
    corex, corey = ellipses['core'][0]
    # radius = ellipses['core'][1]
    radius = ellipses['coreResult']['shortAxisLen']
    core = (int(corex + radius * 0.7), int(corey - radius * 0.7))
    coreR = "%4.2f" % result[1]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    corex, corey = ellipses['clad'][0]
    radius = ellipses['cladResult']['shortAxisLen']
    core = (int(corex + radius * 0.5), int(corey - radius * 0.5))
    coreR = "%4.2f" % result[2]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    return origin


def oldDecorateImg(origin, ellipses, result=False):
    if len(origin.shape) < 3:
        print 'origin shape', origin.shape
        origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2RGB)
    if not (ellipses or result):
        return origin
    result = ellipses['showResult']
    cv2.ellipse(origin, ellipses['clad'], (131, 210, 253), 5, lineType=2)  # (162,183,0)(green, blue, red)
    cv2.ellipse(origin, ellipses['core'], (0, 102, 255), 5, lineType=2)  # 255,102,0#FF6600
    corex, corey = ellipses['core'][0]
    radius = ellipses['core'][1]
    radius = (radius[0] + radius[1]) / 4
    core = (int(corex + radius * 0.7), int(corey - radius * 0.7))
    coreR = "%4.2f" % result[1]
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (215, 207, 39), thickness=3)
    # clad radius
    corex, corey = ellipses['clad'][0]
    radius = ellipses['clad'][1]
    radius = (radius[0] + radius[1]) / 4
    core = (int(corex + radius * 0.7), int(corey - radius * 0.7))
    coreR = "%4.2f" % result[2]
    # print ('clad', coreR, core)
    cv2.putText(origin, coreR, core,
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=3)
    # corex, corey = result[0], result[1]
    return origin

#
# def DecorateImg(origin, ellipses, result=False):
#     if SETTING().get("fiberType") in ("20400", "G652"):
#         return decorateDoubleCircle(origin, ellipses, result)
#     if isinstance(ellipses, dict):
#         return decorateOctagon(origin, ellipses, result)
#     else:
#         return oldDecorateImg(origin, ellipses, result)
#

def duck_type_decorate(origin,methods):
    for m in methods:
        if len(m) == 2:
            fun_name, args, = m
            kwargs = {}
        elif len(m) == 3:
            fun_name, args, kwargs = m
        else:
            raise ValueError("methods parameter error")
        fun = getattr(cv2,fun_name)
        fun(origin,*args,**kwargs)
    return origin

def decorateMethod(obj):
    if obj in OCTAGON_FIBERS:
        return decorateOctagon
    else:
        return decorateDoubleCircle


def drawCoreCircle(img, core, minRange, maxRange):
    cv2.circle(img, core, int(minRange), (0, 0, 0), 4)
    x0, y0 = core
    x1, y1 = x0 + minRange, y0
    x2, y2 = x0 + maxRange, y0
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    x1, y1 = x0, y0 + minRange
    x2, y2 = x0, y0 + maxRange
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    x1, y1 = x0 - minRange, y0
    x2, y2 = x0 - maxRange, y0
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    x1, y1 = x0, y0 - minRange
    x2, y2 = x0, y0 - maxRange
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    return img




def output_axies_plot_to_dir(core, img, dir_):
    x, y = map(int, core)
    shape = img.shape
    print dir(img)
    print img.dtype
    if len(shape) == 3:
        img = img[::, ::, 1].astype(int) - img[::, ::, 0].astype(int)
    print img.dtype
    horizontal = img[y, ::].tolist()
    vertical = img[::, x].tolist()

    xlist = [h - x for h in xrange(shape[1])]
    ylist = [v - y for v in xrange(shape[0])]

    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax1.plot(xlist, horizontal)
    ax1.set_ylabel('bit')
    ax2 = ax1.twinx()
    ax2.plot(ylist, vertical, 'r')
    ax2.set_ylabel('bit')
    ax2.set_xlabel('pix')
    # plt.show()
    plt.savefig(dir_)


def output_axies_plot_to_matplot(core, img):
    x, y = map(int, core)
    shape = img.shape

    if len(shape) == 3:
        img = img[::, ::, 1].astype(int) - img[::, ::, 0].astype(int)

    horizontal = img[y, ::].tolist()
    vertical = img[::, x].tolist()

    xlist = [h - x for h in xrange(shape[1])]
    ylist = [v - y for v in xrange(shape[0])]
    xhalf = (x, shape[1] - x)
    yhalf = (y, shape[0] - y)

    short_axies_ranges = [abs(x - y) for x, y in zip(xhalf, yhalf)]
    start, end = short_axies_ranges
    if len(xlist) > len(ylist):
        xlist = xlist[start:-end]
        horizontal = horizontal[start:-end]
    else:
        ylist = ylist[start:-end]
        vertical = vertical[start:-end]

    return (xlist, horizontal, ylist, vertical)


def show_temp_imgs(fun):
    wraps(fun)

    def inner(self, *args, **kwargs):
        result = fun(self, *args, **kwargs)
        if not SAVE_TEMP_IMG:
            return result
        imgs = self.temp_imgs
        columns = []
        for temps in imgs:
            column_stack = np.column_stack(temps)
            columns.append(column_stack)

        img = np.row_stack(columns)
        text_parameter = (cv2.FONT_HERSHEY_TRIPLEX, 5, (255, 0, 255), 5, False)
        times = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        cv2.putText(img, times, (100, 2000), *text_parameter)
        cv2.imwrite("tests\\data\\temp.png", img[::8, ::8])
        sleep(1)
        return result

    return inner
