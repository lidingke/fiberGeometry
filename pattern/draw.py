#coding:utf-8
from __future__ import division

from functools import wraps
from time import sleep
import time

import cv2

import matplotlib;

from setting import config

matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import numpy as np

from setting.config import SAVE_TEMP_IMG, OCTAGON_FIBERS, FRAME_CORE
from setting.parameter import SETTING


def decorateOctagon(origin, ellipses, result=False):
    u"""old style 八边形图像注释器，
    将相关标注标注到八边形的图像上，
    比如长短轴、轮廓、纤芯等图像。
    :param origin: 原始图像
    :param ellipses: 轮廓集合
    :param result: 图形参数集合
    :return:
    """
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
    u"""old style 双圈图像注释器，
    将相关标注标注到符合单模光纤内外两圈圆的图像上，
    比如内轮廓、外轮廓等图像。
    :param origin: 原始图像
    :param ellipses: 轮廓集合
    :param result: 图形参数集合
    :return:
    """
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


def duck_type_decorate_list(origin, methods):
    u"""methods是绘图方法和参数的集合，其中一条methods为一个元组，
    格式为(string fun_name, list args, dict kwargs)，
    其中fun_name必须得是cv2中可用的方法，因为该字符串可用来动态的从cv2中获取方法。
    :param origin:原始图片
    :param methods: 绘图方法和参数集合
    :return: 更新后的图片
    """
    for m in methods:
        if len(m) == 2:
            fun_name, args, = m
            kwargs = {}
        elif len(m) == 3:
            fun_name, args, kwargs = m
        else:
            raise ValueError("methods parameter error {} {}", len(m), m)
        fun = getattr(cv2, fun_name)
        fun(origin, *args, **kwargs)
    return origin


def duck_type_decorate(origin, methods):
    u"""根据methods命令行动态的更新标注到图片中，返回该图片。
    :param origin: 原始图片
    :param methods: 方法集合
    :return: 标注后的图片
    """
    assert isinstance(methods, dict)
    for k, v in methods.items():
        duck_type_decorate_list(origin, v)
    return origin


# def decorateMethod(obj):
#     if obj in OCTAGON_FIBERS:
#         return decorateOctagon
#     else:
#         return decorateDoubleCircle


# def drawCoreCircle(img, core, minRange, maxRange):
#     cv2.circle(img, core, int(minRange), (0, 0, 0), 4)
#     x0, y0 = core
#     x1, y1 = x0 + minRange, y0
#     x2, y2 = x0 + maxRange, y0
#     cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
#     x1, y1 = x0, y0 + minRange
#     x2, y2 = x0, y0 + maxRange
#     cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
#     x1, y1 = x0 - minRange, y0
#     x2, y2 = x0 - maxRange, y0
#     cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
#     x1, y1 = x0, y0 - minRange
#     x2, y2 = x0, y0 - maxRange
#     cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
#     return img

def draw_core_cross(core, diffrange, line=10, line_type=5):
    u"""在图片中央绘制一个十字。
    :param core: 中心坐标
    :param diffrange:十字星内圈长度
    :param line:十字星外圈长度
    :param line_type:线宽
    :return:
    """
    x0, y0 = core
    lists = []
    x1, y1 = x0 + line, y0 + diffrange
    x2, y2 = x0 - line, y0 + diffrange
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': line_type})
    lists.append(_)
    x1, y1 = x0 + line, y0 - diffrange
    x2, y2 = x0 - line, y0 - diffrange
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': line_type})
    lists.append(_)
    x1, y1 = x0 + diffrange, y0 + line
    x2, y2 = x0 + diffrange, y0 - line
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': line_type})
    lists.append(_)
    x1, y1 = x0 - diffrange, y0 + line
    x2, y2 = x0 - diffrange, y0 - line
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': line_type})
    lists.append(_)
    return lists


def core_cross_flag(core, minRange, maxRange):
    u"""绘制十字
    :param core:
    :param minRange:
    :param maxRange:
    :return:
    """
    lists = []
    _ = ("circle", (core, int(minRange), (0, 0, 0), 4), {'lineType': 5})
    lists.append(_)
    x0, y0 = core
    x1, y1 = x0 + minRange, y0
    x2, y2 = x0 + maxRange, y0
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': 5})
    lists.append(_)
    x1, y1 = x0, y0 + minRange
    x2, y2 = x0, y0 + maxRange
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': 5})
    lists.append(_)
    x1, y1 = x0 - minRange, y0
    x2, y2 = x0 - maxRange, y0
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': 5})
    lists.append(_)
    x1, y1 = x0, y0 - minRange
    x2, y2 = x0, y0 - maxRange
    _ = ("line", ((x1, y1), (x2, y2), (255, 255, 255), 4,), {'lineType': 5})
    lists.append(_)
    return lists


def output_axies_plot_to_dir(core, img, dir_):
    u"""保存坐标图像到路径
    :param core:
    :param img:
    :param dir_:
    :return:
    """
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
    plt.savefig(dir_)


def output_axies_plot_to_matplot(core, img):
    u"""绘制图像到坐标轴
    :param core:
    :param img:
    :return:
    """
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
    u"""
    一个缓存图片处理中间结果的装饰器，
    缓存结果后放在这该目录下tests\\data\\temp.png
    :param fun:
    :return:
    """
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
