# coding:utf-8
import cv2
import numpy as np
import time

from setting import config
from setting.config import OCTAGON_FIBERS, CAPILLARY, THIN_FIBERS
from pattern.draw import show_temp_imgs, draw_core_cross
from pattern.sharp import corner_noise
from setting.parameter import ClassifyParameter
from picker import PickHullCircle, PickPoly, PickCircle
from pattern.coverimg import outer_fill, cover_core_by_circle, inner_fill_by_value, cover_core_by_circle_auto_value, \
    out_fill_by_white_circle
from pattern.edge import ExtractEdge
import logging

from util.observer import PyTypeSignal
from util.timing import timing

logger = logging.getLogger(__name__)


class MetaClassify(object):
    u"""
    图像分类用的抽象类/基类，其他的子类需要继承该基类，
    重写相应的方法。
    """

    def __init__(self, fiberType, ):
        u"""
        :param fiberType:光纤类型
        引入全局配置sets，在init函数中配置好所有外部引入的属性和方法，
        用self传递到其他函数中。
        """
        super(MetaClassify, self).__init__()
        self.result = {}
        self.sets = ClassifyParameter()
        self.sets.update_by_key(fiberType)
        self.amp_ratio = self.sets.get("ampPixSize", 1)
        if 'thresholdSize' in self.sets.keys():
            self.core_thr_hight = self.sets['thresholdSize'].get("core", 175)
            self.clad_thr_hight = self.sets['thresholdSize'].get("clad", 175)
        else:
            self.core_thr_hight = 175
            self.clad_thr_hight = 175

        self.core_filter_index = self.sets["medianBlur"].get("corefilter", 3)
        self.clad_filter_index = self.sets["medianBlur"].get("cladfilter", 3)
        meta_logger = "meta_logger-amp:{:0.4f}-thr:{},{}-filter:{},{}".format(
            self.amp_ratio,
            self.core_thr_hight,
            self.clad_thr_hight,
            self.core_filter_index,
            self.clad_filter_index
        )
        logger.error(meta_logger)
        self._cover_core_by_circle = cover_core_by_circle

    def _difcore(self, img):
        u"""
        :param img:
        :return:
        将内外两个圆划分开。
        """
        corecore, core_range, clad_range = self.diff_range
        mincore_range, maxcore_range = core_range
        minclad_range, maxclad_range = clad_range
        diff_radius = (maxcore_range + minclad_range) // 2

        redimg = img[::, ::, 0].copy()

        cladimg = self._cover_core_by_circle(corecore, redimg, diff_radius, 0)

        coreimg = img[::, ::, 1].copy()

        return coreimg, cladimg

    # @timing
    @show_temp_imgs
    def find(self, img, amp_ratio=False):
        u"""
        :param img:
        :param amp_ratio:放大倍率
        :return:
        1、分离纤芯和包层。
        2、获取边界。
        3、椭圆拟合出结果。
        4、缓存中间结果供调试。
        5、合并结果。
        """
        diff_core_img, diff_clad_img = self._difcore(img)
        edge_core_img = self._edge_core(diff_core_img, self.core_thr_hight)
        edge_clad_img = self._edge_clad(diff_clad_img, self.clad_thr_hight)
        core_result = self._pick_core(edge_core_img, self.core_filter_index)
        # clad_result = self._pick_clad(edge_clad_img, self.filter_index(img))
        clad_result = self._pick_clad(edge_clad_img, self.clad_filter_index)
        logger.warning(
            "thr,filter {} {}, {} {}".format(self.core_thr_hight, self.clad_thr_hight,
                                             self.core_filter_index, self.clad_filter_index))
        self.temp_imgs = ((diff_core_img, diff_clad_img), (edge_core_img, edge_clad_img))
        if amp_ratio:
            self.amp_ratio = amp_ratio
        return self.convent_result(core_result, clad_result, self.amp_ratio)

    def get_show_result(self, core, clad, ampRatio):
        u"""
        :param core: 纤芯结果。
        :param clad: 包层结果。
        :param ampRatio: 放大倍率。
        :return:
        对结果进行合并和转换，得到可供显示的结果
        """
        coreRadius = (core["longAxisLen"] + core["shortAxisLen"]) / 2
        cladRadius = (clad["longAxisLen"] + clad["shortAxisLen"]) / 2

        coreCore = core["corePoint"].tolist()[0]
        cladCore = clad["corePoint"].tolist()[0]
        concentricity = ((coreCore[0] - cladCore[0]) ** 2
                         + (coreCore[1] - cladCore[1]) ** 2) ** 0.5
        coreMidRadius = ampRatio * coreRadius
        cladMidRadius = ampRatio * cladRadius
        concentricity = ampRatio * concentricity

        coreRness = ampRatio * abs(core["longAxisLen"] - core["shortAxisLen"])
        cladRness = ampRatio * abs(clad["longAxisLen"] - clad["shortAxisLen"])
        return (concentricity, coreMidRadius, cladMidRadius, coreRness, cladRness)

    def convent_result(self, core, clad, amp):
        u"""
        :param core:
        :param clad:
        :param amp:
        :return:
        合并/转换结果
        """
        corecore = core['corePoint'][0]
        output_result = {}
        output_result['showResult'] = self.get_show_result(core, clad, amp)
        output_result['plots'] = {"core": core['plots'], "clad": clad['plots']}
        output_result["corecore"] = corecore
        return output_result


