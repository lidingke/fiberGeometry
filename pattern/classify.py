import cv2
import numpy as np
from setting.orderset import SETTING
from pickmethod import PickCircle, PickOctagon, PickHullCircle
# from pattern.meta import CV2MethodSet
from pattern.sizefilter import inner_fill, outer_fill
from pattern.edge import ExtractEdge
from util.filter import MedianLimitFilter, MedianFilter
import logging
logger = logging.getLogger(__name__)

class MetaClassify(object):
    """docstring for MetaClassify"""
    def __init__(self, ):
        super(MetaClassify, self).__init__()
        # self.arg = arg
        self.result = {}
        self.SET = SETTING()
        self.amp_ratio = self.SET.get("ampPixSize", 1)
        if 'thresholdSize' in self.SET.keys():
            self.core_thr_hight = self.SET['thresholdSize'].get("core",175)
        else:
            self.core_thr_hight = 175

        if 'thresholdSize' in self.SET.keys():
            self.clad_thr_hight = self.SET['thresholdSize'].get("clad", 40)
        else:
            self.clad_thr_hight = 175
        self.core_filter_index = self.SET["medianBlur"].get("corefilter", 3)
        self.clad_filter_index = self.SET["medianBlur"].get("cladfilter", 3)



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


# self.medianlimitFilterCore.append(coreMidRadius)
# coreMidRadius = self.medianlimitFilterCore.get()

# cladMidRadius = self.medianlimitFilterClad.append(cladMidRadius)
# cladMidRadius = self.medianlimitFilterClad.get()
# cladMidRadius = (cladRadius[0] + cladRadius[1])
def convent_result(core,clad,amp):
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


    def find(self, img):

        coreimg, cladimg = self._difcore(img)

        coreimg = ExtractEdge().directThr(coreimg,self.core_thr_hight )

        cladimg = ExtractEdge().run(cladimg)
        coreResult = PickCircle().run(coreimg,self.core_filter_index)
        cladResult = PickOctagon().run(cladimg,self.clad_filter_index)
        logger.info('start octagon test {} {}'.format(cladResult.keys(), cladResult['ellipese']))

        return convent_result(coreResult, cladResult, self.amp_ratio)

    # cv2.imshow('core', coreimg[::4, ::4])
    # cv2.waitKey()
    # cv2.imshow('clad', cladimg[::4, ::4])
    # cv2.waitKey()
    # blurindex = self.SET["medianBlur"].get("corefilter", 3)
    # blurindex = self.SET["medianBlur"].get("cladfilter", 3)


    # result = {}
    # result['core'] = coreResult['ellipese']
    # result['coreResult'] = coreResult
    # result['clad'] = cladResult['ellipese']
    # result['cladResult'] = cladResult
    # result['showResult'] = get_show_result(result, self.ampRatio)

    def _difcore(self,img):
        corecore = self.SET["corepoint"]
        minRange, maxRange = self.SET["cladRange"]
        # cv2.imshow("redimg", img[::4,::4,0])
        # cv2.waitKey()
        # cv2.imshow("redimg", img[::4,::4,1])
        # cv2.waitKey()
        # cv2.imshow("redimg", img[::4,::4,2])
        # cv2.waitKey()
        redimg =img[::,::,0].copy()

        redimg = cv2.bitwise_not(redimg)

        cladimg = self._getFilterImgClad(corecore, redimg, minRange, maxRange)
        # print 'get clad img ?'
        # cv2.imshow("clad", cladimg[::4,::4])
        # cv2.waitKey()
        minRange, maxRange = self.SET["coreRange"]
        # coreimg = cv2.bitwise_not(img.copy())
        # coreimg = self._getFilterImgCore(corecore, img[::,::,1], minRange, maxRange)
        # coreimg = self._getFilterImgCoreRange(corecore, img, minRange, maxRange)
        coreimg = img[::,::,1].copy()
        # cv2.imshow("core", img[::4, ::4, 1])
        # cv2.waitKey()
        return coreimg, cladimg

    def _getFilterImg(self, core, origin, minRange, maxRange):
        img = np.ones(origin.shape, dtype='uint8') * 255
        core = [core,1]
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(maxRange), (0, 0, 0), -1)
        cv2.circle(img, (int(core[0][0]), int(core[0][1])), int(minRange), (255, 255, 255), -1)
        # origin = cv2.bitwise_not(origin)
        img = cv2.bitwise_or(img, origin)
        return img

    def _getFilterImgClad(self, core, origin, minRange, maxRange):
        # core = [
        # origin = origin.copy()
        print 'get core inner', (int(core[0]), int(core[1])), int(minRange), origin.shape
        cv2.circle(origin, (int(core[0]), int(core[1])), int(minRange), 255, -1)

        return origin


