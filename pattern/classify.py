import cv2
import numpy as np

from pattern.draw import show_temp_imgs
from setting.orderset import SETTING
from pickmethod import PickCircle, PickOctagon, PickHullCircle
from pattern.sizefilter import inner_fill, outer_fill, cover_core_by_circle
from pattern.edge import ExtractEdge
import logging

logger = logging.getLogger(__name__)


class MetaClassify(object):
    def __init__(self, ):
        super(MetaClassify, self).__init__()
        self.result = {}
        self.SET = SETTING()
        self.amp_ratio = self.SET.get("ampPixSize", 1)
        if 'thresholdSize' in self.SET.keys():
            self.core_thr_hight = self.SET['thresholdSize'].get("core", 175)
            self.clad_thr_hight = self.SET['thresholdSize'].get("clad", 40)

        else:
            self.core_thr_hight = 175
            self.clad_thr_hight = 175

        self.core_filter_index = self.SET["medianBlur"].get("corefilter", 3)
        self.clad_filter_index = self.SET["medianBlur"].get("cladfilter", 3)
        meta_logger = "meta_logger-amp:{}-thr:{},{}-filter:{},{}".format(
            self.amp_ratio,
            self.core_thr_hight,
            self.clad_thr_hight,
            self.core_filter_index,
            self.clad_filter_index
        )
        logger.error(meta_logger)

    def _difcore(self, img):
        corecore, core_range, clad_range = self.diff_range

        mincore_range, maxcore_range = core_range
        minclad_range, maxclad_range = clad_range
        diff_radius = (maxcore_range+minclad_range)//2

        redimg = img[::, ::, 0].copy()

        cladimg = cover_core_by_circle(corecore, redimg, diff_radius, 0)

        coreimg = img[::, ::, 1].copy()

        return coreimg, cladimg


    @show_temp_imgs
    def find(self, img):
        diff_core_img, diff_clad_img = self._difcore(img)

        edge_core_img = self._edge_core(diff_core_img, self.core_thr_hight)
        edge_clad_img = self._edge_clad(diff_clad_img)
        core_result = self._pick_core(edge_core_img, self.core_filter_index)
        clad_result = self._pick_clad(edge_clad_img, self.clad_filter_index)
        self.temp_imgs = ((diff_core_img,diff_clad_img),(edge_core_img,edge_clad_img))
        return convent_result(core_result, clad_result, self.amp_ratio)


def get_show_result(result, ampRatio):
    coreResult = result.get('coreResult', False)
    cladResult = result.get('cladResult', False)
    if coreResult and cladResult:
        coreCore = coreResult["corePoint"].tolist()[0]
        cladCore = cladResult["corePoint"].tolist()[0]
        coreRadius = (coreResult["longAxisLen"] + coreResult["shortAxisLen"]) / 2
        cladRadius = (cladResult["longAxisLen"] + cladResult["shortAxisLen"]) / 2
        concentricity = ((coreCore[0] - cladCore[0]) ** 2
                         + (coreCore[1] - cladCore[1]) ** 2) ** 0.5
        concentricity = concentricity * ampRatio
        coreMidRadius = ampRatio * coreRadius
        cladMidRadius = ampRatio * cladRadius

        coreRness = ampRatio * abs(coreResult["longAxisLen"] - coreResult["shortAxisLen"])
        cladRness = ampRatio * abs(cladResult["longAxisLen"] - cladResult["shortAxisLen"])
        return (concentricity, coreMidRadius, cladMidRadius, coreRness, cladRness)
    else:
        print 'error find core or clad'
        return ()


def convent_result(core, clad, amp):
    result = {}
    result['core'] = core['ellipese']
    result['coreResult'] = core
    result['clad'] = clad['ellipese']
    result['cladResult'] = clad
    result['showResult'] = get_show_result(result, amp)
    return result


class OctagonClassify(MetaClassify):
    def __init__(self):
        super(OctagonClassify, self).__init__()
        self.diff_range = (self.SET["corepoint"],
                           self.SET["coreRange"], self.SET["cladRange"])
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickCircle().run
        self._pick_clad = PickOctagon().run


    def _difcore(self, img):
        corecore, core_range, clad_range = self.diff_range

        mincore_range, maxcore_range = core_range
        minclad_range, maxclad_range = clad_range
        diff_radius = (maxcore_range+minclad_range)//2

        redimg = img[::, ::, 0].copy()
        cladimg = cover_core_by_circle(corecore, redimg, diff_radius, 0)

        coreimg = img[::, ::, 1].copy()
        return coreimg, cladimg



class DoubleCircleClassify(MetaClassify):
    def __init__(self):
        super(DoubleCircleClassify, self).__init__()
        self.diff_range = (self.SET["corepoint"],
                           self.SET["cladRange"], self.SET["coreRange"])
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickCircle().run
        self._pick_clad = PickHullCircle().run


class Capillary(MetaClassify):
    def __init__(self):
        super(Capillary, self).__init__()

        self.diff_radius = self.SET.get("diff_radius", False)
        if not self.diff_radius:
            raise KeyError("no diff_radius")
        self._edge_core = ExtractEdge().directThr
        self._edge_clad = ExtractEdge().directThr
        self._pick_core = PickHullCircle().run
        self._pick_clad = PickHullCircle().run

    def _difcore(self, img):
        coreimg = img[::, ::, 0].copy()
        coreimg = outer_fill(coreimg, radius=self.diff_radius)

        cladimg = img[::, ::, 0].copy()
        cladimg = inner_fill(cladimg, radius=self.diff_radius)

        return coreimg, cladimg



G652Classify = DoubleCircleClassify
Big20400Classify = DoubleCircleClassify


def classifyObject(fiberType):
    logger.error('get fiber type{}'.format(fiberType))
    fiberType = str(fiberType)
    SETTING().keyUpdates(fiberType)
    if fiberType in ["octagon", "10/130(oc)", "10/130(oc)"]:
        return OctagonClassify()
    elif fiberType in ["capillary"]:
        return Capillary()
    else:
        return DoubleCircleClassify()