# class OctagonClassify(MetaClassify):
#     def __init__(self,fiberType):
#         super(OctagonClassify, self).__init__(fiberType)
#         self.diff_range = (self.sets["corepoint"],
#                            self.sets["coreRange"], self.sets["cladRange"])
#         self._edge_core = ExtractEdge().directThr
#         self._edge_clad = ExtractEdge().directThr
#         self._pick_core = PickCircle().run
#         self._pick_clad = PickOctagon().run
#
#
#     def _difcore(self, img):
#         corecore, core_range, clad_range = self.diff_range
#
#         mincore_range, maxcore_range = core_range
#         minclad_range, maxclad_range = clad_range
#         diff_radius = (maxcore_range+minclad_range)//2
#
#         redimg = img[::, ::, 0].copy()
#         cladimg = cover_core_by_circle_auto_value(corecore, redimg, diff_radius)
#
#         coreimg = img[::, ::, 1].copy()
#         return coreimg, cladimg

class PolyClassify(MetaClassify):
    u"""多边形识别子类"""

    def __init__(self, fiberType, ploy=8):
        u"""
        :param fiberType:光纤类型。
        :param ploy: 多边形边数。
        引入一个识别多边形的外部变量。
        """
        super(PolyClassify, self).__init__(fiberType)
        self.diff_range = (self.sets["corepoint"],
                           self.sets["coreRange"], self.sets["cladRange"])
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickCircle().run
        self._pick_clad = PickPoly(ploy).run
        self._cover_core_by_circle_auto_value = cover_core_by_circle_auto_value

    def _difcore(self, img):
        corecore, core_range, clad_range = self.diff_range

        mincore_range, maxcore_range = core_range
        minclad_range, maxclad_range = clad_range
        diff_radius = (maxcore_range + minclad_range) // 2

        redimg = img[::, ::, 0].copy()
        cladimg = self._cover_core_by_circle_auto_value(corecore, redimg, diff_radius)

        coreimg = img[::, ::, 1].copy()

        # cv2.imshow('r',redimg[::4,::4])
        # cv2.waitKey()
        # cv2.imshow('g',coreimg[::4,::4])
        # cv2.waitKey()
        # cv2.imshow('b',img[::, ::, 2].copy()[::4,::4])
        # cv2.waitKey()

        return coreimg, cladimg


class DoubleCircleClassify(MetaClassify):
    def __init__(self, fiberType):
        super(DoubleCircleClassify, self).__init__(fiberType)
        self.diff_range = (self.sets["corepoint"],
                           self.sets["coreRange"], self.sets["cladRange"])
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickCircle().run
        self._pick_clad = PickHullCircle().run
        self._out_fill_by_white_circle = out_fill_by_white_circle

    def _difcore(self, img):
        corecore, core_range, clad_range = self.diff_range
        mincore_range, maxcore_range = core_range
        minclad_range, maxclad_range = clad_range
        diff_radius = maxcore_range + minclad_range // 4
        outer_radius = int(maxclad_range * 1.2)
        logger.warning("dif_core para: {},{}\n{}".format(diff_radius, outer_radius, self.diff_range))

        redimg = img[::, ::, 0].copy()

        cladimg = self._cover_core_by_circle(corecore, redimg, diff_radius, 0)
        cladimg = self._out_fill_by_white_circle(cladimg, corecore, outer_radius)

        coreimg = img[::, ::, 1].copy()

        return coreimg, cladimg


