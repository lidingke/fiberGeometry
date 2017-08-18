from __future__ import division

import pdb

import numpy as np
import cv2
from setting.orderset import SETTING


def decorateOctagon(origin, ellipses, result=False):
    # print ellipses.keys()
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
    # core radius
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


def DecorateImg(origin, ellipses, result=False):
    if SETTING().get("fiberType") in ("20400", "G652"):
        return decorateDoubleCircle(origin, ellipses, result)
    if isinstance(ellipses, dict):
        return decorateOctagon(origin, ellipses, result)
    else:
        return oldDecorateImg(origin, ellipses, result)


def decorateMethod(obj):
    if obj in ('octagon',):
        return decorateOctagon
    else:
        return decorateDoubleCircle


def drawCoreCircle(img):
    SET = SETTING()
    corecore = SET.get("corepoint", (1296, 972))
    core = [corecore, 1]
    # print "corecorex, corecorey", corecorex, corecorey
    minRange, maxRange = SET.get("coreRange")
    # cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (255, 255, 255), 4)
    cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (0, 0, 0), 4)
    x0, y0 = corecore
    x1, y1 = x0 + minRange, y0
    x2, y2 = x0 + maxRange, y0
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 4)
    x1, y1 = x0, y0 + minRange
    x2, y2 = x0, y0 + maxRange
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    x1, y1 = x0 - minRange, y0
    x2, y2 = x0 - maxRange, y0
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    x1, y1 = x0, y0 - minRange
    x2, y2 = x0, y0 - maxRange
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
    if SET.get("draw_clad", False):
        minRange, maxRange = SET.get("cladRange")
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), 4)
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), 4)
    return img


import matplotlib;

matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import numpy as np


def output_axies_plot_to_dir(core, img, dir_):
    x, y = map(int, core)
    shape = img.shape
    print dir(img)
    print img.dtype
    if len(shape) == 3:
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = img[::, ::, 1].astype(int) - img[::, ::, 0].astype(int)
    print img.dtype
    horizontal = img[y, ::].tolist()
    vertical = img[::, x].tolist()

    # sub = lambda x,y: x-y
    xlist = [h - x for h in xrange(shape[1])]
    ylist = [v - y for v in xrange(shape[0])]

    # print 'map',map(len,hplots),map(len,vplots)
    # pdb.set_trace()
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

    # sub = lambda x,y: x-y
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
    # pdb.set_trace()

    return (xlist, horizontal, ylist, vertical)
