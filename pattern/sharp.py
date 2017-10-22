import collections
import cv2
import numpy as np
import pdb
from pattern.edge import ExtractEdge
# from pattern.meta import CV2MethodSet
from setting.parameter import SETTING
import logging

from util.timing import timing

logger = logging.getLogger(__name__)


class IsSharp(object):
    """docstring for IsSharp"""

    def __init__(self):
        super(IsSharp, self).__init__()
        # self.SET = SETTING()

    def isSharp(self, img):
        # better than isSharpCanny
        # midsize = self._midSize(sizecoup = img.shape)
        # img = img[midsize[0]:midsize[1],midsize[2]:midsize[3]]
        # img = cv2.GaussianBlur(img,(5, 5 ),0)
        img = self.erodeDilate(img)
        # self.Show.show("sharp", img[::4,::4])
        sumGrad2 = (img ** 2).sum()
        normalizationSharp = sumGrad2 * 1000 // img.size
        return normalizationSharp / 1000.0

    def _imgs2gray(self, imgs):
        result = []
        for img in imgs:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            result.append(img)
        return result

    # @timing
    def isSharpDiff(self, imgs):
        if len(imgs[0].shape) == 3:
            imgs = self._imgs2gray(imgs)
        # for i,img in enumerate(imgs):
        #     img.tofile("tests\\data\\imgforsharp{}.bin".format(i))
        imgs = [self._doSharpRange(img) for img in imgs]
        # self._doSharpRange(img)

        imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
        for img in imgs[-3:]:
            img = ExtractEdge().directThr(img)
            # cv2.medianBlur(img, 7)
            imgAllor = cv2.bitwise_or(imgAllor, img)
        imgAllor = cv2.bitwise_not(imgAllor)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        imgAllor = cv2.erode(imgAllor, kernel)
        # self.Show.show('sharp', imgAllor)
        # imgAllor = cv2.medianBlur(imgAllor, 7)
        sumGrad2 = imgAllor.sum()
        normalizationSharp = sumGrad2 ** 2 // imgAllor.size // 100

        return normalizationSharp

    def _doSharpRange(self, img):
        # if hasattr(self.SET, "corepoint") and hasattr(self.SET, "cladRange"):
        if "cladRange" in self.SET:
            corex, corey = self.SET["corepoint"]
            minRange, maxRange = self.SET["cladRange"]
            begin = (corex - maxRange, corey - maxRange)
            end = (corex + maxRange, corey + maxRange)
            return img[begin[0]:end[0]:2, begin[1]:end[1]:2]
        else:
            return img[::5, ::5]

    def erodeDilate(self, img):
        # img = cv2.medianBlur(img, 9)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        erode = cv2.erode(img, kernel)
        dilate = cv2.dilate(img, kernel)
        img = cv2.absdiff(dilate, erode)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)
        return img

    def _midSize(self, sizecoup=(100, 100), rato=0.1):
        x00 = int(sizecoup[0] * rato)
        x01 = int(sizecoup[0] * (1 - rato))
        x10 = int(sizecoup[1] * (rato))
        x11 = int(sizecoup[1] * (1 - rato))
        return (x00, x01, x10, x11)

    def issharpla(self, img):

        if isinstance(img, list):
            img = img[0]
        if isinstance(img, np.ndarray):
            logger.debug("laplacian sharp:{}".format(img.shape))

            sharp = cv2.Laplacian(img, cv2.CV_64F).var()

            return sharp
        else:
            cmd = (str(type(img)), img)
            raise ValueError(cmd)

    def issharplaall(self, img):

        if isinstance(img, list):
            img = img[0]
        if isinstance(img, np.ndarray):
            logger.debug("laplacian sharp:{}".format(img.shape))
            # byimg = ExtractEdge().runMax(img)
            # byimg = cv2.bitwise_not(byimg)
            # sum_ = byimg.sum()
            sharp = cv2.Laplacian(img, cv2.CV_64F).var()
            imgfiltered = cv2.medianBlur(img, 21, )
            roundsharp = cv2.Laplacian(imgfiltered, cv2.CV_64F).var()
            # sharp = sharp / sum_
            print 'all_sharp', roundsharp, sharp
            return sharp, roundsharp
        else:
            cmd = (str(type(img)), img)
            raise ValueError(cmd)


class MaxSharp(object):
    def __init__(self):
        super(MaxSharp, self).__init__()
        self.deque = collections.deque(maxlen=20)

    def isRight(self, sharp):
        sharp = float(sharp)
        self.deque.append(sharp)

        if len(self.deque) < 5:
            return False
        sortque = sorted(list(self.deque))
        if sharp > sortque[-1] * 0.6:
            return True
        else:
            return False


def corner_noise(img, slice_point=300, dimension=0):
    shape = img.shape
    if len(shape) == 3:
        img = img[::, ::, dimension].copy()
    else:
        img = img[::, ::].copy()
    corner00 = img[:slice_point, :slice_point]
    corner01 = img[-slice_point:, :slice_point]
    corner10 = img[:slice_point, -slice_point:]
    corner11 = img[-slice_point:, -slice_point:]
    corners = (corner00, corner01, corner10, corner11)
    laplacians = [cv2.Laplacian(corner, cv2.CV_64F).var() for corner in corners]
    return sum(laplacians)


def black_points(img, slice_point=300, dimension=0):
    """ avoid implicit conversion from np.int64 to int. """
    img = img[::, ::, dimension].copy()
    corner00 = img[:slice_point, :slice_point]
    corner01 = img[-slice_point:, :slice_point]
    corner10 = img[:slice_point, -slice_point:]
    corner11 = img[-slice_point:, -slice_point:]
    # cv2.imshow("img",cv2.bitwise_not(corner11))
    # cv2.waitKey()
    corners = (corner00, corner01, corner10, corner11)
    imgs = [cv2.bitwise_not(corner).sum() // 255 for corner in corners]
    return int(sum(imgs) // 255)

def black_points_not(img, slice_point=300, dimension=0):
    """ avoid implicit conversion from np.int64 to int. """
    img = img[::, ::, dimension].copy()
    corner00 = img[:slice_point, :slice_point]
    corner01 = img[-slice_point:, :slice_point]
    corner10 = img[:slice_point, -slice_point:]
    corner11 = img[-slice_point:, -slice_point:]
    # cv2.imshow("img",cv2.bitwise_not(corner11))
    # cv2.waitKey()
    corners = (corner00, corner01, corner10, corner11)
    # cornersbitwise =
    imgs = [corner.sum() for corner in corners]

    return int(sum(imgs) // 255)#4*slice_point**2 -


def take_white_light_in_core(img, slice_point=800, dimension=2):
    img = img[::, ::, dimension].copy()
    s = slice_point
    core = img[s:-s, s:-s]
    # cv2.imshow("core",core)
    # cv2.waitKey()s
    # print int(core.sum() // 255),core.sum(), core.shape
    # print core.tolist()[::100]
    return int(core.sum() // 255)