class CapillaryClassify(MetaClassify):
    u"""
    毛细管识别，毛细管需要指定一个半径去区分内外孔径。
    """

    def __init__(self, fiberType):
        super(CapillaryClassify, self).__init__(fiberType)
        self.diff_radius = self.sets.get("diff_radius", False)
        if not self.diff_radius:
            raise KeyError("no diff_radius")
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickHullCircle().run
        self._pick_clad = PickHullCircle().run
        self._outer_fill = outer_fill
        self._inner_fill_by_value = inner_fill_by_value
        self.frame_core = config.FRAME_CORE
        self.draw_core_cross = draw_core_cross
        # self.emit_return_plot = PyTypeSignal()

    def _difcore(self, img):
        coreimg = img[::, ::, 0].copy()
        coreimg = self._outer_fill(coreimg, radius=self.diff_radius)

        cladimg = img[::, ::, 0].copy()
        cladimg = self._inner_fill_by_value(cladimg, radius=self.diff_radius)

        return coreimg, cladimg

    def change_diff_radius(self, value):
        self.diff_radius = value

    #
    #     def return_plot_fun(value):
    #         plots = draw_core_cross(self.frame_core,self.diff_radius)
    #         self.emit_return_plot.emit(plots)
    #     self.cap_diffrange.valueChanged.connect(return_plot_fun)

    def get_show_result(self, core, clad, ampRatio):
        # print "get cap result"
        coreRadius = (core["longAxisLen"] + core["shortAxisLen"]) / 2
        cladRadius = (clad["longAxisLen"] + clad["shortAxisLen"]) / 2

        coreCore = core["corePoint"].tolist()[0]
        cladCore = clad["corePoint"].tolist()[0]
        concentricity = ((coreCore[0] - cladCore[0]) ** 2
                         + (coreCore[1] - cladCore[1]) ** 2) ** 0.5
        coreMidRadius = ampRatio * coreRadius
        cladMidRadius = ampRatio * cladRadius
        concentricity = ampRatio * concentricity

        coreRness = abs(core["longAxisLen"] - core["shortAxisLen"]) / coreRadius
        cladRness = abs(clad["longAxisLen"] - clad["shortAxisLen"]) / cladRadius
        return (concentricity, coreMidRadius, cladMidRadius, coreRness, cladRness)

    def convent_result(self, core, clad, amp):
        output_result = super(CapillaryClassify, self).convent_result(core, clad, amp)
        output_result['plots'].update({
            "diff_range": self.draw_core_cross(self.frame_core, self.diff_radius)
        })
        return output_result


class ThinClassify(MetaClassify):
    u"""
    大芯径光纤识别，大芯径光纤边缘很薄，需要小心选取分界半径。
    """

    def __init__(self, fiberType):
        super(ThinClassify, self).__init__(fiberType)
        self.diff_range = (self.sets["corepoint"],
                           self.sets["coreRange"], self.sets["cladRange"])
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickCircle().run
        self._pick_clad = PickHullCircle().run

        self._cover_core_by_circle = cover_core_by_circle
        self._outer_fill = outer_fill

    def _difcore(self, img):
        corecore, core_range, clad_range = self.diff_range
        mincore_range, maxcore_range = core_range
        minclad_range, maxclad_range = clad_range
        diff_radius = (maxcore_range + minclad_range) // 2
        outer_radius = int(maxclad_range * 1.2)
        logger.warning("dif_core para: {},{}\n{}".format(diff_radius, outer_radius, self.diff_range))

        redimg = img[::, ::, 0].copy()

        cladimg = self._cover_core_by_circle(corecore, redimg, diff_radius, 0)
        # cladimg = self._outer_fill(redimg, radius=outer_radius, value=255)

        coreimg = img[::, ::, 1].copy()

        return coreimg, cladimg


# G652Classify = DoubleCircleClassify
# Big20400Classify = DoubleCircleClassify


def classifyObject(fiberType):
    fiberType = str(fiberType)
    # SETTING().update_by_key(fiberType)
    # SETTING()["fiberType"] = fiberType
    if fiberType in OCTAGON_FIBERS:
        # classify =  OctagonClassify(fiberType)
        classify = PolyClassify(fiberType)
    elif fiberType in CAPILLARY:
        classify = CapillaryClassify(fiberType)
    elif fiberType in THIN_FIBERS:
        classify = ThinClassify(fiberType)
    else:
        classify = DoubleCircleClassify(fiberType)
    logger.error('get fiber type: {} - {}'.format(fiberType, classify))
    return classify
