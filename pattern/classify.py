import cv2
import numpy as np
from setting.orderset import SETTING
from pickmethod import PickCircle, PickOctagon
from pattern.meta import CV2MethodSet
from pattern.sizefilter import inner_fill, outer_fill
from pattern.edge import ExtractEdge
from util.filter import MedianLimitFilter, MedianFilter

class MetaClassify(CV2MethodSet):
    """docstring for MetaClassify"""
    def __init__(self, ):
        super(MetaClassify, self).__init__()
        # self.arg = arg
        self.result = {}
        self.SET = SETTING()
        self.ampRatio = self.SET.get("ampPixSize", 1)
        self.medianlimitFilterCore = MedianFilter()
        self.medianlimitFilterClad = MedianFilter()

    # @timing
    def find(self, img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        self._filter(contours, hierarchys)
        return self.result

    def _filter(self, contours, hierarchys):
        pass

    def getResult(self):
        coreResult = self.result.get('coreResult', False)
        cladResult = self.result.get('cladResult', False)
        if coreResult and cladResult:
            coreCore = coreResult["corePoint"].tolist()[0]
            cladCore = cladResult["corePoint"].tolist()[0]
            coreRadius = (coreResult["longAxisLen"] + coreResult["shortAxisLen"])/2
            cladRadius = (cladResult["longAxisLen"] + cladResult["shortAxisLen"])/2
            concentricity = ((coreCore[0] - cladCore[0]) ** 2
                             + (coreCore[1] - cladCore[1]) ** 2) ** 0.5
            concentricity = concentricity * self.ampRatio
            coreMidRadius = self.ampRatio * coreRadius
            # self.medianlimitFilterCore.append(coreMidRadius)
            # coreMidRadius = self.medianlimitFilterCore.get()
            cladMidRadius = self.ampRatio * cladRadius
            # cladMidRadius = self.medianlimitFilterClad.append(cladMidRadius)
            # cladMidRadius = self.medianlimitFilterClad.get()
            # cladMidRadius = (cladRadius[0] + cladRadius[1])
            coreRness = self.ampRatio * abs(coreResult["longAxisLen"] - coreResult["shortAxisLen"])
            cladRness = self.ampRatio * abs(cladResult["longAxisLen"] - cladResult["shortAxisLen"])

            return (concentricity, coreMidRadius, cladMidRadius, coreRness, cladRness)
        else:
            print 'error find core or clad'
            return ()


class OctagonClassify(MetaClassify):

    def __init__(self):
        super(OctagonClassify, self).__init__()

        # self.ampRatio = 1

    def find(self, img):
        self.img = img

        coreimg, cladimg = self._difcore(img)


        sets = SETTING()
        if 'thresholdSize' in sets.keys():
            hight = sets['thresholdSize'].get("core")

            coreimg = ExtractEdge().directThr(coreimg,hight)

        else:
            coreimg = ExtractEdge().directThr(coreimg)
        # coreimg = ExtractEdge().run(coreimg)
        cladimg = ExtractEdge().run(cladimg)
        # cv2.imshow('core', coreimg[::4, ::4])
        # cv2.waitKey()
        # cv2.imshow('clad', cladimg[::4, ::4])
        # cv2.waitKey()
        coreResult = PickCircle().run(coreimg)
        cladResult = PickOctagon().run(cladimg)
        print 'start octagon test', cladResult.keys(), cladResult['ellipese']
        self.result['core'] = coreResult['ellipese']
        self.result['coreResult'] = coreResult
        self.result['clad'] = cladResult['ellipese']
        self.result['cladResult'] = cladResult
        self.result['showResult'] = self.getResult()
        return self.result

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

    def find(self, img):
        self.img = img

        coreimg, cladimg = self._difcore(img)
        # cv2.imshow("clad edge", cladimg[::4,::4])
        # cv2.waitKey()
        sets = SETTING()
        if 'thresholdSize' in sets.keys():
            hight = sets['thresholdSize'].get("core")
            coreimg = ExtractEdge().directThr(coreimg,hight)
        else:
            coreimg = ExtractEdge().directThr(coreimg)
        # coreimg = ExtractEdge().run(coreimg)
        cladimg = ExtractEdge().run(cladimg)

        # if 'thresholdSize' in sets.keys():
        #     hight = sets['thresholdSize'].get("clad",40)
        #
        #     cladimg = ExtractEdge().directThr(cladimg,hight)
        # else:
        #     cladimg = ExtractEdge().directThr(cladimg)
        # cladimg = cv2.bilateralFilter(cladimg, 20, 80, 75)
        # cv2.imshow("cladimg edge", cladimg[::4,::4])
        # cv2.waitKey()

        coreResult = PickCircle().run(coreimg)
        # print 'get diff'
        cladResult = PickCircle().run(cladimg)

        print 'amp',self.SET['ampPixSize'], self.SET['fiberType']
        self.result['core'] = coreResult['ellipese']
        self.result['coreResult'] = coreResult
        self.result['clad'] = cladResult['ellipese']
        self.result['cladResult'] = cladResult
        self.result['showResult'] = self.getResult()
        return self.result


    def _difcore(self, img):
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

    def _getFilterImgCoreRange(self, core, origin, minRange, maxRange):
        x,y = core
        print x,y,x-maxRange,x+maxRange,y-maxRange,y+maxRange
        img = origin[x-maxRange:x+maxRange,y-maxRange:y+maxRange,1].copy()
        return img

    def _getFilterImgCore(self, core, origin, minRange, maxRange):
        img = np.ones(origin.shape, dtype='uint8') * 255
        cv2.circle(img, (int(core[0]), int(core[1])), int(maxRange), (0, 0, 0), -1)
        cv2.circle(img, (int(core[0]), int(core[1])), int(minRange), (255, 255, 255), -1)
        # origin = cv2.bitwise_not(origin)
        img = cv2.bitwise_or(img, origin)
        return img


    def _getFilterImgClad(self, core, origin, minRange, maxRange):
        # core = [
        # origin = origin.copy()
        print 'get core inner', (int(core[0]), int(core[1])), int(minRange), origin.shape
        cv2.circle(origin, (int(core[0]), int(core[1])), int(minRange), 255, -1)

        return origin


class Capillary(DoubleCircleClassify):

    def __init__(self):
        super(Capillary, self).__init__()


    def _difcore(self, img):

        diff_radius = self.SET.get("diff_radius",False)
        if not diff_radius:
            raise KeyError("no diff_radius")
        coreimg =img[::,::,0].copy()
        coreimg = outer_fill(coreimg, radius = diff_radius)


        cladimg = img[::,::,0].copy()
        cladimg = inner_fill(cladimg, radius = diff_radius)
        # cv2.imshow("core", cladimg[::4, ::4])
        # cv2.waitKey()
        return coreimg, cladimg

    def find(self, img):
        self.img = img

        coreimg, cladimg = self._difcore(img)
        # cv2.imshow("clad edge", cladimg[::4,::4])
        # cv2.waitKey()
        sets = SETTING()
        if 'thresholdSize' in sets.keys():
            hight = sets['thresholdSize'].get("core")
            coreimg = ExtractEdge().directThr(coreimg,hight)
        else:
            coreimg = ExtractEdge().directThr(coreimg)
        # coreimg = ExtractEdge().run(coreimg)
        # cladimg = ExtractEdge().run(cladimg)

        if 'thresholdSize' in sets.keys():
            hight = sets['thresholdSize'].get("clad",40)

            cladimg = ExtractEdge().directThr(cladimg,hight)
        else:
            cladimg = ExtractEdge().directThr(cladimg)
        # cladimg = cv2.bilateralFilter(cladimg, 20, 80, 75)
        # cv2.imshow("cladimg edge", cladimg[::4,::4])
        # cv2.waitKey()

        coreResult = PickCircle().run(coreimg)
        # print 'get diff'
        cladResult = PickCircle().run(cladimg)

        print 'amp',self.SET['ampPixSize'], self.SET['fiberType']
        self.result['core'] = coreResult['ellipese']
        self.result['coreResult'] = coreResult
        self.result['clad'] = cladResult['ellipese']
        self.result['cladResult'] = cladResult
        self.result['showResult'] = self.getResult()
        return self.result

# class NewG652Classify(Big20400Classify):
#
#     def __init__(self):
#         super(NewG652Classify, self).__init__()

G652Classify = DoubleCircleClassify
Big20400Classify = DoubleCircleClassify


def classifyObject(fiberType):
    print 'get fiber type', fiberType
    if fiberType in ["octagon","10/130(oc)"]:
        return OctagonClassify()
    elif fiberType in ["capillary"]:
        print 'return Capillary',
        return Capillary()
    else:
        # import DoubleCircleClassify as Classify
        return DoubleCircleClassify()
    # return Classify()