#Big20400Classify
class DoubleCircleClassify(MetaClassify):
    
    def __init__(self):
        super(DoubleCircleClassify, self).__init__()


    def find(self, img):
        coreimg, cladimg = self._difcore(img)

        coreimg = ExtractEdge().directThr(coreimg,self.core_thr_hight)

        cladimg = ExtractEdge().directThr(cladimg,40)
        coreResult = PickCircle().run(coreimg,self.core_filter_index)
        cladResult = PickHullCircle().run(cladimg,self.clad_filter_index)
        logger.info('amp:{}:{}'.format(self.SET['ampPixSize'], self.SET['fiberType']))

        return convent_result(coreResult, cladResult, self.amp_ratio)

    # else:
    #     coreimg = ExtractEdge().directThr(coreimg)
    # coreimg = ExtractEdge().run(coreimg)
    # if 'thresholdSize' in self.SET.keys():
    #     hight = self.SET['thresholdSize'].get("core")
    # cv2.imshow("clad edge", cladimg[::4,::4])
    # cv2.waitKey()

    # cladimg = cv2.medianBlur(cladimg,11)
    # raise ValueError()
    # if 'thresholdSize' in sets.keys():
    #     hight = sets['thresholdSize'].get("clad",40)
    #
    #     cladimg = ExtractEdge().directThr(cladimg,hight)
    # else:
    #     cladimg = ExtractEdge().directThr(cladimg)
    # cladimg = cv2.bilateralFilter(cladimg, 20, 80, 75)
    # cv2.imshow("cladimg edge", coreimg[::4,::4])
    # cv2.waitKey()
    # blurindex = self.SET["medianBlur"].get("corefilter", 3)

    # # print 'get diff'
    # cladResult = PickCircle().run(cladimg)
    # coreResult = PickHullCircle().run(coreimg)
    # blurindex = self.SET["medianBlur"].get("corefilter", 3)

    # result = {}
    # result['core'] = coreResult['ellipese']
    # result['coreResult'] = coreResult
    # result['clad'] = cladResult['ellipese']
    # result['cladResult'] = cladResult
    # result['showResult'] = get_show_result(result, self.ampRatio)

    def _difcore(self, img):
        corecore = self.SET["corepoint"]
        minRange, maxRange = self.SET["cladRange"]

        redimg =img[::,::,0].copy()

        cladimg = self._getFilterImgClad(corecore, redimg, minRange, maxRange)

        minRange, maxRange = self.SET["coreRange"]

        coreimg = img[::,::,1].copy()

        return coreimg, cladimg

    # coreimg = cv2.bitwise_not(img.copy())
    # coreimg = self._getFilterImgCore(corecore, img[::,::,1], minRange, maxRange)
    # coreimg = self._getFilterImgCoreRange(corecore, img, minRange, maxRange)
    # cv2.imshow("core", img[::4, ::4, 1])
    # cv2.waitKey()
    # print 'get clad img ?'
    # cv2.imshow("clad", cladimg[::4,::4])
    # cv2.waitKey()
    # cv2.imshow("redimg", img[::4,::4,0])
    # cv2.waitKey()
    # cv2.imshow("redimg", img[::4,::4,1])
    # cv2.waitKey()
    # cv2.imshow("redimg", img[::4,::4,2])
    # cv2.waitKey()
    # redimg = cv2.bitwise_not(redimg)


    # def _getFilterImgCoreRange(self, core, origin, minRange, maxRange):
    #     x,y = core
    #     print x,y,x-maxRange,x+maxRange,y-maxRange,y+maxRange
    #     img = origin[x-maxRange:x+maxRange,y-maxRange:y+maxRange,1].copy()
    #     return img
    #
    # def _getFilterImgCore(self, core, origin, minRange, maxRange):
    #     img = np.ones(origin.shape, dtype='uint8') * 255
    #     cv2.circle(img, (int(core[0]), int(core[1])), int(maxRange), (0, 0, 0), -1)
    #     cv2.circle(img, (int(core[0]), int(core[1])), int(minRange), (255, 255, 255), -1)
    #     # origin = cv2.bitwise_not(origin)
    #     img = cv2.bitwise_or(img, origin)
    #     return img


    def _getFilterImgClad(self, core, origin, minRange, maxRange):
        # core = [
        # origin = origin.copy()
        logger.warning('get core inner{}-{}-{}'.format((int(core[0]), int(core[1])), int(minRange), origin.shape))
        cv2.circle(origin, (int(core[0]), int(core[1])), int(minRange), 255, -1)

        return origin

class Capillary(MetaClassify):

        def __init__(self):
            super(Capillary, self).__init__()

            self.diff_radius = self.SET.get("diff_radius", False)
            if not self.diff_radius:
                raise KeyError("no diff_radius")

        def _difcore(self, img):

            coreimg = img[::, ::, 0].copy()
            coreimg = outer_fill(coreimg, radius=self.diff_radius)

            cladimg = img[::, ::, 0].copy()
            cladimg = inner_fill(cladimg, radius=self.diff_radius)
            # cv2.imshow("core", cladimg[::4, ::4])
            # cv2.waitKey()
            return coreimg, cladimg

        def find(self, img):
            # self.img = img

            coreimg, cladimg = self._difcore(img)
            # cv2.imshow("clad edge", cladimg[::4,::4])
            # cv2.waitKey()

            # self.SET = SETTING()
            # if 'thresholdSize' in self.SET.keys():
            #     hight = self.SET['thresholdSize'].get("core")
            coreimg = ExtractEdge().directThr(coreimg, self.core_thr_hight)
            # else:
            #     coreimg = ExtractEdge().directThr(coreimg)
            # coreimg = ExtractEdge().run(coreimg)
            # cladimg = ExtractEdge().run(cladimg)

            # if 'thresholdSize' in self.SET.keys():
            #     hight = self.SET['thresholdSize'].get("clad", 40)
            cladimg = ExtractEdge().directThr(cladimg, self.clad_thr_hight)
            # else:
            #     cladimg = ExtractEdge().directThr(cladimg)
            # cladimg = cv2.bilateralFilter(cladimg, 20, 80, 75)
            # cv2.imshow("cladimg edge", coreimg[::4,::4])
            # cv2.waitKey()

            # blurindex =self.SET["medianBlur"].get("corefilter", 3)
            coreResult = PickHullCircle().run(coreimg,self.core_filter_index)
            cladResult = PickHullCircle().run(cladimg,self.clad_filter_index)
            # print 'amp', self.SET['ampPixSize'], self.SET['fiberType']
            # result ={}
            # result['core'] = coreResult['ellipese']
            # result['coreResult'] = coreResult
            # result['clad'] = cladResult['ellipese']
            # result['cladResult'] = cladResult
            # result['showResult'] = get_show_result(result, self.ampRatio)

            return convent_result(coreResult, cladResult, self.amp_ratio)


G652Classify = DoubleCircleClassify
Big20400Classify = DoubleCircleClassify


def classifyObject(fiberType):
    print 'get fiber type', fiberType
    fiberType =str(fiberType)
    SETTING().keyUpdates(fiberType)
    if fiberType in ["octagon","10/130(oc)"]:
        return OctagonClassify()
    elif fiberType in ["capillary"]:
        print 'return Capillary',
        # return Capillary()
        return Capillary()
    else:
        # import DoubleCircleClassify as Classify
        return DoubleCircleClassify()
    # return Classify()